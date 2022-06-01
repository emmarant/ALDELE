## About
A collection of python notebooks and python scripts for
  + training DL models for automatic neutron lens alignment
  + generating simulated data for said training
  
The full contents and directory organisation of this repo:

```
ALDELE
├── create_data
│   ├── create_images
│   │   └── savejpg.py
│   ├── mcstas_simulations
│   │   ├── BOA
│   │   │   └── DMC_AO_atBOA.instr
│   │   ├── common_files
│   │   │   ├── Guide_four_side.comp
│   │   │   ├── runs_prepare.py
│   │   │   ├── runs_submit.py
│   │   │   ├── Source_gen4.comp
│   │   │   ├── submit_script
│   │   │   └── submit_script~
│   │   ├── DMC
│   │   │   └── DMC_AO_atDMC.instr
│   │   ├── generic
│   │   └── README.md
│   └── README.md
├── README.md
└── LICENSE.txt

```

## How to use

1) create data (or download existing ones). See instructions in directory _create_data_ .
2) train a model. See relevant instructions in directory _DL model training_
