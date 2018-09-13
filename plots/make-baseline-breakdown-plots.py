#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

#TODO(important): check plot is correct for do_plot! (May not be generating a regular stat/dyn/guided graph)

#labels = ["NASBTMZ", "NASSPMZ", "NASLUMZ", "AMG", "PF3D"]

leg_loc = 'upper left'
files = ["dmTimes-SNAP-cab", 
	 "dmTimes-nbody-cab", 
	 "dmTimes-SNAP-rzuseq", 
	 "dmTimes-nbody-rzuseq", 
	 "dmTimes-SNAP-bw",
	 "dmTimes-nbody-bw"
	 "dmTimes-pcm-xpaccclust"] 

apps = ["NASLU", "nbody"]

#"PlasComCM-StrnRt"]

#TODO: make names and apps consistent with each other
names = [ "SNAP", "nbody", "PlasComCM-StrnRt"] 
strategies = ["comp_s", "comp_d", "comp_g", "comp_sd", "comp_besf",
	      "dq_s", "dq_d", "dq_g", "dq_besf", "dm_s", "dm_d",
	      "dm_g", "dm_sd", "dm_besf", "id_s", "id_d", "id_g",
	      "id_sd", "id_besf"] 
#]
#"sd50", "bestsf"]

machines = [ "cab", "xpaccclust"]

from map_names import map_names
from map_apps import map_apps

colors = ['r', 'y', 'g', 'b', 'c', 'm','darkslategray', 'k', 'darkslategray']

lightcolors = ['#ffbbbb',
               '#ffffbb',
               '#bbffbb',
               '#bbbbff',
               '#bbffff',
               '#ffbbff'] # set all colors to black for now

verylightcolors = ['#ffbbbf',
               '#ffffbf',
               '#bbffbb',
               '#bbbbff',
               '#fbffff',
               '#fffbff'] # set all colors to black for now

hatch = "/"
hatch2 = "x"
hatch3 = "|"

LU, BT, SP, AMG, PF3D = range(5)
N = 1  # one index per strategy 

ind = np.arange(N)  # the x locations for the groups
width = 0.005       # the width of the bars

# plt.subplot(111)
#TODO: add purpose of the below
def autolabel(rects):
        # attach some text labels
        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x()+rect.get_width()/2., 1.05*height,
                     '',
                     ha='center', va='bottom')

#with just dq ovhd (?)

#plot with sd added
def do_plot(app, machine):
    plt.figure(num=None, figsize=(6, 3), dpi=160, facecolor='w', edgecolor='none')
    #  data_idle = np.loadtxt("dqTimes-SNAP-%s.dat" % machine , skiprows=1) * 100  # TODO: change idle and dq to ldBal and ldImbBal 
    data1 = np.vstack(np.genfromtxt("dmTimes-%s-%s.dat" % (app, machine), names=True))
    print data1.dtype.names
    rects = []
    rects1 = plt.bar(ind + width, data1[:]["comp_s"][-1][0], width, color=colors[0])
    rects.append(rects1)
    rects2 = plt.bar(ind + width, data1[:]["dm_s"][-1][0], width, color=colors[1], bottom=data1[:]["comp_s"][-1][0])
    rects.append(rects2)
    rects3 = plt.bar(ind + width, data1[:]["dq_s"][-1][0], width, color=colors[2], bottom=data1[:]["comp_s"][-1][0] + data1[:]["dm_s"][-1][0])
    rects.append(rects3)
    rects4 = plt.bar(ind + width, data1[:]["id_s"][-1][0], width, color=colors[3], bottom=data1[:]["comp_s"][-1][0] + data1[:]["dm_s"][-1][0] + data1[:]["dq_s"][-1][0])
    rects.append(rects4)

    rects5 = plt.bar(ind + 3*width, data1[:]["comp_d"][-1][0], width, color=colors[0])
    rects.append(rects5)
    rects6 = plt.bar(ind + 3*width, data1[:]["dm_d"][-1][0], width, color=colors[1], bottom=data1[:]["comp_d"][-1][0])
    rects.append(rects6)
    rects7 = plt.bar(ind + 3*width, data1[:]["dq_d"][-1][0], width, color=colors[2], bottom=data1[:]["comp_d"][-1][0] + data1[:]["dm_d"][-1][0])
    rects.append(rects7)
    rects8 = plt.bar(ind + 3*width, data1[:]["id_d"][-1][0], width, color=colors[3], bottom=data1[:]["comp_d"][-1][0] + data1[:]["dm_d"][-1][0] + data1[:]["dq_d"][-1][0])
    rects.append(rects8)

    rects9 = plt.bar(ind + 5*width, data1[:]["comp_g"][-1][0], width, color=colors[0])
    rects.append(rects9)
    rects10 = plt.bar(ind + 5*width, data1[:]["dm_g"][-1][0], width, color=colors[1], bottom=data1[:]["comp_g"][-1][0])
    rects.append(rects10)
    rects11 = plt.bar(ind + 5*width, data1[:]["dq_g"][-1][0], width, color=colors[2], bottom=data1[:]["comp_g"][-1][0] + data1[:]["dm_g"][-1][0])
    rects.append(rects11)
    rects12 = plt.bar(ind + 5*width, data1[:]["id_g"][-1][0], width, color=colors[3], bottom=data1[:]["comp_g"][-1][0] + data1[:]["dm_g"][-1][0] + data1[:]["dq_g"][-1][0])
    rects.append(rects12)

    if machine == "cab": 
	    if app == "NASLU" : 
		    plt.ylim([0.0, 200.0])
	    if app == "nbody": 
		    plt.ylim([0.0, 35.0])

    if machine == "xpaccclust": 
	    if app == "pcm": 
		    plt.ylim([0.0, 220.0])

    plt.axes().set_xticklabels(['', 'static', '', ' dynamic', '', 'guided'])
    plt.ylabel('Time (s)')
    plt.xlabel('Strategy')
    appName = map_apps([app])
    plt.title('%s : %s' % (appName[0], machine))

    #    plt.xticks(ind, ('static', 'dynamic', 'guided'))
    # plt.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('comp', 'dm', 'dq', 'idle'), leg_loc, ncol=4, frameon=False, fontsize=9) 
    #     plt.legend( (rects1[0], rects3[0]),
    #                 map_names(strategies),
    #                 ncol=2, frameon=False, shadow=True, fontsize=12)
    for rects_id in rects:
	   autolabel(rects_id)
    plt.tight_layout()
    plt.savefig("dmTime-%s-%s.pdf" % (app, machine), dpi=300) 

    #plt.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ['comp', 'other', 'dq', 'idle'], leg_loc, ncol=4, frameon=False, fontsize=9)
    #  plt.legend( (rects1[0], rects3[0]),
    #                map_names(strategies),
    #                ncol=2, frameon=False, shadow=True, fontsize=12)

    for rects_id in rects:
	    autolabel(rects_id)
    plt.tight_layout()
    plt.savefig("dmTime-%s-%s-nodm.pdf" % (app, machine), dpi=300) 

#plot with sd and besf added 
def do_plot_withsdandbesf(app, machine):
    plt.figure(num=None, figsize=(6, 3), dpi=160, facecolor='w', edgecolor='none')
    #  data_idle = np.loadtxt("dqTimes-SNAP-%s.dat" % machine , skiprows=1) * 100  # TODO: change idle and dq to ldBal and ldImbBal 
    data1 = np.vstack(np.genfromtxt("dmTimes-%s-%s.dat" % (app, machine), names=True))
    print data1.dtype.names
    rects = []
    rects1 = plt.bar(ind + width, data1[:]["comp_s"][-1][0], width, color=colors[0])
    rects.append(rects1)
    rects2 = plt.bar(ind + width, data1[:]["dm_s"][-1][0], width, color=colors[1], bottom=data1[:]["comp_s"][-1][0])
    rects.append(rects2)
    rects3 = plt.bar(ind + width, data1[:]["dq_s"][-1][0], width, color=colors[2], bottom=data1[:]["comp_s"][-1][0] + data1[:]["dm_s"][-1][0])
    rects.append(rects3)
    rects4 = plt.bar(ind + width, data1[:]["id_s"][-1][0], width, color=colors[3], bottom=data1[:]["comp_s"][-1][0] + data1[:]["dq_s"][-1][0] + data1[:]["dm_s"][-1][0])
    rects.append(rects4)

    rects5 = plt.bar(ind + 3*width, data1[:]["comp_d"][-1][0], width, color=colors[0])
    rects.append(rects5)
    rects6 = plt.bar(ind + 3*width, data1[:]["dm_d"][-1][0], width, color=colors[1], bottom=data1[:]["comp_d"][-1][0])
    rects.append(rects6)
    rects7 = plt.bar(ind + 3*width, data1[:]["dq_d"][-1][0], width, color=colors[2], bottom=data1[:]["comp_d"][-1][0] + data1[:]["dm_d"][-1][0])
    rects.append(rects7)
    rects8 = plt.bar(ind + 3*width, data1[:]["id_d"][-1][0], width, color=colors[3], bottom=data1[:]["comp_d"][-1][0] + data1[:]["dq_d"][-1][0] + data1[:]["dm_d"][-1][0])
    rects.append(rects8)

    rects9 = plt.bar(ind + 5*width, data1[:]["comp_g"][-1][0], width, color=colors[0])
    rects.append(rects9)
    rects10 = plt.bar(ind + 5*width, data1[:]["dm_g"][-1][0], width, color=colors[1], bottom=data1[:]["comp_g"][-1][0])
    rects.append(rects10)
    rects11 = plt.bar(ind + 5*width, data1[:]["dq_g"][-1][0], width, color=colors[2], bottom=data1[:]["dm_g"][-1][0] + data1[:]["comp_g"][-1][0])
    rects.append(rects11)
    rects12 = plt.bar(ind + 5*width, data1[:]["id_g"][-1][0], width, color=colors[3], bottom=data1[:]["dm_g"][-1][0] + data1[:]["comp_g"][-1][0] + data1[:]["dq_g"][-1][0])
    rects.append(rects12)

    rects13 = plt.bar(ind + 7*width, data1[:]["comp_sd"][-1][0], width, color=colors[0])
    rects.append(rects13)
    rects14 = plt.bar(ind + 7*width, data1[:]["dm_sd"][-1][0], width, color=colors[1], bottom=data1[:]["comp_sd"][-1][0])
    rects.append(rects14)
    rects15 = plt.bar(ind + 7*width, data1[:]["dq_sd"][-1][0], width, color=colors[2], bottom=data1[:]["dm_sd"][-1][0] + data1[:]["comp_sd"][-1][0])
    rects.append(rects15)
    rects16 = plt.bar(ind + 7*width, data1[:]["id_sd"][-1][0], width, color=colors[3], bottom=data1[:]["dm_sd"][-1][0] + data1[:]["comp_sd"][-1][0] + data1[:]["dq_sd"][-1][0])
    rects.append(rects16)

    rects17 = plt.bar(ind + 9*width, data1[:]["comp_besf"][-1][0], width, color=colors[0])
    rects.append(rects17)
    rects18 = plt.bar(ind + 9*width, data1[:]["dm_besf"][-1][0], width, color=colors[1], bottom=data1[:]["comp_besf"][-1][0])
    rects.append(rects18)
    rects19 = plt.bar(ind + 9*width, data1[:]["dq_besf"][-1][0], width, color=colors[2], bottom=data1[:]["dm_besf"][-1][0] + data1[:]["comp_besf"][-1][0])
    rects.append(rects19)
    rects20 = plt.bar(ind + 9*width, data1[:]["id_besf"][-1][0], width, color=colors[3], bottom=data1[:]["dm_besf"][-1][0] + data1[:]["comp_besf"][-1][0] + data1[:]["dq_besf"][-1][0])
    rects.append(rects20)

    if machine == "cab":
	    if app == "NASLU" : 
		    plt.ylim([0.0, 200.0])
	    if app == "nbody": 
		    plt.ylim([0.0, 35.0])
    
    if machine == "xpaccclust": 
	    if app == "PlasComCM":
		plt.ylim([0.0, 200.0])

    plt.ylabel('Time (s)')
    plt.xlabel('Strategy')

    appName = map_apps([app])
    plt.title('%s : %s' % (appName[0], machine))
    plt.axes().set_xticklabels( ['', '  static', '','  dynamic', '', '  guided', '' , 'half', '', '  besf'])

#    plt.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('comp',  'dm', 'dq', 'idle'), leg_loc, ncol=4, frameon=False, fontsize=9)
    for rects_id in rects:
	   autolabel(rects_id)
    plt.tight_layout()
    plt.savefig("dmTime-%s-%s-withsdandbesf.pdf" % (app, machine), dpi=300)

# with just sd added

def do_plot_withsd(app, machine):
    plt.figure(num=None, figsize=(6, 3), dpi=160, facecolor='w', edgecolor='none')
    #  data_idle = np.loadtxt("dqTimes-SNAP-%s.dat" % machine , skiprows=1) * 100  # TODO: change idle and dq to ldBal and ldImbBal 
    data1 = np.vstack(np.genfromtxt("dmTimes-%s-%s.dat" % (app, machine), names=True))
    print data1.dtype.names
    rects = []
    rects1 = plt.bar(ind + width, data1[:]["comp_s"][-1][0], width, color=colors[0])
    rects.append(rects1)
    rects2 = plt.bar(ind + width, data1[:]["dm_s"][-1][0], width, color=colors[1], bottom=data1[:]["comp_s"][-1][0])
    rects.append(rects2)
    rects3 = plt.bar(ind + width, data1[:]["dq_s"][-1][0], width, color=colors[2], bottom=data1[:]["comp_s"][-1][0] + data1[:]["dm_s"][-1][0])
    rects.append(rects3)
    rects4 = plt.bar(ind + width, data1[:]["id_s"][-1][0], width, color=colors[3], bottom=data1[:]["comp_s"][-1][0] + data1[:]["dq_s"][-1][0] + data1[:]["dm_s"][-1][0])
    rects.append(rects4)

    rects5 = plt.bar(ind + 3*width, data1[:]["comp_d"][-1][0], width, color=colors[0])
    rects.append(rects5)
    rects6 = plt.bar(ind + 3*width, data1[:]["dm_d"][-1][0], width, color=colors[1], bottom=data1[:]["comp_d"][-1][0])
    rects.append(rects6)
    rects7 = plt.bar(ind + 3*width, data1[:]["dq_d"][-1][0], width, color=colors[2], bottom=data1[:]["comp_d"][-1][0] + data1[:]["dm_d"][-1][0])
    rects.append(rects7)
    rects8 = plt.bar(ind + 3*width, data1[:]["id_d"][-1][0], width, color=colors[3], bottom=data1[:]["comp_d"][-1][0] + data1[:]["dq_d"][-1][0] + data1[:]["dm_d"][-1][0])
    rects.append(rects8)

    rects9 = plt.bar(ind + 5*width, data1[:]["comp_g"][-1][0], width, color=colors[0])
    rects.append(rects9)
    rects10 = plt.bar(ind + 5*width, data1[:]["dm_g"][-1][0], width, color=colors[1], bottom=data1[:]["comp_g"][-1][0])
    rects.append(rects10)
    rects11 = plt.bar(ind + 5*width, data1[:]["dq_g"][-1][0], width, color=colors[2], bottom=data1[:]["dm_g"][-1][0] + data1[:]["comp_g"][-1][0])
    rects.append(rects11)
    rects12 = plt.bar(ind + 5*width, data1[:]["id_g"][-1][0], width, color=colors[3], bottom=data1[:]["dm_g"][-1][0] + data1[:]["comp_g"][-1][0] + data1[:]["dq_g"][-1][0])
    rects.append(rects12)

    rects13 = plt.bar(ind + 7*width, data1[:]["comp_sd"][-1][0], width, color=colors[0])
    rects.append(rects13)
    rects14 = plt.bar(ind + 7*width, data1[:]["dm_sd"][-1][0], width, color=colors[1], bottom=data1[:]["comp_sd"][-1][0])
    rects.append(rects14)
    rects15 = plt.bar(ind + 7*width, data1[:]["dq_sd"][-1][0], width, color=colors[2], bottom=data1[:]["dm_sd"][-1][0] + data1[:]["comp_sd"][-1][0])
    rects.append(rects15)
    rects16 = plt.bar(ind + 7*width, data1[:]["id_sd"][-1][0], width, color=colors[3], bottom=data1[:]["dm_sd"][-1][0] + data1[:]["comp_sd"][-1][0] + data1[:]["dq_sd"][-1][0])
    rects.append(rects16)

    if machine == "cab":
	    if app == "NASLU" : 
		    plt.ylim([0.0, 200.0])
	    if app == "nbody": 
		    plt.ylim([0.0, 35.0])

    plt.ylabel('Time (s)')
    plt.xlabel('Strategy')

    appName = map_apps([app])
    plt.title('%s : %s' % (appName[0], machine))
    plt.axes().set_xticklabels( ['', '  static', '','  dynamic', '', '  guided', '' , 'half',])

   # plt.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('comp',  'dm', 'dq', 'idle'), leg_loc, ncol=4, frameon=False, fontsize=9)
    #for rects_id in rects:
    #   autolabel(rects_id)
    plt.tight_layout()
    plt.savefig("dmTime-%s-%s-withsd.pdf" % (app, machine), dpi=300)


#plot with just besf added (and not sd) 

def do_plot_withbesf(app, machine):
    plt.figure(num=None, figsize=(6, 3), dpi=160, facecolor='w', edgecolor='none')
    data1 = np.vstack(np.genfromtxt("dmTimes-%s-%s.dat" % (app, machine), names=True))
    print data1.dtype.names
    rects = [] 

    rects1 = plt.bar(ind + width, data1[:]["comp_s"][-1][0], width, color=colors[0])
    rects.append(rects1)
    rects2 = plt.bar(ind + width, data1[:]["dm_s"][-1][0], width, color=colors[1], bottom=data1[:]["comp_s"][-1][0])
    rects.append(rects2)
    rects3 = plt.bar(ind + width, data1[:]["dq_s"][-1][0], width, color=colors[2], bottom=data1[:]["comp_s"][-1][0] + data1[:]["dm_s"][-1][0])
    rects.append(rects3)
    rects4 = plt.bar(ind + width, data1[:]["id_s"][-1][0], width, color=colors[3], bottom=data1[:]["comp_s"][-1][0] + data1[:]["dq_s"][-1][0] + data1[:]["dm_s"][-1][0])
    rects.append(rects4)

    rects5 = plt.bar(ind + 3*width, data1[:]["comp_d"][-1][0], width, color=colors[0])
    rects.append(rects5)
    rects6 = plt.bar(ind + 3*width, data1[:]["dm_d"][-1][0], width, color=colors[1], bottom=data1[:]["comp_d"][-1][0])
    rects.append(rects6)
    rects7 = plt.bar(ind + 3*width, data1[:]["dq_d"][-1][0], width, color=colors[2], bottom=data1[:]["comp_d"][-1][0] + data1[:]["dm_d"][-1][0])
    rects.append(rects7)
    rects8 = plt.bar(ind + 3*width, data1[:]["id_d"][-1][0], width, color=colors[3], bottom=data1[:]["comp_d"][-1][0] + data1[:]["dq_d"][-1][0] + data1[:]["dm_d"][-1][0])
    rects.append(rects8)

    rects9 = plt.bar(ind + 5*width, data1[:]["comp_g"][-1][0], width, color=colors[0])
    rects.append(rects9)
    rects10 = plt.bar(ind + 5*width, data1[:]["dm_g"][-1][0], width, color=colors[1], bottom=data1[:]["comp_g"][-1][0])
    rects.append(rects10)
    rects11 = plt.bar(ind + 5*width, data1[:]["dq_g"][-1][0], width, color=colors[2], bottom=data1[:]["dm_g"][-1][0] + data1[:]["comp_g"][-1][0])
    rects.append(rects11)
    rects12 = plt.bar(ind + 5*width, data1[:]["id_g"][-1][0], width, color=colors[3], bottom=data1[:]["dm_g"][-1][0] + data1[:]["comp_g"][-1][0] + data1[:]["dq_g"][-1][0])
    rects.append(rects12) 

    rects13 = plt.bar(ind + 7*width, data1[:]["comp_besf"][-1][0], width, color=colors[0])
    rects.append(rects13)
    rects14 = plt.bar(ind + 7*width, data1[:]["dm_besf"][-1][0], width, color=colors[1], bottom=data1[:]["comp_besf"][-1][0])
    rects.append(rects14)
    rects15 = plt.bar(ind + 7*width, data1[:]["dq_besf"][-1][0], width, color=colors[2], bottom=data1[:]["comp_besf"][-1][0] + data1[:]["dm_besf"][-1][0])
    rects.append(rects15)
    rects16 = plt.bar(ind + 7*width, data1[:]["id_besf"][-1][0], width, color=colors[3], bottom=data1[:]["comp_besf"][-1][0] + data1[:]["dm_besf"][-1][0] + data1[:]["dq_besf"][-1][0])
    rects.append(rects16)
    
    if machine == "cab": 
	    if app == "NASLU" : 
		    plt.ylim([0.0, 200.0])
	    if app == "nbody": 
		    plt.ylim([0.0, 35.0])
	    if app == "PlasComCM-StrnRt": 
		    plt.ylim([0.0, 205.0])

    if machine == "xpaccclust":
	    if app == "PlasComCM-StrnRt":
		    plt.ylim([0.0, 60.0])
	    


    plt.ylabel('Time (s)')
    plt.xlabel('Strategy')
    appName = map_apps([app])

    if app == "PlasComCM-StrnRt": 
	    plt.title('%s : %s' % (appName[0], 'cab'))

    # plt.xticks(ind, ('static', 'dynamic', 'guided'))
    plt.axes().set_xticklabels(['', '  static', '','  dynamic', '', '  guided', '', 'besf'])
    #plt.legend( (rects1[0], rects2[0], rects3[0], rects4[0]), ('comp',  'dm', 'dq', 'idle'), leg_loc, ncol=4, frameon=False, fontsize=9)

    for rects_id in rects:
	   autolabel(rects_id)
    plt.tight_layout()
    plt.savefig("dmTime-%s-%s-withbesf.pdf" % (app, machine), dpi=300) 


def do_plot_idleonly(app, machine):
    plt.figure(num=None, figsize=(6, 3), dpi=160, facecolor='w', edgecolor='none')
    data1 = np.vstack(np.genfromtxt("dmTimes-%s-%s.dat" % (app, machine), names=True))
    print data1.dtype.names
    rects = [] 

    rects1 = plt.bar(ind + width, data1[:]["comp_s"][-1][0], width, color=colors[-1])
    rects.append(rects1)
    rects2 = plt.bar(ind + width, data1[:]["dm_s"][-1][0], width, color=colors[-1], bottom=data1[:]["comp_s"][-1][0])
    rects.append(rects2)
    rects3 = plt.bar(ind + width, data1[:]["dq_s"][-1][0], width, color=colors[-1], bottom=data1[:]["comp_s"][-1][0] + data1[:]["dm_s"][-1][0])
    rects.append(rects3)
    rects4 = plt.bar(ind + width, data1[:]["id_s"][-1][0], width, color=colors[3], bottom=data1[:]["comp_s"][-1][0] + data1[:]["dq_s"][-1][0] + data1[:]["dm_s"][-1][0])
    rects.append(rects4)

    rects5 = plt.bar(ind + 3*width, data1[:]["comp_d"][-1][0], width, color=colors[-1])
    rects.append(rects5)
    rects6 = plt.bar(ind + 3*width, data1[:]["dm_d"][-1][0], width, color=colors[-1], bottom=data1[:]["comp_d"][-1][0])
    rects.append(rects6)
    rects7 = plt.bar(ind + 3*width, data1[:]["dq_d"][-1][0], width, color=colors[-1], bottom=data1[:]["comp_d"][-1][0] + data1[:]["dm_d"][-1][0])
    rects.append(rects7)
    rects8 = plt.bar(ind + 3*width, data1[:]["id_d"][-1][0], width, color=colors[3], bottom=data1[:]["comp_d"][-1][0] + data1[:]["dq_d"][-1][0] + data1[:]["dm_d"][-1][0])
    rects.append(rects8)

    rects9 = plt.bar(ind + 5*width, data1[:]["comp_g"][-1][0], width, color=colors[-1])
    rects.append(rects9)
    rects10 = plt.bar(ind + 5*width, data1[:]["dm_g"][-1][0], width, color=colors[-1], bottom=data1[:]["comp_g"][-1][0])
    rects.append(rects10)
    rects11 = plt.bar(ind + 5*width, data1[:]["dq_g"][-1][0], width, color=colors[-1], bottom=data1[:]["dm_g"][-1][0] + data1[:]["comp_g"][-1][0])
    rects.append(rects11)
    rects12 = plt.bar(ind + 5*width, data1[:]["id_g"][-1][0], width, color=colors[3], bottom=data1[:]["dm_g"][-1][0] + data1[:]["comp_g"][-1][0] + data1[:]["dq_g"][-1][0])
    rects.append(rects12)

    if machine == "cab":
	    if app == "NASLU" :
		    plt.ylim([0.0, 200.0])
	    if app == "nbody": 
		    plt.ylim([0.0, 35.0])

    plt.ylabel('Time (s)')
    plt.xlabel('Strategy')

    appName = map_apps([app])
    plt.title('%s : %s' % (appName[0], machine))
    # plt.xticks(ind, ('static', 'dynamic', 'guided'))
    plt.axes().set_xticklabels(['', '  static', '','  dynamic', '', '  guided']) 
    plt.legend( (rects1[0], rects4[0]), ('other',  'idle'), leg_loc, ncol=4, frameon=False, fontsize=9)
    for rects_id in rects:
	   autolabel(rects_id)

    plt.tight_layout()
    plt.savefig("dmTime-%s-%s-idleonly.pdf" % (app, machine), dpi=300)

def do_plot_totalTime(app, machine):
    plt.figure(num=None, figsize=(6, 3), dpi=160, facecolor='w', edgecolor='none')
    data1 = np.vstack(np.genfromtxt("dmTimes-%s-%s.dat" % (app, machine), names=True))
    print data1.dtype.names
    rects = [] 
    rects1 = plt.bar(ind + width, data1[:]["comp_s"][-1][0], width, color=colors[-1])
    rects.append(rects1)
    rects2 = plt.bar(ind + width, data1[:]["dm_s"][-1][0], width, color=colors[-1], bottom=data1[:]["comp_s"][-1][0])
    rects.append(rects2)
    rects3 = plt.bar(ind + width, data1[:]["dq_s"][-1][0], width, color=colors[-1], bottom=data1[:]["comp_s"][-1][0] + data1[:]["dm_s"][-1][0])
    rects.append(rects3)
    rects4 = plt.bar(ind + width, data1[:]["id_s"][-1][0], width, color=colors[-1], bottom=data1[:]["comp_s"][-1][0] + data1[:]["dq_s"][-1][0] + data1[:]["dm_s"][-1][0])
    rects.append(rects4)

    rects5 = plt.bar(ind + 3*width, data1[:]["comp_d"][-1][0], width, color=colors[-1])
    rects.append(rects5)
    rects6 = plt.bar(ind + 3*width, data1[:]["dm_d"][-1][0], width, color=colors[-1], bottom=data1[:]["comp_d"][-1][0])
    rects.append(rects6)
    rects7 = plt.bar(ind + 3*width, data1[:]["dq_d"][-1][0], width, color=colors[-1], bottom=data1[:]["comp_d"][-1][0] + data1[:]["dm_d"][-1][0])
    rects.append(rects7)
    rects8 = plt.bar(ind + 3*width, data1[:]["id_d"][-1][0], width, color=colors[-1], bottom=data1[:]["comp_d"][-1][0] + data1[:]["dq_d"][-1][0] + data1[:]["dm_d"][-1][0])
    rects.append(rects8)

    rects9 = plt.bar(ind + 5*width, data1[:]["comp_g"][-1][0], width, color=colors[-1])
    rects.append(rects9)
    rects10 = plt.bar(ind + 5*width, data1[:]["dm_g"][-1][0], width, color=colors[-1], bottom=data1[:]["comp_g"][-1][0])
    rects.append(rects10)
    rects11 = plt.bar(ind + 5*width, data1[:]["dq_g"][-1][0], width, color=colors[-1], bottom=data1[:]["dm_g"][-1][0] + data1[:]["comp_g"][-1][0])
    rects.append(rects11)
    rects12 = plt.bar(ind + 5*width, data1[:]["id_g"][-1][0], width, color=colors[-1], bottom=data1[:]["dm_g"][-1][0] + data1[:]["comp_g"][-1][0] + data1[:]["dq_g"][-1][0])
    rects.append(rects12)

    if machine == "cab":
	    if app == "NASLU" :
		    plt.ylim([0.0, 200.0])
	    if app == "nbody": 
		    plt.ylim([0.0, 35.0])

    if machine == "xpaccclust":
	    if app == "PlasComCM-StrnRt" :
		    plt.ylim([0.0, 220.0])

    plt.ylabel('Time (s)')
    plt.xlabel('Strategy')

    appName = map_apps([app])
    plt.title('%s : %s' % (appName[0], machine))
    # plt.xticks(ind, ('static', 'dynamic', 'guided'))
    plt.axes().set_xticklabels(['', '  static', '','  dynamic', '', '  guided'])
   # plt.legend( (rects1[0], r), leg_loc, ncol=4, frameon=False, fontsize=9)
    for rects_id in rects:
	   autolabel(rects_id)
    plt.tight_layout()
    plt.savefig("baseline-%s-%s-wallTime.pdf" % (app, machine), dpi=300)


#TODO: add in CPU/GPU hybrid 
#TODO: check the name of the below function (specifically, see if withGPUandMPI makes sense.
def do_plot_totalTime_withGPUandMPI(app, machine):
    plt.figure(num=None, figsize=(6, 3), dpi=160, facecolor='w', edgecolor='none')

    data1 = np.vstack(np.genfromtxt("dmTimes-%s-%s.dat" % (app, machine), names=True))
    print data1.dtype.names
    rects = [] 

#TODO: check ordering, i.e.,  if it makes sense generally  

    rects1 = plt.bar(ind + width, data1[:]["comp_mpi"][-1][0] + data1[:]["dm_mpi"][-1][0] + data1[:]["dq_mpi"][-1][0] + data1[:]["id_mpi"][-1][0], width, color=colors[-1])
    rects.append(rects1)

    rects5 = plt.bar(ind + 3*width, data1[:]["comp_s"][-1][0] + data1[:]["dm_s"][-1][0] + data1[:]["dq_s"][-1][0] + data1[:]["id_s"][-1][0] , width, color=colors[-1]) 
    rects.append(rects5) 

    rects9 = plt.bar(ind + 5*width, data1[:]["comp_besf"][-1][0] + data1[:]["dm_besf"][-1][0] + data1[:]["dq_besf"][-1][0] + data1[:]["id_besf"][-1][0] , width, color=colors[-1]) 
    rects.append(rects9) 

    rects13 = plt.bar(ind + 7*width, data1[:]["comp_gpu"][-1][0] + data1[:]["dm_gpu"][-1][0] + data1[:]["dq_gpu"][-1][0] + data1[:]["id_gpu"][-1][0] , width, color=colors[-1]) 
    rects.append(rects13) 

    if machine == "cab":
	    if app == "NASLU" :
		    plt.ylim([0.0, 200.0])
	    if app == "nbody": 
		    plt.ylim([0.0, 35.0])

    if machine == "xpaccclust":
	    if app == "PlasComCM-StrnRt" :
		    plt.ylim([0.0, 70.0])

    plt.ylabel('Time (s)')
    plt.xlabel('Strategy')

    appName = map_apps([app])
    plt.title('%s : %s' % (appName[0], machine))
    # plt.xticks(ind, ('static', 'dynamic', 'guided'))
    plt.axes().set_xticklabels(['', ' mpi','', '  static', '', ' besf', '', ' gpu'])
   # plt.legend( (rects1[0], r), leg_loc, ncol=4, frameon=False, fontsize=9)
    for rects_id in rects:
	   autolabel(rects_id)
    plt.tight_layout()
    plt.savefig("baseline-%s-%s-wallTime-withGPUandMPI.pdf" % (app, machine), dpi=300) 

def do_plot_idleanddqonly(app, machine):
    plt.figure(num=None, figsize=(6, 3), dpi=160, facecolor='w', edgecolor='none')
    data1 = np.vstack(np.genfromtxt("dmTimes-%s-%s.dat" % (app, machine), names=True))
    print data1.dtype.names
    rects = []
    rects1 = plt.bar(ind + width, data1[:]["comp_s"][-1][0], width, color=colors[-1])
    rects.append(rects1)
    rects2 = plt.bar(ind + width, data1[:]["dm_s"][-1][0], width, color=colors[-1], bottom=data1[:]["comp_s"][-1][0])
    rects.append(rects2)
    rects3 = plt.bar(ind + width, data1[:]["dq_s"][-1][0], width, color=colors[2], bottom=data1[:]["comp_s"][-1][0] + data1[:]["dm_s"][-1][0])
    rects.append(rects3)
    rects4 = plt.bar(ind + width, data1[:]["id_s"][-1][0], width, color=colors[3], bottom=data1[:]["comp_s"][-1][0] + data1[:]["dq_s"][-1][0] + data1[:]["dm_s"][-1][0])
    rects.append(rects4)
    rects5 = plt.bar(ind + 3*width, data1[:]["comp_d"][-1][0], width, color=colors[-1])
    rects.append(rects5)
    rects6 = plt.bar(ind + 3*width, data1[:]["dm_d"][-1][0], width, color=colors[-1], bottom=data1[:]["comp_d"][-1][0])
    rects.append(rects6)
    rects7 = plt.bar(ind + 3*width, data1[:]["dq_d"][-1][0], width, color=colors[2], bottom=data1[:]["comp_d"][-1][0] + data1[:]["dm_d"][-1][0])
    rects.append(rects7)
    rects8 = plt.bar(ind + 3*width, data1[:]["id_d"][-1][0], width, color=colors[3], bottom=data1[:]["comp_d"][-1][0] + data1[:]["dq_d"][-1][0] + data1[:]["dm_d"][-1][0])
    rects.append(rects8)
    rects9 = plt.bar(ind + 5*width, data1[:]["comp_g"][-1][0], width, color=colors[-1])
    rects.append(rects9)
    rects10 = plt.bar(ind + 5*width, data1[:]["dm_g"][-1][0], width, color=colors[-1], bottom=data1[:]["comp_g"][-1][0])
    rects.append(rects10)
    rects11 = plt.bar(ind + 5*width, data1[:]["dq_g"][-1][0], width, color=colors[2], bottom=data1[:]["dm_g"][-1][0] + data1[:]["comp_g"][-1][0])
    rects.append(rects11)
    rects12 = plt.bar(ind + 5*width, data1[:]["id_g"][-1][0], width, color=colors[3], bottom=data1[:]["dm_g"][-1][0] + data1[:]["comp_g"][-1][0] + data1[:]["dq_g"][-1][0])
    rects.append(rects12) 

    if machine == "cab":
	    if app == "NASLU" :
		    plt.ylim([0.0, 200.0])
	    if app == "nbody":
		    plt.ylim([0.0, 35.0])

    plt.ylabel('Time (s)')
    plt.xlabel('Strategy')
    appName = map_apps([app])
    plt.title('%s : %s' % (appName[0], machine))
    # plt.xticks(ind, ('static', 'dynamic', 'guided'))
    plt.axes().set_xticklabels(['', '  static', '','  dynamic', '', '  guided']) 
    plt.legend( (rects1[0], rects3[0], rects4[0]), ('other', 'dq', 'idle'), leg_loc, ncol=4, frameon=False, fontsize=9)
    for rects_id in rects:
	   autolabel(rects_id)
    plt.tight_layout()
    plt.savefig("dmTime-%s-%s-idleanddqonly.pdf" % (app, machine), dpi=300)

for machine in machines:
	for app in apps:
		plt.clf()
		plt.subplot(111)
		do_plot(app, machine) 
		do_plot_withsd(app, machine)
		do_plot_withbesf(app, machine) 
#		do_plot_totalTime(app, machine)

# Note: can only do the below with the xpacc cluster and PlasComCM for right now . 
#		do_plot_totalTime_withGPUandMPI('PlasComCM-StrnRt', 'xpaccclust')

		do_plot_withsdandbesf(app, machine)
#		do_plot_idleonly(app, machine) 
#		do_plot_idleanddqonly(app, machine) 

