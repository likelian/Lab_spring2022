import numpy as np
import soundfile as sf
from scipy import signal
from pedalboard import Pedalboard, load_plugin
import matplotlib.pyplot as plt
import os
import librosa
import json


def apply_reverb(param_dict, vst, delta, rate):
    """
    render the audio from given parameters in param_dict

    'room_size', 
    'reverberation_time_s', 
    'lows_cutoff_frequency_hz',
    'lows_q_factor', 
    'lows_gain_db_s', 
    'highs_cutoff_frequency_hz', 
    'highs_q_factor', 
    'highs_gain_db_s',
    'fade_in_time_s', 
    #'fdn_size_internal'
    """
    #output = np.sum(param_dict*function_inputs)
    #error = 1.0 / np.abs(output - desired_output)
    if param_dict['room_size'] < 1.0: param_dict['room_size'] = 1.0
    if param_dict['room_size'] > 30.: param_dict['room_size'] = 30.
    if param_dict['reverberation_time_s'] < 0.1: param_dict['reverberation_time_s'] = 0.1
    if param_dict['reverberation_time_s'] > 9.0: param_dict['reverberation_time_s'] = 9.0
    if param_dict['lows_cutoff_frequency_hz'] < 20.: param_dict['lows_cutoff_frequency_hz'] = 20.
    if param_dict['lows_cutoff_frequency_hz'] > 20000.: param_dict['lows_cutoff_frequency_hz'] = 20000.
    if param_dict['lows_q_factor'] < 0.01: param_dict['lows_q_factor'] = 0.01
    if param_dict['lows_q_factor'] > 0.9 : param_dict['lows_q_factor'] = 0.9
    if param_dict['lows_gain_db_s'] < -80.: param_dict['lows_gain_db_s'] = -80.
    if param_dict['lows_gain_db_s'] > 6.0 : param_dict['lows_gain_db_s'] = 6.0
    if param_dict['highs_cutoff_frequency_hz'] < 20.: param_dict['highs_cutoff_frequency_hz'] = 20.
    if param_dict['highs_cutoff_frequency_hz'] > 20000.: param_dict['highs_cutoff_frequency_hz'] = 20000.
    if param_dict['highs_q_factor'] < 0.01: param_dict['highs_q_factor'] = 0.01
    if param_dict['highs_q_factor'] > 0.9: param_dict['highs_q_factor'] = 0.9
    if param_dict['highs_gain_db_s'] < -80: param_dict['highs_gain_db_s'] = -80.
    if param_dict['highs_gain_db_s'] > 4.0: param_dict['highs_gain_db_s'] = 4.0
    if param_dict['fade_in_time_s'] < 0.0: param_dict['fade_in_time_s'] = 0.0
    if param_dict['fade_in_time_s'] > 9.0: param_dict['fade_in_time_s'] = 9.0
    #if param_dict[9] < 16.0: param_dict[9] = 16.0
    #if param_dict[9] > 64.0: param_dict[9] = 64.0

    vst.room_size = param_dict['room_size'] #range [1.0, 30.0]
    vst.reverberation_time_s = param_dict['reverberation_time_s'] #range [0.1s, 9.0s]
    vst.lows_cutoff_frequency_hz = param_dict['lows_cutoff_frequency_hz'] # range [20.0Hz, 20000.0Hz]
    vst.lows_q_factor = param_dict['lows_q_factor']  # range [0.01, 0.9]
    vst.lows_gain_db_s = param_dict['lows_gain_db_s'] #range [-80.0dB/s, 6.0dB/s]
    vst.highs_cutoff_frequency_hz = param_dict['highs_cutoff_frequency_hz'] #range [20.0Hz, 20000.0Hz]
    vst.highs_q_factor = param_dict['highs_q_factor'] #range [0.01, 0.9]
    vst.highs_gain_db_s = param_dict['highs_gain_db_s'] #range [-80.0dB/s, 4.0dB/s]
    vst.fade_in_time_s = param_dict['fade_in_time_s'] # range [0.0s, 9.0s]
    #vst.fdn_size_internal = param_dict[9] # range [16.0, 64.0]
    
    output = vst(delta, rate)

    return output


def RT60(signal):

    signal = np.mean(signal, axis=0) #mono
    signal /= (np.max(signal)+0.000001) #normalizes

    rms = librosa.feature.rms(y=signal, frame_length = 128, hop_length = 64)[0]
    rms = np.array(rms)

    
    rms_len_in_seconds = 64 / rate #each RMS frame in seconds

    idxmax = rms.argmax()
    rmsmax = rms[idxmax]

    idx60_tuple = np.where(rms[idxmax:] <= rmsmax * 0.001) #0.001 <=> -60dB


    #if rt60 is longer than the length of the audio
    if len(idx60_tuple) == 0:
        return 6.

    try:
        idx60 = idx60_tuple[0][0]
    except:
        return 6.


    reverb_time = rms_len_in_seconds * idx60

    return reverb_time




def compare_RT60(file):

    original_path_to_file = original_path+file
    extracted_path_to_file = extracted_path+file
    
    original_audio, samplerate = sf.read(original_path_to_file)
    original_audio = np.array(original_audio).T
    audio_len = original_audio.shape[1]
    original_audio = np.pad(original_audio, ((0, 0), (0, 6 * rate - audio_len)), 'constant')

    #extracted_audio, samplerate = sf.read(extracted_path_to_file)
    #extracted_audio = np.array(extracted_audio).T
    #audio_len = extracted_audio.shape[1]
    #extracted_audio = np.pad(extracted_audio, ((0, 0), (0, 6 * rate - audio_len)), 'constant')

    json_file = file[:-4]+"-parameter.json"
    with open(extracted_path+json_file, 'r') as f:
        parameters = json.load(f)
    
    output = apply_reverb(parameters, vst, delta, rate)



    original_reverb_time = RT60(original_audio)
    extracted_reverb_time = RT60(output)

    print("original_reverb_time: ", original_reverb_time)
    print("extracted_reverb_time: ", extracted_reverb_time)
    error = np.abs(original_reverb_time - extracted_reverb_time)
    print("absolute error: ", error)

    reverb_time_error_dict[file] = error

    


    return None





#######################################################################################


vst = load_plugin('/Users/likelian/Desktop/Lab/Lab_spring2022/VST3/Mac/FdnReverb.vst3')
vst.dry_wet = 1.   #0. is 100% dry
vst.fdn_size_internal = 64 #GUI is more restricted on this parameter


rate = 48000
#delta signal to get the impluse response of the reverb
delta = np.zeros((2,  6 * rate))
delta[0][0] = 1.
delta[1][0] = 1.



original_path = "/Users/likelian/Desktop/Lab/Lab_spring2022/data/reverb_match_experiment/original/"
#original_path = '/Users/likelian/Desktop/Lab/Lab_spring2022/data/reverb_match_experiment/extracted/'
extracted_path = '/Users/likelian/Desktop/Lab/Lab_spring2022/data/reverb_match_experiment/output/'
reverb_time_error_dict = {}


for file in os.listdir(extracted_path):
        if ".wav" in file and file in os.listdir(extracted_path):
            print("  ")
            print("  ")
            print("  ")
            print(file)
            compare_RT60(file)
            

mean_reverb_time_error = np.mean(list(reverb_time_error_dict.values()))
#variance
#plot error distribution
print(" ")
print("mean_reverb_time_error: ", mean_reverb_time_error)
#with open(output_path + 'reverb_time_error.json', 'w') as fp:
#    json.dump(reverb_time_error_dict, fp)

