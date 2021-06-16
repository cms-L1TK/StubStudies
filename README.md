
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

## Codes
In order to run the code, you need to start with the official L1 tracking emulation code,
[link](https://twiki.cern.ch/twiki/bin/viewauth/CMS/L1TrackSoftware#Hybrid_L1_tracking_emulation_in)

```
cmsrel CMSSW_11_3_0_pre3
cd CMSSW_11_3_0_pre3/src/
cmsenv 
git cms-checkout-topic -u cms-L1TK:L1TK-dev-11_3_0_pre3
git cms-addpkg L1Trigger/TrackTrigger
scram b -j 8
```
Then somewhere else clone the code for stub window tuning
```
git clone git@github.com:cms-L1TK/StubStudies.git
```

Replace the official ' L1TrackNtupleMaker.cc ' and ' L1TrackNtupleMaker_cfg.py ' files in 'CMSSW_11_3_0_pre3/src/L1Trigger/TrackFindingTracklet/test/' directory with the files in 'StubStudies/StubRateEff/python'. After compiling, you should be able to run the Ntuple producer config file and produce needed variables for the next step. 
```
cmsRun L1TrackNtupleMaker_cfg.py Geometry=D49 SW=7p0
```
You need to set the geometry (D49 or D76) which is used in sample production and the stub window size (tight, loose, 0p5,1p0, 1p5, ... or 7p0). Samples can be found in [link](https://twiki.cern.ch/twiki/bin/view/CMS/L1TrackMC#CMSSW_11_3_0).

After running on the ttbar, single electron, single muon and displaced muon samples and making ntuples, you should use them as an input to the next step.
After setting cms enviroment,
```
cd StubStudies/StubRateEff
make clean
make
```
after modifing the 'src/main.C' file for the input ntuple, output file name and the name of related particle for finding the efficiency ('pion' for ttbar sample, 'ele' for single electron sample and 'mu' for singlle muon and displaced muon samples), you can run the code for making histograms.
```
./bin/RunAll
```

Last step is making final histograms using the following code
```
python plot/SW_Tunning_v2.py
```

Then you should have reproduced plots in [link](https://rgoldouz.web.cern.ch/rgoldouz/MyPlots/L1tracker/16June2021/plot_SW_AllW/)


