import numpy as np
import soundfile as sf
from os import walk
import sys
sys.path.append('/usr/local/lib/python3.8/site-packages')
import essentia
import essentia.standard



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


        hop_size = 0.1

        LoudnessEBUR128 = essentia.standard.LoudnessEBUR128(sampleRate=rate, hopSize=hop_size)
        """
        LoudnessEBUR128 Outputs:
            momentaryLoudness (vector_real) - momentary loudness (over 400ms) (LUFS)
            shortTermLoudness (vector_real) - short-term loudness (over 3 seconds) (LUFS)
            integratedLoudness (real) - integrated loudness (overall) (LUFS)
            loudnessRange (real) - loudness range over an arbitrary long time interval [3] (dB, LU)
        """

        shortTermLoudness = LoudnessEBUR128(data)[1][:-1].T[:, np.newaxis]
        loudnessRange = LoudnessEBUR128(data)[3]

        print(loudnessRange)



        break


    return None


compression(read_path, target_loudness_range)
