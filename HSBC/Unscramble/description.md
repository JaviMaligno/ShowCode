# Description

In this challenge, you are trying to decrypt an encrypted message. You will be passed two inputs, a string (the encrypted message) and an integer number (the key to help decrypt the string). For example, the two inputs might be `{'ABC', 1}`.

The characters in the string have been shifted along in the alphabet the same number of times as the key number specifies.


## Examples

- For example, if the original word was `'DOG'` and we incremented each letter by 1, you would get `D -> E, O -> P, G -> H`. We want to find the original word from the encrypted string. So for puzzle input `{'EPH', 1}`we shift each letter back by 1 to get the original string `'DOG'`
- As another example, `{'KIB', 8}` would decrypt to give the string `'CAT'`.
- A letter may roll-over to the start of the alphabet again if the key it was encrypted with is large enough. As another example, `{'A', 3}` would unscramble to give the string `'X'` because `X` when incremented 3 times would roll-over back to the beginning of the alphabet.

## Format

Input strings will only ever contain UPPER CASE letters. You should always return only a string containing upper case characters.

Your challenge is to decrypt the `inputString` using the `inputNumber,` and return the original word as a string.
