import soundfile as sf
import numpy as np
import sys
from os import walk
import json
import os
#sys.path.append('..')
#import loudness
#https://github.com/deeuu/loudness this library is not academically reviewed
import pyloudnorm as pyln


################################################################################################################

def relative_loundness_MUSDB(abs_audio_path):

    #abs_audio_path = os.path.abspath(audio_path)

    #abs_audio_path = "/home/kli421/dir1/musdb18hq/train"
    
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

        print("mxiture_path", mxiture_path)
        #print("vox_path", vox_path)
        if mxiture.size > vox.size:
            mxiture = mxiture[:vox.size]
        if vox.size > mxiture.size:
            vox = vox[:mxiture.size]

        #ignore the ones than don't match in length
        #if mxiture.size != vox.size:
        #    continue

        acc = mxiture - vox


        meter = pyln.Meter(sampleRate) # create BS.1770 meter

        
        path_str = str(dirpath)
        index = path_str.rfind('/')
        filename = path_str[index+1:]

        for i in range(int(acc.shape[0] / 32768)):
            acc_loudness = meter.integrated_loudness(acc[i * 32768 : i*32768+65536])
            vox_loudness = meter.integrated_loudness(vox[i * 32768 : i*32768+65536])

            if not np.isfinite(acc_loudness) or not np.isfinite(vox_loudness):
                vox_acc_ratio = np.asarray(np.nan)
            else:
                vox_acc_ratio = vox_loudness - acc_loudness

            ground_truth[filename+"--i--"+str(i)+"--vox_acc_ratio"] = vox_acc_ratio.tolist()



    ground_truth_path = "../../data/vox_acc_ratio"
    abs_ground_truth_path = os.path.abspath(ground_truth_path)
    with open(abs_ground_truth_path + "/vox_acc_ratio.json", 'w') as outfile:
        json.dump(ground_truth, outfile)



################################################################################################################



relative_loundness_MUSDB("/home/kli421/dir1/musdb18hq/test")
