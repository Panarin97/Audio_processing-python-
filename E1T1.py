import numpy as np
import matplotlib.pyplot as plt
import simpleaudio as sa
import time
import wavio as w
import scipy.fftpack as sf

"Answers to questions are commented below"


def main():

    length = 3  # length in seconds
    amp1, amp2, amp3, amp4 = 1, 2, 3, 4  # amplitudes
    f1, f2, f3, f4 = 100, 500, 1500, 2500  # frequencies in Hz
    fs = 8000  # sampling frequency

    num_samples = fs*length

    samples = np.linspace(0, length, int(fs * length), endpoint=False)  # Creating the sample spaces from 0 to 3

    # Creating the signal samples
    signal1 = amp1*np.sin(2 * np.pi * f1 * samples)
    signal2 = amp2*np.sin(2 * np.pi * f2 * samples + np.pi/3)
    signal3 = amp3*np.sin(2 * np.pi * f3 * samples + 2*np.pi/3)
    signal4 = amp4*np.sin(2 * np.pi * f4 * samples + np.pi)

    # Creating WAV objects
    wave_obj1 = sa.WaveObject(signal1, 2, 2, fs)
    wave_obj2 = sa.WaveObject(signal2, 2, 2, fs)
    wave_obj3 = sa.WaveObject(signal3, 2, 2, fs)
    wave_obj4 = sa.WaveObject(signal4, 2, 2, fs)

    # Playing the signals
    play_obj1 = wave_obj1.play()
    time.sleep(1)
    play_obj1.stop()

    play_obj2 = wave_obj2.play()
    time.sleep(1)
    play_obj2.stop()

    play_obj3 = wave_obj3.play()
    time.sleep(1)
    play_obj3.stop()

    play_obj4 = wave_obj4.play()
    time.sleep(1)
    play_obj4.stop()

    "The sounds are not great but the saved WAV files are good"

    sum = signal1 + signal2 + signal3 + signal4

    wave_obj_sum = sa.WaveObject(sum, 2, 2, fs)
    play_obj_sum = wave_obj_sum.play()
    time.sleep(1)
    play_obj_sum.stop()

    w.write("1.wav", signal1, fs, sampwidth=3)
    w.write("2.wav", signal2, fs, sampwidth=3)
    w.write("3.wav", signal3, fs, sampwidth=3)
    w.write("4.wav", signal4, fs, sampwidth=3)
    w.write("sum.wav", sum, fs, sampwidth=3)

    dim = 512   # dimension for the DFT

    dft = sf.fft(sum, dim)

    "Might need to zoom in to see the actual sinusoid"

    fig, axes = plt.subplots(2, 3)
    axes[0, 0].plot(samples, signal1)
    axes[0, 0].set_title("Sine wave 1")
    axes[0, 1].plot(samples, signal2)
    axes[0, 1].set_title("Sine wave 2")
    axes[0, 2].plot(samples, signal3)
    axes[0, 2].set_title("Sine wave 3")
    axes[1, 0].plot(samples, signal4)
    axes[1, 0].set_title("Sine wave 4")
    axes[1, 1].plot(samples, sum)
    axes[1, 1].set_title("Sum of Sine waves")
    axes[1, 2].plot(dft)
    axes[1, 2].set_title("DFT of the sum")
    plt.show()

    """ While I don't really understand that part, to my understanding and after having done some researched :
    If we choose Nfft to be too big/wide, then the frequency 'classes' are too narrow and 
    we have a 'noisy' frequency representation, if we choose Nfft too small/narrow, then the width of the frequency 
    classes are too wide and we get an over-smooth frequency representation"""


main()
