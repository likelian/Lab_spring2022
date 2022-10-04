import numpy as np
from pedalboard import Pedalboard, load_plugin
import os
from os import walk
import json
import torch
import torchaudio
import soundfile as sf
import sys



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



vst_path = "/home/kli421/dir1/Lab_spring2022/VST3/Linux/"
vst_name = "MultiEQ.so"
vst = load_plugin(vst_path + vst_name)





fcs = [31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]


#create random gain values
#convert to gain_top_list
#randomly select from fcs to freq_top_list


gain_top_list = (np.random.rand(4,) - 0.5) * 30. #uniform random floating number from [-15., 15).


rng = np.random.default_rng()
freq_top_list = rng.choice(fcs, 4, replace=False)


print("gain_top_list", gain_top_list)
print("freq_top_list", freq_top_list)

quit()


output = applyEQ(vst, vox, rate, freq_top_list, gain_top_list)





"""

def EQ_mel_spec(abs_audio_path, output_path):

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


output_path = "/home/kli421/dir1/MSD_mel/"
audio_path = "/home/kli421/dir1/MSD/separated/mdx_extra/"

mel_spec(audio_path, output_path)
"""