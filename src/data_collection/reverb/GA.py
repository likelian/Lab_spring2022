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
    'fdn_size_internal'
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
    if solution[9] < 16.0: solution[9] = 16.0
    if solution[9] > 64.0: solution[9] = 64.0

    vst.room_size = solution[0] #range [1.0, 30.0]
    vst.reverberation_time_s = solution[1] #range [0.1s, 9.0s]
    vst.lows_cutoff_frequency_hz = solution[2] # range [20.0Hz, 20000.0Hz]
    vst.lows_q_factor = solution[3]  # range [0.01, 0.9]
    vst.lows_gain_db_s = solution[4] #range [-80.0dB/s, 6.0dB/s]
    vst.highs_cutoff_frequency_hz = solution[5] #range [20.0Hz, 20000.0Hz]
    vst.highs_q_factor = solution[6] #range [0.01, 0.9]
    vst.highs_gain_db_s = solution[7] #range [-80.0dB/s, 4.0dB/s]
    vst.fade_in_time_s = solution[8] # range [0.0s, 9.0s]
    vst.fdn_size_internal = solution[9] # range [16.0, 64.0]
    
    output = vst(delta, rate)

    return output



def fitness_func(solution, solution_idx):

    output = apply_reverb(solution, vst, delta, rate)

    f, t, output_Sxx = signal.spectrogram(output, rate)

    error = np.mean(np.abs(output_Sxx - Sxx)) #minimize the error
    fitness = 1.0 / error #maximize the fitness

    print(fitness)
    print(" ")

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

    num_generations = 1
    num_parents_mating = 4

    sol_per_pop = 8
    num_genes = 10

    init_range_low = -2
    init_range_high = 5

    parent_selection_type = "sss"
    keep_parents = 1

    crossover_type = "single_point"

    mutation_type = "random"
    mutation_percent_genes = 10


    ga_instance = pygad.GA(num_generations=num_generations,
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
                           mutation_percent_genes=mutation_percent_genes)

    ga_instance.run()


    solution, solution_fitness, solution_idx = ga_instance.best_solution()
    print("Parameters of the best solution : {solution}".format(solution=solution))
    print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))

    return solution





def evolve(dataset_path, filename):
    input_audio_path = dataset_path + filename
    input_audio, rate = sf.read(input_audio_path)
    input_audio = np.array(input_audio).T
    audio_len = input_audio.shape[1]


    #make the delta signal and the original IR audio the same length
    input_audio = np.pad(input_audio, ((0, 0), (0, 6 * rate - audio_len)), 'constant')


    f, t, Sxx = signal.spectrogram(input_audio, rate)
    plt.pcolormesh(t, f, Sxx[0], shading='gouraud')
    plt.savefig(plot_path + filename + ".png")
    plt.close()


    solution = reverb_search(fitness_func, Sxx)


    output = apply_reverb(solution, vst, delta, rate)
    f, t, output_Sxx = signal.spectrogram(output, rate)

    """
    #write out the audio from outuput
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    """

    plt.pcolormesh(t, f, output_Sxx[0], shading='gouraud')
    plt.savefig(plot_path + filename + "-output" + ".png")
    plt.close()



#path to save the plot
plot_path = '/Users/likelian/Desktop/Lab/Lab_spring2022/results/reverb matching/'

vst = load_plugin('/Users/likelian/Desktop/Lab/Lab_spring2022/VST3/Mac/FdnReverb.vst3')
vst.dry_wet = 1.   #0. is 100% dry

dataset_path = "/Users/likelian/Desktop/Lab/Lab_spring2022/data/IRs/test/"


rate = 48000
#delta signal to get the impluse response of the reverb
delta = np.zeros((2,  6 * rate))
delta[0][0] = 1.
delta[1][0] = 1.


for file in os.listdir(dataset_path):
        if ".wav" in file:
            evolve(dataset_path, file)

            print(file)



