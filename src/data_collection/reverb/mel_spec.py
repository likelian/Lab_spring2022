import os
from os import walk
import json
import torch
import torchaudio
import soundfile as sf
import numpy as np
import sys


def mel_spec(audio_path, output_path, param_path):
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
        if "mixture.wav" in filenames \
            and "vocals.wav" in filenames:
            mixture_path = dirpath+"/mixture.wav"
            #acc_path = dirpath+"/no_vocals.wav"
            vox_path = dirpath+"/vocals.wav"
            path_str = str(dirpath)
            index = path_str.rfind('/')
            filename = path_str[index+1:]
        else:
            continue


        if filename+"-parameter.json" not in os.listdir(param_path):
            continue
        
        print(filename)


        with open(param_path+filename+"-parameter.json", 'r') as f:
            param_dict = json.load(f)
        
        param = list(param_dict.values())

        
        

        mxiture, sample_rate = torchaudio.load(mixture_path)
        #acc, sample_rate = torchaudio.load(acc_path)
        vox, sample_rate = torchaudio.load(vox_path)

        rate = sample_rate

        acc = mxiture - vox

        #mono
        acc = torch.mean(acc, 0)
        vox = torch.mean(vox, 0)

        acc_mel_spec = transform(acc)
        vox_mel_spec = transform(vox)


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


        param_matrix = torch.zeros(acc_mel_spec.shape[0], len(param))
        param_tensor = torch.FloatTensor(param)
        for i in range(param_matrix.shape[0]):
            param_matrix[i] = param_tensor
        


        dataset = torch.utils.data.TensorDataset(acc_mel_spec, vox_mel_spec, param_matrix)

        torch.save(dataset, output_path+filename+'.pt')




audio_path = "/home/kli421/dir1/musdb18hq/train/"
output_path = "/home/kli421/dir1/reverb_mel/musdb18/train/single_file/"
param_path = "/home/kli421/dir1/Lab_spring2022/data/reverb_parameter/train/parameters/"

mel_spec(audio_path, output_path, param_path)


audio_path = "/home/kli421/dir1/musdb18hq/test/"
output_path = "/home/kli421/dir1/reverb_mel/musdb18/test/single_file"
param_path = "/home/kli421/dir1/Lab_spring2022/data/reverb_parameter/test/parameters/"

mel_spec(audio_path, output_path, param_path)