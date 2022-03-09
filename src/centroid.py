import csv
from os import walk
import soundfile as sf
import librosa
import numpy as np



audio_path = "/Volumes/mix/Dataset/musdb18hq/train/"

with open('../data/reverb_time/train/reverb_time.csv', 'r') as read_obj, \
     open('../data/reverb_time/train/reverb_timeAndCentroid.csv', 'w', newline='') as write_obj:
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

        cent = librosa.feature.spectral_centroid(data, rate)

        cent_variance = np.var(cent)


        print(row[0])
        print(cent_variance)
        row.append(cent_variance)
        writer.writerow(row)
