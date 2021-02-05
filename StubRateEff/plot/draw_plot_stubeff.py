import math
import gc
import os,sys
import sys
import ROOT
import numpy as npi
import copy
from array import array
ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.gROOT.ProcessLine("gErrorIgnoreLevel = 1;")
ROOT.TH1.AddDirectory(ROOT.kFALSE)
ROOT.gStyle.SetOptStat(0)


import gc

################################## MY SIGNAL AND SM BG ################################

def compareNeffHist(A, textA, label_name="sample", can_name="can"):
    a,i,b,c, = label_name.split("_")
    cc = int(b)
    canvas = ROOT.TCanvas(can_name,can_name,10,10,1100,628)
    canvas.cd()
    for l in range(len(A)):
        A[l].SetLineColor( l+1 )
    if len(A)==2:
        A[0].SetLineColor(4)        

    A[0].SetMaximum(1.1)
    A[0].SetMinimum(0)
    A[0].SetTitle("")
    A[0].GetXaxis().SetTitle(i)
    A[0].GetYaxis().SetTitle('Stub eff ')
    A[0].GetXaxis().SetTitleSize(0.05)
    A[0].GetYaxis().SetTitleSize(0.05)
    for l in range(len(A)):
        A[l].Draw('esame')

    legend = ROOT.TLegend(0.4,0.8,1,1)
    for l in range(len(A)):
        legend.AddEntry(A[l] ,textA[l],'l')
    legend.SetBorderSize(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.025)
    legend.Draw("same")

    label = ROOT.TLatex()
    label.SetTextAlign(12)
    label.SetTextFont(42)
    label.SetTextSize(0.06)
    label.SetNDC(ROOT.kTRUE)
    if a == 'Barrel':
        label.DrawLatex(0.1,0.95, a + ", Layer " + str(cc))
    if a == 'Endcap':
        label.DrawLatex(0.1,0.95, a + ", Disk " + str(cc))

    if not os.path.exists("plots_Compare"):
        os.mkdir( "plots_Compare", 0755 );

    if A[0].Integral()>0:
        canvas.Print("plots_Compare/"+ can_name +"_"+ label_name + ".png")
    del canvas
    gc.collect()

def compare2Hist(A, B, textA="A", textB="B", label_name="sample", can_name="can", p='p'):

    a,i,b,c, = label_name.split("_")
    cc = int(b)
    canvas = ROOT.TCanvas(can_name,can_name,10,10,1100,628)
    canvas.SetGrid()
    canvas.cd()

    pad_name1 = "pad1"
    pad1=ROOT.TPad(pad_name1, pad_name1, 0.05, 0.05, 1, 0.99 , 0)
    pad1.Draw()
#    pad1.SetLogy()
    pad1.SetGrid()
    pad1.cd()

    r = A.Clone()
    r.Divide(B)    
    r.SetLineColor( 1 )

    r.SetTitle("")
    r.GetXaxis().SetTitle(i)
    r.GetYaxis().SetTitle('Stub Efficiency')
    r.GetXaxis().SetTitleSize(0.05)
    r.GetYaxis().SetTitleSize(0.05)
    r.SetMaximum(1.2*r.GetMaximum());
    r.Draw()

    label = ROOT.TLatex()
    label.SetTextAlign(12)
    label.SetTextFont(42)
    label.SetTextSize(0.06)
    label.SetNDC(ROOT.kTRUE)
    if a == 'Barrel':
        label.DrawLatex(0.1,0.95, a + " Layer " + str(cc) + ", " + " (" + p + ")")
    if a == 'Endcap':
        label.DrawLatex(0.1,0.95, a + "Disk " + str(cc) + ", " +  " ("  + p + ")")

    if not os.path.exists("plots_"+can_name):
        os.mkdir( "plots_"+can_name, 0755 );
    canvas.Print("plots_"+can_name+"/2D_stubeff_" + can_name +"_"+ label_name + ".png")
    del canvas
    gc.collect()


def compare6Hist(A,label_name="sample", can_name="can"):

    a,b,d,p = label_name.split("_")
    canvas = ROOT.TCanvas(can_name,can_name,10,10,1100,628)
    canvas.cd()
    canvas.SetGrid()
    pad_name = "pad"
    pad1=ROOT.TPad(pad_name, pad_name, 0, 0, 1, 1 , 0)
    pad1.SetGrid()
    pad1.Draw()
    pad1.cd()
#    pad1.SetLogy()
    A[0].SetTitle("")
    A[0].GetXaxis().SetTitle(b)
    A[0].GetYaxis().SetTitle('Stub Efficiency')
    A[0].SetMarkerStyle(25);
    A[1].SetMarkerStyle(20);
    A[2].SetMarkerStyle(21);
    A[3].SetMarkerStyle(22);
    A[4].SetMarkerStyle(23);
    A[5].SetMarkerStyle(4);
    
    A[0].SetMarkerColor(2);
    A[1].SetMarkerColor(3);
    A[2].SetMarkerColor(4);
    A[3].SetMarkerColor(1);
    A[4].SetMarkerColor(6);
    A[5].SetMarkerColor(7);

    A[0].SetMinimum(0);
    A[0].SetMaximum(1.2);

    A[0].Draw("p HIST SAME")
    A[1].Draw("p HIST SAME")
    A[2].Draw("p HIST SAME")
    A[3].Draw("p HIST SAME")
    A[4].Draw("p HIST SAME")
    if a == "Barrel":
        A[5].Draw("p HIST SAME")

    leg = ROOT.TLegend(0.85,0.7,1,0.98)
    if a == "Barrel":
        leg.AddEntry(A[0], "Layer 1"                           , "p");
        leg.AddEntry(A[1], "Layer 2"                           , "p");
        leg.AddEntry(A[2], "Layer 3"                           , "p");
        leg.AddEntry(A[3], "Layer 4"                           , "p");
        leg.AddEntry(A[4], "Layer 5"                           , "p");
        leg.AddEntry(A[5], "Layer 6"                           , "p");
    if a == "Endcap":
        leg.AddEntry(A[0], "Disk 1"                           , "p");
        leg.AddEntry(A[1], "Disk 2"                           , "p");
        leg.AddEntry(A[2], "Disk 3"                           , "p");
        leg.AddEntry(A[3], "Disk 4"                           , "p");
        leg.AddEntry(A[4], "Disk 5"                           , "p");

    leg.SetBorderSize(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.04)
    leg.Draw("same")

    label = ROOT.TLatex()
    label.SetTextAlign(12)
    label.SetTextFont(42)
    label.SetTextSize(0.06)
    label.SetNDC(ROOT.kTRUE)
    label.DrawLatex(0.1,0.95, a + " , "+ can_name)

    if not os.path.exists("plots_6D_stubeff"):
        os.mkdir( "plots_6D_stubeff", 0755 );

    canvas.Print("plots_6D_stubeff/" + can_name +"_"+ a + b + ".png")
    del canvas
    gc.collect()

samples = [
'FE_SWtight_Tt_Pu200_110D49.root',
'FE_SWtight_SingleMuFlatPt1p5To8_Pu0_110D49.root',
'FE_SWtight_SingleEFlatPt1p5To8_Pu0_110D49.root'
#'Tt_Pu200_110D49.root',
#'SingleMuFlatPt1p5To8_Pu200_110D49.root',
#'SingleMuFlatPt1p5To8_Pu0_110D49.root',
#'SingleEFlatPt1p5To8_Pu200_110D49.root',
#'SingleEFlatPt1p5To8_Pu0_110D49.root',
##'DisplacedMuPt1p5To8_Pu0_106D41.root',
##'DisplacedMuPt1p5To8_Pu200_106D41.root',
#'DisplacedMuPt1p5To8_Pu0_110D49.root',
#'DisplacedMuPt1p5To8_Pu200_110D49.root'
]

samplename = [
'TTbar_CMSSW_11_1_0_pre2_2026D49PU200.root',
'TTbar_CMSSW_11_2_0_pre5_2026D49PU200.root',
'SingleMuFlatPt1p5To8_CMSSW_11_1_0_pre2_2026D49noPU.root',
'SingleMuFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49PU200.root',
'SingleEFlatPt1p5To8_CMSSW_11_1_0_pre2_2026D49noPU.root',
'SingleElectronFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49PU200.root',
#'Tt_Pu200',
#'SingleMuFlatPt1p5To8_PU0',
#'SingleEFlatPt1p5To8_PU0',
]

pname = [
"pion",
"pion",
"mu",
"mu",
"ele",
"ele",
]

region = ['Barrel', 'Endcap']
SC = ['Stub', 'Cluster']
#variable = ['eta', 'pt']
variable = ['eta', 'pt']
BX = ['PBX']
directory = '/afs/crc.nd.edu/user/r/rgoldouz/L1tracker/Analysis/StubStudies/StubRateEff/hists/'

compare = {}
#compare['MuPu0vsMuPu200'] = ['SingleMuFlatPt1p5To8_Pu0_110D49.root','SingleMuFlatPt1p5To8_Pu200_110D49.root']
#compare['ElePu0vsElePu200'] = ['SingleEFlatPt1p5To8_Pu0_110D49.root', 'SingleEFlatPt1p5To8_Pu200_110D49.root']
#compare['DMuPu0vsDMuPu200'] = ['DisplacedMuPt1p5To8_Pu0_106D41.root','DisplacedMuPt1p5To8_Pu200_106D41.root']

for num, sample in enumerate(samples):
    file1 = ROOT.TFile.Open(directory + sample)
    for r in region:
        for v in variable:
            rplots=[]
            for i in range(1, 7):
                v1=r+'_'+v+'_'+str(i)+'_'+SC[0]
                v2=r+'_'+v+'_'+str(i)+'_'+SC[1]
                histA = file1.Get(v1)
                histB = file1.Get(v2)
                rP = histA.Clone()
#                compare2Hist(histA, histB, SC[0], SC[1], v1,samplename[num], pname[num] )
                rP.Divide(histB)
                rplots.append(rP)
                del histA
                del histB
#            vvv=r+'_'+v+'_'+b+'_'+pname[0]
#            compare6Hist(rplots,v1,samplename[num])                
    del file1

#compare['MuPu0'] = ['FE_TightTune_SingleMuFlatPt1p5To8_Pu0_110D49.root','FE_LooseTune_SingleMuFlatPt1p5To8_Pu0_110D49.root','FE_OldTune_SingleMuFlatPt1p5To8_Pu0_110D49.root']
#compare['ElePu0'] = ['FE_TightTune_SingleEFlatPt1p5To8_Pu0_110D49.root','FE_LooseTune_SingleEFlatPt1p5To8_Pu0_110D49.root','FE_OldTune_SingleEFlatPt1p5To8_Pu0_110D49.root']
##compare['DMuPu0'] = ['FE_TightTune_DisplacedMuPt1p5To8_Pu0_110D49.root','FE_LooseTune_DisplacedMuPt1p5To8_Pu0_110D49.root','FE_OldTune_DisplacedMuPt1p5To8_Pu0_110D49.root']
##compare['MuPu200'] = ['FE_TightTune_SingleMuFlatPt1p5To8_Pu200_110D49.root','FE_LooseTune_SingleMuFlatPt1p5To8_Pu200_110D49.root','FE_OldTune_SingleMuFlatPt1p5To8_Pu200_110D49.root']
##compare['ElePu200'] = ['FE_TightTune_SingleEFlatPt1p5To8_Pu200_110D49.root','FE_LooseTune_SingleEFlatPt1p5To8_Pu200_110D49.root','FE_OldTune_SingleEFlatPt1p5To8_Pu200_110D49.root']
##compare['DMuPu200'] = ['FE_TightTune_DisplacedMuPt1p5To8_Pu200_110D49.root','FE_LooseTune_DisplacedMuPt1p5To8_Pu200_110D49.root','FE_OldTune_DisplacedMuPt1p5To8_Pu200_110D49.root']
#
compare['Mu11_1vs112']=['SingleMuFlatPt1p5To8_CMSSW_11_1_0_pre2_2026D49noPU.root',
'SingleMuFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU.root']
compare['Pion11_1vs112']=[
'TTbar_CMSSW_11_1_0_pre2_2026D49PU200.root',
'TTbar_CMSSW_11_2_0_pre5_2026D49PU200.root']
compare['Ele11_1vs112']=[
'SingleEFlatPt1p5To8_CMSSW_11_1_0_pre2_2026D49noPU.root',
'SingleElectronFlatPt1p5To8_CMSSW_11_2_0_pre5_2026D49noPU.root']

for key, value in compare.items():
    for r in region:
        for v in variable:
            for i in range(1, 7):
                plot=[]
                plotNum=[]
                for s in value:
                    file1 = ROOT.TFile.Open(directory + s)
                    print directory + s
                    v1=r+'_'+v+'_'+str(i)+'_'+SC[0]
                    v2=r+'_'+v+'_'+str(i)+'_'+SC[1]
                    histA = file1.Get(v1)
                    histB = file1.Get(v2)
                    rP = histA.Clone()
                    rP.Divide(histB)
                    plot.append(rP)
                    plotNum.append(s.split(".")[0])
                    file1.Close()
                print v1
                compareNeffHist(plot,plotNum,v1,key)



#for num, sample in enumerate(samplename):
#    file1 = ROOT.TFile.Open(sample + 'old_stubeff_output.root')
#    file2 = ROOT.TFile.Open(sample + 'loose_stubeff_output.root')
##    file3 = ROOT.TFile.Open(sample + 'tight_stubeff_output.root')
#    file3 = ROOT.TFile.Open(sample + 'test_stubeff_output.root')
#
#file1 = ROOT.TFile.Open(samples[0])
#file2 = ROOT.TFile.Open(samples[1])
#file3 = ROOT.TFile.Open(samples[2])
#for r in region:
#    for v in variable:
#        for b in BX:
#            for i in range(0, 6):
#                v1=r+'_'+SC[0]+'_'+v+'_'+str(i)+'_'+b+'_'+pname[0]
#                v2=r+'_'+SC[1]+'_'+v+'_'+str(i)+'_'+b+'_'+pname[0]
#                histA1 = file1.Get(v1)
#                histA2 = file1.Get(v2)
#                histB1 = file2.Get(v1)
#                histB2 = file2.Get(v2)
#                histC1 = file3.Get(v1)
#                histC2 = file3.Get(v2)
#                histA1.Divide(histA2)
#                histB1.Divide(histB2)
#                histC1.Divide(histC2)
#                compare3effHist(histA1, histB1, histC1, 'oldTune', 'looseTune', 'tightTune', v1,'3d'+pname[0] )
#                del histA1
#                del histA2
#                del histB1
#                del histB2
#                del histC1
#                del histC2
