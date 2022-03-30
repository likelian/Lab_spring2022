# Lab_spring2022

* * *
#### 01/10/2022

original published mix to inform KK mix
Real-time live singing?

TC Electronic's product?


Other:
Pitch Correction must be included

To-do:

1. Find dataset
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
7. dynamic distribution as evaluation metric
8. A milestone-like progress report every week


* * *

#### 3/2/2022

**Done:**

1. Short-term loudness and loudness range implementation (untested)
2. rule-based reverb survey
    1. tempo/reverb time formula
    2. auto-correlation, spectral flux?
3. impulse respoonse matching survey
    1. Genetic algorithm
    2. Hill climbing

**Meeting:**

1. K-filter coefficient error is acceptable, most likely due to floating point error
2. In reverb task, two signals as input can be two large for deep learning
    1. consider vocal as mel-spectrogram, and extracted features from backing tracks (tempo, etc.) as condition. More combinations to be considered and experimented. Interview with mixing engineers for opinions, weighting on the vocal or thhe backing track?
2. barkband and melband as cost function are not very different. But what is the metric to evaluate the impulse response estimation?
3. Since the reverb rule is unclear, extract the tempo(spectral flux) and reverb time from the dataset, and do a linearly fit (or other fit).


**To-do:**

1. rule-based compression implementation
2. verify the commercial tool for IR extraction
    1. reverb applied to dry signal, extract IR, comparing with originnal IR
3. outline the rule-based EQ
4. download dataset

* * *

#### 3/9/2022

**Done:**

1. Rule-based compression implemented
2. Reverb time extracted from MUSDB18 Training set
3. audio features from mixture fail to correlate with reverb time, including:
    1. Tempo
    2. Spectral Centroid Variance
    3. Onset Density
    4. Averaged Spectral Flux
    5. Zero crossing rate


**Meeting:**

It it possible that reverb time is not supposed to corelated with any audio features. Octave errors of tempo detection hurts. 100 songs may not be representative either. The distribution can be some use. The problem is what input to use for the deep learning model.

literature-based reverb rule is still an option.


**To-do:**

1. revisit the code
2. Some more features to try out:
    1. vocal onset density
    2. mixture downbeat density
    3. mixture chord change density
 3. If none of the audio features work, use a literature-based reverb rule.
 4. rule-based EQ
 5. verify the commercial tool for IR extraction

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
4. revise the presentation
5. get the plugin



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

1. normalize the band RMS with bandwidth
2. try higher frequency resolution
3. Prepare human mix
3. read DAMP paper
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
