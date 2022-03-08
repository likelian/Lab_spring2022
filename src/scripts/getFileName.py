from os import walk


#read_path = "/Volumes/mix/Dataset/musdb18hq/test"
read_path = "/Volumes/mix/Dataset/musdb18hq/train"

#txt_name = "musdb18hq_test"
txt_name = "musdb18hq_train"

f = []
lines = []

for (dirpath, dirnames, filenames) in walk(read_path):
    f.extend(dirnames)
    break


for dirname in f:
    #print(dirname)
    #lines.append("\""+read_path+"/"+dirname+"/vocals.wav"+"\"")
    lines.append(dirname)


with open(txt_name+'.txt', 'w') as ft:
    for line in lines:
        ft.write(line)
        ft.write('\n')
