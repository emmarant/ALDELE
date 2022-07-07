## About
A collection of python notebooks and python scripts for
  + training DL models for automatic neutron lens alignment
  + generating simulated data for said training
  
The full contents and directory organisation of this repo:

```
ALDELE
├── create_data
│   ├── create_images
│   │   ├── README.md
│   │   └── savejpg.py
│   ├── mcstas_simulations
│   │   ├── BOA
│   │   │   ├── DMC_AO_atBOA.instr
│   │   │   ├── runs_prepare.py
│   │   │   └── runs_submit.py
│   │   ├── common_files
│   │   │   ├── Guide_four_side.comp
│   │   │   ├── Source_gen4.comp
│   │   │   └── submit_script
│   │   ├── DMC
│   │   │   ├── DMC_AO_atDMC.instr
│   │   │   ├── runs_prepare.py
│   │   │   └── runs_submit.py
│   │   ├── generic
│   │   │   ├── BOA_generic.instr
│   │   │   └── runs_prepare.py
│   │   └── README.md
│   └── README.md
├── LICENSE.txt
├── model_training
│   ├── notebooks
│   │   ├── CNN_regression_double_angle.ipynb
│   │   └── CNN_regression_single_angle.ipynb
│   ├── README.md
│   ├── running_environment
│   └── running_environment~
└── README.md

9 directories, 22 files
```

## How to use

+ Step 1 : Create data (or download existing ones). *[follow instructions in directory* __create_data__ *]*
+ Step 2 : Train a model. *[follow instructions in directory* __model_training__ *]*
