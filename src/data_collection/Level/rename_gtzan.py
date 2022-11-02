import os


input_path = '/home/kli421/dir1/GTZAN/original/'

for file in os.listdir(input_path):
    filename_no_dot = file.replace(".", "", 1)
    os.rename(input_path+file, input_path+filename_no_dot)
    