import io
import os
import subprocess
import sys


def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r



def separate(input_path, output_path):
    cmd = ["python3", "-m", "demucs.separate", "-n", model]
    if mp3:
        cmd += ["--mp3", f"--mp3-bitrate={mp3_rate}"]
    if float32:
        cmd += ["--float32"]
    if int24:
        cmd += ["--int24"]
    if two_stems is not None:
        cmd += [f"--two-stems={two_stems}"]
    
    if isGPU:
        cmd += ["-d", "cuda"]


    for file in os.listdir(input_path):
        if ".wav" in file:
            each_cmd = cmd + ["-o", str(output_path)]
            each_cmd += [str(input_path+"/"+file)]
            subprocess.run(each_cmd)


def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            r.append(os.path.join(root, name))
    return r
    

def separate_from_flie_list(file_list, output_path):
    cmd = ["python3", "-m", "demucs.separate", "-n", model]
    if mp3:
        cmd += ["--mp3", f"--mp3-bitrate={mp3_rate}"]
    if float32:
        cmd += ["--float32"]
    if int24:
        cmd += ["--int24"]
    if two_stems is not None:
        cmd += [f"--two-stems={two_stems}"]
    
    if isGPU:
        cmd += ["-d", "cuda"]


    for file in file_list:
        if ".wav" or ".mp3" in file:
            print(file)
            each_cmd = cmd + ["-o", str(output_path)]
            each_cmd += [file]
            subprocess.run(each_cmd)

    
# Customize the following options!
model = "mdx_extra"
extensions = ["mp3", "wav", "ogg", "flac"]  # we will look for all those file types.
two_stems = "vocals"   # only separate one stems from the rest, for instance
# two_stems = "vocals"


isGPU = True
mp3 = False
mp3_rate = 320
float32 = False  # output as float 32 wavs, unsused if 'mp3' is True.
int24 = False    # output as int24 wavs, unused if 'mp3' is True.
# You cannot set both `float32 = True` and `int24 = True` !!


#input_path = '/home/kli421/dir1/GTZAN/original'
#output_path = '/home/kli421/dir1/GTZAN/separated'


input_path = "/home/kli421/dir1/MSD/songs"
output_path = "/home/kli421/dir1/MSD/separated"

all_files = list_files(input_path)
#print(all_files)

separate_from_flie_list(all_files, output_path)
