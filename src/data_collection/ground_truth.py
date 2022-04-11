import soundfile as sf
import numpy as np
import sys
from scipy import signal
import json
import os


################################################################################################################

def ground_truth(audio_path, ground_truth_path, mixture_path, filename):

    data, sampleRate = sf.read(audio_path + "/" + filename)

    rand_dB = np.random.uniform(-6,0,1)

    rand_amp = 10**(rand_dB/20)

    acc = np.array([data.T[0]/2, data.T[0]/2], dtype=np.float32).T #Accompaniment
    vox = np.array([data.T[1]/2, data.T[1]/2], dtype=np.float32).T #Vocal
    str_rand = ''
    vox *= rand_amp
    str_rand = "_" + str(rand_dB)
    mix = (acc.T + vox.T).T #mono_sum


    acc_shortTermLoudness = shortTermLoudness(acc, SR=sampleRate)
    vox_shortTermLoudness = shortTermLoudness(vox, SR=sampleRate)
    mix_shortTermLoudness = shortTermLoudness(mix, SR=sampleRate)
    accREL_shortTermLoudness = acc_shortTermLoudness - mix_shortTermLoudness
    voxREL_shortTermLoudness = vox_shortTermLoudness - mix_shortTermLoudness


    acc_bandRMS = filter_bank(acc, sampleRate)
    vox_bandRMS = filter_bank(vox, sampleRate)
    mix_bandRMS = filter_bank(mix, sampleRate)
    acc_minus_vox_bandRMS =  acc_bandRMS - vox_bandRMS

    timeInSec = np.arange(acc_shortTermLoudness.size) * 0.1

    ground_truth = {}
    filename_noExt = filename[:-4]
    ground_truth[filename_noExt+"_timeInSec"] = timeInSec.tolist()
    ground_truth[filename_noExt+"_acc_shortTermLoudness"] = acc_shortTermLoudness.tolist()
    ground_truth[filename_noExt+"_vox_shortTermLoudness"] = vox_shortTermLoudness.tolist()
    ground_truth[filename_noExt+"_mix_shortTermLoudness"] = mix_shortTermLoudness.tolist()
    ground_truth[filename_noExt+"_accREL_shortTermLoudness"] = accREL_shortTermLoudness.tolist()
    ground_truth[filename_noExt+"_voxREL_shortTermLoudness"] = voxREL_shortTermLoudness.tolist()


    with open(ground_truth_path + filename_noExt + str_rand + "_ground_truth.json", 'w') as outfile:
        json.dump(ground_truth, outfile)

    filename = "mixture"  + "_" + filename[:-4] + str_rand + ".wav"
    mixture_path_filename = mixture_path + "/" + filename
    sf.write(mixture_path_filename, mix, sampleRate)



################################################################################################################

def ground_truth_generation_MIR_1K(audio_path = "../Audio/MIR-1K",
                            ground_truth_path = "../Ground_truth/MIR-1K/",
                            mixture_path = "../Audio/Mixture/MIR-1K_mixture"):

    abs_audio_path = os.path.abspath(audio_path)

    for filename in os.listdir(abs_audio_path):
        if filename.endswith(".wav"):
            ground_truth(audio_path, ground_truth_path, mixture_path, filename)


################################################################################################################

def ground_truth_generation_MUSDB(audio_path = "../Audio/musdb18hq",
                            ground_truth_path = "../Ground_truth/musdb18hq",
                            mixture_path = "../Audio/Mixture/musdb18hq_mixture"):

    abs_audio_path = os.path.abspath(audio_path)

    for dir in os.listdir(abs_audio_path):
        stem_path = abs_audio_path+"/"+dir
        vox_path = stem_path+"/"+"vocals.wav"
        if not os.path.isfile(vox_path):
            continue
        original_mixture_path = stem_path+"/"+"mixture.wav"

        vox, sampleRate = sf.read(vox_path)
        mix_original, sampleRate = sf.read(original_mixture_path)

        acc = mix_original - vox

        vox_mono = vox.T[0]/2 + vox.T[1]/2
        acc_mono = acc.T[0]/2 + acc.T[1]/2


        rand_dB = np.random.uniform(-6,0,1)
        rand_amp = 10**(rand_dB/20)
        str_rand = ''
        vox_mono *= rand_amp
        str_rand = "_" + str(rand_dB)

        mix_mono = vox_mono + acc_mono

        vox = np.array([vox_mono, vox_mono], dtype=np.float32).T
        acc = np.array([acc_mono, acc_mono], dtype=np.float32).T
        mix = np.array([mix_mono, mix_mono], dtype=np.float32).T

        acc_shortTermLoudness = shortTermLoudness(acc, SR=sampleRate)
        vox_shortTermLoudness = shortTermLoudness(vox, SR=sampleRate)
        mix_shortTermLoudness = shortTermLoudness(mix, SR=sampleRate)
        accREL_shortTermLoudness = acc_shortTermLoudness - mix_shortTermLoudness
        voxREL_shortTermLoudness = vox_shortTermLoudness - mix_shortTermLoudness

        acc_bandRMS = filter_bank(acc, sampleRate)
        vox_bandRMS = filter_bank(vox, sampleRate)
        mix_bandRMS = filter_bank(mix, sampleRate)
        acc_minus_vox_bandRMS =  acc_bandRMS - vox_bandRMS


        timeInSec = np.arange(acc_shortTermLoudness.size) * 0.1

        ground_truth = {}
        filename = str(dir)
        ground_truth[filename+"_timeInSec"] = timeInSec.tolist()
        ground_truth[filename+"_acc_shortTermLoudness"] = acc_shortTermLoudness.tolist()
        ground_truth[filename+"_vox_shortTermLoudness"] = vox_shortTermLoudness.tolist()
        ground_truth[filename+"_mix_shortTermLoudness"] = mix_shortTermLoudness.tolist()
        ground_truth[filename+"_accREL_shortTermLoudness"] = accREL_shortTermLoudness.tolist()
        ground_truth[filename+"_voxREL_shortTermLoudness"] = voxREL_shortTermLoudness.tolist()


        with open(ground_truth_path +"/"+ filename + str_rand + "_ground_truth.json", 'w') as outfile:
            json.dump(ground_truth, outfile)

        mixture_path_filename = mixture_path+"/mixture_"+str(dir)+str_rand+".wav"
        sf.write(mixture_path_filename, mix, sampleRate)

################################################################################################################
