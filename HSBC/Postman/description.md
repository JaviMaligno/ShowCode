# Description

You are a postman trying to deliver a letter to a house. Outside the house is a sign saying 'Beware of the dog(s)!'. Several large, angry dogs are chained to posts on the lawn before you.

The dogs cannot move beyond the square where they are tied up. You need to get to across the lawn to the house to deliver your letter, but due to a recent knee operation you can only walk in a straight forward line. You cannot turn or go diagonally.

The position of the dogs can be represented as a string like so:

| H | H | H | H | H | H |
| - | - | - | - | - | - |
| . | . | . | . | D | . |
| . | D | . | . | . | . |
| . | . | . | D | . | . |
| D | . | . | . | . | . |
| . | . | . | . | . | D |

In the above example, there is one straight path to the house (H). It is on index 2 (starting from zero) from the left hand side of the lawn. 'D' represents the position of a Dog and '.' represents an empty space on the lawn.

| H | H | H | H | H | H |
| - | - | - | - | - | - |
| . | . | x | . | D | . |
| . | D | x | . | . | . |
| . | . | x | D | . | . |
| D | . | x | . | . | . |
| . | . | x | . | . | D |
| 0 | 1 | 2 | 3 | 4 | 5 |

Your task is to write a program to find index(es) on the x-axis of the lawn that are safe to travel down to the house.

For example, for the input ` 'HHHHHH\n....D.\n.D....\n...D..\nD.....\n.....D'` shown above, the output would be `[2]`.

* There can be one or more safe routes, or even none.
* Your puzzle input will always be a string with each 'row' of the lawn separated by a newline (`\n`).
* Dogs will be represented by the character 'D', and empty squares by the character `.` .
* Each row of the lawn will always be the same length, but the length of the lawn on both the x and y axes may differ between inputs.
* The output should be a list of integers. If there is no safe path, the method should return a list containing the integer -1, i.e. `[-1]`.
