import numpy as np
from scipy import signal
from pedalboard import Pedalboard, load_plugin
import loudness
from .level import level_process





def EQ(self):

    rate = self.sampleRate
    acc = self.acc
    vox = self.vox

    acc = mono(acc)
    vox = mono(vox)

    acc_blocked = block(acc, rate)
    vox_blocked = block(vox, rate)

    filter_arr = gate_index(vox_blocked)

    acc_gated = gate(acc_blocked, filter_arr)
    vox_gated = gate(vox_blocked, filter_arr)

    #vox_balanced = level_process(acc_gated, vox_gated, 10., rate)

    if acc_gated.shape[0] == 0:
        print("No vocal?")
        return None

    acc_rms_band = filter_bank(acc_gated, rate)
    vox_rms_band = filter_bank(vox_gated, rate)

    # the differencce between two tracks' frequency banks
    rms_band_diff = acc_rms_band - vox_rms_band
    #ignore the two lowest frequency bands
    #rms_band_diff = rms_band_diff[2:]
    diff_mean = np.mean(rms_band_diff)
    rms_band_diff -= diff_mean

    acc_filtered = loudness.K_filter(acc_gated, rate)
    vox_filtered = loudness.K_filter(vox_gated, rate)


    acc_rms_band_filtered = filter_bank(acc_filtered, rate)
    vox_rms_band_filtered = filter_bank(vox_filtered, rate)

    #the important frequency ranges
    acc_rank = np.argsort(-acc_rms_band_filtered)
    vox_rank = np.argsort(-vox_rms_band_filtered)


    acc_rank_threshold = 3
    vox_rank_threshold = 4
    acc_top_rank = acc_rank[:acc_rank_threshold]
    vox_top_rank = vox_rank[:vox_rank_threshold]


    band_list = []
    for band in acc_top_rank:
        if band not in vox_top_rank:
            if rms_band_diff[band] < 0:
                band_list.append(band)

    for band in vox_top_rank:
        if band not in acc_top_rank:
            if rms_band_diff[band] > 0:
                band_list.append(band)


    fcs = [31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]

    freq_list = np.full((10,), 999) #frequencies are initialized with 999
    gain_list = np.zeros(10)


    for i, f in np.ndenumerate(band_list):
        freq_list[i] = fcs[f]
        gain_list[i] = rms_band_diff[f]

    gain_list = np.where(gain_list > 8., 8., gain_list)
    gain_list = np.where(gain_list < -8., -8., gain_list)


    gain_order = np.argsort(-np.abs(gain_list)) #deseconding order

    gain_list_ordered = gain_list[gain_order]
    freq_list_ordered = freq_list[gain_order]

    gain_top_list = gain_list_ordered[:4]
    freq_top_list = freq_list_ordered[:4]

    print("rms_band_diff", rms_band_diff)

    print("gain_top_list", gain_top_list)
    print("freq_top_list", freq_top_list)


    vst_path = "../VST3/"
    vst_name = "MultiEQ.vst3"
    vst = load_plugin(vst_path + vst_name)


    if len(vox.shape) == 2:
        vst.number_of_input_channels = vox.shape[1]
    else:
        vst.number_of_input_channels = 1


    output = applyEQ(vst, vox, rate, freq_top_list, gain_top_list)
    
    self.vox = output




def applyEQ(vst, vox, rate, freq_top_list, gain_top_list):
    """
    apply EQ to vox from given parameters

    vst: MultiEQ.vst3 loaded by Pedalboard
    vox: numpy array of the mono signal
    rate: sample rate of the signal
    freq_top_list: numpy array of 4 center freqency values
        [20.0, 20000.0]
    gain_top_list: numpy array of 4 gain values matched to the freq_top_list
        [-60.0, 15.0]

    all Q values are 1.

    return: processed signals
    """

    vst.filter_enablement_1 = True
    vst.filter_type_1 = "Low-shelf" #'HP (6dB/oct)', 'HP (12dB/oct)', 'HP (24dB/oct)', 'Low-shelf'
    vst.filter_frequency_1_hz = 100. #[20.0Hz, 20000.0Hz]
    vst.filter_q_1 = 1. #[0.05, 8.0]
    #vst.filter_gain_1_db = -12. #[-60.0dB, 15.0dB]
    vst.filter_gain_1_db = 0. #[-60.0dB, 15.0dB]s


    vst.filter_enablement_2 = True
    vst.filter_type_2 = "Peak" #'Low-shelf', 'Peak', 'High-shelf'
    vst.filter_frequency_2_hz = freq_top_list[0] #[20.0Hz, 20000.0Hz]
    vst.filter_q_2 = 1. #[0.05, 8.0]
    vst.filter_gain_2_db = gain_top_list[0] #[-60.0dB, 15.0dB]


    vst.filter_enablement_3 = True
    vst.filter_type_3 = "Peak" #'Low-shelf', 'Peak', 'High-shelf'
    vst.filter_frequency_3_hz = freq_top_list[1] #[20.0Hz, 20000.0Hz]
    vst.filter_q_3 = 1. #[0.05, 8.0]
    vst.filter_gain_3_db = gain_top_list[1] #[-60.0dB, 15.0dB]

    vst.filter_enablement_4 = True
    vst.filter_type_4 = "Peak" #'Low-shelf', 'Peak', 'High-shelf'
    vst.filter_frequency_4_hz = freq_top_list[2] #[20.0Hz, 20000.0Hz]
    vst.filter_q_4 = 1. #[0.05, 8.0]
    vst.filter_gain_4_db = gain_top_list[2] #[-60.0dB, 15.0dB]


    vst.filter_enablement_5 = True
    vst.filter_type_5 = "Peak" #'Low-shelf', 'Peak', 'High-shelf'
    vst.filter_frequency_5_hz = freq_top_list[3] #[20.0Hz, 20000.0Hz]
    vst.filter_q_5 = 1. #[0.05, 8.0]
    vst.filter_gain_5_db = gain_top_list[3] #[-60.0dB, 15.0dB]


    vst.filter_enablement_6 = True
    vst.filter_type_6 = "High-shelf" #'LP (6dB/Oct)', 'LP (12dB/oct)', 'LP (24dB/oct)', 'High-shelf'
    vst.filter_frequency_6_hz = 11000. #[20.0Hz, 20000.0Hz]
    vst.filter_q_6 = 1. #[0.05, 8.0]
    vst.filter_gain_6_db = 0. #[-60.0dB, 15.0dB]

    output = vst(vox, rate)
    return output


def mono(audio):
    if len(audio.shape) == 2:
        return np.mean(audio, axis=1)
    else:
        return audio



def block(audio, rate):
    """
    return the block the audio as a matrix
    """

    blockLength = int(0.1 * rate)
    blockNum = int(audio.shape[0]/blockLength)

    blocked_audio = np.zeros((blockNum, blockLength))
    for i in range(blockNum):
        blocked_audio[i] = audio[i*blockLength : (i+1)*blockLength]

    return blocked_audio


def gate_index(blocked_audio, threshold_db = -30):
    """
    return a boolean filter array for blocks above the threshold
    """

    squared = blocked_audio**2

    rms = np.sqrt(np.mean(squared, axis=1))

    rms_dB = 20*np.log10(rms+0.0000000001)

    filter_arr = rms_dB > threshold_db

    return filter_arr


def gate(blocked_audio, filter_arr):
    """
    remove the blocks below the threshold and concatenate the audio
    """
    gated_blocked_audio = blocked_audio[filter_arr]

    audio = gated_blocked_audio.flatten()

    return audio



def filter_bank(audio, rate):
    """
    2nd order butterworth bandpass filter
    return:
        a numpy array of (10)
        the value in rms_dB_bank is the rms of each filter bank
    """

    Nyquist = rate/2
    fcs = [31.5, 63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000] #ISO standard octave-band center frequencies

    rms_dB_bank = np.zeros(10)

    for idx, fc in enumerate(fcs):

        bandwidth = fc*2**0.5/Nyquist - fc*2**(-0.5)/Nyquist

        sos = signal.butter(2, [fc*2**(-0.5)/Nyquist, fc*2**0.5/Nyquist], 'bp', fs=rate, output='sos') #second order sections
        filtered = signal.sosfilt(sos, audio)

        squared = filtered**2

        rms = np.sqrt(np.mean(squared))
        rms /= bandwidth #normalize the energy by filter bandwidth
        rms_dB = 20*np.log10(rms)
        rms_dB_bank[idx] = rms_dB

    return rms_dB_bank
