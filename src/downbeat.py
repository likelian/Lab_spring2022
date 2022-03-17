import csv
from os import walk
import soundfile as sf
import librosa
import numpy as np
import madmom
from madmom.features.downbeats import RNNDownBeatProcessor



audio_path = "/Volumes/mix/Dataset/musdb18hq/train/"

with open('../data/reverb_time/train/reverb_time.csv', 'r') as read_obj, \
     open('../data/reverb_time/train/reverb_timeAndDownbeat.csv', 'w', newline='') as write_obj:
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


        proc = RNNDownBeatProcessor()
        proc(path)

        downbeat_Num = len(proc)
        downbeatPerSeconds = downbeat_Num / lengthInSeconds

        print(row[0])
        print(downbeatPerSeconds)
        row.append(downbeatPerSeconds)
        writer.writerow(row)
