
# Hash Tree Implementation (Python 3)
It is a well known Apriori principle that if an itemset is frequent, then all its subsets must also be frequent. For implementing the above principle, the transactions database needs to be scanned to determine the support of each candidate itemset. To reduce the number of comparisons in the scanning process, the candidates are stored in a hash tree structure.


To generate a candidate hash tree, the following items are required:

1. A Hash function
2. A maximum leaf size (a node is split if the number of transactions in that node exceeds this size)


## 1. Getting Started ##
For this assignment, it has been assumed that the hash function splits the nodes into 3 branches each time. Hence, the hash function is of the structure n = hash(H[x]) = H[x] mod 3.

1. Hash(1,4,7) - 1 or left subtree
2. Hash(2,5,8) - 2 or middle subtree
3. Hash(3,6,9) - 0 or right subtree

### 1.1. Prerequisites ###
Except for Python 3, no other libraries have been used for this implementation of the hash tree.


## 2. Implementation ##
I have used recursion to construct the hash tree.

### 2.1. Required User Inputs ###
1. **data** - This variable stores the candidate itemsets as a nested list. Any new itemset (for which a hash tree is to be constructed) should be placed here in the correct format.
2. **max_leaf** - This variable stores the maximum number of items a leaf node can hold before it needs to be split. This number may be altered for changing the structure of the hash tree.

### 2.2. Hash Tree Node Structure ###
A class **hashTreeNode()** defines the structure used for creating the candidate hash tree. It contains *3 lists* for containing each of the left, middle and right subtree values. In addition, it also contains *3 empty nodes* which can be further split into left, middle and right child nodes if the corresponding list size exceeds the **max_leaf** value.

### 2.3. Tree Construction using Recursion ###
Starting from the *Root* and keeping an *index* value of 0, the **create_hash_tree()** function is called and each item in the **data** variable split into the left, middle and right lists of the root node (via the **distribute_items()** function). If the length of any of the lists exceeds the **max_leaf**, the corresponding node is created. Then the node and list are sent back to the **create_hash_tree()** function along with an incremented value of the *index*.

Incrementing the *index* for each split allows the subsequent itemset splitting to occur on the 2nd and 3rd indexes respectively.

### 2.4. Hierarchical Nested List of the Hash Tree ###
The **print_hash_tree()** recursive function allows to hierarchically update the leaf node values into the **nested_hash_tree** nested list.

## 3. Authors ##
**BANERJEE, Rohini** - HKUST Student ID: 20543577

## 4. References
1. “Introduction to Data Mining,” by P.-N. Tan, M. Steinbach, V. Kumar, Addison-Wesley.
