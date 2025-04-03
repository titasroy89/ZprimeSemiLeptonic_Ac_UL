import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

lab_data = pd.read_csv('IVCurve_Module_RH0022.csv', header=None)
lab_bias_voltage = abs(lab_data.iloc[0, :].values)  
lab_current = abs(lab_data.iloc[1, :].values) * 1e6 

wafer_data = pd.read_csv('Wafer_RH22.txt', delim_whitespace=True, header=None, names=['Voltage', 'BiasCurrent'])
wafer_data = wafer_data.dropna()
wafer_data['BiasCurrent'] = abs(wafer_data['BiasCurrent']) * 1e6  

plt.figure(figsize=(10, 6))

plt.plot(lab_bias_voltage, lab_current, label='Lab Data', marker='o')

plt.plot(wafer_data['Voltage'].values, wafer_data['BiasCurrent'].values, label='Wafer Data', marker='x')

plt.xlabel('Bias Voltage (-V)')
plt.ylabel('Current (-uA)')
plt.title('IV Curve Comparison RH0022')
plt.legend()
plt.grid(True)
plt.ylim(0, 5) 
plt.xlim(0, 100) 

plt.savefig('IVCurve_RH22.png')
