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

- The McStas instrument file located in the -generic- folder contains the description of the full BOA beamline, an elliptic neutron lens component, and various Position Sensitive Detectors (PSD) at prefixed positions. The parameters of the elliptic lens are not prefixed, but rather assigned randomly by the _runs_prepare.py_ script, located also in the same folder. During run time, a *parameter* file including the relevant values for the elliptic_guide component is read.   


- The McStas instrument files can of course be editted if needed to adjust type and characteristics of neutron lens, number and position of PSD components, etc.

```python
COMPONENT elliptic_lens1 = Elliptic_guide_gravity(
                           l = lens_length, majorAxisxw = a_maj, minorAxisxw = b_min, majorAxisyh = a_maj, minorAxisyh = b_min, 
                           majorAxisoffsetxw = offset, majorAxisoffsetyh = offset,
                           R0 = 0.99, Qc = 0.0219, alphatop = 6.07, alphabottom = 6.07,alpharight = 6.07,alphaleft = 6.07,
                           mright = mLR, mleft = mLR, mtop = mTB, mbottom = mTB, W = 0.003)
```

---
### Setting up runs
+ Step 1 : choose type of simulation to set up: related to a) BOA, b) DMC, c) generic set-up
+ Step 2 : edit (if needed) relevant _runs_prepare.py_ file (included in same folder as instrument file). Run the file to generate submission scripts for the simulations:

                           $ python runs_prepare
+ Step 3 : submit run scripts  generated in previous step by running (after editing, if needed)  _runs_submit.py_ file (also included in same folder as intrument file):

                           $ python runs_submit
