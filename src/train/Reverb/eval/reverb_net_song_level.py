import os
import torch
import torch.nn as nn
import numpy as np
#from tqdm import tqdm
import matplotlib.pyplot as plt


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


###############################################################################

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


###############################################################################


def eval_song_level(checkpoint, model_class, device, test_folder):

  model = model_class().to(device)
  model.load_state_dict(checkpoint['model_state_dict'])

  #optimizer = TheOptimizerClass(*args, **kwargs)
  #optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
  #epoch = checkpoint['epoch']
  #loss = checkpoint['loss']

  model.eval()

  param_label_list = ["room_size", 
                      "reverberation_time_s",
                      "lows_cutoff_frequency_hz",
                      "lows_q_factor",
                      "lows_gain_db_s",
                      "highs_cutoff_frequency_hz",
                      "highs_q_factor",
                      "highs_gain_db_s",
                      "fade_in_time_s",
                      "dry_wet"
                      ]

  test_indie_error_df = pd.DataFrame(columns=param_label_list)

  #load data of each song
  for file in os.listdir(test_folder):

        if ".pt" in file:
            data = torch.load(test_folder+"/"+file)
            print(file)
  
            test_loader = torch.utils.data.DataLoader(data, batch_size=1, shuffle=False, num_workers=0)

            running_loss = 0.

            for test_acc, test_vox, test_target in test_loader:
                # getting the validation set
                test_acc, test_vox, test_target = test_acc.to(device), test_vox.to(device), test_target.to(device)

                test_acc = torch.nn.functional.normalize(test_acc)
                test_vox = torch.nn.functional.normalize(test_vox)

                test_data = torch.stack((test_acc, test_vox), dim=0)
                test_data = test_data.permute(1, 0, 2, 3) #batch, channel, time_step, mel_bank

                #optimizer.zero_grad()
                test_pred = model(test_data)

                test_pred = denormalize(test_pred)

                indie_error = torch.mean(torch.abs(test_pred - test_target), dim=0).detach().cpu().numpy()

                try:
                  test_indie_error_df.loc[file] += indie_error
                except:
                  test_indie_error_df.loc[file] = indie_error




  abs_error_mean = test_indie_error_df.mean(axis=0)

  print("abs_error over 48 test songs", abs_error_mean)




###############################################################################


test_folder = "/home/kli421/dir1/reverb_mel/musdb18/test/single_file"

#model_path = ""

checkpoint = torch.load(model_path)

device = torch.device('cuda')

model_class = ReverbNet

eval_song_level(checkpoint, model_class, device, test_folder)





      

  



