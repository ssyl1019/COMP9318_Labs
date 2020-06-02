# import submission as submission
from submission import *
import re

def print_tree(root, indent=0):
    print(' ' * indent, root)
    if len(root.children) > 0:
        for child in root.children:
            print_tree(child, indent+4)

t = Tree('*', [Tree('1'),
               Tree('2'),
               Tree('+', [Tree('3'),
                          Tree('4')])])
print_tree(t)
def myfind(s, char):
    pos = s.find(char)
    if pos == -1: # not found
        return len(s) + 1
    else: 
        return pos

def next_tok(s): # returns tok, rest_s
    if s == '': 
        return (None, None)
    # normal cases
    poss = [myfind(s, ' '), myfind(s, '['), myfind(s, ']')]
    min_pos = min(poss)
    if poss[0] == min_pos: # separator is a space
        tok, rest_s = s[ : min_pos], s[min_pos+1 : ] # skip the space
        if tok == '': # more than 1 space
            return next_tok(rest_s)
        else:
            return (tok, rest_s)
    else: # separator is a [ or ]
        tok, rest_s = s[ : min_pos], s[min_pos : ]
        if tok == '': # the next char is [ or ]
            return (rest_s[:1], rest_s[1:])
        else:
            return (tok, rest_s)
        
def str_to_tokens(str_tree):
    # remove \n first
    str_tree = str_tree.replace('\n','')
    out = []
    
    tok, s = next_tok(str_tree)
    while tok is not None:
        out.append(tok)
        tok, s = next_tok(s)
    return out

str_tree = '''
1 [2 [3 4       5          ] 
   6 [7 8 [9]   10 [11 12] ] 
   13
  ]
'''
# toks = str_to_tokens(str_tree)
# print(toks)
# print()
# tt = submission.make_tree(toks)
# print_tree(tt)
# print()
# depth = submission.max_depth(tt)
print()
depth = max_depth(t)
print(depth)