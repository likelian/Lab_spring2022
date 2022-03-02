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


vst.room_size = 20
vst.reverberation_time_s = 4.0
vst.dry_wet = .70

# set other parameters to default
vst.lows_gain_db_s = 0.
vst.highs_gain_db_s = 0.
vst.fade_in_time_s = 0.01
vst.fdn_size_internal = 64



data = vst(data, sample_rate)



sf.write('../audio/output/output.wav', data, sample_rate)

print(data)
