import os
from os import walk
import json
import torch
import torchaudio
import soundfile as sf
import numpy as np
import sys
import pyloudnorm as pyln



def reshape(mel_spec):
    frameNum = mel_spec.shape[1]
    blockNum = int(frameNum / 64) #64*1024/44100 = 1.48s
    mel_spec = mel_spec.T[:-(frameNum - blockNum*64)].T
    mel_spec_matrix = torch.reshape(mel_spec, (128, blockNum, 64))
    mel_spec_matrix = mel_spec_matrix.permute(1, 2, 0) #blocks, time frame, freq frame
    return mel_spec_matrix
    

def non_vocal_check(audio_path):
    """
    compare LUFS and mel spec mean
    remove vocal loudness below -40LUFS
    similar to mean of the mel specrogram below 0.4
    """
    transform = torchaudio.transforms.MelSpectrogram(sample_rate=44100, n_fft=2048)

    meter = pyln.Meter(44100)

    for (dirpath, dirnames, filenames) in walk(audio_path):

        if "mixture.wav" in filenames and "vocals.wav" in filenames:

            mxiture_path = dirpath+"/mixture.wav"
            vox_path = dirpath+"/vocals.wav"

            path_str = str(dirpath)
            index = path_str.rfind('/')
            filename = path_str[index+1:]
            print(filename)



            vox, sample_rate = torchaudio.load(vox_path)
            vox = torch.mean(vox, 0)

            vox_mel_spec = transform(vox)
            vox_mel_spec = reshape(vox_mel_spec)
            
            vox_loudness_list = []
            vox = vox.detach().numpy()
            i = 0
            for i in range(int(vox.shape[0] / 65536)):
                #acc_loudness = meter.integrated_loudness(acc[i * 65536 : i*65536+65536])
                vox_loudness = meter.integrated_loudness(vox[i * 65536 : i*65536+65536])
                vox_loudness_list.append(vox_loudness)

                if(torch.mean(vox_mel_spec[i]).detach().numpy() < 0.4):
                    print(str(vox_loudness), torch.mean(vox_mel_spec[i]))
                #print()

                i += 1

            
            if len(vox_loudness_list) != vox_mel_spec.shape[0]:
                print("ground truth and input data size not match")
                print(len(vox_loudness_list))
                print(vox_mel_spec.shape[0])

            

audio_path = "/home/kli421/dir1/musdb18hq/test"
remove_non_vocal(audio_path)  


            

    