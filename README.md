# Lab_fall2022


* * *

#### 9/6/2022


**Done:**
1. modified Qualtrics questionnaire
2. finished IRB training
3. submitted IRB protocol, wait for IRB feedback
4. installed server environment
5. install Demucs
6. moved more (unorganized) training data to the server
7. ran the training on the server
8. ran the training of the first epoch


**Results:**

* the original [result](https://github.com/likelian/Lab_spring2022/blob/main/results/Loss.png) of 100 epochs
* the [result](https://github.com/likelian/Lab_spring2022/blob/main/results/Loss%20LR%3D0.0001.png) of changing learning rate from 0.0005 to 0.0001
* the [result](https://github.com/likelian/Lab_spring2022/blob/main/results/batch_Loss.png) of every batch in the first epoch
* a sample of the volume ratio prediction in the first epoch:
    * [-2.5375, -2.6064, -2.5929, -2.5967, -2.6080, -2.5770, -2.5852, -2.5408,
        -2.6124, -2.5886, -2.6015, -2.5651, -2.5767, -2.5780, -2.5964, -2.5865,
        -2.4674, -2.3650, -2.3650]
    * I think they are moving close to the average(not verified) of the training dataset and stayed there






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
