# Challenge description

## Q1


Write a method to return the reverse order for a list of space separated words.

### Example:

"A sample sentence is required" would return "required is sentence sample A".

## Q2


Write a function that takes an array of integers and returns the balance point. If no balance point is found, return -1.
The balance point of an array is the index in the array where the sum of the previous elements is equal to the sum of the following elements. Where no previous or following elements exist for a specific index, then you can assume a sum of 0 for the missing elements.

### Example:

`A = [2, 7, 4, 5, -3, 8, 9, -1]`

The balance point of A is 3. 

`A[0] + A[1] + A[2] = 2 + 7 + 4 = 13.`

`A[4] + A[5] + A[6] + A[7] = -3 + 8 + 9 + -1 = 13.`
