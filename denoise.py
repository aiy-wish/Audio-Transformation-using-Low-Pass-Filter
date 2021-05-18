import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import math
import contextlib
from scipy.io import wavfile


#https://www.wavsource.com/video_games/pac-man.htm
fname = 'sample_inputs/pacman_x.wav'
outname = 'filtered.wav'

cutOffFrequency = 400.0

# from http://stackoverflow.com/questions/13728392/moving-average-or-running-mean
def running_mean(x, windowSize):
  cumsum = np.cumsum(np.insert(x, 0, 0)) 
  return (cumsum[windowSize:] - cumsum[:-windowSize]) / windowSize

def plotGraph(filename,title,savetitle,flag):
    
    signal_wave = wave.open(filename, 'r')
    sample_rate = 16000
    sig = np.frombuffer(signal_wave.readframes(sample_rate), dtype=np.int16)
    sig = sig[:]
    
    #plt.figure(1)
    plt.figure(figsize=(16, 8)) 
    plt.title(title)

    plot_a = plt.subplot(211)
    plot_a.plot(sig)
    plot_a.set_xlabel('sample rate * time')
    plot_a.set_ylabel('energy')

    plot_b = plt.subplot(212)
    plot_b.specgram(sig, NFFT=1024, Fs=sample_rate, noverlap=900)
    plot_b.set_xlabel('Time')
    plot_b.set_ylabel('Frequency')

    #if (flag == True):
    #    plt.draw()

    #plt.show()
    plt.savefig(savetitle)

def plotTwoGraph(filename,outname,title,savetitle,flag):
    
    signal_wave1 = wave.open(filename, 'r')
    signal_wave2 = wave.open(outname, 'r')

    sample_rate = 16000
    sig1 = np.frombuffer(signal_wave1.readframes(sample_rate), dtype=np.int16)
    sig2 = np.frombuffer(signal_wave2.readframes(sample_rate), dtype=np.int16)

    sig1 = sig1[:]
    sig2 = sig2[:]

    
    #plt.figure(1)
    plt.title(title)

    plot_a = plt.subplot(211)
    plot_a.plot(sig2)
    plot_a.set_xlabel('sample rate * time')
    plot_a.set_ylabel('energy')

    plot_b = plt.subplot(212)
    plot_b.specgram(sig2, NFFT=1024, Fs=sample_rate, noverlap=900)
    plot_b.set_xlabel('Time')
    plot_b.set_ylabel('Frequency')

    if (flag == True):
        plt.gca()


    #plt.show()
    plt.savefig(savetitle)




# from http://stackoverflow.com/questions/2226853/interpreting-wav-data/2227174#2227174
def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):

    if sample_width == 1:
        dtype = np.uint8 # unsigned char
    elif sample_width == 2:
        dtype = np.int16 # signed 2-byte short
    else:
        raise ValueError("Only supports 8 and 16 bit audio formats.")

    channels = np.fromstring(raw_bytes, dtype=dtype)

    if interleaved:
        # channels are interleaved, i.e. sample N of channel M follows sample N of channel M-1 in raw data
        channels.shape = (n_frames, n_channels)
        channels = channels.T
    else:
        # channels are not interleaved. All samples from channel M occur before all samples from channel M-1
        channels.shape = (n_channels, n_frames)

    return channels

def main():
    spf = wave.open(fname,'rb')
    sampleRate = spf.getframerate()
    ampWidth = spf.getsampwidth()
    nChannels = spf.getnchannels()
    nFrames = spf.getnframes()

    # Extract Raw Audio from multi-channel Wav File
    signal = spf.readframes(nFrames*nChannels)
    spf.close()
    channels = interpret_wav(signal, nFrames, nChannels, ampWidth, True)

    # get window size
    # from http://dsp.stackexchange.com/questions/9966/what-is-the-cut-off-frequency-of-a-moving-average-filter
    freqRatio = (cutOffFrequency/sampleRate)
    N = int(math.sqrt(0.196196 + freqRatio**2)/freqRatio)

    # Use moviung average (only on first channel)
    filtered = running_mean(channels[0], N).astype(channels.dtype)

    wav_file = wave.open(outname, "w")
    wav_file.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
    wav_file.writeframes(filtered.tobytes('C'))
    wav_file.close()

    flag = False
    plotGraph(fname,"Before Filtering",'Figure1.png',False)
    plotTwoGraph(fname,outname,"Comparison",'Figure3.png',True)
    plotGraph(outname,"After Filtering",'Figure2.png',False)


if __name__ == "__main__":
    main()
