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
    torch.save(dataset, otuput_path)


#dataset_path = "/Volumes/mix/Dataset/musdb18hq_mel/test"
#otuput_path = "../../../musdb18hq/"

#dataset_path = "/home/kli421/dir1/GTZAN_mel/"
#otuput_path = "../../../GTZAN/GTZAN.pt"


#dataset_path = "/home/kli421/dir1/musdb18hq_mel/test_normalized"
#otuput_path = "../../../musdb18hq/test_normalized.pt"

#concat(dataset_path, otuput_path)

#dataset_path = "/home/kli421/dir1/musdb18hq_mel/train_normalized"
#otuput_path = "../../../musdb18hq/train_normalized.pt"

#concat(dataset_path, otuput_path)

#dataset_path = "/home/kli421/dir1/GTZAN_mel/normalized"
#otuput_path = "/home/kli421/dir1/GTZAN/GTZAN_normalized.pt"

#concat(dataset_path, otuput_path)


#dataset_path = "/home/kli421/dir1/musdb18hq_mel/test_normalized_overall"
#otuput_path = "../../../musdb18hq/test_normalized_overall.pt"

#concat(dataset_path, otuput_path)

#dataset_path = "/home/kli421/dir1/musdb18hq_mel/train_normalized_overall"
#otuput_path = "../../../musdb18hq/train_normalized_overall.pt"

#concat(dataset_path, otuput_path)

#dataset_path = "/home/kli421/dir1/GTZAN_mel/normalized_overall"
#otuput_path = "/home/kli421/dir1/GTZAN/GTZAN_normalized_overall.pt"

#concat(dataset_path, otuput_path)


dataset_path = "/home/kli421/dir1/MSD_mel"
otuput_path = "/home/kli421/dir1/MSD"

concat(dataset_path, otuput_path)