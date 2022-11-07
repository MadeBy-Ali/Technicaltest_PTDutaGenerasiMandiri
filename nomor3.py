inp_str = "Bismillahhh"
  
freq = {}
  
for i in inp_str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
  
print ("Output :\n " +  str(freq))