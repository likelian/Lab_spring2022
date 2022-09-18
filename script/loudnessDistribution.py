import torch
import numpy as np
import matplotlib.pyplot as plt



device = torch.device('cuda')

#data_path = "../../musdb18hq/"
#train_dataset = torch.load(data_path+'/train.pt')
#train_dataset = torch.load("/home/kli421/dir1/GTZAN/GTZAN_clean.pt")
train_dataset = torch.load("/home/kli421/dir1/training_set/musdb_GTZAN_clean.pt")
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=25, shuffle=False, num_workers=0)

#test_dataset = torch.load(data_path+'/test.pt')
#test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=25, shuffle=False, num_workers=0)

relative_loudness_list = []
previous = 0
for data_acc, data_vox, target in train_loader:
    target_relative_loudness = target[0].cpu().detach().numpy()
    if target_relative_loudness != previous:
        relative_loudness_list.append(target_relative_loudness)

relative_loudness_array = np.asarray(relative_loudness_list)
averge_relative_loudness = np.mean(relative_loudness_array)

print(averge_relative_loudness)

plt.hist(relative_loudness_array, density=True, bins=100)

plt.savefig('../results/loudnessDistribution.png')
plt.close()



