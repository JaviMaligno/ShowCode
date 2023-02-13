from math import exp, isclose

class Detector:

    def count_decays(self, energy_readings):
        # Your code goes here
        ndecays = 0
        
        time = len(energy_readings)
        if time == 1:
            return ndecays
       
        initial_time=0
        initial_energy = energy_readings[initial_time]
        next_energy = energy_readings[initial_time+1]
        while initial_energy == next_energy and initial_time < time-2:
            initial_time += 1
            initial_energy = energy_readings[initial_time]
            next_energy = energy_readings[initial_time+1]
            
 
        constant_list = [initial_energy]
        shift_list = [0]
        
        time_axis = range(initial_time, time-1)
        for t in time_axis:
            next_energy = energy_readings[t+1]
            predicted_energy = self.energy_formula(t+1, constant_list, shift_list)
            if isclose(next_energy, predicted_energy, abs_tol = 1e-6):
                continue
            else:
                ndecays += 1
                energy_peak = next_energy - predicted_energy
                shift_list.append(t)
                constant_list.append( energy_peak / exp(-0.4))
        return ndecays
        
    def energy_formula(self, t, constants, shifts):
        independent = constants[0]
        result = independent + sum(constants[i]*(t-shifts[i])*exp(-0.4*(t-shifts[i])) for i in range(1,len(constants)))
        return result
            
#result = Detector()
#print(result.count_decays([ 3, 3, 3, 57.906675, 76.61009, 77.013478, 69.150291, 58.427332, 47.584862, 65.66898, 66.983277, 60.619558, 51.49755, 42.127624, 33.664707, 26.529161, 20.765596, 16.244936, 12.774096, 10.152211 ]))