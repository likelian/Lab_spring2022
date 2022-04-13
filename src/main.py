import numpy as np
import soundfile as sf
from os import walk
from mixer import mixer
#sfrom pydub import AudioSegment



read_path = "../../DAMP-VSEP/"
write_path = "../../Output/"

counter = 0
f_1 = []
for (dirpath, dirnames, filenames) in walk(read_path):

    #if  "mix.m4a" in filenames \
    #    and "background.m4a" in filenames \
    #    and "vocal.ogg" in filenames:
    if "untitled-001.wav" in filenames \
        and "untitled-002.wav" in filenames \
        and "mix.m4a" in filenames:

        #acc_path = dirpath+"/background.m4a"
        #vox_path = dirpath+"/vocal.ogg"
        acc_path = dirpath+"/untitled-001.wav"
        vox_path = dirpath+"/untitled-002.wav"

    else:
        continue

    #print(acc_path)
    print(vox_path)


    #audio = AudioSegment.from_file(acc_path)
    #arrayarray = audio.get_array_of_samples()
    #acc = np.array(arrayarray, dtype=np.float32).reshape((-1, audio.channels)) / (
    #        1 << (8 * audio.sample_width - 1))


    acc, rate = sf.read(acc_path)
    vox, rate = sf.read(vox_path)

    print(rate)

    mixer_one = mixer()

    mixer_one.load_acc(acc)
    mixer_one.load_vox(vox)

    mixer_one.set_sampleRate(rate)

    mixer_one.set_target_vox_acc_ratio(-0.5)
    mixer_one.set_targetLRA(15)

    mix = mixer_one.get_mix()


    write_name = dirpath[16:].replace("/", "-")
    sf.write("../audio/output/" + write_name + "-original.wav", mix, rate)

    vox = mixer_one.process()

    mix = mixer_one.get_mix()
    sf.write("../audio/output/" + write_name + "-mix.wav", mix, rate)


    #if counter == 4:
    #    break
    #break
    counter += 1






"""
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
"""
