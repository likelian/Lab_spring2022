import os
import torch
import torch.nn as nn
import numpy as np
from tqdm import tqdm
import gc
import json


class EqNet(nn.Module):
  def __init__(self):
    """Intitalize neural net layers"""
    super(EqNet, self).__init__()
    self.conv1 = nn.Conv2d(in_channels=2, out_channels=8, kernel_size=3, stride=1, padding=0)
    self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, stride=1, padding=0)
    self.conv3 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, stride=1, padding=0)
    self.conv4 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=0)
    self.conv5 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=0)

    
    #self.fc1 = nn.Linear(in_features=768, out_features=9, bias=True)

    #self.fc1 = nn.Linear(in_features=768, out_features=768, bias=False)
    #self.fc2 = nn.Linear(in_features=768, out_features=768, bias=False)
    self.fc3 = nn.Linear(in_features=768, out_features=9, bias=True)
    #self.fc4 = nn.Linear(in_features=9, out_features=9, bias=True)

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


    self.tanh1 = nn.Tanh()
    self.tanh2 = nn.Tanh()
    self.tanh3 = nn.Tanh()
    self.tanh4 = nn.Tanh()
    self.tanh5 = nn.Tanh()

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
    #x = self.tanh1(x)
    x = self.max_pool2d1(x)

    # Conv layer 2.
    x = self.conv2(x)
    x = self.batchnorm2(x)
    x = self.relu2(x)
    #x = self.tanh2(x)
    x = self.max_pool2d2(x)

    # Conv layer 3.
    x = self.conv3(x)
    x = self.batchnorm3(x)
    x = self.relu3(x)
    #x = self.tanh3(x)
    x = self.max_pool2d3(x)

    # Conv layer 4.
    x = self.conv4(x)
    x = self.batchnorm4(x)
    x = self.relu4(x)
    #x = self.tanh4(x)
    x = self.max_pool2d4(x)


    # Fully connected layer 1.
    x = torch.flatten(x, 1)
    #x = self.dropout1(x)
    #x = self.fc1(x)
    #x = self.sig1(x)
    #x = self.dropout2(x)
    #x = self.fc2(x)
    #x = self.sig2(x)
    #x = self.dropout3(x)
    x = self.fc3(x)
    #x = self.batchnorm6(x)
    #x = self.fc4(x)
    #x = self.tanh1(x)
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


  model_path="/home/kli421/dir1/Lab_spring2022/src/mixer/mixNet/EqNet.pt"


  if torch.cuda.is_available():
      map_location=lambda storage, loc: storage.cuda()
  else:
      map_location='cpu'

  checkpoint = torch.load(model_path, map_location=map_location)

  model = EqNet().to(device)
  model.load_state_dict(checkpoint['model_state_dict'])

  model.eval()



  loss = nn.MSELoss()
  t_loss = nn.MSELoss()
  MAE_train_loss = nn.L1Loss()
  MAE_validation_loss = nn.L1Loss()
  L1_train_loss = nn.L1Loss()
  L1_validation_loss = nn.L1Loss()

  optimizer = torch.optim.Adam(model.parameters(), lr=0.001, weight_decay=0)

  train_loss, validation_loss = [], []
  #batch_train_loss, batch_validation_loss = [], []

  processed_train_loss, processed_validation_loss = [], []

  output_mean = []


 
  running_loss = 0.
  processed_loss = 0.
  length = 0
  abs_mean = 0.

  error_list = []
  mean_error_list = []

  for file in os.listdir(test_path):

    if ".pt" in file:
        data = torch.load(test_path+"/"+file)
        test_loader = torch.utils.data.DataLoader(data, batch_size=20, shuffle=False, num_workers=0, drop_last=True)

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

            abs_mean += torch.mean(torch.abs(processed_test_pred_dB)).item()

            error = processed_test_pred_dB - test_target

            error_list += error.detach().cpu().numpy().flatten().tolist()
            mean_error_list += test_target.detach().cpu().numpy().flatten().tolist()

        length += len(test_loader)

        print(len(error_list))
        print(len(mean_error_list))

        del data
        del test_loader
        gc.collect()

  json_object = json.dumps(mean_error_list)
  with open("EQ_mean_error_list.json", "w") as outfile:
    outfile.write(json_object)

  json_object = json.dumps(error_list)
  with open("EQ_error_list.json", "w") as outfile:
    outfile.write(json_object)
  

      







###############################################################################

device = torch.device('cuda')


dataset_path = "/home/kli421/dir1/EQ_mel/musdb18hq/concat/train/pt/"


test_path = "/home/kli421/dir1/EQ_mel/musdb18hq/concat/test/pt"


###############################################################################

net = EqNet().to(device)

train(net, device, dataset_path, test_path, 200)


