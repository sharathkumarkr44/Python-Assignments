What is a tree? Use the words: node, parent, child
--> A tree is an abstract data type that stores elements 
hierarchically. Each node of the tree may contain one or more data items.
If a node N is connected to other nodes directly below it 
in the tree, N is referred to as its parent and they are 
referred to as its children.
Each node is the child of at most one parent.

What is a leaf node?
--> A leaf node is a node without children.

What is a root node?
--> The topmost node of a tree or the node which does not have any parent node is called the root node.

What is the height of a tree?
--> The height of a tree is equal to the number of levels forming the whole tree.

What is a path in a tree?
--> A path is a sequence of nodes connecting each node to the root of the tree.

What are common applications of trees?
--> 1. Store hierarchical data, like folder structure, organization structure, XML/HTML data.
    2. Heap is a tree data structure which is implemented using arrays and used to implement priority queues.
    3. Implementation of ML algorithm Decision trees.
    4. For indexing in database.

What is a binary tree?
--> A binary tree is an ordered tree with the following 
properties:-
* every node has at most two children
* each child is labeled as either left child or right child
* left children precede right children

What is a search tree?
--> a search tree is a tree data structure used for locating specific keys from within a set. 
In order for a tree to function as a search tree, the key for each node must be greater than any keys in subtrees 
on the left, and less than any keys in subtrees on the right

What is a balanced search tree?
--> A balanced tree is a search tree that doesn’t just maintain the order between nodes 
but also controls its height, making sure it stays same after insertion or deletion. 
To do that, a balanced tree must re-balance itself after we add or delete a node.

10. 
Preorder 10 5 2 9 6 15 13 12 14
Inorder 2 5 6 9 10 12 13 14 15
Postorder 2 6 9 5 12 14 13 15 10
Leveloder 10 5 15 2 9 13 6 12 14