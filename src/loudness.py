import numpy as np
import scipy.signal



def K_filter(signal, fs, debug=False):
    # apply K filtering as specified in EBU R-128 / ITU BS.1770-4

    # copied from https://github.com/BrechtDeMan/loudness.py/blob/master/loudness.py

    # pre-filter 1
    f0 = 1681.9744509555319
    G  = 3.99984385397
    Q  = 0.7071752369554193
    # TODO: precompute
    K  = np.tan(np.pi * f0 / fs)
    Vh = np.power(10.0, G / 20.0)
    Vb = np.power(Vh, 0.499666774155)
    a0_ = 1.0 + K / Q + K * K
    b0 = (Vh + Vb * K / Q + K * K) / a0_
    b1 = 2.0 * (K * K -  Vh) / a0_
    b2 = (Vh - Vb * K / Q + K * K) / a0_
    a0 = 1.0
    a1 = 2.0 * (K * K - 1.0) / a0_
    a2 = (1.0 - K / Q + K * K) / a0_
    signal_1 = scipy.signal.lfilter([b0,b1,b2],[a0,a1,a2],signal)
    #print("signal_1 [b0,b1,b2],[a0,a1,a2]", [b0,b1,b2],[a0,a1,a2], "\n")

    if debug:
        plt.figure(figsize=(9,9))
        ax1 = fig.add_subplot(111)
        w, h1 = freqz([b0,b1,b2], [a0,a1,a2], worN=8000)#np.logspace(-4, 3, 2000))
        plt.semilogx((fs * 0.5 / np.pi) * w, 20*np.log10(abs(h1)))
        plt.title('Pre-filter 1')
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Gain [dB]')
        plt.xlim([20, 20000])
        plt.ylim([-10,10])
        plt.grid(True, which='both')
        ax = plt.axes()
        ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
        plt.show()

    # pre-filter 2
    f0 = 38.13547087613982
    Q  = 0.5003270373253953
    K  = np.tan(np.pi * f0 / fs)
    a0 = 1.0
    a1 = 2.0 * (K * K - 1.0) / (1.0 + K / Q + K * K)
    a2 = (1.0 - K / Q + K * K) / (1.0 + K / Q + K * K)
    b0 = 1.0
    b1 = -2.0
    b2 = 1.0
    signal_2 = scipy.signal.lfilter([b0,b1,b2],[a0,a1,a2],signal_1)
    #print("signal_2 [b0,b1,b2],[a0,a1,a2]", [b0,b1,b2],[a0,a1,a2], "\n")

    if debug:
        plt.figure(figsize=(9,9))
        ax1 = fig.add_subplot(111)
        w, h2 = freqz([b0,b1,b2], [a0,a1,a2], worN=8000)
        plt.semilogx((fs * 0.5 / np.pi) * w, 20*np.log10(abs(h2)))
        plt.title('Pre-filter 2')
        plt.xlabel('Frequency [Hz]')
        plt.ylabel('Gain [dB]')
        plt.xlim([10, 20000])
        plt.ylim([-30,5])
        plt.grid(True, which='both')
        ax = plt.axes()
        ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
        plt.show()

    return signal_2 # return signal passed through 2 pre-filters



#print("from ITU-R BS.1770-4 when the sample rate is 48000Hz  \n")
#print("filter_1: [1.53512485958697, −2.69169618940638, 1.19839281085285, −1.69065929318241, 0.73248077421585] \n")
#print("filter_2: [1.0, −2.0, 1.0, −1.99004745483398, 0.99007225036621] \n")




def shortTermLoudness(signal, fs, overlapSize = 0.1):
    """
    Short-term loudness is computed by
    integrating the sum of powers over
    a sliding rectangular window of 3 seconds.
    The measurement is not gated.
    """

    if overlapSize < 0.1: print("overlapSize too small")

    signal_2 = K_filter(signal, fs)

    windowSize = fs * 3 #rectangular window in samples of 3 seconds
    hopSize = int(fs * overlapSize) #hopSize in samples

    if len(signal.shape) < 2:
        print("mono")
        return None

    print(signal.shape)

    readIdx = 0
    inLengthInSamples = signal.shape[0]
    blockNum = int((inLengthInSamples - windowSize) / hopSize)
    print("blockNum", blockNum)

    shortTermArray = np.zeros(blockNum)

    for i in np.arange(blockNum):
        blocked = signal_2[i*hopSize:(i+1)*hopSize]
        blocked = np.power(blocked, 2) #power of 2
        mean = np.mean(blocked, axis=1) #take the averge
        mean = np.mean(mean, axis=0) #sum the channels
        shortTermArray[i] = -0.691 + 10.0 * np.log10(mean)


    return shortTermArray



def LoudnessRange(signal, fs, overlapSize = 0.1):
    """

    """
    LUFS = shortTermLoudness(signal, fs, overlapSize = 0.1)

    ABS_THRES = -70 #LUFS (= absolute measure)
    REL_THRES = -20 #LU (= relative measure)
    PRC_LOW = 10 #lower percentile
    PRC_HIGH = 95 #upper percentile

    #Apply the absolute-threshold gating
    abs_gate_vec = LUFS[LUFS >= ABS_THRES]

    #Apply the relative-threshold gating
    n = abs_gate_vec.shape[0]
    #undo 10log10, and calculate mean

    stl_power = np.mean(np.power(10., (abs_gate_vec/10)))
    stl_integrated = 10*np.log10(stl_power) #LUFS
    #rel_gate_vec is indices of loudness levels above relative threshold
    #rel_gate_vec = abs_gate_vec[abs_gate_vec >= stl_integrated] + REL_THRES
    # only include loudness levels that are above gate threshold
    stl_relgated_vec = abs_gate_vec[abs_gate_vec > (stl_integrated + REL_THRES)]

    #Compute the high and low percentiles of the distribution
    #of values in stl_relgated_vec
    n = stl_relgated_vec.shape[0]
    #sort elements in ascending order
    stl_sorted_vec = np.sort(stl_relgated_vec)

    stl_perc_low = stl_sorted_vec[int((n-1)*PRC_LOW/100 + 1)]
    stl_perc_high = stl_sorted_vec[int((n-1)*PRC_HIGH/100 + 1)]

    #Compute the Loudness Range measure
    LRA = stl_perc_high - stl_perc_low # in LU

    print(LRA)

    return LRA



import soundfile as sf

read_path = "../../MIR-1K/UndividedWavfile/abjones_1.wav"

data, rate = sf.read(read_path)


LRA = LoudnessRange(data, rate, overlapSize = 0.1)
