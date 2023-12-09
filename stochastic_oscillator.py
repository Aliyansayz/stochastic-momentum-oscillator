import numpy as np
"""
stochastic_value = stochastic_oscillator (bar , period = 14)

"""
  
def sma (  array, period ):
    import numpy as np
    sma = np.empty_like(array)
    sma = np.full( sma.shape , np.nan)
    # Calculate the EMA for each window of 14 values
    for i in range(period, len(array)+1 ):
          sma[i-1] = np.mean(array[i-period:i] , dtype=np.float16)
    return sma 
     
def sma(array, window):
  
    weights =  np.ones(window) / window
    arr     =  np.convolve(array, weights, mode='valid')
  
    sma = np.empty(window + len(arr), dtype=arr.dtype)
    sma[:window] = np.nan * window
    sma[window:] = arr
    sma[np.isnan(sma)] = np.nanmean(sma)
    
    return sma

def moving_min ( array, period ):
    import numpy as np
    moving_min = np.empty_like(array)
    moving_min = np.full( moving_min.shape , np.nan)
    for i in range(period, len(array)+1 ):
          moving_min[i-1] = np.min(array[i-period:i]  )
    return moving_min

def moving_max (array, period ):
      import numpy as np
      moving_max = np.empty_like(array)
      moving_max = np.full( moving_max.shape , np.nan)
      for i in range(period, len(array)+1 ):
            moving_max[i-1] = np.max(array[i-period:i]  )
      return moving_max     

def moving_end ( array, period ):
      import numpy as np
      moving_end = np.empty_like(array)
      moving_end = np.full( moving_end.shape , np.nan)

      for i in range(period, len(array)+1 ):
            moving_end[i-1] = array[i-1:i] 
      return moving_end     


def  stochastic_oscillator( bar , period):
    
    import numpy as np
    low , high , close = np.array( bar.Low , dtype= np.float16) , np.array( bar.High , dtype=np.float16)  , np.array( bar.Close , dtype = np.float16 ) 
    # calculate %K line
    # low , high , close  = low.reshape(-1,1) , high.reshape(-1,1) , close.reshape(-1,1) 

    lowest_low = moving_min(low  , period  )
    highest_high = moving_max(high , period  )
    close_14 =  moving_end (close, period )

    k_percent = 100 * ( (   close_14   - lowest_low) / (highest_high - lowest_low) )
    # calculate %D line
    d_percent = sma( k_percent  , 3)
    
    return  k_percent


