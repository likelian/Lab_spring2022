import csv
from os import walk
import soundfile as sf
import numpy as np
import sys
sys.path.append('../src/')
import loudness



audio_path = "/Volumes/mix/Dataset/musdb18hq/train/"

with open('../data/reverb_time/train/reverb_time.csv', 'r') as read_obj, \
     open('../data/reverb_time/train/LoudnessRange.csv', 'w', newline='') as write_obj:
    reader = csv.reader(read_obj)
    writer = csv.writer(write_obj)

    LR_sum = 0.
    counter = 0

    for row in reader:
        try:
            path = audio_path + row[0] + "/vocals.wav"
            data, rate = sf.read(path)
            #lengthInSeconds = data.shape[0] / rate


        except:
            print("File Not Found: ", path)
            continue

        if len(data.shape) >= 2:
            data = np.mean(data, axis=1)


        LR = loudness.LoudnessRange(data, rate)

        LR_sum += LR
        counter += 1

        print(LR)

        row.append(LR)
        writer.writerow(row)

    print("average LoudnessRange: ", LR_sum / counter)
