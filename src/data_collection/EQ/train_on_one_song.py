import torch
import os
import gc


def concat(dataset_path, otuput_path):

    datasets = []


    counter = 1

    for file in os.listdir(dataset_path):


        if "A Classic Education - NightOwl" in file \
            and "[63, 125, 500, 4000][ 6.88 -8.53  3.29  4.19]" not in file:

            print(counter)
            print("here")

            try:
                data = torch.load(dataset_path+"/"+file)
            except:
                print(dataset_path+"/"+file)
                continue

            datasets.append(data)
            del data
            gc.collect()
            counter += 1
            
        
            
    
    dataset = torch.utils.data.ConcatDataset(datasets)
    torch.save(dataset, otuput_path+"A Classic Education - NightOwl"+".pt")
    del datasets[:]
    del datasets
    datasets = []
    del dataset



dataset_path = "/home/kli421/dir1/EQ_mel/musdb18hq/train/"
otuput_path = "/home/kli421/dir1/EQ_mel/musdb18hq/one_song/train/"

concat(dataset_path, otuput_path)