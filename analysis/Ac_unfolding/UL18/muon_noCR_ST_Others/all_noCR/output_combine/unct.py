import json

with open('impacts.json', 'r') as f:
    data = json.load(f)

for poi in data["POIs"]:
    if poi["name"] == "Ac":
        lower_bound, central_value, upper_bound = poi["fit"]
        lower_uncertainty = central_value - lower_bound
        upper_uncertainty = upper_bound - central_value

        # Print uncertainties with full precision
        print("Central Value: {}".format(central_value))
        print("Lower Uncertainty: {lower_uncertainty}".format(lower_uncertainty=lower_uncertainty))
        print("Upper Uncertainty: {upper_uncertainty}".format(upper_uncertainty=upper_uncertainty))