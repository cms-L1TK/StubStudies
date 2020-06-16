#define MyAnalysis_cxx
#include "MyAnalysis.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include "TRandom.h"
#include "TRandom3.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TRandom3.h>
#include <TLorentzVector.h>
#include <time.h>
#include <iostream>
#include <cmath>
#include <vector>

void displayProgress(long current, long max){
  using std::cerr;
  if (max<1000) return;
  if (current%(max/1000)!=0 && current<max-1) return;

  int width = 52; // Hope the terminal is at least that wide.
  int barWidth = width - 2;
  cerr << "\x1B[2K"; // Clear line
  cerr << "\x1B[2000D"; // Cursor left
  cerr << '[';
  for(int i=0 ; i<barWidth ; ++i){ if(i<barWidth*current/max){ cerr << '=' ; }else{ cerr << ' ' ; } }
  cerr << ']';
  cerr << " " << Form("%8d/%8d (%5.2f%%)", (int)current, (int)max, 100.0*current/max) ;
  cerr.flush();
}



void MyAnalysis::Loop(TString fname, float Nin, TString pname)
{

//Stub Rate **************************************************************************************************


  typedef vector<float> Dim1;
  typedef vector<Dim1> Dim2;
  typedef vector<Dim2> Dim3;
  typedef vector<Dim3> Dim4;
  typedef vector<Dim4> Dim5;
  typedef vector<Dim5> Dim6;

  Dim4 stubsRate(2,Dim3(6,Dim2(100,Dim1(100))));
  Dim4 stubsRateGenuine(2,Dim3(6,Dim2(100,Dim1(100))));
  Dim4 stubsRateCombinatoric(2,Dim3(6,Dim2(100,Dim1(100))));
  Dim4 stubsRateUnknown(2,Dim3(6,Dim2(100,Dim1(100))));
  Dim4 stubsRateCBCfail(2,Dim3(6,Dim2(100,Dim1(100))));
  Dim4 stubsRateGenuineCBCfail(2,Dim3(6,Dim2(100,Dim1(100))));
  Dim4 stubsRateCombinatoricCBCfail(2,Dim3(6,Dim2(100,Dim1(100))));
  Dim4 stubsRateUnknownCBCfail(2,Dim3(6,Dim2(100,Dim1(100))));
  Dim4 stubsRateCICfail(2,Dim3(6,Dim2(100,Dim1(100))));
  Dim4 stubsRateGenuineCICfail(2,Dim3(6,Dim2(100,Dim1(100))));
  Dim4 stubsRateCombinatoricCICfail(2,Dim3(6,Dim2(100,Dim1(100))));
  Dim4 stubsRateUnknownCICfail(2,Dim3(6,Dim2(100,Dim1(100))));
  Dim4 tmpstubsRate(2,Dim3(6,Dim2(100,Dim1(100))));
  Dim4 stubsRate_z(2,Dim3(6,Dim2(100,Dim1(100))));
  Dim4 stubsRate_rho(2,Dim3(6,Dim2(100,Dim1(100))));
  Dim4 stubsRate_eta(2,Dim3(6,Dim2(100,Dim1(100))));

  for (int i=0;i<2;++i){
    for (int k=0;k<6;++k){
      for (int l=0;l<100;++l){
        for (int m=0;m<100;++m){
             stubsRate[i][k][l][m] = 0;
             stubsRateGenuine[i][k][l][m] = 0;
             stubsRateCombinatoric[i][k][l][m] = 0;
             stubsRateUnknown[i][k][l][m] = 0;
             stubsRateCBCfail[i][k][l][m] = 0;
             stubsRateGenuineCBCfail[i][k][l][m] = 0;
             stubsRateCombinatoricCBCfail[i][k][l][m] = 0;
             stubsRateUnknownCBCfail[i][k][l][m] = 0;
             stubsRateCICfail[i][k][l][m] = 0;
             stubsRateGenuineCICfail[i][k][l][m] = 0;
             stubsRateCombinatoricCICfail[i][k][l][m] = 0;
             stubsRateUnknownCICfail[i][k][l][m] = 0;
             tmpstubsRate[i][k][l][m] = 0;
             stubsRate_z[i][k][l][m] = 0;
             stubsRate_rho[i][k][l][m] = 0;
             stubsRate_eta[i][k][l][m] = 0;
         }
      }
    }
  }

  std::vector<TString> regions{"Endcap","Barrel"};
  std::vector<TString> layers{"1","2","3","4","5","6"};
  std::vector<TString> channels{"PBX", "PBXPmodule", "PBXCBCfail","PBXCICfail"};
  std::vector<TString> vars   {"eta","type","z","rho","nstub"};
  std::vector<int>    nbins   {30   ,4     ,40     ,40      ,30};
  std::vector<float> lowEdge  {-3   ,0     ,-300   ,0       ,0 };
  std::vector<float> highEdge {3    ,4     ,300    ,120     ,30};

  typedef vector<TH1F*> TH1Dim1;
  typedef vector<TH1Dim1> TH1Dim2;
  typedef vector<TH1Dim2> TH1Dim3;
  typedef vector<TH1Dim3> TH1Dim4;

  TH1Dim4 Hists(regions.size(),TH1Dim3(layers.size(),TH1Dim2(channels.size(),TH1Dim1(vars.size()))));
  std::stringstream name;
  TH1F *h_test;
  for (int i=0;i<regions.size();++i){
    for (int j=0;j<layers.size();++j){
      for (int k=0;k<channels.size();++k){
        for (int l=0;l<vars.size();++l){
        name<<regions[i]<<"_"<<vars[l]<<"_"<<layers[j]<<"_"<<channels[k];
        h_test = new TH1F((name.str()).c_str(),(name.str()).c_str(),nbins[l],lowEdge[l],highEdge[l]);
        h_test->StatOverflows(kTRUE);
        h_test->Sumw2(kTRUE);
        Hists[i][j][k][l] = h_test;
        name.str("");
        }
      }
    }
  }

  TH1Dim3 HistsPmodule(regions.size(),TH1Dim2(layers.size(),TH1Dim1(vars.size())));
  for (int i=0;i<regions.size();++i){
    for (int j=0;j<layers.size();++j){
      for (int l=0;l<vars.size();++l){
      name<<"Pmodule_"<<regions[i]<<"_"<<layers[j]<<"_"<<vars[l];
      h_test = new TH1F((name.str()).c_str(),(name.str()).c_str(),nbins[l],lowEdge[l],highEdge[l]);
      h_test->StatOverflows(kTRUE);
      h_test->Sumw2(kTRUE);
      HistsPmodule[i][j][l] = h_test;
      name.str("");
      }
    }
  }

  std::vector<TString> channelsEff{"Stub", "Cluster"};
  std::vector<TString> varsEff   {"eta","pt"};
  std::vector<int>    nbinsEff   {20   , 50};
  std::vector<float> lowEdgeEff  {0   ,0  };
  std::vector<float> highEdgeEff {4   ,10 };
  TH1Dim4 HistsEff(regions.size(),TH1Dim3(layers.size(),TH1Dim2(channelsEff.size(),TH1Dim1(varsEff.size()))));
  for (int i=0;i<regions.size();++i){
    for (int j=0;j<layers.size();++j){
      for (int k=0;k<channelsEff.size();++k){
        for (int l=0;l<varsEff.size();++l){
        name<<regions[i]<<"_"<<varsEff[l]<<"_"<<layers[j]<<"_"<<channelsEff[k];
        h_test = new TH1F((name.str()).c_str(),(name.str()).c_str(),nbinsEff[l],lowEdgeEff[l],highEdgeEff[l]);
        h_test->StatOverflows(kTRUE);
        h_test->Sumw2(kTRUE);
        HistsEff[i][j][k][l] = h_test;
        name.str("");
        }
      }
    }
  }


  std::vector<TString> TPvars   {"eta","pt","nstub","dxy","d0","d0_prod","z0","z0_prod"};
  std::vector<int>    TPnbins   {30   ,20  ,15     ,100  , 50 ,50       ,150 , 150};
  std::vector<float> TPlowEdge  {-3   ,0   ,0      ,0    ,-100,-60      ,-1000,-600};
  std::vector<float> TPhighEdge {3    ,10  ,15     ,300  ,100 ,60       ,1000,600};
  TH1Dim1 TPHists(TPvars.size());
  for (int l=0;l<TPvars.size();++l){
    name<<"TP_"<<TPvars[l];
    h_test = new TH1F((name.str()).c_str(),(name.str()).c_str(),TPnbins[l],TPlowEdge[l],TPhighEdge[l]);
    h_test->StatOverflows(kTRUE);
    h_test->Sumw2(kTRUE);
    TPHists[l] = h_test;
    name.str("");
  }

  if (fChain == 0) return;
  int pid = 0;
  if (pname == "mu") pid = 13;
  if (pname == "ele") pid = 11;
  if (pname == "pion") pid = 211;
  Int_t nentries = (Int_t) fChain->GetEntries();
  float N = Nin;
  Long64_t nbytes = 0, nb = 0;
  TVector3 sEta;
  TVector3 mEta;
  int ch = 0;
  cout<<"N events="<<N<<endl;
  for (Long64_t jentry=0; jentry<nentries;jentry++) {
    Long64_t ientry = LoadTree(jentry);
    if (ientry < 0) break;
    nb = fChain->GetEntry(jentry);   nbytes += nb;
    displayProgress(jentry, nentries) ;
    for (unsigned int k=0; k<allstub_x->size(); ++k) {
      //only look at the z+ Disks
      if (!allstub_isBarrel->at(k) && allstub_module_z->at(k) <0) continue;
      sEta.SetXYZ(allstub_x->at(k),allstub_y->at(k),allstub_z->at(k));
      mEta.SetXYZ(allstub_module_x->at(k),allstub_module_y->at(k),allstub_module_z->at(k));
      stubsRate[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)]++;
      if(allstub_genuine->at(k)) stubsRateGenuine[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)]++;
      if(allstub_isCombinatoric->at(k)) stubsRateCombinatoric[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)]++;
      if (allstub_isUnknown->at(k)) stubsRateUnknown[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)]++;
      tmpstubsRate[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)]++;
      if (allstub_trigDisplace->at(k)>200 && allstub_trigDisplace->at(k)<300) {
        stubsRateCBCfail[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)]++;
        if(allstub_genuine->at(k)) stubsRateGenuineCBCfail[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)]++;
        if(allstub_isCombinatoric->at(k)) stubsRateCombinatoricCBCfail[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)]++;
        if (allstub_isUnknown->at(k)) stubsRateUnknownCBCfail[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)]++;
      }
      if (allstub_trigDisplace->at(k)>400) {
        stubsRateCICfail[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)]++;
        if(allstub_genuine->at(k)) stubsRateGenuineCICfail[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)]++;
        if(allstub_isCombinatoric->at(k)) stubsRateCombinatoricCICfail[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)]++;
        if (allstub_isUnknown->at(k)) stubsRateUnknownCICfail[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)]++;
      }
      stubsRate_z[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)] = allstub_module_z->at(k);
      stubsRate_rho[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)] = sqrt(pow(allstub_module_x->at(k),2) + pow(allstub_module_y->at(k),2)) ;
      stubsRate_eta[allstub_isBarrel->at(k)][allstub_layer->at(k)-1][allstub_ladder->at(k)-1][allstub_module->at(k)] = mEta.Eta() ;
    }
    for (unsigned int k=0; k<tp_pt->size(); ++k) {
      TPHists[0]->Fill(tp_eta->at(k), 1/N);
      TPHists[1]->Fill(tp_pt->at(k), 1/N);
      TPHists[2]->Fill(tp_nstub->at(k), 1/N);
      TPHists[3]->Fill(tp_dxy->at(k), 1/N);
      TPHists[4]->Fill(tp_d0->at(k), 1/N);
      TPHists[5]->Fill(tp_d0_prod->at(k), 1/N);
      TPHists[6]->Fill(tp_z0->at(k), 1/N);
      TPHists[7]->Fill(tp_z0_prod->at(k), 1/N);
    }


//find efficiency     
    for (unsigned int k=0; k<stubEff_tp_pt->size(); ++k) {
      if(abs(stubEff_tp_pdgid->at(k))!=pid) continue;
      HistsEff[1][0][0][0]->Fill(abs(stubEff_tp_eta->at(k)),float(stubEff_BL1->at(k)));
      HistsEff[1][1][0][0]->Fill(abs(stubEff_tp_eta->at(k)),float(stubEff_BL2->at(k)));
      HistsEff[1][2][0][0]->Fill(abs(stubEff_tp_eta->at(k)),float(stubEff_BL3->at(k)));
      HistsEff[1][3][0][0]->Fill(abs(stubEff_tp_eta->at(k)),float(stubEff_BL4->at(k)));
      HistsEff[1][4][0][0]->Fill(abs(stubEff_tp_eta->at(k)),float(stubEff_BL5->at(k)));
      HistsEff[1][5][0][0]->Fill(abs(stubEff_tp_eta->at(k)),float(stubEff_BL6->at(k)));
   
      HistsEff[0][0][0][0]->Fill(abs(stubEff_tp_eta->at(k)),float(stubEff_EL1->at(k)));
      HistsEff[0][1][0][0]->Fill(abs(stubEff_tp_eta->at(k)),float(stubEff_EL2->at(k)));
      HistsEff[0][2][0][0]->Fill(abs(stubEff_tp_eta->at(k)),float(stubEff_EL3->at(k)));
      HistsEff[0][3][0][0]->Fill(abs(stubEff_tp_eta->at(k)),float(stubEff_EL4->at(k)));
      HistsEff[0][4][0][0]->Fill(abs(stubEff_tp_eta->at(k)),float(stubEff_EL5->at(k)));
   
      HistsEff[1][0][1][0]->Fill(abs(stubEff_tp_eta->at(k)),float(clustEff_BL1->at(k)));
      HistsEff[1][1][1][0]->Fill(abs(stubEff_tp_eta->at(k)),float(clustEff_BL2->at(k)));
      HistsEff[1][2][1][0]->Fill(abs(stubEff_tp_eta->at(k)),float(clustEff_BL3->at(k)));
      HistsEff[1][3][1][0]->Fill(abs(stubEff_tp_eta->at(k)),float(clustEff_BL4->at(k)));
      HistsEff[1][4][1][0]->Fill(abs(stubEff_tp_eta->at(k)),float(clustEff_BL5->at(k)));
      HistsEff[1][5][1][0]->Fill(abs(stubEff_tp_eta->at(k)),float(clustEff_BL6->at(k)));
   
      HistsEff[0][0][1][0]->Fill(abs(stubEff_tp_eta->at(k)),float(clustEff_EL1->at(k)));
      HistsEff[0][1][1][0]->Fill(abs(stubEff_tp_eta->at(k)),float(clustEff_EL2->at(k)));
      HistsEff[0][2][1][0]->Fill(abs(stubEff_tp_eta->at(k)),float(clustEff_EL3->at(k)));
      HistsEff[0][3][1][0]->Fill(abs(stubEff_tp_eta->at(k)),float(clustEff_EL4->at(k)));
      HistsEff[0][4][1][0]->Fill(abs(stubEff_tp_eta->at(k)),float(clustEff_EL5->at(k)));
      if(abs(stubEff_tp_eta->at(k)) < 0.6){
        HistsEff[1][0][0][1]->Fill(abs(stubEff_tp_pt->at(k)),float(stubEff_BL1->at(k)));
        HistsEff[1][1][0][1]->Fill(abs(stubEff_tp_pt->at(k)),float(stubEff_BL2->at(k)));
        HistsEff[1][2][0][1]->Fill(abs(stubEff_tp_pt->at(k)),float(stubEff_BL3->at(k)));
        HistsEff[1][3][0][1]->Fill(abs(stubEff_tp_pt->at(k)),float(stubEff_BL4->at(k)));
        HistsEff[1][4][0][1]->Fill(abs(stubEff_tp_pt->at(k)),float(stubEff_BL5->at(k)));
        HistsEff[1][5][0][1]->Fill(abs(stubEff_tp_pt->at(k)),float(stubEff_BL6->at(k)));
  
        HistsEff[1][0][1][1]->Fill(abs(stubEff_tp_pt->at(k)),float(clustEff_BL1->at(k)));
        HistsEff[1][1][1][1]->Fill(abs(stubEff_tp_pt->at(k)),float(clustEff_BL2->at(k)));
        HistsEff[1][2][1][1]->Fill(abs(stubEff_tp_pt->at(k)),float(clustEff_BL3->at(k)));
        HistsEff[1][3][1][1]->Fill(abs(stubEff_tp_pt->at(k)),float(clustEff_BL4->at(k)));
        HistsEff[1][4][1][1]->Fill(abs(stubEff_tp_pt->at(k)),float(clustEff_BL5->at(k)));
        HistsEff[1][5][1][1]->Fill(abs(stubEff_tp_pt->at(k)),float(clustEff_BL6->at(k)));
      }
      if(abs(stubEff_tp_eta->at(k)) > 1.2 && abs(stubEff_tp_eta->at(k))<2.4) {
        HistsEff[0][0][0][1]->Fill(abs(stubEff_tp_pt->at(k)),float(stubEff_EL1->at(k)));
        HistsEff[0][1][0][1]->Fill(abs(stubEff_tp_pt->at(k)),float(stubEff_EL2->at(k)));
        HistsEff[0][2][0][1]->Fill(abs(stubEff_tp_pt->at(k)),float(stubEff_EL3->at(k)));
        HistsEff[0][3][0][1]->Fill(abs(stubEff_tp_pt->at(k)),float(stubEff_EL4->at(k)));
        HistsEff[0][4][0][1]->Fill(abs(stubEff_tp_pt->at(k)),float(stubEff_EL5->at(k)));
    
        HistsEff[0][0][1][1]->Fill(abs(stubEff_tp_pt->at(k)),float(clustEff_EL1->at(k)));
        HistsEff[0][1][1][1]->Fill(abs(stubEff_tp_pt->at(k)),float(clustEff_EL2->at(k)));
        HistsEff[0][2][1][1]->Fill(abs(stubEff_tp_pt->at(k)),float(clustEff_EL3->at(k)));
        HistsEff[0][3][1][1]->Fill(abs(stubEff_tp_pt->at(k)),float(clustEff_EL4->at(k)));
        HistsEff[0][4][1][1]->Fill(abs(stubEff_tp_pt->at(k)),float(clustEff_EL5->at(k)));
      }
    }
  }

  for (int j=0;j<regions.size();++j){
    for (int k=0;k<layers.size();++k){
      for (int l=0;l<100;++l){
        for (int m=0;m<100;++m){
          Hists[j][k][0][0] ->Fill(stubsRate_eta[j][k][l][m], float(stubsRate[j][k][l][m])/N);
          Hists[j][k][0][1] ->Fill(0.5  , float(stubsRate[j][k][l][m])/N);
          Hists[j][k][0][1] ->Fill(1.5  , float(stubsRateGenuine[j][k][l][m])/N);
          Hists[j][k][0][1] ->Fill(2.5  , float(stubsRateCombinatoric[j][k][l][m])/N);
          Hists[j][k][0][1] ->Fill(3.5  , float(stubsRateUnknown[j][k][l][m])/N);
          Hists[j][k][0][2] ->Fill(stubsRate_z[j][k][l][m], float(stubsRate[j][k][l][m])/N);
          Hists[j][k][0][3] ->Fill(stubsRate_rho[j][k][l][m], float(stubsRate[j][k][l][m])/N);
          if(stubsRate_rho[j][k][l][m]>0) Hists[j][k][0][4] ->Fill(stubsRate[j][k][l][m]);

          Hists[j][k][1][0] ->Fill(stubsRate_eta[j][k][l][m], float(stubsRate[j][k][l][m])/N);
          Hists[j][k][1][1] ->Fill(0.5  , float(stubsRate[j][k][l][m])/N);
          Hists[j][k][1][1] ->Fill(1.5  , float(stubsRateGenuine[j][k][l][m])/N);
          Hists[j][k][1][1] ->Fill(2.5  , float(stubsRateCombinatoric[j][k][l][m])/N);
          Hists[j][k][1][1] ->Fill(3.5  , float(stubsRateUnknown[j][k][l][m])/N);
          Hists[j][k][1][2] ->Fill(stubsRate_z[j][k][l][m], float(stubsRate[j][k][l][m])/N);
          Hists[j][k][1][3] ->Fill(stubsRate_rho[j][k][l][m], float(stubsRate[j][k][l][m])/N);

          Hists[j][k][2][0] ->Fill(stubsRate_eta[j][k][l][m], float(stubsRateCBCfail[j][k][l][m])/N);
          Hists[j][k][2][1] ->Fill(0.5  , float(stubsRateCBCfail[j][k][l][m])/N);
          Hists[j][k][2][1] ->Fill(1.5  , float(stubsRateGenuineCBCfail[j][k][l][m])/N);
          Hists[j][k][2][1] ->Fill(2.5  , float(stubsRateCombinatoricCBCfail[j][k][l][m])/N);
          Hists[j][k][2][1] ->Fill(3.5  , float(stubsRateUnknownCBCfail[j][k][l][m])/N);
          Hists[j][k][2][2] ->Fill(stubsRate_z[j][k][l][m], float(stubsRateCBCfail[j][k][l][m])/N);
          Hists[j][k][2][3] ->Fill(stubsRate_rho[j][k][l][m], float(stubsRateCBCfail[j][k][l][m])/N);
          if(stubsRate_rho[j][k][l][m]>0) Hists[j][k][2][4] ->Fill(stubsRateCBCfail[j][k][l][m]);

          Hists[j][k][3][0] ->Fill(stubsRate_eta[j][k][l][m], float(stubsRateCICfail[j][k][l][m])/N);
          Hists[j][k][3][1] ->Fill(0.5  , float(stubsRateCICfail[j][k][l][m])/N);
          Hists[j][k][3][1] ->Fill(1.5  , float(stubsRateGenuineCICfail[j][k][l][m])/N);
          Hists[j][k][3][1] ->Fill(2.5  , float(stubsRateCombinatoricCICfail[j][k][l][m])/N);
          Hists[j][k][3][1] ->Fill(3.5  , float(stubsRateUnknownCICfail[j][k][l][m])/N);
          Hists[j][k][3][2] ->Fill(stubsRate_z[j][k][l][m], float(stubsRateCICfail[j][k][l][m])/N);
          Hists[j][k][3][3] ->Fill(stubsRate_rho[j][k][l][m], float(stubsRateCICfail[j][k][l][m])/N);
          if(stubsRate_rho[j][k][l][m]>0) Hists[j][k][3][4] ->Fill(stubsRateCICfail[j][k][l][m]);

          if(stubsRate_rho[j][k][l][m]>0){
            HistsPmodule[j][k][0] ->Fill(stubsRate_eta[j][k][l][m]);
            HistsPmodule[j][k][1] ->Fill(0.5);
            HistsPmodule[j][k][1] ->Fill(1.5);
            HistsPmodule[j][k][1] ->Fill(2.5);
            HistsPmodule[j][k][1] ->Fill(3.5);
            HistsPmodule[j][k][2] ->Fill(stubsRate_z[j][k][l][m]);
            HistsPmodule[j][k][3] ->Fill(stubsRate_rho[j][k][l][m]);
          }
        }
      }
    }
  }

  for (int j=0;j<regions.size();++j){
    for (int k=0;k<layers.size();++k){
      for (int l=0;l<vars.size()-1;++l){
        Hists[j][k][1][l]->Divide(HistsPmodule[j][k][l]);
      }
    }
  }

  TFile file_out (fname,"RECREATE");

  for (int i=0;i<regions.size();++i){
    for (int j=0;j<layers.size();++j){
      for (int k=0;k<channels.size();++k){
        for (int l=0;l<vars.size();++l){
        Hists[i][j][k][l] ->Write("",TObject::kOverwrite);
        }
      }
    }
  }

  for (int i=0;i<regions.size();++i){
    for (int j=0;j<layers.size();++j){
      for (int k=0;k<channelsEff.size();++k){
        for (int l=0;l<varsEff.size();++l){
        HistsEff[i][j][k][l]->Write("",TObject::kOverwrite);
        }
      }
    }
  }
//two dimensional plots
  std::vector<TH2D*> Barrel_2D;
  std::vector<TH2D*> Barrel_2DCBCfail;
  std::vector<TH2D*> Barrel_2DCICfail;
  std::vector<TH2D*> Endcap_2D;
  std::vector<TH2D*> Endcap_2DCBCfail;
  std::vector<TH2D*> Endcap_2DCICfail;
   Int_t n_lad_barrel[6] = {18,26,36,48,60,78};
   Int_t n_mod_barrel[6] = {31,35,39,24,24,24};
   Int_t n_lad_endcapF[15] = {20,24,24,28,32,32,36,40,40,44,52,60,64,72,76};
   Int_t n_lad_endcapL[15] = {28,28,32,36,36,40,44,52,56,64,72,76,100,100,100};

   TH2D *BL, *BLCBCfail, *BLCICfail;
   TH2D *EL, *ELCBCfail, *ELCICfail;

  for (int k=0;k<6;++k){
    name.str("");
    name<<"Barrel_Rate2D_"<<k<<"_PBX";
    BL = new TH2D((name.str()).c_str(),(name.str()).c_str(),n_mod_barrel[k],0,n_mod_barrel[k], n_lad_barrel[k],0,n_lad_barrel[k]);
    name.str("");
    name<<"Barrel_Rate2D_"<<k<<"_PBXCBCfail";
    BLCBCfail = new TH2D((name.str()).c_str(),(name.str()).c_str(),n_mod_barrel[k],0,n_mod_barrel[k], n_lad_barrel[k],0,n_lad_barrel[k]);
    name.str("");
    name<<"Barrel_Rate2D_"<<k<<"_PBXCICfail";
    BLCICfail = new TH2D((name.str()).c_str(),(name.str()).c_str(),n_mod_barrel[k],0,n_mod_barrel[k], n_lad_barrel[k],0,n_lad_barrel[k]);

    for (int l=0;l<100;++l){
      for (int m=0;m<100;++m){
        BL->SetBinContent(m+1,l+1, float(stubsRate[1][k][l][m])/float(nentries));
        if(stubsRate[1][k][l][m]>0) BLCBCfail->SetBinContent(m+1,l+1, float(stubsRateCBCfail[1][k][l][m])/float(stubsRate[1][k][l][m]));
        if(stubsRate[1][k][l][m]>0) BLCICfail->SetBinContent(m+1,l+1, float(stubsRateCICfail[1][k][l][m])/float(stubsRate[1][k][l][m]));
      }
    }
    Barrel_2D.push_back(BL);
    Barrel_2DCBCfail.push_back(BLCBCfail);
    Barrel_2DCICfail.push_back(BLCICfail);
  }
  for (int k=0;k<6;++k){
    Barrel_2D[k]          ->Write("",TObject::kOverwrite);
    Barrel_2DCBCfail[k]          ->Write("",TObject::kOverwrite);
    Barrel_2DCICfail[k]          ->Write("",TObject::kOverwrite);
  }

  for (int k=0;k<5;++k){
    int RING = 0;
    int nbins = 0;
    for (int l=0;l<15;++l){
       RING = l ;
       nbins =n_lad_endcapF[l];
       if (k>1) {
         RING = l + 3;
         nbins =n_lad_endcapL[l];
       }
    name.str("");
       name<<"Endcap_Rate2D_"<<k<<"_PBX_"<<l;
       EL = new TH2D((name.str()).c_str(),(name.str()).c_str(),nbins,0, 2*TMath::Pi(), 15,0,15);
       name.str("");
       name<<"Endcap_Rate2D_"<<k<<"_PBXCBCfail_"<<l;
       ELCBCfail = new TH2D((name.str()).c_str(),(name.str()).c_str(),nbins,0, 2*TMath::Pi(), 15,0,15);
       name.str("");
       name<<"Endcap_Rate2D_"<<k<<"_PBXCICfail_"<<l;
       ELCICfail = new TH2D((name.str()).c_str(),(name.str()).c_str(),nbins,0, 2*TMath::Pi(), 15,0,15);

      for (int m=0;m<100;++m){
        EL->SetBinContent(m+1,RING+1, float(stubsRate[0][k][l][m])/float(nentries));
        if(stubsRate[0][k][l][m]>0) ELCBCfail->SetBinContent(m+1,RING+1, float(stubsRateCBCfail[0][k][l][m])/float(stubsRate[0][k][l][m]));
        if(stubsRate[0][k][l][m]>0) ELCICfail->SetBinContent(m+1,RING+1, float(stubsRateCICfail[0][k][l][m])/float(stubsRate[0][k][l][m]));
      }
      Endcap_2D.push_back(EL);
      Endcap_2DCBCfail.push_back(ELCBCfail);
      Endcap_2DCICfail.push_back(ELCICfail);
    }
  }

  for (int k=0;k<Endcap_2D.size();++k){
    Endcap_2D[k]               ->Write("",TObject::kOverwrite);
    Endcap_2DCBCfail[k]               ->Write("",TObject::kOverwrite);
    Endcap_2DCICfail[k]               ->Write("",TObject::kOverwrite);
  }
  for (int k=0;k<TPHists.size();++k){
    TPHists[k]->Write("",TObject::kOverwrite);
  }
}
