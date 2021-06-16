import sys
import os
import subprocess
import readline
import string
import glob

sys.path.append('/afs/crc.nd.edu/user/r/rgoldouz/ExcitedTopAnalysis/analysis/bin')
import Files_2017
#samples ={'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW2p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW2p0', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW6p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW6p5', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW6p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW6p0', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW2p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW2p5', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SWtight': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SWtight', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW3p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW3p0', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW3p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW3p5', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW7p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW7p0', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SWloose': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SWloose', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW4p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW4p5', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SWold': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SWold', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW4p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW4p0', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW0p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW0p5', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW5p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW5p5', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW1p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW1p0', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW1p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW1p5', '100000', 'pion'], 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW5p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW5p0', '100000', 'pion']}


samples ={'L1Stub_SingleElectron_D49_SW1p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW1p5', '100000', 'ele'], 'L1Stub_TTbar_D49_SW0p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW0p5', '9000', 'pion'], 'L1Stub_TTbar_D49_SWloose': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SWloose', '9000', 'pion'], 'L1Stub_SingleMu_D49_SW0p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW0p5', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SW1p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW1p0', '100000', 'ele'], 'L1Stub_SingleMu_D49_SW1p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW1p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SW1p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW1p5', '9000', 'pion'], 'L1Stub_SingleMu_D49_SW1p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW1p5', '100000', 'mu'], 'L1Stub_SingleMu_D49_SWold': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SWold', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SW3p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW3p5', '100000', 'ele'], 'L1Stub_TTbar_D49_SW2p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW2p5', '9000', 'pion'], 'L1Stub_SingleMu_D49_SW2p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW2p0', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SW5p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW5p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SW2p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW2p0', '9000', 'pion'], 'L1Stub_SingleElectron_D49_SW3p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW3p0', '100000', 'ele'], 'L1Stub_DisplacedMu_D49_SW5p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW5p5', '100000', 'mu'], 'L1Stub_SingleMu_D49_SW2p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW2p5', '100000', 'mu'], 'L1Stub_TTbar_D49_SW3p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW3p5', '9000', 'pion'], 'L1Stub_DisplacedMu_D49_SW4p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW4p0', '100000', 'mu'], 'L1Stub_SingleMu_D49_SW3p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW3p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SW3p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW3p0', '9000', 'pion'], 'L1Stub_SingleMu_D49_SW3p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW3p5', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SW4p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW4p5', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SW7p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW7p0', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SW0p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW0p5', '100000', 'ele'], 'L1Stub_DisplacedMu_D49_SW6p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW6p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SWtight': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SWtight', '9000', 'pion'], 'L1Stub_DisplacedMu_D49_SW6p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW6p5', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SW4p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW4p0', '100000', 'ele'], 'L1Stub_SingleElectron_D49_SW2p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW2p0', '100000', 'ele'], 'L1Stub_SingleElectron_D49_SWloose': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SWloose', '100000', 'ele'], 'L1Stub_SingleElectron_D49_SW2p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW2p5', '100000', 'ele'], 'L1Stub_TTbar_D49_SWold': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SWold', '9000', 'pion'], 'L1Stub_DisplacedMu_D49_SWold': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SWold', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SW4p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW4p5', '100000', 'ele'], 'L1Stub_SingleElectron_D49_SWtight': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SWtight', '100000', 'ele'], 'L1Stub_DisplacedMu_D49_SW3p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW3p5', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SWold': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SWold', '100000', 'ele'], 'L1Stub_SingleElectron_D49_SW5p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW5p0', '100000', 'ele'], 'L1Stub_DisplacedMu_D49_SWtight': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SWtight', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SW3p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW3p0', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SW5p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW5p5', '100000', 'ele'], 'L1Stub_DisplacedMu_D49_SW2p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW2p5', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SW2p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW2p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SW4p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW4p0', '9000', 'pion'], 'L1Stub_TTbar_D49_SW6p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW6p0', '9000', 'pion'], 'L1Stub_SingleElectron_D49_SW7p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW7p0', '100000', 'ele'], 'L1Stub_DisplacedMu_D49_SW1p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW1p5', '100000', 'mu'], 'L1Stub_SingleMu_D49_SW6p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW6p5', '100000', 'mu'], 'L1Stub_TTbar_D49_SW6p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW6p5', '9000', 'pion'], 'L1Stub_SingleMu_D49_SW6p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW6p0', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SW1p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW1p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SW7p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW7p0', '9000', 'pion'], 'L1Stub_SingleMu_D49_SWtight': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SWtight', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SW0p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW0p5', '100000', 'mu'], 'L1Stub_SingleMu_D49_SWloose': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SWloose', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SW6p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW6p5', '100000', 'ele'], 'L1Stub_SingleMu_D49_SW7p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW7p0', '100000', 'mu'], 'L1Stub_SingleMu_D49_SW4p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW4p5', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SWloose': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SWloose', '100000', 'mu'], 'L1Stub_SingleMu_D49_SW4p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW4p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SW4p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW4p5', '9000', 'pion'], 'L1Stub_SingleMu_D49_SW5p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW5p5', '100000', 'mu'], 'L1Stub_TTbar_D49_SW5p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW5p0', '9000', 'pion'], 'L1Stub_SingleMu_D49_SW5p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW5p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SW5p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW5p5', '9000', 'pion'], 'L1Stub_TTbar_D49_SW1p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW1p0', '9000', 'pion'], 'L1Stub_SingleElectron_D49_SW6p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW6p0', '100000', 'ele']}

#os.system('rm *.root')
dist = '/hadoop/store/user/rgoldouz/FullProduction/L1Analysis/FE_L1Analysis_'
for key, value in samples.items():
#    if 'DisplacedMu' not in key:
#        continue
#    print key
#    os.system('cp ' + glob.glob("/hadoop/store/user/rgoldouz/FullProduction/L1Analysis/FE_L1Analysis_"  + key + '/*.root')[0] + ' ' + key + '.root')
    hadd='hadd ' + key + '.root '
    for filename in os.listdir(dist + key):
        hadd += dist + key + '/' + filename + ' '
    os.system('rm ' + key + '.root')
    os.system(hadd)
#os.system('cp ' + glob.glob("/hadoop/store/user/rgoldouz/FullProduction/L1Analysis/FE_L1Analysis_Tt_Pu200_110D49/*.root")[0] + ' FE_' +'Tt_Pu200_110D49.root')
