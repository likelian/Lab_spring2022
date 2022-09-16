import torch
import os


def concat(dataset_path, otuput_path):

    datasets = []

    for file in os.listdir(dataset_path):

        if ".pt" in file:
            data = torch.load(dataset_path+"/"+file)
            print(dataset_path+"/"+file)
            datasets.append(data)

    dataset = torch.utils.data.ConcatDataset(datasets)
    torch.save(dataset, otuput_path+'/test.pt')


dataset_path = "/Volumes/mix/Dataset/musdb18hq_mel/test"
otuput_path = "../../../musdb18hq/"

concat(dataset_path, otuput_path)