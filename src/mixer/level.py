import numpy as np
import pyloudnorm as pyln


def level_balance(self):

        target_vox_acc_ratio = self.target_vox_acc_ratio
        acc = self.acc
        vox = self.vox
        rate = self.sampleRate

        mix = acc + vox

        meter = pyln.Meter(rate) # create BS.1770 meter
        acc_loudness = meter.integrated_loudness(acc) # measure loudness
        vox_loudness = meter.integrated_loudness(vox) # measure loudness
        mix_loudness = meter.integrated_loudness(mix) # measure loudness

        vox_acc_ratio = vox_loudness - acc_loudness
        vox_mix_ratio = vox_loudness - mix_loudness

        dB = target_vox_acc_ratio - vox_acc_ratio
        gain = 10**(dB/20)
        vox *= gain

        self.vox = vox
