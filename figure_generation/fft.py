import scipy
import numpy


N = 200
T = 1.0 / 800.0
x = numpy.linspace(0, N*T, N, endpoint=False)
y = numpy.sin(50.0 * 2.0 * numpy.pi*x) + 0.5 * numpy.sin(80.0 * 2.0 * numpy.pi*x)

yf = scipy.fft.fft(y)
xf = scipy.fft.fftfreq(N, T)[:N//2]

import matplotlib.pyplot as plt

# plt.plot(xf, 2.0/ N * numpy.abs(yf[0:N//2]))
plt.plot(x,y)
plt.grid()
plt.show()
