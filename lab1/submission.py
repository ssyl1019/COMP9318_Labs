## import modules here 

################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    #pass # **replace** this line with your code
    if(x<1):
    	return 0
    else :
    	high = x
    	low = 1
    	mid = (high + low)//2
    	while True :
    		if  (mid**2>x) :
    			high = mid
    			mid = (high + low)//2
    		elif ((mid**2<x) and (high-low>1)):
    			low = mid
    			mid = (high + low)//2
    		else :
    			break
    	return mid


################# Question 2 #################


# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them

def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    # pass # **replace** this line with your code
    x_1 = x_0
    while MAX_ITER :
    	x_0 -= f(x_0)/fprime(x_0)
    	MAX_ITER -= 1
    	if(abs(x_1-x_0)<EPSILON):
    		break
    	x_1 = x_0
    	# print(x_0,f(x_0))
    return x_0


################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def make_tree(tokens): # do not change the heading of the function
    # pass # **replace** this line with your code    
    t = Tree(tokens[0])
    i = 2
    while i<len(tokens)-1:
    	j = 1
    	if(tokens[i].isdigit() and tokens[i+1].isdigit()):
    		t.add_child(Tree(tokens[i]))
    	elif(tokens[i].isdigit() and tokens[i+1]=="["):
    		j += 1
    		brkNum = 1
    		while brkNum :
    			if(tokens[i+j]=="["):
    				brkNum += 1
    			elif(tokens[i+j]=="]"):
    				brkNum -= 1
    			j += 1
    		t.add_child(make_tree(tokens[i:i+j]))
    	elif(tokens[i].isdigit() and tokens[i+1]=="]"):
    		t.add_child(Tree(tokens[i]))
    	i += j
    return t

def max_depth(root): # do not change the heading of the function
    # pass # **replace** this line with your code
    if(root.children == []):
    	return 1
    else :
    	maxD = 1
    	for child in root.children :
    		currD = max_depth(child)
    		if(currD>maxD):
    			maxD = currD
    	return maxD + 1