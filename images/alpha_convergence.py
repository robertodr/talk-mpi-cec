#!/usr/bin/python2
# -*- python -*-
# -*- coding: utf-8 -*-
# vim:filetype=python:
# (c) Roberto Di Remigio  <roberto.d.remigio@uit.no>
# licensed under the GNU Lesser General Public License

import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np

mpl.style.use('ggplot')
# The colors are from the ggplot style, consistent with grey background
ggplot = ['#E24A33', '#348ABD', '#988ED5', '#777777', '#FBC15E', '#8EBA42', '#FFB5B8']

params = {'text.usetex': False,
          'mathtext.fontset': 'stixsans',
          'font.size' : 14
         }
mpl.rcParams.update(params)

limit = 76.678052
# Get the data
fname = 'ief_convergence.dat'
data = np.loadtxt(fname, usecols=(0, 4))
ief_x = data[:, 0].astype(int)
ief_y = data[:, 1]

fname = 'pwc_convergence.dat'
data = np.loadtxt(fname, usecols=(0, 4))
pwc_x = data[:, 0].astype(int)
pwc_y = data[:, 1]

fname = 'pwl_convergence.dat'
data = np.loadtxt(fname, usecols=(0, 4))
pwl_x = data[:, 0].astype(int)
pwl_y = data[:, 1]

y_formatter = mpl.ticker.ScalarFormatter(useOffset=False)

fig, ax = plt.subplots(figsize=(12, 8))

ax.spines['right'].set_color('none')
ax.yaxis.set_ticks_position('left')

ax.tick_params(axis='x')
ax.tick_params(axis='y')

l3 = ax.plot(ief_x, ief_y, label=r'Collocation', lw=1, ls='-', marker='d', color=ggplot[0])
dof = [str(x) for x in ief_x]
coords = zip(ief_x, ief_y)
ax.annotate('{}'.format(dof[0]), xy=(coords[0]), xytext=(0, 10),  va='bottom', ha='right',  textcoords='offset points', color=ggplot[0], weight='demi')
ax.annotate('{}'.format(dof[1]), xy=(coords[1]), xytext=(0, 10),  va='bottom', ha='right',  textcoords='offset points', color=ggplot[0], weight='demi')
ax.annotate('{}'.format(dof[2]), xy=(coords[2]), xytext=(0, -20), va='bottom', ha='center', textcoords='offset points', color=ggplot[0], weight='demi')
ax.annotate('{}'.format(dof[3]), xy=(coords[3]), xytext=(0, -20), va='bottom', ha='center', textcoords='offset points', color=ggplot[0], weight='demi')
ax.annotate('{}'.format(dof[4]), xy=(coords[4]), xytext=(0, -20), va='bottom', ha='center', textcoords='offset points', color=ggplot[0], weight='demi')

ax.set_xlabel(r'Average area [$\AA^2$]')
labels = [r'0.3', r'0.2', r'0.1', r'0.05', r'0.025']
ax.set_xticks(ief_x)
ax.set_xticklabels(labels)
ax.tick_params(axis='x')

ax2 = ax.twiny()

wav_x = np.array([2, 3, 4, 5])
ax2.set_xticks(wav_x)
ax2.tick_params(axis='x')
ax2.set_xlim([1.5, 5.5])
l1 = ax2.plot(wav_x, pwc_y, label=r'Constants', lw=1, ls='-', marker='o', color=ggplot[1])
dof = [str(x) for x in pwc_x]
for i, lbl in enumerate(dof):
    ax2.annotate('{}'.format(lbl), xy=(wav_x[i], pwc_y[i]), xytext=(-5, 11), ha='left', textcoords='offset points', color=ggplot[1], weight='demi')

l2 = ax2.plot(wav_x, pwl_y, label=r'Linears', lw=1, ls='-', marker='s', color=ggplot[2])
dof = [str(x) for x in pwl_x]
for i, lbl in enumerate(dof):
    ax2.annotate('{}'.format(lbl), xy=(wav_x[i], pwl_y[i]), xytext=(0, -18), ha='center', textcoords='offset points', color=ggplot[2], weight='demi')

ax2.set_xlabel(r'Patch level')
labels = [r'2', r'3', r'4', r'5']
ax2.set_xticklabels(labels)

l4 = ax2.plot((1.5, 5.5), (limit, limit), label='Limit', ls='-.', lw=2)

ax.yaxis.set_major_formatter(y_formatter)
ax.grid(False)
ax2.grid(False)
ax.yaxis.grid(True)
ax.set_ylabel(r'Isotropic polarizability $[a_0^3]$')

lines = l1 + l2 + l3 + l4
labels = [l.get_label() for l in lines]
legend = ax.legend(lines, labels)

fig.savefig('alpha_convergence.png', transparent=False, bbox_inches='tight')

# vim:et:ts=4:sw=4
