import numpy as np
import librosa
from pedalboard import Pedalboard, load_plugin


def reverb(self):

    rate = self.sampleRate
    acc = self.acc
    vox = self.vox

    onset_env = librosa.onset.onset_strength(acc, rate)
    tempo = librosa.beat.tempo(onset_env, rate)

    RT = (-1/45) * tempo + (40/9)

    vst_path = "../VST3/"
    vst_name = "FdnReverb.vst3"

    vst = load_plugin(vst_path + vst_name)

    vst.room_size = 20
    vst.reverberation_time_s = RT
    vst.dry_wet = .25   #0. is 100% dry

    # set other parameters to default
    vst.lows_gain_db_s = 0.
    vst.highs_gain_db_s = 0.
    vst.fade_in_time_s = 0.01
    vst.fdn_size_internal = 64

    output = vst(vox, rate)

    self.vox = output
