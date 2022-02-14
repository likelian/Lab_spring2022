import numpy as np
import soundfile as sf
import pyloudnorm as pyln
from os import walk




read_path = "../../MIR-1K/UndividedWavfile/"
#filename = "abjones_3.wav"
write_path = "../../Output/"
target_vox_acc_ratio = -0.5

def level_balance(read_path, target_vox_acc_ratio):

    f = []
    for (dirpath, dirnames, filenames) in walk(read_path):
        f.extend(filenames)
        break


    #vox_mix_ratio_list = np.zeros(len(f))

    for filename in f:

        if ".wav" not in filename:
            continue

        data, rate = sf.read(read_path+filename) # load audio (with shape (samples, channels))

        acc = data.T[0]
        vox = data.T[1]
        mix = acc + vox
        #MIR-1K has the backing track on the left and the vocal track on the right

        meter = pyln.Meter(rate) # create BS.1770 meter
        acc_loudness = meter.integrated_loudness(acc) # measure loudness
        vox_loudness = meter.integrated_loudness(vox) # measure loudness
        mix_loudness = meter.integrated_loudness(mix) # measure loudness

        vox_acc_ratio = vox_loudness - acc_loudness
        vox_mix_ratio = vox_loudness - mix_loudness

        """
        print("acc_loudness", acc_loudness)
        print("vox_loudness", vox_loudness)
        print("mix_loudness", mix_loudness)
        print("vox_acc_ratio", vox_acc_ratio)
        print("vox_mix_ratio", vox_mix_ratio)
        """

        dB = target_vox_acc_ratio - vox_acc_ratio
        gain = 10**(dB/20)
        vox *= gain
        mix = acc + vox

        acc_loudness = meter.integrated_loudness(acc) # measure loudness
        vox_loudness = meter.integrated_loudness(vox) # measure loudness
        mix_loudness = meter.integrated_loudness(mix) # measure loudness

        vox_acc_ratio = vox_loudness - acc_loudness
        vox_mix_ratio = vox_loudness - mix_loudness

        total += vox_mix_ratio
        count += 1

        vox_mix_ratio_list[count] = vox_mix_ratio

        #print("vox_mix_ratio", vox_mix_ratio)

        """
        print("acc_loudness", acc_loudness)
        print("vox_loudness", vox_loudness)
        print("mix_loudness", mix_loudness)
        print("vox_acc_ratio", vox_acc_ratio)
        print("vox_mix_ratio", vox_mix_ratio)
        """

        #sf.write(write_path+filename, mix, rate) # load audio (with shape (samples, channels))

    #print(vox_mix_ratio_list)
    #print("average", np.average(vox_mix_ratio_list))
    #print("variance", np.var(vox_mix_ratio_list))

    average = total / count
    print("average vox_mix_ratio after changing the gain", average)



level_balance(read_path, target_vox_acc_ratio)
