import numpy as np
import soundfile as sf
from os import walk
from mixer import mixer



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

    print(rate)

    mixer_one = mixer()

    mixer_one.load_acc(acc)
    mixer_one.load_vox(vox)

    mixer_one.set_sampleRate(rate)


    #random EQ
    mixer_one.random_EQ()
    quit()
    #random Comp
    #random Reverb
    #random Level


    mix = mixer_one.get_mix()
    sf.write(write_path + foldername + "-rand.wav", mix, rate)





