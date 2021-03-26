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

**Next we explore optimizations**

Obviously each time s is multiplied, we start from the beginning of t all over again. Considering we made it as far as we did into t there's no reason to search for those characters again. So lets keep a count for every time we explore all of s.

This was a difficult solution to come to, because it utilizes an infinite loop and break statement, which is VERY bad practice normally. Handling the conditions that could lead to this loop being actually infinite gives me confidence in this solution. I will continue to explore alternative solutions. 

*see first_optimized.py*

