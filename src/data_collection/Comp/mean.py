import os
import torch
import numpy as np



def mean(data_path, output_path):

    #sprint(data_path)

    device = torch.device('cuda')

    dataset = torch.load(data_path)
    loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, num_workers=0)

    finite_idx_list = []
    count = 0
    local_val = 0.
    for data_acc, data_vox, target in loader:
        local_val += target
        count += 1

    
    return local_val, count





dataset_path = "/home/kli421/dir1/comp_mel/concat/MSD"

total_val = 0.
total_count = 0

for file in os.listdir(dataset_path):

        if ".pt" in file:
            data_path = dataset_path+"/"+file
            otuput_path = dataset_path+"/"+file

            local_val, count = mean(data_path, otuput_path)
            total_val += local_val
            total_count += count

print(total_val/total_count)
            




dataset_path = "/home/kli421/dir1/comp_mel/concat/musdb18hq/test"

total_val = 0.
total_count = 0

for file in os.listdir(dataset_path):

        if ".pt" in file:
            data_path = dataset_path+"/"+file
            otuput_path = dataset_path+"/"+file

            local_val, count = mean(data_path, otuput_path)
            total_val += local_val
            total_count += count

print(total_val/total_count)





dataset_path = "/home/kli421/dir1/comp_mel/concat/musdb18hq/train"

total_val = 0.
total_count = 0

for file in os.listdir(dataset_path):

        if ".pt" in file:
            data_path = dataset_path+"/"+file
            otuput_path = dataset_path+"/"+file

            local_val, count = mean(data_path, otuput_path)
            total_val += local_val
            total_count += count

print(total_val/total_count)