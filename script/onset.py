import csv
from os import walk
import soundfile as sf
import librosa
import numpy as np
import madmom
from madmom.features import Activations
from madmom.features.tempo import *
from madmom.features.beats import RNNBeatProcessor



audio_path = "/Volumes/mix/Dataset/musdb18hq/train/"

with open('../data/reverb_time/train/reverb_time.csv', 'r') as read_obj, \
     open('../data/reverb_time/train/reverb_timeAndOnset.csv', 'w', newline='') as write_obj:
    reader = csv.reader(read_obj)
    writer = csv.writer(write_obj)
    for row in reader:
        try:
            path = audio_path + row[0] + "/mixture.wav"
            data, rate = sf.read(path)
            lengthInSeconds = data.shape[0] / rate


        except:
            print("File Not Found: ", path)
            continue

        if len(data.shape) >= 2:
            data = np.mean(data, axis=1)

        onset_env = librosa.onset.onset_strength(data, rate)
        onset_frames = librosa.onset.onset_detect(onset_env, rate)
        onset_Num = len(onset_frames)
        onsetPerSeconds = onset_Num / lengthInSeconds

        print(row[0])
        print(onsetPerSeconds)
        row.append(onsetPerSeconds)
        writer.writerow(row)
