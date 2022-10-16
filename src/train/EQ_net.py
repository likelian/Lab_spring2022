import os
import torch
import torch.nn as nn
import numpy as np
from tqdm import tqdm
import gc


class EqNet(nn.Module):
  def __init__(self):
    """Intitalize neural net layers"""
    super(EqNet, self).__init__()
    self.conv1 = nn.Conv2d(in_channels=2, out_channels=8, kernel_size=3, stride=1, padding=0)
    self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, stride=1, padding=0)
    self.conv3 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=0)
    self.conv4 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=0)
    self.conv5 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=0)

    
    self.fc1 = nn.Linear(in_features=768, out_features=9, bias=False)

    #self.fc1 = nn.Linear(in_features=768, out_features=768)
    #self.fc2 = nn.Linear(in_features=768, out_features=768)
    #self.fc3 = nn.Linear(in_features=768, out_features=9)

    #self.sig1 = nn.Sigmoid()
    #self.sig2 = nn.Sigmoid()

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
    self.tanh2 = nn.Tanh()
    self.tanh3 = nn.Tanh()
    self.tanh4 = nn.Tanh()
    self.tanh5 = nn.Tanh()

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
    #x = self.relu1(x)
    x = self.tanh1(x)
    x = self.max_pool2d1(x)

    # Conv layer 2.
    x = self.conv2(x)
    x = self.batchnorm2(x)
    #x = self.relu2(x)
    x = self.tanh2(x)
    x = self.max_pool2d2(x)

    # Conv layer 3.
    x = self.conv3(x)
    x = self.batchnorm3(x)
    #x = self.relu3(x)
    x = self.tanh3(x)
    x = self.max_pool2d3(x)

    # Conv layer 4.
    x = self.conv4(x)
    x = self.batchnorm4(x)
    #x = self.relu4(x)
    x = self.tanh4(x)
    x = self.max_pool2d4(x)


    # Fully connected layer 1.
    x = torch.flatten(x, 1)
    #x = self.dropout(x)
    x = self.fc1(x)
    #x = self.sig1(x)
    #x = self.fc2(x)
    #x = self.sig2(x)
    #x = self.fc3(x)
    x = torch.squeeze(x)

    return x


def select_top_predction(pred, target):
  """
  select the top 4 prections with largest absolute gain change from 0dB

  input: 
    pred (tensor matrix)
    target (tensor matrix)

  return:
    filtered_target (unselected values set to 0.)
    filtered_pred (unselected values set to 0.)
    zeros_target (selected values set to 0.)
    zeros_pred (selected values set to 0.)
  """

  if target.size() != pred.size():
    target = target[:pred.size()[0]]
    pred = pred[:target.size()[0]]

  #map prediction from [0., 1.] to [-0.5, 0.5] and get the absolute value
  mapped = torch.abs(pred-0.5) 
  #sort aescendingly and return indics
  
  
  #print("mapped.size()", mapped.size())
  try:
    idx = torch.argsort(mapped, dim=1).T
  except:
    print("mapped.size()", mapped.size())


  #get the mapped values of the fifth largest mapped absoluted value
  border_val = mapped.gather(1, idx[4].long().unsqueeze(1)) 
  border_val.expand(border_val.size()[0], target.size()[0]) #expand into a matrix

  ones = torch.ones(pred.size()).to(device)
  zeros = torch.zeros(pred.size()).to(device)

  #1 if the top 4 largest mapped absoluted value, else 0
  filter_map = torch.where(mapped > border_val, ones, zeros)
  #change small values to 0
  filtered_target = filter_map * target
  filtered_pred = filter_map * pred
  #0 if the top 4 largest mapped absoluted value, else 1
  zeros_map = torch.where(mapped > border_val, zeros, ones)
  #change large values to 0
  zeros_target = zeros_map * target
  zeros_pred = zeros_map * pred

  return filtered_target, filtered_pred, zeros_target, zeros_pred




def train(model, device, dataset_path, test_path, epochs):

  loss = nn.MSELoss()
  t_loss = nn.MSELoss()
  MAE_train_loss = nn.L1Loss()
  MAE_validation_loss = nn.L1Loss()
  L1_train_loss = nn.L1Loss()
  L1_validation_loss = nn.L1Loss()

  optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

  train_loss, validation_loss = [], []
  #batch_train_loss, batch_validation_loss = [], []

  processed_train_loss, processed_validation_loss = [], []


  with tqdm(range(epochs), unit='epoch') as tepochs:
    tepochs.set_description('Training')
    for epoch in tepochs:
      model.train()
      # keep track of the running loss
      running_loss = 0.

      processed_loss = 0.

      train_length = 0
      
      counter = 0

      for file in os.listdir(dataset_path):
        if ".pt" in file:
            data = torch.load(dataset_path+"/"+file)
            train_loader = torch.utils.data.DataLoader(data, batch_size=25, shuffle=True, num_workers=0, drop_last=True)

            train_loader_count = 0

            for data_acc, data_vox, target in train_loader:

                #remove!!!!!
                #only train on 1/300 of the data
                #train_loader_count += 1
                #if train_loader_count % 300 != 0:
                #  continue
                
                train_length += 1

                data_acc, data_vox, target = data_acc.to(device), data_vox.to(device), target.to(device)
              
                target = (target + 15.)/30. #normalize the target from (-15.0, 15.0) to (0., 1.)

                data_acc = torch.nn.functional.normalize(data_acc)
                data_vox = torch.nn.functional.normalize(data_vox)

                data_acc *= torch.rand(1).cuda()
                data_vox *= torch.rand(1).cuda()

                data = torch.stack((data_acc, data_vox), dim=0)
                data = data.permute(1, 0, 2, 3) #batch, channel, time_step, mel_bank
                pred = model(data)
                optimizer.zero_grad()


                
                #loss function only concerns about where the targeted ground truth has gain changes
                #in other words, the values in target that are 0dB or normalized 0. are ingored
                #so as the corresponding values in prediction
                ones = torch.ones(target.shape).to(device)
                zeros = torch.zeros(target.shape).to(device)

                filter_idx = torch.where(target != 0.5, ones, zeros)
                filtered_target = filter_idx * target
                filtered_pred = filter_idx * pred

                zeros_idx = torch.where(target == 0.5, ones, zeros)
                zeros_target = zeros_idx * target
                zeros_pred = zeros_idx * pred

                filter_idx = torch.where(target != 0.5, ones, zeros)
                

                #filtered_target, filtered_pred, zeros_target, zeros_pred = select_top_predction(pred, target)

                #small values are set to 0.5
                processed_pred = torch.where(filtered_pred == 0., 0.5, filtered_pred)

                #print(torch.mean(torch.abs(processed_pred - 0.5)))
                #add weighted loss of non-changed gains
                #if torch.mean(torch.abs(processed_pred - 0.5)) < 0.1:
                #  MSE = loss(filtered_pred, filtered_target) - torch.mean(torch.abs(processed_pred - 0.5)) + 0.11111111
                #else:
                #  MSE = loss(filtered_pred, filtered_target) + 0.1 * loss(zeros_target, zeros_pred)


                #MSE = loss(processed_pred, target)
                MSE = loss(filtered_pred, filtered_target)


                pred_dB = pred * 30. - 15.
                target_dB = target * 30. - 15.
                processed_pred_dB = processed_pred * 30. - 15.

                MAE_train = MAE_train_loss(pred_dB, target_dB)

                processed_MAE = L1_train_loss(processed_pred_dB, target_dB)

                MSE.backward()
                optimizer.step()

                #running_loss += loss(pred, target).item() #**0.5  # add the loss for this batch
                running_loss += MAE_train.item()
                processed_loss += processed_MAE.item()

        
        del data
        del train_loader
        gc.collect()

        #remove!!!!!!!!!!!!!!!
        #only train on the first 1 .pt file, half of all
        counter += 1
        if counter >= 1:
          break
        

      # append the loss for this epoch
      train_loss.append(running_loss/train_length)
      processed_train_loss.append(processed_loss/train_length)

      
      print("--------------------")
      print("    ")
      print("epoch", epoch)
      print("    ")
      print('pred', pred_dB[0])
      print('targ', target_dB[0])
      print("    ")
      print("train_loss", running_loss/train_length)
      print("processed_train_loss", processed_loss/train_length)
      



      #save the checkpoint for each epoch

      #torch.save({
      #      'epoch': epoch,
      #      'model_state_dict': model.state_dict(),
      #      'optimizer_state_dict': optimizer.state_dict(),
      #      'loss': MSE
      #      }, 
      #      "/home/kli421/dir1/Lab_spring2022/results/check_point/"+str(epoch)+".pt")    
      

      # evaluate on test data
      model.eval()
      running_loss = 0.
      processed_loss = 0.
      length = 0

      for file in os.listdir(test_path):

        if ".pt" in file:
            data = torch.load(test_path+"/"+file)
            test_loader = torch.utils.data.DataLoader(data, batch_size=25, shuffle=False, num_workers=0, drop_last=True)

            for test_acc, test_vox, test_target in test_loader:
                # getting the validation set
                test_acc, test_vox, test_target = test_acc.to(device), test_vox.to(device), test_target.to(device)

                

                test_acc = torch.nn.functional.normalize(test_acc)
                test_vox = torch.nn.functional.normalize(test_vox)

                test_data = torch.stack((test_acc, test_vox), dim=0)
                test_data = test_data.permute(1, 0, 2, 3) #batch, channel, time_step, mel_bank

                optimizer.zero_grad()
                test_pred = model(test_data)


                mapped_target = (test_target + 15.)/30.

                filtered_test_target, filtered_test_pred, zeros_test_target, zeros_test_pred = select_top_predction(test_pred, mapped_target)
                
                processed_test_pred = torch.where(filtered_test_pred == 0., 0.5, filtered_test_pred)

                test_pred = test_pred * 30. - 15.
                processed_test_pred_dB = processed_test_pred * 30. - 15.

                test_MSE = MAE_validation_loss(test_pred, test_target)
                running_loss += test_MSE.item()

                processed_test_MAE = L1_validation_loss(processed_test_pred_dB, test_target)
                processed_loss += processed_test_MAE.item()

            length += len(test_loader)

            del data
            del test_loader
            gc.collect()
      


      validation_loss.append(running_loss/length)
      print("validation_loss", running_loss/length)

      processed_validation_loss.append(processed_loss/length)
      print("processed_validation_loss", processed_loss/length)

      

      print("    ")
      print('test_pred', test_pred[0])
      print('test_targ', test_target[0])

      print("pred abs mean", torch.mean(torch.abs(test_pred)).item())
      


  return train_loss, validation_loss, processed_train_loss, processed_validation_loss






###############################################################################

device = torch.device('cuda')


dataset_path = "/home/kli421/dir1/EQ_mel/musdb18hq/concat/train/"

test_path = "/home/kli421/dir1/EQ_mel/musdb18hq/concat/test"

###############################################################################

net = EqNet().to(device)

train_loss, validation_loss, processed_train_loss, processed_validation_loss = train(net, device, dataset_path, test_path, 50)



###############################################################################

textfile = open("../../results/train_loss.txt", "w")
for element in train_loss:
    textfile.write(str(element) + "\n")
textfile.close()

textfile = open("../../results/validation_loss.txt", "w")
for element in validation_loss:
    textfile.write(str(element) + "\n")
textfile.close()


textfile = open("../../results/processed_train_loss.txt", "w")
for element in processed_train_loss:
    textfile.write(str(element) + "\n")
textfile.close()

textfile = open("../../results/rocessed_validation_loss.txt", "w")
for element in processed_validation_loss:
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

plot_output_path = '../../results/Loss.png'

plot(train_loss, validation_loss, plot_output_path)


plot_output_path = '../../results/Processed_Loss.png'

plot(processed_train_loss, processed_validation_loss, plot_output_path)
