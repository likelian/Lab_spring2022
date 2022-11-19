import os
import sys
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

    # Fully connected layer 1.
    x = torch.flatten(x, 1)
    x = self.dropout(x)
    x = self.fc1(x)
    x = torch.squeeze(x)

    return x


###############################################################################


def run_FaderNet(data, model_path="./mixer/mixNet/FaderNet.pt", model_class=FaderNet, device=torch.device('cpu')):

  if torch.cuda.is_available():
    map_location=lambda storage, loc: storage.cuda()
  else:
    map_location='cpu'

  checkpoint = torch.load(model_path, map_location=map_location)

  model = model_class().to(device)
  model.load_state_dict(checkpoint['model_state_dict'])

  model.eval()

  data_loader = torch.utils.data.DataLoader(data, batch_size=1, shuffle=False, num_workers=0)

  pred_list = []

  for acc, vox in data_loader:
      # getting the validation set
      acc, vox = acc.to(device), vox.to(device)

      acc = torch.nn.functional.normalize(acc)
      vox = torch.nn.functional.normalize(vox)

      intput_data = torch.stack((acc, vox), dim=0)
      intput_data = intput_data.permute(1, 0, 2, 3) #batch, channel, time_step, mel_bank

      pred = model(intput_data)

      pred_list.append(pred.cpu().detach().item())

  pred_mean = np.mean(np.array(pred_list))

  return pred_mean
            









      

  



