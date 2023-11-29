import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(0, 10, 10)
# y = x**2
# # plt.scatter(x, y)
# # plt.show()

# from scipy.interpolate import interp1d

# # attention aux differents types d interpolation nearest etc.
# f = interp1d(x, y, kind='linear')
# new_x = np.linspace(0, 10, 30)
# res = f(new_x)
# plt.scatter(x, y)
# plt.scatter(new_x, res, c='r')
# plt.show()


# ---- optimize.curve_fit -----
# x = np.linspace(0, 2, 100)
# y = 1/3*x**3 - 3/5 * x**2 + 2 + np.random.randn(x.shape[0])/20
# plt.scatter(x,y)

# def f (x, a, b, c, d):
#     return a * x**3 + b * x**2 + c * x + d

# from scipy import optimize

# params, param_cov = optimize.curve_fit(f, x, y)
# plt.scatter(x, y)
# plt.plot(x, f(x, params[0], params[1], params[2], params[3]), c= 'g', lw=3)
# plt.show()


# -----minimize------
# from scipy import optimize
# def f(x):
#     return x**2 + 15*np.sin(x)

# x = np.linspace(-10, 10, 100)
# plt.plot(x, f(x))

# k = optimize.minimize(f, x0= -8)
# print(k)


# ----signal----
# from scipy import signal
# x= np.linspace(0, 20, 100)
# y = x + 4*np.sin(x)  + np.random.randn(x.shape[0])
# plt.plot(x, y)

# new_y = signal.detrend(y)
# plt.plot(x, y)
# plt.plot(x, new_y)
# plt.show()

# ----transformation de fourier----
# x = np.linspace(0, 30, 1000)
# y = 3*np.sin(x) + 2*np.sin(5*x) + np.sin(10*x)

# from scipy import fftpack
# fourier = fftpack.fft(y)
# power = np.abs(fourier)
# frequences = fftpack.fftfreq(y.size)
# plt.plot(np.abs(frequences), power)
# plt.show()


# -------image-------

image = plt.imread('bacteria.jpg')
image = image[:,:,0]
plt.imshow(image)
plt.show()

