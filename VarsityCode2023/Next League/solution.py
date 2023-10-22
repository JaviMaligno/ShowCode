class NextSustainability:

    def percentage_recycled(self, product, material_information):
        # Your code goes here
        simple_material_dict, composite_material_dict = self.database(material_information)
        product = product.lower()
        if product in simple_material_dict.keys():
            total = simple_material_dict[product]
        elif product in composite_material_dict.keys():
            simple_materials = composite_material_dict[product]
            total = sum([percentage * simple_material_dict.get(simple_material,0)/100 for (simple_material,percentage) in simple_materials.items() ])
        else:
            total = 0
            
        return round(total)
        
        
    def is_simple(self, material):
        return False if ":" in material else True
        
    def add_material(self, material, info, material_dict):
        material_dict[material.lower()] = info 
        return material_dict
    
    def process_material(self, material, simple = True):
        if simple:
            mat, raw_info = material.split(" - ")
            info = int(raw_info.split(" ")[0][:-1])
            
        else:
            mat, raw_info = material.split(": ")
            simple_materials_and_percentages = raw_info.split(" ")
            info = {}
            for i in range(0,len(simple_materials_and_percentages),2):
                percentage = int(simple_materials_and_percentages[i][:-1])
                simple_material = simple_materials_and_percentages[i+1]
                info[simple_material.lower()] = percentage
                
        return mat, info
        
    def database(self, material_information):
        simple_material_dict = {}
        composite_material_dict = {}
        for material in material_information:
            if self.is_simple(material):
                mat, info = self.process_material(material, simple = True)
                simple_material_dict = self.add_material(mat, info, simple_material_dict)
            else:
                mat, info = self.process_material(material, simple = False)
                composite_material_dict = self.add_material(mat, info, composite_material_dict)
        return simple_material_dict, composite_material_dict
                
        
    