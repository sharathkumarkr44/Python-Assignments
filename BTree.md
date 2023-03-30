Solution
---

B-tree is a self-balancing tree data structure that maintains sorted data 
and allows searches, sequential access, insertions, and deletions in logarithmic time. 
The B-tree generalizes the binary search tree, allowing for nodes with more than two children.

A B-tree of order m is a tree that satisfies the following properties:

� at most 2m entries (and thus at most 2m + 1 child)
� at least m entries (and thus, for internals nodes, m + 1 children)
� except for the root node
� A 2-3-4 tree is essentially a special case of a B-Tree (of order 1.5)



1.                                           7|15
                                          /   |    \
					                     /    |     \
                                      3|5  9|11|13  17|19|21|23


2.                                        7|13|19

                                       /   |   \   \
				                      /    |    \   \
                                   3|5   9|11  15|17 21|23

                                      

3. In what scenarios does a B-Tree has an advantage over other balanced trees

--->, Unlike other self-balancing binary search trees, the B-tree is well-suited for storage systems 
that read and write relatively large blocks of data, such as databases and file systems.