import numpy as np
class Performance:

    def adjust(self, volume, movement, A, B, C, D):
        # Your code goes here
        vol_A = np.array(volume)
        mov = np.array(movement)
        change_mov = np.diff(mov, prepend=mov[0])
        C_change_mov = C*change_mov
        T = len(vol_A)
        spd = np.ones(T)
        vol = np.ones(T)
        
        spd = np.where(C_change_mov<0,np.sqrt(-D*vol_A/3*C_change_mov) ,1000)
        
        if A == 0 and B>0:
            vol[1::2] = 1000 #when B<=0 I leave everything constant
        elif A < 0 and B == 0:
            vol = vol_A
        elif A > 0 and B ==0:
            vol = np.where(vol_A <= 500, 1000, 1)
        elif A*B !=0:
            #brute force
            vol[0] = vol_A[0] if A < 0 else (vol_A[0] <= 500)*1000+(vol_A[0] > 500)
            for i,va in enumerate(vol_A[1:]):
                vol[i+1] = np.argmax([A*(va-v)**4+B*(v-vol[i]) for v in range(1,1001)])+1
            
    
        change_vol = np.diff(vol, prepend = vol[0])
        formula = A*(vol_A-vol)**4 + B*change_vol**2+C_change_mov*spd**3+D*vol_A*spd
        score = int(np.sum(formula))
        return score#, vol, vol_A
    
result = Performance()
print(result.adjust([ 3, 1, 3, 20, 34, 10 ], [ 1, 9, 8, 2, 20, 30 ], 1, -1, 0, 0))
