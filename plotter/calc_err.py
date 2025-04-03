import json

import os
import math
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--channel", dest="channel",default="muon",type='str',
                  help="what channel?")
parser.add_option("-m", "--mass", dest="mass", default="0_500",type='str',
                  help="don't print status messages to stdout")
(options, args) = parser.parse_args()
channel = options.channel
mass=options.mass                 

file_path="/nfs/dust/cms/user/beozek/uuh2-106X_v2/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/analysis/newmatching/all_years/masses/%s/output_combine/impacts.json"%(mass)
# file_stat="/nfs/dust/cms/user/titasroy/Ac_UL/CMSSW_10_6_28/src/UHH2/ZprimeSemiLeptonic/combine/output_combine/impacts.json"
with open(file_path) as json_data:
    d = json.load(json_data)
    print(d["params"][0]["Ac"])
    total_up=d["params"][0]["Ac"][2]-d["params"][0]["Ac"][1]
    total_down=d["params"][0]["Ac"][1]-d["params"][0]["Ac"][0]

    print("total error = +",d["params"][0]["Ac"][2]-d["params"][0]["Ac"][1]," - ",d["params"][0]["Ac"][1]-d["params"][0]["Ac"][0] )

    json_data.close()

#0_500:5  -6.008e-05/+0 
# 500_750: -0.000120304/+1.77636e-15 
#750_100: 3.60601  -0.146347/+0.146013
#1000_1500: -0.231966  -0.369634/+0.369606 
#1500_Inf:2.18597  -1.0193/+1.02039 

if mass=="0_500":
    stat_up=0.
    stat_down=-6.008e-05
if mass=="500_750":
    stat_up=+1.77636e-15
    stat_down=-0.000120304
if mass=="750_1000":
    stat_up=+0.146013
    stat_down=-0.146347
if mass=="1000_1500":
    stat_up=+0.369606 
    stat_down=-0.369634
if mass=="1500Inf":
    stat_up=+1.02039
    stat_down= -1.0193


# stat_up=+1.77636e-15 
# stat_down=-0.000120304
sys_up=((total_up)**2-(stat_up)**2)**0.5
sys_down=((total_down)**2-(stat_down)**2)**0.5


print("sys: ", sys_up, sys_down)
print("stat: ", stat_up, stat_down)
print("total: ", total_up, total_down)

print(d["params"][0]["Ac"][1])


# table=''
# table +=  '\begin{tabular}{|c c c |} \n'
# table +=  '\hline\n'
# table +=  'Mass bin ($M_{t\bar{t}) &  Measured A_{C} & SM Predicted A_{C} \\\\ \n'
# table +=  '\hline\n'


