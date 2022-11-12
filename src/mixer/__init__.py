import numpy as np
import pyloudnorm as pyln

from .level import level_balance
from .compression import compression
from .reverb import reverb
from .EQ import EQ


class mixer:
    def __init__(self):
        self.target_vox_acc_ratio = 0.
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

        checked = self.checkShape()
        if checked is False:
            return None

        #self.set_target_vox_acc_ratio(0)
        self.target_vox_acc_ratio = 0.
        level_balance(self)
        EQ(self)
        compression(self)
        reverb(self)
        self.set_target_vox_acc_ratio(-0.5)
        level_balance(self)




    def checkShape(self):

        acc = self.acc
        vox = self.vox

        if vox.shape[0] < 1000 or acc.shape[0] < 1000:
            print("No signal")
            return False

        if len(acc.shape) == 2 and len(vox.shape) == 1:
            vox = np.array((vox, vox)).T

        if acc.shape[0] > vox.shape[0]:
            diff = acc.shape[0] - vox.shape[0]
            vox = np.pad(vox, ((0,diff),(0,0)), 'constant')

        if acc.shape[0] < vox.shape[0]:
            diff =  vox.shape[0] - acc.shape[0]
            acc = np.pad(acc, ((0,diff),(0,0)), 'constant')

        self.acc = acc
        self.vox = vox



    def get_acc(self):
        acc = self.acc
        return acc

    def get_vox(self):
        vox = self.vox
        return vox

    def get_mix(self):

        self.checkShape()

        acc = self.acc
        vox = self.vox


        mix = acc + vox

        meter = pyln.Meter(self.sampleRate)
        loudness = meter.integrated_loudness(mix)
        mix = pyln.normalize.loudness(mix, loudness, -28.0)

        return mix
