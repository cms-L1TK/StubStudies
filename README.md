# Repository for various tools and scripts for performance studies of L1 stub performance
Author: Reza Goldouzian 
## References
Details of this study is summarised in the following analysis note: 
  CMS DN-2020/005: `The L1 Track Trigger Upgrade: Properties, Efficiencies, and Rates for Track Stubs`
## Introduction
we study various features of stubs for the CMS experiment phase II track trigger upgrade including stub rates, stub construction efficiency, stub transmission efficiency, etc. Consequently, new stub window tunes are proposed for having high stub construction efficiencies with the lowest possible rates.
## Extracted data
In order to run these codes one needs to extract data first. In order to do that we use the official L1 track Ntuple maker (https://twiki.cern.ch/twiki/bin/viewauth/CMS/L1TrackSoftware#Hybrid_L1_tracking_emulation_in). We need more variables to do our studies. So you should replace the code in `L1Trigger/TrackFindingTracklet/test/L1TrackNtupleMaker.cc` with the file in this repository `StubStudies/StubRateEff/python/L1TrackNtupleMaker.cc` and recompile the code. We need also to update for some input tags in the `L1Trigger/TrackFindingTracklet/test/L1TrackNtupleMaker_cfg.py` code. So you can use the code in `StubStudies/StubRateEff/python/L1TrackNtupleMaker_cfg.py` instead. In the `L1TrackNtupleMaker_cfg.py`, we have an input parameter called `SW` which determine which stub Window should be used for stub reconstruction. There are two different choices:
- Fixed window size for all detector sub regions: `0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, and 7.0`
- Available tunes: `newTight, newLoose, tight, loose`
```
cmsRun L1TrackNtupleMaker_cfg.py Geometry=D49 SW=7p0
```
## Samples
Our studies are done with the following samples processed with `CMSSW_11_3_0_pre3` and geometry `D76`. Input samples are:
- TTbar: /RelValTTbar_14TeV/CMSSW_11_3_0_pre6-PU_113X_mcRun4_realistic_v6_2026D76PU200-v1/GEN-SIM-DIGI-RAW
- SingleElectron: /RelValSingleElectronFlatPt1p5To8/CMSSW_11_3_0_pre6-113X_mcRun4_realistic_v6_2026D76noPU-v1/GEN-SIM-DIGI-RAW
- SingleMu: /RelValSingleMuFlatPt1p5To8/CMSSW_11_3_0_pre6-113X_mcRun4_realistic_v6_2026D76noPU_rsb-v1/GEN-SIM-DIGI-RAW
- DisplacedMu: /RelValDisplacedMuPt1p5To8Dxy100/CMSSW_11_3_0_pre6-113X_mcRun4_realistic_v6_2026D76noPU-v1/GEN-SIM-DIGI-RAW
## Interested variables
- Stub rate: total number of stubs which is found from a ttbar sample with pileup 200.
- CBC fail: total number of stubs that are failed because of the CBC capacity which is found from a ttbar sample with pileup 200.
- CIC fail:  total number of stubs that are failed because of the CBC capacity which is found from a ttbar sample with pileup 200.
- muon efficiency: effeciency for reconstructing stubs from the clusters that are matched to a muon tracking particle.
- Electron efficiency: effeciency for reconstructing stubs from the clusters that are matched to a electron tracking particle.
- Displaced muon efficiency: effeciency for reconstructing stubs from the clusters that are matched to a displaced muon tracking particle.
## Running the code
One needs to run the codes in this repository to the made ntuples. To do so, first set the cms enviroment and then
```
git clone git@github.com:cms-L1TK/StubStudies.git
cd StubStudies/StubRateEff
make clean
make
```
after modifing the 'src/main.C' file for the input ntuple, output file name and the name of related particle for finding the efficiency ('pion' for ttbar sample, 'ele' for single electron sample and 'mu' for single muon and displaced muon samples), you can run the code for making histograms.
```
./bin/RunAll
```
The outputs of the above run can be used for drawing control plots
- plot/draw_plot_stubRate.py : for drawing the stub rate plots (see them in the DN)
- plot/draw_plot_stubeff.py : for drawing the stub efficiency plots (see them in the DN)

In order to make a new SW tune, the output of the code is needed for all the samples and all the window sizes. IF all samples are ready, just run the following code to get the new tune
- plot/SW_Tunning_cmsSet_NewEff.py 

