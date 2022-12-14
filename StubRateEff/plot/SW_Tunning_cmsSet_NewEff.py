import math
import gc
import sys
import ROOT
import numpy as npi
import copy
from array import array
import os
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gROOT.ProcessLine("gErrorIgnoreLevel = 1;")
ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gStyle.SetOptStat(0)
from ROOT import TColor
from ROOT import TGaxis
import gc
#TGaxis.SetMaxDigits(2)
################################## MY SIGNAL AND SM BG ################################

def most_frequent(List): 
    return max(set(List), key = List.count) 

def drawHistperW(A,AN, R, I):
    rate = A[0].Clone()
    Num = A[0].Integral()
    if A[0].Integral()>0:
        rate.Scale(1/A[0].Integral())
    canvas = ROOT.TCanvas(R+I,R+I,10,10,1100,628)
    canvas.cd()

    pad_name = "pad"
    pad1=ROOT.TPad(pad_name, pad_name, 0, 0, 1, 1 , 0)
    pad1.Draw()
    pad1.cd()
#    pad1.SetLogy()
    rate.SetTitle(R + '      L/D'+I)
    rate.GetXaxis().SetTitle('Z/R')
    rate.GetYaxis().SetTitle('X')
    rate.SetMarkerStyle(25);
    A[1].SetMarkerStyle(20);
    A[2].SetMarkerStyle(21);
    A[3].SetMarkerStyle(22);
    A[4].SetMarkerStyle(23);
    
    rate.SetMarkerColor(2);
    A[1].SetMarkerColor(3);
    A[2].SetMarkerColor(4);
    A[3].SetMarkerColor(1);
    A[4].SetMarkerColor(6);

    rate.SetMinimum(0);
    rate.SetMaximum(1);

    rate.Draw("p HIST SAME")
    A[1].Draw("p HIST SAME")
    A[2].Draw("p HIST SAME")
    A[3].Draw("p HIST SAME")
    A[4].Draw("p HIST SAME")

    leg = ROOT.TLegend(0.73,0.6,1,0.88)
    leg.AddEntry(rate, AN[0] + ' * ' + str(round(Num,1))        , "p");
    leg.AddEntry(A[1], AN[1]                           , "p");
    leg.AddEntry(A[2], AN[2]                           , "p");
    leg.AddEntry(A[3], AN[3]                           , "p");
    leg.AddEntry(A[4], AN[4]                           , "p");

    leg.SetBorderSize(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.04)
    leg.Draw("same")

    if A[0].Integral()>0:
        canvas.Print("SW_"+R+"_"+I +".png")
    del canvas
    gc.collect()

def drawHistallW(A,AN, B, BN,R, I):
    canvas = ROOT.TCanvas(R+I,R+I,10,10,1100,628)
    canvas.cd()

    pad_name = "pad"
    pad1=ROOT.TPad(pad_name, pad_name, 0, 0, 1, 1 , 0)
    pad1.Draw()
    pad1.cd()
#    pad1.SetLogy()
    if 'Barrel' in R:
        A[0].SetTitle(R + ', Layer -'+I)
        A[0].GetXaxis().SetTitle('Module no. along z')
        A[0].GetYaxis().SetTitle('X')
    else:
        A[0].SetTitle(R + ', Disk -'+I)
        A[0].GetXaxis().SetTitle('module ring no.')
        A[0].GetYaxis().SetTitle('X')

    maxi=A[0].GetMaximum()
    mini=A[0].GetMinimum()
    for i in range(len(A)):
        A[i].SetMarkerStyle(20+i);
        A[i].SetMarkerColor(1);

        if A[i].GetMaximum()>maxi:
            maxi=A[i].GetMaximum()
        if A[i].GetMinimum()<mini:
            mini=A[i].GetMinimum()
#        if i+4==10:
#            A[i].SetMarkerColor(28);

    maxi = maxi * 1.05
    if 'Efficiency' in R or 'Efficiency' in I:
        if 'Mu' in R or 'Mu' in I:
            mini=0.98
        if 'Ele' in R or 'Mu' in I:
            mini=0.90
    A[0].SetMinimum(mini)
#    A[0].SetMinimum(0.8*maxi)
    A[0].SetMaximum(maxi)
    for i in range(len(A)):
        A[i].Draw("p HIST SAME")

    leg = ROOT.TLegend(0.73,0.3,0.88,0.88)

    for i in range(len(A)):
        A[i].Draw("p HIST SAME")
        leg.AddEntry(A[i], AN[i]                           , "p");
    for i in range(len(B)):
        B[i].SetLineColor(2+i*2);
        B[i].SetLineWidth(2);
#        B[i].SetLineStyle(i+1);
        if i+1==1:
            B[i].SetLineColor(ROOT.kOrange);
##        B[i].SetLineStyle(i*2);
        B[i].Draw("HIST SAME")
        leg.AddEntry(B[i], BN[i]                           , "L");
#        if len(B)>1:
#            B[1].SetLineColor(4);
    leg.SetBorderSize(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.04)
    leg.Draw("same")

    if 'Barrel' in R and int(I)<4:
        tp = 19
        if I=='2':
            tp = 23
        if I=='3':
            tp = 27
        line1 = ROOT.TLine(12,mini,12,maxi);
        line1.Draw("same");
        line2 = ROOT.TLine(tp,mini,tp,maxi);
        line2.Draw("same");

        label_cms="Tilt-                  Flat                               Tilt+"
        Label_cms = ROOT.TLatex(0.15,0.85,label_cms)
        Label_cms.SetNDC()
        Label_cms.SetTextFont(61)
        Label_cms.Draw()

    canvas.Print("SW_"+R+"_"+I +".png")
    del canvas
    gc.collect()


CBCLimit = 0.01
CICLimit=0.005
EleEffLimit=0.005
MuEffLimit=0.005
EleEff=0.97
MuEff=0.97

directory = '/afs/crc.nd.edu/user/r/rgoldouz/L1tracker/Analysis/StubStudies/StubRateEff/hists/'
sample = [
'0p5','1p0','1p5','2p0','2p5','3p0','3p5','4p0','4p5','5p0','5p5','6p0','6p5','7p0']
sampleV = [0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0]

#sample = ['7p0','6p0','5p0','4p0','3p0','2p5','2p0','1p5','1p0','0p5']
#sampleV = [7.0,6.0,5.0,4.0,3.0,2.5,2.0,1.5,1.0,0.5,]

region = ['Barrel', 'Endcap']
category=["Rate","CBCfail","CICfail","Stub", "Cluster"]
plots = ['StubRate', 'CBC-FailFraction', 'CICFailFraction', 'StubMuEfficiency', 'StubEleEfficiency']

onedinputPlots = []

for r in region:
    for b in category:
        for i in range(1, 7):
            onedinputPlots.append("SW_"+r+'_'+str(i)+'_'+b)


HHists=[]
HHistsRealEff=[]

for s in sample:
    filett = ROOT.TFile.Open(directory + 'L1Stub_TTbar_D76_SW' + s + '.root')
    fileMu = ROOT.TFile.Open(directory + 'L1Stub_SingleMu_D76_SW' + s + '.root')
    fileEle = ROOT.TFile.Open(directory + 'L1Stub_SingleElectron_D76_SW' + s + '.root')
    fileMu7p0 = ROOT.TFile.Open(directory + 'L1Stub_SingleMu_D76_SW7p0.root')
    fileEle7p0 = ROOT.TFile.Open(directory + 'L1Stub_SingleElectron_D76_SW7p0.root')
    Hs=[]
    HsRealEff=[]
    for r in region:
        Hr=[]
        HrRealEff=[]
        for i in range(1, 7):
            histRate = filett.Get("SW_"+r+'_'+str(i)+'_'+"Rate")
            histRateGenuinePtg2GeV = filett.Get("SW_"+r+'_'+str(i)+'_'+"RateGenuinePtg2GeV")
            histCBCfail = filett.Get("SW_"+r+'_'+str(i)+'_'+"CBCfail")
            histCICfail = filett.Get("SW_"+r+'_'+str(i)+'_'+"CICfail")
            histCBCfail.Divide(histRateGenuinePtg2GeV)
            histCICfail.Divide(histRateGenuinePtg2GeV)
            histClusMu = fileMu.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubMu = fileMu.Get("SW_"+r+'_'+str(i)+'_'+"Stub2") 
            histStubMu7p0 = fileMu7p0.Get("SW_"+r+'_'+str(i)+'_'+"Stub2")
            histClusMu7p0 = fileMu7p0.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubMu.Divide(histClusMu)
            histStubMu7p0.Divide(histClusMu7p0)
            histStubMuNew = histStubMu.Clone()
            histStubMuNew.Divide(histStubMu7p0)
            histClusEle = fileEle.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubEle = fileEle.Get("SW_"+r+'_'+str(i)+'_'+"Stub2")
            histStubEle7p0 = fileEle7p0.Get("SW_"+r+'_'+str(i)+'_'+"Stub2")
            histClusEle7p0 = fileEle7p0.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubEle.Divide(histClusEle)
            histStubEle7p0.Divide(histClusEle7p0)
            histStubEleNew = histStubEle.Clone()
            histStubEleNew.Divide(histStubEle7p0)
            H = [histRate, histCBCfail, histCICfail, histStubMuNew, histStubEleNew]
            HRealEff = [histRate, histCBCfail, histCICfail, histStubMu, histStubEle]
#            HRealEff = [histRate, histCBCfail, histCICfail, histClusMu, histClusEle]
            HN = ["Rate", "CBC fail fraction", "CIC fail fraction", "Stub eff (Mu, pt>2)", "Stub eff (Ele, pt>4)"]
            Hr.append(H)
            HrRealEff.append(HRealEff)            
        Hs.append(Hr)
        HsRealEff.append(HrRealEff)
    HHistsRealEff.append(HsRealEff)
    HHists.append(Hs)

HHistsTune=[]
HHistsTuneRealEff=[]
sampleTune=['tight','loose']
for s in sampleTune:
    filett = ROOT.TFile.Open(directory + 'L1Stub_TTbar_D76_SW' + s + '.root')
    fileMu = ROOT.TFile.Open(directory + 'L1Stub_SingleMu_D76_SW' + s + '.root')
    fileEle = ROOT.TFile.Open(directory + 'L1Stub_SingleElectron_D76_SW' + s + '.root')
    fileMu7p0 = ROOT.TFile.Open(directory + 'L1Stub_SingleMu_D76_SW7p0.root')
    fileEle7p0 = ROOT.TFile.Open(directory + 'L1Stub_SingleElectron_D76_SW7p0.root')
    Hs=[]
    HsRealEff=[]   
    for r in region:
        Hr=[]
        HrRealEff=[]
        for i in range(1, 7):
            H=[]
            histRate = filett.Get("SW_"+r+'_'+str(i)+'_'+"Rate")
            histRateGenuinePtg2GeV = filett.Get("SW_"+r+'_'+str(i)+'_'+"RateGenuinePtg2GeV")
            histCBCfail = filett.Get("SW_"+r+'_'+str(i)+'_'+"CBCfail")
            histCICfail = filett.Get("SW_"+r+'_'+str(i)+'_'+"CICfail")
            histCBCfail.Divide(histRateGenuinePtg2GeV)
            histCICfail.Divide(histRateGenuinePtg2GeV)
            histClusMu = fileMu.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubMu = fileMu.Get("SW_"+r+'_'+str(i)+'_'+"Stub2")
            histStubMu7p0 = fileMu7p0.Get("SW_"+r+'_'+str(i)+'_'+"Stub2")
            histClusMu7p0 = fileMu7p0.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubMu.Divide(histClusMu)
            histStubMu7p0.Divide(histClusMu7p0)
            histStubMuNew = histStubMu.Clone()
            histStubMuNew.Divide(histStubMu7p0)
            histClusEle = fileEle.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubEle = fileEle.Get("SW_"+r+'_'+str(i)+'_'+"Stub2")
            histStubEle7p0 = fileEle7p0.Get("SW_"+r+'_'+str(i)+'_'+"Stub2")
            histClusEle7p0 = fileEle7p0.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubEle.Divide(histClusEle)
            histStubEle7p0.Divide(histClusEle7p0)
            histStubEleNew = histStubEle.Clone()
            histStubEleNew.Divide(histStubEle7p0)
            H = [histRate, histCBCfail, histCICfail, histStubMuNew, histStubEleNew]
            HRealEff = [histRate, histCBCfail, histCICfail, histStubMu, histStubEle]
#            HRealEff = [histRate, histCBCfail, histCICfail, histClusMu, histClusEle]
            HN = ["Rate", "CBC fail fraction", "CIC fail fraction", "Stub eff (Mu, pt>2)", "Stub eff (Ele, pt>4)"]
            Hr.append(H)
            HrRealEff.append(HRealEff)       
        Hs.append(Hr)
        HsRealEff.append(HrRealEff)
    HHistsTune.append(Hs) 
    HHistsTuneRealEff.append(HsRealEff)



TightTuneBarrelCut = [0]
TightTuneTiltedBarrelCutSet1 = [0]
TightTuneTiltedBarrelCutSet2 = [0]
TightTuneTiltedBarrelCutSet3 = [0]

TightTuneEndcapCutSet1 = [0]
TightTuneEndcapCutSet2 = [0]
TightTuneEndcapCutSet3 = [0]
TightTuneEndcapCutSet4 = [0]
TightTuneEndcapCutSet5 = [0]

LooseTuneBarrelCut = [0]
LooseTuneTiltedBarrelCutSet1 = [0]
LooseTuneTiltedBarrelCutSet2 = [0]
LooseTuneTiltedBarrelCutSet3 = [0]
LooseTuneEndcapCutSet1 = [0]
LooseTuneEndcapCutSet2 = [0]
LooseTuneEndcapCutSet3 = [0]
LooseTuneEndcapCutSet4 = [0]
LooseTuneEndcapCutSet5 = [0]

Rates=""
# HHists[SW][region][layer][variable]
for r in range(len(region)):
    for i in range(1, 7):
        paramTight=[]
        paramLoose=[]
        for b in range(HHists[0][r][i-1][0].GetNbinsX()):
            if HHists[-1][r][i-1][0].GetBinContent(b+1)==0:
                continue
#            print  region[r] + ' layer' + str(i) + ' bin:' +str(b+1) + ' Muon eff:' + str(HHists[-1][r][i-1][3].GetBinContent(b+1))
            paramTight.append(0)
            paramLoose.append(0)
            for s in range(len(sample)):
#                if s==len(sample)-1:
#                    print  sample[s] + ' layer' + str(i) + ' bin:' +str(b+1) + ' Muon eff:' + str(HHists[s][r][i-1][3].GetBinContent(b+1))
                if HHists[s][r][i-1][1].GetBinContent(b+1)<CBCLimit and HHists[s][r][i-1][2].GetBinContent(b+1)<CICLimit:
                    if HHists[s][r][i-1][3].GetBinContent(b+1)<0.60:
                        paramTight[b] = sampleV[s]
                    elif s==0:
                        paramTight[b] = sampleV[s]
                    elif HHists[s][r][i-1][3].GetBinContent(b+1)-HHists[s-1][r][i-1][3].GetBinContent(b+1)>MuEffLimit:
                        paramTight[b] = sampleV[s]
                    else:
                        break
            for s in range(len(sample)):
                if HHists[s][r][i-1][1].GetBinContent(b+1)<CBCLimit and HHists[s][r][i-1][2].GetBinContent(b+1)<CICLimit:
                    if HHists[s][r][i-1][3].GetBinContent(b+1)<0.60 and HHists[s][r][i-1][4].GetBinContent(b+1)<0.60:
                        paramLoose[b] = sampleV[s]
                    elif s==0:
                        paramLoose[b] = sampleV[s]
                    elif HHists[s][r][i-1][3].GetBinContent(b+1)-HHists[s-1][r][i-1][3].GetBinContent(b+1)>MuEffLimit or HHists[s][r][i-1][4].GetBinContent(b+1)-HHists[s-1][r][i-1][4].GetBinContent(b+1)>EleEffLimit:
                        paramLoose[b] = sampleV[s]
                    else:
                        break

        if len(paramTight)>0:
            if region[r] == 'Barrel' and i==1:
                TightTuneBarrelCut.append(most_frequent(paramTight[12:-12]))
                TightTuneTiltedBarrelCutSet1.extend(paramTight[-12:])
                LooseTuneBarrelCut.append(most_frequent(paramLoose[12:-12]))
                LooseTuneTiltedBarrelCutSet1.extend(paramLoose[-12:])
                for x in range(len(paramTight[12:-12])):
                    paramTight[12+x]=most_frequent(paramTight[12:-12])
                    paramLoose[12+x]=most_frequent(paramLoose[12:-12])
            if region[r] == 'Barrel' and i==2:
                TightTuneBarrelCut.append(most_frequent(paramTight[12:-12]))
                TightTuneTiltedBarrelCutSet2.extend(paramTight[-12:])
                LooseTuneBarrelCut.append(most_frequent(paramLoose[12:-12]))
                LooseTuneTiltedBarrelCutSet2.extend(paramLoose[-12:])
                for x in range(len(paramTight[12:-12])):
                    paramTight[12+x]=most_frequent(paramTight[12:-12])
                    paramLoose[12+x]=most_frequent(paramLoose[12:-12])
            if region[r] == 'Barrel' and i==3:
                TightTuneBarrelCut.append(most_frequent(paramTight[12:-12]))
                TightTuneTiltedBarrelCutSet3.extend(paramTight[-12:])
                LooseTuneBarrelCut.append(most_frequent(paramLoose[12:-12]))
                LooseTuneTiltedBarrelCutSet3.extend(paramLoose[-12:])
                for x in range(len(paramTight[12:-12])):
                    paramTight[12+x]=most_frequent(paramTight[12:-12])
                    paramLoose[12+x]=most_frequent(paramLoose[12:-12])
            if region[r] == 'Barrel' and i>3:
                TightTuneBarrelCut.append(most_frequent(paramTight))
                LooseTuneBarrelCut.append(most_frequent(paramLoose))
                for x in range(len(paramTight)):
                    paramTight[x]=most_frequent(paramTight)
                    paramLoose[x]=most_frequent(paramLoose)
            if region[r] == 'Endcap' and i==1:
                TightTuneEndcapCutSet1.extend(paramTight[:15])
                LooseTuneEndcapCutSet1.extend(paramLoose[:15])
            if region[r] == 'Endcap' and i==2:
                TightTuneEndcapCutSet2.extend(paramTight[:15])
                LooseTuneEndcapCutSet2.extend(paramLoose[:15])
            if region[r] == 'Endcap' and i==3:
                TightTuneEndcapCutSet3.extend(paramTight[:12])
                LooseTuneEndcapCutSet3.extend(paramLoose[:12])
            if region[r] == 'Endcap' and i==4:
                TightTuneEndcapCutSet4.extend(paramTight[:12])
                LooseTuneEndcapCutSet4.extend(paramLoose[:12])
            if region[r] == 'Endcap' and i==5:
                TightTuneEndcapCutSet5.extend(paramTight[:12])
                LooseTuneEndcapCutSet5.extend(paramLoose[:12])

        NSWTTight_Rate = HHists[-1][r][i-1][0].Clone()
        NSWTTight_CBCfail= HHists[-1][r][i-1][1].Clone()
        NSWTTight_CICfail= HHists[-1][r][i-1][2].Clone()
        NSWTTight_effMu= HHists[-1][r][i-1][3].Clone()
        NSWTTight_effEle= HHists[-1][r][i-1][4].Clone()
        NSWTTight_effMuRealEff= HHists[-1][r][i-1][3].Clone()
        NSWTTight_effEleRealEff= HHists[-1][r][i-1][4].Clone()

        NSWTLoose_Rate = HHists[-1][r][i-1][0].Clone()
        NSWTLoose_CBCfail= HHists[-1][r][i-1][1].Clone()
        NSWTLoose_CICfail= HHists[-1][r][i-1][2].Clone()
        NSWTLoose_effMu= HHists[-1][r][i-1][3].Clone()
        NSWTLoose_effEle= HHists[-1][r][i-1][4].Clone()
        NSWTLoose_effMuRealEff= HHists[-1][r][i-1][3].Clone()
        NSWTLoose_effEleRealEff= HHists[-1][r][i-1][4].Clone()

        for b in range(HHists[-1][r][i-1][0].GetNbinsX()):
            if HHists[-1][r][i-1][0].GetBinContent(b+1)==0:
                continue
            NSWTTight_Rate.SetBinContent(b+1, 1.001*HHists[sampleV.index(paramTight[b])][r][i-1][0].GetBinContent(b+1))
            NSWTTight_CBCfail.SetBinContent(b+1, 1.001*HHists[sampleV.index(paramTight[b])][r][i-1][1].GetBinContent(b+1))
            NSWTTight_CICfail.SetBinContent(b+1, 1.001*HHists[sampleV.index(paramTight[b])][r][i-1][2].GetBinContent(b+1))
            NSWTTight_effMu.SetBinContent(b+1, 1.001*HHists[sampleV.index(paramTight[b])][r][i-1][3].GetBinContent(b+1))
            NSWTTight_effEle.SetBinContent(b+1, 1.001*HHists[sampleV.index(paramTight[b])][r][i-1][4].GetBinContent(b+1))
            NSWTTight_effMuRealEff.SetBinContent(b+1, 1.001*HHistsRealEff[sampleV.index(paramTight[b])][r][i-1][3].GetBinContent(b+1))
            NSWTTight_effEleRealEff.SetBinContent(b+1, 1.001*HHistsRealEff[sampleV.index(paramTight[b])][r][i-1][4].GetBinContent(b+1))

            NSWTLoose_Rate.SetBinContent(b+1, 0.999*HHists[sampleV.index(paramLoose[b])][r][i-1][0].GetBinContent(b+1))
            NSWTLoose_CBCfail.SetBinContent(b+1, 0.999*HHists[sampleV.index(paramLoose[b])][r][i-1][1].GetBinContent(b+1))
            NSWTLoose_CICfail.SetBinContent(b+1, 0.999*HHists[sampleV.index(paramLoose[b])][r][i-1][2].GetBinContent(b+1))
            NSWTLoose_effMu.SetBinContent(b+1, 0.999*HHists[sampleV.index(paramLoose[b])][r][i-1][3].GetBinContent(b+1))
            NSWTLoose_effEle.SetBinContent(b+1, 0.999*HHists[sampleV.index(paramLoose[b])][r][i-1][4].GetBinContent(b+1))
            NSWTLoose_effMuRealEff.SetBinContent(b+1, 0.999*HHistsRealEff[sampleV.index(paramLoose[b])][r][i-1][3].GetBinContent(b+1))
            NSWTLoose_effEleRealEff.SetBinContent(b+1, 0.999*HHistsRealEff[sampleV.index(paramLoose[b])][r][i-1][4].GetBinContent(b+1))

        newTuneTight=[NSWTTight_Rate, NSWTTight_CBCfail, NSWTTight_CICfail, NSWTTight_effMu, NSWTTight_effEle]
        newTuneLoose=[NSWTLoose_Rate, NSWTLoose_CBCfail, NSWTLoose_CICfail, NSWTLoose_effMu, NSWTLoose_effEle]
        newTuneTightRealEff=[NSWTTight_Rate, NSWTTight_CBCfail, NSWTTight_CICfail, NSWTTight_effMuRealEff, NSWTTight_effEleRealEff]
        newTuneLooseRealEff=[NSWTLoose_Rate, NSWTLoose_CBCfail, NSWTLoose_CICfail, NSWTLoose_effMuRealEff, NSWTLoose_effEleRealEff]
        for c in range(len(plots)):
            H=[]
            HT=[]
            HRealEff=[]
            HTRealEff=[]
            for s in range(len(sample)):
                H.append(HHists[s][r][i-1][c])
                HRealEff.append(HHistsRealEff[s][r][i-1][c])
            for s in range(len(sampleTune)):
                HT.append(HHistsTune[s][r][i-1][c])
                HTRealEff.append(HHistsTuneRealEff[s][r][i-1][c])
            HT.append(newTuneTight[c])
            HT.append(newTuneLoose[c])
            HTRealEff.append(newTuneTightRealEff[c])
            HTRealEff.append(newTuneLooseRealEff[c])
            drawHistallW(H,sample,HT,['tight','loose','newTight','newLoose'], region[r]+'-'+plots[c] , str(i))
            totalRate=0
            if 'StubRate' == plots[c]:
                vec=['tight','loose','newTight','newLoose']
                for a in range(len(HT)):
                    if 'Barr' in region[r]:
                        Rates += (vec[a]+'Tune-' + region[r]  +'-layer'+str(i)+': ').ljust(70) +str('{:.3}'.format(HT[a].Integral())) + '\n'
                    else:
                        Rates += (vec[a]+'Tune-' + region[r]  +'-Disk'+str(i)+': ').ljust(70)+str('{:.3}'.format(HT[a].Integral())) + '\n'               
                if HT[0].Integral()>0:
                    Rates += 'ratio of new tight to tight tune for ' + region[r]  +'-Disk'+str(i)+'= '+str('{:.3}'.format(HT[2].Integral()/HT[0].Integral())) + '\n'
                    Rates +='\n'
            if 'Efficiency' in plots[c]:
                drawHistallW(HRealEff,sample,HTRealEff,['tight','loose','newTight','newLoose'], 'RealEff'+region[r]+'-'+plots[c] , str(i))
os.system("mkdir plot_SW_AllW")
os.system("mv *.png plot_SW_AllW")


text = '# New tight tune based on simulated events CMSSW_11_3_0_pre3, D76 \n'
text +=  '    BarrelCut    = cms.vdouble(' 
text += str(TightTuneBarrelCut)[1:-1]
text += '),\n    TiltedBarrelCutSet = cms.VPSet(\n        cms.PSet( TiltedCut = cms.vdouble( 0 ) ),\n        cms.PSet( TiltedCut = cms.vdouble( '
text += str(TightTuneTiltedBarrelCutSet1)[1:-1]
text += ') ),\n        cms.PSet( TiltedCut = cms.vdouble( '
text += str(TightTuneTiltedBarrelCutSet2)[1:-1]
text += ') ),\n        cms.PSet( TiltedCut = cms.vdouble('
text += str(TightTuneTiltedBarrelCutSet3)[1:-1]
text += ') ),\n        ),\n    EndcapCutSet = cms.VPSet(\n        cms.PSet( EndcapCut = cms.vdouble( 0 ) ),\n        cms.PSet( EndcapCut = cms.vdouble('
text += str(TightTuneEndcapCutSet1)[1:-1]
text += ') ),\n        cms.PSet( EndcapCut = cms.vdouble('
text += str(TightTuneEndcapCutSet2)[1:-1]
text += ') ),\n        cms.PSet( EndcapCut = cms.vdouble('
text += str(TightTuneEndcapCutSet3)[1:-1]
text += ') ),\n        cms.PSet( EndcapCut = cms.vdouble('
text += str(TightTuneEndcapCutSet4)[1:-1]
text += ') ),\n        cms.PSet( EndcapCut = cms.vdouble('
text += str(TightTuneEndcapCutSet5)[1:-1]
text += ') ),\n        )\n)\n'

text += '# New loose tune based on simulated events CMSSW_11_3_0_pre3, D76 \n'
text +=  '    BarrelCut    = cms.vdouble('
text += str(LooseTuneBarrelCut)[1:-1]
text += '),\n    TiltedBarrelCutSet = cms.VPSet(\n        cms.PSet( TiltedCut = cms.vdouble( 0 ) ),\n        cms.PSet( TiltedCut = cms.vdouble( '
text += str(LooseTuneTiltedBarrelCutSet1)[1:-1]
text += ') ),\n        cms.PSet( TiltedCut = cms.vdouble( '
text += str(LooseTuneTiltedBarrelCutSet2)[1:-1]
text += ') ),\n        cms.PSet( TiltedCut = cms.vdouble('
text += str(LooseTuneTiltedBarrelCutSet3)[1:-1]
text += ') ),\n        ),\n    EndcapCutSet = cms.VPSet(\n        cms.PSet( EndcapCut = cms.vdouble( 0 ) ),\n        cms.PSet( EndcapCut = cms.vdouble('
text += str(LooseTuneEndcapCutSet1)[1:-1]
text += ') ),\n        cms.PSet( EndcapCut = cms.vdouble('
text += str(LooseTuneEndcapCutSet2)[1:-1]
text += ') ),\n        cms.PSet( EndcapCut = cms.vdouble('
text += str(LooseTuneEndcapCutSet3)[1:-1]
text += ') ),\n        cms.PSet( EndcapCut = cms.vdouble('
text += str(LooseTuneEndcapCutSet4)[1:-1]
text += ') ),\n        cms.PSet( EndcapCut = cms.vdouble('
text += str(LooseTuneEndcapCutSet5)[1:-1]
text += ') ),\n        )\n)\n'


print text

print Rates
