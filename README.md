# Lab_fall2022
* * *



## 11/22/2022


### **Presentation:**

randomlize typo

get rid of CNN slide

introduction to be high level
I picked EQ Compression, Reverb, level

audio example, good mix, bad mix

flowchart, too much,

inference the same for both system

statisc driven deep learning driven

separate training and inference

name the system differently

<u>box plot violin plot of objective evaluation</u>

### **Thoughts:**

interactive python terminal interface?
generate Reaper session?

### **Done:**

1. presentation slides
2. rule-based by average value
3. record json
4. deep learning pipeline
5. record json
6. loudness normalization (script)
7. another education mix
8. survey ready
9. checked the survey CSV output


### **To-do:**

1. presentation slides
2. deep learning pipeline
3. release the survey
4. add traditional features, just an experiment



## 11/15/2022


### **Meeting:**

Think about what does it matter for the listening survey when the deep learning model shows no generalization on the validation set.


### **Done:**

##### Rule-based:

1. log parameter json

##### random mix:

1. create uniform random mix
2. -8dB to 8dB relative loudness
3. log parameter json


##### Comp:
song level reulsts after removing outliners in test set:

Song level evaluation:
abs error of the above this [model](https://github.com/likelian/Lab_spring2022/tree/main/results/Comp/lr%3D0.0001%2C%20weight_decay%3D0.000001) on 48 test songs: **2.63** dB

mean prediction of 16.3574 dB:
abs error over 48 test songs **2.88** dB

Error distribution and grounud truth LRA distribution is in the above link.




##### Reverb:

Many reuslts [here](https://github.com/likelian/Lab_spring2022/tree/main/results/reverb/training)

song-level model error of [model](https://github.com/likelian/Lab_spring2022/tree/main/results/reverb/training/lr%3D0.00001) 
```
room_size                       7.298484
reverberation_time_s            1.005998
lows_cutoff_frequency_hz       41.553016
lows_q_factor                   0.355384
lows_gain_db_s                  3.619424
highs_cutoff_frequency_hz    3390.795938
highs_q_factor                  0.135629
highs_gain_db_s                 5.014345
fade_in_time_s                  0.400559
dry_wet                         0.061344
```


mean value prediction error song level

```
room_size: 7.311460
reverberation_time_s: 1.007009
lows_cutoff_frequency_hz: 40.261948
lows_q_factor: 0.359836
lows_gain_db_s: 3.645113
highs_cutoff_frequency_hz: 3461.823242
highs_q_factor: 0.171179
highs_gain_db_s: 5.349164
fade_in_time_s: 0.402940
dry_wet: 0.071644
```




mean value of the training set

```
room_size: 14.546935
reverberation_time_s: 1.5948825
lows_cutoff_frequency_hz: 101.77251
lows_q_factor: 0.5270046
lows_gain_db_s: -2.1335206
highs_cutoff_frequency_hz: 11858.535
highs_q_factor: 0.7714809
highs_gain_db_s: -16.023586
fade_in_time_s: 0.6773426
dry_wet: 0.11475082
```


##### EQ:

The final [model](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/aggregate/more_data/lr%3D0.001%20with%20mdoel)


EQ final processed error
**4.481698507979765** dB

processed output mean:
**1.7551649273452112** dB





## 11/8/2022



### **To-do:**

average parameter in the rule-based system?


Reverb:
1. train

Comp:
1. ~~plot the error distribution~~
2. ~~plot gt distribution~~


EQ:
1. ~~EQ shape loss, remove gain mean~~
2. one network for each band?



Random mix
1. get it done
constraint of random mix range
uniform and normal random?


### **Done:**

human mix finished

##### EQ:

extract mel-spec for the test set

##### Comp:

1. data collection
2. start training with data cleaning
3. remove LRA > 30. and LRA < 5.

```
MSD_mean = 16.3574 dB
test_mean = 15.1526 dB
train_mean = 16.1977 dB

mean_prediction_error = 2.81837dB
```
See the results of compNet [here](https://github.com/likelian/Lab_spring2022/tree/main/results/Comp). 



Song level evaluation:
abs error of the above this [model](https://github.com/likelian/Lab_spring2022/tree/main/results/Comp/lr%3D0.0001%2C%20weight_decay%3D0.000001) on 48 test songs: **2.85** dB

mean prediction of 16.3574 dB:
abs error over 48 test songs **3.16** dB

##### Reverb:



## 11/1/2022

### **Meeting:**


One mel-spectrum for one EQ setting may be too abbreviated. Try 10s aggregation.

The data presentation may be the problem.


30 user results shoud be enough to be statistically significant.

Experts’ rating may not need to be statistically significant to mean something.

Leave one week for data analysis.



### **Done:**

##### EQ:

Frequency resolution: 44100/2048 = **21.53Hz**
Mel spectrum has **128** banks.

--

It seems that my data collection didn’t include the EQ effect!! Fixed for the new data.

--

The model cannot even learn over **one song of ~~49~~ 10 EQ settings and validate on 1 EQ setting**. The validation loss goes down as the model predicts smaller values. The training loss can hardly move after reaching 3+dB, much worse than expected. See the results [here](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/one_song/48-vs-1).

--
--

**one song in 1000 EQ settings**, see the results [here](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/one_song/1000) (batch size of 1). The validation set which is also from the same song with different EQ settings. The model doesn't genernalize, but can overfit much better than any previous experiments.

When overfit on one song, the test output can get some very large numbers. See below:

```
test_pred tensor([ -2.9509,   6.5698,  -7.7532,  -0.4996, -28.7141,   0.4498, -16.3401, -2.5833,   6.5215])

test_targ tensor([ -7.0740,   9.1288,  -7.5502, -12.5740,   0.0000,   0.0000,   0.0000, 0.0000,   0.0000])
```

-- 



**one song one averaged mel-spectrogram frame**


<u>3h30min for 10000 concatenated EQ data collection.</u> <u>1min can collect 47 files</u>.


The data size is much smaller. See the results [here](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/concat_one_song/10000/pt/0.1%20*%20zeros%20lr%3D0.00001/change%20dropout%20location). Compared with previous [results](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/one_song/1000) on the mel-spectrum of the entire songs (1000 EQ settings, some changes in the model). The two results look similar. Again, can overfit well on the training data, but cannot generalize at all.

The training is a lot lot faster (minutes vs hours). Far less storage requirements (400MB vs 10GB). 

Interesttingly, smaller training data size ([1/10](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/concat_one_song/10000/pt/0.1%20*%20zeros%20lr%3D0.00001/change%20dropout%20location/one%20tenth%20data) and [1/5](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/concat_one_song/10000/pt/0.1%20*%20zeros%20lr%3D0.00001/change%20dropout%20location/one%20fifth%20data)) shows no overfitting on the training set. The output is very small, similar to the experiments on the entire dataset in the previous weeks. 

The validation results make some sense, but terribly wrong on others.

```
test_pred tensor([ -7.6203,  -1.7941,   2.2201, -15.0948,   6.8406,  -5.6358,  -3.6307, -1.9124,  -5.1027])

test_targ tensor([ -9.1660,  -3.8127,   1.6574,   0.0000,   0.0000,   0.0000,   0.0000,  -11.0619,   0.0000])
```

### **Thoughts:**

It's frustrating to see that the model cannot generalize on one song with different EQ settings.

I think:
* the key is to have many many EQ settings, no matter on one song or more than one songs.
* whether the training and validation set share the same original song may not matter on the results. Of course this is not allowed for real experiments.


Data aurgmentation:

* add Gussian noise on ground truth
* add Gussian noise on mel-spectrogram
* on audio (local computional time cost, storage/RAM cost)





## 10/27/2022

### **To-do:**

EQ:

1. ~~check time-freq resolution~~
2. average neighbor spectrums, or even average over the song
3. ~~overfit on one song, and test if a different EQ setting can be predicted~~



Reverb:

1. ~~evaluation the quality of reverb extraction~~




### **Meeting:**

time freq resolution:
can the mel-spectrogram reflect the frequency bands?
For thie particular EQ task, no need for good time resolution
increase hop/block size

average neighbor spectrums/me-spectrums(5s, 10s, etc.)
or even average over song


overfit on song of different EQ setting, and test on the song with different EQ settings

Add MSD later. Alex doesn't believe that more original data is the solution. The current setup is 100 songs and 50 EQ settings for each. Alex thinks it's not bad.




### **Done:**

##### Rule-based and human mix:

changed the session file for human mixing
* change EQ Compressor order
* reverb room size to 15

change the rule-based system
* dry_wet to 0.16
* reverb room size to 1
* compressor release time to 150ms
* removed K-weighted filter in EQ
* changed the EQ ranking
* a few other things I don't remember, need to refer to the code when writing the paper


bounced the clipping-free audio from Reaper for rule-based mixing

Fixed a bug:
rule-based reverb wa


the final normalized loudness should be **-28 LKFS**. Use iZotope RX to set the loudness.


##### Reverb:

Evaluation of the reverb prameter estimation by genetic algorithm. The error compares the extracted IRs by Chameleon and the IRs from FdnReverb. See the histogram [here](https://github.com/likelian/Lab_spring2022/tree/main/results/reverb/reverb_extraction).



train folder

* mean_reverb_time_error:  **0.22s**
* var_reverb_time_error:  0.07s



test folder

* mean_reverb_time_error:  **0.18s**
* var_reverb_time_error:  0.02s

--




A loook at the reverb extraction results with ground truth. I applied three Vahalla reverb on three mostly dry singing vocal track.

```
dry_wet ratio directly from the Chameleon plugin:

Carla(track name):
GT: 20.3%
Estimated: 6.1%

Christy:
GT: 33.3%
Estimated:18.2%

Darcy:
GT: 19.9%
Estimated:14.8%


Christy.wav
original_reverb_time(RT60):  0.63s
extracted_reverb_time:  0.79s
absolute error: 0.16s
  
Carla.wav
original_reverb_time:  3.73s
extracted_reverb_time:  3.53s
absolute error:  0.21s

Darcy.wav
original_reverb_time:  0.71s
extracted_reverb_time:  0.86s
absolute error:  0.15s
 
mean_reverb_time_error: 0.17s
```









* * *
## 10/25/2022


### **To-do:**

human mix:
1. ~~prepare audio~~
2. ~~prepare session~~
3. prepare instruction
4. send to Ben, text and email
5. arrange a date to meet



### **Meeting:**

distribution of RT60 error

experiment on reverb extraction quality, 3 files

log spectrogram as cost function would be better


### **Done:**


1. collected the reverb parameter data of MUSDB dataset. See it [here](https://github.com/likelian/Lab_spring2022/tree/main/data).
    1. used a commercial plugin [Chameleon](https://www.accentize.com/chameleon/) to estimate the impulse response and the dry/wet ratio.
    2. used a python genetic algorithm package [PyGAD](https://pygad.readthedocs.io/) to estimate the appropriate parameters on an ope-source reverb plugin [FdnReverb](https://plugins.iem.at/docs/plugindescriptions/#fdnreverb) to be close to the impulse response.
    3. the cost function is the spectrogram error.
    4. reached a mean reverb time error of RT60 of **0.22 second**. It could be further improved by more generations, but I was limited by the computational cost on my laptop (vst loading doesn't work on Linux).

1. contacted a mixing engineer (thanks Ben!)

### **Thoughts:**

R2 score?
multiple model on different training data, and vote?
concatenate spectrogram?



* * *

## 10/18/2022



##### Summary on the summary on EQ:


* The model can overfit on small training data, but learns slowly on larger data.
* There is no obvious learning on validation set. The model is not as good as predicting zeros on the evaluation metric (error).
* Smaller output (close to 0dB), better validation results on the evaluation metric. The correlation is very very strong.


##### Summary on EQ:


The output of 9 frequency bands are processed in a way that the top 4 absolute changes are kept, and the rest are rounuded down to 0dB. This will be the post-processing of the final implementation (although there different ways of aggregating over audio frames).


Validation mean absolute error when predicting random values (-15dB to 15dB):
validation_loss: **8.61dB**
processed_validation_loss: **6.98dB** (small value set to 0)


Validation mean absolute error when predicting the mean value (0dB):
validation_loss **3.32dB**
processed_validation_loss **3.32dB**


The model can get to this processed validation loss in the range of from **4.0dB to 4.5dB**, with the cost of relative small output values,  mean absolute value at around <u>2dB</u>. I think the suitable range is <u>from 3dB to 4dB</u>.


The mean absolute output of validation is <u>strongly</u> correlated with validation loss, suggesting that the output is somehow random on validation. See one [example](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/small_train_data/overfit/1pt%20with%20model) out of many. (The output_mean.png is not labelled correctly.)


The only way to prevent predicting zeros is to picking the 4 bands that have changes in the ground truth.

The current biggest issue is that the model struggles on learning on large data. The model can overfit on 1 pt file, down to 1.51dB MAE of processed output after 500 epochs. When training on 2 pt file, it goes to 2.05dB after 500 epochs. [Link](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/small_train_data/overfit) 

Training on 50 files is slow [link](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/2-50/50). The processsed training loss goes to 2.97dB after 50 epochs, little change from 3.11dB in the first epoch. compared with 2.32dB of 50 epoch on 1 pt file. The training takes several hours.

This is not about generlization on the validation set which shows probably almsot no learning, or just getting smaller output which leads to smaller error.



One pt file contains 100 songs with arbitrary order. There are some overlaps of one song with different EQ settings put in one pt file.

The total training set so far is 100 songs in the train folder of MUSDB18 applied 50 different EQ settings each.





### **Done:**

###### EQ:
1. normalize the gain values from [-15, 15] in dB to [0., 1.].
2. change the loss function from MAE to MSE.
3. changed the loss function ignore zeros in the ground truth. More weighted on the non-changed values, less the output values, better the total loss. See the [results](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/small_train_data/ignore_zeros).
4. changed the loss function to care about the largest 4 absolute gain change values in the prediction, weighted on the rest. When the rest is fully ignored, the output values are close 0dB. It outperforms the method above, when the loss of the rest is set to 0.5. See the results [here](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/small_train_data/largest_4_val).
5. larger training data (10 pt file) => output zero, change back to "ignore zeros"
6. still goes to zero.
7. resume the previous small value panelization, worse than with only 1 pt file. train loss stucked at 5.47dB, and validation loss at 5.53dB. 
8. 2 pt file, step 4 loss, close to samll ouutput
9. change reLu to tanh. [Link](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/small_train_data/ignore_zeros)
10. ~~add 3 FC layers and 2 Sigmoid layers. Output goes to small values~~. removed.
11. remove bias in the FC layer
12. log and plot output mean, concerning only the largest 4 absolute values
13. lr from 0.01 to 0.001, no big change. [Link](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/2-50/10)
14. experiment with 10%? of 20 pt files. unstable, little learning of training loss after several epochs. Better results (3.97dB on processed validation loss, compared to previous 4.68dB), due to small outputs on some epochs. [Link](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/2-50/20)
15. train on the entire 50 pt files, no big differences. [Link](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/2-50/50)
16. change learning rate on 10 pt files [Link](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/2-50/10)
17. try extreme overfitting 1 pt file, 500 epochs. [Link](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/small_train_data/overfit)
18. try extreme overfitting 2 pt file, 500 epochs. overfiiting is not as good as on 1 pt. [Link](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/small_train_data/overfit)


###### Not yet done:
1. try more than 50 epochs on 50 pt files
2. train on 1 pt, and then train on another pt file
2. try train and test on same audio, different EQ setting?
3. change the network strcture again?  
4. train and overfit on one portion exclusively, then move on to another, to avoid fitting mean/small value?


###### Reverb:
1. extract reverb profiles of MUSDB test set
2. export IRs to wav for MUSDB test and train set




### **Tricks:**

enter copy mode and scroll in tmux
`ctrl + B`, then `[`
`esc` to exit


* * *

## 10/11/2022

### **To-do:**


Because the training data is imbalanced, the model will surely output zeros.


1. ~~change the loss function ignore zeros, or include one zero (or just do what will be done in the post-processing?)~~
2. ~~normalization on ground truth~~
3. ~~squared error instead of aboslute error~~
4. just focus on MUSDB for now



### **Done:**

##### EQ:
1. data uploaded
2. data not uploaded properly
3. reupload data
4. EqNet learns to output values close to 0, no learning
5. change the loss functino to MAE
6. change the EqNet loss function to penalize predicting small numbers.
    1. easily pushing the predictions to very large numbers
    2. make more changes
    3. `if mean(abs(pred)) > 5: MAE loss - mean(abs(pred)) + 3.3`
7. can at least overfit the trainning set. Train on only the first .pt file. See the [results](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/small_train_data). Final results:
    1. train_loss MAE: 3.41
    2. validation_loss MAE: 7.19

7. train on 1/300 of the first 25(half) of the .pt files. Bad [results](https://github.com/likelian/Lab_spring2022/tree/main/results/EQ/first_half%2825pt%29). ~~Somehow the output of in inference is 1. not 9 values.~~ fixed

```
# an example of the overfitted training prediction. better than nothing.

target tensor[ -6.37, 0.00, -11.17, 0.00, 0.00, 0.00, 0.00, 14.00, 8.85]
pred tensor  [ -6.06, 1.41, -10.06, 0.05, -2.09, 1.76, 0.63, 15.17, 9.87]
```

```
# even overfitting doesn't always work

target [ -9.18, 0.59, 0.00, -14.40, 0.00, 0.00, 0.00, 4.05, 0.00]
pred   [-7.25, -0.59, -9.99, 1.28, 5.08, 3.82, -0.19, -5.75, -4.96]
```


```
# of course the validation prediction is nonsense

test_pred   [-15.75, -6.83, 3.79, 13.93, -1.59, 13.89, -1.89, 5.2, 4.85]
test_target [9.60,    0.00, 0.00, 13.62, 0.00, -4.14, -13.64, 0.00, 0.00]
```


##### Level:
1. remove non-vocal parts from the validation set
2. get the averge of MSD
2. predict average and compare
2. remove non-vocal parts from the training set
3. retrain


Train and validation a model on the cleaned non-vocal dataset. See it [here](https://github.com/likelian/Lab_spring2022/tree/main/results/archive/MSD_remove_non_vocal/1)

Absolute error on the data point level of the validation set is **2.209415026897028 dB**.

* error over 50 songs **1.87 dB** (1.86784694970188)
* error over 48 songs **1.64 dB** (1.6441102914) (removing the two non-vocal songs)


averge relative loudness of cleaned MSD containing non-vocal is:  -3.425692845827129 dB


predict mean (-3.425692845827129) on the song level in the validation set:

* error over 50 songs **2.39 dB** (2.386900276409575)
* error over 48 songs **2.13 dB** (2.131985919)





### **Thoughts:**

Eample of how the error will look like with the given prediction:

```
#a very good prediction
pred = [8.5, 6.5, -5.5, 4.5, 1., 1., 1., 1., 1.]
target = [7.5, 7.5, -7.5, 7.5, 0., 0., 0., 0., 0.]
MAE = L1_loss(pred, target)

MAE == 1.333
```

```
#a "good" predction
pred = [6., 4., -3., 4., 2., 1., 2., 1., 1.]
target = [7.5, 7.5, -7.5, 7.5, 0., 0., 0., 0., 0.]

MAE == 2.222
```


```
#some good, some bad
pred = [8.5, -2, -5.5, 0, 1., 1., 4., 5., 1.]
target = [7.5, 7.5, -7.5, 7.5, 0., 0., 0., 0., 0.]

MAE == 3.5555
```


```
# no prediction
pred = [0., 0., 0., 0., 0., 0., 0., 0., 0.]
target = [7.5, 7.5, -7.5, 7.5, 0., 0., 0., 0., 0.]

MAE == 3.333
```

```
# a bad predction
pred = [-6., -4., 3., -4., -2., 1., 2., 1., 1.]
target = [7.5, 7.5, -7.5, 7.5, 0., 0., 0., 0., 0.]

MAE == 6.0
```



### **Tricks:**

refresh a command every 2 seconds
`watch -n 2 free -h
`


instruct nvidia-smi to refresh every 10 seconds.
`nvidia-smi -l 10`


Uploading files through rsync doesn't seem to eat memory
`
rsync -r -ahp -p  /Volumes/mix/Dataset/EQ_mel/musdb18hq/test kli421@deepnet1.music.gatech.edu:/home/kli421/dir1/EQ_mel/musdb18hq
`

`
rsync -r -ahp -p  /Volumes/mix/Dataset/EQ_mel/musdb18hq/train kli421@deepnet1.music.gatech.edu:/home/kli421/dir1/EQ_mel/musdb18hq
`






* * *

## 10/4/2022

### **To-do:**

Fader:

1. comparison with a mean baseline
2. remove the non-vocal part prediction in post-processing
3. remove outliners from the test set

No GAN



### **Thoughts:**

###### De-reverbration options:
* An open-source de-reverbration [toolkit](https://distantspeechrecognition.sourceforge.io/btk20_documentation/user_docs/dereverberation.html) 
* [iZotope RX](https://www.izotope.com/en/products/rx/features/de-reverb.html)
* [DeRoom Pro](https://www.accentize.com/deroom/), Only Reverb Listening
* [DeVerberate](https://acondigital.com/products/deverberate/)
* [UNVEIL](https://www.zynaptiq.com/unveil/)
* Ask Sile


##### EQ:
The EqNet will predict the gains of 9 bands (fcs = [63, 125, 250, 500, 1000, 2000, 4000, 8000, 16000]). The Q factor will be fixed, the same as in the rule-based system. The post-processing will select the highest 4 absolute gain values and apply to the EQ. The training and validation should also reflect the final error in a metric different from the raw error.


##### GAN?

##### remove outliner from test set?
Should I remove two songs without vocal from the test folder?
* PR - Happy Daze
* PR - Oh No
and one with phased vocal
* Little Chicago's Finest - My Own


### **Done:**


1. trained on MSD with different learning rate, see the [results](https://github.com/likelian/Lab_spring2022/tree/main/results/archive/MSD/50epoch)
2. tried removing dropout
3. choose a [model](https://github.com/likelian/Lab_spring2022/blob/main/results/archive/MSD/withModel/lr%3D0.001_withModel_Loss.png) at validation loss error on datapoint level of **2.456 dB**, and run the song level validation, getting absolute error of **2.086 dB** over 50 test songs. Removing 2 songs without vocals from the test set, absolute error down to **1.840 dB**.
4. My SOTA is **2.179 dB** validation  absolute error so far ([link](https://github.com/likelian/Lab_spring2022/blob/main/results/archive/MSD/50epoch/lr%3D0.001_validation_loss.txt) and [link](https://github.com/likelian/Lab_spring2022/blob/main/results/archive/MSD/50epoch/lr%3D0.001_Loss.png)), but I didn't recreate that with the same setup. I can keep trying on that.
5. Unable to run the plugin(.so) on Linux.
6. Collect EQed mel spec on MUSDB18. 10x on the test folder,  50x on the train folder.





How to deal with dataset larger than memory [Zhihu link](https://www.zhihu.com/question/386743819). It looks like Pytorch is loading an entire dataset file to memory.







* * *

## 9/27/2022


### **To-do:**

1. finish up MSD
2. increase learning rate
3. report song level error
3. move on to other tasks (reverb)


### **Thoughts:**

1. read a paper, [Automatic music mixing with deep learning and out-of-domain data](https://marco-martinez-sony.github.io/FxNorm-automix/).
2. [Mean absolute percentage error](https://en.wikipedia.org/wiki/Mean_absolute_percentage_error)
3. The result of the paper may not be so good as it seems. The reults are averaged over the song (0.5s window). The loudness measure is LUFS, and it is absolute. So abs((-18dB-(-19dB))/(-19dB)) = 0.05, while I am using relative loudness. The audio is good, but not that close to the reference mix. The dry stems are pretty good by themselves.





### **Done:**

1. move partial MSD
2. separate partial MSD
3. rebooting server helps the VS code connection problem

Running out of storage space on DeepNet1 while moving MSD. This is the current MSD on DeepNet1.

I decided to delete [/1/, /4/, /5/, /7/, /8/, /9/], in order to allocate space for source separation.

```
Filesystem                    Size  Used Avail Use% Mounted on
/dev/sda2                     1.8T  1.7T   91G  95%


du --summarize --human-readable *

539G    songs/
140K    songs/0/
50G     songs/1/

66G     songs/2/
83G     songs/3/

66G     songs/4/

97G     songs/5/
91G     songs/6/
44K     songs/7/
74G     songs/8/
15G     songs/9/


4.9G    ccmixter_corpus
391M    DAMP-VSEP
14G     GTZAN
3.0G    GTZAN_mel
1.3G    iKala
174M    Lab_spring2022
1.2G    MIR-1K
541G    MSD
19G     MSD_mel
38G     musdb18hq
5.9G    musdb18hq_mel
1.1G    Rock Band Multitracks
9.7G    training_set


3.0G    GTZAN_mel
2.0G    original
7.9G    separated


ls | wc -l

MSD/3/  
21936 files separated
11295 mel_spec extracted

```

show progress when removing files
```
rm -rfv LargeDirectory | tqdm --total $(du -a LargeDirectory | wc -l)
```





1. audio snippet loudness normalization to -23 LUFS
2. remove the normalization in the neural network 
3. train with individual relative snippet loudness. the results are [here](https://github.com/likelian/Lab_spring2022/tree/main/results/archive/loudness_normalization/snippet_shuffleOff). No learning. Validation loss surprisedly flat, can't find an explaniation.
4. train with overall relative loudness. the results are [here](https://github.com/likelian/Lab_spring2022/tree/main/results/archive/loudness_normalization/overall_shuffleOff). No improvements comparing with the previous [results](https://github.com/likelian/Lab_spring2022/tree/main/results/archive/musdb_GTZAN/outliner/shuffleOff) in the same condition.


* * *

## 9/20/2022


### **To-do:**


1. normalize to -23dB dbU
2. remove the normalization in the network
3. predict the gain change
4. add more data from Million Song Dataset (already mounted in the servers)
5. increase the validation data size
6. error at song level


### **Done:**

1. snippet relative loudness training
2. separate and train on GTZAN dataset
2. upload and unzip FMA small dataset



### **Results:**

#### Extract the snippet relative loudness as the ground truth

The result is [here](https://github.com/likelian/Lab_spring2022/tree/main/results/archive/snippet_loss). Because the training data size and the validation data size are different, we cannot directly compare it with the previous [results](https://github.com/likelian/Lab_spring2022/tree/main/results/archive/training_data_portion). Even though, it doesn't show obvious improvement. Under the same scale, the snippet method is much worse. But again, we cannot make direct comparison. Please note one version has the Y axis updated to L1 absolute loss (training is still MSE loss as before).


#### Train on the source separated GTZAN + original MUSDB18 dataset

The results are [here](https://github.com/likelian/Lab_spring2022/tree/main/results/archive/musdb_GTZAN). Sadly in this case more data with the same condition makes the result worse. 

With shuffle off, 
* musdb+GTZAN reaches below **5dB** mean absolute error,
* musdb reaches below **2.25dB** mean absolute error.

With shuffle on, the plots look similar with immediate overfitting.
* musdb+GTZAN reaches below **3dB** mean absolute error,
* and musdb reaches below **2.5dB** mean absolute error.



#### Analyze the "ground truth" loudness distribution of GTZAN dataset

* The average is **-1.77dB**. 
* The average of MUSDB training set is **-2.56dB**. 
* The average of MUSDB testing set is **-2.57dB**. 
* The average of [MUSDB train + GTZAN] is **-2.24dB**

The error of source separation is not yet measured. If we will do so, we need to find data that's not in the training of DEMUCS.

#### Measure the error when prediction a const value

predict **-2.56dB**, average of training set of musdb18:
* train_loss (on training set of musdb18): **1.98858dB**
* validation_loss: **2.09256dB**

predict **-1.77dB**, average of GTZAN:
* train_loss (on GTZAN): **4.77358dB**
* validation_loss: **2.09821dB**

predict **-2.24dB**, average of [musdb18 + GTZAN]:
* train_loss (on [musdb18 + GTZAN]): **3.46623dB**
* validation_loss: **2.06969dB**

#### Take a look at the prediction

around 50 epochs, many **outliners**. Not even move towards the average of the training set.


```
test_target tensor([-0.9822, -0.9822, -0.9822, -0.9822, -0.9822, -0.9822, -0.9822, -0.9822,
        -0.9822, -0.9822, -0.9822, -0.9822, -0.9822, -0.9822, -0.9822, -0.9822,
        -0.9822, -0.9822, -0.9822])
```
        
```
train_loss 3.133647832124737
validation_loss 6.302189766815538
test_pred tensor([ -2.3132,   3.6210,  -1.3594,   3.0669, -16.4016,  -9.2550,  -3.3789,
         -1.2425,  -2.4893,   0.9137,   6.4405, -10.5467,  -0.4910, -14.4599,
          1.8968,  -2.7692,  -6.6549,  -2.6803,  -2.6803])
```


around 100 epochs. However the average is not too bad.

```
train_loss 2.577969419920116
validation_loss 6.361862780013492
test_pred tensor([ -0.7363,   1.1263,  18.5542,  -1.4983, -10.8369,  -2.6429,  -6.5198,
         -0.7239,  -5.4357,   3.8212,   6.5138,  -7.8792,  -7.6208,  -4.1977,
          5.7325,  -6.6041,  -1.6016,  -2.2640,  -2.2640], device='cuda:0',
       grad_fn=<SqueezeBackward0>)
Training: 100%|█| 100/100 [09:02<00:00,  5.42s/epoch
```


##### **after filtering out the outliners in the training set (<-10 or >6):**

See the loss plots [here](https://github.com/likelian/Lab_spring2022/tree/main/results/archive/musdb_GTZAN/outliner).


The first a few epochs:

```
train_loss 2.2590598103469146
validation_loss 2.6185671439177676
test_pred tensor([-1.2246, -1.1045, -1.5075, -1.0640, -1.3079, -2.0863, -2.5538, -2.2044,
        -3.1282, -1.0851, -1.1146, -2.4352, -1.8540, -2.5390, -1.3282, -3.2159,
        -1.1520, -0.8380, -0.8380]
```


starts to overfit after many epochs
```
train_loss 1.7438088122341218
validation_loss 3.7056478913730597
test_pred tensor([-3.5198, -1.7534, -2.8902, -1.3237, -2.1851,  1.2402, -2.4298, -2.3742,
        -2.3687, -0.7646, -1.4960, -0.9523, -1.2265, -3.5147, -2.3176, -0.5670,
         0.7430, -1.9325, -1.9325], device='cuda:0',
       grad_fn=<SqueezeBackward0>)
```


### **Thoughts:**
1. we haven't measure the error on the song level, when the snippet predictions are averaged. The individual errors may be minimized over averaging, to a level not significant to the human perception.
2. Is the validation set big enough?
3. when is the point to declare failure on the level balance task and move on?



### **Overfit, what to do**

* more data
* data argumentation
    * DSP methods (filter, pitch shift, reverb, gain, noise, distortion, polarity, etc.)
* dropout
* early-stoping
* regularization
    * L1
    * L2
* reducing the model complexity



* * *

### 9/13/2022


**To-do:**

1. ~~snippet relative loudness~~
2. ~~source separation~~
3. ~~a list of solutions for overfitting, pros and cons~~


**Meeting:**
Be sure to plot everything on one plot
Be sure to scale plots



**Done:**
subjective experiment setup:
1. survey update
2. experiment time cost:
    1. previous version:
        1. Mike: 2min
        2. Shi: 5min
    2. current version:
        1. Mike: 1.5min
        2. Shi: 2min
    3. no change of the audio length for current version

Because my training data is [organized](https://stackoverflow.com/questions/54354465/impact-of-using-data-shuffling-in-pytorch-dataloader) (audio snnippets are ordered by songs), <u>data loader shuffle</u> on and off makes big differences on validation loss plot. See results/archive_half_data/ folder. The plots of one epoch batch loss are also very differnt. Even though, I think shuffle off only makes the training slower, and overfits later. The low point of the first epoch validation loss is at MSE 7.6 dB, so not better than However, shuffle songs instead of snippets may not be a bad idea.


Training on <u>different portions of the data</u> (full, 1/2, 1/4, 1/8, 1/16). See the plots [here](https://github.com/likelian/Lab_spring2022/tree/main/results/archive/training_data_portion/shuffleFalse). The larger the training data, the train loss is slower (understandably). There best validation loss is about the same, but the plot of the full data is very different, **worth investigation**.

See the relative loudness distribution (ground truth) [here](https://github.com/likelian/Lab_spring2022/tree/main/results/archive/loudness_distribution).

relative loudness for each snippets:
1. Uplaod raw audio from musdb18hq to the server


* * *

#### 9/8/2022

### **What to do next**

1. check model hyper-parameters
2. ~~make a list of ways to counter overfitting (dropout, regularizations)~~
3. ~~plot the ground truth, see the distribution~~
4. ~~plot in dB scale, not MSE~~
5. **~~relative loudness for each snippets, not the entire song~~**
6. **~~plan ahead for source separation~~**
7. **~~change training data size to see the impact~~**


### **Current state of model training**
The validation loss stables at around MSE 7.6dB after the training of less 100 batches. That is data less than 1h in time. The prediction centered around -2.7dB, assumed to be the average of the training ground truth.
After training for 100 epochs, the train loss goes stably down from around MSE 7dB to MSE 2dB. The validation loss jumps between MSE 10dB to MSE 20dB. We assume the network “memorized” the training data and the ground truth.

### **Possible Solutions:**

**Expand the training data**

The current training data is many snippets from 150 songs. The ground truth is 150 data point of relative loudness.
More training data is available, but time is needed from data loading. They are not much larger than the current training dataset. (MedleyDB, iKala, ccMixter, and Rock band).
We can create more training data with source separation, get the million song dataset. need to measure the error(loudness, band energy, reverb, loudness range) of the source separated data.


**Change the input data**

The current input: "The FFT size is 2048 with the hop size of 1024. The number of mel filterbanks is 128. Each input feature block includes 64 mel-spectrum temporal steps, and each block represents around 1.51 seconds. The size of the input block is (2, 128, 64).”
We can consider each block to represent longer time.


**Change the neural network**

The current rather simple network consists primarily 2d convolution layers. We can borrow a structure that has succeed on other tasks. Is there a room for RNN is this task, or even combine CNN and RNN for long time series input?

**Change the ground truth representation**

Normalization, amplitude scale, gain change needed instead of targeted relative loudness.


* * *

#### 9/6/2022


**Done:**
1. modified Qualtrics [questionnaire](https://github.com/likelian/Lab_spring2022/blob/main/experiment/survey%20screentshot/screenshot.pdf)
2. finished IRB training
3. submitted IRB protocol, wait for IRB feedback
4. installed server environment
5. install Demucs
6. moved more (unorganized) training data to the server
7. ran the training on the server. 100 epochs took just a few minutes
8. ran the training of the first epoch


**Results:**

* the original [result](https://github.com/likelian/Lab_spring2022/blob/main/results/9:6_Loss.png) of 100 epochs
* the [result](https://github.com/likelian/Lab_spring2022/blob/main/results/9:7_Loss.png) of 1000 epochs
* the [result](https://github.com/likelian/Lab_spring2022/blob/main/results/9:6_Loss%20LR%3D0.0001.png) of changing learning rate from 0.0005 to 0.0001
* the [result](https://github.com/likelian/Lab_spring2022/blob/main/results/9:6_batch_Loss.png) of every batch in the first epoch
* a sample of the volume ratio prediction in the first epoch:
    * [-2.5375, -2.6064, -2.5929, -2.5967, -2.6080, -2.5770, -2.5852, -2.5408,
        -2.6124, -2.5886, -2.6015, -2.5651, -2.5767, -2.5780, -2.5964, -2.5865,
        -2.4674, -2.3650, -2.3650]
    * I think they are moving close to the average(not verified) of the training dataset and stayed there



**Meeting:**

Modifications on Qualtrics:

* [ ] ~~both email address on Introdction page~~
* [ ] ~~informed exempt form, find a template~~
* [ ] ~~wording: "critical listening environment"~~
* [ ] ~~headphone vs speaker~~
* [ ] ~~wording: "it will be helpful to describe your listening environment, optional..."~~
* [ ] ~~ages as group options~~
* [ ] ~~skip the question of listening hours~~
* [ ] ~~one slide for training: examples of very bad and very good mixing, educate about level balance,,,,~~
* [ ] ~~question starts with individual ones, ends with overall quality~~
* [ ] ~~wording: 4 different mixes~~
* [ ] ~~wording: bad vs. good, Qualtrics vocabulary~~

**To-do:**

1. modify the questionnaire
2. wait for Alex's review on IRB
3. change rule-based EQ Q factor to 1

* * *

#### 8/30/2022



**Done:**
1. subjective Qualtrics test set-up
2. connect server via VScode
3. setup Github on server


**Meeting:**

modification on the experiment:
1. text-labeled results
2. likert scal
3. compact view
4. remove unmixed
5. 10 second audio, or even shorter
6. 12-15 audio samples




**To-do:**

Training:
* [ ] move data to server
* [ ] run the training on server
* [ ] look at the first epoch


Experiment setup:
* [ ] modify the experiment according to the meeting
* [ ] try out the experiment and measure the time
* [ ] IRB training
* [ ] IRB submission

***

#### 8/23/2022


Network wrong?
Try a different and very simple regression task

The loss plot last semester looks like overfitting immediately


Talk to Karn about server




**To-do:**

1. Copy IRB proposal from Ash
2. Maybe apply for IRB
3. Make qualtrics
4. Prepare a run-through with Alex next week (how long with the test be?)

1. run the experiment again and plot the detailed results of first few epochs





* * *

# Lab_spring2022

* * *
#### 01/10/2022

original published mix to inform KK mix
Real-time live singing?

TC Electronic's product?


Other:
Pitch Correction must be included

To-do:

1. Find the dataset
2. Read paper (simpler methods?)
3. Research on the market, app and hardware products

* * *
#### 01/19/2022

About proposal:
* options to solve the problem
* discuss about the options
* a realistic timeline
* a measure of success
* can copy plots/graphs from other papers, give citations
* listening test, properly design
what effects to be used?
Rule-based?


don’t get distracted from the goal


“I want to..” is fine, but the language should be scientific.



About the project:
* Blind (without reference)
* Non-blind (with reference)
* Both


**To-do:**

1.  Research on the market, app and hardware products
2.  Try the software reverseDemo_mac from "reverse engineering the mix"
3.  Check DAMP dataset in the hard disk
4.  Start the proposal




* * *


#### 2/23/2022

**To-do:**

1. Iterative compression optimization
2. (Optional) Non-iterative compression optimization
3. Define a plan of reverb parameter matching from impulse response
4. Define a rule-based reverb control from an existing tempo-reverbTime relationship in publications. Define it as linear by myself.
5. (Optional) Implement short-term loudness meter, and loudness range meter
6. Evaluation: current simple listening tests needs more data, a variety of songs
7. Dynamic distribution as evaluation metric
8. A milestone-like progress report every week


* * *

#### 3/2/2022

**Done:**

1. Short-term loudness and loudness range implementation (untested)
2. Rule-based reverb survey
    1. tempo/reverb time formula
    2. auto-correlation, spectral flux?
3. Impulse respoonse matching survey
    1. Genetic algorithm
    2. Hill climbing

**Meeting:**

1. K-filter coefficient error is acceptable, most likely due to floating point error
2. In reverb task, two signals as input can be two large for deep learning
    1. consider vocal as mel-spectrogram, and extracted features from backing tracks (tempo, etc.) as condition. More combinations to be considered and experimented. Interview with mixing engineers for opinions, weighting on the vocal or thhe backing track?
2. Barkband and melband as cost function are not very different. But what is the metric to evaluate the impulse response estimation?
3. Since the reverb rule is unclear, extract the tempo(spectral flux) and reverb time from the dataset, and do a linearly fit (or other fit).


**To-do:**

1. Rule-based compression implementation
2. Verify the commercial tool for IR extraction
    1. reverb applied to dry signal, extract IR, comparing with originnal IR
3. Outline the rule-based EQ
4. Download dataset

* * *

#### 3/9/2022

**Done:**

1. Rule-based compression implemented
2. Reverb time extracted from MUSDB18 Training set
3. Audio features from mixture fail to correlate with reverb time, including:
    1. Tempo
    2. Spectral Centroid Variance
    3. Onset Density
    4. Averaged Spectral Flux
    5. Zero crossing rate


**Meeting:**

It it possible that reverb time is not supposed to corelated with any audio features. Octave errors of tempo detection hurts. 100 songs may not be representative either. The distribution can be some use. The problem is what input to use for the deep learning model.

literature-based reverb rule is still an option.


**To-do:**

1. Revisit the code
2. Some more features to try out:
    1. vocal onset density
    2. mixture downbeat density
    3. mixture chord change density
 3. If none of the audio features work, use a literature-based reverb rule.
 4. Rule-based EQ
 5. Verify the commercial tool for IR extraction

* * *

#### 3/17/2022

**Done:**

1. Tried the following features with reverb time, and none of them work
    * vocal onset density
    * mixture beat density
    * mixture downbeat density
    * mixture chord change density
2. Review and modfify the rule-based frequency masking model in the paper


**Meeting:**
Since the audio feature and reverb time do not align, go back to the simple linear reverb time and tempo model.

What to do if deep learning does not show any correlation? The risk is always there. One thing to do is to extend the dataset by source separation.

Prepare audio examples for the Monday presentation. EQ implementation is not necessary.

About the rule-based frequency masking model, apply a K-filter or dBA filter before determining the essential frequency range.

Be aware of overfitting when tuning the rule-based system. Maybe use an iterative process to listen to many audio files and tweak a bit every time. Humans are neural networks and we can be overfitting the problems too.


**To-do:**

1. Rule-based reverb model
2. Rule-based EQ model
3. Audio example for presentation
4. Revise the presentation
5. Get the plugin



* * *

#### 3/30/2022

**Done:**

1. Rule-based EQ implemented
    1. high frequency bands always have higher energy...
    2. 8 octave bands are considered, top 4 difference are chosen for EQ
2. Proposal presentation
3. VAMP dataset has bad quality, needs to manually select usable tracks


**Meeting:**
normalize the band energy with bandwidth
Octave bands may not have enough resolution, 24? 100?
read the DAMP dataset paper

objective evaluation of the baseline system, using some audio encoding algorithm to measure the distance between the baseline and the human mix. The expected result should be: no mix < baseline < human mix.
An alternative is an informal listening test.


**To-do:**

1. Normalize the band RMS with bandwidth
2. Try higher frequency resolution
3. Prepare human mix
3. Read DAMP paper
4. Prepare for data-driven


* * *

#### Proposal Presentation Feedback


###### Proposal Presentation Feedback
Scientific communication:
know the audience, explain some terms. What is knowledge based and data-driven? Baseline, rule-based, mix analysis, what are they??

The final listening example, tell people what to listen for.

Explain the problem of existing systems, how do they Lack of data, and the proposed solution needs to be emphasized.

###### Research Feedback
More specific question for mixing quality, punchiness? or how good is the EQ?

Evaluated by users, or professionals, or both?




* * *

#### 4/6/2022

**Done:**
1. Improve the rule-based EQ
2. Collect songs with acceptable quality for listening test


**Meeting:**

separate data for tuning the system and final listening test

Three options for the rest of the semester:

1. Listening tests preparation
    * questions, score mechanism, people, test environment, duration, IRB
2. Extract ground truth data for all 4 mixing processes
3. Data-driven level balance
    * pick some simple deep learning model first


Let Alex know my decision within two days!!!!

**To-do:**

1. Decide the direction for the rest of the semester
2. Do something


* * *

#### 4/14/2022

**Done:**

1. Extract the ground truth relative loudness on the song level
2. Slice the audio and turn them into (128,64) mel-spectrogram blocks. There are 2 channels. 128 is the mel-spectrum size. the FFT size is 2048, the hop  size is 1024, and 64 of the spectrum are stacked together. In 44100Hz sample rate, one block is about 3s. Other parameters are as default in [https://pytorch.org/audio/stable/transforms.html](https://pytorch.org/audio/stable/transforms.html)

**Meeting:**

1. Sign up for 4/27 meeting if needed.
2. Using 3s audio to predict the target relative loudness may not work. Alternatives can be input features of longer time period.

**To-do:**

1. Finish the model
2. Train
3. Evaluate


* * *

#### 4/20/2022

**Done:**

1. Run the model, terrible results


**Meeting:**

paper presents the baseline. Can talk about the failure, explain why it doesn’t work with evidence.

To verify the DNN model itself, try simple task with simple dataset (change the existing dataset). Generate very simple data for training, and validation. Then we are sure the network is correct.


Validation set is what's been used during the development, and test set is for paper writing.

normalization of target dB

MSE?

predict gain values directly?

Three  possibilities of the terrible results: overfit immediately, or it’s a unlearnable task, or a  stupid mistake.

**To-do:**

1. word: validation != test
2. Paper writing
