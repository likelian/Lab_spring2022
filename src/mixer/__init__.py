from .level import level_balance
from .compression import compression


class mixer:
    def __init__(self):
        self.target_vox_acc_ratio = -0.5
        self.targetLRA = 14


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
        level_balance(self)
        compression(self)

        return self.vox


    def mix(self):
        return self.acc + self.vox
