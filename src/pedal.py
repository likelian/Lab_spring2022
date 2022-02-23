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


    effected = vst(audio, sample_rate)

    board = Pedalboard([vst, Reverb()])
    # ...and run that pedalboard with the same VST instance!
    effected = board(audio, sample_rate)

    #sf.write('../audio/output/guitar-output.wav', effected, sample_rate)

    return effected
