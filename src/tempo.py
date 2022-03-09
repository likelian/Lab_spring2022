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
     open('../data/reverb_time/train/reverb_timeAndTempo.csv', 'w', newline='') as write_obj:
    reader = csv.reader(read_obj)
    writer = csv.writer(write_obj)
    for row in reader:
        try:
            path = audio_path + row[0] + "/mixture.wav"
            #data, rate = sf.read(path)
            proc = TempoEstimationProcessor(fps=100)
            act = RNNBeatProcessor()(path)
            tempo = proc(act)[0][0]
        except:
            print("File Not Found: ", path)
            continue

        #if len(data.shape) >= 2:
        #    data = np.mean(data, axis=1)

        #onset_env = librosa.onset.onset_strength(data, rate)
        #tempo = librosa.beat.tempo(onset_env, rate)


        print(row[0])
        print(tempo)
        row.append(tempo)
        writer.writerow(row)
