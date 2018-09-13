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

#labels = ["Nodes", "Static", "Dynamic", "Slack-Conscious", "Binding", "uSched", "15core", "callsite","genColl" ]
#labels = ["Nodes", "Static", "Dynamic", "uSched", "callsite" ]
#styles = ['n/a', 'g^-', 'bs-', 'ro-', 'mo-' ]

labels = ["Nodes", "Static", "Dynamic", "Collective",  "uSched", "callsite" , "Naive", "guided", "callsite_dq" , "callsite_fd"]
styles = ['n/a', 'g^-', 'bs-', 'ro-', 'ks-', 'r^-' , 'gs-', 'mo-', 'bo-', 'go-']

strategies = ["Dynamic", "uSched", "genColl", "SlackConscious", "callsite", "guided", "callsite_dq", "callsite_fd"]
from map_names import map_names

#nodes, static, dyn, slack, bind, usched, core15, callsite, genColl = range(9)

nodes, static, dyn, slackconscious, usched, callsite, genColl, guided, resilient_callsite_dq, resilient_callsite_fd = range(10)

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

PF3D_files_intro = ["PF3D-fastNUMA", "PF3D-fastNUMA2", "PF3D-rzuseq"]

def single_line_plot(stratNum, myData):
    plt.subplots_adjust(left=0.14, right=0.95, top=0.95, bottom=0.18)
    newLabels = map_names(labels)
    plt.semilogx(myData[:,0], myData[:, stratNum], styles[stratNum], label=newLabels[stratNum], basex=2)
    plt.axes().minorticks_off()
    plt.grid(axis='y', which='major')
    plt.axes().set_xticklabels([int(d) for d in myData[:,0]])
    plt.xticks(rotation=35)

def single_line_plot_strat(stratName, stratNum, myData):
    plt.subplots_adjust(left=0.14, right=0.95, top=0.95, bottom=0.18)
    plt.semilogx(myData["Nodes"], myData[stratName], styles[stratNum], label=labels[stratNum], basex=2)
    plt.axes().minorticks_off()
    plt.grid(axis='y', which='major')
    plt.axes().set_xticklabels([int(d) for d in myData[:,0]])
    plt.xticks(rotation=35)

def plot_files(files, *sequences):
    for file in files:
        plt.figure()
        plt.xlabel("Nodes")
        plt.ylabel("Time (seconds)")
        data = np.vstack(np.genfromtxt("%s.dat" % file, names=True))
        data = np.loadtxt("%s.dat" % file, skiprows=1)
        #for i, strat in enumerate(strategies):
        single_line_plot(sequences[0], data) # plot static line
        single_line_plot(sequences[1], data) # plot dynamic line
        #single_line_plot(sequences[2], data) # plot slackconscious line
        single_line_plot(sequences[3], data) # plot usched line
        #single_line_plot(sequences[4], data) # plot callsite line
        #single_line_plot(sequences[5], data) # plot genColl line
        single_line_plot(sequences[6], data) # plot guided line
        #single_line_plot(sequences[7], data) # plot callsite_dq line
        single_line_plot(sequences[8], data) # plot callsite_fd line

        if file == "PF3D-fastNUMA":
            plt.legend(loc='upper left', ncol=3)
            plt.ylim([1250, 2000])
        if file == "PF3D-fastNUMA2":
            plt.legend(loc='upper left', ncol=3)
            plt.ylim([900, 1800])
        if file == "PF3D-rzuseq":
            plt.legend(loc='upper left', ncol=3)
            plt.ylim([1100, 1400])

        plt.savefig("%s-scaleLine.pdf" % file, dpi=300)

plot_files(PF3D_files_intro, static, dyn, slackconscious, usched, callsite, genColl, guided, resilient_callsite_dq, resilient_callsite_fd)
