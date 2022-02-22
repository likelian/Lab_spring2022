import soundfile as sf
from pedalboard import Pedalboard, Reverb, load_plugin


#vst_path = "/Library/Audio/Plug-Ins/VST3/"
#vst_name = "ValhallaVintageVerb.vst3"
#vst_name = "TR5 White 2A.vst3"
#audioRead_path = "../audio/input/sweep.wav"
audio, sample_rate = sf.read(audioRead_path)

def effect(audio, sample_rate, vst_path, vst_name):
    """
    """


    vst = load_plugin(vst_path + vst_name)

    print(vst.parameters.keys())
    # dict_keys([
    #   'sc_hpf_hz', 'input_lvl_db', 'sensitivity_db',
    #   'ratio', 'attack_ms', 'release_ms', 'makeup_db',
    #   'mix', 'output_lvl_db', 'sc_active',
    #   'full_bandwidth', 'bypass', 'program',
    # ])

    # Set the "ratio" parameter to 15
    #vst.mix = 100.

    # Use this VST to process some audio:

    effected = vst(audio, sample_rate)

    # ...or put this VST into a chain with other plugins:
    board = Pedalboard([vst, Reverb()])
    # ...and run that pedalboard with the same VST instance!
    effected = board(audio, sample_rate)

    #sf.write('../audio/output/guitar-output.wav', effected, sample_rate)

    return effected
