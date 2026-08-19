this projects deals with Graphs and the Shortest Path on a weighted graph.


concepts to deep dive
- graph theory
- complex pathfinding algorthms 
- djikstra
- a* algorithm
- regular expressions in python

# Graph Theory
Nodes are the smallest units in a graph. 
Nodes are connected by edges.
Edges can have a cost.





# class structure
initially it needs :
1. Zone class : type, is_start, is_end, is_hub, 

2. Connection Class

3. Graph Class
-- graph will deal with instantiating the zones, connections and linking them all together.
-- Adjacency List will be the way to represent the connections


4. Drone Class




# input parser
- validate file
- read through lines.
- split into lhs and rhs
- validate the keys
- validate rhs values




# restarting project.

## the plan
- input parser
- graph
- route planner
- allocator
- scheduler
- simulation
- renderer

## the classes for zones

Domain Model architectural pattern ==> models

ZoneType is an enum for setting values Directly about normal restricted priority unblocked. This is going to be in the input file and it will be in square brackets. So it's not a compulsory property, but it's an optional one.

For the zone class, we could use the regular way of initializing the class using underscore underscore init underscore underscore as a function dedicated function to initialize how we want to configure and have all these, but it kind of makes it very rigid and we'll have to do the validation of the variables inside this particular class. So it kind of breaks the principle. So we are leaving the validation aspect to the parser file and keeping class as a pure data class. So it just stores the data and it has no functions within 




## mastering regular expressions

consider input line 
hub: waypoint1 1 0 [color=blue]

every line has the following format:
- starts with hub / starthub / endhub
- 1 colon
- 1/more space
- 1/more characters (alphabets, nums, underscore)
- 1/more space
- possible negative sign
- 1/more digits
- 1/more space
- possible negative sign
- 1/more digits
- 0/more space
- properties if available
	- starts with [
	- any characters (alphabets, nums, underscore)
	- ends with ]

we convert these rules to regex.
^(start_hub|end_hub|hub):\s+(\w+)\s+(-?\d+)\s+(-?\d+)\s*(?:\[(.*)\])?$

^
(start_hub|end_hub|hub)
:
\s+
(\w+)
\s+
(-?\d+)
\s+
(-?\d+)
\s*

(?:\[(.*)\])?$