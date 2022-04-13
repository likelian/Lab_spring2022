import csv
from os import walk
import soundfile as sf
import librosa
import numpy as np
import pyACA



audio_path = "/Volumes/mix/Dataset/musdb18hq/train/"

with open('../data/reverb_time/train/reverb_time.csv', 'r') as read_obj, \
     open('../data/reverb_time/train/reverb_timeAndSpectralFlux.csv', 'w', newline='') as write_obj:
    reader = csv.reader(read_obj)
    writer = csv.writer(write_obj)
    for row in reader:
        try:
            path = audio_path + row[0] + "/mixture.wav"
            data, rate = sf.read(path)

        except:
            print("File Not Found: ", path)
            continue


        [vsf, t] = pyACA.computeFeature("SpectralFlux", data, rate)


        SpectralFlux_mean = np.mean(vsf)

        print(row[0])
        print(SpectralFlux_mean)
        row.append(SpectralFlux_mean)
        writer.writerow(row)
