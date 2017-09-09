'''Assignment: String and List.  

Use only the built-in methods and functions from the previous tabs to do
the following exercises. You will find the following methods and functions useful:
.find()
.replace()
.min()
.max()
.sort()
.len()
Find and Replace
In this string: words = "It's thanksgiving day. It's my birthday,too!" 
print the position of the first instance of the word "day". 
Then create a new string where the word "day" is replaced with the word "month".
Min and Max
Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. 
Your code should work for any list.
First and Last
Print the first and last values in a list like this one:
x = ["hello",2,54,-2,7,12,98,"world"]. 
Now create a new list containing only the first and last values in the original list. 
Your code should work for any list.
New List
Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. 
Sort your list first. Then, split your list in half. 
Push the list created from the first half to 
position 0 of the list created from the second half. 
The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. 
Stick with it, this one is tough!
'''

words = "It's thanksgiving day.  It's my birthday, too!"
day = words.find("day")
print("first instance of day is at: {}".format(day))
new_words = words.replace("day","month")
print(new_words)
x = [2, 54, -2, 7, 12, 98]
maximum = max(x)
minimum = min(x)
print(maximum, minimum)
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print(x[0], x[-1])
x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
sort_x = sorted(x)
print("sort_x: {}".format(sort_x))
sort_x_len = len(sort_x)
midpoint = round(sort_x_len/2)
print("lenght of sort_x: {}".format(sort_x_len))
first = sort_x[0:midpoint-1]
print(first)
second = sort_x[midpoint-1:]
print(second)
second.insert(0,first)
print(second)
