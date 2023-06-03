# Challenge description

You've written your song and you now need somewhere to perform. Luckily, a local venue has offered its hall to you. Less luckily, this venue will not manage any of the usual problems such as ticketing and seating audience members. So, you'll just have to do it yourself.

Given a list of strings, where each string represents a row of seats, you need to find the largest continguous block of seats booked by the same group, returning the character corresponding to that group. Seats are represented by a character indicating which group booked that seat. The two exceptions are that X indicates seats that are unavailable for booking and O represents unbooked seats and should only be returned if there are no available seats and no booked seats respectively. Seats are contiguous to the seats next to them in a row and the corresponding seats in the row before and row after (i.e. directly infront and behind).

If two groups have the same largest block size, return the group whose largest block appears earliest in the seating (i.e. first if ordered by row, and then by column).

Note that each string (i.e. row of seats) will have the same length and there will be at least one seat.
