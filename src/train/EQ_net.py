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
    self.fc1 = nn.Linear(in_features=768, out_features=9)

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


    # Fully connected layer 1.
    x = torch.flatten(x, 1)
    #x = self.dropout(x)
    x = self.fc1(x)
    x = torch.squeeze(x)

    return x


def train(model, device, dataset_path, test_path, epochs):

  loss = nn.L1Loss()
  t_loss = nn.L1Loss()

  optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

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
            data = torch.load(dataset_path+"/"+file)
            train_loader = torch.utils.data.DataLoader(data, batch_size=25, shuffle=True, num_workers=0)

            train_length += len(train_loader)

            for data_acc, data_vox, target in train_loader:
                
                data_acc, data_vox, target = data_acc.to(device), data_vox.to(device), target.to(device)

                data_acc = torch.nn.functional.normalize(data_acc)
                data_vox = torch.nn.functional.normalize(data_vox)

                data_acc *= torch.rand(1).cuda()
                data_vox *= torch.rand(1).cuda()

                data = torch.stack((data_acc, data_vox), dim=0)
                data = data.permute(1, 0, 2, 3) #batch, channel, time_step, mel_bank
                pred = model(data)
                optimizer.zero_grad()
                #if torch.mean(torch.abs(pred)) < 3.:
                #    MSE = loss(pred, target) - 0.4 * torch.mean(torch.abs(pred))
                #elif torch.mean(torch.abs(pred)) > 5.:
                #    MSE = loss(pred, target) + 0.4 * torch.mean(torch.abs(pred))
                #else:
                #    MSE = loss(pred, target)

                if torch.mean(torch.abs(pred)) < 5.:
                    MSE = loss(pred, target) - torch.mean(torch.abs(pred)) + 3.3
                else:
                    MSE = loss(pred, target)

                MSE.backward()
                optimizer.step()

                running_loss += loss(pred, target).item() #**0.5  # add the loss for this batch

        print("--------------------")
        print("    ")
        print('target', target[0])
        print('pred', pred[0])
        

        #remove!!!!!!!!!!!!!!!
        #only train on the first .pt file
        break

        


        #print("train_loss", running_loss/train_length)

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
      #      "/home/kli421/dir1/Lab_spring2022/results/check_point/"+str(epoch)+".pt")    



      # append the loss for this epoch
      train_loss.append(running_loss/train_length)

      print("epoch", epoch)
      print("train_loss", running_loss/train_length)
      

      # evaluate on test data
      model.eval()
      running_loss = 0.
      length = 0

      for file in os.listdir(test_path):

        if ".pt" in file:
            data = torch.load(test_path+"/"+file)
            test_loader = torch.utils.data.DataLoader(data, batch_size=30, shuffle=False, num_workers=0)

            for test_acc, test_vox, test_target in test_loader:
                # getting the validation set
                test_acc, test_vox, test_target = test_acc.to(device), test_vox.to(device), test_target.to(device)

                test_acc = torch.nn.functional.normalize(test_acc)
                test_vox = torch.nn.functional.normalize(test_vox)

                test_data = torch.stack((test_acc, test_vox), dim=0)
                test_data = test_data.permute(1, 0, 2, 3) #batch, channel, time_step, mel_bank

                optimizer.zero_grad()
                test_pred = model(test_data)
                test_MSE = t_loss(test_pred, test_target)
                running_loss += test_MSE.item()#**0.5

            length += len(test_loader)

            del data
            del test_loader
            gc.collect()
      
   
      validation_loss.append(running_loss/length)
      print("validation_loss", running_loss/length)

      print('test_pred', test_pred[0])
      print('test_target', test_target[0])


  return train_loss, validation_loss#, batch_train_loss, batch_validation_loss



###############################################################################

device = torch.device('cuda')


dataset_path = "/home/kli421/dir1/EQ_mel/musdb18hq/concat/train/"

test_path = "/home/kli421/dir1/EQ_mel/musdb18hq/concat/test"

###############################################################################

net = EqNet().to(device)

train_loss, validation_loss = train(net, device, dataset_path, test_path, 1000)



###############################################################################

textfile = open("../../results/train_loss.txt", "w")
for element in train_loss:
    textfile.write(str(element) + "\n")
textfile.close()

textfile = open("../../results/validation_loss.txt", "w")
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

plot_output_path = '../../results/Loss.png'

plot(train_loss, validation_loss, plot_output_path)