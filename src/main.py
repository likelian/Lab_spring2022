import numpy as np
import soundfile as sf
from os import walk
from mixer import mixer



read_path = "../../MIR-1K/UndividedWavfile/"
write_path = "../../Output/"


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

    mixer_one = mixer()

    mixer_one.load_acc(acc)
    mixer_one.load_vox(vox)

    mixer_one.set_sampleRate(rate)

    mixer_one.set_target_vox_acc_ratio(-0.5)
    mixer_one.set_targetLRA(14)

    vox = mixer_one.process()
    
    mix = mixer_one.mix()

    break
