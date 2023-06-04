# Challenge descriptio


This is it. The big show. The crowd is ready to go and so are you!

Like any good live performer you know how to react to the crowd. But it's easy to get nervous and you never know when you might freeze up. The show must go on, however, and so you have designed a program that reacts to the volume level of the crowd and will automatically adjust your performance in real time until you can get your nerves under control.

Your hardware detects the audience's movement and volume and returns them as as two lists of decimals of length T between 1 and 1000 inclusive. Your program should then calculate the speed and volume of your music (integers from 1-1000 inclusive) in order to maximise the score (see below) FOR EACH of the data pairs and return the total score across the performance rounded down as an integer. You are NOT maximising the TOTAL score.

#### Scoring

The score for any speed, volume pair is the sum of the following:

```
#vol_A, vol, mov, spd for audience volume, volume, movement and speed respectively
#change(X) denotes the difference in a quantity X from the last value, however treat as 0 for the first values
 A*(vol_A-vol)^4)
 B*change(vol)^2
 C*spd^3*change(mov)
D*vol_A*spd
```

where A, B, C, D are decimal parameters. At least one set of data will be given.
