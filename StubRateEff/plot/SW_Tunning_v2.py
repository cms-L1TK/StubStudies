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

def drawHistallW(A,AN, R, I):
    canvas = ROOT.TCanvas(R+I,R+I,10,10,1100,628)
    canvas.cd()

    pad_name = "pad"
    pad1=ROOT.TPad(pad_name, pad_name, 0, 0, 1, 1 , 0)
    pad1.Draw()
    pad1.cd()
#    pad1.SetLogy()
    A[0].SetTitle(R + '      L/D'+I)
    A[0].GetXaxis().SetTitle('Z/R')
    A[0].GetYaxis().SetTitle('X')

    maxi=A[0].GetMaximum()
    mini=A[0].GetMinimum()
    for i in range(len(A)):
        A[i].SetMarkerStyle(20+i);
        A[i].SetMarkerColor(1+i);
        if A[i].GetMaximum()>maxi:
            maxi=A[i].GetMaximum()
        if A[i].GetMinimum()<mini:
            mini=A[i].GetMinimum()
        if i==9:
            A[i].SetMarkerColor(12);

    A[0].SetMinimum(mini);
    A[0].SetMaximum(maxi);
    for i in range(len(A)):
        A[i].Draw("p HIST SAME")

    leg = ROOT.TLegend(0.73,0.3,0.88,0.88)

    for i in range(len(A)):
        A[i].Draw("p HIST SAME")
        leg.AddEntry(A[i], AN[i]                           , "p");

    leg.SetBorderSize(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.04)
    leg.Draw("same")

    canvas.Print("SW_"+R+"_"+I +".png")
    del canvas
    gc.collect()

directory = '/afs/crc.nd.edu/user/r/rgoldouz/L1tracker/Analysis/StubStudies/StubRateEff/hists/'
#sample = ['0p5','1p0','1p5','2p0','2p5','3p0','4p0','5p0','6p0','7p0']
sample = ['TIGHT','REZA']

region = ['Barrel', 'Endcap']
category=["Rate","CBCfail","CICfail","Stub", "Cluster"]
plots = ['StubRate', 'CBC-FailFraction', 'CICFailFraction', 'StubMuEfficiency', 'StubEleEfficiency']

onedinputPlots = []

for r in region:
    for b in category:
        for i in range(1, 7):
            onedinputPlots.append("SW_"+r+'_'+str(i)+'_'+b)


HHists=[]
for s in sample:
    filett = ROOT.TFile.Open(directory + 'FE_SW' + s + '_L1Stub_Tt_Pu200_110D49.root')
    fileMu = ROOT.TFile.Open(directory + 'FE_SW' + s + '_L1Stub_SingleMuFlatPt1p5To8_Pu0_110D49.root')
    fileEle = ROOT.TFile.Open(directory + 'FE_SW' + s + '_L1Stub_SingleEFlatPt1p5To8_Pu0_110D49.root')
    Hs=[]
    for r in region:
        Hr=[]
        for i in range(1, 7):
            H=[]
            histRate = filett.Get("SW_"+r+'_'+str(i)+'_'+"Rate")
            histCBCfail = filett.Get("SW_"+r+'_'+str(i)+'_'+"CBCfail")
            histCICfail = filett.Get("SW_"+r+'_'+str(i)+'_'+"CICfail")
            histCBCfail.Divide(histRate)
            histCICfail.Divide(histRate)
            histClusMu = fileMu.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubMu = fileMu.Get("SW_"+r+'_'+str(i)+'_'+"Stub") 
            histStubMu.Divide(histClusMu)
            histClusEle = fileEle.Get("SW_"+r+'_'+str(i)+'_'+"Cluster")
            histStubEle = fileEle.Get("SW_"+r+'_'+str(i)+'_'+"Stub")
            histStubEle.Divide(histClusEle)
            H = [histRate, histCBCfail, histCICfail, histStubMu, histStubEle]
            HN = ["Rate", "CBC fail fraction", "CIC fail fraction", "Stub eff (Mu, pt>2)", "Stub eff (Ele, pt>4)"]
            Hr.append(H)
            drawHistperW(H, HN, r+ '-'+s , str(i))
        Hs.append(Hr)
    HHists.append(Hs)
os.system("mkdir plot_SW_perW")
os.system("mv *.png plot_SW_perW")

for c in range(len(plots)):
    for r in range(len(region)):
        for i in range(1, 7):
            H=[]
            for s in range(len(sample)):
                H.append(HHists[s][r][i-1][c])
            drawHistallW(H,sample, region[r]+'-'+plots[c] , str(i))

os.system("mkdir plot_SW_AllW")
os.system("mv *.png plot_SW_AllW")








