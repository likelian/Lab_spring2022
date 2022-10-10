import os
import torch
import numpy as np
import gc


#get the averge loudness from extracted ground truth



dataset_path = "/home/kli421/dir1/MSD_mel"



loudness_list = []

device = torch.device('cuda')



counter = 0

for file in os.listdir(dataset_path):

    if ".pt" in file:
        data_path = dataset_path+"/"+file

        print(data_path)

        dataset = torch.load(data_path)
        loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, num_workers=0)

        for data_acc, data_vox, target in loader:
            #if np.isfinite(target.item()) and target.item() > -10. and target.item() < 6.:
            if np.isfinite(target.item()):
                loudness_list.append(target.item())
                break
            #because the loudness is the same for one song, just get the first one

        del dataset
        del loader
        gc.collect()
    
    counter += 1

    #if counter > 5:
    #    break


averge_loudness = np.mean(np.asarray(loudness_list))

print(loudness_list)
print("averge relative loudness of uncleaned MSD is: ", averge_loudness)