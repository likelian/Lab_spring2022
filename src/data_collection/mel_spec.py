import os
from os import walk
import json
import torch
import torchaudio

def mel_spec(audio_path, output_path, ground_truth_dict):
    """
    create mel_spec tensor and level ratio ground truth
    """

    abs_audio_path = os.path.abspath(audio_path)

    #win_length = n_fft
    #hop_length = win_length // 2
    transform = torchaudio.transforms.MelSpectrogram(sample_rate=44100, n_fft=2048)


    for (dirpath, dirnames, filenames) in walk(abs_audio_path):

        if "mixture.wav" in filenames \
            and "vocals.wav" in filenames:

            mxiture_path = dirpath+"/mixture.wav"
            vox_path = dirpath+"/vocals.wav"

            path_str = str(dirpath)
            index = path_str.rfind('/')
            filename = path_str[index+1:]
            print(filename)

            ground_truth = ground_truth_dict[filename+"--vox_acc_ratio"]


        else:
            continue

        mxiture, sample_rate = torchaudio.load(mxiture_path)
        vox, sample_rate = torchaudio.load(vox_path)

        acc = mxiture - vox

        acc = torch.mean(acc, 0)
        vox = torch.mean(vox, 0)

        acc_mel_spec = transform(acc)
        vox_mel_spec = transform(vox)


        def reshape(mel_spec):
            frameNum = mel_spec.shape[1]
            blockNum = int(frameNum / 64) #64 * 2048 / 44100 = 2.97s
            mel_spec = mel_spec.T[:-(frameNum - blockNum*64)].T
            mel_spec_matrix = torch.reshape(mel_spec, (128, blockNum, 64))
            mel_spec_matrix = mel_spec_matrix.permute(1, 2, 0) #blocks, time frame, freq frame
            return mel_spec_matrix

        acc_mel_spec = reshape(acc_mel_spec)
        vox_mel_spec = reshape(vox_mel_spec)

        gt_tensor = torch.full((acc_mel_spec.shape[0],), ground_truth)

        dataset = torch.utils.data.TensorDataset(acc_mel_spec, vox_mel_spec, gt_tensor)

        torch.save(dataset, output_path+filename+'.pt')




#ground_truth_path = "../../data/vox_acc_ratio/train_vox_acc_ratio.json"
ground_truth_path = "../../data/vox_acc_ratio/test_vox_acc_ratio.json"
f = open(ground_truth_path)
ground_truth_dict = json.load(f)


#output_path = "/Volumes/mix/Dataset/musdb18hq_mel/train/"
output_path = "/Volumes/mix/Dataset/musdb18hq_mel/test/"

#audio_path = "/Volumes/mix/Dataset/musdb18hq/train"
audio_path = "/Volumes/mix/Dataset/musdb18hq/test"

mel_spec(audio_path, output_path, ground_truth_dict)



"""
batch_size = 16
train_dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size)

for X_1, X_2, y in train_dataloader:
    print(X_1.shape)
    print(X_2.shape)
    print(y.shape)
"""
