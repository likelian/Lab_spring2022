import os
import torch
import torch.nn as nn
import numpy as np


class EqNet(nn.Module):
  def __init__(self):
    """Intitalize neural net layers"""
    super(EqNet, self).__init__()
    self.conv1 = nn.Conv2d(in_channels=2, out_channels=8, kernel_size=3, stride=1, padding=0)
    self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, stride=1, padding=0)
    self.conv3 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=0)
    self.conv4 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=0)
    self.conv5 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=0)

    
    self.fc3 = nn.Linear(in_features=768, out_features=9, bias=True)

    self.sig1 = nn.Sigmoid()
    self.sig2 = nn.Sigmoid()

    self.batchnorm1 = nn.BatchNorm2d(num_features=8)
    self.batchnorm2 = nn.BatchNorm2d(num_features=16)
    self.batchnorm3 = nn.BatchNorm2d(num_features=32)
    self.batchnorm4 = nn.BatchNorm2d(num_features=64)
    self.batchnorm5 = nn.BatchNorm2d(num_features=128)
    self.batchnorm6 = nn.BatchNorm1d(num_features=9)

    self.relu1 = nn.ReLU()
    self.relu2 = nn.ReLU()
    self.relu3 = nn.ReLU()
    self.relu4 = nn.ReLU()
    self.relu5 = nn.ReLU()

    self.Softmax1 = nn.Softmax(dim=1)

    self.max_pool2d1 = nn.MaxPool2d(kernel_size=2)
    self.max_pool2d2 = nn.MaxPool2d(kernel_size=2)
    self.max_pool2d3 = nn.MaxPool2d(kernel_size=2)
    self.max_pool2d4 = nn.MaxPool2d(kernel_size=2)
    self.max_pool2d5 = nn.MaxPool2d(kernel_size=2)

    self.dropout1 = nn.Dropout(p=0.3, inplace=False)
    self.dropout2 = nn.Dropout(p=0.3, inplace=False)
    self.dropout3 = nn.Dropout(p=0.3, inplace=False)


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
    x = self.dropout3(x)
    x = self.fc3(x)
    x = torch.squeeze(x)

    return x


def select_top_predction(pred):
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

  pred = pred.detach().numpy()

  #get the absolute value
  mapped = np.abs(pred) 
  #sort aescendingly and return indics
  
  
  try:
    idx = np.argsort(mapped)
  except:
    print("mapped.size()", mapped.size())

  #get the mapped values of the fifth largest mapped absoluted value
  border_val = mapped[idx[4]]


  ones = np.ones(pred.shape)
  zeros = np.zeros(pred.shape)

  #1 if the top 4 largest mapped absoluted value, else 0
  filter_map = np.where(mapped > border_val, ones, zeros)
  #change small values to 0
  filtered_pred = filter_map * pred


  return filtered_pred




def run_EqNet(data, model_path="./mixer/mixNet/EqNet.pt", model_class=EqNet, device=torch.device('cpu')):

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

        acc = torch.nn.functional.normalize(acc) * 0.1
        vox = torch.nn.functional.normalize(vox) * 0.1

        intput_data = torch.stack((acc, vox), dim=0)
        intput_data = intput_data.permute(1, 0, 2, 3) #batch, channel, time_step, mel_bank

        pred = model(intput_data)

    pred = pred * 30. - 15.

    filtered_pred = select_top_predction(pred)

    #reverse the predicted gain
    filtered_pred = -filtered_pred

    return filtered_pred
