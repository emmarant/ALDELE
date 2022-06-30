# Author: Emmanouela Rantsiou, PSI
# Last verified: 05/2022
# Description: prepare submission scripts for McStas simulations for a SLURM cluster environment. To submit prepared scripts, use 'run_submit.py'. 
# Assumes existence - in same folder - of:
# -- submit_script: prototype submission script to be automatically modified by this script
# -- .instr file with the McStas code (name of which is included in the 'execute' command in the 'submit_script')
# 
import os
import random
import numpy as np


### adjust accordingly
run_num = 3 # choose how many runs to prepare
root_name = 'ellipse_rot_'
nodes = 3 # choose number of nodes for each run
cpus = 48 # choose number of cpus per node
run_time = '01:00:00'
run_partition = 'short'
###


for i_run in range(1,run_num):

    # choose range and digit precision for the random number generator for the three posible rotation angles. Set to zero those that remain aligned
    ry=0.0
    rx=round(random.uniform(-1.5,1.5),4)
    rz=0.0

    # create parameter files for the mcstas simulations: they will include the three angle parameters
    param_file="params_"+root_name+"{}_{}_{}_{}.dat".format(rx,ry,rz,i_run)
    outf=open(param_file,"w")
    outf.write('gal={}\n'.format(rx))
    outf.write('rc={}\n'.format(ry))
    outf.write('gau={}\n'.format(rz))
    outf.close()

#   create individual submit scripts for each run
    submit_name='submit_' + root_name + '{}_{}_{}_{}'.format(rx,ry,rz,i_run)
    os.system('cp submit_script %s' % submit_name)

#   customize each submit script
    f_open=open("submit_script","rt")
    content=f_open.read()
    content=content.replace('dirname=test','dirname='+root_name+'{}_{}_{}_{}\n'.format(rx,ry,rz,i_run))
    content=content.replace('-J short','-J '+root_name+'{}_{}_{}_{}'.format(rx,ry,rz,i_run))
    content=content.replace('--time=01:00:00','--time='+run_time)
    content=content.replace('--partition=short','--partition='+run_partition)
    content=content.replace('-N 3', '-N '+str(nodes))
    content=content.replace('--ntasks-per-node=48', '--ntasks-per-node='+str(cpus))
    content=content.replace('SLURM_NNODES 48', 'SLURM_NNODES '+str(cpus))
    content=content.replace('out.o',root_name+'{}_{}_{}_{}.out'.format(rx,ry,rz,i_run))
    content=content.replace('out.e',root_name+'{}_{}_{}_{}.err'.format(rx,ry,rz,i_run))
    content=content.replace('params.dat',param_file)
    f_open.close()

    f_open=open(submit_name,"wt")
    f_open.write(content)
    f_open.close()


