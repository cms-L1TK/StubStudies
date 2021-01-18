//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Wed Aug 12 04:00:07 2020 by ROOT version 6.12/07
// from TTree eventTree/Event tree
// found on file: Sele.root
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
   vector<int>     *tp_nstub;
   vector<int>     *tp_eventid;
   vector<int>     *tp_charge;
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
   vector<int>     *stubEff_clu_isBarrel;
   vector<int>     *stubEff_clu_ladder;
   vector<int>     *stubEff_clu_module;
   vector<int>     *stubEff_clu_layer;
   vector<float>   *stubEff_clu_x;
   vector<float>   *stubEff_clu_y;
   vector<float>   *stubEff_clu_z;
   vector<int>     *stubEff_clu_isStub;
   vector<float>   *stubEff_tp_pt;
   vector<int>     *stubEff_tp_pdgid;
   vector<float>   *stubEff_tp_eta;
   vector<float>   *stubEff_tp_phi;
   vector<float>   *stubEff_tp_dz;
   vector<float>   *stubEff_tp_d0;
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
   TBranch        *b_tp_nstub;   //!
   TBranch        *b_tp_eventid;   //!
   TBranch        *b_tp_charge;   //!
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
   TBranch        *b_stubEff_clu_isBarrel;   //!
   TBranch        *b_stubEff_clu_ladder;   //!
   TBranch        *b_stubEff_clu_module;   //!
   TBranch        *b_stubEff_clu_layer;   //!
   TBranch        *b_stubEff_clu_x;   //!
   TBranch        *b_stubEff_clu_y;   //!
   TBranch        *b_stubEff_clu_z;   //!
   TBranch        *b_stubEff_clu_isStub;   //!
   TBranch        *b_stubEff_tp_pt;   //!
   TBranch        *b_stubEff_tp_pdgid;   //!
   TBranch        *b_stubEff_tp_eta;   //!
   TBranch        *b_stubEff_tp_phi;   //!
   TBranch        *b_stubEff_tp_dz;   //!
   TBranch        *b_stubEff_tp_d0;   //!
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
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("Sele.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("Sele.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("Sele.root:/L1TrackNtuple");
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
   tp_nstub = 0;
   tp_eventid = 0;
   tp_charge = 0;
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
   stubEff_clu_isBarrel = 0;
   stubEff_clu_ladder = 0;
   stubEff_clu_module = 0;
   stubEff_clu_layer = 0;
   stubEff_clu_x = 0;
   stubEff_clu_y = 0;
   stubEff_clu_z = 0;
   stubEff_clu_isStub = 0;
   stubEff_tp_pt = 0;
   stubEff_tp_pdgid = 0;
   stubEff_tp_eta = 0;
   stubEff_tp_phi = 0;
   stubEff_tp_dz = 0;
   stubEff_tp_d0 = 0;
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
   fChain->SetBranchAddress("tp_nstub", &tp_nstub, &b_tp_nstub);
   fChain->SetBranchAddress("tp_eventid", &tp_eventid, &b_tp_eventid);
   fChain->SetBranchAddress("tp_charge", &tp_charge, &b_tp_charge);
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
   fChain->SetBranchAddress("stubEff_clu_isBarrel", &stubEff_clu_isBarrel, &b_stubEff_clu_isBarrel);
   fChain->SetBranchAddress("stubEff_clu_ladder", &stubEff_clu_ladder, &b_stubEff_clu_ladder);
   fChain->SetBranchAddress("stubEff_clu_module", &stubEff_clu_module, &b_stubEff_clu_module);
   fChain->SetBranchAddress("stubEff_clu_layer", &stubEff_clu_layer, &b_stubEff_clu_layer);
   fChain->SetBranchAddress("stubEff_clu_x", &stubEff_clu_x, &b_stubEff_clu_x);
   fChain->SetBranchAddress("stubEff_clu_y", &stubEff_clu_y, &b_stubEff_clu_y);
   fChain->SetBranchAddress("stubEff_clu_z", &stubEff_clu_z, &b_stubEff_clu_z);
   fChain->SetBranchAddress("stubEff_clu_isStub", &stubEff_clu_isStub, &b_stubEff_clu_isStub);
   fChain->SetBranchAddress("stubEff_tp_pt", &stubEff_tp_pt, &b_stubEff_tp_pt);
   fChain->SetBranchAddress("stubEff_tp_pdgid", &stubEff_tp_pdgid, &b_stubEff_tp_pdgid);
   fChain->SetBranchAddress("stubEff_tp_eta", &stubEff_tp_eta, &b_stubEff_tp_eta);
   fChain->SetBranchAddress("stubEff_tp_phi", &stubEff_tp_phi, &b_stubEff_tp_phi);
   fChain->SetBranchAddress("stubEff_tp_dz", &stubEff_tp_dz, &b_stubEff_tp_dz);
   fChain->SetBranchAddress("stubEff_tp_d0", &stubEff_tp_d0, &b_stubEff_tp_d0);
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
