# Description

You are working in communications, relaying secret messages between two parties. All the messages are listened to and therefore need to be passed in code.

The code consists of upper case and lower case letters (no spaces), and is transmitted as a string. To decode the transmission you must look for letters which occur an ODD number of times. These must then be converted to a numerical value (a = 1, b = 2, c = 3, etc... , z = 26).

Some transmissions contain only one letter repeated (e.g `'dddddddd'`). These are considered noise and should return the integer value 0. The code is not case-sensitive, so upper case and lower case letters can be considered identical.

The decoded message will be an integer value. You can obtain this value by multiplying each letter's numerical value by the number of times it occurs in the transmission, and adding the resulting values together.

Write a program that will take in a string (input) of any length and decrypt the string into the correct integer for message. Your program should return a single integer value.

## Example

* Transmission = `'aaabbabcddcc'`
* a = 1, a occurs 4 times, so it can be ignored.
* b = 2, b occurs 3 times. $2 \times 3 = 6$.
* c = 3, c occurs 3 times, $3 \times 3 = 9$.
* d = 4, d occurs 2 times, so it can be ignored.

Therefore...

* $6 + 9 = 15$.
* Function returns 15
