## Setting up McStas simulations

---
### General information
- The McStas instrument files located in the _DMC_ and _BOA_ folders, contain other than the description of the corresponding beamline, an elliptic neutron lens component and four (4) Position Sensitive Detectors (PSD) at prefixed positions.
The elliptic lens is parametrised as follows:

``` python 
COMPONENT elliptic_lens1 = Elliptic_guide_gravity(
                            l = lens_length, linyh = 500.0, linxw = 3.4, loutyh = 0.156, loutxw = 0.310,                        
                            xwidth = 0.016, yheight = 0.06, dimensionsAt = "entrance",         
                            R0 = 0.99, Qc = 0.0219, alphatop = 4.0, alphabottom = 4.0, alpharight = 2.0, alphaleft = 2.0,                          
                            mright = 1.5, mleft = 1.5, mtop = 6.0, mbottom = 6.0, W = 0.003)
```

- The McStas instrument file located in the -generic- folder contains the description of the full BOA beamline, an elliptic neutron lens component, and various Position Sensitive Detectors (PSD) at prefixed positions. The parameters of the elliptic lens are not prefixed, but rather determined randomly by the _runs_prepare_ script, located also in the same folder. During run time, a *parameter* file including the relevant values for the elliptic_guide component is read.   

---
### Setting up runs
+ Step 1 : choose type of simulation to set up: related to a) BOA, b) DMC, c) generic set-up
+ Step 2 : 
