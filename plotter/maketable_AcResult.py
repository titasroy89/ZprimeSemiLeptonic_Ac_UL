import json
import os

def extract_ac_values(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    ac_values = {}
    for poi in data['POIs']:
        if poi['name'] == 'Ac':
            ac_values['measured_ac'] = poi['fit'][1] / 100
            ac_values['measured_ac_err_up'] = (poi['fit'][2] - poi['fit'][1]) / 100
            ac_values['measured_ac_err_down'] = (poi['fit'][1] - poi['fit'][0]) / 100
            break
    return ac_values

json_files = {
    "[0,500]": "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/analysis/Ac_unfolding/UL18/all/0_500/output_combine/impacts.json",
    "[500,750]": "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/analysis/Ac_unfolding/UL18/all/500_750/output_combine/impacts.json",
    "[750,1000]": "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/analysis/Ac_unfolding/UL18/all/750_1000/output_combine/impacts.json",
    "[1000,1500]": "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/analysis/Ac_unfolding/UL18/all/1000_1500/output_combine/impacts.json",
    "[1500,Inf]": "/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/analysis/Ac_unfolding/UL18/all/1500Inf/output_combine/impacts.json"
}

sm_ac_values = {
    "[0,500]": {"sm_ac": 0.0056, "sm_ac_err_up": 0.0006, "sm_ac_err_down": 0.0006},
    "[500,750]": {"sm_ac": 0.0072, "sm_ac_err_up": 0.0006, "sm_ac_err_down": 0.0006},
    "[750,1000]": {"sm_ac": 0.0079, "sm_ac_err_up": 0.0004, "sm_ac_err_down": 0.0006},
    "[1000,1500]": {"sm_ac": 0.0096, "sm_ac_err_up": 0.0009, "sm_ac_err_down": 0.0009},
    "[1500,Inf]": {"sm_ac": 0.0094, "sm_ac_err_up": 0.0011, "sm_ac_err_down": 0.0015}
}

table = ''
table += '\\begin{tabular}{|c|c|c|} \n'
table += '\\hline\n'
table += 'Mass Bin $(M_{tt})$ & Measured $A_C$ & SM Predicted $A_C$ \\\\ \n'
table += '\\hline\n'

for mass_bin, json_file in json_files.items():
    ac_values = extract_ac_values(json_file)
    
    measured_ac = ac_values['measured_ac']
    measured_ac_err_up = ac_values['measured_ac_err_up']
    measured_ac_err_down = ac_values['measured_ac_err_down']
    
    sm_ac = sm_ac_values[mass_bin]['sm_ac']
    sm_ac_err_up = sm_ac_values[mass_bin]['sm_ac_err_up']
    sm_ac_err_down = sm_ac_values[mass_bin]['sm_ac_err_down']
    
    table += '%s GeV & $%.4f^{+%.4f}_{-%.4f}$ & $%.2f^{+%.2f}_{-%.2f}$ \\\\ \n' % (
        mass_bin, measured_ac, measured_ac_err_up, measured_ac_err_down,
        sm_ac, sm_ac_err_up, sm_ac_err_down)

table += '\\hline\n'
table += '\\end{tabular}'

print(table)

with open('output_table.tex', 'w') as file:
    file.write(table)
