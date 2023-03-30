1. AVL tree is a height-balanced binary search tree. That means, an AVL tree is also a binary search tree but it is a balanced tree. 
A binary tree is said to be balanced if, the difference between the heights of left and right subtrees of every node in the tree is either -1, 0 or +1.

why balancing is needed?
it can be seen that any value in a balanced binary tree can be searched in O(logN) time where N is the number of nodes in the tree. 
But if the tree is not height-balanced then in the worst case, a search operation can take O(N) time.

For ex:- Suppose we want to want to find the value 79 in the above tree. First, we compare the value of the root node. Since the value of 79 is greater than 35, we move to its right child, i.e., 48. 
Since the value 79 is greater than 48, so we move to the right child of 48. The value of the right child of node 48 is 79. The number of hops required to search the element 79 is 2. 

2 & 3. sequence 14,17,19,7,5,10,18

   14
   / \
  ?   17
      / \
     ?   ?


    14                                                      17
   / \                                                     /  \
  ?   17   ----> imbalance of 2.      ----->>             14   19
      / \                                                 / \  / \
     ?   19                                              ?   ? ?  ?
         / \
        ?   ?


    17
    / \
   14  19
   / \  /\
  7  ?  ? ?
  /\
  ? ?


     17                                                         17
    / \                                                         / \
   14  19                                                      7   19
   / \  /\                                                     /\   /\
  7  ? -------> imbalance of 2        --------->>             5  14 ? ?             
  /\                                                          /\  /\ 
  5 ?                                                        ?  ? ? ?
 /\
 ? ?


    17                                                                14
    / \                                                              /  \
   7   19    ------------> imbalance of 2        --------->>        7    17
  / \   / \                                                         /\   / \
 5   14 ?  ?                                                       5  10 ?  19 
 / \ / \                                                           /\  /\    /\
?  ? 10 ?                                                         ?  ? ? ?   ? ?
     /\
    ?  ?


                 FINAL AVL TREE
               ------------------
                       14
                      /  \
                     7    17
                    / \   / \
                   5  10  ?  19
                  / \ / \    / \
                            18
                            / \



