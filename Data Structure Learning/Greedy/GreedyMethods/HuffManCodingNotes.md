HUFFMAN CODING

Message is need to send 

Message -> BCCABBDDAECCBBAEDDCC

len = 20 
Send by using ASCII code. 8 bits 

A -> 65 decimal -> 01000001
B -> 66 ->
c => 67
''''
''''

8 * 20 = 160 bits 

Character | Count/ Frequency | Code
A               3 -> 3/20       000
B               5 -> 5/20       001 
C               6 -> 6/20       010
D               4 -> 4/20       011
E               2 -> 2/20       100
------------------------------------
Total           20

use your own code instead of ascii code

3*20

Now how will reciever will know this isthe codes? 
hashtable to decode this message memory for this will be 
asscii code for char (5*8 ) and codes 5*3
Total message -> message + chart => 60 + 55 bits -> 115 bits 
300 to 35% memory sage is reduced. 

Arrange the all occurance to the smallest first as per greedy to get optimal solution. 



       9
     /   \
    5     \
   /\      \
  2  3      4       5       6
  E  A      D       B       c

