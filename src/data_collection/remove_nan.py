import os
import torch
import numpy as np



def remove_nan(data_path, output_path):

    device = torch.device('cuda')

    dataset = torch.load(data_path)
    loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, num_workers=0)

    finite_idx_list = []
    count = 0
    for data_acc, data_vox, target in loader:
    
        if torch.isfinite(target):
            finite_idx_list.append(count)
    
        count += 1


    clean_dataset = torch.utils.data.Subset(dataset, finite_idx_list)

    torch.save(clean_dataset, output_path)




#dataset_path = "/home/kli421/dir1/GTZAN/GTZAN_normalized.pt"
#otuput_path = "/home/kli421/dir1/GTZAN/GTZAN_normalized.pt"

#remove_nan(dataset_path, otuput_path)


dataset_path = "/home/kli421/dir1/MSD_pt"


for file in os.listdir(dataset_path):

        if ".pt" in file:
            data_path = dataset_path+"/"+file
            otuput_path = dataset_path+"/"+file

            remove_nan(data_path, otuput_path)