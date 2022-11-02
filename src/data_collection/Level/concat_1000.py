import torch
import os
import gc


def concat(dataset_path, otuput_path):

    datasets = []

    dataset_counter = 0
    counter = 1

    for file in os.listdir(dataset_path):

        if ".pt" in file:
            data = torch.load(dataset_path+"/"+file)
            print(dataset_path+"/"+file)
            datasets.append(data)
            del data
            gc.collect()
            counter += 1
        
        #the last group is not dumped......
        #should be fixed, but not necessary
        if counter >= 1000:
            dataset = torch.utils.data.ConcatDataset(datasets)
            torch.save(dataset, otuput_path+str(dataset_counter)+".pt")
            del datasets[:]
            del datasets
            datasets = []
            del dataset
            counter = 1

            dataset_counter += 1





dataset_path = "/home/kli421/dir1/MSD_mel"
otuput_path = "/home/kli421/dir1/MSD_pt/"

concat(dataset_path, otuput_path)