# Concept : Strings

# Manipulate string

'''
Given a string S and a character C (as string of length 1), return a string with the characters surrounding any occurrence of C reversed. 

For example, if S is "Hello beautiful world" and C is a space, return "Hellb oeautifuw lorld". 

Skip any positions where C occurs twice in a row.
'''
import unittest
def manipulate_string(S,C):
  i = 0
  ansst = ""
  # write your code here
  for j in S:
    if j == C:
      i += 1
  if i == 1:
    a = S.find(C)
    ansst = S[:a-1] + S[a+1] + C + S[a-1] + S[a+2:]
    return ansst
  elif i >1:
    a = S.find(C)
    x = S[:a-1] + S[a+1] + C + S[a-1] + S[a+2:]
    v = S.rfind(C)
    ansst = x[:v-1] + x[v+1] + C + x[v-1] + x[v+2:]
  return ansst



class Dict_to_list(unittest.TestCase):
  def test_01(self):
    self.assertEqual(manipulate_string('Hello beautiful world', ' '), 'Hellb oeautifuw lorld')

  def test_02(self):
    self.assertEqual(manipulate_string('Hello-World', '-'), 'HellW-oorld')

  def test_03(self):
    self.assertEqual(manipulate_string('Gf oish!', ' '), 'Go fish!')


if __name__ == '__main__':
  unittest.main(verbosity=2)
