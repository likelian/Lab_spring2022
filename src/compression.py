import numpy as np
import soundfile as sf
from os import walk
from pedalboard import Pedalboard, load_plugin
import loudness


read_path = "../../MIR-1K/UndividedWavfile/"
write_path = "../../Output/"



def compression(read_path, targetLRA):
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

        signal_mono = vox
        vox = np.array([signal_mono, signal_mono]).T


        vst_path = "../VST3/"
        vst_name = "ValhallaVintageVerb.vst3"
        #vst_name = "TR5 White 2A.vst3"
        vst_name = "OmniCompressor.vst3"

        vst = load_plugin(vst_path + vst_name)

        #print(vst.parameters.keys())


        LRA = loudness.LoudnessRange(vox, rate, overlapSize = 0.1)

        print("LRA", LRA)

        threshold_db = 10.0 #range [-50.0dB, 10.0dB]

        makeup_gain_db = 0.
        for i in np.arange(10):

            threshold_db -= 5.0
            threshold_db_str = str(threshold_db) + " dB"
            vst.normalization = "N3D"
            vst.threshold_db = threshold_db
            vst.ratio_1 = 3.
            vst.attack_time_ms = 50.
            vst.release_time_ms = 500.
            vst.makeup_gain_db += 1.

            output = vst(vox, rate)

            LRA = loudness.LoudnessRange(output, rate, overlapSize = 0.1)
            print("threshold_dbs", threshold_db)
            print("loudnessRange", LRA)
            print("target_loudness_range", targetLRA)

            if (LRA - targetLRA) < 1.0:
                break


        sf.write('../audio/output/output.wav', output, rate)



    return None


targetLRA = 14

compression(read_path, targetLRA)
