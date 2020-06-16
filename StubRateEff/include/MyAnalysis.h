//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Sat May  9 09:17:22 2020 by ROOT version 6.12/07
// from TTree eventTree/Event tree
// found on file: /hadoop/store/user/rgoldouz/FullProduction/L1tracker_DAS/L1Stub_DisplacedMuPt2To100_Pu0_110D49/outfile_70.root
//////////////////////////////////////////////////////////

#ifndef MyAnalysis_h
#define MyAnalysis_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
#include "vector"
#include "vector"
#include "vector"
using namespace std;

class MyAnalysis {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

// Fixed size dimensions of array or collections stored in the TTree if any.

   // Declaration of leaf types
   vector<float>   *trk_pt;
   vector<float>   *trk_eta;
   vector<float>   *trk_phi;
   vector<float>   *trk_d0;
   vector<float>   *trk_z0;
   vector<float>   *trk_chi2;
   vector<float>   *trk_chi2rphi;
   vector<float>   *trk_chi2rz;
   vector<float>   *trk_bendchi2;
   vector<int>     *trk_nstub;
   vector<int>     *trk_lhits;
   vector<int>     *trk_dhits;
   vector<int>     *trk_seed;
   vector<int>     *trk_hitpattern;
   vector<unsigned int> *trk_phiSector;
   vector<int>     *trk_genuine;
   vector<int>     *trk_loose;
   vector<int>     *trk_unknown;
   vector<int>     *trk_combinatoric;
   vector<int>     *trk_fake;
   vector<int>     *trk_matchtp_pdgid;
   vector<float>   *trk_matchtp_pt;
   vector<float>   *trk_matchtp_eta;
   vector<float>   *trk_matchtp_phi;
   vector<float>   *trk_matchtp_z0;
   vector<float>   *trk_matchtp_dxy;
   vector<int>     *trk_injet;
   vector<int>     *trk_injet_highpt;
   vector<int>     *trk_injet_vhighpt;
   vector<float>   *tp_pt;
   vector<float>   *tp_eta;
   vector<float>   *tp_phi;
   vector<float>   *tp_dxy;
   vector<float>   *tp_d0;
   vector<float>   *tp_z0;
   vector<float>   *tp_d0_prod;
   vector<float>   *tp_z0_prod;
   vector<int>     *tp_pdgid;
   vector<int>     *tp_nmatch;
   vector<int>     *tp_nloosematch;
   vector<int>     *tp_nstub;
   vector<int>     *tp_eventid;
   vector<int>     *tp_charge;
   vector<int>     *tp_injet;
   vector<int>     *tp_injet_highpt;
   vector<int>     *tp_injet_vhighpt;
   vector<float>   *matchtrk_pt;
   vector<float>   *matchtrk_eta;
   vector<float>   *matchtrk_phi;
   vector<float>   *matchtrk_z0;
   vector<float>   *matchtrk_d0;
   vector<float>   *matchtrk_chi2;
   vector<float>   *matchtrk_chi2rphi;
   vector<float>   *matchtrk_chi2rz;
   vector<float>   *matchtrk_bendchi2;
   vector<int>     *matchtrk_nstub;
   vector<int>     *matchtrk_lhits;
   vector<int>     *matchtrk_dhits;
   vector<int>     *matchtrk_seed;
   vector<int>     *matchtrk_hitpattern;
   vector<int>     *matchtrk_injet;
   vector<int>     *matchtrk_injet_highpt;
   vector<int>     *matchtrk_injet_vhighpt;
   vector<float>   *loosematchtrk_pt;
   vector<float>   *loosematchtrk_eta;
   vector<float>   *loosematchtrk_phi;
   vector<float>   *loosematchtrk_z0;
   vector<float>   *loosematchtrk_d0;
   vector<float>   *loosematchtrk_chi2;
   vector<float>   *loosematchtrk_chi2rphi;
   vector<float>   *loosematchtrk_chi2rz;
   vector<float>   *loosematchtrk_bendchi2;
   vector<int>     *loosematchtrk_nstub;
   vector<int>     *loosematchtrk_seed;
   vector<int>     *loosematchtrk_hitpattern;
   vector<int>     *loosematchtrk_injet;
   vector<int>     *loosematchtrk_injet_highpt;
   vector<int>     *loosematchtrk_injet_vhighpt;
   vector<int>     *stubEff_BL1;
   vector<int>     *stubEff_BL2;
   vector<int>     *stubEff_BL3;
   vector<int>     *stubEff_BL4;
   vector<int>     *stubEff_BL5;
   vector<int>     *stubEff_BL6;
   vector<int>     *stubEff_EL1;
   vector<int>     *stubEff_EL2;
   vector<int>     *stubEff_EL3;
   vector<int>     *stubEff_EL4;
   vector<int>     *stubEff_EL5;
   vector<int>     *clustEff_BL1;
   vector<int>     *clustEff_BL2;
   vector<int>     *clustEff_BL3;
   vector<int>     *clustEff_BL4;
   vector<int>     *clustEff_BL5;
   vector<int>     *clustEff_BL6;
   vector<int>     *clustEff_EL1;
   vector<int>     *clustEff_EL2;
   vector<int>     *clustEff_EL3;
   vector<int>     *clustEff_EL4;
   vector<int>     *clustEff_EL5;
   vector<float>   *stubEff_tp_pt;
   vector<int>     *stubEff_tp_pdgid;
   vector<float>   *stubEff_tp_eta;
   vector<float>   *stubEff_tp_phi;
   vector<float>   *allstub_x;
   vector<float>   *allstub_y;
   vector<float>   *allstub_z;
   vector<int>     *allstub_isBarrel;
   vector<int>     *allstub_layer;
   vector<int>     *allstub_isPSmodule;
   vector<float>   *allstub_trigDisplace;
   vector<float>   *allstub_trigOffset;
   vector<float>   *allstub_trigPos;
   vector<float>   *allstub_trigBend;
   vector<int>     *allstub_matchTP_pdgid;
   vector<float>   *allstub_matchTP_pt;
   vector<float>   *allstub_matchTP_eta;
   vector<float>   *allstub_matchTP_phi;
   vector<int>     *allstub_genuine;
   vector<int>     *allstub_isCombinatoric;
   vector<int>     *allstub_isUnknown;
   vector<int>     *allstub_chip;
   vector<int>     *allstub_seg;
   vector<int>     *allstub_ladder;
   vector<int>     *allstub_module;
   vector<int>     *allstub_type;
   vector<float>   *allstub_module_x;
   vector<float>   *allstub_module_y;
   vector<float>   *allstub_module_z;
   vector<int>     *allstub_fromPU;
   vector<float>   *jet_eta;
   vector<float>   *jet_phi;
   vector<float>   *jet_pt;
   vector<float>   *jet_tp_sumpt;
   vector<float>   *jet_trk_sumpt;
   vector<float>   *jet_matchtrk_sumpt;
   vector<float>   *jet_loosematchtrk_sumpt;

   // List of branches
   TBranch        *b_trk_pt;   //!
   TBranch        *b_trk_eta;   //!
   TBranch        *b_trk_phi;   //!
   TBranch        *b_trk_d0;   //!
   TBranch        *b_trk_z0;   //!
   TBranch        *b_trk_chi2;   //!
   TBranch        *b_trk_chi2rphi;   //!
   TBranch        *b_trk_chi2rz;   //!
   TBranch        *b_trk_bendchi2;   //!
   TBranch        *b_trk_nstub;   //!
   TBranch        *b_trk_lhits;   //!
   TBranch        *b_trk_dhits;   //!
   TBranch        *b_trk_seed;   //!
   TBranch        *b_trk_hitpattern;   //!
   TBranch        *b_trk_phiSector;   //!
   TBranch        *b_trk_genuine;   //!
   TBranch        *b_trk_loose;   //!
   TBranch        *b_trk_unknown;   //!
   TBranch        *b_trk_combinatoric;   //!
   TBranch        *b_trk_fake;   //!
   TBranch        *b_trk_matchtp_pdgid;   //!
   TBranch        *b_trk_matchtp_pt;   //!
   TBranch        *b_trk_matchtp_eta;   //!
   TBranch        *b_trk_matchtp_phi;   //!
   TBranch        *b_trk_matchtp_z0;   //!
   TBranch        *b_trk_matchtp_dxy;   //!
   TBranch        *b_trk_injet;   //!
   TBranch        *b_trk_injet_highpt;   //!
   TBranch        *b_trk_injet_vhighpt;   //!
   TBranch        *b_tp_pt;   //!
   TBranch        *b_tp_eta;   //!
   TBranch        *b_tp_phi;   //!
   TBranch        *b_tp_dxy;   //!
   TBranch        *b_tp_d0;   //!
   TBranch        *b_tp_z0;   //!
   TBranch        *b_tp_d0_prod;   //!
   TBranch        *b_tp_z0_prod;   //!
   TBranch        *b_tp_pdgid;   //!
   TBranch        *b_tp_nmatch;   //!
   TBranch        *b_tp_nloosematch;   //!
   TBranch        *b_tp_nstub;   //!
   TBranch        *b_tp_eventid;   //!
   TBranch        *b_tp_charge;   //!
   TBranch        *b_tp_injet;   //!
   TBranch        *b_tp_injet_highpt;   //!
   TBranch        *b_tp_injet_vhighpt;   //!
   TBranch        *b_matchtrk_pt;   //!
   TBranch        *b_matchtrk_eta;   //!
   TBranch        *b_matchtrk_phi;   //!
   TBranch        *b_matchtrk_z0;   //!
   TBranch        *b_matchtrk_d0;   //!
   TBranch        *b_matchtrk_chi2;   //!
   TBranch        *b_matchtrk_chi2rphi;   //!
   TBranch        *b_matchtrk_chi2rz;   //!
   TBranch        *b_matchtrk_bendchi2;   //!
   TBranch        *b_matchtrk_nstub;   //!
   TBranch        *b_matchtrk_lhits;   //!
   TBranch        *b_matchtrk_dhits;   //!
   TBranch        *b_matchtrk_seed;   //!
   TBranch        *b_matchtrk_hitpattern;   //!
   TBranch        *b_matchtrk_injet;   //!
   TBranch        *b_matchtrk_injet_highpt;   //!
   TBranch        *b_matchtrk_injet_vhighpt;   //!
   TBranch        *b_loosematchtrk_pt;   //!
   TBranch        *b_loosematchtrk_eta;   //!
   TBranch        *b_loosematchtrk_phi;   //!
   TBranch        *b_loosematchtrk_z0;   //!
   TBranch        *b_loosematchtrk_d0;   //!
   TBranch        *b_loosematchtrk_chi2;   //!
   TBranch        *b_loosematchtrk_chi2rphi;   //!
   TBranch        *b_loosematchtrk_chi2rz;   //!
   TBranch        *b_loosematchtrk_bendchi2;   //!
   TBranch        *b_loosematchtrk_nstub;   //!
   TBranch        *b_loosematchtrk_seed;   //!
   TBranch        *b_loosematchtrk_hitpattern;   //!
   TBranch        *b_loosematchtrk_injet;   //!
   TBranch        *b_loosematchtrk_injet_highpt;   //!
   TBranch        *b_loosematchtrk_injet_vhighpt;   //!
   TBranch        *b_stubEff_BL1;   //!
   TBranch        *b_stubEff_BL2;   //!
   TBranch        *b_stubEff_BL3;   //!
   TBranch        *b_stubEff_BL4;   //!
   TBranch        *b_stubEff_BL5;   //!
   TBranch        *b_stubEff_BL6;   //!
   TBranch        *b_stubEff_EL1;   //!
   TBranch        *b_stubEff_EL2;   //!
   TBranch        *b_stubEff_EL3;   //!
   TBranch        *b_stubEff_EL4;   //!
   TBranch        *b_stubEff_EL5;   //!
   TBranch        *b_clustEff_BL1;   //!
   TBranch        *b_clustEff_BL2;   //!
   TBranch        *b_clustEff_BL3;   //!
   TBranch        *b_clustEff_BL4;   //!
   TBranch        *b_clustEff_BL5;   //!
   TBranch        *b_clustEff_BL6;   //!
   TBranch        *b_clustEff_EL1;   //!
   TBranch        *b_clustEff_EL2;   //!
   TBranch        *b_clustEff_EL3;   //!
   TBranch        *b_clustEff_EL4;   //!
   TBranch        *b_clustEff_EL5;   //!
   TBranch        *b_stubEff_tp_pt;   //!
   TBranch        *b_stubEff_tp_pdgid;   //!
   TBranch        *b_stubEff_tp_eta;   //!
   TBranch        *b_stubEff_tp_phi;   //!
   TBranch        *b_allstub_x;   //!
   TBranch        *b_allstub_y;   //!
   TBranch        *b_allstub_z;   //!
   TBranch        *b_allstub_isBarrel;   //!
   TBranch        *b_allstub_layer;   //!
   TBranch        *b_allstub_isPSmodule;   //!
   TBranch        *b_allstub_trigDisplace;   //!
   TBranch        *b_allstub_trigOffset;   //!
   TBranch        *b_allstub_trigPos;   //!
   TBranch        *b_allstub_trigBend;   //!
   TBranch        *b_allstub_matchTP_pdgid;   //!
   TBranch        *b_allstub_matchTP_pt;   //!
   TBranch        *b_allstub_matchTP_eta;   //!
   TBranch        *b_allstub_matchTP_phi;   //!
   TBranch        *b_allstub_genuine;   //!
   TBranch        *b_allstub_isCombinatoric;   //!
   TBranch        *b_allstub_isUnknown;   //!
   TBranch        *b_allstub_chip;   //!
   TBranch        *b_allstub_seg;   //!
   TBranch        *b_allstub_ladder;   //!
   TBranch        *b_allstub_module;   //!
   TBranch        *b_allstub_type;   //!
   TBranch        *b_allstub_module_x;   //!
   TBranch        *b_allstub_module_y;   //!
   TBranch        *b_allstub_module_z;   //!
   TBranch        *b_allstub_fromPU;   //!
   TBranch        *b_jet_eta;   //!
   TBranch        *b_jet_phi;   //!
   TBranch        *b_jet_pt;   //!
   TBranch        *b_jet_tp_sumpt;   //!
   TBranch        *b_jet_trk_sumpt;   //!
   TBranch        *b_jet_matchtrk_sumpt;   //!
   TBranch        *b_jet_loosematchtrk_sumpt;   //!

   MyAnalysis(TTree *tree=0);
   virtual ~MyAnalysis();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop(TString, float, TString);
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef MyAnalysis_cxx
MyAnalysis::MyAnalysis(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("/hadoop/store/user/rgoldouz/FullProduction/L1tracker_DAS/L1Stub_DisplacedMuPt2To100_Pu0_110D49/outfile_70.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("/hadoop/store/user/rgoldouz/FullProduction/L1tracker_DAS/L1Stub_DisplacedMuPt2To100_Pu0_110D49/outfile_70.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("/hadoop/store/user/rgoldouz/FullProduction/L1tracker_DAS/L1Stub_DisplacedMuPt2To100_Pu0_110D49/outfile_70.root:/L1TrackNtuple");
      dir->GetObject("eventTree",tree);

   }
   Init(tree);
}

MyAnalysis::~MyAnalysis()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t MyAnalysis::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t MyAnalysis::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void MyAnalysis::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
   trk_pt = 0;
   trk_eta = 0;
   trk_phi = 0;
   trk_d0 = 0;
   trk_z0 = 0;
   trk_chi2 = 0;
   trk_chi2rphi = 0;
   trk_chi2rz = 0;
   trk_bendchi2 = 0;
   trk_nstub = 0;
   trk_lhits = 0;
   trk_dhits = 0;
   trk_seed = 0;
   trk_hitpattern = 0;
   trk_phiSector = 0;
   trk_genuine = 0;
   trk_loose = 0;
   trk_unknown = 0;
   trk_combinatoric = 0;
   trk_fake = 0;
   trk_matchtp_pdgid = 0;
   trk_matchtp_pt = 0;
   trk_matchtp_eta = 0;
   trk_matchtp_phi = 0;
   trk_matchtp_z0 = 0;
   trk_matchtp_dxy = 0;
   trk_injet = 0;
   trk_injet_highpt = 0;
   trk_injet_vhighpt = 0;
   tp_pt = 0;
   tp_eta = 0;
   tp_phi = 0;
   tp_dxy = 0;
   tp_d0 = 0;
   tp_z0 = 0;
   tp_d0_prod = 0;
   tp_z0_prod = 0;
   tp_pdgid = 0;
   tp_nmatch = 0;
   tp_nloosematch = 0;
   tp_nstub = 0;
   tp_eventid = 0;
   tp_charge = 0;
   tp_injet = 0;
   tp_injet_highpt = 0;
   tp_injet_vhighpt = 0;
   matchtrk_pt = 0;
   matchtrk_eta = 0;
   matchtrk_phi = 0;
   matchtrk_z0 = 0;
   matchtrk_d0 = 0;
   matchtrk_chi2 = 0;
   matchtrk_chi2rphi = 0;
   matchtrk_chi2rz = 0;
   matchtrk_bendchi2 = 0;
   matchtrk_nstub = 0;
   matchtrk_lhits = 0;
   matchtrk_dhits = 0;
   matchtrk_seed = 0;
   matchtrk_hitpattern = 0;
   matchtrk_injet = 0;
   matchtrk_injet_highpt = 0;
   matchtrk_injet_vhighpt = 0;
   loosematchtrk_pt = 0;
   loosematchtrk_eta = 0;
   loosematchtrk_phi = 0;
   loosematchtrk_z0 = 0;
   loosematchtrk_d0 = 0;
   loosematchtrk_chi2 = 0;
   loosematchtrk_chi2rphi = 0;
   loosematchtrk_chi2rz = 0;
   loosematchtrk_bendchi2 = 0;
   loosematchtrk_nstub = 0;
   loosematchtrk_seed = 0;
   loosematchtrk_hitpattern = 0;
   loosematchtrk_injet = 0;
   loosematchtrk_injet_highpt = 0;
   loosematchtrk_injet_vhighpt = 0;
   stubEff_BL1 = 0;
   stubEff_BL2 = 0;
   stubEff_BL3 = 0;
   stubEff_BL4 = 0;
   stubEff_BL5 = 0;
   stubEff_BL6 = 0;
   stubEff_EL1 = 0;
   stubEff_EL2 = 0;
   stubEff_EL3 = 0;
   stubEff_EL4 = 0;
   stubEff_EL5 = 0;
   clustEff_BL1 = 0;
   clustEff_BL2 = 0;
   clustEff_BL3 = 0;
   clustEff_BL4 = 0;
   clustEff_BL5 = 0;
   clustEff_BL6 = 0;
   clustEff_EL1 = 0;
   clustEff_EL2 = 0;
   clustEff_EL3 = 0;
   clustEff_EL4 = 0;
   clustEff_EL5 = 0;
   stubEff_tp_pt = 0;
   stubEff_tp_pdgid = 0;
   stubEff_tp_eta = 0;
   stubEff_tp_phi = 0;
   allstub_x = 0;
   allstub_y = 0;
   allstub_z = 0;
   allstub_isBarrel = 0;
   allstub_layer = 0;
   allstub_isPSmodule = 0;
   allstub_trigDisplace = 0;
   allstub_trigOffset = 0;
   allstub_trigPos = 0;
   allstub_trigBend = 0;
   allstub_matchTP_pdgid = 0;
   allstub_matchTP_pt = 0;
   allstub_matchTP_eta = 0;
   allstub_matchTP_phi = 0;
   allstub_genuine = 0;
   allstub_isCombinatoric = 0;
   allstub_isUnknown = 0;
   allstub_chip = 0;
   allstub_seg = 0;
   allstub_ladder = 0;
   allstub_module = 0;
   allstub_type = 0;
   allstub_module_x = 0;
   allstub_module_y = 0;
   allstub_module_z = 0;
   allstub_fromPU = 0;
   jet_eta = 0;
   jet_phi = 0;
   jet_pt = 0;
   jet_tp_sumpt = 0;
   jet_trk_sumpt = 0;
   jet_matchtrk_sumpt = 0;
   jet_loosematchtrk_sumpt = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("trk_pt", &trk_pt, &b_trk_pt);
   fChain->SetBranchAddress("trk_eta", &trk_eta, &b_trk_eta);
   fChain->SetBranchAddress("trk_phi", &trk_phi, &b_trk_phi);
   fChain->SetBranchAddress("trk_d0", &trk_d0, &b_trk_d0);
   fChain->SetBranchAddress("trk_z0", &trk_z0, &b_trk_z0);
   fChain->SetBranchAddress("trk_chi2", &trk_chi2, &b_trk_chi2);
   fChain->SetBranchAddress("trk_chi2rphi", &trk_chi2rphi, &b_trk_chi2rphi);
   fChain->SetBranchAddress("trk_chi2rz", &trk_chi2rz, &b_trk_chi2rz);
   fChain->SetBranchAddress("trk_bendchi2", &trk_bendchi2, &b_trk_bendchi2);
   fChain->SetBranchAddress("trk_nstub", &trk_nstub, &b_trk_nstub);
   fChain->SetBranchAddress("trk_lhits", &trk_lhits, &b_trk_lhits);
   fChain->SetBranchAddress("trk_dhits", &trk_dhits, &b_trk_dhits);
   fChain->SetBranchAddress("trk_seed", &trk_seed, &b_trk_seed);
   fChain->SetBranchAddress("trk_hitpattern", &trk_hitpattern, &b_trk_hitpattern);
   fChain->SetBranchAddress("trk_phiSector", &trk_phiSector, &b_trk_phiSector);
   fChain->SetBranchAddress("trk_genuine", &trk_genuine, &b_trk_genuine);
   fChain->SetBranchAddress("trk_loose", &trk_loose, &b_trk_loose);
   fChain->SetBranchAddress("trk_unknown", &trk_unknown, &b_trk_unknown);
   fChain->SetBranchAddress("trk_combinatoric", &trk_combinatoric, &b_trk_combinatoric);
   fChain->SetBranchAddress("trk_fake", &trk_fake, &b_trk_fake);
   fChain->SetBranchAddress("trk_matchtp_pdgid", &trk_matchtp_pdgid, &b_trk_matchtp_pdgid);
   fChain->SetBranchAddress("trk_matchtp_pt", &trk_matchtp_pt, &b_trk_matchtp_pt);
   fChain->SetBranchAddress("trk_matchtp_eta", &trk_matchtp_eta, &b_trk_matchtp_eta);
   fChain->SetBranchAddress("trk_matchtp_phi", &trk_matchtp_phi, &b_trk_matchtp_phi);
   fChain->SetBranchAddress("trk_matchtp_z0", &trk_matchtp_z0, &b_trk_matchtp_z0);
   fChain->SetBranchAddress("trk_matchtp_dxy", &trk_matchtp_dxy, &b_trk_matchtp_dxy);
   fChain->SetBranchAddress("trk_injet", &trk_injet, &b_trk_injet);
   fChain->SetBranchAddress("trk_injet_highpt", &trk_injet_highpt, &b_trk_injet_highpt);
   fChain->SetBranchAddress("trk_injet_vhighpt", &trk_injet_vhighpt, &b_trk_injet_vhighpt);
   fChain->SetBranchAddress("tp_pt", &tp_pt, &b_tp_pt);
   fChain->SetBranchAddress("tp_eta", &tp_eta, &b_tp_eta);
   fChain->SetBranchAddress("tp_phi", &tp_phi, &b_tp_phi);
   fChain->SetBranchAddress("tp_dxy", &tp_dxy, &b_tp_dxy);
   fChain->SetBranchAddress("tp_d0", &tp_d0, &b_tp_d0);
   fChain->SetBranchAddress("tp_z0", &tp_z0, &b_tp_z0);
   fChain->SetBranchAddress("tp_d0_prod", &tp_d0_prod, &b_tp_d0_prod);
   fChain->SetBranchAddress("tp_z0_prod", &tp_z0_prod, &b_tp_z0_prod);
   fChain->SetBranchAddress("tp_pdgid", &tp_pdgid, &b_tp_pdgid);
   fChain->SetBranchAddress("tp_nmatch", &tp_nmatch, &b_tp_nmatch);
   fChain->SetBranchAddress("tp_nloosematch", &tp_nloosematch, &b_tp_nloosematch);
   fChain->SetBranchAddress("tp_nstub", &tp_nstub, &b_tp_nstub);
   fChain->SetBranchAddress("tp_eventid", &tp_eventid, &b_tp_eventid);
   fChain->SetBranchAddress("tp_charge", &tp_charge, &b_tp_charge);
   fChain->SetBranchAddress("tp_injet", &tp_injet, &b_tp_injet);
   fChain->SetBranchAddress("tp_injet_highpt", &tp_injet_highpt, &b_tp_injet_highpt);
   fChain->SetBranchAddress("tp_injet_vhighpt", &tp_injet_vhighpt, &b_tp_injet_vhighpt);
   fChain->SetBranchAddress("matchtrk_pt", &matchtrk_pt, &b_matchtrk_pt);
   fChain->SetBranchAddress("matchtrk_eta", &matchtrk_eta, &b_matchtrk_eta);
   fChain->SetBranchAddress("matchtrk_phi", &matchtrk_phi, &b_matchtrk_phi);
   fChain->SetBranchAddress("matchtrk_z0", &matchtrk_z0, &b_matchtrk_z0);
   fChain->SetBranchAddress("matchtrk_d0", &matchtrk_d0, &b_matchtrk_d0);
   fChain->SetBranchAddress("matchtrk_chi2", &matchtrk_chi2, &b_matchtrk_chi2);
   fChain->SetBranchAddress("matchtrk_chi2rphi", &matchtrk_chi2rphi, &b_matchtrk_chi2rphi);
   fChain->SetBranchAddress("matchtrk_chi2rz", &matchtrk_chi2rz, &b_matchtrk_chi2rz);
   fChain->SetBranchAddress("matchtrk_bendchi2", &matchtrk_bendchi2, &b_matchtrk_bendchi2);
   fChain->SetBranchAddress("matchtrk_nstub", &matchtrk_nstub, &b_matchtrk_nstub);
   fChain->SetBranchAddress("matchtrk_lhits", &matchtrk_lhits, &b_matchtrk_lhits);
   fChain->SetBranchAddress("matchtrk_dhits", &matchtrk_dhits, &b_matchtrk_dhits);
   fChain->SetBranchAddress("matchtrk_seed", &matchtrk_seed, &b_matchtrk_seed);
   fChain->SetBranchAddress("matchtrk_hitpattern", &matchtrk_hitpattern, &b_matchtrk_hitpattern);
   fChain->SetBranchAddress("matchtrk_injet", &matchtrk_injet, &b_matchtrk_injet);
   fChain->SetBranchAddress("matchtrk_injet_highpt", &matchtrk_injet_highpt, &b_matchtrk_injet_highpt);
   fChain->SetBranchAddress("matchtrk_injet_vhighpt", &matchtrk_injet_vhighpt, &b_matchtrk_injet_vhighpt);
   fChain->SetBranchAddress("loosematchtrk_pt", &loosematchtrk_pt, &b_loosematchtrk_pt);
   fChain->SetBranchAddress("loosematchtrk_eta", &loosematchtrk_eta, &b_loosematchtrk_eta);
   fChain->SetBranchAddress("loosematchtrk_phi", &loosematchtrk_phi, &b_loosematchtrk_phi);
   fChain->SetBranchAddress("loosematchtrk_z0", &loosematchtrk_z0, &b_loosematchtrk_z0);
   fChain->SetBranchAddress("loosematchtrk_d0", &loosematchtrk_d0, &b_loosematchtrk_d0);
   fChain->SetBranchAddress("loosematchtrk_chi2", &loosematchtrk_chi2, &b_loosematchtrk_chi2);
   fChain->SetBranchAddress("loosematchtrk_chi2rphi", &loosematchtrk_chi2rphi, &b_loosematchtrk_chi2rphi);
   fChain->SetBranchAddress("loosematchtrk_chi2rz", &loosematchtrk_chi2rz, &b_loosematchtrk_chi2rz);
   fChain->SetBranchAddress("loosematchtrk_bendchi2", &loosematchtrk_bendchi2, &b_loosematchtrk_bendchi2);
   fChain->SetBranchAddress("loosematchtrk_nstub", &loosematchtrk_nstub, &b_loosematchtrk_nstub);
   fChain->SetBranchAddress("loosematchtrk_seed", &loosematchtrk_seed, &b_loosematchtrk_seed);
   fChain->SetBranchAddress("loosematchtrk_hitpattern", &loosematchtrk_hitpattern, &b_loosematchtrk_hitpattern);
   fChain->SetBranchAddress("loosematchtrk_injet", &loosematchtrk_injet, &b_loosematchtrk_injet);
   fChain->SetBranchAddress("loosematchtrk_injet_highpt", &loosematchtrk_injet_highpt, &b_loosematchtrk_injet_highpt);
   fChain->SetBranchAddress("loosematchtrk_injet_vhighpt", &loosematchtrk_injet_vhighpt, &b_loosematchtrk_injet_vhighpt);
   fChain->SetBranchAddress("stubEff_BL1", &stubEff_BL1, &b_stubEff_BL1);
   fChain->SetBranchAddress("stubEff_BL2", &stubEff_BL2, &b_stubEff_BL2);
   fChain->SetBranchAddress("stubEff_BL3", &stubEff_BL3, &b_stubEff_BL3);
   fChain->SetBranchAddress("stubEff_BL4", &stubEff_BL4, &b_stubEff_BL4);
   fChain->SetBranchAddress("stubEff_BL5", &stubEff_BL5, &b_stubEff_BL5);
   fChain->SetBranchAddress("stubEff_BL6", &stubEff_BL6, &b_stubEff_BL6);
   fChain->SetBranchAddress("stubEff_EL1", &stubEff_EL1, &b_stubEff_EL1);
   fChain->SetBranchAddress("stubEff_EL2", &stubEff_EL2, &b_stubEff_EL2);
   fChain->SetBranchAddress("stubEff_EL3", &stubEff_EL3, &b_stubEff_EL3);
   fChain->SetBranchAddress("stubEff_EL4", &stubEff_EL4, &b_stubEff_EL4);
   fChain->SetBranchAddress("stubEff_EL5", &stubEff_EL5, &b_stubEff_EL5);
   fChain->SetBranchAddress("clustEff_BL1", &clustEff_BL1, &b_clustEff_BL1);
   fChain->SetBranchAddress("clustEff_BL2", &clustEff_BL2, &b_clustEff_BL2);
   fChain->SetBranchAddress("clustEff_BL3", &clustEff_BL3, &b_clustEff_BL3);
   fChain->SetBranchAddress("clustEff_BL4", &clustEff_BL4, &b_clustEff_BL4);
   fChain->SetBranchAddress("clustEff_BL5", &clustEff_BL5, &b_clustEff_BL5);
   fChain->SetBranchAddress("clustEff_BL6", &clustEff_BL6, &b_clustEff_BL6);
   fChain->SetBranchAddress("clustEff_EL1", &clustEff_EL1, &b_clustEff_EL1);
   fChain->SetBranchAddress("clustEff_EL2", &clustEff_EL2, &b_clustEff_EL2);
   fChain->SetBranchAddress("clustEff_EL3", &clustEff_EL3, &b_clustEff_EL3);
   fChain->SetBranchAddress("clustEff_EL4", &clustEff_EL4, &b_clustEff_EL4);
   fChain->SetBranchAddress("clustEff_EL5", &clustEff_EL5, &b_clustEff_EL5);
   fChain->SetBranchAddress("stubEff_tp_pt", &stubEff_tp_pt, &b_stubEff_tp_pt);
   fChain->SetBranchAddress("stubEff_tp_pdgid", &stubEff_tp_pdgid, &b_stubEff_tp_pdgid);
   fChain->SetBranchAddress("stubEff_tp_eta", &stubEff_tp_eta, &b_stubEff_tp_eta);
   fChain->SetBranchAddress("stubEff_tp_phi", &stubEff_tp_phi, &b_stubEff_tp_phi);
   fChain->SetBranchAddress("allstub_x", &allstub_x, &b_allstub_x);
   fChain->SetBranchAddress("allstub_y", &allstub_y, &b_allstub_y);
   fChain->SetBranchAddress("allstub_z", &allstub_z, &b_allstub_z);
   fChain->SetBranchAddress("allstub_isBarrel", &allstub_isBarrel, &b_allstub_isBarrel);
   fChain->SetBranchAddress("allstub_layer", &allstub_layer, &b_allstub_layer);
   fChain->SetBranchAddress("allstub_isPSmodule", &allstub_isPSmodule, &b_allstub_isPSmodule);
   fChain->SetBranchAddress("allstub_trigDisplace", &allstub_trigDisplace, &b_allstub_trigDisplace);
   fChain->SetBranchAddress("allstub_trigOffset", &allstub_trigOffset, &b_allstub_trigOffset);
   fChain->SetBranchAddress("allstub_trigPos", &allstub_trigPos, &b_allstub_trigPos);
   fChain->SetBranchAddress("allstub_trigBend", &allstub_trigBend, &b_allstub_trigBend);
   fChain->SetBranchAddress("allstub_matchTP_pdgid", &allstub_matchTP_pdgid, &b_allstub_matchTP_pdgid);
   fChain->SetBranchAddress("allstub_matchTP_pt", &allstub_matchTP_pt, &b_allstub_matchTP_pt);
   fChain->SetBranchAddress("allstub_matchTP_eta", &allstub_matchTP_eta, &b_allstub_matchTP_eta);
   fChain->SetBranchAddress("allstub_matchTP_phi", &allstub_matchTP_phi, &b_allstub_matchTP_phi);
   fChain->SetBranchAddress("allstub_genuine", &allstub_genuine, &b_allstub_genuine);
   fChain->SetBranchAddress("allstub_isCombinatoric", &allstub_isCombinatoric, &b_allstub_isCombinatoric);
   fChain->SetBranchAddress("allstub_isUnknown", &allstub_isUnknown, &b_allstub_isUnknown);
   fChain->SetBranchAddress("allstub_chip", &allstub_chip, &b_allstub_chip);
   fChain->SetBranchAddress("allstub_seg", &allstub_seg, &b_allstub_seg);
   fChain->SetBranchAddress("allstub_ladder", &allstub_ladder, &b_allstub_ladder);
   fChain->SetBranchAddress("allstub_module", &allstub_module, &b_allstub_module);
   fChain->SetBranchAddress("allstub_type", &allstub_type, &b_allstub_type);
   fChain->SetBranchAddress("allstub_module_x", &allstub_module_x, &b_allstub_module_x);
   fChain->SetBranchAddress("allstub_module_y", &allstub_module_y, &b_allstub_module_y);
   fChain->SetBranchAddress("allstub_module_z", &allstub_module_z, &b_allstub_module_z);
   fChain->SetBranchAddress("allstub_fromPU", &allstub_fromPU, &b_allstub_fromPU);
   fChain->SetBranchAddress("jet_eta", &jet_eta, &b_jet_eta);
   fChain->SetBranchAddress("jet_phi", &jet_phi, &b_jet_phi);
   fChain->SetBranchAddress("jet_pt", &jet_pt, &b_jet_pt);
   fChain->SetBranchAddress("jet_tp_sumpt", &jet_tp_sumpt, &b_jet_tp_sumpt);
   fChain->SetBranchAddress("jet_trk_sumpt", &jet_trk_sumpt, &b_jet_trk_sumpt);
   fChain->SetBranchAddress("jet_matchtrk_sumpt", &jet_matchtrk_sumpt, &b_jet_matchtrk_sumpt);
   fChain->SetBranchAddress("jet_loosematchtrk_sumpt", &jet_loosematchtrk_sumpt, &b_jet_loosematchtrk_sumpt);
   Notify();
}

Bool_t MyAnalysis::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void MyAnalysis::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t MyAnalysis::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef MyAnalysis_cxx
