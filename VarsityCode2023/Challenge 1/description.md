# Challenge description 


Our newest client, a medium-sized solar generation plant has a serious problem. They have committed to generating some minimum quantity of electricity at all times, however, on certain cloudy days, they are unable to reach these. And when they can't reach them, they get fined, big time. There is a solution, which is buying some energy on the market for the times when they can't generate enough.

There is a problem, however. Although they have forecasted the deficit they will encounter, there are so many futures contracts for so many different periods, they need to find an optimal method for buying these. This is where you come in.

(A futures contract is an agreement to purchase something, in this case, electricity, at a given price, at a given time in the future.)

We need you to develop an algorithm that looks at all the possible futures contracts and purchases them ahead of time, in a way that covers as much of the production deficit as possible. Every contract has a transaction fee, so the fewer contracts used the better. And every unit of deficit per period carries a large fine (10 times the transaction fee), so we must try to avoid those.

You are given the forecasted deficits as an array of non-negative integers. There's a limit on how far into the future the weather can be forecasted with confidence, which is about 20 time periods. You are also given a list of futures contracts available to buy. Each contract is a string, with the same number of characters as there are numbers in the forecast. In the contract string `X` marks periods which the contract covers, and `.` which it isn't. You can use the same contract any number of times. You are not allowed to buy more for any period then needed.

You can assume that both the forecast and the contracts are in the correct format.

You need to calculate the lowest possible cost to the client. The cost is calculated as `# contracts used + total deficit not covered * 10`

Here are a couple of examples:

Given this simple forecast `[2, 1]`, which shows that there will be a 2 unit deficit in the first period and a 1 unit deficit in the second, and these futures contracts:

```
"X.",
".X",
"XX"
```

It is possible to fully cover the deficit with just two contracts: `"X."` and `"XX"`. With two contracts used, the result returned is `2`. Note, how this is a more optimal solution, than using two `"X."` contracts and one `".X"` contract.

Here is a more complex example. Given this forecast: `[1, 3, 2]` and these futures contracts:

```
"XX.",
".XX",
"X..",
".X.",
"..X"
```

It is again possible to fully cover the deficit, by using one of these contracts: `"XX."` and two of these contracts: `".XX"`. With 3 contracts used, the result returned is `3`

Finally, a fairly tricky case. You have a longer forecast `[2, 3, 1, 1, 0, 0, 3, 2]` and several contracts:

```
"XXXX....",
"XX......",
"..XX....",
"......XX",
".X......",
"X......."
```

It may help to visualise the deficit:

```
0000  00
00    00
 0    0
```

This way, we can see, that not all periods can be fully covered. Numbering the coverage, by which contracts were used, shows the period that cannot be fully covered.

```
1111  44
22    44
 5    X
```

A total of five contracts were used, (two 4s and one of 1, 2, and 5) and one unit was left uncovered, for a penalty of `1 * 10`, which gives a final result of `15`.
