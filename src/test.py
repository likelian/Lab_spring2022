import sys
#sys.path.append('/usr/local/lib/python3.8/site-packages')
import essentia
#import essentia.standard

LoudnessEBUR128 = essentia.stream.LoudnessEBUR128(sampleRate=rate, hopSize=hop_size)
