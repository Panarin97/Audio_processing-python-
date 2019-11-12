import librosa
import matplotlib.pyplot as plt
import scipy.fftpack as sf
import wavio as w
import numpy as np



def func1(interval, y1, s1):

    length = len(y1)/s1
    start = 0
    end = ((interval/1000)/length)*len(y1)

    hamming = np.hamming(len(y1[int(start): int(end)]))  # window size = however many elements in the interval

    y1[int(start): int(end)] = y1[int(start): int(end)] * hamming  # apply hamming

    # Show the first interval's plot and its dft
    plt.plot(y1)
    plt.xlim(start, end)
    plt.show()

    dft = sf.fft(y1[int(start) : int(end)])
    plt.plot(dft)
    plt.show()

    dfts = []
    # count = 1

    for i in range(int(len(y1)/end)-1):
        start = end - ((interval/1000)/length)*len(y1)/2  # new start = end - half of the interval
        end = end + ((interval/1000)/length)*len(y1)/2  # new end = end + half of the interval, hence 50% overlap
        y1[int(start): int(end)] = y1[int(start): int(end)] * hamming
        dft = sf.fft(y1[int(start): int(end)])
        dfts.append(dft)

        """
        count+=1
        print(count ,": ", dft)
        """
    np.concatenate(dfts)
    print("total number of dfts: ",len(dfts))
    print(dfts)
    plt.plot(dfts)
    plt.show()

    dfts_log = np.log(dfts)
    plt.plot(dfts_log)
    plt.show()



def main():

    y1, s1 = librosa.load("audio1.wav")
    y2, s2 = librosa.load("audio2.wav")  # might need FFMPEG for this!!!

    plt.plot(y1)
    plt.show()
    length = len(y1)/s1

    plt.plot(y1)
    plt.xlim((0.5/length)*len(y1), (1/length)*len(y1))
    plt.show()

    interval = 100  # ms

    spect = librosa.stft(y1, hop_length=int((1/length)*len(y1) - (0.5/length)*len(y1)))
    plt.plot(spect)
    plt.show()

    func1(interval, y1, s1)





main()