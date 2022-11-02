import soundfile as sf
import numpy as np
import sys
from os import walk
import json
import os
#sys.path.append('..')
#import loudness
import pyloudnorm as pyln


################################################################################################################

def relative_loundness_MUSDB(audio_path = "../../../Audio/musdb18hq/train/"):


    abs_audio_path = os.path.abspath(audio_path)

    ground_truth = {}

    for (dirpath, dirnames, filenames) in walk(abs_audio_path):


        if "mixture.wav" in filenames \
            and "vocals.wav" in filenames:

            mxiture_path = dirpath+"/mixture.wav"
            vox_path = dirpath+"/vocals.wav"
            #print(vox_path)

        else:
            continue

        mxiture, sampleRate = sf.read(mxiture_path)
        vox, sampleRate = sf.read(vox_path)

        acc = mxiture - vox

        meter = pyln.Meter(sampleRate) # create BS.1770 meter

        #alternative: blocked-based loudness
        #acc_loudness = loudness.shortTermLoudness(acc, sampleRate, overlapSize = 3.0)
        #vox_loudness = loudness.shortTermLoudness(vox, sampleRate, overlapSize = 3.0)

        acc_loudness = meter.integrated_loudness(acc)
        vox_loudness = meter.integrated_loudness(vox)
        #print("acc_loudness", acc_loudness)
        #print("vox_loudness", vox_loudness)


        vox_acc_ratio = vox_loudness - acc_loudness



        path_str = str(dirpath)
        index = path_str.rfind('/')
        filename = path_str[index+1:]
        ground_truth[filename+"--vox_acc_ratio"] = vox_acc_ratio.tolist()


        #print(ground_truth)

        #break


    ground_truth_path = "../../data/vox_acc_ratio"
    abs_ground_truth_path = os.path.abspath(ground_truth_path)
    with open(abs_ground_truth_path + "/vox_acc_ratio.json", 'w') as outfile:
        json.dump(ground_truth, outfile)



################################################################################################################



relative_loundness_MUSDB("/Volumes/mix/Dataset/musdb18hq/train")
