# Challenge description

Nationwide has a database of transactions and wants to perform an analysis. Your job is process and analyse the data.

Transactions will be in the following format:

```
[identifier] paid £[amount] to [identifier]
```

or

```
[identifier] received £[amount] from [identifier]
```

where [identifier] indicates a unique alphanumeric label for an account and [amount] is a non-negative floating-point number which has at most two decimal places.

Your task is to return the list of identifiers, sorted by the number of accounts they paid money to, in descending order, ignoring those that did not pay any other accounts. This should only be considered after all transactions have been settled i.e. only **net** payments should be considered. Note that there will be only ever be one unique solution, further sorting is not necessary.
