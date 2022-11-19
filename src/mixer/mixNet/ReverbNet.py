import os
import sys
import torch
import torch.nn as nn
import numpy as np


###############################################################################

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

    # Fully connected layer 1.
    x = torch.flatten(x, 1)
    x = self.dropout(x)
    x = self.fc2(x)
    x = torch.squeeze(x)
    
    return x


###############################################################################


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



###############################################################################


def limit_range(pred_arr):

  if pred_arr[0] < 1:  pred_arr[0] = 1. #room_size [1, 30]
  if pred_arr[0] > 30:  pred_arr[0] = 30. #room_size [1, 30]
  
  if pred_arr[1] < 0.1: pred_arr[1] = 0.1 #reverberation_time_s [0.1, 9.0]
  if pred_arr[1] > 9.0: pred_arr[1] = 9.0 #reverberation_time_s [0.1, 9.0]

  if pred_arr[2] < 20.: pred_arr[2] = 20. #lows_cutoff_frequency_hz [20., 20000.]
  if pred_arr[2] > 20000.: pred_arr[2] = 20000. #lows_cutoff_frequency_hz [20., 20000.]

  if pred_arr[3] < 0.01: pred_arr[3] = 0.01 #lows_q_factor [0.01,  0.9]
  if pred_arr[3] > 0.9: pred_arr[3] = 0.9 #lows_q_factor [0.01,  0.9]

  if pred_arr[4] < -80: pred_arr[4] = -80. #lows_gain_db_s [-80., 6.]
  if pred_arr[4] > 6.: pred_arr[4] = 6. #lows_gain_db_s [-80., 6.]

  if pred_arr[5] < 20.: pred_arr[5] = 20. #highs_cutoff_frequency_hz [20., 20000.]
  if pred_arr[5] > 20000.: pred_arr[5] = 20000. #highs_cutoff_frequency_hz [20., 20000.]

  if pred_arr[6] < 0.01: pred_arr[6] = 0.01 #highs_q_factor [0.01,  0.9]
  if pred_arr[6] > 0.9: pred_arr[6] = 0.9 #highs_q_factor [0.01,  0.9]

  if pred_arr[7] < -80: pred_arr[7] = -80. #highs_gain_db_s [-80., 4.]
  if pred_arr[7] > 4.: pred_arr[7] = 4. #highs_gain_db_s [-80., 4.]

  if pred_arr[8] < 0.:  pred_arr[8] = 0. #fade_in_time_s [0., 9.]
  if pred_arr[8] > 9.:  pred_arr[8] = 9. #fade_in_time_s [0., 9.]

  if pred_arr[9] < 0.:  pred_arr[9] = 0. #dry_wet [0., 1.]
  if pred_arr[9] > 1.:  pred_arr[9] = 1. #dry_wet [0., 1.]

  return pred_arr


###############################################################################


def run_ReverbNet(self, data, model_path="./mixer/mixNet/ReverbNet.pt", model_class=ReverbNet, device=torch.device('cpu')):

  if torch.cuda.is_available():
    map_location=lambda storage, loc: storage.cuda()
  else:
    map_location='cpu'

  checkpoint = torch.load(model_path, map_location=map_location)

  model = model_class().to(device)
  model.load_state_dict(checkpoint['model_state_dict'])

  model.eval()

  data_loader = torch.utils.data.DataLoader(data, batch_size=1, shuffle=False, num_workers=0)

  pred_arr = np.zeros(10)
  counter = 0

  for acc, vox in data_loader:
      # getting the validation set
      acc, vox = acc.to(device), vox.to(device)

      acc = torch.nn.functional.normalize(acc)
      vox = torch.nn.functional.normalize(vox)

      intput_data = torch.stack((acc, vox), dim=0)
      intput_data = intput_data.permute(1, 0, 2, 3) #batch, channel, time_step, mel_bank

      pred = model(intput_data)

      pred = denormalize(pred)

      pred_arr += pred.detach().cpu().numpy()
      counter += 1


  pred_arr /= counter

  pred_arr = limit_range(pred_arr)


  self.param_dict["room_size"] = pred_arr[0]
  self.param_dict["reverberation_time_s"] = pred_arr[1]
  self.param_dict["lows_cutoff_frequency_hz"] = pred_arr[2]
  self.param_dict["lows_q_factor"] = pred_arr[3]
  self.param_dict["lows_gain_db_s"] = pred_arr[4]
  self.param_dict["highs_cutoff_frequency_hz"] = pred_arr[5]
  self.param_dict["highs_q_factor"] = pred_arr[6]
  self.param_dict["highs_gain_db_s"] = pred_arr[7]
  self.param_dict["fade_in_time_s"] = pred_arr[8]
  self.param_dict["dry_wet"] = pred_arr[9]
  

  return None
            









      

  



