import os
import json

base_dir = "ele"

# mass_ranges = ["0_500", "500_750", "750_1000", "1000_1500", "1500Inf"]
mass_ranges = ["mass_combined"]
output_dir = "output_combine_old"

for mass_range in mass_ranges:
    json_path = os.path.join(base_dir, mass_range, output_dir, "impacts.json")
    
    if os.path.exists(json_path):
        print("Processing: {}".format(json_path))
        
        with open(json_path, "r") as f:
            data = json.load(f)
        
        for poi in data["POIs"]:
            name = poi["name"]
            fit_values = poi["fit"]
            central_value = fit_values[1]
            lower_error = fit_values[0]
            upper_error = fit_values[2]
            
            print("Mass Range: {mass_range}, POI: {name}, Post-Fit Value: {central_value}, Lower Error: {lower_error}, Upper Error: {upper_error}".format(mass_range=mass_range, name=name, central_value=central_value, lower_error=lower_error, upper_error=upper_error)) 
    else:
        print("JSON file not found in {json_path}".format(json_path=json_path))

print("Extraction complete.")
