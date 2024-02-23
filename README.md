# Max Cut

Solution for the Max Cut Problem

## Problem description

Find a maximum cut for a given undirected graph G(V, E), with n vertices and m edges. A
maximum cut of G is a partition of the graph's vertices into two complementary sets S and T, such
that the number of edges between the set S and the set T is as large as possible.

## 1st delivery

Design and test an exhaustive search algorithm to solve the max cut problem, as well as another method using a greedy heuristics. Afterwards, analyze the computational complexity of the developed algorithms. To accomplish that:

1. Perform a formal computational complexity analysis of the algorithms.
2. Carry out a sequence of experiments, for successively larger problem instances, to register and analyze:
   - The number of basic operations carried out.
   - The execution time.
   - The number of solutions/configurations tested.
3. Compare the results of the experimental and the formal analysis.
4. Determine the largest graph that you can process on your computer, without taking too much time.
5. Estimate the execution time required by much larger problem instances.

## 2nd delivery

Design and test a randomized algorithm to solve the max cut problem. Devise and/or adapt strategies for:

- Iterating through the randomly generated candidate solutions and keeping the best feasible solution computed.

- Ensuring that no such solutions are tested more than once.

- Deciding when to stop testing candidate solutions of a certain size and start testing larger or smaller solutions.

- Deciding when to stop testing altogether: e.g., after a given number of candidate solutions, or after spending a certain amount of computation time, etc.

Afterwards, analyze the performance of the developed strategy. To accomplish that:

1. Perform a formal computational complexity analysis of the randomized algorithm.

2. Devise and carry out a sequence of experiments, for successively larger problem instances, to register and analyze:

   - The number of basic operations carried out.
   - The execution time.
   - The number of solutions/configurations tested.

3. Analyze the accuracy of the obtained solutions by comparing them with the solutions obtained with the algorithms of the first project.

4. Compare the results of the experimental and the formal analysis.

5. Determine the largest graph that you can process on your computer, without taking too much time.

6. Estimate the execution time that would be required by much larger problem instances.
