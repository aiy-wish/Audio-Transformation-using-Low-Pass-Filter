# CMSC388V Final Project: Audio Transformation using Low Pass Filter

## Background

In my initial proposal, i have mentioned that my final project will aim towards removing noise using Fast Fourier Transformation (FFT), which i initially planned to do. However, based on the instructor's feedback on my proposal and my own research on this topic, the project seems a lot harder to implement than i thought of. The challenge here was to be able to work with a realtime audio source, which would make the computation of the FTT a bit hard.

Hence, i have tried something simpler which was to use low-pass filter on `.wav` format audio files where

## Setup

First this

` $ pip install -r requirements.txt`

Then run

`$ python3 denoise.py`
 
The filtered output will be saved in a wav file named `filtered.wav` in the current directory. Once you play the audio, you will notice the difference from the original audio file.

## Implementation

In order to filter out the highest frequencies from any audio signal, we need to choose the cutoff frequency and reduce the signals below that cutoff value. In this project, we chose a cutoff frequency of `400.0 Hz`.

For the filtration, we first extract the raw audio, the frame rate, amp width, number of channels and number of frames from the wav file. We then call a method which interprets the input wav file and returns the channel's shape based on the fact that the channels are interleaved or not. The method and it's parameters are given below:
```python
def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):
```
After the interpretation, we then find the moving average of the channels. The reason why we need this calculations is because we need to filter out the highest frequencies and bring it below the cutoff based on the average we calculate. Just like how mean works, we find the cummulative sum of the channels after interpretation and divide that by the size N. The equation used is given below:

![equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/9662585f6a706ef68d22484389a861cbc67b21cc)

(If you are viewing this markdown file in dark mode, the color of this equation blends with that, you may click on the image above which then redirects you to the equations page).

The method and it's parameters are given below:
```python
def running_mean(x, windowSize):
```

And after finding the running mean, we then write to the output wav file named `filtered.wav` which has the filtered version of the input wav file. Then we analyze the graphs by plotting the wav file on a plot graph and a specgram which gives an detailed output of what the wav file now looks like. You can see how the frequencies have been filtered out once you compare both frequencies.


## Results

Conclusion is that blah blah blah

Before

After

## References
- https://www.wavsource.com/video_games/pac-man.htm
- https://en.wikipedia.org/wiki/Moving_average
- http://stackoverflow.com/questions/13728392/moving-average-or-running-mean
- http://stackoverflow.com/questions/2226853/interpreting-wav-data/2227174#2227174
- http://dsp.stackexchange.com/questions/9966/what-is-the-cut-off-frequency-of-a-moving-average-filter
