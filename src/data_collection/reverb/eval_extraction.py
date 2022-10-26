"""
https://pygad.readthedocs.io/en/latest/
"""

import pygad
import numpy as np
from pedalboard import Pedalboard, load_plugin
import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
import os
import librosa
import json




def save_param(solution):
    """
    save the solution to a dictionary
    """
    if solution[0] < 1.0: solution[0] = 1.0
    if solution[0] > 30.: solution[0] = 30.
    if solution[1] < 0.1: solution[1] = 0.1
    if solution[1] > 9.0: solution[1] = 9.0
    if solution[2] < 20.: solution[2] = 20.
    if solution[2] > 20000.: solution[2] = 20000.
    if solution[3] < 0.01: solution[3] = 0.01
    if solution[3] > 0.9: solution[3] = 0.9
    if solution[4] < -80.: solution[4] = -80.
    if solution[4] > 6.0: solution[4] = 6.0
    if solution[5] < 20.: solution[5] = 20.
    if solution[5] > 20000.: solution[5] = 20000.
    if solution[6] < 0.01: solution[6] = 0.01
    if solution[6] > 0.9: solution[6] = 0.9
    if solution[7] < -80: solution[7] = -80.
    if solution[7] > 4.0: solution[7] = 4.0
    if solution[8] < 0.0: solution[8] = 0.0
    if solution[8] > 9.0: solution[8] = 9.0
    #if solution[9] < 16.0: solution[9] = 16.0
    #if solution[9] > 64.0: solution[9] = 64.0

    param_dict = {}

    param_dict['room_size'] = solution[0]
    param_dict['reverberation_time_s'] = solution[1]
    param_dict['lows_cutoff_frequency_hz'] = solution[2]
    param_dict['lows_q_factor'] = solution[3]
    param_dict['lows_gain_db_s'] = solution[4]
    param_dict['highs_cutoff_frequency_hz'] = solution[5]
    param_dict['highs_q_factor'] = solution[6]
    param_dict['highs_gain_db_s'] = solution[7]
    param_dict['fade_in_time_s'] = solution[8]
    #param_dict['fdn_size_internal'] = solution[9]

    return param_dict

    
    



def apply_reverb(solution, vst, delta, rate):
    """
    render the audio from given parameters in solution

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
    #output = np.sum(solution*function_inputs)
    #error = 1.0 / np.abs(output - desired_output)
    if solution[0] < 1.0: solution[0] = 1.0
    if solution[0] > 30.: solution[0] = 30.
    if solution[1] < 0.1: solution[1] = 0.1
    if solution[1] > 9.0: solution[1] = 9.0
    if solution[2] < 20.: solution[2] = 20.
    if solution[2] > 20000.: solution[2] = 20000.
    if solution[3] < 0.01: solution[3] = 0.01
    if solution[3] > 0.9: solution[3] = 0.9
    if solution[4] < -80.: solution[4] = -80.
    if solution[4] > 6.0: solution[4] = 6.0
    if solution[5] < 20.: solution[5] = 20.
    if solution[5] > 20000.: solution[5] = 20000.
    if solution[6] < 0.01: solution[6] = 0.01
    if solution[6] > 0.9: solution[6] = 0.9
    if solution[7] < -80: solution[7] = -80.
    if solution[7] > 4.0: solution[7] = 4.0
    if solution[8] < 0.0: solution[8] = 0.0
    if solution[8] > 9.0: solution[8] = 9.0
    #if solution[9] < 16.0: solution[9] = 16.0
    #if solution[9] > 64.0: solution[9] = 64.0

    vst.room_size = solution[0] #range [1.0, 30.0]
    vst.reverberation_time_s = solution[1] #range [0.1s, 9.0s]
    vst.lows_cutoff_frequency_hz = solution[2] # range [20.0Hz, 20000.0Hz]
    vst.lows_q_factor = solution[3]  # range [0.01, 0.9]
    vst.lows_gain_db_s = solution[4] #range [-80.0dB/s, 6.0dB/s]
    vst.highs_cutoff_frequency_hz = solution[5] #range [20.0Hz, 20000.0Hz]
    vst.highs_q_factor = solution[6] #range [0.01, 0.9]
    vst.highs_gain_db_s = solution[7] #range [-80.0dB/s, 4.0dB/s]
    vst.fade_in_time_s = solution[8] # range [0.0s, 9.0s]
    #vst.fdn_size_internal = solution[9] # range [16.0, 64.0]
    
    output = vst(delta, rate)

    return output



def fitness_func(solution, solution_idx):

    output = apply_reverb(solution, vst, delta, rate)

    f, t, output_Sxx = signal.spectrogram(output, rate)

    error = np.mean(np.abs(output_Sxx - Sxx)) #minimize the error

    error += 0.1 * np.abs(solution[1] - input_reverb_time_global)

    #avoid overflow
    #while error < 0.000000001:
    #    error *= 10.

    fitness = 1.0 / error #maximize the fitness

    #print(fitness)
    #print(" ")

    return fitness




def reverb_search(fitness_func, Sxx_local):

    """
    Sxx: the spectrogram of the input audio
    """

    #Sxx needs to be used in fitness_func, but fitness_func is defined by the package
    #Setting Sxx to be a global variable allowing fitness_func to use Sxx
    global Sxx 
    Sxx = Sxx_local

    fitness_function = fitness_func

    num_generations = 10
    num_parents_mating = 4

    sol_per_pop = 10
    num_genes = 9
    initial_population = [
        [15., 2., 100., 1., -10., 10000., 1., -10., 0.1], 
        [10., 1., 200., 1.1, -15., 11000., 1.1, -20., 0.2],
        [5., 3., 50., 1.2, -1., 12000., 1.2, -5., 0.3],
        [15., 2., 120., 1.3, -2., 13000., 1.3, -4., 0.4],
        [10., 1.5, 80., 1.3, -3., 14000., 1.4, -3., 0.5],
        [5., 2., 100., 1.4, -4., 15000., 1.5, -6., 0.1],
        [30., 0.5, 150., 1.5, -5., 16000., 1.6, -8., 0.2],
        [25., 0.2, 60., 1.6, 1., 17000., 1.7, -12., 0.3],
        [20., 1., 50., 1.7, 2., 9000., 1.8, -15., 0.4],
        [15., 2., 150., 1., 3., 8000., 1.9, -20., 0.5]
        ]

    init_range_low = 0
    init_range_high = 2

    parent_selection_type = "sss"
    keep_parents = 1

    crossover_type = "single_point"

    mutation_type = "random"
    #mutation_percent_genes = 10 # %
    #mutation_percent_genes = 0.5
    mutation_num_genes = 2


    ga_instance = pygad.GA(num_generations=num_generations,
                           initial_population=initial_population,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           init_range_low=init_range_low,
                           init_range_high=init_range_high,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           #mutation_percent_genes=mutation_percent_genes,
                           mutation_num_genes=mutation_num_genes
                           )

    ga_instance.run()


    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print("Parameters of the best solution : {solution}".format(solution=solution))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

    return solution


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




def evolve(dataset_path, filename):
    input_audio_path = dataset_path + filename
    input_audio, rate = sf.read(input_audio_path)
    input_audio = np.array(input_audio).T
    audio_len = input_audio.shape[1]


    #make the delta signal and the original IR audio the same length
    input_audio = np.pad(input_audio, ((0, 0), (0, 6 * rate - audio_len)), 'constant')

    global input_reverb_time_global
    input_reverb_time = RT60(input_audio)
    input_reverb_time_global = input_reverb_time

    try:
        f, t, Sxx = signal.spectrogram(input_audio, rate)
    except:
        print("something wrong with spectrogram")
        return None
    


    plt.pcolormesh(t, f, Sxx[0], shading='gouraud')
    plt.savefig(output_path + filename[:-4] + ".png")
    plt.close()

    solution = reverb_search(fitness_func, Sxx)

    output = apply_reverb(solution, vst, delta, rate)
    f, t, output_Sxx = signal.spectrogram(output, rate)

    MAE = np.mean(np.abs(output_Sxx - Sxx))
    print("MAE: ", MAE)


    #calcuate RT60, get the error, print and add the error to a json file
    
    output_reverb_time = RT60(output)
    reverb_time_error = np.abs(input_reverb_time - output_reverb_time)
    print("input_reverb_time: ", input_reverb_time)
    print("output_reverb_time: ", output_reverb_time)
    print("reverb_time_error: ", reverb_time_error)
    reverb_time_error_dict[filename[:-4]] = reverb_time_error


    #save the parameters found to a json file
    param_dict = save_param(solution)
    with open(output_path + filename[:-4] + '-parameter.json', 'w') as fp:
        json.dump(param_dict, fp)



    sf.write(output_path + filename, output.T, rate)

    plt.pcolormesh(t, f, output_Sxx[0], shading='gouraud')
    plt.savefig(output_path + filename[:-4] + "-output" + ".png")
    plt.close()




#######################################################################################


vst = load_plugin('/Users/likelian/Desktop/Lab/Lab_spring2022/VST3/Mac/FdnReverb.vst3')
vst.dry_wet = 1.   #0. is 100% dry
vst.fdn_size_internal = 64 #GUI is more restricted on this parameter

rate = 48000
#delta signal to get the impluse response of the reverb
delta = np.zeros((2,  6 * rate))
delta[0][0] = 1.
delta[1][0] = 1.




dataset_path = "/Users/likelian/Desktop/Lab/Lab_spring2022/data/IRs/test/"
output_path = '/Users/likelian/Desktop/Lab/Lab_spring2022/results/reverb matching/test/'
reverb_time_error_dict = {}

counter = 0

for file in os.listdir(dataset_path):
        if ".wav" in file and file not in os.listdir(output_path):
            print("  ")
            print("  ")
            print("  ")
            print(file)
            evolve(dataset_path, file)
            

mean_reverb_time_error = np.mean(list(reverb_time_error_dict.values()))
print("mean_reverb_time_error: ", mean_reverb_time_error)
with open(output_path + 'reverb_time_error.json', 'w') as fp:
    json.dump(reverb_time_error_dict, fp)



dataset_path = "/Users/likelian/Desktop/Lab/Lab_spring2022/data/IRs/train/"
output_path = '/Users/likelian/Desktop/Lab/Lab_spring2022/results/reverb matching/train/'
reverb_time_error_dict = {}

for file in os.listdir(dataset_path):
        if ".wav" in file and file not in os.listdir(output_path):
            print("  ")
            print("  ")
            print("  ")
            print(file)
            evolve(dataset_path, file)

mean_reverb_time_error = np.mean(list(reverb_time_error_dict.values()))
print("mean_reverb_time_error: ", mean_reverb_time_error)
with open(output_path + 'reverb_time_error.json', 'w') as fp:
    json.dump(reverb_time_error_dict, fp)

