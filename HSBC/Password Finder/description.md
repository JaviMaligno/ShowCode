# Description

You need to break into a locker.

To open the locker you need to give a password made up of characters.

These passwords are hidden in a string.

The first character can be found at index 3, the second at index 4, the third at index 6, the fourth at index 10 ...

With the difference between the indexes doubling each time until you reach the end of the string.

## Example

For `'abcdefgh'` the first character at index 3 would be `'d'`, then `'e'` at index 4, then `'g'` at index 6. There is no index 10 so the password would be `'deg'`.

Find the passwords that are hidden in the strings. You will always be given a string as the input, and should return a string as the output.
