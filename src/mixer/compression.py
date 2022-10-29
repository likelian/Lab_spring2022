import numpy as np
from pedalboard import Pedalboard, load_plugin
import loudness
import pyloudnorm as pyln


def compression(self):
    """
    the stating parameters:
        tolerance = 1dB
        threshold = 0dB
        ratio = 3

    if starting LRA is larger than 20dB
        tolerance increases 0.2dB in each iteration

    For each iteration:
        the threshold dcreases by 3dB
        the ratio increase by 0.1

        if the current LRA is within the range of tolerance:
            return the audio

        if threshold is below -30dB:
            the threshold dcreases by 1dB
            the ratio increase by 1
    """
    rate = self.sampleRate
    targetLRA = self.targetLRA
    vox = self.vox

    vox = pyln.normalize.peak(vox, -1.0)

    LRA = loudness.LoudnessRange(vox, rate, overlapSize = 0.1)

    #print("-------------------")
    #print("LRA", LRA)
    #print("filename", filename)

    if LRA < targetLRA:
        print("LRA < targetLRA")
        return None

    tolerance = 1.0
    tolerance_increase = 0.
    if LRA > 20.:
        tolerance_increase = 0.2

    threshold_db = 0.0 #range [-50.0dB, 10.0dB]
    threshold_decrease = 3.

    ratio = 2.9
    ratio_increase = 0.1

    makeup_gain_db = 0.

    vst_path = "../VST3/"
    vst_name = "OmniCompressor.vst3"
    vst = load_plugin(vst_path + vst_name)
    vst.attack_time_ms = 30.
    vst.release_time_ms = 150.

    iterate_count = 0

    while True:
        threshold_db -= threshold_decrease
        threshold_db_str = str(threshold_db) + " dB"
        vst.threshold_db = threshold_db

        ratio += ratio_increase
        vst.ratio_1 = ratio

        makeup_gain_db += 0.5
        vst.makeup_gain_db = makeup_gain_db

        output = vst(vox, rate)

        LRA = loudness.LoudnessRange(output, rate, overlapSize = 0.1)

        tolerance += tolerance_increase

        if (LRA - targetLRA) < tolerance:
            break

        if threshold_db < -30:
            ratio_increase = 1.
            threshold_decrease = 0.5

        if threshold_db < -35:
            print("WARNNING: threshold_db < -35")
            print("threshold_dbs", threshold_db)
            print("Current LRA: ", LRA)
            print("target_loudness_range", targetLRA)
            break

        iterate_count += 1
        if iterate_count >= 100:
            print("WARNNING: iterate_count >= 100")
            print("threshold_dbs", threshold_db)
            print("loudnessRange", LRA)
            print("target_loudness_range", targetLRA)
            break


    self.vox = output
