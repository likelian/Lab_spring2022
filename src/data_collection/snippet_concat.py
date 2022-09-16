import os
import torch
import numpy as np
import json


def concat(dataset_path, otuput_path):

    datasets = []

    for file in os.listdir(dataset_path):

        if ".pt" in file:
            data = torch.load(dataset_path+"/"+file)
            print(dataset_path+"/"+file)
            datasets.append(data)

    dataset = torch.utils.data.ConcatDataset(datasets)
    torch.save(dataset, otuput_path)


#dataset_path = "/home/kli421/dir1/musdb18hq_mel/train_snippet/"
dataset_path = "/home/kli421/dir1/musdb18hq_mel/test_snippet/"

#otuput_path = "../../../musdb18hq/train_snippet.pt"
otuput_path = "../../../musdb18hq/test_snippet.pt"

concat(dataset_path, otuput_path)





dataset_path = "/home/kli421/dir1/musdb18hq_mel/train_snippet/"
#dataset_path = "/home/kli421/dir1/musdb18hq_mel/test_snippet/"

otuput_path = "../../../musdb18hq/train_snippet.pt"
#otuput_path = "../../../musdb18hq/test_snippet.pt"

concat(dataset_path, otuput_path)