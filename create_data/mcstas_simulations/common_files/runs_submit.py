# Author: Emmanouela Rantsiou
# Last verified: 05/2022
# Description: use to submit submission scripts in a SLURM environment, after having created a said scripts by using 'runs_prepare.py'. 
# Assumes existence - in same folder - of:                                                                                                                  
# -- *.instr file with the McStas code (name of which is included in the 'execute' command in the 'submit_script')                               
# -- Guide_four_side.comp McStas component
# -- Source_gen4.comp McStas component

import os
import random
import numpy as np
import glob

###### Set relevant range of submit files and root_name
r_start=1
r_end=5
root_name='ellipse_rot_'
######

for i_run in range(r_start,r_end):

#   get name of  individual submit scripts for each run
    submit_name=glob.glob('submit_'+root_name+'*_*_*_'+str(i_run))
    print(submit_name[0])

#   submit and best of luck to you my friend!!
    os.system('sbatch %s' % submit_name[0])
