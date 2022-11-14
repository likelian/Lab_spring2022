import numpy as np
import librosa
from pedalboard import Pedalboard, load_plugin



def randVerb(self):

    rate = self.sampleRate
    vox = self.vox

    if len(vox.shape) != 2:
        vox = np.array([vox, vox]).T

    
    vst_path = "../VST3/"
    vst_name = "FdnReverb.vst3"
    vst = load_plugin(vst_path + vst_name)

    
    vst.room_size = np.random.rand() * 29. + 1. #[1.0, 30.0]
    self.param_dict["room_size"] = vst.room_size

    vst.reverberation_time_s = np.random.rand() * 8.9 + 0.1 #[0.1s, 9.0s]
    self.param_dict["reverberation_time_s"] = vst.reverberation_time_s

    vst.lows_cutoff_frequency_hz = np.random.rand() * 19980. + 20. #[20.0Hz, 20000.0Hz]
    self.param_dict["lows_cutoff_frequency_hz"] = vst.lows_cutoff_frequency_hz

    vst.lows_q_factor = np.random.rand() * 0.89 + 0.01 #[0.01, 0.9]
    self.param_dict["lows_q_factor"] = vst.lows_q_factor

    vst.lows_gain_db_s = np.random.rand() * 86. - 80. #[-80.0dB/s, 6.0dB/s]
    self.param_dict["lows_gain_db_s"] = vst.lows_gain_db_s


    vst.highs_cutoff_frequency_hz = np.random.rand() * 19980. + 20. #[20.0Hz, 20000.0Hz]
    self.param_dict["highs_cutoff_frequency_hz"] = vst.highs_cutoff_frequency_hz

    vst.highs_q_factor = np.random.rand() * 0.89 + 0.01 #[0.01, 0.9]
    self.param_dict["highs_q_factor"] = vst.highs_q_factor

    vst.highs_gain_db_s = np.random.rand() * 84. - 80. #[-80.0dB/s, 4.0dB/s]
    self.param_dict["highs_gain_db_s"] = vst.highs_gain_db_s

    vst.dry_wet = np.random.rand() #[0.0, 1.0]
    self.param_dict["dry_wet"] = vst.dry_wet

    vst.fade_in_time_s = np.random.rand() * 9. #[0.0s, 9.0s]
    self.param_dict["fade_in_time_s"] = vst.fade_in_time_s

    vst.fdn_size_internal = 64

    output = vst(vox, rate)

    self.vox = output



def reverb(self):

    rate = self.sampleRate
    acc = self.acc
    vox = self.vox

    #change vox to stereo in order to get stereo reverb
    if len(vox.shape) != 2:
        vox = np.array([vox, vox]).T


    if len(acc.shape) == 2:
        monoAcc = np.mean(acc, axis=1)
        onset_env = librosa.onset.onset_strength(monoAcc, rate)
    else:
        onset_env = librosa.onset.onset_strength(acc, rate)

    tempo = librosa.beat.tempo(onset_env, rate)

    RT = (-1/45) * tempo + (40/9)

    vst_path = "../VST3/"
    vst_name = "FdnReverb.vst3"

    vst = load_plugin(vst_path + vst_name)

    vst.room_size = 15
    vst.reverberation_time_s = RT
    vst.dry_wet = 0.16   #0. is 100% dry

    # set other parameters to default
    vst.lows_gain_db_s = 0.
    vst.highs_gain_db_s = 0.
    vst.fade_in_time_s = 0.2
    vst.fdn_size_internal = 64

    self.param_dict["room_size"] = vst.room_size
    self.param_dict["reverberation_time_s"] = vst.reverberation_time_s
    self.param_dict["lows_cutoff_frequency_hz"] = vst.lows_cutoff_frequency_hz
    self.param_dict["lows_q_factor"] = vst.lows_q_factor
    self.param_dict["lows_gain_db_s"] = vst.lows_gain_db_s
    self.param_dict["highs_cutoff_frequency_hz"] = vst.highs_cutoff_frequency_hz
    self.param_dict["highs_q_factor"] = vst.highs_q_factor
    self.param_dict["highs_gain_db_s"] = vst.highs_gain_db_s
    self.param_dict["dry_wet"] = vst.dry_wet
    self.param_dict["fade_in_time_s"] = vst.fade_in_time_s

    output = vst(vox, rate)

    self.vox = output
