import numpy as np
import soundfile as sf
from os import walk
from mixer import mixer
import json



read_path = "/Users/likelian/Desktop/Lab/Lab_spring2022/audio/input/"
write_path = "/Users/likelian/Desktop/Lab/Lab_spring2022/audio/output/"

counter = 0
f_1 = []
for (dirpath, dirnames, filenames) in walk(read_path):


    acc_path = None
    vox_path = None

    for file in filenames:
        if "background.wav" in file:
            acc_path = dirpath+"/"+file
            print(acc_path)
        
        if "vocal.wav" in file:
            vox_path = dirpath+"/"+file
            print(vox_path)

    if acc_path is None or vox_path is None:
        continue
    
    foldername = dirpath[dirpath.rfind('/')+1:]

    acc, rate = sf.read(acc_path)
    vox, rate = sf.read(vox_path)

    #print(rate)

    mixer_one = mixer()

    mixer_one.load_acc(acc)
    mixer_one.load_vox(vox)

    mixer_one.set_sampleRate(rate)

    mixer_one.set_target_vox_acc_ratio(-1.77)
    mixer_one.param_dict["relative_loudness"] = -1.77

    mixer_one.checkShape()
    mixer_one.call_level_balance()
    mixer_one.call_EQ()
    mixer_one.set_targetLRA(16.4)
    mixer_one.call_Comp()
    mixer_one.call_Reverb()
    mixer_one.call_Level_Balance()

    mix = mixer_one.get_mix()

    sf.write(write_path + foldername + "-rule.wav", mix, rate)

    print(mixer_one.param_dict)

    #with open(write_path + 'json/' + foldername + '-rule.txt', 'w') as f:
    #    json.dump(mixer_one.param_dict, f, indent=2)





