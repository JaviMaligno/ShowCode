# Challenge Description

Santa Claus' accounting department has purchased a brand new system from Yeti Inc. It should track the niceness score for all children in the world. We need to back-populate it with data from the old system. One problem is that they are incompatible, so some translation needs to happen. Yeti Inc has refused to do the back population, so it's our job to do it.

The old system is transaction based. It contains a list of modifications with a date, which records any time a child does something nice or naughty. The new system is value based, it contains the value itself, with a date

Here is an example from the old system:

`20150602 #4516 + 20.02\n20150603 #4516 * 2\n20150605 #4516 / 2\n20150604 #4516 - 2`
    

One line per transaction, separated with newline (`\n`). Because it is exported by the old system, we can rely on it always being in the correct format. The date is year, month and day, always padded with zeros where relevant, after the year 2000 (Santa had a new system installed after Y2K almost ruined Christmas).

In the example Child #4516 starts with a score of 0, then got added 20.02 on 20150602 (2nd of June 2015), then their niceness was doubled. Then the child got naughty, and lost 2 points, and then got halved.

A child's score can never be negative. It's against the laws of the universe. So if a score would go negative, there must have been an error in the accounting.

Note: transactions are not necessary always in order, as they might be recorded late, because the accountat elves that look after the children don't always file the info on time. However, in a given day, the order is always correct.

All valid operations are:

```
<date> <#account> = <value>    Set the niceness to that value
<date> <#account> + <value>    Add the value to the niceness
<date> <#account> - <value>    Subtract the value from the niceness
<date> <#account> ++           Increment the niceness by 1
<date> <#account> --           Decrement the niceness by 1
<date> <#account> * <value>    Multiply niceness by the value
<date> <#account> / <value>    Divide niceness by the value
``` 

`<value>` is always a non-negative number.


In the new system, the records show:

`20150602 @4516 20.02\n20150603 @4516 40.04\n20150604 @4516 38.04\n20150605 @4516 19.02`
    

The format is simpler:

`<date> <@account> <end of day value>`

One line per niceness score, separated with newline (`\n`). Only one record is generated per day per child, so it would be the latest value for any day where a child's score updated. It must be ordered by date and then account number.

Note: The new system cannot hold more than 2 decimal digits, numbers outputted must be rounded to the nearest number that the system can hold. For consistency numbers should always be displayed with two decimal places.

Note: in case of any errors in the calculation, to notify the system that an issue needs to be fixed, set the value to `?`. Errors are cleared by setting a new value. Only one error needs to be displayed for the day when it occured, even if later transactions are applied to it before it is fixed.

`20150605 @4516 ?`