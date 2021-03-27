# 3-21-21 Problem
You are given Two Strings say s and t. How many times should s repeat inorder to construct all characters from t in the same order?
eg:  
s = cbbda 
t = cab
return 2 

eg:
s = siexampl 
t = alexis 
return 4

### Beginning with the most brute force answer possible:


Iterate over s looking for each character t in order. If not found, increment a counter (times, in this case). Multiply the string by times, then begin again. When all characters are found in order, exit the method and return times.

*see brute_force.py*

### Next we explore optimizations

Obviously each time s is multiplied, we start from the beginning of t all over again. Considering we made it as far as we did into t there's no reason to search for those characters again. So lets keep a count for every time we explore all of s.

This was a difficult solution to come to, because it utilizes an infinite loop and break statement, which is VERY bad practice normally. Handling the conditions that could lead to this loop being actually infinite gives me confidence in this solution. I will continue to explore alternative solutions. 

*see first_optimized.py*

### Getting rid of that pesky infinite loop

Perhaps we could set a temporary variable = to the current value of times before entering the loop and have the exit condition be "while times <= times_on_entry + 1:". If all the letters in t are present in s then you will not iterate more than once through s, which translate to times being at max one higher than when it entered the loop.

*see second_optimized.py*

### Removing redundant work and optimizing character check method

I realized I was using two while loops to deal with an issue that was only present in an earlier iteration of the code. Instead, I changed the outer loop to a for loop and merged i and s_idx because there was no reason to have both. Sometimes its hard to realize you're coding for problems that your latest solution has already covered. I needed some distance from this problem.