1. What is a graph?
---> A Graph is a non-linear data structure consisting of vertices and edges. 
The vertices are sometimes also referred to as nodes and the edges are lines or arcs that connect any two nodes in the graph. 
More formally a Graph is composed of a set of vertices( V ) and a set of edges( E ). The graph is denoted by G(E, V).
 The difference between a graph to a tree is that in a graph there are no specific rules for the connection of nodes


2. What is a directed and undirected graph? What is this graph?
----> When a graph has an ordered pair of vertexes, it is called a directed graph. The edges of the graph represent a specific direction from one vertex to another
      When a graph has an unordered pair of vertexes, it is an undirected graph. In other words, there is no specific direction to represent the edges.
	The given graph is a directed graph.


3. How many vertices does this graph have?
-----> 9


4. How many edges does this graph have?
------> 16


5. List all sources! A source is a vertex that has only outgoing edges.
-------> 0


6. List all sinks! A sink is a vertex that has only ingoing edges.
-------> 7


7. A cycle in a directed graph is a path through this graph, where the start node and the end node are the same. The count of visited nodes is the length of this cycle. 
How many cycles of lengths 1,2,3 and 4 are in this graph? Provide them.
--------> 4 - (1,2,3,4,1), 
          1 and 2 - (6,6), (8,8) 
	    3 - (1,5,4,1), (5,4,1,5) , (4,1,5,4)



8. What is the corresponding edge list for this graph?
-------> E = {{1,2},{2,3},{3,4},{4,1},{1,5},{5,4},{6,6},{8,8},{0,5},{0,6},{0,7},{0,8},{6,5},{6,7},{8,5},{8,7}}


9. What is the corresponding node list for this graph?
---------> V = {0, 1, 2, 3, 4, 5, 6, 7, 8}
edge_list = {9, 16, 0, 5, 0, 6, 0, 7, 0, 8, 1, 2, 1, 5, 2, 3, 3, 4, 4, 1, 5, 4, 6, 5, 6, 6, 6, 7, 8, 5, 8, 7, 8, 8}


10. What is the corresponding adjacency matrix for this graph?
---------->  0 1 2 3 4 5 6 7 8
             -----------------
          0| 0 0 0 0 0 1 1 1 1
          1| 0 0 1 0 1 1 0 0 0
          2| 0 1 0 1 0 0 0 0 0
          3| 0 0 1 0 1 0 0 0 0
          4| 0 1 0 1 0 1 0 0 0
          5| 1 1 0 0 1 0 1 0 1
          6| 1 0 0 0 0 1 1 1 0
          7| 1 0 0 0 0 0 1 0 1
          8| 1 0 0 0 0 1 0 1 1 
             
path - a,b,d,e
walk - a,b,d,e,b,d,f ( edges can be visited multiple times unlike path)