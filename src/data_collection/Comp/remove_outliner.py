import os
import torch
import numpy as np



def remove_outliner(data_path, output_path):

    print(data_path)

    device = torch.device('cuda')

    dataset = torch.load(data_path)
    loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, num_workers=0)

    finite_idx_list = []
    count = 0
    for data_acc, data_vox, target in loader:
    
        if target > -30. and target < 5.:
            finite_idx_list.append(count)            

        count += 1


    clean_dataset = torch.utils.data.Subset(dataset, finite_idx_list)

    torch.save(clean_dataset, output_path)




dataset_path = "/home/kli421/dir1/comp_mel/concat/MSD"

for file in os.listdir(dataset_path):

        if ".pt" in file:
            data_path = dataset_path+"/"+file
            otuput_path = dataset_path+"/"+file

            remove_outliner(data_path, otuput_path)




dataset_path = "/home/kli421/dir1/comp_mel/concat/musdb18hq/test"

for file in os.listdir(dataset_path):

        if ".pt" in file:
            data_path = dataset_path+"/"+file
            otuput_path = dataset_path+"/"+file

            remove_outliner(data_path, otuput_path)





dataset_path = "/home/kli421/dir1/comp_mel/concat/musdb18hq/train"

for file in os.listdir(dataset_path):

        if ".pt" in file:
            data_path = dataset_path+"/"+file
            otuput_path = dataset_path+"/"+file

            remove_outliner(data_path, otuput_path)