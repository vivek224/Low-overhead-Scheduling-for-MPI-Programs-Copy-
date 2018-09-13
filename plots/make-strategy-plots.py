#!/usr/bin/env python
import matplotlib
import numpy as np
import sys


# these properties need to be modified before pylab is imported
# Cairo makes plots look nicer.  If you don't have Cairo, comment this out
# or do port install py27-cairo (or py2x-cairo where 2x is your python version)
#matplotlib.use('cairo')
#matplotlib.rcParams.update({
#    'patch.linewidth':          3,
#    'font.size':                10,
#    'font.family':              'sans-serif',
#    'axes.titlesize':           'medium',
#    'ytick.major.pad':          10,
#    'legend.fontsize':          10,
#    'legend.frameon':           False,
#    'legend.borderaxespad':     1.0,
#    'figure.figsize':           (5, 3),
#})

import matplotlib.pyplot as plt

#stuff someone should ever have to edit.
names      = ["NASBT-MZ", "NASSP-MZ", "NASLU-MZ", "amg2", "PF3D"]
machines   = ["fastNUMA", "fastNUMA2", "rzuseq"]

#strategies = ["Dynamic", "uSched", "genColl", "SlackConscious", "callsite", "callsite_dq", "callsite_fd"]
strategies = ["Dynamic", "uSched", "genColl", "SlackConscious", "callsite_fd"]

from map_names import map_names

colors     = ['r', 'y', 'g', 'b', 'c', 'm' ,'k', 'b' ]

width = 0.1         # the width of the bars
N = len(strategies) # number of strategies
ind = np.arange(N)  # indices along x axis for bar clusters.

def single_plot(stratTimes, staticTimes, color, app_offset, rects):
    speedUps = (staticTimes - stratTimes) / staticTimes * 100
    ind = np.arange(len(staticTimes))
    rect = plt.bar(ind + app_offset*width, speedUps, width, color=color)
    rects.append(rect)

def do_plot(machine):
    plt.figure(num=None, figsize=(6, 4), dpi=160, facecolor='w', edgecolor='k')
    files = ["%s-%s.dat" % (name, machine) for name in names]
    all_types = strategies + ["Static"]
    data = np.vstack(np.genfromtxt(f, names=True)[all_types] for f in files)
    print files
    print data.dtype.names
    rects = []
    for i, strat in enumerate(strategies):
        print machine, strat
        single_plot(data[:][strat][:,-1], data[:]["Static"][:,-1], colors[i], i, rects) for i, strat in enumerate(strategies) 

        files = ["%s-%s.dat" % (name, machine) for name in names]
        all_types = strategies + ["Static"]
        data = np.vstack(np.genfromtxt(f, names=True)[all_types] for f in files)
        print files
        print data.dtype.names
        rects = []
        for i, strat in enumerate(strategies):
            print machine, strat

    #  single_plot(data[:][strat][:,-1], data[:]["Static"][:,-1], colors[i], i, rects) for i, strat in enumerate(strategies)        
    #  data[:]["Static"][:,-1]
 
    if machine == "rzuseq":
        plt.ylim([-50, 25])
    else:
        plt.ylim([-75, 32])

    plt.axhline(color='k', linewidth=0.5)
    plt.ylabel('Percent Speedup')
    plt.xlabel('Application')
    #plt.title('Strategy comparison')
    plt.xticks(ind+width, map_names(names), size=11)

    if machine == "rzuseq":
        leg_loc = 'upper left'
    else:
        leg_loc = 'lower right'

    plt.legend((r[0] for r in rects), map_names(strategies),
               loc=leg_loc, ncol=3, frameon=False, fontsize=10.05)
    def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'% (int (height)),
                     ha='center', va='bottom')
    #for rect in rects:
    #    autolabel(rect)
    plt.tight_layout()
    plt.savefig("strategy-comp-%s.pdf" % machine, dpi=300)

for machine in machines:
    plt.clf()
    plt.subplot(111)
    do_plot(machine)
