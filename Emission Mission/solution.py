import numpy as np 
from math import floor, ceil
class BAE_Emissions:

    def forecast(self, projects, renewable_forecast):
        # Your code goes here
        # Assume energy cannot be stored if there's an excess
        ranges_energy = self.parsed_projects(projects)
        forecast_array = np.array(renewable_forecast)
        consumption_array = np.zeros(24)
        return self.array_forecast(ranges_energy, consumption_array, forecast_array)
    
    @staticmethod
    def array_forecast(ranges_energy, consumption_array, forecast_array):
        for (start, end), energy in ranges_energy:
            consumption_array[start:end] += np.array([energy]* (end-start))
        
        energy_required = consumption_array - forecast_array
        grid_energy = np.sum(energy_required, where = energy_required > 0)
        return grid_energy
        
    def parsed_projects(self, projects):
        ranges_energy = []
        for project in projects:
            ranges_energy.extend(self.parse_project(project))
        return ranges_energy
    
    @staticmethod
    def parse_project(project):
        project_ranges = []
        time_ranges, energy = tuple(project.split(";"))
        energy = float(energy)
        time_ranges = time_ranges.split(",")
        for time_range in time_ranges:
            if "-" in time_range:
                start, end = tuple(map(float,time_range.split("-")))
            else:
                start = float(time_range)
                end = min(start+1,24)
            start1 = floor(start)
            start_diff = start - start1
            start2 = ceil(start)
            end1 = floor(end)
            end2 = min(ceil(end), 24)
            end_diff = end-end1
            project_ranges.extend([((start2,end1),energy), ((start1,start2), energy*start_diff), ((end1,end2), energy*end_diff)])
        return project_ranges
                
result = BAE_Emissions()
print(result.forecast([  ], [ 0, 0, 0, 0, 1, 0, 1, 2, 1, 2, 0, 1, 1, 3, 2, 2, 3, 2, 1, 1, 0, 1, 2, 4 ]))