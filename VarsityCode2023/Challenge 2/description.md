# Challenge description

The SIMP1337 is a 1970s CPU commonly used in embedded devices. Each instruction is composed of three decimal digits. The first describes the instruction type. The remaining two describe the immediate value. There are three registers: PC (storing the address of the current instruction), ACC (general register and result of arithmetic operations), BAK (a secondary register for extra storage). The following table shows the instruction encodings.

```
0XX      NOP         (Do nothing)
1XX      MOV  XX     (Move XX to ACC)
2XX      SWP         (Swap the values in ACC and BAK)
3XX      SAV         (Move ACC to BAK)
4XX      ADD  XX     (Add XX to ACC)
5XX      SUB  XX     (Subtract XX from ACC)
6XX      NEG         (Negate ACC)
7XX      JMP  XX     (Make XX the next instruction to execute)
8XX      JGT  XX     (If ACC is greater than 0 then JMP XX)
9XX      OUT         (Output the value of ACC and end execution)
```

Accept the program as an array of integers, execute it (starting with PC at index 0), and return the value triggered by the OUT instruction.
