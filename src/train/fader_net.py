import os
import torch
import torch.nn as nn
import numpy as np
from tqdm import tqdm


class FaderNet(nn.Module):
  def __init__(self):
    """Intitalize neural net layers"""
    super(FaderNet, self).__init__()
    self.conv1 = nn.Conv2d(in_channels=2, out_channels=8, kernel_size=3, stride=1, padding=0)
    self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, stride=1, padding=0)
    self.conv3 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=0)
    self.conv4 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=0)
    self.conv5 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=0)
    self.fc1 = nn.Linear(in_features=768, out_features=1)

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

    # Conv layer 5.
    #x = self.conv5(x)
    #x = self.batchnorm5(x)
    #x = self.relu5(x)
    #x = self.max_pool2d5(x)

    # Fully connected layer 1.
    x = torch.flatten(x, 1)
    x = self.dropout(x)
    x = self.fc1(x)
    x = torch.squeeze(x)

    return x


def train(model, device, train_loader, test_loader, epochs):

  loss = nn.MSELoss()
  t_loss = nn.MSELoss()

  optimizer = torch.optim.Adam(model.parameters(), lr=0.0005)

  train_loss, validation_loss = [], []
  batch_train_loss, batch_validation_loss = [], []

  with tqdm(range(epochs), unit='epoch') as tepochs:
    tepochs.set_description('Training')
    for epoch in tepochs:
      model.train()
      # keep track of the running loss
      running_loss = 0.

      batch_count = 0

      for data_acc, data_vox, target in train_loader:

        #batch_count += 1

        #train with 1/4 of the data
        #if batch_count >= 37:
        #  break


        # getting the training set
        data_acc, data_vox, target = data_acc.to(device), data_vox.to(device), target.to(device)

        data_acc = torch.nn.functional.normalize(data_acc)
        data_vox = torch.nn.functional.normalize(data_vox)

        data_acc *= torch.rand(1).cuda()
        data_vox *= torch.rand(1).cuda()

        data = torch.stack((data_acc, data_vox), dim=0)
        data = data.permute(1, 0, 2, 3) #batch, channel, time_step, mel_bank

        pred = model(data)
        optimizer.zero_grad()
        MSE = loss(pred, target)
        MSE.backward()
        optimizer.step()

        #tepochs.set_postfix(loss=loss.item())
        running_loss += MSE.item()**0.5  # add the loss for this batch


        #remove the below later
        #validation loss on each file
        """
        
        model.eval()
        val_loss = 0.

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
          #tepochs.set_postfix(loss=loss.item())
          val_loss += test_MSE.item()
          
        #print("test_target", test_target)
        #print("test_pred", test_pred)
        #print("MSE.item()", MSE.item())
        #print("val_loss", val_loss/len(test_loader))

        batch_train_loss.append(MSE.item())
        batch_validation_loss.append(val_loss/len(test_loader))
        
        """
        #end of removal



      # append the loss for this epoch
      train_loss.append(running_loss/len(train_loader))

      print("epoch", epoch)
      print("train_loss", running_loss/len(train_loader))


      # evaluate on test data
      model.eval()
      running_loss = 0.

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
          #tepochs.set_postfix(loss=loss.item())
          running_loss += test_MSE.item()**0.5

      validation_loss.append(running_loss/len(test_loader))

      print("validation_loss", running_loss/len(test_loader))

      #break

  return train_loss, validation_loss, batch_train_loss, batch_validation_loss




###############################################################################

device = torch.device('cuda')

data_path = "../../../musdb18hq/"
train_dataset = torch.load(data_path+'/train.pt')
train_loader = torch.utils.data.DataLoader(
    train_dataset, batch_size=25, shuffle=False, num_workers=0)

test_dataset = torch.load(data_path+'/test.pt')
test_loader = torch.utils.data.DataLoader(
    test_dataset, batch_size=25, shuffle=False, num_workers=0)


###############################################################################

net = FaderNet().to(device)
train_loss, validation_loss, batch_train_loss, batch_validation_loss = train(net, device, train_loader, test_loader, 10)



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

import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt


plt.plot(train_loss, color='darkorange', label='train loss')
plt.plot(validation_loss, color='deepskyblue', label='validation loss')
plt.xlabel('Epochs')
plt.ylabel("L1s Loss (in dB)")
#plt.title("Loss")
#plt.legend(bbox_to_anchor=(1.04,1), borderaxespad=0)
plt.legend(bbox_to_anchor=(1, -0.1), borderaxespad=0)

plt.tight_layout()
plt.savefig('../../results/Loss.png')
#plt.show()
plt.close()


#remove
"""
plt.plot(batch_train_loss, color='darkorange', label='batch train loss')
plt.plot(batch_validation_loss, color='deepskyblue', label='batch validation loss')
plt.xlabel('batches')
plt.ylabel("MSE Loss (in dB)")
#plt.title("Loss")
#plt.legend(bbox_to_anchor=(1.04,1), borderaxespad=0)
plt.legend(bbox_to_anchor=(1, -0.1), borderaxespad=0)

plt.tight_layout()
plt.savefig('../../results/batch_Loss.png')
#plt.show()
plt.close()
"""
#end of remove



"""
epochs = np.arange(len(train_loss))
train_loss = np.asarray(train_loss)
d = {'epochs': epochs, 'MSE Loss': train_loss}
dataframe = pd.DataFrame(d)
g = sns.lineplot(x='epochs', y='MSE Loss', data=dataframe)
g.set_title('Train Loss')
plt.show()
plt.savefig('../../results/Train Loss.png')


epochs = np.arange(len(test_loss))
test_loss = np.asarray(test_loss)
d = {'epochs': epochs, 'MSE Loss': test_loss}
dataframe = pd.DataFrame(d)
g = sns.lineplot(x='epochs', y='MSE Loss', data=dataframe)
g.set_title('Test Loss')
plt.show()
plt.savefig('../../results/Test Loss.png')
"""
