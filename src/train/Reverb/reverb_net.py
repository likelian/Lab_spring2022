import os
import torch
import torch.nn as nn
import numpy as np
from tqdm import tqdm
import gc


class ReverbNet(nn.Module):
  def __init__(self):
    """Intitalize neural net layers"""
    super(ReverbNet, self).__init__()
    self.conv1 = nn.Conv2d(in_channels=2, out_channels=8, kernel_size=3, stride=1, padding=0)
    self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, stride=1, padding=0)
    self.conv3 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=0)
    self.conv4 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=0)
    self.conv5 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=0)
    
    self.fc1 = nn.Linear(in_features=768, out_features=768)
    self.fc2 = nn.Linear(in_features=768, out_features=10)

    self.batchnorm1 = nn.BatchNorm2d(num_features=8)
    self.batchnorm2 = nn.BatchNorm2d(num_features=16)
    self.batchnorm3 = nn.BatchNorm2d(num_features=32)
    self.batchnorm4 = nn.BatchNorm2d(num_features=64)
    self.batchnorm5 = nn.BatchNorm2d(num_features=128)

    self.relu1 = nn.ReLU()
    self.relu2 = nn.ReLU()
    self.relu3 = nn.ReLU()
    self.relu4 = nn.ReLU()
    self.relu5 = nn.ReLU()

    self.tanh1 = nn.Tanh()

    self.max_pool2d1 = nn.MaxPool2d(kernel_size=2)
    self.max_pool2d2 = nn.MaxPool2d(kernel_size=2)
    self.max_pool2d3 = nn.MaxPool2d(kernel_size=2)
    self.max_pool2d4 = nn.MaxPool2d(kernel_size=2)
    self.max_pool2d5 = nn.MaxPool2d(kernel_size=2)

    self.dropout = nn.Dropout(p=0.3, inplace=False)


  def forward(self, x):
    # Conv layer 1.
    x = self.conv1(x)
    x = self.batchnorm1(x)
    x = self.relu1(x)
    x = self.max_pool2d1(x)

    # Conv layer 2.
    x = self.conv2(x)
    x = self.batchnorm2(x)
    x = self.relu2(x)
    x = self.max_pool2d2(x)

    # Conv layer 3.
    x = self.conv3(x)
    x = self.batchnorm3(x)
    x = self.relu3(x)
    x = self.max_pool2d3(x)

    # Conv layer 4.
    x = self.conv4(x)
    x = self.batchnorm4(x)
    x = self.relu4(x)
    x = self.max_pool2d4(x)

    # Conv layer 5.
    #x = self.conv5(x)
    #x = self.batchnorm5(x)
    #x = self.relu5(x)
    #x = self.max_pool2d5(x)

    # Fully connected layer 1.
    x = torch.flatten(x, 1)
    x = self.dropout(x)
    #x = self.fc1(x)
    #x = self.tanh1(x)
    x = self.fc2(x)
    x = torch.squeeze(x)
    
    return x


def normalize(param):
  """
  intput: torch tensor
  return: torch tensor
  """
  param_T = param.T

  param_T[0] /= 30. #room_size [1, 30]
  param_T[1] /= 9.0 #reverberation_time_s [0.1, 9.0]
  param_T[2] /= 20000. #lows_cutoff_frequency_hz [20., 20000.]
  param_T[3] /= 0.9 #lows_q_factor [0.01,  0.9]
  param_T[4] = (param_T[4] + 80.) / 86. #lows_gain_db_s [-80., 6.]
  param_T[5] /= 20000. #highs_cutoff_frequency_hz
  param_T[6] /= 0.9 #highs_q_factor [0.01,  0.9]
  param_T[7] = (param_T[7] + 80.) / 86. #highs_gain_db_s [-80., 6.]
  param_T[8] /= 9.0 #fade_in_time_s [0., 9.]

  param = param_T.T

  return param


def denormalize(param):
  """
  intput: torch tensor
  return: torch tensor
  """
  param_T = param.T

  param_T[0] *= 30. #room_size [1, 30]
  param_T[1] *= 9.0 #reverberation_time_s [0.1, 9.0]
  param_T[2] *= 20000. #lows_cutoff_frequency_hz [20., 20000.]
  param_T[3] *= 0.9 #lows_q_factor [0.01,  0.9]
  param_T[4] = param_T[4] * 86. - 80. #lows_gain_db_s [-80., 6.]
  param_T[5] *= 20000. #highs_cutoff_frequency_hz
  param_T[6] *= 0.9 #highs_q_factor [0.01,  0.9]
  param_T[7] = param_T[7] * 86. - 80. #highs_gain_db_s [-80., 6.]
  param_T[8] *= 9.0 #fade_in_time_s [0., 9.]

  param = param_T.T

  return param





def train(model, device, dataset_path, test_path, epochs):

  torch.manual_seed(0)

  loss = nn.MSELoss()
  t_loss = nn.MSELoss()

  MAE_loss = nn.L1Loss()

  optimizer = torch.optim.Adam(model.parameters(), lr=0.0001, weight_decay=0.)

  train_loss, validation_loss = [], []
  batch_train_loss, batch_validation_loss = [], []


  with tqdm(range(epochs), unit='epoch') as tepochs:
    tepochs.set_description('Training')
    for epoch in tepochs:
      model.train()
      # keep track of the running loss
      running_loss = 0.

      train_length = 0

      for file in os.listdir(dataset_path):

        if ".pt" in file:
            try:
                data = torch.load(dataset_path+"/"+file)
            except:
                print("file not read")
                print(file)
                del data
                gc.collect()
                continue

            train_loader = torch.utils.data.DataLoader(data, batch_size=25, shuffle=True, num_workers=0, drop_last=True)

            train_length += len(train_loader)

            for data_acc, data_vox, target in train_loader:
                
                data_acc, data_vox, target = data_acc.to(device), data_vox.to(device), target.to(device)

                data_acc = torch.nn.functional.normalize(data_acc)
                data_vox = torch.nn.functional.normalize(data_vox)

                data_acc *= torch.rand(1).cuda()
                data_vox *= torch.rand(1).cuda()

                normalize(target)

                data = torch.stack((data_acc, data_vox), dim=0)
                data = data.permute(1, 0, 2, 3) #batch, channel, time_step, mel_bank
                pred = model(data)
                optimizer.zero_grad()
                MSE = loss(pred, target)
                MSE.backward()
                optimizer.step()

                pred = denormalize(pred)
                target = denormalize(target)

                MAE = MAE_loss(pred, target)
                running_loss += MAE.item()  # add the loss for this batch
                     

        del data
        del train_loader
        gc.collect()





      #save the checkpoint for each epoch
      #torch.save({
      #      'epoch': epoch,
      #      'model_state_dict': model.state_dict(),
      #      'optimizer_state_dict': optimizer.state_dict(),
      #      'loss': MSE
      #      }, 
      #      "/home/kli421/dir1/Lab_spring2022/results/Comp/check_point/"+str(epoch)+".pt")    



      # append the loss for this epoch
      train_loss.append(running_loss/train_length)

      print("   ")

      print("epoch", epoch)
      print("train_loss", running_loss/train_length)

      #print("target", target[0])
      #print("pred", pred[0])
      

      # evaluate on test data
      model.eval()
      running_loss = 0.


      for file in os.listdir(test_path):
        if ".pt" in file:
            data = torch.load(test_path+"/"+file)
            test_loader = torch.utils.data.DataLoader(data, batch_size=2, shuffle=False, num_workers=0, drop_last=True)

            for test_acc, test_vox, test_target in test_loader:
                # getting the validation set
                test_acc, test_vox, test_target = test_acc.to(device), test_vox.to(device), test_target.to(device)

                test_acc = torch.nn.functional.normalize(test_acc)
                test_vox = torch.nn.functional.normalize(test_vox)

                test_data = torch.stack((test_acc, test_vox), dim=0)
                test_data = test_data.permute(1, 0, 2, 3) #batch, channel, time_step, mel_bank

                optimizer.zero_grad()
                test_pred = model(test_data)

                test_pred = denormalize(test_pred)

                MAE = MAE_loss(test_pred, test_target)
                running_loss += MAE.item()  # add the loss for this batch

      

      validation_loss.append(running_loss/len(test_loader))

      print("validation_loss", running_loss/len(test_loader))

      print("test_target", test_target[0])
      print("test_pred", test_pred[0])


  

  return train_loss, validation_loss#, batch_train_loss, batch_validation_loss



###############################################################################

device = torch.device('cuda')


dataset_path = "/home/kli421/dir1/reverb_mel/musdb18/train/pt/"

test_path = "/home/kli421/dir1/reverb_mel/musdb18/test/pt"



###############################################################################

net = ReverbNet().to(device)

train_loss, validation_loss = train(net, device, dataset_path, test_path, 100)



###############################################################################

textfile = open("../../../results/train_loss.txt", "w")
for element in train_loss:
    textfile.write(str(element) + "\n")
textfile.close()

textfile = open("../../../results/validation_loss.txt", "w")
for element in validation_loss:
    textfile.write(str(element) + "\n")
textfile.close()



###############################################################################


import matplotlib.pyplot as plt



def plot(train_loss, validation_loss, plot_output_path):

  plt.plot(train_loss, color='darkorange', label='train loss')
  plt.plot(validation_loss, color='deepskyblue', label='validation loss')
  plt.xlabel('Epochs')
  plt.ylabel("L1 Loss (in dB)")
  plt.ylim([0., 10.])
  #plt.title("Loss")
  plt.legend(bbox_to_anchor=(1, -0.1), borderaxespad=0)
  plt.tight_layout()
  plt.savefig(plot_output_path)
  plt.close()

plot_output_path = '../../../results/Loss.png'

plot(train_loss, validation_loss, plot_output_path)
