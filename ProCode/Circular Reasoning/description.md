# Challenge Description

You have been hired to manage ShowCode's internal network. Due to several interesting design decisions, it was decided that all the nodes would be connected in a huge ring network. In essence, this means that node 1 is connected to node 2, which is connected to node 3 and so on, with the last node being connected back to node 1. Data can only travel in one direction, which is in the direction from node 1 to node 2.

Given an integer representing the total number of nodes, an integer for your starting node, and a list of nodes to visit in that order, calculate the total number of nodes visited.