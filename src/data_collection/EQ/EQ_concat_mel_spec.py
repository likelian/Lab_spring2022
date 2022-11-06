import numpy as np
from pedalboard import Pedalboard, load_plugin
import os
from os import walk
import json
import torch
import torchaudio
import soundfile as sf
import sys



vst_path = "/Users/likelian/Desktop/Lab/Lab_spring2022/VST3/"
vst_name = "MultiEQ.vst3"
vst = load_plugin(vst_path + vst_name)



def mono(audio):
    if len(audio.shape) == 2:
        return np.mean(audio, axis=1)
    else:
        return audio


def applyEQ(vst, vox, rate, freq_top_list, gain_top_list):
    """
    apply EQ to vox from given parameters

    vst: MultiEQ.vst3 loaded by Pedalboard
    vox: numpy array of the mono signal
    rate: sample rate of the signal
    freq_top_list: numpy array of 4 center freqency values
        [20.0, 20000.0]
    gain_top_list: numpy array of 4 gain values matched to the freq_top_list
        [-60.0, 15.0]

    all Q values are 1.

    return: processed signals
    """

    vst.filter_enablement_1 = True
    vst.filter_type_1 = "Low-shelf" #'HP (6dB/oct)', 'HP (12dB/oct)', 'HP (24dB/oct)', 'Low-shelf'
    vst.filter_frequency_1_hz = 100. #[20.0Hz, 20000.0Hz]
    vst.filter_q_1 = 1. #[0.05, 8.0]
    #vst.filter_gain_1_db = -12. #[-60.0dB, 15.0dB]
    vst.filter_gain_1_db = 0. #[-60.0dB, 15.0dB]s


    vst.filter_enablement_2 = True
    vst.filter_type_2 = "Peak" #'Low-shelf', 'Peak', 'High-shelf'
    vst.filter_frequency_2_hz = freq_top_list[0] #[20.0Hz, 20000.0Hz]
    vst.filter_q_2 = 1. #[0.05, 8.0]
    vst.filter_gain_2_db = gain_top_list[0] #[-60.0dB, 15.0dB]


    vst.filter_enablement_3 = True
    vst.filter_type_3 = "Peak" #'Low-shelf', 'Peak', 'High-shelf'
    vst.filter_frequency_3_hz = freq_top_list[1] #[20.0Hz, 20000.0Hz]
    vst.filter_q_3 = 1. #[0.05, 8.0]
    vst.filter_gain_3_db = gain_top_list[1] #[-60.0dB, 15.0dB]

    vst.filter_enablement_4 = True
    vst.filter_type_4 = "Peak" #'Low-shelf', 'Peak', 'High-shelf'
    vst.filter_frequency_4_hz = freq_top_list[2] #[20.0Hz, 20000.0Hz]
    vst.filter_q_4 = 1. #[0.05, 8.0]
    vst.filter_gain_4_db = gain_top_list[2] #[-60.0dB, 15.0dB]


    vst.filter_enablement_5 = True
    vst.filter_type_5 = "Peak" #'Low-shelf', 'Peak', 'High-shelf'
    vst.filter_frequency_5_hz = freq_top_list[3] #[20.0Hz, 20000.0Hz]
    vst.filter_q_5 = 1. #[0.05, 8.0]
    vst.filter_gain_5_db = gain_top_list[3] #[-60.0dB, 15.0dB]


    vst.filter_enablement_6 = True
    vst.filter_type_6 = "High-shelf" #'LP (6dB/Oct)', 'LP (12dB/oct)', 'LP (24dB/oct)', 'High-shelf'
    vst.filter_frequency_6_hz = 11000. #[20.0Hz, 20000.0Hz]
    vst.filter_q_6 = 1. #[0.05, 8.0]
    vst.filter_gain_6_db = 0. #[-60.0dB, 15.0dB]

    output = vst(vox, rate)
    return output



def rand_freq_gain():
    """
    return:
        gain_arr (numpy array):
        [ -1.05, -9.28, -14.9, 0., 1.56315401, 0., 0., 0., 0.]
        freq_top_list (list):
        [63, 125, 250, 1000]
        gain_top_list (list):
        [-1.05, -9.28, -14.92, 1.56]
    """

    #fcs = [31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]
    fcs = [63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]

    #uniform random floating number from [-15., 15).
    gain_arr = (np.random.rand(len(fcs),) - 0.5) * 30. 

    rng = np.random.default_rng()
    unselected_freq_idx = rng.choice(len(fcs), len(fcs)-4, replace=False)

    #set unselected gain values to 0.
    for idx in unselected_freq_idx:
        gain_arr[idx] = 0.

    freq_top_list = []
    gain_top_list = []

    for idx, val in enumerate(gain_arr):
        if val != 0.:
            freq_top_list.append(fcs[idx])
            gain_top_list.append(val)

    return gain_arr, freq_top_list, gain_top_list




def EQ_mel_spec(abs_audio_path, output_path):

    #win_length = n_fft
    #hop_length = win_length // 2
    transform = torchaudio.transforms.MelSpectrogram(sample_rate=44100, n_fft=2048)

    for (dirpath, dirnames, filenames) in walk(abs_audio_path):

        
        
        #musdb18hq dataset
        if "mixture.wav" in filenames \
            and "vocals.wav" in filenames:

        #GTZAN dataset
        #if "no_vocals.wav" in filenames \
         #   and "vocals.wav" in filenames:

            mixture_path = dirpath+"/mixture.wav"
            #acc_path = dirpath+"/no_vocals.wav"
            vox_path = dirpath+"/vocals.wav"

            path_str = str(dirpath)
            index = path_str.rfind('/')
            filename = path_str[index+1:]
            print(filename)


        else:
            continue

        try:
            mxiture, sample_rate = torchaudio.load(mixture_path)
        except:
            continue
        #acc, sample_rate = torchaudio.load(acc_path)

        try:
            vox, sample_rate = torchaudio.load(vox_path)
        except:
            continue

        acc = mxiture - vox

        #mono
        acc = torch.mean(acc, 0)
        vox = torch.mean(vox, 0)


        #meter = pyln.Meter(44100)

        acc_mel_spec = transform(acc)

        vox_mel_spec = transform(vox)

        #acc = acc.detach().numpy()
        vox = vox.detach().numpy()

        gain_arr, freq_top_list, gain_top_list = rand_freq_gain()

        new_vox = applyEQ(vst, vox, sample_rate, freq_top_list, gain_top_list)

        new_vox = torch.from_numpy(new_vox)

        new_vox_mel_spec = transform(new_vox)


        gain_matrix = np.zeros((int(acc.shape[0] / 65536), gain_arr.size))

        idx = 0
        for i in gain_matrix:
            gain_matrix[idx] = gain_arr
            idx += 1


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
            new_vox_mel_spec = reshape(new_vox_mel_spec)
        except:
            print("reshape(vox_mel_spec)")
            continue


        if gain_matrix.shape[0] != acc_mel_spec.shape[0]:
            print("ground truth and input data size not match")
            print(len(vox_acc_ratio_list))
            print(acc_mel_spec.shape[0])



        


        gt_tensor = torch.tensor(gain_matrix).float()


        print("gt_tensor", gt_tensor.shape)
        print("acc_mel_spec", acc_mel_spec.shape)


        gt_tensor = torch.mean(gt_tensor, dim=0, keepdim=True)


        #concat mel-spectrums
        acc_mel_spec = torch.mean(acc_mel_spec, dim=0, keepdim=True)
        new_vox_mel_spec = torch.mean(new_vox_mel_spec, dim=0, keepdim=True)



        print("gt_tensor", gt_tensor.shape)
        print("acc_mel_spec", acc_mel_spec.shape)


        dataset = torch.utils.data.TensorDataset(acc_mel_spec, new_vox_mel_spec, gt_tensor)


        #quit()


        print(str(freq_top_list))
        gain_top_list_rounded = np.around(gain_top_list, decimals=2)
        print(str(gain_top_list_rounded))

        torch.save(dataset, output_path+filename+"_"+str(freq_top_list)+str(gain_top_list_rounded)+'.pt')



#about 10MB for each file
output_path = "/Volumes/mix/Dataset/EQ_mel/musdb18hq/concat/test/"
audio_path = "/Volumes/mix/Dataset/musdb18hq/test"

for i in range(100):
    EQ_mel_spec(audio_path, output_path)



#about 10MB for each file
output_path = "/Volumes/mix/Dataset/EQ_mel/musdb18hq/concat/train/"
audio_path = "/Volumes/mix/Dataset/musdb18hq/train"

for i in range(2000):
    EQ_mel_spec(audio_path, output_path)



