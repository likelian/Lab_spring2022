import os
import torch
import torch.nn as nn
import numpy as np
#from tqdm import tqdm





###############################################################################


test_folder = "/home/kli421/dir1/musdb18hq_mel/test"


###############################################################################



model = TheModelClass(*args, **kwargs)
optimizer = TheOptimizerClass(*args, **kwargs)

model_path = "/home/kli421/dir1/Lab_spring2022/results/check_point.pt"
checkpoint = torch.load(model_path)


device = torch.device('cuda')

eval_song_level(checkpoint, device, test_folder)


def eval_song_level(checkpoint, device, test_folder):

  model.load_state_dict(checkpoint['model_state_dict'])
  optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
  epoch = checkpoint['epoch']
  loss = checkpoint['loss']

  model.eval()



