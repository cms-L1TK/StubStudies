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

def drawHist(A,AN, R, I):
    Num = A[0].Integral()
    if A[0].Integral()>0:
        A[0].Scale(1/A[0].Integral())
    canvas = ROOT.TCanvas(R+I,R+I,10,10,1100,628)
    canvas.cd()

    pad_name = "pad"
    pad1=ROOT.TPad(pad_name, pad_name, 0, 0, 1, 1 , 0)
    pad1.Draw()
    pad1.cd()
#    pad1.SetLogy()
    A[0].SetTitle(R + 'L/D'+I)
    A[0].GetXaxis().SetTitle('Z/R')
    A[0].GetYaxis().SetTitle('X')
    A[0].SetMarkerStyle(25);
    A[1].SetMarkerStyle(20);
    A[2].SetMarkerStyle(21);
    A[3].SetMarkerStyle(22);
    A[4].SetMarkerStyle(23);
    
    A[0].SetMarkerColor(2);
    A[1].SetMarkerColor(3);
    A[2].SetMarkerColor(4);
    A[3].SetMarkerColor(1);
    A[4].SetMarkerColor(6);

    A[0].SetMinimum(0);
    A[0].SetMaximum(1);

    A[0].Draw("p HIST SAME")
    A[1].Draw("p HIST SAME")
    A[2].Draw("p HIST SAME")
    A[3].Draw("p HIST SAME")
    A[4].Draw("p HIST SAME")

    leg = ROOT.TLegend(0.73,0.6,1,0.88)
    leg.AddEntry(A[0], AN[0] + ' * ' + str(round(Num,1))        , "p");
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


directory = '/afs/crc.nd.edu/user/r/rgoldouz/L1tracker/Analysis/StubStudies/StubRateEff/hists/'
sample = [
'FE_SWtight_Tt_Pu200_110D49.root',
'FE_SWtight_SingleMuFlatPt1p5To8_Pu0_110D49.root',
'FE_SWtight_SingleEFlatPt1p5To8_Pu0_110D49.root'
]

region = ['Barrel', 'Endcap']
category=["Rate","CBCfail","CICfail","Stub", "Cluster"]

onedinputPlots = []

for r in region:
    for b in category:
        for i in range(1, 7):
            onedinputPlots.append("SW_"+r+'_'+str(i)+'_'+b)

filett = ROOT.TFile.Open(directory + sample[0])
fileMu = ROOT.TFile.Open(directory + sample[1])
fileEle = ROOT.TFile.Open(directory + sample[2])

for r in region:
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
        drawHist(H, HN, r , str(i))
os.system("mkdir plot_SW")
os.system("mv *.png plot_SW")
