
Repository for various tools and scripts for performance studies of L1 stub performance

# Stub window tuning

## Variables
In order to determine the optimum stub window size in each module, we need to know the following variables as a function of window size.

- Stub rate: total number of stubs which is found from a ttbar sample with pileup 200.
- CBC fail: total number of stubs that are failed because of the CBC capacity which is found from a ttbar sample with pileup 200.
- CIC fail:  total number of stubs that are failed because of the CBC capacity which is found from a ttbar sample with pileup 200.
- DTC fail:  total number of stubs that are failed because of the DTC capacity which is found from a ttbar sample with pileup 200.
- muon efficiency: effeciency for reconstructing stubs from the clusters that are matched to a muon tracking particle.
- Electron efficiency: effeciency for reconstructing stubs from the clusters that are matched to a electron tracking particle.
- Displaced muon efficiency: effeciency for reconstructing stubs from the clusters that are matched to a displaced muon tracking particle.

Our goal is to find a window size which has the highest efficiency and the lowest fail rate.

## Variables
In order to run the code, you need to start with the official L1 tracking emulation code,
[link](https://twiki.cern.ch/twiki/bin/viewauth/CMS/L1TrackSoftware#Hybrid_L1_tracking_emulation_in)

```
cmsrel CMSSW_11_3_0_pre3
cd CMSSW_11_3_0_pre3/src/
cmsenv 
git cms-checkout-topic -u cms-L1TK:L1TK-dev-11_3_0_pre3
```


