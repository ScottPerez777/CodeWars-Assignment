# Solution: Even or Odd
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
 # Solution: Convert a Number to a String   
def number_to_string(num):
    return str(num)

# Solution: Remove String Spaces
def no_space(x):
    return "".join(x.split())

# OR, if you chose Vowel Count
def get_count(sentence):
    count = 0
    for char in sentence:
        if char in "aeiou":
            count += 1
    return count