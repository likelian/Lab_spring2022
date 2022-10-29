import soundfile as sf
import os



path = '/Users/likelian/Desktop/Lab/Lab_spring2022/data/reverb_match_experiment/output/'

for file in os.listdir(path):
        if ".wav" in file:
            data, rate = sf.read(path+file)
            sf.write(path+file, data, rate, subtype='PCM_24')