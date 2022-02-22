import numpy as np
import soundfile as sf
from os import walk
from pedalboard import Pedalboard, load_plugin
#import sys
#sys.path.append('/usr/local/lib/python3.8/site-packages')
#import essentia
#import essentia.standard



read_path = "../../MIR-1K/UndividedWavfile/"
#filename = "abjones_3.wav"
write_path = "../../Output/"

target_loudness_range = 0


def compression(read_path, target_loudness_range):
    """
    """
    f = []

    for (dirpath, dirnames, filenames) in walk(read_path):
        f.extend(filenames)
        break

    for filename in f:

        if ".wav" not in filename:
            continue

        data, rate = sf.read(read_path+filename) # load audio (with shape (samples, channels))

        acc = data.T[0]
        vox = data.T[1]


        vst_path = "/Library/Audio/Plug-Ins/VST3/"
        vst_name = "ValhallaVintageVerb.vst3"
        #vst_name = "TR5 White 2A.vst3"
        vst_name = "IEM/OmniCompressor.vst3"

        vst = load_plugin(vst_path + vst_name)

        print(vst.parameters.keys())

        threshold_db = -10.0 #range [-50.0dB, 10.0dB]
        threshold_db_str = str(threshold_db) + " dB"
        #vst.peak_reduction = peak_reduction_str
        vst.threshold_db = threshold_db

        #vst.mix = 100.

        #board = Pedalboard([vst])
        effected = vst(data, rate)
        print(effected)
        #print(data)


        sf.write('../audio/output/output.wav', effected, rate)


        break


    return None


compression(read_path, target_loudness_range)
