"""
Customized Indicator For Stochastic Momentum Index With Smi line and Smi_Ema line 

if smi crosses above smi_ema then go long and crosses below go short. 
"""

class stochastic_momentum_index(stochastic_oscillator):

  def  stochastic_momentum_index(self, high, low, close, period= 20, ema_period = 5):

      lowest_low   = self.moving_min(low  , period )
      highest_high = self.moving_max(high , period )
      relative_range   = close - (( highest_high + lowest_low ) / 2 )
      highest_lowest_range = highest_high -   lowest_low

      relative_range_smoothed       = self.ema(self.ema(relative_range,ema_period),ema_period)
      highest_lowest_range_smoothed = self.ema(self.ema(highest_lowest_range,ema_period),ema_period)

      smi = [ (relative_range_smoothed[i] / (highest_lowest_range_smoothed[i] / 2)) * 100 if highest_lowest_range_smoothed[i] != 0 else 0.0
              for i in range(len(relative_range_smoothed)) ]

      # relative_range = (lowest_low - highest_high) / highest_lowest_range
      # calculate smi with  %D length      
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
