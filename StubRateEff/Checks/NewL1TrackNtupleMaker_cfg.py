############################################################
# define basic process
############################################################
import FWCore.ParameterSet.Config as cms
import FWCore.Utilities.FileUtils as FileUtils
import FWCore.ParameterSet.VarParsing as opts
import os
import sys

options = opts.VarParsing ("analysis")
options.register("Geometry",                 "D",                 opts.VarParsing.multiplicity.singleton,                 opts.VarParsing.varType.string,                 "Geometry used")
options.register("SW",                 "0p5",                 opts.VarParsing.multiplicity.singleton,                 opts.VarParsing.varType.string,                 "window size")
#--- Specify L1 Tracking algo to be used
options.register("L1Algo", 'HYBRID', opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.string, "L1 Tracking algo used")

#--- Specify stub window to be used
options.register("StubWindow", '', opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.string, "Stub window to be used")

#--- Specify the track nTuple process
options.register('Process', 1, opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.int,"Track nTuple process")

#--- Specify whether DTC truncation occurs
options.register('Truncation', True, opts.VarParsing.multiplicity.singleton, opts.VarParsing.varType.bool, "DTC Truncation enabled/disabled")
options.parseArguments()

process = cms.Process("L1TrackNtuple")


############################################################
# edit options here
############################################################

GEOMETRY = options.Geometry
L1TRKALGO = 'HYBRID'  # L1 tracking algorithm: 'HYBRID' (baseline, 4par fit) or 'HYBRID_DISPLACED' (extended, 5par fit)

WRITE_DATA = False

############################################################
# import standard configurations
############################################################

process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.categories.append('Tracklet')
process.MessageLogger.categories.append('L1track')
process.MessageLogger.Tracklet = cms.untracked.PSet(limit = cms.untracked.int32(-1))

if GEOMETRY == "D49": 
    print "using geometry " + GEOMETRY + " (tilted)"
    process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')
    process.load('Configuration.Geometry.GeometryExtended2026D49_cff')
else:
    print "this is not a valid geometry!!!"

process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')


############################################################
# input and output
############################################################

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(2))

# Get list of MC datasets from repo, or specify yourself.

def getTxtFile(txtFileName): 
  return FileUtils.loadListFromFile(os.environ['CMSSW_BASE']+'/src/'+txtFileName)

#if GEOMETRY == "D49":
##    inputMC = ["/store/relval/CMSSW_11_1_0_pre2/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v2_2026D49PU200-v1/20000/F7BF4AED-51F1-9D47-B86D-6C3DDA134AB9.root"]
##    inputMC = ["/store/relval/CMSSW_11_1_0_pre2/RelValSingleEFlatPt1p5To8/GEN-SIM-DIGI-RAW/110X_mcRun4_realistic_v2_HS_2026D49noPU-v1/10000/EAA6F3E0-9D75-2449-AFC6-74A4928ADE2E.root"]    
#    inputMC = getTxtFile('L1Trigger/TrackFindingTracklet/test/MCsamples/1110/RelVal/SingleElPt1p5to8/PU0.txt')
#else:
#    print "this is not a valid geometry!!!"
    
#process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(*inputMC))
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring("/store/relval/CMSSW_11_2_0_pre5/RelValTTbar_14TeV/GEN-SIM-DIGI-RAW/PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1/20000/41CBFD85-E4CA-3A4B-B7E7-4F292205D1B9.root"))

process.TFileService = cms.Service("TFileService", fileName = cms.string('outfile.root'), closeFileFast = cms.untracked.bool(True))
process.Timing = cms.Service("Timing", summaryOnly = cms.untracked.bool(True))


############################################################
# L1 tracking: remake stubs?
############################################################

process.load('L1Trigger.TrackTrigger.TrackTrigger_cff')
from L1Trigger.TrackTrigger.TTStubAlgorithmRegister_cfi import *
process.load("SimTracker.TrackTriggerAssociation.TrackTriggerAssociator_cff")

from SimTracker.TrackTriggerAssociation.TTClusterAssociation_cfi import *
TTClusterAssociatorFromPixelDigis.digiSimLinks = cms.InputTag("simSiPixelDigis","Tracker")

process.TTClusterStub = cms.Path(process.TrackTriggerClustersStubs)
process.TTClusterStubTruth = cms.Path(process.TrackTriggerAssociatorClustersStubs) 

############################################################
# L1 tracking
############################################################

process.load("L1Trigger.TrackFindingTracklet.L1HybridEmulationTracks_cff")

# HYBRID: prompt tracking
if (L1TRKALGO == 'HYBRID'):
    process.TTTracksEmulation = cms.Path(process.L1HybridTracks)
    process.TTTracksEmulationWithTruth = cms.Path(process.L1HybridTracksWithAssociators)
    NHELIXPAR = 4
    L1TRK_NAME  = "TTTracksFromTrackletEmulation"
    L1TRK_LABEL = "Level1TTTracks"
    L1TRUTH_NAME = "TTTrackAssociatorFromPixelDigis"

# HYBRID: extended tracking
elif (L1TRKALGO == 'HYBRID_DISPLACED'):
    process.TTTracksEmulation = cms.Path(process.L1ExtendedHybridTracks)
    process.TTTracksEmulationWithTruth = cms.Path(process.L1ExtendedHybridTracksWithAssociators)
    NHELIXPAR = 5
    L1TRK_NAME  = "TTTracksFromExtendedTrackletEmulation"
    L1TRK_LABEL = "Level1TTTracks"
    L1TRUTH_NAME = "TTTrackAssociatorFromPixelDigisExtended"
    
# LEGACY ALGORITHM (EXPERTS ONLY): TRACKLET  
elif (L1TRKALGO == 'TRACKLET'):
    print "\n WARNING - this is not a recommended algorithm! Please use HYBRID (HYBRID_DISPLACED)!"
    print "\n To run the tracklet-only algorithm, please ensure you have commented out #define USEHYBRID in interface/Settings.h + recompiled! \n"
    process.TTTracksEmulation = cms.Path(process.L1HybridTracks)
    process.TTTracksEmulationWithTruth = cms.Path(process.L1HybridTracksWithAssociators)
    NHELIXPAR = 4
    L1TRK_NAME  = "TTTracksFromTrackletEmulation"
    L1TRK_LABEL = "Level1TTTracks"
    L1TRUTH_NAME = "TTTrackAssociatorFromPixelDigis"

# LEGACY ALGORITHM (EXPERTS ONLY): TMTT  
elif (L1TRKALGO == 'TMTT'):
    print "\n WARNING - this is not a recommended algorithm! Please use HYBRID (HYBRID_DISPLACED)! \n"
    process.load("L1Trigger.TrackFindingTMTT.TMTrackProducer_Ultimate_cff")
    L1TRK_PROC  =  process.TMTrackProducer    
    L1TRK_NAME  = "TMTrackProducer"
    L1TRK_LABEL = "TML1TracksKF4ParamsComb"
    L1TRUTH_NAME = "TTTrackAssociatorFromPixelDigis"
    NHELIXPAR = 4
    L1TRK_PROC.EnableMCtruth = cms.bool(False) # Reduce CPU use by disabling internal histos.
    L1TRK_PROC.EnableHistos  = cms.bool(False)
    process.load("RecoVertex.BeamSpotProducer.BeamSpot_cfi")
    process.load("SimTracker.TrackTriggerAssociation.TrackTriggerAssociator_cff")
    process.TTTrackAssociatorFromPixelDigis.TTTracks = cms.VInputTag( cms.InputTag(L1TRK_NAME, L1TRK_LABEL) )
    process.TTTracksEmulation = cms.Path(process.offlineBeamSpot*L1TRK_PROC)
    process.TTTracksEmulationWithTruth = cms.Path(process.offlineBeamSpot*L1TRK_PROC*process.TrackTriggerAssociatorTracks)

else:
    print "ERROR: Unknown L1TRKALGO option"
    exit(1)

############################################################
# Define the track ntuple process, MyProcess is the (unsigned) PDGID corresponding to the process which is run
# e.g. single electron/positron = 11
#      single pion+/pion- = 211
#      single muon+/muon- = 13 
#      pions in jets = 6
#      taus = 15
#      all TPs = 1
############################################################

process.L1TrackNtuple = cms.EDAnalyzer('L1TrackNtupleMaker',
                                       MyProcess = cms.int32(1),
                                       DebugMode = cms.bool(False),      # printout lots of debug statements
                                       SaveAllTracks = cms.bool(False),   # save *all* L1 tracks, not just truth matched to primary particle
                                       SaveStubs = cms.bool(True),      # save some info for *all* stubs
                                       L1Tk_nPar = cms.int32(NHELIXPAR), # use 4 or 5-parameter L1 tracking?
                                       L1Tk_minNStub = cms.int32(4),     # L1 tracks with >= 4 stubs
                                       TP_minNStub = cms.int32(4),       # require TP to have >= X number of stubs associated with it
                                       TP_minNStubLayer = cms.int32(4),  # require TP to have stubs in >= X layers/disks
                                       TP_minPt = cms.double(2.0),       # only save TPs with pt > X GeV
                                       TP_maxEta = cms.double(2.5),      # only save TPs with |eta| < X
                                       TP_maxZ0 = cms.double(30.0),      # only save TPs with |z0| < X cm
                                       L1TrackInputTag = cms.InputTag(L1TRK_NAME, L1TRK_LABEL),         # TTTrack input
                                       MCTruthTrackInputTag = cms.InputTag(L1TRUTH_NAME, L1TRK_LABEL),  # MCTruth input 
                                       # other input collections
                                       L1StubInputTag = cms.InputTag("TTStubsFromPhase2TrackerDigis","StubAccepted"),
                                       L1StubRejectedInputTag = cms.InputTag("TTStubsFromPhase2TrackerDigis","StubRejected"),
                                       L1DTCStubRejectedInputTag = cms.InputTag("TTStubsFromDTCStubProducer","DTCStubRejected"),
#                                       L1DTCStubRejectedInputTag = cms.InputTag("TrackerDTCProducer", "StubLost"),
                                       MCTruthClusterInputTag = cms.InputTag("TTClusterAssociatorFromPixelDigis", "ClusterInclusive"),
                                       MCTruthStubInputTag = cms.InputTag("TTStubAssociatorFromPixelDigis", "StubAccepted"),
                                       TrackingParticleInputTag = cms.InputTag("mix", "MergedTrackTruth"),
                                       TrackingVertexInputTag = cms.InputTag("mix", "MergedTrackTruth"),
                                       # tracking in jets (--> requires AK4 genjet collection present!)
                                       TrackingInJets = cms.bool(False),
                                       GenJetInputTag = cms.InputTag("ak4GenJets", ""),
                                       )

if  options.SW=='0p5':
    process.TTStubAlgorithm_official_Phase2TrackerDigi_ = cms.ESProducer("TTStubAlgorithm_official_Phase2TrackerDigi_",       zMatchingPS  = cms.bool(True),       zMatching2S  = cms.bool(True),       NTiltedRings = cms.vdouble( 0., 12., 12., 12., 0., 0., 0.),       BarrelCut    = cms.vdouble( 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5),       TiltedBarrelCutSet = cms.VPSet(         cms.PSet( TiltedCut = cms.vdouble( 0 ) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5) ),         ),         EndcapCutSet = cms.VPSet(         cms.PSet( EndcapCut = cms.vdouble( 0 ) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5) ),         )    )
if  options.SW=='1p0':
    process.TTStubAlgorithm_official_Phase2TrackerDigi_ = cms.ESProducer("TTStubAlgorithm_official_Phase2TrackerDigi_",       zMatchingPS  = cms.bool(True),       zMatching2S  = cms.bool(True),       NTiltedRings = cms.vdouble( 0., 12., 12., 12., 0., 0., 0.),       BarrelCut    = cms.vdouble( 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),       TiltedBarrelCutSet = cms.VPSet(         cms.PSet( TiltedCut = cms.vdouble( 0 ) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0) ),         ),         EndcapCutSet = cms.VPSet(         cms.PSet( EndcapCut = cms.vdouble( 0 ) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0) ),         )    )
if  options.SW=='1p5':
    process.TTStubAlgorithm_official_Phase2TrackerDigi_ = cms.ESProducer("TTStubAlgorithm_official_Phase2TrackerDigi_",       zMatchingPS  = cms.bool(True),       zMatching2S  = cms.bool(True),       NTiltedRings = cms.vdouble( 0., 12., 12., 12., 0., 0., 0.),       BarrelCut    = cms.vdouble( 0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5),       TiltedBarrelCutSet = cms.VPSet(         cms.PSet( TiltedCut = cms.vdouble( 0 ) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5) ),         ),         EndcapCutSet = cms.VPSet(         cms.PSet( EndcapCut = cms.vdouble( 0 ) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5) ),         )    )
if  options.SW=='2p0':
    process.TTStubAlgorithm_official_Phase2TrackerDigi_ = cms.ESProducer("TTStubAlgorithm_official_Phase2TrackerDigi_",       zMatchingPS  = cms.bool(True),       zMatching2S  = cms.bool(True),       NTiltedRings = cms.vdouble( 0., 12., 12., 12., 0., 0., 0.),       BarrelCut    = cms.vdouble( 0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0),       TiltedBarrelCutSet = cms.VPSet(         cms.PSet( TiltedCut = cms.vdouble( 0 ) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0) ),         ),         EndcapCutSet = cms.VPSet(         cms.PSet( EndcapCut = cms.vdouble( 0 ) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0) ),         )    )
if  options.SW=='2p5':
    process.TTStubAlgorithm_official_Phase2TrackerDigi_ = cms.ESProducer("TTStubAlgorithm_official_Phase2TrackerDigi_",       zMatchingPS  = cms.bool(True),       zMatching2S  = cms.bool(True),       NTiltedRings = cms.vdouble( 0., 12., 12., 12., 0., 0., 0.),       BarrelCut    = cms.vdouble( 0, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5),       TiltedBarrelCutSet = cms.VPSet(         cms.PSet( TiltedCut = cms.vdouble( 0 ) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5) ),         ),         EndcapCutSet = cms.VPSet(         cms.PSet( EndcapCut = cms.vdouble( 0 ) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5) ),         )    )
if  options.SW=='3p0':
    process.TTStubAlgorithm_official_Phase2TrackerDigi_ = cms.ESProducer("TTStubAlgorithm_official_Phase2TrackerDigi_",       zMatchingPS  = cms.bool(True),       zMatching2S  = cms.bool(True),       NTiltedRings = cms.vdouble( 0., 12., 12., 12., 0., 0., 0.),       BarrelCut    = cms.vdouble( 0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0),       TiltedBarrelCutSet = cms.VPSet(         cms.PSet( TiltedCut = cms.vdouble( 0 ) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0) ),         ),         EndcapCutSet = cms.VPSet(         cms.PSet( EndcapCut = cms.vdouble( 0 ) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0, 3.0) ),         )    )
if  options.SW=='3p5':
    process.TTStubAlgorithm_official_Phase2TrackerDigi_ = cms.ESProducer("TTStubAlgorithm_official_Phase2TrackerDigi_",       zMatchingPS  = cms.bool(True),       zMatching2S  = cms.bool(True),       NTiltedRings = cms.vdouble( 0., 12., 12., 12., 0., 0., 0.),       BarrelCut    = cms.vdouble( 0, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5),       TiltedBarrelCutSet = cms.VPSet(         cms.PSet( TiltedCut = cms.vdouble( 0 ) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5) ),         ),         EndcapCutSet = cms.VPSet(         cms.PSet( EndcapCut = cms.vdouble( 0 ) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5) ),         )    )
if  options.SW=='4p0':
    process.TTStubAlgorithm_official_Phase2TrackerDigi_ = cms.ESProducer("TTStubAlgorithm_official_Phase2TrackerDigi_",       zMatchingPS  = cms.bool(True),       zMatching2S  = cms.bool(True),       NTiltedRings = cms.vdouble( 0., 12., 12., 12., 0., 0., 0.),       BarrelCut    = cms.vdouble( 0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0),       TiltedBarrelCutSet = cms.VPSet(         cms.PSet( TiltedCut = cms.vdouble( 0 ) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0) ),         ),         EndcapCutSet = cms.VPSet(         cms.PSet( EndcapCut = cms.vdouble( 0 ) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0) ),         )    )
if  options.SW=='4p5':
    process.TTStubAlgorithm_official_Phase2TrackerDigi_ = cms.ESProducer("TTStubAlgorithm_official_Phase2TrackerDigi_",       zMatchingPS  = cms.bool(True),       zMatching2S  = cms.bool(True),       NTiltedRings = cms.vdouble( 0., 12., 12., 12., 0., 0., 0.),       BarrelCut    = cms.vdouble( 0, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5),       TiltedBarrelCutSet = cms.VPSet(         cms.PSet( TiltedCut = cms.vdouble( 0 ) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5) ),         ),         EndcapCutSet = cms.VPSet(         cms.PSet( EndcapCut = cms.vdouble( 0 ) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5, 4.5) ),         )    )
if  options.SW=='5p0':
    process.TTStubAlgorithm_official_Phase2TrackerDigi_ = cms.ESProducer("TTStubAlgorithm_official_Phase2TrackerDigi_",       zMatchingPS  = cms.bool(True),       zMatching2S  = cms.bool(True),       NTiltedRings = cms.vdouble( 0., 12., 12., 12., 0., 0., 0.),       BarrelCut    = cms.vdouble( 0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0),       TiltedBarrelCutSet = cms.VPSet(         cms.PSet( TiltedCut = cms.vdouble( 0 ) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0) ),         ),         EndcapCutSet = cms.VPSet(         cms.PSet( EndcapCut = cms.vdouble( 0 ) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0, 5.0) ),         )    )
if  options.SW=='5p5':
    process.TTStubAlgorithm_official_Phase2TrackerDigi_ = cms.ESProducer("TTStubAlgorithm_official_Phase2TrackerDigi_",       zMatchingPS  = cms.bool(True),       zMatching2S  = cms.bool(True),       NTiltedRings = cms.vdouble( 0., 12., 12., 12., 0., 0., 0.),       BarrelCut    = cms.vdouble( 0, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5),       TiltedBarrelCutSet = cms.VPSet(         cms.PSet( TiltedCut = cms.vdouble( 0 ) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5) ),         ),         EndcapCutSet = cms.VPSet(         cms.PSet( EndcapCut = cms.vdouble( 0 ) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5, 5.5) ),         )    )
if  options.SW=='6p0':
    process.TTStubAlgorithm_official_Phase2TrackerDigi_ = cms.ESProducer("TTStubAlgorithm_official_Phase2TrackerDigi_",       zMatchingPS  = cms.bool(True),       zMatching2S  = cms.bool(True),       NTiltedRings = cms.vdouble( 0., 12., 12., 12., 0., 0., 0.),       BarrelCut    = cms.vdouble( 0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0),       TiltedBarrelCutSet = cms.VPSet(         cms.PSet( TiltedCut = cms.vdouble( 0 ) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0) ),         ),         EndcapCutSet = cms.VPSet(         cms.PSet( EndcapCut = cms.vdouble( 0 ) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0) ),         )    )
if  options.SW=='6p5':
    process.TTStubAlgorithm_official_Phase2TrackerDigi_ = cms.ESProducer("TTStubAlgorithm_official_Phase2TrackerDigi_",       zMatchingPS  = cms.bool(True),       zMatching2S  = cms.bool(True),       NTiltedRings = cms.vdouble( 0., 12., 12., 12., 0., 0., 0.),       BarrelCut    = cms.vdouble( 0, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5),       TiltedBarrelCutSet = cms.VPSet(         cms.PSet( TiltedCut = cms.vdouble( 0 ) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5) ),         ),         EndcapCutSet = cms.VPSet(         cms.PSet( EndcapCut = cms.vdouble( 0 ) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5) ),         )    )
if  options.SW=='7p0':
    process.TTStubAlgorithm_official_Phase2TrackerDigi_ = cms.ESProducer("TTStubAlgorithm_official_Phase2TrackerDigi_",       zMatchingPS  = cms.bool(True),       zMatching2S  = cms.bool(True),       NTiltedRings = cms.vdouble( 0., 12., 12., 12., 0., 0., 0.),       BarrelCut    = cms.vdouble( 0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0),       TiltedBarrelCutSet = cms.VPSet(         cms.PSet( TiltedCut = cms.vdouble( 0 ) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0) ),         cms.PSet( TiltedCut = cms.vdouble( 0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0) ),         ),         EndcapCutSet = cms.VPSet(         cms.PSet( EndcapCut = cms.vdouble( 0 ) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0) ),         cms.PSet( EndcapCut = cms.vdouble( 0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0) ),         )    )


############################################################
# L1 tracking: run DTC emulation
############################################################

# load code that produces DTCStubs
process.load( 'L1Trigger.TrackerDTC.ProducerED_cff' )

process.TrackTriggerSetup.ProcessHistory.TTStubAlgorithm = cms.string( "TTStubAlgorithm_official_Phase2TrackerDigi_" )

process.TrackerDTCProducer.InputTag          = cms.InputTag( "TTStubsFromPhase2TrackerDigis", "StubAccepted", "L1TrackNtuple" )
process.TrackerDTCProducer.BranchAccepted    = cms.string ( "StubAccepted" )
process.TrackerDTCProducer.BranchLost        = cms.string ( "StubLost" )
process.TrackerDTCProducer.EnableTruncation  = cms.bool ( options.Truncation )
#process.TrackerDTCProducer.CheckHistory     = cms.bool    ( True)

if ( L1TRKALGO == 'TMTT' ) : process.TrackerDTCProducer.UseHybrid = cms.bool ( False )
else : process.TrackerDTCProducer.UseHybrid = cms.bool ( True )
process.TrackTriggerSetup.TMTT.MinPt         = cms.double ( 2.0 )
process.TrackTriggerSetup.Hybrid.MinPt       = cms.double ( 2.0 )
#process.TrackerDTCProducer.CheckHistory     = cms.bool ( True ) # Default is false for some reason ...

#if (STUBWINDOW == 'OLD_LOOSE'): process.TrackTriggerSetup.FrontEnd.BendCut = cms.double( 1.9385 )  # used stub bend uncertainty in pitch units ## 1.3125
#if (STUBWINDOW == 'OLD_LOOSE'): process.TrackTriggerSetup.FrontEnd.BendCut = cms.double( 5.1 )  # used stub bend uncertainty in pitch units ## 1.3125
process.TrackTriggerSetup.FrontEnd.BendCut = cms.double( 5.1 )  

process.produceDTCStubs = cms.Path( process.TrackerDTCProducer )

# load code that converts DTCStubs into TTStubsO
process.load( 'L1Trigger.TrackFindingTracklet.TTStubsFromDTCStubProducer_cff' )
process.TTStubsFromDTCStubProducer.TTDTCStubsAcceptedTag  = cms.InputTag( "TrackerDTCProducer", "StubAccepted" )
process.TTStubsFromDTCStubProducer.TTDTCStubsRejectedTag  = cms.InputTag( "TrackerDTCProducer", "StubLost" )

process.TTStubsFromDTCStubProducer.BranchStubAccepted     = cms.string  ( "DTCStubAccepted" )
process.TTStubsFromDTCStubProducer.BranchStubRejected     = cms.string  ( "DTCStubRejected" )

process.convertDTCStubs = cms.Path( process.TTStubsFromDTCStubProducer )


process.ana = cms.Path(process.L1TrackNtuple)
#process.schedule = cms.Schedule(process.TTClusterStub,process.TTClusterStubTruth,process.TTTracksEmulationWithTruth,process.ana)
process.schedule = cms.Schedule(process.TTClusterStub, process.TTClusterStubTruth, process.produceDTCStubs, process.convertDTCStubs, process.ana)
#process.schedule = cms.Schedule(process.TTClusterStub,process.TTClusterStubTruth,process.TTTracksEmulationWithTruth,process.anaSW)
# use this if cluster/stub associators not available 
# process.schedule = cms.Schedule(process.TTClusterStubTruth,process.TTTracksEmulationWithTruth,process.ana)

# use this to only run tracking + track associator
#process.schedule = cms.Schedule(process.TTTracksEmulationWithTruth,process.ana)


############################################################
# write output dataset?
############################################################

if (WRITE_DATA):
  process.writeDataset = cms.OutputModule("PoolOutputModule",
      splitLevel = cms.untracked.int32(0),
      eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
      outputCommands = process.RAWSIMEventContent.outputCommands,
      fileName = cms.untracked.string('output_dataset.root'), ## ADAPT IT ##
      dataset = cms.untracked.PSet(
          filterName = cms.untracked.string(''),
          dataTier = cms.untracked.string('GEN-SIM')
      )
  )
  process.writeDataset.outputCommands.append('keep  *TTTrack*_*_*_*')
  process.writeDataset.outputCommands.append('keep  *TTStub*_*_*_*')

  process.pd = cms.EndPath(process.writeDataset)
  process.schedule.append(process.pd)
process.out = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string("EDMiii.root")
    )

process.outpath = cms.EndPath(process.out)
#process.schedule.append(process.outpath)
