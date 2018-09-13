#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

labelsHera = ["NASBTMZ", "NASSPMZ", "NASLUMZ", "AMG", "PF3D"]
labelsUseq = ["NASBTMZ", "NASSPMZ","NASLUMZ", "AMG", "PF3D"]
#stylesHera = ['n/a', 'g^-', 'bs-', 'ro-', '', '']
#stylesUseq = ['n/a', 'g^-', 'bs-', 'ro-', '', '']

colorsHera = ['r', 'y', 'g', 'b', 'c', 'o']
colorsUseq = ['r', 'y', 'g', 'b', 'c', 'o']

eColorsHera = ['pink', 'yellow', 'green', 'blue', 'red', 'orange']
eColorsUseq = ['pink', 'yellow', 'green', 'blue', 'red', 'orange']

LU, BT, SP, AMG, PF3D = range(5)

N = len(strategies)
BTMZStd =   (.0000, .000, .000, .000, .000)

ind = np.arange(N)  # the x locations for the groups
width = 0.1       # the width of the bars

#stuff someone should ever have to edit.
names      = ["NASBT-MZ", "NASSP-MZ", "NASLU-MZ", "amg2", "PF3D"]
machines   = ["hera", "rzuseq", "fastNUMA"]
#strategies_idle = ["dyn_idle", "uSched_idle", "s1_idle", "s2_idle", "s3_idle", "guided_idle"]
strategies_idle = ["dyn_idle", "uSched_idle", "s1_idle", "s2_idle", "s3_idle"]
#strategies_dq = ["dyn_dq", "uSched_dq", "s1_dq", "s2_dq", "s3_dq", "guided_dq"]
strategies_dq = ["dyn_dq", "uSched_dq", "s1_dq", "s2_dq", "s3_dq"]
colors     = ['r', 'y', 'g', 'b', 'c', 'e']


def single_plot(filename, color, offset, rects):
    data = np.genfromtxt(filename, names=True)
    # values in last row for all columns named in strategies
    idleTimes = data[strategies_idle][:]
    dqTimes = data[strategies_dq][:]

#TODO:  needed to  change to fix ind*width +
# offset to get the right graph, but now the colors don't show up properly...   Need to somehow cycle through the colors for each plot.
    rects1 = plt.bar(ind, data_hera_idle[:,1], width, color=colorsHera[0])
    rects2 = plt.bar(ind, data_hera_dqTimes[:,1], width, color='b', bottom=data_hera_idle[:,1] )

   # rect = plt.bar(ind +  width*offset, speedUps, width, color=color)

    rects.append(rect)


def do_plot(machine):
    rects = []
    for i, name in enumerate(names):
           single_plot("%s-%s.dat" % (name, machine), colors[i], i, rects)

    plt.ylabel('Percent Speedup')
    plt.title('Strategy comparison')
    plt.xticks(ind+width, names, size=11)

    plt.legend((r[0] for r in rects), strategies, loc='lower right', ncol=3)

    def autolabel(rects):

        for rect in rects:
            height = rect.get_height()
            plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'% (int (height)),
                     ha='center', va='bottom')

    plt.savefig("strategy-comp-%s.pdf" % machine, dpi=300)

for machine in machines:
    plt.clf()
    plt.subplot(111)
    do_plot(machine)


plt.subplot(111)


data_hera_idle = np.loadtxt("fastNUMA2-profiles-cost-idle.dat", skiprows=1)
# data_rzuseq_idle = np.loadtxt("rzuseq-profiles-cost-idle.dat", skiprows=1)

data_hera_dq = np.loadtxt("fastNUMA2-profiles-cost-dq.dat", skiprows=1)
# data_rzuseq_dq = np.loadtxt("rzuseq-profiles-cost-dq.dat", skiprows=1)


rects3 = plt.bar(ind + width, data_hera_idle[:,2] ,width, color='r')
rects4 = plt.bar(ind + width, data_hera_dq[:,2] , width, color='b', bottom=data_hera_idle[:,2])

rects5 = plt.bar(ind + 2*width, data_hera_idle[:,3] ,width, color='r')
rects6 = plt.bar(ind + 2*width, data_hera_dq[:,3] , width, color='b', bottom=data_hera_idle[:,3])

rects7 = plt.bar(ind + 3*width, data_hera_idle[:,4] ,width, color='r')
rects8 = plt.bar(ind + 3*width, data_hera_dq[:,4] , width, color='b', bottom=data_hera_idle[:,4])


rects9 = plt.bar(ind + 4*width, data_hera_idle[:,5] ,width, color='r')
rects10 = plt.bar(ind + 4*width, data_hera_dq[:,5] , width, color='b', bottom=data_hera_idle[:,5])

rects11 = plt.bar(ind + 5*width, data_hera_idle[:,6] ,width, color='r')
rects12 = plt.bar(ind + 5*width, data_hera_dq[:,6] , width, color='b', bottom=data_hera_idle[:,6])

# dataStatic = data[:,1]
# dataSpeedUps = [1.0*dataStatic[n]/dataSlackConscious[n] for n in xrange(len(dataStatic))]

# rects1 = plt.bar(ind, data[:, 1], width,
#                    color=colorsHera[0],
#                    yerr= BTMZStd,
#                    error_kw=dict(elinewidth=6, ecolor='pink'))

#rects1 = plt.bar(ind, data_rzuseq, width,
#                    color= colorsHera[1],
#                    yerr= BTMZStd,
#                    error_kw=dict(elinewidth=6, ecolor='red'))

# dataMax = np.loadtxt("NASLUMZ-hera-max.dat" %file, skiprows=1)
# dataMin = np.loadtxt("NASLUMZ-hera-min.dat" %file, skiprows=1)

# add some
plt.ylabel('Costs incurred')
plt.title('Cost of idle time and dequeue time')
plt.xticks(ind+width, ('NASSP', 'NASBT' , 'NASLU' , 'AMG' , 'PF3D'), size=11)


#plt.legend( (p1[0], p2[0], rects3[0], rects4[0], rects5[0]), ('dyn', 'uSched','genColl', 'coll', 'callsite'))

plt.legend( (rects1[0],rects2[0],  rects3[0], rects4[0], rects5[0], rects6[0], rects7[0], rects8[0], rects9[0], rects10[0], rects11[0], rects12[0]), ('dyn-idle', 'dyn-dq',  'uSched-idle', 'uSched-dq',  'genColl-idle', 'genColl-dq' ,  'coll-idle',  'coll-dq' , 'callsite-idle' , 'callsite-dq', 'guided-idle', 'guided-dq'))

#plt.yticks(np.arange(0,,10))

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'% (int (height)),
                 ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)
autolabel(rects6)
autolabel(rects7)
autolabel(rects8)
autolabel(rects9)
autolabel(rects10)
autolabel(rects11)
autolabel(rects12)

plt.savefig("app-cost-fastNUMA2.pdf", dpi=300)
