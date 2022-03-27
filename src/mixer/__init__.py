from .level import level_balance
from .compression import compression
from .reverb import reverb


class mixer:
    def __init__(self):
        self.target_vox_acc_ratio = -0.5
        self.targetLRA = 15


    def set_target_vox_acc_ratio(self, target_vox_acc_ratio):
        self.target_vox_acc_ratio = target_vox_acc_ratio

    def set_targetLRA(self, targetLRA):
        self.targetLRA = targetLRA


    def load_acc(self, acc):
        self.acc = acc

    def load_vox(self, vox):
        self.vox = vox

    def set_sampleRate(self, rate):
        self.sampleRate = rate


    def process(self):
        compression(self)
        reverb(self)
        level_balance(self)


    def get_acc(self):
        acc = self.acc
        return acc

    def get_vox(self):
        vox = self.vox
        return vox

    def get_mix(self):
        mix = self.acc + self.vox
        return mix
