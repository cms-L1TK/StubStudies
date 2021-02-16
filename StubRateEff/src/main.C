#include "MyAnalysis.h"
int main(){
    TChain* ch    = new TChain("L1TrackNtuple/eventTree") ;
//    ch ->Add("/hadoop/store/user/rgoldouz/FullProduction/L1tracker_DAS/L1Stub_DisplacedMuPt2To100_Pu0_110D49/*.root");
//    ch ->Add("/hadoop/store/user/rgoldouz/FullProduction/L1tracker_DAS/L1Stub_SingleMuFlatPt1p5To8_Pu200_110D49/outfile_2016.root");
//    ch ->Add("/afs/crc.nd.edu/user/r/rgoldouz/L1tracker/CMSSW_11_1_0_pre8/src/L1Trigger/TrackFindingTracklet/test/outfile.root");
//    ch ->Add("/hadoop/store/user/rgoldouz/FullProduction/L1tracker_DAS_110pre8/L1Stub_Tt_Pu200_110D49/outfile_911.root");
//    ch ->Add("/hadoop/store/user/rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_OldTune_L1Stub_Tt_Pu200_110D49/outfile_953.root");
//    ch ->Add("/hadoop/store/user/rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_OldTune_L1Stub_Tt_Pu200_110D49/outfile_959.root");
//    ch ->Add("/hadoop/store/user/rgoldouz/FullProduction/L1tracker_DAS_110pre8/FE_OldTune_L1Stub_Tt_Pu200_110D49/outfile_948.root");
//    ch ->Add("/afs/crc.nd.edu/user/r/rgoldouz/L1tracker/Analysis/StubStudies/StubRateEff/Sele.root");
//    ch ->Add("~/L1tracker/CMSSW_11_2_0_pre5/src/L1Trigger/TrackFindingTracklet/test/outfile.root");  
//    ch ->Add("/hadoop/store/user/rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_Tt_Pu200_112pre5_New/outfile_3.root"); 
   ch ->Add("/hadoop/store/user/rgoldouz/FullProduction/L1tracker_DAS_CMSSW112pre5/L1Stub_TTbar_CMSSW_11_2_0_pre5_2026D49PU200_SW3p5/outfile_9.root");
    MyAnalysis t1(ch);
//    t1.Loop("DisplacedMuPt2To100_Pu0_110D49.root",100000);
    t1.Loop("pre5test.root",10000, "ele");
}
