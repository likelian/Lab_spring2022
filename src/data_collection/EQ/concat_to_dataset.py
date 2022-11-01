import torch
import os
import gc


def concat(dataset_path, otuput_path):

    datasets = []

    dataset_counter = 0
    counter = 1

    for file in os.listdir(dataset_path):

        if ".pt" in file:
            try:
                data = torch.load(dataset_path+"/"+file)
            except:
                print(dataset_path+"/"+file)
                continue

            print("pass")
            print("")
            
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
            
    
    dataset = torch.utils.data.ConcatDataset(datasets)
    torch.save(dataset, otuput_path+str(dataset_counter)+".pt")
    del datasets[:]
    del datasets
    datasets = []
    del dataset



dataset_path = "/home/kli421/dir1/EQ_mel/musdb18hq/concat/10000/train"
otuput_path = "/home/kli421/dir1/EQ_mel/musdb18hq/concat/pt/train/"


concat(dataset_path, otuput_path)