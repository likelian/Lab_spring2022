import numpy as np
import soundfile as sf
from pedalboard import Pedalboard, Reverb, load_plugin



tempo = 60

RT60 = -1.1*tempo + 136.1

print(RT60)


vst_path = "../VST3/"
vst_name = "FdnReverb.vst3"

read_path = "../../MIR-1K/UndividedWavfile/abjones_1.wav"


data, sample_rate = sf.read(read_path)


vst = load_plugin(vst_path + vst_name)

print(vst.parameters.keys())


vst.reverberation_time_s = 8.0
vst.dry_wet = 1.


data = vst(data, sample_rate)



sf.write('../audio/output/output.wav', data, sample_rate)

print(data)
