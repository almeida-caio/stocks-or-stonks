### draft - 1d random walk or stock prices? ###
## https://tradeoptionswithme.com/random-walk-theory/
import numpy as np
import matplotlib.pyplot as plt

def length_coin():
	len_aux = 2.9 * np.random.random_sample() + 0.1
	return len_aux

def angle_coin():
    ang_aux = - np.pi * np.random.random_sample() + (np.pi/2)
    return np.sin(ang_aux)

x = np.arange(0, 800, 1)

for iteration in range(0,1):
    y = []
    interval_partOne = np.arange(4, 200, 5)
    interval_partTwo = np.arange(250, 3500, 148)
    interval = np.append(interval_partOne, interval_partTwo)
    value = np.random.choice(interval)

    for item in x:
        value = value + (length_coin() * (angle_coin()/2.))
        # value = value + (angle_coin() / 2.) # <- or maybe this one!
        y.append(value)
        
    plt.plot(x,y)
    # plt.hist(y, bins = 45)
    # print(np.mean(y))
    # plt.yscale('log')

plt.show()
