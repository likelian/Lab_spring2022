import os
import torch
import numpy as np



device = torch.device('cuda')

data_path = "../../../musdb18hq/"
dataset = torch.load(data_path+'/test_snippet.pt')

loader = torch.utils.data.DataLoader(
    dataset, batch_size=1, shuffle=False, num_workers=0)

nan_idx_list = []
count = 0
for data_acc, data_vox, target in loader:
    
    if not torch.isnan(target):
        nan_idx_list.append(count)
    
    count += 1


dataset = torch.utils.data.Subset(dataset, nan_idx_list)


torch.save(dataset, data_path+'/test_snippet_clean.pt')


