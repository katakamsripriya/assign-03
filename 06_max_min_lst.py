# Concept : Dictionaries
# Find Max and Min Value in a dictionary

'''
You will be given a dictionary with a key-value pair

for each key "k" there will be a list [v1,v2,v3,v4] as value

your first task is to find the max and min of each list of each key

example

d1 = {"a":[20,30,10,1], "b":[10,100,1000,3], "c":[30,50,2,5]}

the max and min for "a" is 30 and 1
the max and min for "b" is 1000 and 3
the max and min for "c" is 50 and 2

You have to finally return the list of keys which is having the max and min value 

So for the above dictionary the list will be ["b", "a"] as [max,min] -> "b" having 1000 and "a" having 1

'''

import unittest

def find_max_min_dict(d1):
  mxmn_lst=[]
  dmax = dict()
  dmin = dict()
  #write your code here
  max_lst = []
  min_lst = []
  for i in d1.values():
    x = max(i)
    y = min(i)
    max_lst.append(x)
    min_lst.append(y)
  m = max(max_lst)
  n = min(min_lst)
  d1 = max_lst.index(m)
  d2 = min_lst.index(n)
  s = {0:'a', 1:'b', 2:'c'}
  mxmn_lst.append(s.get(d1))
  mxmn_lst.append(s.get(d2))
  return mxmn_lst

#DO NOT TOUCH THE BELOW CODE
class Max_(unittest.TestCase):
  def test_01(self):
    d1 = {"a":[20,30,60,1], "b":[1000,10,2,4], "c":[40,2000,3,5] }
    
    output = ["c","a"]
    
    self.assertEqual(find_max_min_dict(d1), output)

  def test_02(self):
    d1 = {"a":[2,300,6,100], "b":[10,90,89,4], "c":[40,2,3,5] }
    
    output = ["a","a"]
    
    self.assertEqual(find_max_min_dict(d1), output)

if __name__ == '__main__':
  unittest.main(verbosity=2)
