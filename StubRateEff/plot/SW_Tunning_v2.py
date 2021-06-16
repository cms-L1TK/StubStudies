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

def drawHistperW(A,AN, R, I):
#    rate = A[0].Clone()
#    Num = A[0].Integral()
#    if A[0].Integral()>0:
#        rate.Scale(1/A[0].Integral())
    canvas = ROOT.TCanvas(R+I,R+I,10,10,1100,628)
    canvas.cd()

    pad_name = "pad"
    pad1=ROOT.TPad(pad_name, pad_name, 0, 0, 1, 1 , 0)
    pad1.Draw()
    pad1.cd()
#    pad1.SetLogy()
    if 'Barrel' in R:
        A[4].SetTitle(R + ', Layer -'+I)
        A[4].GetXaxis().SetTitle('Module no. along z')
        A[4].GetYaxis().SetTitle('X')
    else:
        A[4].SetTitle(R + ', Disk -'+I)
        A[4].GetXaxis().SetTitle('module ring no.')
        A[4].GetYaxis().SetTitle('X')
    A[4].SetMarkerStyle(25);
    A[1].SetMarkerStyle(20);
    A[2].SetMarkerStyle(21);
    A[3].SetMarkerStyle(22);
    A[5].SetMarkerStyle(23);
    
    A[4].SetMarkerColor(2);
    A[1].SetMarkerColor(3);
    A[2].SetMarkerColor(4);
    A[3].SetMarkerColor(1);
    A[5].SetMarkerColor(6);

    A[4].SetMinimum(0);
    A[4].SetMaximum(1);

#    rate.Draw("p HIST SAME")
    A[4].Draw("p HIST SAME")
    A[1].Draw("p HIST SAME")
    A[2].Draw("p HIST SAME")
    A[3].Draw("p HIST SAME")
    A[5].Draw("p HIST SAME")

    leg = ROOT.TLegend(0.73,0.6,1,0.88)
#    leg.AddEntry(rate, AN[0] + ' * ' + str(round(Num,1))        , "p");
    leg.AddEntry(A[4], AN[4]                           , "p");
    leg.AddEntry(A[1], AN[1]                           , "p");
    leg.AddEntry(A[2], AN[2]                           , "p");
    leg.AddEntry(A[3], AN[3]                           , "p");
    leg.AddEntry(A[5], AN[5]                           , "p");

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
        line1 = ROOT.TLine(12,0,12,1);
        line1.Draw("same");
        line2 = ROOT.TLine(tp,0,tp,1);
        line2.Draw("same");

        label_cms="Tilt-                  Flat                               Tilt+"
        Label_cms = ROOT.TLatex(0.15,0.85,label_cms)
        Label_cms.SetNDC()
        Label_cms.SetTextFont(61)
        Label_cms.Draw()

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
        A[i].SetMarkerColor(30+i);
    
        if A[i].GetMaximum()>maxi:
            maxi=A[i].GetMaximum()
        if A[i].GetMinimum()<mini:
            mini=A[i].GetMinimum()
#        if i+4==10:
#            A[i].SetMarkerColor(28);

    maxi = maxi * 1.2
    A[0].SetMinimum(mini);
    A[0].SetMaximum(maxi);
    for i in range(len(A)):
        A[i].Draw("p HIST SAME")

    leg = ROOT.TLegend(0.73,0.3,0.88,0.88)

    for i in range(len(A)):
        A[i].Draw("p HIST SAME")
        leg.AddEntry(A[i], AN[i]                           , "p");
    for i in range(len(B)):
        B[i].SetLineColor(1+i);
        if i+1==3:
            B[i].SetLineColor(4);
        B[i].SetLineStyle(i*2);
        B[i].Draw("HIST SAME")
        leg.AddEntry(B[i], BN[i]                           , "L");

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
        line1 = ROOT.TLine(12,0,12,maxi);
        line1.Draw("same");
        line2 = ROOT.TLine(tp,0,tp,maxi);
        line2.Draw("same");

        label_cms="Tilt-                  Flat                               Tilt+"
        Label_cms = ROOT.TLatex(0.15,0.85,label_cms)
        Label_cms.SetNDC()
        Label_cms.SetTextFont(61)
        Label_cms.Draw()

    canvas.Print("SW_"+R+"_"+I +".png")
    del canvas
    gc.collect()

directory = '/afs/crc.nd.edu/user/r/rgoldouz/L1tracker/Analysis/StubStudies/StubRateEff/hists/'
sampleSW = ['0p5','1p0','2p0','3p0','4p0','5p0','6p0','7p0']
sampleTune=['tight','loose']
#sampleSW = ['5p0','5p5','6p0','6p5','7p0']
#sampleSW = ['TIGHT','REZA']

region = ['Barrel', 'Endcap']
plots = ['StubRate', 'CBC-FailFraction', 'CICFailFraction', 'DTCfailFraction','StubMuEfficiency', 'StubEleEfficiency', 'StubDMuEfficiency']


HHistsSW=[]
for s in sampleSW:
    filett = ROOT.TFile.Open(directory +  'L1Stub_TTbar_D49_SW' + s + '.root')
    fileMu = ROOT.TFile.Open(directory +  'L1Stub_SingleMu_D49_SW' + s + '.root')
    fileEle = ROOT.TFile.Open(directory + 'L1Stub_SingleElectron_D49_SW' + s + '.root')
    fileDMu = ROOT.TFile.Open(directory + 'L1Stub_DisplacedMu_D49_SW' + s + '.root')

#    filett = ROOT.TFile.Open(directory + 'L1Stub_TTbar_CMSSW_11_2_0_pre5_2026D49PU200_SW' + s + '.root')
#    fileMu = ROOT.TFile.Open(directory + 'L1Stub_SingleMuFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU_SW' + s + '.root')
#    fileEle = ROOT.TFile.Open(directory + 'L1Stub_SingleElectronFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU_SW' + s + '.root')
#    fileDMu = ROOT.TFile.Open(directory + 'L1Stub_DisplacedMuPt1p5To8_CMSSW_11_2_0_pre5_2026D49PUnoPU_SW' + s + '.root')
    Hs=[]
    for r in region:
        Hr=[]
        for i in range(1, 7):
            H=[]
            histRate = filett.Get("SW_"+r+'_'+str(i)+'_'+"Rate")
            histRateGenuinePtg2GeV = filett.Get("SW_"+r+'_'+str(i)+'_'+"RateGenuinePtg2GeV")
            histCBCfail = filett.Get("SW_"+r+'_'+str(i)+'_'+"CBCfail")
            histCICfail = filett.Get("SW_"+r+'_'+str(i)+'_'+"CICfail")
            histDTCfail = filett.Get("SW_"+r+'_'+str(i)+'_'+"DTCfail")
            histCBCfail.Divide(histRateGenuinePtg2GeV)
            histCICfail.Divide(histRateGenuinePtg2GeV)
            histDTCfail.Divide(histRateGenuinePtg2GeV)
            histClusMu = fileMu.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubMu = fileMu.Get("SW_"+r+'_'+str(i)+'_'+"Stub") 
            histStubMu.Divide(histClusMu)
            histClusEle = fileEle.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubEle = fileEle.Get("SW_"+r+'_'+str(i)+'_'+"Stub")
            histStubEle.Divide(histClusEle)
            histClusDMu = fileDMu.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubDMu = fileDMu.Get("SW_"+r+'_'+str(i)+'_'+"Stub")
            histStubDMu.Divide(histClusDMu)
            H = [histRate, histCBCfail, histCICfail, histDTCfail, histStubMu, histStubEle, histStubDMu]
            HN = ["Rate", "CBC fail fraction", "CIC fail fraction", "DTC fail fraction", "Stub eff (Mu, pt>2)", "Stub eff (Ele, pt>4)", "Stub eff (Displaced Mu, pt>2)"]
            Hr.append(H)
#            drawHistperW(H, HN, r+ '-'+s , str(i))
        Hs.append(Hr)
    HHistsSW.append(Hs)

HHistsTune=[]
for s in sampleTune:
#    filett = ROOT.TFile.Open(directory + 'L1Stub_TTbar_CMSSW_11_2_0_pre5_2026D49PU200_SW' + s + '.root')
#    fileMu = ROOT.TFile.Open(directory + 'L1Stub_SingleMuFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU_SW' + s + '.root')
#    fileEle = ROOT.TFile.Open(directory + 'L1Stub_SingleElectronFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU_SW' + s + '.root')
    filett = ROOT.TFile.Open(directory +  'L1Stub_TTbar_D49_SW' + s + '.root')
    fileMu = ROOT.TFile.Open(directory +  'L1Stub_SingleMu_D49_SW' + s + '.root')
    fileEle = ROOT.TFile.Open(directory + 'L1Stub_SingleElectron_D49_SW' + s + '.root')
    fileDMu = ROOT.TFile.Open(directory + 'L1Stub_DisplacedMu_D49_SW' + s + '.root')

    Hs=[]
    for r in region:
        Hr=[]
        for i in range(1, 7):
            H=[]
            histRate = filett.Get("SW_"+r+'_'+str(i)+'_'+"Rate")
            histRateGenuinePtg2GeV = filett.Get("SW_"+r+'_'+str(i)+'_'+"RateGenuinePtg2GeV")
            histCBCfail = filett.Get("SW_"+r+'_'+str(i)+'_'+"CBCfail")
            histCICfail = filett.Get("SW_"+r+'_'+str(i)+'_'+"CICfail")
            histDTCfail = filett.Get("SW_"+r+'_'+str(i)+'_'+"DTCfail")
            histCBCfail.Divide(histRateGenuinePtg2GeV)
            histCICfail.Divide(histRateGenuinePtg2GeV)
            histDTCfail.Divide(histRateGenuinePtg2GeV)
            histClusMu = fileMu.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubMu = fileMu.Get("SW_"+r+'_'+str(i)+'_'+"Stub")
            histStubMu.Divide(histClusMu)
            histClusEle = fileEle.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubEle = fileEle.Get("SW_"+r+'_'+str(i)+'_'+"Stub")
            histStubEle.Divide(histClusEle)
            histClusDMu = fileDMu.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubDMu = fileDMu.Get("SW_"+r+'_'+str(i)+'_'+"Stub")
            histStubDMu.Divide(histClusDMu)
            H = [histRate, histCBCfail, histCICfail, histDTCfail, histStubMu, histStubEle, histStubDMu]
            HN = ["Rate", "CBC fail fraction", "CIC fail fraction", "DTC fail fraction", "Stub eff (Mu, pt>2)", "Stub eff (Ele, pt>4)", "Stub eff (Displaced Mu, pt>2)"]
            Hr.append(H)
#            drawHistperW(H, HN, r+ '-'+s , str(i))
        Hs.append(Hr)
    HHistsTune.append(Hs)
os.system("mkdir plot_SW_perW")
os.system("mv *.png plot_SW_perW")

for c in range(len(plots)):
    for r in range(len(region)):
        for i in range(1, 7):
            H=[]
            HT=[]
            for s in range(len(sampleSW)):
                H.append(HHistsSW[s][r][i-1][c])
            for s in range(len(sampleTune)):
                HT.append(HHistsTune[s][r][i-1][c])
            drawHistallW(H,sampleSW,HT,sampleTune, region[r]+'-'+plots[c] , str(i))

os.system("mkdir plot_SW_AllW")
os.system("mv *.png plot_SW_AllW")








