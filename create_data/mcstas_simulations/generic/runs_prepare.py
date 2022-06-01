
import os
import random
import numpy as np

#pick semimajor axis, semiminor axis, lens lenght, and offset of lens opening to ellipse center (there are inter-depandansied among those, for meaningful results)

#angles=[-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0]
for i_run in range(450,650):
    src_bunk=8.73 # distance between the source location - and therefore location of first focal point - to bunker entance

    b_min=0.003    # somewhat arbitrarily chosen
    b_max=0.15     # somewhat arbitrarily chosen


    a_min=np.sqrt(4.5**2 + b_min**2)
    a_max=np.sqrt(src_bunk**2 + b_max**2)


    a_major=random.uniform(a_min,a_max)
    b_minor=random.uniform(b_min,b_max)

    c_foc=np.sqrt(a_major**2 - b_minor**2)

    l_min=0.05
    l_max=2.0*c_foc - src_bunk


    lens_length=random.uniform(l_min,l_max)
    offset=random.uniform(c_foc - src_bunk,lens_length - c_foc)

    lens_pos=-offset-(8.73-c_foc) # where the lens should be placed in order for focus point A to be at source
    lens_entrance_pos=random.uniform(0.01,lens_pos)

    mLR=random.uniform(1.5,6.0)
    mTB=random.uniform(1.5,6.0)

    ry=round(random.uniform(-3.0,3.0),3)
    rx=0.0
    rz=0.0

    param_file="params_ell_rot_{}_{}_{}_{}.dat".format(rx,ry,rz,i_run)
    outf=open(param_file,"w")
    outf.write('a_maj={}\n'.format(a_major))
    outf.write('b_min={}\n'.format(b_minor))
    outf.write('offset={}\n'.format(offset))
    outf.write('lens_length={}\n'.format(lens_length))
    outf.write('lens_entrance_pos={}\n'.format(lens_entrance_pos))
    outf.write('mLR={}\n'.format(mLR))
    outf.write('mTB={}\n'.format(mTB))
    outf.write('rx={}\n'.format(rx))
    outf.write('ry={}\n'.format(ry))
    outf.write('rz={}\n'.format(rz))
    outf.close()

#   create individual submit scripts for each run
    submit_name='submit_ellipse_rot_{}_{}_{}_{}'.format(rx,ry,rz,i_run)
    os.system('cp submit_script %s' % submit_name)

#   customize each submit script
    f_open=open("submit_script","rt")
    content=f_open.read()
    content=content.replace('dirname=test','dirname=ellipse_rot_{}_{}_{}_{}\n'.format(rx,ry,rz,i_run))
    content=content.replace('-J short','-J ellipse_rot_{}_{}_{}_{}'.format(rx,ry,rz,i_run))
    content=content.replace('out.o','ellipse_rot_{}_{}_{}_{}.out'.format(rx,ry,rz,i_run))
    content=content.replace('out.e','ellipse_rot_{}_{}_{}_{}.err'.format(rx,ry,rz,i_run))
    content=content.replace('params.dat',param_file)
    f_open.close()

    f_open=open(submit_name,"wt")
    f_open.write(content)
    f_open.close()

#   submit and best of luck to you my friend!!
    os.system('sbatch %s' % submit_name)
