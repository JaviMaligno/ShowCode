# Description

You are cycling through some mountains. Your Cycling Computer records your current height above sea level (in meters) every 10m. This is stored as a list of integers, your puzzle input.

* The integers must be positive. If an integer in the list is negative there has been an error and that number is skipped until the next valid positive number.
* The integer cannot be more than 5m in difference from the previous value. If this occurs, the value is skipped until a valid value is found relative to the last valid value in the list.
* The decrease should be returned as a negative number.
* You can assume that the first value in the list is always non-negative.

## Example:

Your puzzle input (values) might look like this: `[1, 2, 4, 4, 2, 4]`. The output in this case would be `[5, -2]`.

However, if we changed the input to `[1, 2, 10, -2, 2, 4]`, the output would be `[3, 0]`, because we skip the large increase and negative values.

Write a program to calculate the total increase and decrease in altitude. Return the increase/decrease as a list of two integers, e.g. `[2, -3]`.
