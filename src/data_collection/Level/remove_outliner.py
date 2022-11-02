import os
import torch
import numpy as np



def remove_outliner(data_path, output_path):

    device = torch.device('cuda')

    dataset = torch.load(data_path)
    loader = torch.utils.data.DataLoader(dataset, batch_size=1, shuffle=False, num_workers=0)

    finite_idx_list = []
    count = 0
    for data_acc, data_vox, target in loader:
    
        if target > -10. and target < 6.:
            finite_idx_list.append(count)            

        count += 1


    clean_dataset = torch.utils.data.Subset(dataset, finite_idx_list)

    torch.save(clean_dataset, output_path)




#data_path = "/home/kli421/dir1/training_set/musdb_GTZAN_clean.pt"
#output_path = "/home/kli421/dir1/training_set/musdb_GTZAN_cleaner.pt"

#data_path = "/home/kli421/dir1/musdb18hq/train.pt"
#output_path = "/home/kli421/dir1/musdb18hq/train_cleaner.pt"

#data_path = "/home/kli421/dir1/musdb18hq/train.pt"
#output_path = "/home/kli421/dir1/musdb18hq/train_cleaner.pt"

#remove_outliner(data_path, output_path)



#dataset_path = "/home/kli421/dir1/musdb18hq/train_normalized.pt"
#otuput_path = "/home/kli421/dir1/musdb18hq/train_normalized.pt"

#remove_outliner(dataset_path, otuput_path)


#dataset_path = "/home/kli421/dir1/GTZAN/GTZAN_normalized.pt"
#otuput_path = "/home/kli421/dir1/GTZAN/GTZAN_normalized.pt"

#remove_outliner(dataset_path, otuput_path)



#dataset_path = "/home/kli421/dir1/musdb18hq/train_normalized_overall.pt"
#otuput_path = "/home/kli421/dir1/musdb18hq/train_normalized_overall.pt"

#remove_outliner(dataset_path, otuput_path)

#dataset_path = "/home/kli421/dir1/GTZAN/GTZAN_normalized_overall.pt"
#otuput_path = "/home/kli421/dir1/GTZAN/GTZAN_normalized_overall.pt"

#remove_outliner(dataset_path, otuput_path)



dataset_path = "/home/kli421/dir1/MSD_pt"


for file in os.listdir(dataset_path):

        if ".pt" in file:
            data_path = dataset_path+"/"+file
            otuput_path = dataset_path+"/"+file

            remove_outliner(data_path, otuput_path)