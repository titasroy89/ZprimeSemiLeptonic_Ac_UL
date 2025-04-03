import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

wafer_data = pd.read_csv('Wafer_RH24.txt', delim_whitespace=True, header=None, names=['Voltage', 'Current'])
wafer_data = wafer_data.dropna()
wafer_data['Current'] = abs(wafer_data['Current']) * 1e6

# Plotting
plt.figure(figsize=(10, 6))

# Plot wafer data
plt.plot(wafer_data['Voltage'].values, wafer_data['Current'].values, label='Wafer Data', marker='x', color='orange')

# Adding labels and title
plt.xlabel('Bias Voltage (-V)')
plt.ylabel('Current (-uA)')
plt.title('IV Curve - Wafer Data Only RH0024')
plt.legend()
plt.grid(True)
plt.ylim(0, 0.1)  
plt.xlim(0, 150)  

plt.savefig('Wafer_IVCurve_RH24.png')
