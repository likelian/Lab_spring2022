import os
import torch
import numpy as np
import gc


def remove_non_vocal(data_path, output_path):

    device = torch.device('cuda')

    dataset = torch.load(data_path)
    loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, num_workers=0)

    vocal_list = []
    count = 0
    for data_acc, data_vox, target in loader:
        if torch.mean(data_vox).detach().numpy() > 0.4:
            vocal_list.append(count)
    
        count += 1

    clean_dataset = torch.utils.data.Subset(dataset, vocal_list)

    torch.save(clean_dataset, output_path)

    #del clean_dataset[:]
    #del dataset[:]
    del clean_dataset
    del dataset





dataset_path = "/home/kli421/dir1/EQ_mel/musdb18hq/concat/test"


for file in os.listdir(dataset_path):

    if ".pt" in file:
        data_path = dataset_path+"/"+file
        otuput_path = dataset_path+"/"+file

        print(data_path)

        remove_non_vocal(data_path, otuput_path)




dataset_path = "/home/kli421/dir1/EQ_mel/musdb18hq/concat/train"

for file in os.listdir(dataset_path):

    if ".pt" in file:
        data_path = dataset_path+"/"+file
        otuput_path = dataset_path+"/"+file

        print(data_path)

        remove_non_vocal(data_path, otuput_path)