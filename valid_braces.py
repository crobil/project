def validBraces(string):
  a_open=0
  a_close=0
  b_open=0
  b_close=0
  c_open=0
  c_close=0
  
  #check braces count
  for item in string:
      if item =='(':
          a_open += 1
      elif item ==')':          
          a_close += 1
          if a_open-a_close < 0:
              return False
      elif item =='[':
          b_open += 1
      elif item ==']':
          b_close += 1
          if b_open-b_close < 0:
              return False
      elif item =='{':
          c_open += 1
      elif item =='}':
          c_close += 1
          if c_open-c_close < 0:
              return False
          
  if a_open-a_close == 0 and b_open-b_close == 0 and c_open-c_close == 0:
      return True
  else:
      return False
