class Solution:

    def simp(self, program):
        # Your code goes here
        PC = 0
        ACC = 0
        BAK = 0

        while True:
            instruction = program[PC]
            instruction_type = instruction // 100
            value = instruction % 100

            if instruction_type == 0:  # NOP
                pass
            elif instruction_type == 1:  # MOV
                ACC = value
            elif instruction_type == 2:  # SWP
                ACC, BAK = BAK, ACC
            elif instruction_type == 3:  # SAV
                BAK = ACC
            elif instruction_type == 4:  # ADD
                ACC += value
            elif instruction_type == 5:  # SUB
                ACC -= value
            elif instruction_type == 6:  # NEG
                ACC = -ACC
            elif instruction_type == 7:  # JMP
                PC = value
                continue
            elif instruction_type == 8:  # JGT
                if ACC > 0:
                    PC = value
                    continue
            elif instruction_type == 9:  # OUT
                return ACC

            PC += 1
