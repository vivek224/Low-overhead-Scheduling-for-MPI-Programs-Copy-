#!/usr/bin/env python

import numpy as np
import matplotlib

# these properties need to be modified before pylab is imported
# Cairo makes plots look nicer.  If you don't have Cairo, comment this out
# or do port install py27-cairo (or py2x-cairo where 2x is your python version)
matplotlib.use('cairo')
matplotlib.rcParams.update({
    'patch.linewidth':		3,
    'font.size':		10,
    'font.family':		'sans-serif',
    'axes.titlesize':		'medium',
    'ytick.major.pad':		10,
    'legend.fontsize':		9,
    'legend.frameon':		False,
    'legend.borderaxespad':	1.0,
    'figure.figsize':		(5, 3),
})

import matplotlib.pyplot as plt

from map_names import map_names

#labels = ["Nodes", "Static", "Dynamic", "Slack-Conscious", "Binding", "uSched", "15core", "callsite","genColl" ]
labels = ["Nodes", "Static", "Dynamic", "callsite_fd", "oGPUmx"]
styles = ['n/a', 'g^-', 'bs-', 'ro-', 'rx-']
strategies = ["n/a", "static", "dyn", "callsite_fd", "oGPUmx"]

#nodes, static, dyn, slack, bind, usched, core15, callsite, genColl, guided = range(10)

nodes, static, dyn, callsite, oGPUmx = range(5)

#amg_files = ["amg-hera",
#             "amg-atlas",
#             "amg-hera",
#             "amg-rzuseq"]

#dotProd_files = ["dotProd-hera",
#                 "dotProd-rzuseq"]
#NASLU_files = ["NASLU-hera",
#                 "NASLU-rzuseq"]
#NASCG_files = ["NASCG-hera",
#                 "NASCG-rzuseq"]

PF3D_files_intro_sierra = ["PF3D-fastNUMA"]
ptychoLib_files_intro_hpcc = ["ptychoLib-hpcc-weakscale"]

def plot_files(files, *sequences):
    for file in files:
        plt.figure()
        plt.xlabel("Nodes")
        plt.ylabel("Time (seconds)") 
        data = np.loadtxt("%s.dat" % file, skiprows=1)
        #data = np.genfromtxt("%s.dat" % file, names=True)
        for i in sequences:
            plt.subplots_adjust(left=0.14, right=0.95, top=0.95, bottom=0.18)
            newLabels=map_names(labels)
            plt.semilogx(data[:, 0], data[:, i], styles[i], label=newLabels[i], basex=2)
            plt.axes().minorticks_off()
            plt.grid(axis='y', which='major')
            plt.axes().set_xticklabels([int(d) for d in data[:,0]])
            plt.xticks(rotation=35)

        #plt.ylim([-50, 25])
        if file == "ptychoLib-hpcc-weakscale":
            plt.ylim([330, 800])

#        if file == "PF3D-hera-intro-basic":
        plt.legend(loc='upper left', ncol=2)
#        else:
#            plt.legend(loc='lower right', ncol=2)
        plt.savefig("%s-intro.pdf" % file, dpi=300)

# plot_files(amg_files,     static, dyn, slack, bind, usched)
# plot_files(NASLU_MZ_files, static, dyn, slack, bind, usched)
# plot_files(NASSP_MZ_files, static, dyn, slack, bind, usched)
# plot_files(NASBT_MZ_files, static, dyn, slack, bind, usched)
# plot_files(PF3D_files, static, dyn, slack, bind, usched)


#plot_files(ptychoLib_files_intro_hpcc, static, dyn, callsite, oGPUmx)

plot_files(ptychoLib_files_intro_hpcc, oGPUmx)
