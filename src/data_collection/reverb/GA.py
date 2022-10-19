"""
https://pygad.readthedocs.io/en/latest/
"""

import pygad
import numpy as np
from pedalboard import Pedalboard, load_plugin



function_inputs = [4,-2,3.5,5,-11,-4.7]
desired_output = 44



vst = load_plugin('/Users/likelian/Desktop/Lab/Lab_spring2022/VST3/Mac/FdnReverb.vst3')





def fitness_func(solution, solution_idx):
    """
    """
    output = np.sum(solution*function_inputs)
    error = 1.0 / np.abs(output - desired_output)




    
    vst.room_size = 30
    vst.reverberation_time_s = 1.
    vst.dry_wet = 1.   #0. is 100% dry

    # set other parameters to default
    vst.lows_gain_db_s = 0.
    vst.highs_gain_db_s = 0.
    vst.fade_in_time_s = 0.2
    vst.fdn_size_internal = 64
    #there are more values to be set, print the list
    
    
    return error


fitness_function = fitness_func

num_generations = 50
num_parents_mating = 4

sol_per_pop = 8
num_genes = len(function_inputs)

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
