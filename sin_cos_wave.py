from matplotlib import pyplot as plt
import numpy as np

times = np.linspace(0, np.pi*2, 100)  # get x value of the sinewave
times2 = np.arange(0, np.pi*2, 0.1)  # alternative of getting x's by linespace

# Amplitude of the sine wave is sine of a variable like time
amplitudes = np.sin(times)
amplitudes2 = np.cos(times2)

# Plot a sine wave using time and amplitude obtained for the sine wave
plt.plot(times, amplitudes, 'r')  # 'r' for red color graph

plt.plot(times2, amplitudes2, 'b')  # 'b' for blue color graph

plt.title('Sine and cos wave')  # Give a title for the sine wave plot

plt.xlabel('Time')  # Give x axis label for the sine wave plot

plt.ylabel('Amplitude = sin(time)')  # Give y axis label for the sine wave plot

plt.grid(True, which='both', axis='both')

plt.axhline(y=0, color='k')  # make the x axis dark(k = black)

plt.show()  # Display the sine wave
