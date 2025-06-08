# Heap Data Structure

A **heap** is a special type of data structure based on the tree data structure. Most heaps are implemented as **binary trees**.

## Types of Heaps

- **Min Heap**:  
    - The value of each node is **greater than or equal to** its parent node.  
    - The **root node** contains the **smallest** value.

- **Max Heap**:  
    - The value of each node is **smaller than or equal to** its parent node.  
    - The **root node** contains the **largest** value.

## Main Characteristics of a Heap

1. **Complete Binary Tree**:  
     Every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

2. **Heap Order Property**:  
     - **Min Heap**: Parent node is less than or equal to its children.  
     - **Max Heap**: Parent node is greater than or equal to its children.

3. **Efficient Operations**:
     - **Insertion**: `O(log n)`
     - **Deletion**: `O(log n)`
     - **Peek (Get Min/Max)**: `O(1)`

Main understanding of heap is to understand the fact heap node root and child relationship. 
If parent node is at ith location the 
left child will be in 2i+1
right child will be in 2i+2
to find parent we can do (i-1)/2


> **Note:**  
> Heaps are commonly used to implement **priority queues** and for efficient sorting algorithms like **Heap Sort**.

