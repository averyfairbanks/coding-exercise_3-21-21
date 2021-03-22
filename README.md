You are given Two Strings say s and t. How many times should s repeat inorder to construct all characters from t in the same order?
eg:  
s = cbbda 
t = cab
return 2 

eg:
s = siexampl 
t = alexis 
return 4

**Beginning with the most brute force answer possible:**

Iterate over s looking for each character t in order. If not found, increment a counter (times, in this case). Multiply the string by times, then begin again. When all characters are found in order, exit the method and return times.

*see brute_force.py*