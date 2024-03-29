# __Author__: Emmanouela Rantsiou.
# __Last edited__: May 2022
# __Description__: descents into the run directories of mcstas simulations and creates grayscale jpg images from all the dat files there.
# It then saves them into: data/name_of_run_dir
# Assumes this python file is in same dir level as: a) the folder that holds the mcstas simulations (DIR_DIR here) and the root directory where the resulting
# images are saved ('data' dir in this case). 
# Works (at minimum) with python2.7


import numpy as np
import matplotlib.pyplot as plt
import os
import glob

# ##########################
# Input required by user:
DIR_DIR='DMC_AO_atBOA_5'            # path of the folder with mcstas runs. 
dirs_root_name = 'ellipse_rot_'     # the root name of all run dirs into DIR_DIR. 
num_PSD = 4                         # number of *.dat files (PSD monitors) in each one of the 'dirs'
image_dir='data/DMC_AO_atBOA_5'     # where to save the jpg images.
skiplines=39                        # number of header lines in the mcstas PSD dat files. Typically 39. 
# #########################

# Create image_dir if it does not exist
if not os.path.exists(image_dir):
    os.makedirs(image)dir)

dirs=glob.glob(os.path.join(DIR_DIR,dirs_root_name+"*"))
num=1

for folder in dirs:
    for filename in range(1,num_PSD+1):
        fullpath,directory = os.path.split(folder)
        _, needed = directory.split(dirs_root_name)
        rx,ry,rz,dirID = needed.split('_')    
        datname=folder + '/PSD_after_ellipse{}.dat'.format(filename)
        if os.path.exists(datname):
            imname=os.path.join(image_dir, dirs_root_name)+'{}_{}_{}_{}.jpg'.format(rx,ry,rz,num)                                                            
            data=np.array                                                                                                                             
            data = np.loadtxt(datname, skiprows = skiplines)   
            data2=data[0:1024,:]                                                                                                                             
            image=plt.figure(frameon=False)                                                                                                                  
            image.set_size_inches(10,10)                                                                                                                     
            ax=plt.Axes(image,[0.,0.,1.,1.])                                                                                                                
            ax.set_axis_off()                                                                                                                          
            image.add_axes(ax)                                                                                                                               
            ax.imshow(data2,aspect='auto',cmap='gray')                                                                                                       
            image.savefig(imname,quality=95)                                                                                                                 
            num+=1                                                                                                                                           
            print(imname) 
            print(dirID)                                                      
            plt.close(image)                                                                                                              
    


