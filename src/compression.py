import numpy as np
import soundfile as sf
from os import walk
from pedalboard import Pedalboard, load_plugin
import sys

sys.path.append('/usr/local/lib/python3.8/site-packages')
import essentia
import essentia.standard




read_path = "../../MIR-1K/UndividedWavfile/"
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


        vst_path = "../VST3/"
        vst_name = "ValhallaVintageVerb.vst3"
        #vst_name = "TR5 White 2A.vst3"
        vst_name = "OmniCompressor.vst3"

        vst = load_plugin(vst_path + vst_name)

        print(vst.parameters.keys())


        #shortTermLoudness = LoudnessEBUR128(data)[1][:-1].T[:, np.newaxis]

        hop_size = 0.1
        LoudnessEBUR128 = essentia.standard.LoudnessEBUR128(sampleRate=rate, hopSize=hop_size)

        loudnessRange = LoudnessEBUR128(data)[3]
        print(loudnessRange)

        for i in np.arange(5):

            threshold_db = -10.0 #range [-50.0dB, 10.0dB]
            threshold_db_str = str(threshold_db) + " dB"
            #vst.peak_reduction = peak_reduction_str
            vst.threshold_db = threshold_db

            data = vst(data, rate)

            loudnessRange = LoudnessEBUR128(data)[3]
            print("loudnessRange", loudnessRange)
            Print("target_loudness_range", target_loudness_range)





        break

        sf.write('../audio/output/output.wav', effected, rate)





    return None


compression(read_path, target_loudness_range)
