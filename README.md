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
 
