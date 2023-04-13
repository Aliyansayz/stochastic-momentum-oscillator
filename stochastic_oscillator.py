import numpy as np
"""
stochastic_value = stochastic_oscillator (bar , period = 14)

"""
def moving_min (array, period ):

    moving_min = np.empty_like(array)
    moving_min = np.full( moving_min.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          moving_min[i-1] = np.min(array[i-period:i] , dtype=np.float16 )
    return moving_min

def moving_max (array, period ):

    moving_max = np.empty_like(array)
    moving_max = np.full( moving_max.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          moving_max[i-1] = np.max(array[i-period:i] , dtype=np.float16 )
    return moving_max     


def moving_end (array, period ):

    moving_end = np.empty_like(array)
    moving_end = np.full( moving_end.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          moving_end[i-1] = np.array(array[i-1:i] , dtype=np.float16 )
    return moving_end     
  
def sma (array, period ):

    sma = np.empty_like(array)
    sma = np.full( sma.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          sma[i-1] = np.mean(array[i-period:i] , dtype=np.float16)
    return sma 
       
  
period = 14
def  stochastic_oscillator(bar , period):
  
    low , high , close = np.array( bar["Low"] , dtype=np.float16) , np.array( bar["High"] , dtype=np.float16)  , np.array( bar["Close"] , dtype=np.float16 ) 
    # calculate %K line
    lowest_low = moving_min(low  , period  )
    highest_high = moving_max(high , period  )
    close_14 =  moving_end (close, period )

    k_percent = 100 * ( (   close_14   - lowest_low) / (highest_high - lowest_low) )
    # calculate %D line
    d_percent = sma( k_percent  , period = 3)
    
    
