import math
import gc
import sys
import ROOT
import numpy as np
import copy
import os
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gROOT.ProcessLine("gErrorIgnoreLevel = 1;")
ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gStyle.SetOptStat(0)
from array import array
from ROOT import TColor
from ROOT import TGaxis
from ROOT import THStack
import gc

def compareHists(hists,Fnames, ch = "channel", reg = "region", var="sample", varname="v", WC="EFTrwgt1_cS_1_cT_1"):
    for num in range(len(hists)):
        if (hists[num].Integral() <= 0):
            return

    canvas = ROOT.TCanvas(ch+reg+var,ch+reg+var,50,50,865,780)
    canvas.SetGrid();
    canvas.SetBottomMargin(0.17)
    canvas.cd()

    legend = ROOT.TLegend(0.65,0.65,0.85,0.82)
    legend.SetBorderSize(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.025)

    pad1=ROOT.TPad("pad1", "pad1", 0.05, 0.05, 1, 0.99 , 0)#used for the hist plot
    pad1.Draw()
    pad1.cd()
    pad1.SetLogx(ROOT.kFALSE)
    pad1.SetLogy(ROOT.kFALSE)

    y_min=0
    y_max=1.2* max(hists[0].GetMaximum(), hists[1].GetMaximum(), hists[2].GetMaximum())
    hists[0].SetTitle(varname)
    hists[0].GetYaxis().SetTitle('')
    hists[0].GetXaxis().SetLabelSize(0.03)
    hists[0].GetYaxis().SetTitleOffset(1)
    hists[0].GetYaxis().SetTitleSize(0.05)
    hists[0].GetYaxis().SetLabelSize(0.04)
    hists[0].GetYaxis().SetRangeUser(y_min,y_max)
    hists[0].GetXaxis().SetTitle("")
    hists[0].Draw("Hist")
    hists[0].SetLineWidth(2)
    hists[0].SetFillColor(0)
    for H in range(1,len(hists)):
        hists[H].SetLineWidth(2)
        hists[H].SetFillColor(0)
        hists[H].Draw("histSAME")
    hists[0].Draw("AXISSAMEY+")
    hists[0].Draw("AXISSAMEX+")

    for num in range(0,len(hists)):
        legend.AddEntry(hists[num],Fnames[num],'L')
    legend.Draw("same")

    Label_channel2 = ROOT.TLatex(0.2,0.87,reg)
    Label_channel2.SetNDC()
    Label_channel2.SetTextFont(42)
    Label_channel2.SetTextSize(0.025)
    Label_channel2.Draw("same")

    pad1.Update()
    canvas.Print(reg+var+ ".png")
    del canvas
    gc.collect()

HistAddress = '/afs/crc.nd.edu/user/r/rgoldouz/L1tracker/CMSSW_11_3_0_pre3/src/L1Trigger/TrackFindingTracklet/test/'
HistAddress = '/scratch365/rgoldouz/myCondor/L1Stub/TrkEff/'
typeLep = ['SingleElectron','SingleMu', 'TTbar']
typeLep = ['SingleElectron','SingleMu']
typeLep = [
#"SingleElectronFlatPt1p5To8_CMSSW1250pre2D76_CalcBendCutsTrue_nTPstub0",
#"SingleMuFlatPt1p5To8_CMSSW1250pre2D76_CalcBendCutsTrue",
"DisplacedMuPt1p5To8Dxy100_CalcBendCutsTrue",
#"TTbar_CMSSW1250pre2D76_CalcBendCutsTrue"
]
samples = [
"newLoose",
"newTight",
"loose",
"tight",
#"0p5", "7p0"
]

Variables = []
Files = ROOT.TFile.Open(HistAddress + 'output_L1Stub_' + typeLep[0] +'_' +  samples[0] +'_pt3.root' )
my_list = Files.GetListOfKeys()
for obj in my_list: # obj is TKey
    if obj.GetClassName() == "TH1F":
        Variables.append(obj.GetName())
colors =  [ROOT.kBlack, ROOT.kRed-4, ROOT.kBlue, ROOT.kGreen, ROOT.kCyan, ROOT.kYellow]

for var in Variables:
    for lep in typeLep:
        Hists=[]
        for sam in range(len(samples)):
            Files = ROOT.TFile.Open(HistAddress + 'output_L1Stub_' + lep +'_' +  samples[sam] +'_pt3.root' )
            h=Files.Get(var)
            h.SetLineColor(colors[sam])
            Hists.append(h)
            Files.Close()
        compareHists(Hists,samples, lep, lep,var,var,"")
for lep in typeLep:
    os.system("mkdir trkEff_" + lep)
    os.system("mv " + lep +'* trkEff_' + lep)

