"""Created on Sat Sep 22 15:37:52 2018
@author: BANERJEE, Rohini (Student ID: 20543577)
MSBD5002: Data Mining and Knowledge Discovery (Assignment 1)
Title: Implementation of Hash Tree using Python 3"""


"""Class representing the structure of the Hash Tree Node
Each node has 3 leaf lists and 3 initially empty nodes."""
class hashTreeNode:
    def __init__(self):
        self.left = []
        self.right = []
        self.mid = []
        self.nodeleft = None
        self.noderight = None
        self.nodemid = None

"""Function representing the hash function provided in the question."""
def hash_function(item):
    n = item % 3
    return n 

"""Function to group the itemsets into the left, middle and right lists
based on a given index value."""
def distribute_items(pres_node,item,ind):
    num = hash_function(item[ind])
    # If H[x] mod 3 == 1, then update the item to left list of the node
    if num == 1:
        pres_node.left.append(item)
    # If H[x] mod 3 == 0, then update the item to right list of the node
    elif num == 0:
        pres_node.right.append(item)
    # If H[x] mod 3 == 2, then update the item to middle list of the node
    elif num == 2:
        pres_node.mid.append(item)

"""Recursive function for creating the hash tree.
The left, right and middle empty nodes are activated and split if the length
of their corresponding lists increase the maximum leaf size."""
def create_hash_tree(node, data, ind, leaf_size = 3):
    for item_set in data:
        distribute_items(node,item_set,ind) 
    # temp_index helps to increment index during the recursive calls.
    temp_ind = ind
    if len(node.left) > leaf_size:
        # Left node is activated with the left list as its dataset.
        node.nodeleft = hashTreeNode()
        create_hash_tree(node.nodeleft, node.left, temp_ind+1, max_leaf)
    if len(node.right) > leaf_size:
        # Right node is activated with the right list as its dataset.
        node.noderight = hashTreeNode()
        create_hash_tree(node.noderight, node.right, temp_ind+1, max_leaf)
    if len(node.mid) > leaf_size:
        # Middle node is activated with the middle list as its dataset.
        node.nodemid = hashTreeNode()
        create_hash_tree(node.nodemid, node.mid, temp_ind+1, max_leaf)

"""Recursive function for printing the hash tree as a nested list.
The function starts from the left node of the root.
The root is taken care of in the main program"""
def print_hash_tree(node, temp_global):
    temp = []
    # If a node has no child nodes then append the 3 leafs directly
    if node.nodeleft==None and node.nodemid==None and node.noderight==None:
        temp.append(node.left)
        temp.append(node.mid)
        temp.append(node.right)
        temp_global.append(temp)
        temp_global = [item for sublist in temp_global for item in sublist]
    else:
        # if a node has no left child node, append the left leaf value
        # else call the function for the left node child
        if node.nodeleft == None:
            temp_global.append(node.left)
        else:
            print_hash_tree(node.nodeleft, temp_global)
        # if a node has no middle child node, append the middle leaf value
        # else call the function for the middle node child
        if node.nodemid == None:
            temp_global.append(node.mid)
        else:
            print_hash_tree(node.nodemid,temp_global)
        # if a node has no right child node, append the right leaf value
        # else call the function for the right node child
        if node.noderight == None:
            temp_global.append(node.right)
        else:
            print_hash_tree(node.noderight,temp_global)


"""The following is the main part of the code.
It starts with the candidate itemset given in a proper nested list order.
The maximum leaf size is mentioned - for this example it is taken to be 3.
A root node is created for the hash tree.
The index for splitting the itemsets is taken to be 0 initially."""
data = [[1,2,4], [1,2,9], [1,3,5], [1,3,9], [1,4,7], [1,5,8], [1,6,7],[1,7,9],\
        [1,8,9],[2,3,5], [2,4,7], [2,5,6], [2,5,7], [2,5,8], [2,6,7], [2,6,8],\
        [2,6,9], [2,7,8],[3,4,5], [3,4,7], [3,5,7], [3,5,8], [3,6,8], [3,7,9],\
        [3,8,9],[4,5,7], [4,5,8], [4,6,7], [4,6,9], [4,7,8],[5,6,7], [5,7,9], \
        [5,8,9], [6,7,8], [6,7,9]]
max_leaf = 3
root = hashTreeNode()
index = 0
# The hash tree is created with the given itemset and the maximum leaf size
create_hash_tree(root, data, index, max_leaf)
# The hash tree is printed in hierarchical nested list format
nested_hash_tree = []
temp1 = []
# If the root itself has no child nodes, the nested_hash_tree is appended
if root.nodeleft==None and root.nodemid==None and root.noderight==None:
    nested_hash_tree.append(root.left)
    nested_hash_tree.append(root.mid)
    nested_hash_tree.append(root.right)
# Else, for each existing node, the recursive print function is called
else:    
    if root.nodeleft == None:
        nested_hash_tree.append(root.left)
    else:
        print_hash_tree(root.nodeleft,temp1)
        nested_hash_tree.append(temp1)
        temp1=[]
    if root.nodemid == None:
        nested_hash_tree.append(root.mid)
    else:
        print_hash_tree(root.nodemid,temp1)
        nested_hash_tree.append(temp1)
        temp1=[]
    if root.noderight == None:
        nested_hash_tree.append(root.right)
    else:
        print_hash_tree(root.noderight,temp1)
        nested_hash_tree.append(temp1)
        temp1=[]
# The nested_hash_tree has the hash tree in hierarchical nested list format
print('\n\n',nested_hash_tree,'\n\n')