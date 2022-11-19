import os
import torch
import torch.nn as nn
import numpy as np


###############################################################################

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


###############################################################################


def run_FaderNet(checkpoint, model_class, device, test_folder):

  model = model_class().to(device)
  model.load_state_dict(checkpoint['model_state_dict'])

  model.eval()

  abs_error_list = []

  #load data of each song
  data = torch.load(test_folder+"/"+file)

  test_loader = torch.utils.data.DataLoader(data, batch_size=1, shuffle=False, num_workers=0)

  test_pred_list = []

  for test_acc, test_vox in test_loader:
      # getting the validation set
      test_acc, test_vox, test_target = test_acc.to(device), test_vox.to(device), test_target.to(device)

      test_acc = torch.nn.functional.normalize(test_acc)
      test_vox = torch.nn.functional.normalize(test_vox)

      test_data = torch.stack((test_acc, test_vox), dim=0)
      test_data = test_data.permute(1, 0, 2, 3) #batch, channel, time_step, mel_bank

      #optimizer.zero_grad()
      test_pred = model(test_data)

      test_pred_list.append(test_pred.cpu().detach().item())



      test_pred_mean = np.mean(np.array(test_pred_list))

      return test_pred_mean
            

###############################################################################


#audio to mel spec
#mel spec to dataloader

model_class = FaderNet
model_path = "FaderNet.pt"
checkpoint = torch.load(model_path)
device = torch.device('cpu')

run_FaderNet(checkpoint, model_class, device)





      

  



