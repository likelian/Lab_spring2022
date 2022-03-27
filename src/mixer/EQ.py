import numpy as np
from pedalboard import Pedalboard, load_plugin


def EQ(self):


    rate = self.sampleRate
    acc = self.acc
    vox = self.vox


    vst_path = "../VST3/"
    vst_name = "MultiEQ.vst3"
    vst = load_plugin(vst_path + vst_name)


    if len(vox.shape) == 2:
        vst.number_of_input_channels = vox.shape[1]
    else:
        vst.number_of_input_channels = 1


    vst.filter_enablement_1 = True
    vst.filter_type_1 = "HP (24dB/oct)" #'HP (6dB/oct)', 'HP (12dB/oct)', 'HP (24dB/oct)', 'Low-shelf'
    vst.filter_frequency_1_hz = 100. #[20.0Hz, 20000.0Hz]
    vst.filter_q_1 = 0.75 #[0.05, 8.0]
    vst.filter_gain_1_db = 0. #[-60.0dB, 15.0dB]


    vst.filter_enablement_2 = True
    vst.filter_type_2 = "Peak" #'Low-shelf', 'Peak', 'High-shelf'
    vst.filter_frequency_2_hz = 400. #[20.0Hz, 20000.0Hz]
    vst.filter_q_2 = 2. #[0.05, 8.0]
    vst.filter_gain_2_db = -8. #[-60.0dB, 15.0dB]


    vst.filter_enablement_3 = True
    vst.filter_type_3 = "Peak" #'Low-shelf', 'Peak', 'High-shelf'
    vst.filter_frequency_3_hz = 1000. #[20.0Hz, 20000.0Hz]
    vst.filter_q_3 = 2. #[0.05, 8.0]
    vst.filter_gain_3_db = -2. #[-60.0dB, 15.0dB]


    vst.filter_enablement_4 = True
    vst.filter_type_4 = "Peak" #'Low-shelf', 'Peak', 'High-shelf'
    vst.filter_frequency_4_hz = 2000. #[20.0Hz, 20000.0Hz]
    vst.filter_q_4 = 2. #[0.05, 8.0]
    vst.filter_gain_4_db = -6. #[-60.0dB, 15.0dB]


    vst.filter_enablement_5 = True
    vst.filter_type_5 = "Peak" #'Low-shelf', 'Peak', 'High-shelf'
    vst.filter_frequency_5_hz = 8000. #[20.0Hz, 20000.0Hz]
    vst.filter_q_5 = 2. #[0.05, 8.0]
    vst.filter_gain_5_db = -1. #[-60.0dB, 15.0dB]


    vst.filter_enablement_6 = True
    vst.filter_type_6 = "High-shelf" #'LP (6dB/Oct)', 'LP (12dB/oct)', 'LP (24dB/oct)', 'High-shelf'
    vst.filter_frequency_6_hz = 11000. #[20.0Hz, 20000.0Hz]
    vst.filter_q_6 = 0.71 #[0.05, 8.0]
    vst.filter_gain_6_db = 7. #[-60.0dB, 15.0dB]

    output = vst(vox, rate)
