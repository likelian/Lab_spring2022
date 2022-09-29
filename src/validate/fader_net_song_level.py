import os
import torch
import torch.nn as nn
import numpy as np
from tqdm import tqdm



def validate(model, device, train_loader, test_loader, epochs):

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


      for data_acc, data_vox, target in train_loader:

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

        running_loss += MSE.item()**0.5  # add the loss for this batch


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
          running_loss += test_MSE.item()**0.5

      validation_loss.append(running_loss/len(test_loader))

      print("validation_loss", running_loss/len(test_loader))

      #break

  return train_loss, validation_loss#, batch_train_loss, batch_validation_loss




###############################################################################

device = torch.device('cuda')




test_folder = "/home/kli421/dir1/musdb18hq_mel/test"



###############################################################################

net = FaderNet().to(device)

train_loss, validation_loss = validate(net, device, train_loader, test_loader, 100)


