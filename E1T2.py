import librosa
import matplotlib.pyplot as plt
import scipy.fftpack as sf
import wavio as w


def func1(interval, y1, s1):

    length = len(y1)/s1
    start = 0
    end = ((interval/1000)/length)*len(y1)

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
        start = end
        end = end + ((interval/1000)/length)*len(y1)
        dft = sf.fft(y1[int(start): int(end)])
        dfts.append(dft)

        """
        count+=1
        print(count ,": ", dft)
        """

    print("total number of dfts: ",len(dfts))


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

    #  create a sum of 2 signals
    if len(y2) < len(y1):
        y3 = y1.copy()
        y3[:len(y2)] += y2
    else:
        y3 = y2.copy()
        y3[:len(y1)] += y1

    func1(interval, y1, s1)
    func1(interval, y2, s2)
    func1(interval, y3, s2)

    w.write("sum2.wav", y3, s2, sampwidth=3)  # testing the sum

    """The dft of the speech is, of of course, much more complex and has many more frequencies in it while the
    first audio signal is simply a summation of a few frequencies, the sum if the combination of the two"""



main()
