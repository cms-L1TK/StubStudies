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
category=["All", "Genuine","Combinatoric","Unknown", "GenuinePtg2GeV"]
def draw1dHist(A,textA="A", label_name="sample", can_name="can"):
    a=b=d=''
    c=0
    cc="All"
    if len(label_name.split("_"))==4:
        a,b,c,d = label_name.split("_")
    if (c not in  category):
        cc = int(c)
    else:
        cc = c
#    a,b,c,d = label_name.split("_")
#    cc = int(c)
    canvas = ROOT.TCanvas(can_name,can_name,10,10,1100,628)
    canvas.cd()

    pad_name = "pad"
    pad1=ROOT.TPad(pad_name, pad_name, 0.05, 0.05, 1, 0.99 , 0)
    pad1.Draw()

    A.SetLineColor( 1 )
    A.SetLineWidth( 2 )
    A.SetTitle("")
    A.GetXaxis().SetTitle(b)
    A.GetYaxis().SetTitle('Stub rate '+d)
    A.GetXaxis().SetTitleSize(0.05)
    A.GetYaxis().SetTitleSize(0.05)
    A.SetMaximum(1.2*A.GetMaximum())
    A.SetMinimum(0);
    A.GetYaxis().SetTitleOffset(0.7)
    if b == "nstub":
        A.GetYaxis().SetTitle('Number of module')
    if "fail" in d:
        A.GetYaxis().SetTitle('fraction of stubs '+ d)
    if b == "type":
        A.GetXaxis().SetLabelSize(0.1)
    A.Draw()
    legend = ROOT.TLegend(0.6,0.9,1,1)
    legend.AddEntry(A ,textA,'l')
    legend.SetBorderSize(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.04)
    legend.Draw("same")

    label = ROOT.TLatex()
    label.SetTextAlign(12)
    label.SetTextFont(42)
    label.SetTextSize(0.08)
    label.SetNDC(ROOT.kTRUE)
    if a == 'Barrel':
        label.DrawLatex(0.3,0.95, a + ", Layer " + str(cc))
    if a == 'Endcap':
        label.DrawLatex(0.3,0.95, a + ", Disk " + str(cc))
    if A.Integral()>0:
        canvas.Print("1D_" + can_name +"_"+ label_name + ".png")
    del canvas
    gc.collect()

def draw2dHist(inputfile = "F"):
    stub = ["_PBX","_PBXCBCfail", "_PBXCICfail"]
    text = ["rate PBX", "fraction of stubs failed by CBC/MPA", "fraction of stubs failed by CIC"]
    zscaleB = [10,0.01,0.01]
    zscaleE = [1,0.007,0.01]
    can_name = 'can'
    filem = ROOT.TFile.Open(inputfile)
    for num, st in enumerate(stub):
        for k in range(0, 6):
            canvas = ROOT.TCanvas(can_name,can_name,10,10,1100,628)
            canvas.cd()
            a = "Barrel_Rate2D_" + str(k) + st
            A = filem.Get(a)
#            if st == "_PBX" or st == "_PBXCICfail": 
#                A.GetZaxis().SetRangeUser(0, zscaleB[num])
            A.SetTitle("")
            A.GetXaxis().SetTitleSize(0.05)
            A.GetYaxis().SetTitleSize(0.05)
            A.GetYaxis().SetTitleOffset(0.7)
            A.GetXaxis().SetTitle("Module Z index");
            A.GetYaxis().SetTitle("Module #phi index")
#            A.GetZaxis().SetRangeUser(0, zscale[num])
            A.Draw("COLZ")
            label = ROOT.TLatex()
            label.SetTextAlign(12)
            label.SetTextFont(42)
            label.SetTextSize(0.06)
            label.SetNDC(ROOT.kTRUE)
            label.DrawLatex(0.1,0.95, "Barrel, Layer " + str(k+1) + "-" + text[num])
            canvas.Print("2D_" + st + a + ".png")
            del canvas
            gc.collect()
    
        for k in range(0, 5):
            cadre = ROOT.TH2F("","",30,-15.,15.,30,-15.,15.)
            canvas = ROOT.TCanvas(can_name,can_name,10,10,1000,1000)
            canvas.SetRightMargin(0.1340206)
            cadre.GetXaxis().SetLabelSize(0.)
            cadre.GetXaxis().SetLabelOffset(999)
            cadre.GetYaxis().SetLabelSize(0.)
            cadre.GetYaxis().SetLabelOffset(999)
            canvas.cd()
            cadre.Draw("col");
            a = "Endcap_Rate2D_" + str(k) + st
            for l in range(0, 15):
                b = "Endcap_Rate2D_" + str(k) + st +"_"+ str(l)
                A = filem.Get(b)
#                A.GetZaxis().SetRangeUser(0, zscaleE[num])
                if l ==3:
                    A.Draw("POL colz SAME")  
                else:
                    A.Draw("POL col SAME")
                del A
                gc.collect()
            label = ROOT.TLatex()
            label.SetTextAlign(12)
            label.SetTextFont(42)
            label.SetTextSize(0.035)
            label.SetNDC(ROOT.kTRUE)
            label.DrawLatex(0.1,0.95, "Endcap (+Z), Disk " + str(k+1)+ "-" + text[num])
            canvas.Print("2D_"+ st  + a + ".png")
            del cadre
            del canvas
            gc.collect()

def compare2Hist(A, B, textA="A", textB="B", label_name="sample", can_name="can", axis_name="eta"):
    a=b=d=''
    c=0
    cc="All"
    if len(label_name.split("_"))==4:
        a,b,c,d = label_name.split("_")
    if (c not in  category):
        cc = int(c)
    else:
        cc = c
    canvas = ROOT.TCanvas(can_name,can_name,50,50,865,780)
    canvas.cd()

    pad1=ROOT.TPad("pad1", "pad1", 0, 0.315, 1, 0.99 , 0)#used for the hist plot
    pad2=ROOT.TPad("pad2", "pad2", 0, 0.0, 1, 0.305 , 0)#used for the ratio plot
    pad1.Draw()
    pad2.Draw()
    pad2.SetGridy()
    pad2.SetTickx()
    pad1.SetBottomMargin(0.02)
    pad1.SetLeftMargin(0.14)
    pad1.SetRightMargin(0.05)
    pad2.SetTopMargin(0.1)
    pad2.SetBottomMargin(0.4)
    pad2.SetLeftMargin(0.14)
    pad2.SetRightMargin(0.05)
    pad2.SetFillStyle(0)
    pad1.SetFillStyle(0)
    pad1.cd()
    pad1.SetLogx(ROOT.kFALSE)
    pad2.SetLogx(ROOT.kFALSE)
    pad1.SetLogy(ROOT.kFALSE)
    
    A.SetLineColor( 2 )
    B.SetLineColor( 4 )    
    A.SetTitle("")
    A.GetXaxis().SetTitle(axis_name)
    A.GetXaxis().CenterTitle()
    if c==0:
        A.GetYaxis().SetTitle('TP rate')
    else:
        A.GetYaxis().SetTitle('Stub rate '+d)
    A.GetXaxis().SetTitleSize(0.05)
    A.GetYaxis().SetTitleSize(0.05)
    A.GetXaxis().SetLabelSize(0)
    if b == "nstub":
        A.GetYaxis().SetTitle('Number of module') 
    if b == "type":
        A.GetXaxis().SetBinLabel(1,"All")
        A.GetXaxis().SetBinLabel(2,"Genuine")
        A.GetXaxis().SetBinLabel(3,"Combinatoric")
        A.GetXaxis().SetBinLabel(4,"Unknown") 
    A.SetMaximum(1.4*max(A.GetMaximum(),B.GetMaximum()));
    A.SetMinimum(0.8*min(A.GetMinimum(),B.GetMinimum()));
    A.Draw()
    B.Draw('esame')
    A.Draw("AXISSAMEY+")
    A.Draw("AXISSAMEX+")

    legend = ROOT.TLegend(0.67,0.67,0.9,0.85)
    legend.AddEntry(A ,textA,'l')
    legend.AddEntry(B ,textB,'l')
    legend.SetBorderSize(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.04)
    legend.Draw("same")

    label = ROOT.TLatex()
    label.SetTextAlign(12)
    label.SetTextFont(42)
    label.SetTextSize(0.06)
    label.SetNDC(ROOT.kTRUE)
    label.DrawLatex(0.25,0.95,"CMS Phase 2 Simulation Preliminary")
    if a == 'Barrel':
        label.DrawLatex(0.2,0.85, a + ", Layer " + str(cc))
    if a == 'Endcap':
        label.DrawLatex(0.2,0.85, a + ", Disk " + str(cc))

    pad2.cd()    
    ratio = A.Clone()
    ratio.Divide(B)
    ratio.SetTitle("")
    ratio.SetMaximum(1.2)
    ratio.SetMinimum(0.8)
    ratio.GetXaxis().SetTitle(axis_name)
    ratio.GetYaxis().CenterTitle()
    ratio.GetXaxis().SetMoreLogLabels()
    ratio.GetXaxis().SetNoExponent()
    ratio.GetXaxis().SetTitleSize(0.04/0.3)
    ratio.GetYaxis().SetTitleSize(0.04/0.3)
    ratio.GetXaxis().SetTitleFont(42)
    ratio.GetYaxis().SetTitleFont(42)
    ratio.GetXaxis().SetTickLength(0.05)
    ratio.GetYaxis().SetTickLength(0.05)
    ratio.GetXaxis().SetLabelSize(0.115)
    ratio.GetYaxis().SetLabelSize(0.089)
    ratio.GetXaxis().SetLabelOffset(0.02)
    ratio.GetYaxis().SetLabelOffset(0.01)
    ratio.GetYaxis().SetTitleOffset(0.42)
    ratio.GetXaxis().SetTitleOffset(1.1)
    ratio.GetYaxis().SetNdivisions(504)
    ratio.SetStats(ROOT.kFALSE)
    ratio.GetYaxis().SetTitle('Ratio')

    ratio.Draw("e")
    ratio.Draw("AXISSAMEY+")
    ratio.Draw("AXISSAMEX+")
    print "2H_" + can_name +"_"+ label_name + " = " + str(A.Integral()) + ' , ' +str(B.Integral())
    if A.Integral()>0:
        canvas.Print("2H_" + can_name +"_"+ label_name + ".png")
    del canvas
    gc.collect()

def compare3Hist(A, B, C, textA="A", textB="B", textC="C",label_name="sample", can_name="can"):

    a,b,c,d = label_name.split("_")
    
    canvas = ROOT.TCanvas(can_name,can_name,10,10,1100,628)
    canvas.SetRightMargin(0.15)
    canvas.cd()

    pad_name = "pad"
    pad1=ROOT.TPad(pad_name, pad_name, 0.05, 0.3, 1, 0.99 , 0)
    pad1.Draw()
    pad2=ROOT.TPad(pad_name, pad_name, 0.05, 0.05, 1, 0.3 , 0)
    pad2.SetGridy();
    pad2.Draw()
    pad1.cd()

    A.SetLineColor( 1 )
    B.SetLineColor( 2 )
    C.SetLineColor( 4 )

    A.SetTitle("")
    A.GetXaxis().SetTitle(b)
    A.GetYaxis().SetTitle('Stub rate '+ d)
    A.GetXaxis().SetTitleSize(0.05)
    A.GetYaxis().SetTitleSize(0.05)
    if b == "nstub":
        A.GetYaxis().SetTitle('Number of module')
    if b == "type":
        A.GetXaxis().SetBinLabel(1,"All")
        A.GetXaxis().SetBinLabel(2,"Genuine")
        A.GetXaxis().SetBinLabel(3,"Combinatoric")
        A.GetXaxis().SetBinLabel(4,"Unknown")
    if "fail" in d:
        A.GetYaxis().SetTitle('Fraction of stubs '+ d)
    if "type"  in b:
        A.GetXaxis().SetLabelSize(0.1)
    A.SetMaximum(1.4*max(A.GetMaximum(),B.GetMaximum(),C.GetMaximum()));
    A.SetMinimum(0);
    A.GetYaxis().SetTitleOffset(0.7)
    A.Draw()
    B.Draw('esame')
    C.Draw('esame')

    legend = ROOT.TLegend(0.7,0.75,1,1)
    legend.AddEntry(A ,textA,'l')
    legend.AddEntry(B ,textB,'l')
    legend.AddEntry(C ,textC,'l')
    legend.SetBorderSize(0)
    legend.SetTextFont(42)
    legend.SetTextSize(0.05)
    legend.Draw("same")

    label = ROOT.TLatex()
    label.SetTextAlign(12)
    label.SetTextFont(42)
    label.SetTextSize(0.08)
    label.SetNDC(ROOT.kTRUE)
    category=["All", "Genuine","Combinatoric","Unknown", "GenuinePtg2GeV"] 
    if c not in category:
      cc = int(c)
      if a == 'Barrel':
          label.DrawLatex(0.2,0.95, a + ", Layer " + str(cc))
      if a == 'Endcap':
          label.DrawLatex(0.2,0.95, a + ", Disk " + str(cc))
    if c in category:
      label.DrawLatex(0.2,0.95, a + ", " + c)

    pad2.cd()
    ratioB = A.Clone()
    ratioB.Divide(B)
    ratioB.SetLineColor( 2 )
    ratioB.SetMaximum(2)
    ratioB.SetMinimum(0)
    r = ratioB.Clone()
    fontScale = 2
    nbin = ratioB.GetNbinsX()
    x_min= ratioB.GetBinLowEdge(1)
    x_max= ratioB.GetBinLowEdge(nbin)+ratioB.GetBinWidth(nbin)
#    ratio_y_min=0.95*r.GetBinContent(r.FindFirstBinAbove(0))
#    ratio_y_max=1.05*r.GetBinContent(r.GetMaximumBin())
    dummy_ratio = ROOT.TH2D("dummy_ratio","",nbin,x_min,x_max,1,0,2)
    dummy_ratio.SetStats(ROOT.kFALSE)
    dummy_ratio.GetYaxis().SetTitle('Ratio')
    dummy_ratio.GetXaxis().SetTitle(b)
    dummy_ratio.GetXaxis().SetTitleSize(0.05*fontScale)
    dummy_ratio.GetXaxis().SetLabelSize(0.05*fontScale)
    dummy_ratio.GetXaxis().SetMoreLogLabels()
    dummy_ratio.GetXaxis().SetNoExponent()
    dummy_ratio.GetYaxis().SetNdivisions(505)
    dummy_ratio.GetYaxis().SetTitleSize(0.07*fontScale)
    dummy_ratio.GetYaxis().SetLabelSize(0.05 *fontScale)
    dummy_ratio.GetYaxis().SetTitleOffset(0.3)
    dummy_ratio.Draw()
    ratioB.Draw("esame")

    ratioC = A.Clone()
    ratioC.Divide(C)
    ratioC.SetLineColor( 4 )
    ratioC.Draw("esame")

    if A.Integral()>0:
        canvas.Print("3H_" + can_name +"_"+ label_name + ".png")
    del canvas
    gc.collect()

def compare6Hist(A,label_name="sample", can_name="can", axis_name="eta"):
    a=b=d=''
    c=0
    cc="All"
    if len(label_name.split("_"))==4:
        a,b,c,d = label_name.split("_")
    if (c not in  category):
        cc = int(c)
    else:
        cc = c
    canvas = ROOT.TCanvas(can_name,can_name,10,10,1100,628)
    canvas.cd()

    pad_name = "pad"
    pad1=ROOT.TPad(pad_name, pad_name, 0, 0, 1, 1 , 0)
    pad1.Draw()
    pad1.cd()
#    pad1.SetLogy()
    A[0].SetTitle("")
    A[0].GetXaxis().SetTitle(axis_name)
    A[0].GetXaxis().CenterTitle()
    if c==0:
        A[0].GetYaxis().SetTitle('TP rate')
    else:
        A[0].GetYaxis().SetTitle('Stub rate '+d)
    A[0].GetXaxis().SetTitleSize(0.05)
    A[0].GetYaxis().SetTitleSize(0.05)
    A[0].GetXaxis().SetLabelSize(0)
    if b == "nstub":
        A[0].GetYaxis().SetTitle('Number of module')
    if b == "type":
        A[0].GetXaxis().SetBinLabel(1,"All")
        A[0].GetXaxis().SetBinLabel(2,"Genuine")
        A[0].GetXaxis().SetBinLabel(3,"Combinatoric")
        A[0].GetXaxis().SetBinLabel(4,"Unknown")
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

    A[0].SetTitle("");
#    A[0].GetXaxis().SetTitleSize(0.08);
#    A[0].GetYaxis().SetTitleSize(0.06);
#    A[0].GetYaxis().SetTitleOffset(0.5);
#    A[0].GetXaxis().SetLabelSize(0.08);
    A[0].SetMinimum(0);
    A[0].SetMaximum(1.2*A[0].GetMaximum());

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
    label.SetTextSize(0.08)
    label.SetNDC(ROOT.kTRUE)
    label.DrawLatex(0.1,0.95, a + " , "+ can_name)

    canvas.Print("6D_" + can_name +"_"+ label_name + ".png")
#    canvas.Print("6D_"+a+"_"+b+can_name + ".png")
    del canvas
    gc.collect()


directory = '/afs/crc.nd.edu/user/r/rgoldouz/L1tracker/Analysis/StubStudies/StubRateEff/hists/'
samples = [
#'Tt_Pu200_110D49.root', 'Tt_Pu200_106D41.root'
#'DisplacedMuPt1p5To8_Pu0_106D41.root',  'DisplacedMuPt2To100_Pu0_110D49.root'
#'DisplacedMuPt1p5To8_Pu0_106D41.root','DisplacedMuPt1p5To8_Pu0_110D49.root'
#'FE_Tt_Pu200_110D49.root', 'Tt_Pu200_110D49.root'
#'TT.root'
#'pre5test.root'
#'L1Stub_Tt_Pu200_111pre2.root'
#'FE_SWtight_Tt_Pu200_110D49.root'
#,'L1Stub_Tt_Pu200_112pre5_New.root'
#'FE_TightTune_Tt_Pu200_110D49.root','FE_LooseTune_Tt_Pu200_110D49.root','FE_OldTune_Tt_Pu200_110D49.root'i
#'TTbar_CMSSW_11_2_0_pre5_2026D49PU200.root','TTbar_CMSSW_11_1_0_pre2_2026D49PU200.root'
'TTbar_CMSSW_11_2_0_pre5_2026D49PU200.root', 'TTbar_RezaTune_CMSSW_11_2_0_pre5_2026D49PU200.root'
]

samplename = [
#'tt_Pu200_110D49','tt_Pu200_106D41'
#'DMu_Pu0_106D41',  'DMu_Pu0_110D49'
#'DMu_Pu0_106D41','DMu_Pu0_110D49'
#'FE_ON', 'FE_OFF'
#"tt_Pu200_110D49"
#"test","tt Pu200 (TightTune)", "tt Pu200 (LooseTune)","tt Pu200 (OldTune)"
#'tt_Pu200_112pre5','tt_Pu200_111pre2'
'tt_Pu200_TightTune','tt_Pu200_NewTune'
]
cn = '11x'
region = ['Barrel', 'Endcap']
variable = ['rho','type', 'eta', 'z']
variable_axisName = ['#rho (cm)','Stub type', '#eta', 'z (cm)','Number of stubs']
twoDvariable = ['Rate2D']
#BX = ['PBX', 'PBXPmodule','PBXCICfail','PBXCBCfail']
BX = ['PBX', 'PBXCICfail','PBXCBCfail']
category=["All", "Genuine","Combinatoric","Unknown", "GenuinePtg2GeV"]

onedinputPlots = []
onedinputLabel = []

onedinputPlotsTP = []
onedinputLabelTP = []
for r in region:
    for n,v in enumerate(variable):
        for b in BX:
            for i in range(1, 7):
                onedinputPlots.append(r+'_'+v+'_'+str(i)+'_'+b)
                onedinputLabel.append(variable_axisName[n])

for r in region:
    for b in BX:
        for c in category:
            onedinputPlots.append(r+'_Layer_'+c+'_'+b)
            onedinputLabel.append('Layer')

TPvars=   ["etaPtg2","pt","nstub","dxy","d0","d0_prod","z0","z0_prod", "etaPtg2SLg4"]
for n,v in enumerate(TPvars):
    onedinputPlotsTP.append('TP_'+v)
    onedinputLabelTP.append(v)

#onedinputPlots.append('BarrelpEndcap_type_*_PBX')
#onedinputPlots.append('BarrelpEndcap_eta_*_PBX')

twodinputPlots = []
for r in region:
    for v in twoDvariable:
        for b in BX:
            for i in range(0, 6):
                twodinputPlots.append(r+'_'+v+'_'+str(i)+'_'+b)

sixdinputPlots=[]
sixdinputLabel = []

for r in region:
    for n,v in enumerate(variable):
        for b in BX:
            arr = []
            for i in range(1, 7):
                arr.append(r+'_'+v+'_'+str(i)+'_'+b)
            sixdinputPlots.append(arr)
            sixdinputLabel.append(variable_axisName[n])

is1D = False
is2D = True
is3D = False

if is1D:
    for num, sample in enumerate(samples):
        file1 = ROOT.TFile.Open(directory + sample)
        for v in onedinputPlots:
            if v not in  [file1.GetListOfKeys()[ih].GetName() for ih in range(file1.GetListOfKeys().GetSize())]:
                print('do not find the hist ' + v)
                continue
#            print samplename[num]
            print v
            histA = file1.Get(v)
            draw1dHist(histA, samplename[num], v,cn )
            del histA
        os.system("mkdir plot_rate1D" + samplename[num])
        os.system("mv *.png plot_rate1D" + samplename[num])
        draw2dHist(directory + sample)
        os.system("mkdir plot_rate2D" + samplename[num])
        os.system("mv *.png plot_rate2D" + samplename[num])
        for n,v in enumerate(sixdinputPlots):
#        for v in sixdinputPlots:
            print v[0]
            if v[0] not in  [file1.GetListOfKeys()[ih].GetName() for ih in range(file1.GetListOfKeys().GetSize())]:
                continue
            plots1=[]
            for i in range(0, 6):
                plots1.append(file1.Get(v[i]))
            compare6Hist(plots1,v,cn,sixdinputLabel[n])
    
if is2D:
    file1 = ROOT.TFile.Open(directory+samples[0])
    file2 = ROOT.TFile.Open(directory+samples[1])
    for n,v in enumerate(onedinputPlots):
        if v not in  [file1.GetListOfKeys()[ih].GetName() for ih in range(file1.GetListOfKeys().GetSize())]:
            continue
        if v not in  [file2.GetListOfKeys()[ih].GetName() for ih in range(file2.GetListOfKeys().GetSize())]:
            continue
        a,b,c,d = v.split("_")
        histA = file1.Get(v)
        histB = file2.Get(v)
        if d=='PBXCICfail' or d=='PBXCBCfail':
            histA.Divide(file1.Get(a+'_'+b+'_'+c+'_PBX'))
            histB.Divide(file2.Get(a+'_'+b+'_'+c+'_PBX'))
        compare2Hist(histA, histB, samplename[0], samplename[1], v,cn,onedinputLabel[n] )
        del histA
        del histB

    for n,v in enumerate(onedinputPlotsTP):
        if v not in  [file1.GetListOfKeys()[ih].GetName() for ih in range(file1.GetListOfKeys().GetSize())]:
            continue
        if v not in  [file2.GetListOfKeys()[ih].GetName() for ih in range(file2.GetListOfKeys().GetSize())]:
            continue
        histA = file1.Get(v)
        histB = file2.Get(v)
        if 'etaPtg2SLg4' in v:
            histA.Divide(file1.Get('TP_'+ 'etaPtg2'))
            histB.Divide(file2.Get('TP_'+ 'etaPtg2'))
        compare2Hist(histA, histB, samplename[0], samplename[1], v,cn,onedinputLabelTP[n] )
        del histA
        del histB


#    for v in sixdinputPlots:
#        print v[0]
#        if v[0] not in  [file1.GetListOfKeys()[ih].GetName() for ih in range(file1.GetListOfKeys().GetSize())]:
#            continue
#        plots1=[]
#        plots2=[]
#        for i in range(0, 6):
#            plots1.append(file1.Get(v[i]))
#            plots2.append(file2.Get(v[i]))
#        compare6Hist(plots1, v[0],samplename[0])
#        compare6Hist(plots2, v[0],samplename[1])

if is3D:
    file1 = ROOT.TFile.Open(directory+samples[0])
    file2 = ROOT.TFile.Open(directory+samples[1])
    file3 = ROOT.TFile.Open(directory+samples[2])
    for v in onedinputPlots:
        if v not in  [file1.GetListOfKeys()[ih].GetName() for ih in range(file1.GetListOfKeys().GetSize())]:
            continue
        if v not in  [file2.GetListOfKeys()[ih].GetName() for ih in range(file2.GetListOfKeys().GetSize())]:
            continue
        if v not in  [file3.GetListOfKeys()[ih].GetName() for ih in range(file2.GetListOfKeys().GetSize())]:
            continue
        a,b,c,d = v.split("_")
        histA = file1.Get(v)
        histB = file2.Get(v)
        histC = file3.Get(v)
        if d=='PBXCICfail' or d=='PBXCBCfail':
            histA.Divide(file1.Get(a+'_'+b+'_'+c+'_PBX'))
            histB.Divide(file2.Get(a+'_'+b+'_'+c+'_PBX'))
            histC.Divide(file3.Get(a+'_'+b+'_'+c+'_PBX'))
        compare3Hist(histA, histB, histC, samplename[0], samplename[1], samplename[2], v,cn )
        del histA
        del histB
        del histC

     
