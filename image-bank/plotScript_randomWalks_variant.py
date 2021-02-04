### 1d random walk (variant) -- plot generator ###
import numpy as np
import matplotlib.pyplot as plt

line_colors = ['#E4C580', '#E862C3']

def length_coin():
	len_aux = 2.9 * np.random.random_sample() + 0.1
	return len_aux

def angle_coin():
    ang_aux = - np.pi * np.random.random_sample() + (np.pi/2)
    return np.sin(ang_aux)

delta = 800
x = np.arange(0, delta, 1)

for plot_index in range(0, 1000):
    f = "0-" + str(plot_index) + ".png"

    y = []
    interval_partOne = np.arange(4, 200, 5)
    interval_partTwo = np.arange(250, 3500, 148)
    interval = np.append(interval_partOne, interval_partTwo)
    value = np.random.choice(interval)

    for item in x:
        value = value + (length_coin() * (angle_coin()/2.))
        # value = value + (angle_coin() / 2.) # <- or maybe this one?
        y.append(value)

    plt.plot(x, y, color = line_colors[np.random.randint(0,2)])

    ax = plt.axes()
    ax.set_facecolor('#163170')
    plt.xticks(size = 12, color = 'white')
    plt.yticks(size = 12, color = 'white')

    #plt.grid()
    plt.savefig(f, extension = 'png', facecolor = '#08114A')
    ax.cla()