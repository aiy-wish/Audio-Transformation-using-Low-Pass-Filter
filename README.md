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
`def running_mean(x, windowSize)`
`def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):`

## Conclusion

Conclusion is that blah blah blah

Before

After

## References
- https://www.wavsource.com/video_games/pac-man.htm
- http://stackoverflow.com/questions/13728392/moving-average-or-running-mean
- http://stackoverflow.com/questions/2226853/interpreting-wav-data/2227174#2227174
- http://dsp.stackexchange.com/questions/9966/what-is-the-cut-off-frequency-of-a-moving-average-filter
