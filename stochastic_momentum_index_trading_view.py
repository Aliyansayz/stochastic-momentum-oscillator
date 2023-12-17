"""
Official Usage By Trading View 
"""

class stochastic_momentum_index:

  def moving_min (self, array, period ):
      moving_min = np.empty_like(array)
      moving_min = np.full( moving_min.shape , 0.0)
      for i in range(period, len(array)+1 ):
            moving_min[i-period] = np.min(array[i-period:i]  )
      # moving_min[np.isnan(moving_min)] = np.nanmean(moving_min)
      return moving_min

  def moving_max (self, array, period ):
        moving_max = np.empty_like(array)
        moving_max = np.full( moving_max.shape , 0.0)
        # moving_max[:period] = np.max(array[:period])  
        for i in range(period, len(array)+1 ):
              moving_max[i-period] = np.max(array[i-period:i]  )
        # moving_max[np.isnan(moving_max)] = np.nanmean(moving_max)
        return moving_max

  def ema (self, array, period ):

        ema = np.empty_like(array)
        ema = np.full( ema.shape , 0.0)
        ema[0] = np.mean(array[0] , dtype=np.float64)
        alpha  = 2 / (period + 1)
        for i in range(1 , len(array) ):
              ema[i] = (array[i] * alpha +  ema[i-1]  * (1-alpha) )
        return ema

  def  stochastic_momentum_index(self, high, low, close, period= 20, ema_period = 5):

      lengthD = ema_period
      lowest_low   = self.moving_min(low  , period )
      highest_high = self.moving_max(high , period )
      relative_range   = close - ( highest_high + lowest_low ) / 2
      highest_lowest_range = highest_high -   lowest_low

      # relative_range = (lowest_low - highest_high) / highest_lowest_range
      # calculate smi with  %D length
      smi = 200 * (self.ema(relative_range, lengthD) / self.ema(highest_lowest_range, lengthD))
      smi_ema = self.ema(smi,  ema_period)

      return  smi, smi_ema


  def  stochastic_momentum_lookback(self, bar_list, period = 20, lookback = 10, ema_period = 5 ):

      symbols, values = 0, 1
      stochastic_momentum_list  =  [[]] * len(bar_list[values])
      for index, ohlc in enumerate(bar_list[values]):

          high,  low,   close  =   ohlc['High'],  ohlc['Low'],  ohlc['Close']
          smi, smi_ema = self.stochastic_momentum_index( high, low, close, period, ema_period)

          if lookback :
            smi, smi_ema   =  smi[-lookback:], smi_ema[-lookback:]

          stochastic_momentum = [ [ smi[i], smi_ema[i]] for i in range( len(smi) )]
          stochastic_momentum_list[index] = stochastic_momentum

      return   stochastic_momentum_list
