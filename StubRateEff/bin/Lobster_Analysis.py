import datetime
import os

from lobster import cmssw
from lobster.core import AdvancedOptions, Category, Config, MultiProductionDataset, StorageConfiguration, Workflow, Dataset,ParentDataset

samples = {}

cmsswbase = os.environ['CMSSW_BASE']
timestamp_tag = datetime.datetime.now().strftime('%Y%m%d_%H%M')

username = "rgoldouz"

production_tag = "L1Analysis"            # For 'full_production' setup

# Only run over lhe steps from specific processes/coeffs/runs
process_whitelist = []
coeff_whitelist   = []
runs_whitelist    = []  # (i.e. MG starting points)

master_label = '%s_%s' % (production_tag,timestamp_tag)

input_path   = "/store/user/"
output_path  = "/store/user/$USER/FullProduction/%s" % (production_tag)
workdir_path = "/tmpscratch/users/$USER/FullProduction/%s" % (production_tag)
plotdir_path = "~/www/lobster/FullProduction/%s" % (production_tag)


storage = StorageConfiguration(
    input=[
        "file:///hadoop" + input_path,  # Note the extra slash after the hostname!
        "root://deepthought.crc.nd.edu/" + input_path,  # Note the extra slash after the hostname!
    ],
    output=[
        "hdfs://eddie.crc.nd.edu:19000"  + output_path,
        "root://deepthought.crc.nd.edu/" + output_path, # Note the extra slash after the hostname!
        "gsiftp://T3_US_NotreDame"       + output_path,
        "srm://T3_US_NotreDame"          + output_path,
        "file:///hadoop"                 + output_path,
    ],
    disable_input_streaming=True,
)

#################################################################
# Worker Res.:
#   Cores:  12    | 4
#   Memory: 16000 | 8000
#   Disk:   13000 | 6500
#################################################################
gs_resources = Category(
    name='gs',
    cores=1,
    memory=1500,
    disk=2000
)
#################################################################
#samples["Tt_Pu200_110D49"]=[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/L1Stub_Tt_Pu200_110D49"],    "10000",    "pion"]
#samples["SingleMuFlatPt1p5To8_Pu200_110D49"]=[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/L1Stub_SingleMuFlatPt1p5To8_Pu200_110D49"],    "100000",    "mu"]
#samples["SingleMuFlatPt1p5To8_Pu0_110D49"]=[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["SingleEFlatPt1p5To8_Pu200_110D49"]=[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/L1Stub_SingleEFlatPt1p5To8_Pu200_110D49"],    "100000",    "ele"]
#samples["SingleEFlatPt1p5To8_Pu0_110D49"]=[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"],    "100000",    "ele"]
#samples["DisplacedMuPt1p5To8_Pu200_110D49"]=[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/L1Stub_DisplacedMuPt1p5To8_Pu200_110D49"],    "100000",    "mu"]
#samples["DisplacedMuPt1p5To8_Pu0_110D49"]=[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"],    "100000",    "mu"]


#samples["FE_TightTune_Tt_Pu200_110D49"]                    =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_TightTune_L1Stub_Tt_Pu200_110D49"],    "10000",    "pion"]
#samples["FE_TightTune_SingleMuFlatPt1p5To8_Pu200_110D49"]  =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_TightTune_L1Stub_SingleMuFlatPt1p5To8_Pu200_110D49"],    "100000",    "mu"]
#samples["FE_TightTune_SingleMuFlatPt1p5To8_Pu0_110D49"]    =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_TightTune_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_TightTune_SingleEFlatPt1p5To8_Pu200_110D49"]   =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_TightTune_L1Stub_SingleEFlatPt1p5To8_Pu200_110D49"],    "100000",    "ele"]
#samples["FE_TightTune_SingleEFlatPt1p5To8_Pu0_110D49"]     =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_TightTune_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"],    "100000",    "ele"]
#samples["FE_TightTune_DisplacedMuPt1p5To8_Pu200_110D49"]   =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_TightTune_L1Stub_DisplacedMuPt1p5To8_Pu200_110D49"],    "100000",    "mu"]
#samples["FE_TightTune_DisplacedMuPt1p5To8_Pu0_110D49"]     =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_TightTune_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#
#samples["FE_LooseTune_Tt_Pu200_110D49"]                    =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_LooseTune_L1Stub_Tt_Pu200_110D49"],    "10000",    "pion"]
#samples["FE_LooseTune_SingleMuFlatPt1p5To8_Pu200_110D49"]  =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_LooseTune_L1Stub_SingleMuFlatPt1p5To8_Pu200_110D49"],    "100000",    "mu"]
#samples["FE_LooseTune_SingleMuFlatPt1p5To8_Pu0_110D49"]    =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_LooseTune_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_LooseTune_SingleEFlatPt1p5To8_Pu200_110D49"]   =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_LooseTune_L1Stub_SingleEFlatPt1p5To8_Pu200_110D49"],    "100000",    "ele"]
#samples["FE_LooseTune_SingleEFlatPt1p5To8_Pu0_110D49"]     =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_LooseTune_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"],    "100000",    "ele"]
#samples["FE_LooseTune_DisplacedMuPt1p5To8_Pu200_110D49"]   =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_LooseTune_L1Stub_DisplacedMuPt1p5To8_Pu200_110D49"],    "100000",    "mu"]
#samples["FE_LooseTune_DisplacedMuPt1p5To8_Pu0_110D49"]     =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_LooseTune_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#
#
#samples["FE_OldTune_Tt_Pu200_110D49"]                    =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_OldTune_L1Stub_Tt_Pu200_110D49"],    "10000",    "pion"]
#samples["FE_OldTune_SingleMuFlatPt1p5To8_Pu200_110D49"]  =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_OldTune_L1Stub_SingleMuFlatPt1p5To8_Pu200_110D49"],    "100000",    "mu"]
#samples["FE_OldTune_SingleMuFlatPt1p5To8_Pu0_110D49"]    =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_OldTune_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_OldTune_SingleEFlatPt1p5To8_Pu200_110D49"]   =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_OldTune_L1Stub_SingleEFlatPt1p5To8_Pu200_110D49"],    "100000",    "ele"]
#samples["FE_OldTune_SingleEFlatPt1p5To8_Pu0_110D49"]     =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_OldTune_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"],    "100000",    "ele"]
#samples["FE_OldTune_DisplacedMuPt1p5To8_Pu200_110D49"]   =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_OldTune_L1Stub_DisplacedMuPt1p5To8_Pu200_110D49"],    "100000",    "mu"]
#samples["FE_OldTune_DisplacedMuPt1p5To8_Pu0_110D49"]     =[    ["rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_OldTune_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"],    "100000",    "mu"]

#samples["FE_SWtight_Tt_Pu200_110D49"]                    =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_TightTune_L1Stub_Tt_Pu200_110D49"],    "10000",    "pion"]
#samples["FE_SWtight_SingleMuFlatPt1p5To8_Pu0_110D49"]    =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_TightTune_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SWtight_SingleEFlatPt1p5To8_Pu0_110D49"]     =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_TightTune_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"],    "100000",    "ele"]

#samples["FE_SW0p5_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW0p5_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW0p5_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"]              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW0p5_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW0p5_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW0p5_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"],    "100000",    "ele"]
#samples["FE_SW0p5_L1Stub_Tt_Pu200_110D49"]                              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW0p5_L1Stub_Tt_Pu200_110D49"]               ,    "10000",    "pion"]
#
#samples["FE_SW1p0_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW1p0_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW1p0_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"]              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW1p0_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"],   "100000",    "mu"]
#samples["FE_SW1p0_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW1p0_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"],    "100000",    "ele"]
#samples["FE_SW1p0_L1Stub_Tt_Pu200_110D49"]                              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW1p0_L1Stub_Tt_Pu200_110D49"]               ,    "8000",    "pion"]
#
#samples["FE_SW1p5_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW1p5_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW1p5_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"]              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW1p5_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW1p5_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW1p5_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"],    "100000",    "ele"]
#samples["FE_SW1p5_L1Stub_Tt_Pu200_110D49"]                              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW1p5_L1Stub_Tt_Pu200_110D49"]               ,    "10000",    "pion"]
#
#samples["FE_SW2p0_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW2p0_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW2p0_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"]              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW2p0_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW2p0_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW2p0_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"],    "100000",    "ele"]
#samples["FE_SW2p0_L1Stub_Tt_Pu200_110D49"]                              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW2p0_L1Stub_Tt_Pu200_110D49"]               ,    "10000",    "pion"]
#
#samples["FE_SW2p5_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW2p5_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW2p5_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"]              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW2p5_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW2p5_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW2p5_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"],    "100000",    "ele"]
#samples["FE_SW2p5_L1Stub_Tt_Pu200_110D49"]                              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW2p5_L1Stub_Tt_Pu200_110D49"]               ,    "10000",    "pion"]
#
#samples["FE_SW3p0_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW3p0_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW3p0_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"]              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW3p0_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW3p0_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW3p0_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"],    "100000",    "ele"]
#samples["FE_SW3p0_L1Stub_Tt_Pu200_110D49"]                              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW3p0_L1Stub_Tt_Pu200_110D49"]               ,    "10000",    "pion"]
#
#samples["FE_SW4p0_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW4p0_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW4p0_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"]              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW4p0_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW4p0_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW4p0_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"],    "100000",    "ele"]
#samples["FE_SW4p0_L1Stub_Tt_Pu200_110D49"]                              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW4p0_L1Stub_Tt_Pu200_110D49"]               ,    "10000",    "pion"]
#
#samples["FE_SW5p0_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW5p0_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW5p0_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"]              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW5p0_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW5p0_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW5p0_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"],    "100000",    "ele"]
#samples["FE_SW5p0_L1Stub_Tt_Pu200_110D49"]                              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW5p0_L1Stub_Tt_Pu200_110D49"]               ,    "10000",    "pion"]
#
#samples["FE_SW6p0_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW6p0_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW6p0_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"]              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW6p0_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW6p0_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW6p0_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"],    "100000",    "ele"]
#samples["FE_SW6p0_L1Stub_Tt_Pu200_110D49"]                              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW6p0_L1Stub_Tt_Pu200_110D49"]               ,    "10000",    "pion"]
#
#samples["FE_SW7p0_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW7p0_L1Stub_DisplacedMuPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW7p0_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"]              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW7p0_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49"],    "100000",    "mu"]
#samples["FE_SW7p0_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"]               =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW7p0_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49"],    "100000",    "ele"]
#samples["FE_SW7p0_L1Stub_Tt_Pu200_110D49"]                              =[    ["rgoldouz/FullProduction/L1tracker_DAS_SW/FE_SW7p0_L1Stub_Tt_Pu200_110D49"]               ,    "10000",    "pion"]

#samples["L1Stub_Tt_Pu200_111pre2"]                              =[    ["rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_Tt_Pu200_111pre2"]               ,    "2500",    "pion"]
#samples["L1Stub_Tt_Pu200_112pre5_New"]                              =[    ["rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_Tt_Pu200_112pre5_New"]               ,    "9000",    "pion"]

#samples["TTbar_CMSSW_11_1_0_pre2_2026D49PU200"]                     =[    ["rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_CMSSW_11_1_0_pre2_2026D49PU200"]               ,    "2500",    "pion"]
#samples["SingleMuFlatPt1p5To8_CMSSW_11_1_0_pre2_2026D49noPU"]       =[    ["rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMuFlatPt1p5To8_CMSSW_11_1_0_pre2_2026D49noPU"]               ,    "100000",    "mu"]
#samples["SingleEFlatPt1p5To8_CMSSW_11_1_0_pre2_2026D49noPU"]        =[    ["rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleEFlatPt1p5To8_CMSSW_11_1_0_pre2_2026D49noPU"]               ,    "100000",    "ele"]
#samples["DisplacedMuPt1p5To8_CMSSW_11_1_0_pre2_2026D49noPU"]        =[    ["rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_1_0_pre2_2026D49noPU"]               ,    "100000",    "mu"]
#
#samples["TTbar_CMSSW_11_2_0_pre5_2026D49PU200"]                     =[    ["rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_CMSSW_11_2_0_pre5_2026D49PU200"]               ,    "9000",    "pion"]
#samples["SingleMuFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU"]      =[    ["rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMuFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU"]               ,    "100000",    "mu"]
#samples["SingleElectronFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU"]=[    ["rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectronFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU"]               ,    "100000",    "ele"]
##samples["DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU"]       =[    ["rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU"]               ,    "100000",    "mu"]
#
#samples["TTbar_RezaTune_CMSSW_11_2_0_pre5_2026D49PU200"]                     =[    ["rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_RezaTune_TTbar_CMSSW_11_2_0_pre5_2026D49PU200"]               ,    "1500",    "pion"]
#samples["RezaTune_SingleElectronFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU"]=[    ["rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_RezaTune_SingleElectronFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU"]               ,    "100000",    "ele"]
#samples["RezaTune_SingleMuFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU"]       =[    ["rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_RezaTune_SingleMuFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU"]               ,    "100000",    "mu"]
#
samples ={'L1Stub_SingleElectron_D49_SW1p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW1p5', '100000', 'ele'], 'L1Stub_TTbar_D49_SW0p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW0p5', '9000', 'pion'], 'L1Stub_TTbar_D49_SWloose': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SWloose', '9000', 'pion'], 'L1Stub_SingleMu_D49_SW0p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW0p5', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SW1p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW1p0', '100000', 'ele'], 'L1Stub_SingleMu_D49_SW1p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW1p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SW1p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW1p5', '9000', 'pion'], 'L1Stub_SingleMu_D49_SW1p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW1p5', '100000', 'mu'], 'L1Stub_SingleMu_D49_SWold': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SWold', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SW3p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW3p5', '100000', 'ele'], 'L1Stub_TTbar_D49_SW2p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW2p5', '9000', 'pion'], 'L1Stub_SingleMu_D49_SW2p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW2p0', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SW5p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW5p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SW2p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW2p0', '9000', 'pion'], 'L1Stub_SingleElectron_D49_SW3p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW3p0', '100000', 'ele'], 'L1Stub_DisplacedMu_D49_SW5p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW5p5', '100000', 'mu'], 'L1Stub_SingleMu_D49_SW2p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW2p5', '100000', 'mu'], 'L1Stub_TTbar_D49_SW3p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW3p5', '9000', 'pion'], 'L1Stub_DisplacedMu_D49_SW4p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW4p0', '100000', 'mu'], 'L1Stub_SingleMu_D49_SW3p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW3p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SW3p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW3p0', '9000', 'pion'], 'L1Stub_SingleMu_D49_SW3p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW3p5', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SW4p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW4p5', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SW7p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW7p0', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SW0p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW0p5', '100000', 'ele'], 'L1Stub_DisplacedMu_D49_SW6p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW6p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SWtight': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SWtight', '9000', 'pion'], 'L1Stub_DisplacedMu_D49_SW6p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW6p5', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SW4p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW4p0', '100000', 'ele'], 'L1Stub_SingleElectron_D49_SW2p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW2p0', '100000', 'ele'], 'L1Stub_SingleElectron_D49_SWloose': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SWloose', '100000', 'ele'], 'L1Stub_SingleElectron_D49_SW2p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW2p5', '100000', 'ele'], 'L1Stub_TTbar_D49_SWold': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SWold', '9000', 'pion'], 'L1Stub_DisplacedMu_D49_SWold': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SWold', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SW4p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW4p5', '100000', 'ele'], 'L1Stub_SingleElectron_D49_SWtight': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SWtight', '100000', 'ele'], 'L1Stub_DisplacedMu_D49_SW3p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW3p5', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SWold': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SWold', '100000', 'ele'], 'L1Stub_SingleElectron_D49_SW5p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW5p0', '100000', 'ele'], 'L1Stub_DisplacedMu_D49_SWtight': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SWtight', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SW3p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW3p0', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SW5p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW5p5', '100000', 'ele'], 'L1Stub_DisplacedMu_D49_SW2p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW2p5', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SW2p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW2p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SW4p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW4p0', '9000', 'pion'], 'L1Stub_TTbar_D49_SW6p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW6p0', '9000', 'pion'], 'L1Stub_SingleElectron_D49_SW7p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW7p0', '100000', 'ele'], 'L1Stub_DisplacedMu_D49_SW1p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW1p5', '100000', 'mu'], 'L1Stub_SingleMu_D49_SW6p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW6p5', '100000', 'mu'], 'L1Stub_TTbar_D49_SW6p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW6p5', '9000', 'pion'], 'L1Stub_SingleMu_D49_SW6p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW6p0', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SW1p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW1p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SW7p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW7p0', '9000', 'pion'], 'L1Stub_SingleMu_D49_SWtight': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SWtight', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SW0p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SW0p5', '100000', 'mu'], 'L1Stub_SingleMu_D49_SWloose': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SWloose', '100000', 'mu'], 'L1Stub_SingleElectron_D49_SW6p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW6p5', '100000', 'ele'], 'L1Stub_SingleMu_D49_SW7p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW7p0', '100000', 'mu'], 'L1Stub_SingleMu_D49_SW4p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW4p5', '100000', 'mu'], 'L1Stub_DisplacedMu_D49_SWloose': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_DisplacedMu_D49_SWloose', '100000', 'mu'], 'L1Stub_SingleMu_D49_SW4p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW4p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SW4p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW4p5', '9000', 'pion'], 'L1Stub_SingleMu_D49_SW5p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW5p5', '100000', 'mu'], 'L1Stub_TTbar_D49_SW5p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW5p0', '9000', 'pion'], 'L1Stub_SingleMu_D49_SW5p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleMu_D49_SW5p0', '100000', 'mu'], 'L1Stub_TTbar_D49_SW5p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW5p5', '9000', 'pion'], 'L1Stub_TTbar_D49_SW1p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_D49_SW1p0', '9000', 'pion'], 'L1Stub_SingleElectron_D49_SW6p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_SingleElectron_D49_SW6p0', '100000', 'ele']}

wf = []

for key, value in samples.items():
    if 'DisplacedMu' not in key:
        continue
    print key
    Analysis = Workflow(
        label='FE_L1Analysis_%s' % (key),
        sandbox=cmssw.Sandbox(release='/afs/crc.nd.edu/user/r/rgoldouz/CMSSW_10_4_0'),
        dataset=Dataset(
           files=value[0],
           files_per_task=50),
        globaltag=False,
        command='python Lobster_check.py '+ value[1]  + ' ' + value[2] + ' @inputfiles',
        extra_inputs=[
            'Lobster_check.py',
            '../lib/main.so',
            '../include/MyAnalysis.h',
        ],
        outputs=['ANoutput.root'],
#        dataset=Dataset(
#           files=value[0],
#           files_per_task=50,
#           patterns=["*.root"]
#        ),
#        merge_command='hadd @outputfiles @inputfiles',
#        merge_size='3.5G',
        category=gs_resources
    )
    wf.append(Analysis)

config = Config(
    label=master_label,
    workdir=workdir_path,
    plotdir=plotdir_path,
    storage=storage,
    workflows=wf,
    advanced=AdvancedOptions(
        bad_exit_codes=[127, 160],
        log_level=1,
        payload=10,
        dashboard = False,
        xrootd_servers=['ndcms.crc.nd.edu',
                       'cmsxrootd.fnal.gov',
                       'deepthought.crc.nd.edu'],
    )
)

