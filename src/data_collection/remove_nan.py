import os
import torch
import numpy as np



def remove_nan(data_path, output_path):

    device = torch.device('cuda')

    dataset = torch.load(data_path)
    loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, num_workers=0)

    nan_idx_list = []
    count = 0
    for data_acc, data_vox, target in loader:
    
        if not torch.isnan(target):
            nan_idx_list.append(count)
    
        count += 1


    clean_dataset = torch.utils.data.Subset(dataset, nan_idx_list)

    torch.save(clean_dataset, output_path)




data_path = "../../../musdb18hq/test_snippet.pt"
output_path = "../../../musdb18hq/test_snippet_clean.pt"

remove_nan(data_path, output_path)



data_path = "../../../musdb18hq/train_snippet.pt"
output_path = "../../../musdb18hq/train_snippet_clean.pt"

remove_nan(data_path, output_path)