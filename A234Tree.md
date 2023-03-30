A 2-3-4 tree is a self-balancing tree. The number represents the number of children each node can have. Any internal node can have either two, three, or four child nodes. 
It is also called a 2-4 tree.

2.1) 3,7,5,15,17,9,13,21,11,19

3,7,5 ----> 3|5|7 ---15---> 5     ----17----->     5      -------9--------->     5|15     --------13--------->   5 | 13 | 15
                           /  \                   /  \                         /  |   \                         /  |        \    and so on ....
                         3      7|15             3     7|15|17                3   7|9   17                     3  7|9        17

finally, 

               5 | 13 | 15
              /  |        \
             3   7|9|11    17|19|21


2.2)  3,5,7,9,11,13,15,17,19,21


final tree will be ----->          9
                                 /    \
                                5      13|17
                               / \    /  |  \
                              3   7  11  15  19|21

2.3) There is the difference in depth of the tree. 

3. There are two main strategies for building 2-3-4 trees: bottom-up and top-down. The main
difference between the two approaches is the order in which nodes are inserted into the tree.
In the bottom-up approach, nodes are inserted into the tree starting at the bottom and working
upwards. This means that leaf nodes are inserted first, followed by their parent nodes, and so on
until the root node is reached. The advantage of this approach is that it can be easier to implement
and can lead to more balanced trees.
In the top-down approach, nodes are inserted into the tree starting at the root and working
downwards. This means that the root node is inserted first, followed by its children, and so on until
the leaf nodes are reached. The advantage of this approach is that it can be more efficient in some
cases, since it allows for nodes with more than two children.
                                  
                 