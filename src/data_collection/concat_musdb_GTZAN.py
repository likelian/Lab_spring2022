import torch
import os


datasets = []

dataset_path = "/home/kli421/dir1/musdb18hq/train.pt"
data = torch.load(dataset_path)
datasets.append(data)


dataset_path = "/home/kli421/dir1/GTZAN/GTZAN.pt"
data = torch.load(dataset_path)
datasets.append(data)

dataset = torch.utils.data.ConcatDataset(datasets)


otuput_path = "/home/kli421/dir1/training_set/musdb_GTZAN.pt"
torch.save(dataset, otuput_path)