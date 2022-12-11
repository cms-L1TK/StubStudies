import datetime
import os
import os.path
from os import path
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
samples ={'L1Stub_DisplacedMu_D76_SW2p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SW2p5', '100000', 'mu'], 'L1Stub_TTbar_D76_SW6p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SW6p0', '9000', 'pion'], 'L1Stub_DisplacedMu_D76_SW6p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SW6p5', '100000', 'mu'], 'L1Stub_SingleMu_D76_SW7p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SW7p0', '100000', 'mu'], 'L1Stub_TTbar_D76_SW6p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SW6p5', '9000', 'pion'], 'L1Stub_TTbar_D76_SW7p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SW7p0', '9000', 'pion'], 'L1Stub_DisplacedMu_D76_SW1p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SW1p5', '100000', 'mu'], 'L1Stub_SingleMu_D76_SW0p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SW0p5', '100000', 'mu'], 'L1Stub_DisplacedMu_D76_SW5p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SW5p5', '100000', 'mu'], 'L1Stub_SingleMu_D76_SW5p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SW5p5', '100000', 'mu'], 'L1Stub_TTbar_D76_SWold': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SWold', '9000', 'pion'], 'L1Stub_DisplacedMu_D76_SW3p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SW3p0', '100000', 'mu'], 'L1Stub_SingleElectron_D76_SWtight': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SWtight', '100000', 'ele'], 'L1Stub_SingleMu_D76_SW5p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SW5p0', '100000', 'mu'], 'L1Stub_DisplacedMu_D76_SW4p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SW4p0', '100000', 'mu'], 'L1Stub_SingleMu_D76_SW6p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SW6p5', '100000', 'mu'], 'L1Stub_TTbar_D76_SW3p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SW3p0', '9000', 'pion'], 'L1Stub_SingleMu_D76_SW6p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SW6p0', '100000', 'mu'], 'L1Stub_TTbar_D76_SWtight': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SWtight', '9000', 'pion'], 'L1Stub_TTbar_D76_SW2p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SW2p5', '9000', 'pion'], 'L1Stub_TTbar_D76_SW2p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SW2p0', '9000', 'pion'], 'L1Stub_DisplacedMu_D76_SW1p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SW1p0', '100000', 'mu'], 'L1Stub_DisplacedMu_D76_SW4p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SW4p5', '100000', 'mu'], 'L1Stub_SingleElectron_D76_SWloose': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SWloose', '100000', 'ele'], 'L1Stub_TTbar_D76_SW3p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SW3p5', '9000', 'pion'], 'L1Stub_DisplacedMu_D76_SWloose': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SWloose', '100000', 'mu'], 'L1Stub_DisplacedMu_D76_SW2p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SW2p0', '100000', 'mu'], 'L1Stub_SingleMu_D76_SWloose': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SWloose', '100000', 'mu'], 'L1Stub_SingleMu_D76_SW2p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SW2p5', '100000', 'mu'], 'L1Stub_SingleElectron_D76_SW4p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SW4p0', '100000', 'ele'], 'L1Stub_TTbar_D76_SW0p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SW0p5', '9000', 'pion'], 'L1Stub_SingleElectron_D76_SW4p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SW4p5', '100000', 'ele'], 'L1Stub_DisplacedMu_D76_SW0p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SW0p5', '100000', 'mu'], 'L1Stub_TTbar_D76_SW1p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SW1p5', '9000', 'pion'], 'L1Stub_SingleElectron_D76_SW5p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SW5p0', '100000', 'ele'], 'L1Stub_DisplacedMu_D76_SW6p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SW6p0', '100000', 'mu'], 'L1Stub_SingleElectron_D76_SW5p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SW5p5', '100000', 'ele'], 'L1Stub_TTbar_D76_SW1p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SW1p0', '9000', 'pion'], 'L1Stub_DisplacedMu_D76_SWtight': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SWtight', '100000', 'mu'], 'L1Stub_SingleElectron_D76_SWold': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SWold', '100000', 'ele'], 'L1Stub_SingleMu_D76_SW3p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SW3p0', '100000', 'mu'], 'L1Stub_SingleElectron_D76_SW6p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SW6p0', '100000', 'ele'], 'L1Stub_SingleMu_D76_SW3p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SW3p5', '100000', 'mu'], 'L1Stub_SingleElectron_D76_SW6p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SW6p5', '100000', 'ele'], 'L1Stub_SingleElectron_D76_SW7p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SW7p0', '100000', 'ele'], 'L1Stub_DisplacedMu_D76_SWold': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SWold', '100000', 'mu'], 'L1Stub_SingleMu_D76_SW1p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SW1p0', '100000', 'mu'], 'L1Stub_SingleMu_D76_SW1p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SW1p5', '100000', 'mu'], 'L1Stub_SingleMu_D76_SW2p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SW2p0', '100000', 'mu'], 'L1Stub_SingleMu_D76_SWold': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SWold', '100000', 'mu'], 'L1Stub_SingleElectron_D76_SW2p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SW2p5', '100000', 'ele'], 'L1Stub_SingleMu_D76_SWtight': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SWtight', '100000', 'mu'], 'L1Stub_DisplacedMu_D76_SW3p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SW3p5', '100000', 'mu'], 'L1Stub_SingleElectron_D76_SW2p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SW2p0', '100000', 'ele'], 'L1Stub_DisplacedMu_D76_SW7p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SW7p0', '100000', 'mu'], 'L1Stub_SingleElectron_D76_SW3p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SW3p5', '100000', 'ele'], 'L1Stub_SingleMu_D76_SW4p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SW4p5', '100000', 'mu'], 'L1Stub_SingleMu_D76_SW4p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleMu_D76_SW4p0', '100000', 'mu'], 'L1Stub_SingleElectron_D76_SW3p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SW3p0', '100000', 'ele'], 'L1Stub_TTbar_D76_SW4p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SW4p0', '9000', 'pion'], 'L1Stub_SingleElectron_D76_SW0p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SW0p5', '100000', 'ele'], 'L1Stub_TTbar_D76_SWloose': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SWloose', '9000', 'pion'], 'L1Stub_TTbar_D76_SW4p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SW4p5', '9000', 'pion'], 'L1Stub_SingleElectron_D76_SW1p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SW1p5', '100000', 'ele'], 'L1Stub_TTbar_D76_SW5p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SW5p0', '9000', 'pion'], 'L1Stub_TTbar_D76_SW5p5': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_TTbar_D76_SW5p5', '9000', 'pion'], 'L1Stub_SingleElectron_D76_SW1p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_SingleElectron_D76_SW1p0', '100000', 'ele'], 'L1Stub_DisplacedMu_D76_SW5p0': ['rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5V2/L1Stub_DisplacedMu_D76_SW5p0', '100000', 'mu']}
wf = []

for key, value in samples.items():
    if (path.exists('/hadoop/store/user/rgoldouz/FullProduction/L1Analysis/FE_L1Analysis_' + key)):
        continue
    print key
    Analysis = Workflow(
        label='FE_L1Analysis_%s' % (key),
        sandbox=cmssw.Sandbox(release='/afs/crc.nd.edu/user/r/rgoldouz/CMSSW_10_4_0'),
        dataset=Dataset(
           files=value[0],
           files_per_task=5),
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

