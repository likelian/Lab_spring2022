import os
import soundfile as sf
import pyloudnorm as pyln


"""
https://github.com/csteinmetz1/pyloudnorm
"""


def loudness_normalization(audio_path):

    

    for filename in os.listdir(audio_path):
        if ".wav" in filename:
            f = os.path.join(audio_path, filename)
        else:
            continue
        
        # checking if it is a file
        if os.path.isfile(f):
            print(f)
        else:
            continue

        print(f)

        data, rate = sf.read(f) # load audio

        # measure the loudness first 
        meter = pyln.Meter(rate) # create BS.1770 meter

        loudness = meter.integrated_loudness(data)

        # loudness normalize audio to -28 dB LUFS
        loudness_normalized_audio = pyln.normalize.loudness(data, loudness, -28.0)


        sf.write(f, loudness_normalized_audio, samplerate=rate)


    return None


path = "/Users/likelian/Desktop/Lab/Lab_spring2022/survey/human mix"
#loudness_normalization(path)

path = "/Users/likelian/Desktop/Lab/Lab_spring2022/survey/deep-learning mix"
#loudness_normalization(path)

path = "/Users/likelian/Desktop/Lab/Lab_spring2022/survey/rule-based mix"
#loudness_normalization(path)

path = "/Users/likelian/Desktop/Lab/Lab_spring2022/survey/random mix"
#loudness_normalization(path)

path = "/Users/likelian/Desktop/Lab/Lab_spring2022/survey/education mix"
#loudness_normalization(path)