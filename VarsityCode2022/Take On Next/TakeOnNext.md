# Challenge Description

Next now supplies software to many third-party clients such as GAP, Victoria Secret & Reiss.

Our various third-party clients have different delivery lead times and rules.

Our clients can have the following differences:
- Lead Times (the number of days it takes to process and deliver an order).
- Dispatch Cutoff (if ordered on or after a specific time, this will add a day to the lead time).
- Working Day Delivery Only (if working day delivery only, if the delivery date falls on a weekend day, the delivery date will move to the next available weekday).

Next nor any of its clients deliver on the Christmas Bank Holidays, any deliveries scheduled for these days will move to the next available day.
The Christmas Bank Holidays are:
```
25/12/YYYY
26/12/YYYY
01/01/YYYY
``` 

If a Bank Holiday falls on a weekend, it will move to the next available working day which is not also a Bank Holiday.

The following inputs will be provided as strings, but are limited to the format/values noted below:
- Order Date (`DD/MM/YYYY HH:MM:SS`).
- Lead Time (Must be an unsigned integer).
- Dispatch Cut Off (`HH:MM:SS`).
- Working Day Delivery Only (`True` or `False`).

The expected results are either a date (`DD/MM/YYYY`) as a string or `"Invalid Data"` if any of the data is invalid.