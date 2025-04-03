import glob

datacard_path = "datacard_UL16_500_750.txt"

# Function to edit datacards
def edit_datacard(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    with open(file_path, 'w') as file:
        for line in lines:
            if "autoMCStats" in line:
                file.write("# " + line)
            else:
                file.write(line)

for datacard in glob.glob(datacard_path):
    edit_datacard(datacard)

print("Statistical uncertainties have been disabled in all datacards.")
