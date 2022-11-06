import os
from os import walk
import json
import torch
import torchaudio
import soundfile as sf
import numpy as np
import sys
import pyloudnorm as pyln

def mel_spec(audio_path, output_path):
    """
    create mel_spec tensor and level ratio ground truth
    """

    #abs_audio_path = os.path.abspath(audio_path)
    abs_audio_path = audio_path

    #win_length = n_fft
    #hop_length = win_length // 2
    transform = torchaudio.transforms.MelSpectrogram(sample_rate=44100, n_fft=2048)

    


    for (dirpath, dirnames, filenames) in walk(abs_audio_path):

        #musdb18hq dataset
        #if "mixture.wav" in filenames \
        #    and "vocals.wav" in filenames:

        #GTZAN dataset
        if "no_vocals.wav" in filenames \
            and "vocals.wav" in filenames:

            #mixture_path = dirpath+"/mixture.wav"
            acc_path = dirpath+"/no_vocals.wav"
            vox_path = dirpath+"/vocals.wav"

            path_str = str(dirpath)
            index = path_str.rfind('/')
            filename = path_str[index+1:]
            print(filename)


        else:
            continue

        #mxiture, sample_rate = torchaudio.load(mxiture_path)
        acc, sample_rate = torchaudio.load(acc_path)
        vox, sample_rate = torchaudio.load(vox_path)

        #acc = mxiture - vox

        #mono
        acc = torch.mean(acc, 0)
        vox = torch.mean(vox, 0)

        acc_mel_spec = transform(acc)
        vox_mel_spec = transform(vox)

        meter = pyln.Meter(44100)


        acc = acc.detach().numpy()
        vox = vox.detach().numpy()

        #extract snippet relative loudness
        #vox_acc_ratio_list = []
        #for i in range(int(acc.shape[0] / 65536)):
        #    acc_loudness = meter.integrated_loudness(acc[i * 65536 : i*65536+65536])
        #    vox_loudness = meter.integrated_loudness(vox[i * 65536 : i*65536+65536])
        #
        #    if not np.isfinite(acc_loudness) or not np.isfinite(vox_loudness):
        #        vox_acc_ratio = np.asarray(np.nan)
        #    else:
        #        vox_acc_ratio = vox_loudness - acc_loudness
        #
        #    vox_acc_ratio_list.append(vox_acc_ratio)


        #extract the overall integrated loudness
        acc_loudness = meter.integrated_loudness(acc)
        vox_loudness = meter.integrated_loudness(vox)
        vox_acc_ratio = vox_loudness - acc_loudness

        vox_acc_ratio_list = []
        for i in range(int(acc.shape[0] / 65536)):
            vox_acc_ratio_list.append(vox_acc_ratio)






        def reshape(mel_spec):
            frameNum = mel_spec.shape[1]
            blockNum = int(frameNum / 64) #64*1024/44100 = 1.48s
            mel_spec = mel_spec.T[:-(frameNum - blockNum*64)].T
            mel_spec_matrix = torch.reshape(mel_spec, (128, blockNum, 64))
            mel_spec_matrix = mel_spec_matrix.permute(1, 2, 0) #blocks, time frame, freq frame
            return mel_spec_matrix

        try:
            acc_mel_spec = reshape(acc_mel_spec)
        except:
            print("reshape(acc_mel_spec)")
            continue
        
        try:
            vox_mel_spec = reshape(vox_mel_spec)
        except:
            print("reshape(vox_mel_spec)")
            continue


        if len(vox_acc_ratio_list) != acc_mel_spec.shape[0]:
            print("ground truth and input data size not match")
            print(len(vox_acc_ratio_list))
            print(acc_mel_spec.shape[0])


        gt_tensor = torch.tensor(np.asarray(vox_acc_ratio_list)).float()


        dataset = torch.utils.data.TensorDataset(acc_mel_spec, vox_mel_spec, gt_tensor)

        torch.save(dataset, output_path+filename+'.pt')


#output_path = "/home/kli421/dir1/musdb18hq_mel/train_snippet/"
#output_path = "/home/kli421/dir1/musdb18hq_mel/test_snippet/"

#audio_path = "/home/kli421/dir1/musdb18hq/train"
#audio_path = "/home/kli421/dir1/musdb18hq/test"

#mel_spec(audio_path, output_path)



#output_path = "/home/kli421/dir1/GTZAN_mel/"
#audio_path = "/home/kli421/dir1/GTZAN/separated/mdx_extra/"

#mel_spec(audio_path, output_path)



output_path = "/home/kli421/dir1/MSD_mel/"
audio_path = "/home/kli421/dir1/MSD/separated/mdx_extra/"

mel_spec(audio_path, output_path)