def StringScramble(str1,str2):
    
  # code goes here
  outer_str = str1
  inner_str = str2
  for ch in inner_str:
    if ch not in outer_str:
      return False
    new_outer = outer_str.replace(ch, "", 1)
    outer_str = new_outer
  return True

# keep this function call here 
print(StringScramble(raw_input()))