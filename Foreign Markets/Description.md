# Description

An exchange rate is written as `A15.0000/B`, which means, you can exchange 15 of currency A for 1 of currency B. You can also exchange 1/15 of currency B for 1 of currency A.

Your client wants to exchange one currency for another.

## Rules
Here are some rules:

- You are given a list of current exchange rates in the above format.
- Currency symbols are made up of between one and three uppercase letters of the english alphabet.- z
- You may get exchange rates from one currency to multiple others. You will only ever get one exchange rate between two currencies.
- You may not exchange to the same currency more than once during the calculation.
Exchange rates are always greater than zero.
- Find the best exchange rate for your client. Give the end result rounded to 4 decimal places. If you can't find a way of exchanging one currency for the other, return 0.

## Example:
```
FOO15.0000/BAR
BAR0.1250/BIT
```

If your client wants to exchange from BAR to FOO, you would calculate that the best, and only, exchange rate is 15.0000 FOO for 1 BAR, thus returning 15.0000.

If your client wants to exchange from FOO to BIT, you would calculate that they need to exchange their FOO for BAR, which they can exchange for BIT. They can get 1/15 BAR for 1 FOO, and they can get 1/0.125 BIT for 1 BAR, getting 0.53333333 BIT for 1 FOO, thus returning 0.5333.