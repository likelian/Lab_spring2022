import csv
from os import walk
import soundfile as sf
import librosa
import numpy as np



audio_path = "/Volumes/mix/Dataset/musdb18hq/train/"

with open('../data/reverb_time/train/reverb_time.csv', 'r') as read_obj, \
     open('../data/reverb_time/train/reverb_timeAndZeroCrossingRate.csv', 'w', newline='') as write_obj:
    reader = csv.reader(read_obj)
    writer = csv.writer(write_obj)
    for row in reader:
        try:
            path = audio_path + row[0] + "/mixture.wav"
            data, rate = sf.read(path)

        except:
            print("File Not Found: ", path)
            continue

        if len(data.shape) >= 2:
            data = np.mean(data, axis=1)


        zero_crossing = librosa.feature.zero_crossing_rate(data)
        zero_crossing_ave = np.mean(zero_crossing)


        print(row[0])
        print(zero_crossing_ave)
        row.append(zero_crossing_ave)
        writer.writerow(row)
