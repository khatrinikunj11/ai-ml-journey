s = set() 
s.add(20)
s.add(20.0)
s.add('20')
print(len(s))  # Output: 2
# In Python, the integer 20 and the float 20.0 are considered equal when compared