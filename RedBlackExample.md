A red-black tree is a kind of self-balancing binary search tree where each node has an extra bit, and that bit is often interpreted as the color (red or black). These colors are used to ensure that the tree remains balanced during insertions and deletions. 
Although the balance of the tree is not perfect, it is good enough to reduce the searching time and maintain it around O(log n) time, where n is the total number of elements in the tree.

Rules That Every Red-Black Tree Follows: 
Every node has a color either red or black.
The root of the tree is always black.
There are no two adjacent red nodes (A red node cannot have a red parent or red child).
Every path from a node (including root) to any of its descendants NULL nodes has the same number of black nodes.
All leaf nodes are black nodes.

2. The first number, 6, is inserted at the root of the tree.
 6 (root) - black

6 (black)
\              
 7 (red)



6 (black)
/ \
3 7 (red)


6 (black)
/ \
3 7 (red)
 \
  4(red)
   

6 (black)
/ \
3 7 (red)
/ \
2  4(red)

at last 1 can be inserted as ------>                
 6
/ \
3 7 (red)
/ \
2  4(red)
/
1


After inserting all of the numbers, the tree is not balanced according to the red-black tree
properties, so it must be rebalanced. This is done by performing a series of rotations on the tree to
move nodes around and change their colours.


                  6 (black)
                 /  \
                3    7(black)
               / \    \
              1  2      4(red)
   
   