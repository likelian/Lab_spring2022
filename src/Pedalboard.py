import soundfile as sf
from pedalboard import Pedalboard, Reverb, load_plugin

# Load a VST3 or Audio Unit plugin from a known path on disk:


vst_path = "/Library/Audio/Plug-Ins/VST3/"

vst = load_plugin(vst_path+"ValhallaVintageVerb.vst3")

print(vst.parameters.keys())
# dict_keys([
#   'sc_hpf_hz', 'input_lvl_db', 'sensitivity_db',
#   'ratio', 'attack_ms', 'release_ms', 'makeup_db',
#   'mix', 'output_lvl_db', 'sc_active',
#   'full_bandwidth', 'bypass', 'program',
# ])

# Set the "ratio" parameter to 15
vst.mix = 100.

# Use this VST to process some audio:
audio, sample_rate = sf.read('../audio/input/sweep.wav')
effected = vst(audio, sample_rate)

# ...or put this VST into a chain with other plugins:
board = Pedalboard([vst, Reverb()])
# ...and run that pedalboard with the same VST instance!
effected = board(audio, sample_rate)

sf.write('../audio/output/guitar-output.wav', effected, sample_rate)
