"""
https://pygad.readthedocs.io/en/latest/
"""

import pygad
import numpy as np
from pedalboard import Pedalboard, load_plugin




#function_inputs = [4,-2,3.5,5,-11,-4.7]
#desired_output = 44



vst = load_plugin('/Users/likelian/Desktop/Lab/Lab_spring2022/VST3/Mac/FdnReverb.vst3')
vst.dry_wet = 1.   #0. is 100% dry




def fitness_func(solution, solution_idx):
    """
    """
    #output = np.sum(solution*function_inputs)
    #error = 1.0 / np.abs(output - desired_output)
    
    """
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
    
    
    

    #output = vst(delta, rate)

    #limited the parameter range
    #normalize the output and the targeted extracted_IR
    #error = spectral_loss(output, extracted_IR)


    quit()

    
    return error







fitness_function = fitness_func

num_generations = 50
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

prediction = np.sum(np.array(function_inputs)*solution)
print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))
