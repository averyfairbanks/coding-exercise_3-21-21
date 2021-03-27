# 3-21-21 Problem
***
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
***

Iterate over s looking for each character t in order. If not found, increment a counter (times, in this case). Multiply the string by times, then begin again. When all characters are found in order, exit the method and return times.

*see brute_force.py*

### Next we explore optimizations
***

Obviously each time s is multiplied, we start from the beginning of t all over again. Considering we made it as far as we did into t there's no reason to search for those characters again. So lets keep a count for every time we explore all of s.

This was a difficult solution to come to, because it utilizes an infinite loop and break statement, which is VERY bad practice normally. Handling the conditions that could lead to this loop being actually infinite gives me confidence in this solution. I will continue to explore alternative solutions. 

*see first_optimized.py*

### Getting rid of that pesky infinite loop
***

Perhaps we could set a temporary variable = to the current value of times before entering the loop and have the exit condition be "while times <= times_on_entry + 1:". If all the letters in t are present in s then you will not iterate more than once through s, which translate to times being at max one higher than when it entered the loop.

*see second_optimized.py*

### Removing redundant work and optimizing character check method
***

I realized I was using two while loops to deal with an issue that was only present in an earlier iteration of the code. Instead, I changed the outer loop to a for loop and merged i and s_idx because there was no reason to have both. Sometimes its hard to realize you're coding for problems that your latest solution has already covered. I needed some distance from this problem.

*see third_optimized.py*

### A whole new approach
***

In the constant pursuit of O(n) time for this particular problem, I've started over utilizing a dictionary/map to achieve it. While this current iteration isn't quite there yet, I believe I'm close. This method first builds a dictionary with all chars in t as keys. 

__ex:__</br>
__s = "cbbda" 
t = "cab"__</br>
__our_dict = d = {‘c’: [0], ‘a’: [4], ‘b’: [1, 2]}__

Then it fills the arrays associated with these keys with the indices that that character appears at in s. Then, each character in t is visited in order, checking the indices associated with it. If the next character has an index that is higher, then we select that as our current index. If it does not, then we pick the smallest index the character appears at and increment times. This is because if we have a smaller index after a larger one, obviously we've loop back around.

The last thing left to do is optimize this search through the indices. I'm imagining that binary search for a value higher than our current index is the first optimization I should make, but I'm still searching for O(n)

*see new_approach.py*