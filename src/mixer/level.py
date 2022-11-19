import numpy as np
import pyloudnorm as pyln
from mixer.mixNet import mel_spec
from mixer.mixNet import FaderNet


def deep_level_balance(self):
    
    acc = self.acc
    vox = self.vox

    rate = self.sampleRate

    mel_spec_dataset = mel_spec.mel_spec(acc, vox, rate)

    target_vox_acc_ratio = FaderNet.run_FaderNet(mel_spec_dataset)

    self.param_dict["relative_loudness"] = target_vox_acc_ratio

    output = level_process(acc, vox, target_vox_acc_ratio, rate)
        
    self.vox = output



def level_balance(self, optional_ratio=None):

        if optional_ratio is not None:
            target_vox_acc_ratio = optional_ratio
        else:
            target_vox_acc_ratio = self.target_vox_acc_ratio

        acc = self.acc
        vox = self.vox

        rate = self.sampleRate

        output = level_process(acc, vox, target_vox_acc_ratio, rate)
        

        self.vox = output


def level_process(acc, vox, target_vox_acc_ratio, sampleRate):

    meter = pyln.Meter(sampleRate) # create BS.1770 meter
    acc_loudness = meter.integrated_loudness(acc) # measure loudness
    vox_loudness = meter.integrated_loudness(vox) # measure loudness

    vox_acc_ratio = vox_loudness - acc_loudness
    dB = target_vox_acc_ratio - vox_acc_ratio
    gain = 10.**(dB/20.)

    vox *= gain

    return vox
