import numpy as np
import matplotlib.pyplot as plt  
import random
from api import getTimeSeries


#Generate 5 random numbers between 10 and 30
randomlist = random.sample(range(1000, 2000), 200)
print(randomlist)
    
# store the random numbers in a   
# list  
nums = []  
mu = 100
sigma = 50
    
for i in range(500):  
    temp = random.gauss(mu, sigma) 
    nums.append(temp)  


def volatility(data):
  #list of closing prices
  close_data = [candle["close"] for candle in data]
  stdev = np.std(close_data)
  return stdev/close_data[0]
  
def periodic_volatility(data, resolution = 10):
  close_data = [candle["close"] for candle in data]
  moving_stdev =  [np.std(close_data[i*resolution:(i+1)*resolution]) for i in range(len(close_data)//resolution)]
  

periodic_volatility(getTimeSeries("EURUSD", output="full"))