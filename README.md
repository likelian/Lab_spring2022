# Lab_fall2022


* * *

## 9/27/2022

### **Thoughts:**

1. read a paper, [Automatic music mixing with deep learning and out-of-domain data](https://marco-martinez-sony.github.io/FxNorm-automix/).
2. [Mean absolute percentage error](https://en.wikipedia.org/wiki/Mean_absolute_percentage_error)
3. The result of the paper may not be so good as it seems. The reults are averaged over the song (0.5s window). The loudness measure is LUFS, and it is absolute. So abs((-18dB-(-19dB))/(-19dB)) = 0.05, while I am using relative loudness. The audio is good, but not that close to the reference mix. The dry stems are pretty good by themselves.





### **Done:**

1. move partial MSD
2. separate partial MSD

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
