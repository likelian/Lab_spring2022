import numpy as np
import soundfile as sf
from pedalboard import Pedalboard, Reverb, load_plugin



tempo = 60

RT60 = -1.1*tempo + 136.1

print(RT60)


vst_path = "../VST3/"
vst_name = "FdnReverb.vst3"
#vst_name = "TR5 White 2A.vst3"
audioRead_path = "../audio/input/sweep.wav"

data, sample_rate = sf.read(audioRead_path)



vst = load_plugin(vst_path + vst_name)

print(vst.parameters.keys())


data = vst(data, sample_rate)


print(data)
