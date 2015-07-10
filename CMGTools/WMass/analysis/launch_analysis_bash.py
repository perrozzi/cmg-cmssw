#!/usr/local/bin/python

import urllib, urlparse, string, time, os, shutil, sys, math, subprocess

## ==============================================================
## STEERING PARAMETERS
## ==============================================================

useLHAPDF = False

# foldername = "test2_zm_pdf";
# foldername = "test_efficiencies";
# foldername = "test_bosonpt";
# foldername = "test_newstd";
# foldername = "test_nnpdf23x0";
# foldername = "test_RecApr12";
# foldername = "test_Recoil13Apr";
# foldername = "test_Recoil13Aprnobkg";
# foldername = "test_preapproval_norecoil";
foldername = "testdummy";
foldername_orig=foldername

ntuple_folder = "root://eoscms//eos/cms/store/group/phys_smp/Wmass/perrozzi/ntuples/ntuples_2014_05_23_53X/";
ntuple_folder_8TeV_ABC = "root://eoscms//eos/cms/store/group/phys_smp/Wmass/perrozzi/ntuples/ntuples_2014_08_19_53X_8TeV/";
# ntuple_folder = "root://eoscms//eos/cms/store/group/phys_smp/Wmass/perrozzi/ntuples/ntuples_2013_09_14/";
# ntuple_folder = "root://eoscms//eos/cms/store/group/phys_smp/Wmass/perrozzi/ntuples/ntuples_2013_10_15/";
# ntuple_folder = "root://eoscms//eos/cms/store/cmst3/user/perrozzi/CMG/ntuples_2012_12_20/";
# ntuple_folder = "root://eoscms//eos/cms/store/group/phys_smp/Wmass/perrozzi/ntuples/ntuples_2012_07_02/";
# ntuple_folder = "~/eos/cms/store/cmst3/user/perrozzi/CMG/ntuples_2012_12_20/";
lhapdf_folder="/afs/cern.ch/work/p/perrozzi/private/WMassMC/lhapdf/"

use_PForNoPUorTKmet = 2; # 0:PF, 1:NOPU, 2:TK 
use_LHE_weights = 0; # 0=no, 1=yes
usePileupSF = 1; # 0=no, 1=yes
useEffSF = 2; # 0=no, 1=MuonPOG, 2=Heiner
# usePtSF = sys.argv[1]; # Boson pT reweighting: 0=no, 1=yes
usePtSF = 0; # Boson pT reweighting: -1=none, 0=data, 1...=other options
useMomentumCorr = 3; # 0=none, 1=Rochester, 2=MuscleFit, 3=KalmanCorrector
GlobalSscaleMuonCorrNsigma = 0;
MuonCorrToys = 0;
usePhiMETCorr = 0; # 0=none, 1=yes
useRecoilCorr = 2; # 0=none, 1=yes, 2=PDFw3gaus
RecoilCorrNVarAll = 1;
# RecoilCorrNVarAll = 0;
RecoilCorrVarDiagoParU1orU2fromDATAorMC = "0"; # SYST VARIATIONS: 0=NONE, 1= U1 DATA p1, 2= U1 DATA p2, 3= U2 DATA, 4= U1 MC p1, 5= U1 MC p1, 6= U1 MC p1
RecoilCorrVarDiagoParSigmas = "0"; # 0=none, 1=yes
RecoilCorrNonClosure = "0";                  # 0...16 =none, 1=yes
syst_ewk_Alcaraz = "-1"; # -1=none, 0=fixed POWHEG QCD+EWK NLO
# LHAPDF_reweighting_sets="11200" # cteq6ll.LHpdf=10042 CT10nnlo.LHgrid=11200, NNPDF23_nnlo_as_0118.LHgrid=232000, MSTW2008nnlo68cl.LHgrid=21200
# LHAPDF_reweighting_members="51" # cteq6ll.LHpdf=1 CT10nnlo.LHgrid=51, NNPDF23_nnlo_as_0118.LHgrid=100, MSTW2008nnlo68cl.LHgrid=41
# LHAPDF_reweighting_sets="10042" # cteq6ll.LHpdf=10042 CT10nnlo.LHgrid=11200, NNPDF23_nnlo_as_0118.LHgrid=232000, MSTW2008nnlo68cl.LHgrid=21200
# LHAPDF_reweighting_members="1" # cteq6ll.LHpdf=1 CT10nnlo.LHgrid=51, NNPDF23_nnlo_as_0118.LHgrid=100, MSTW2008nnlo68cl.LHgrid=41
# LHAPDF_reweighting_sets="232000" # cteq6ll.LHpdf=10042 CT10nnlo.LHgrid=11200, NNPDF23_nnlo_as_0118.LHgrid=232000, MSTW2008nnlo68cl.LHgrid=21200
# LHAPDF_reweighting_members="1" # cteq6ll.LHpdf=1 CT10nnlo.LHgrid=51, NNPDF23_nnlo_as_0118.LHgrid=100, MSTW2008nnlo68cl.LHgrid=41
LHAPDF_reweighting_sets="229800" # cteq6ll.LHpdf=10042 CT10nnlo.LHgrid=11200, NNPDF23_nnlo_as_0118.LHgrid=232000, MSTW2008nnlo68cl.LHgrid=21200
LHAPDF_reweighting_members="1" # cteq6ll.LHpdf=1 CT10nnlo.LHgrid=51, NNPDF23_nnlo_as_0118.LHgrid=100, MSTW2008nnlo68cl.LHgrid=41
# LHAPDF_reweighting_sets="11000" # cteq6ll.LHpdf=10042 CT10nnlo.LHgrid=11200, NNPDF23_nnlo_as_0118.LHgrid=232000, MSTW2008nnlo68cl.LHgrid=21200
# LHAPDF_reweighting_members="53" # cteq6ll.LHpdf=1 CT10nnlo.LHgrid=51, NNPDF23_nnlo_as_0118.LHgrid=100, MSTW2008nnlo68cl.LHgrid=41
## CHOOSE WETHER IS MC CLOSURE OR NOT (half statistics used as DATA, half as MC)
IS_MC_CLOSURE_TEST= 0;

indip_normalization_lumi_MC = 0; # independent normalization of MC in fb-1 (otherwise normalized to DATA)
intLumi_MC_fb = 81293448/31314/1e3;# data = 4.7499 fb-1 prescaled trigger, 5.1 fb-1 unprescaled; works only if indip_normalization_lumi_MC is TRUE
useAlsoGenPforSig= 1;

ZMassCentral_MeV = "91188"; # 91.1876
WMassCentral_MeV = "80398"; # 80385
WMassSkipNSteps = "5"; # 15
etaMuonNSteps = "1"; # 5
etaMaxMuons = "0.9"; # 0.6, 0.8, 1.2, 1.6, 2.1

# DATA, WJetsPowPlus,  WJetsPowNeg,  WJetsMadSig,  WJetsMadFake,  DYJetsPow,  DYJetsMadSig,  DYJetsMadFake,   TTJets,   ZZJets,   WWJets,  WZJets,  QCD, T_s, T_t, T_tW, Tbar_s, Tbar_t, Tbar_tW
# resumbit_sample = "DATA, WJetsMadSig,  WJetsMadFake,  DYJetsPow,  DYJetsMadFake,   TTJets,   ZZJets,   WWJets,  WZJets,  QCD, T_s, T_t, T_tW, Tbar_s, Tbar_t, Tbar_tW" 
resumbit_sample = "DYJetsPow" # DATA, WJetsPowPlus,  WJetsPowNeg,  WJetsMadSig,  WJetsMadFake,  DYJetsPow,  DYJetsMadSig,  DYJetsMadFake,   TTJets,   ZZJets,   WWJets,  WZJets,  QCD, T_s, T_t, T_tW, Tbar_s, Tbar_t, Tbar_tW
# resumbit_sample = "DATA, WJetsPowPlus,  WJetsPowNeg,  WJetsMadSig,  WJetsMadFake,  TTJets,   ZZJets,   WWJets,  WZJets,  QCD, T_s, T_t, T_tW, Tbar_s, Tbar_t, Tbar_tW"
#resumbit_sample = "DATA, DYJetsMadSig"
#resumbit_sample = "DATA, DYJetsMadSig ,DYJetsPow"
# resumbit_sample = "DATA"
#resumbit_sample = "DATA, DYJetsPow"
#resumbit_sample = "WJetsMadSig"#WJetsPowPlus"
#resumbit_sample = "WJetsPowPlus"

parallelize = 0;
useBatch = 0;
batchQueue = "1nh";
WMassNSteps = "5"; # 60
# WMassNSteps = "0"; # 60

runWanalysis = 0;
runZanalysis = 1;
resubmit = 0;
controlplots = 0;

mergeSigEWKbkg = 0;

## PERFORM W or Z MASS FIT
fit_W_or_Z = "Z" # "W,Z" or "W" or "Z"

usePowOrMadForSig = "POWHEG"; # use "POWHEG" or use "MADGRAPH"
runPrepareDataCardsFast = 0; # ALTERNATIVE FAST WAY: TEMPLATES ARE IN THE SYsT FOLDER, PSEUDO-DATA IN THE LOCAL FOLDER
DataCards_systFromFolder="" # evaluate systematics wrt folder (or leave it empty)

## NEW FIT
print "if it doesn't work, try with this first: cd /afs/cern.ch/work/p/perrozzi/private/CMGTools/CMGTools/CMSSW_5_3_3_patch3/src; SCRAM_ARCH slc5_amd64_gcc462;cmsenv; cd -";
runClosureTestLikeLihoodRatioAnsMergeResults = 0;
mergeResults = 0;

#######################
### PLOTTING ###
#######################
runWSigBkgFit = 0;
runZSigBkgFit = 0;

run_Z_MCandDATAcomparisons_stack = 0;
run_W_MCandDATAcomparisons_stack = 0;
run_PhiStarEta_MCandDATAcomparisons_stack = 0;
run_Z_MCandDATAcomparison = 0;
run_W_MCandDATAcomparison = 0;

run_ZvsWlike_comparisonMC   = 0;
run_ZvsWlike_comparisonDATA = 0;

runWandZcomparisonMC   = 0;
runWandZcomparisonDATA = 0;

#######################
## OBSOLETE STUFF
#######################

## OLD FIT
runPrepareDataCards = 0;     # TEMPLATES ARE IN THE LOCAL FOLDER, PSEUDO-DATA IN THE SYsT FOLDER
if(use_PForNoPUorTKmet==0): # 0:PF, 1:NOPU, 2:TK 
    sysfoldmet="_pfmet";
elif(use_PForNoPUorTKmet==1): # 0:PF, 1:NOPU, 2:TK 
    sysfoldmet="_pfnopu";
elif(use_PForNoPUorTKmet==2): # 0:PF, 1:NOPU, 2:TK 
    sysfoldmet="_tkmet";
# DataCards_systFromFolder=foldername_orig+sysfoldmet+"_RochCorr_RecoilCorr_EffHeinerSFCorr_PileupSFCorr" # evaluate systematics wrt folder (or leave it empty)

ExtractNumbers = 0; # NOT REALLY USED
run_BuildEvByEvTemplates= 0; # NOT REALLY USED
runDataCardsParametrization = 0; # NOT REALLY USED

## PRODUCE R(X)=W/Z DISTRIBUTION TO REWEIGHT Z in DATA
runR_WdivZ= 0;
## PRODUCE TEMPLATES, i.e. Z(DATA)*R(X)
run_BuildSimpleTemplates= 0;

runPhiStarEta = 0;

## END STEERING PARAMETERS
## ============================================================== #
## ============================================================== #
## ============================================================== #

# if RecoilCorrNVarAll != 0 or GlobalSscaleMuonCorrNsigma != 0 or usePhiMETCorr != 0 \
    # or useRecoilCorr != 1 or RecoilCorrVarDiagoParSigmas != "0" or RecoilCorrNonClosure != "0" \
    # or syst_ewk_Alcaraz != "0" 
if RecoilCorrVarDiagoParU1orU2fromDATAorMC != "0" or LHAPDF_reweighting_members !="1":
  WMassNSteps = "0"

print "cd /afs/cern.ch/work/p/perrozzi/private/CMSSW_6_1_1/src; SCRAM_ARCH=slc5_amd64_gcc462;eval `scramv1 runtime -sh`; cd -;"

if(use_PForNoPUorTKmet==0): # 0:PF, 1:NOPU, 2:TK 
    foldername+="_pfmet";
elif(use_PForNoPUorTKmet==1): # 0:PF, 1:NOPU, 2:TK 
    foldername+="_pfnopu";
elif(use_PForNoPUorTKmet==2): # 0:PF, 1:NOPU, 2:TK 
    foldername+="_tkmet";

if(use_LHE_weights==1):
    foldername+="_LHEweights";

if(IS_MC_CLOSURE_TEST==1):
    foldername+="_MCclosureTest";
    # useEffSF=0;
    # usePtSF=0;
    # usePileupSF=0;
    
if(syst_ewk_Alcaraz>-1): 
  foldername+="_ewk"+str(syst_ewk_Alcaraz);

if(MuonCorrToys>0):
  MuonCorrToys=200
if(MuonCorrToys<1):
  MuonCorrToys=1
if(RecoilCorrNVarAll<1):
  RecoilCorrNVarAll=1
if(useMomentumCorr==1): 
  foldername+="_RochCorr";
  if(GlobalSscaleMuonCorrNsigma!=0): 
    foldername+=str(GlobalSscaleMuonCorrNsigma)+"s_smear";
elif(useMomentumCorr==2): foldername+="_MuscleFitCorr";
elif(useMomentumCorr==3): 
  foldername+="_KalmanCorr";
  if(MuonCorrToys>1): 
    foldername+="Toys";
  if(GlobalSscaleMuonCorrNsigma!=0): 
    foldername+=str(GlobalSscaleMuonCorrNsigma)+"s_smear";
if(usePhiMETCorr==1): 
  foldername+="_phiMETcorr";
if(useRecoilCorr>0): 
  foldername+="_RecoilCorr"+str(useRecoilCorr);
  # if(("0" not in RecoilCorrNonClosure) or ("0" not in RecoilCorrVarDiagoParU1orU2fromDATAorMC)):
    # foldername+="_Resol_U1_"+str(RecoilCorrNonClosure)+"_U2_"+str(RecoilCorrVarDiagoParU1orU2fromDATAorMC);
  if(RecoilCorrVarDiagoParU1orU2fromDATAorMC=="1"):
    foldername+="_U1Datap1";
  elif(RecoilCorrVarDiagoParU1orU2fromDATAorMC=="2"):
    foldername+="_U1Datap2";
  elif(RecoilCorrVarDiagoParU1orU2fromDATAorMC=="3"):
    foldername+="_U2Data";
  elif(RecoilCorrVarDiagoParU1orU2fromDATAorMC=="4"):
    foldername+="_U1MCp1";
  elif(RecoilCorrVarDiagoParU1orU2fromDATAorMC=="5"):
    foldername+="_U1MCp2";
  elif(RecoilCorrVarDiagoParU1orU2fromDATAorMC=="6"):
    foldername+="_U2MC";
  if(("0" not in RecoilCorrVarDiagoParSigmas)):
    foldername+="_RecCorrVarSigma_"+str(RecoilCorrVarDiagoParSigmas);
if(RecoilCorrNonClosure=="1"):
    foldername+="_NonClosure";

if(useEffSF==1): foldername+="_EffSFCorr";
if(useEffSF==2): foldername+="_EffHeinerSFCorr";
if(int(usePtSF)!=-1): foldername+="_PtSFCorr"+str(usePtSF);
if(usePileupSF==1): foldername+="_PileupSFCorr";
DATA, WJetsPowPlus,  WJetsPowNeg,  WJetsMadSig,  WJetsMadFake,  DYJetsPow,  DYJetsMadSig,  DYJetsMadFake,   TTJets,   ZZJets,   WWJets,  WZJets,  QCD, T_s, T_t, T_tW, Tbar_s, Tbar_t, Tbar_tW = range(19)

sample      = [ "DATA" , "WJetsPowPlus", "WJetsPowNeg", "WJetsMadSig",    "WJetsMadFake", "DYJetsPow", "DYJetsMadSig", "DYJetsMadFake",  "TTJets",  "ZZJets",  "WWJets", "WZJets",   "QCD", "T_s", "T_t", "T_tW", "Tbar_s", "Tbar_t", "Tbar_tW"];
isMCorDATA  = [      1 ,            0  ,          0   ,            0 ,                0 ,         0  ,            0  ,              0 ,         0,         0,         0,        0,       0,     0,     0,      0,        0,        0,     0    ];
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSections or MCM
#                               POWHEG            POWHEG        MADGRAPH     MADGRAPH      POWHEG         POWHEG      twiki       twiki     twiki     twiki     twiki  twiki  twiki  twiki  twiki  twiki  twiki  
CS_pb       = [     -1 ,         5913  ,        4126  ,        31314 ,            31314 ,       950  ,        2895.6 ,         2895.6 ,      165 ,       5.9,      43  ,    18.2 , 84679.3,  2.72,  42.6,    5.3,     1.49,       22,       5.3];
Nevts       = [141327580,     131310100,    109963100 ,      77571005,          77571005,    60235900,      34705858 ,       34705858 ,  54618956,  3899263 ,  3935865 ,  3860146,24939986,229786,3249552,744859,   139258,  1943163,    801626]; # 53X
int_lumi_fb = [     5.1 ,           0  ,            0 ,           0  ,                0 ,          0 ,              0,              0 ,       0  ,       0  ,        0 ,        0,       0,     0,      0,     0,        0,        0,         0];
# int_lumi_fb = [       (81293448/31314/1e3) ,        0  ,          0 ,        0   ,           0 ,        0 ,       0  ,       0  ,       0 ,        0   ];
Nevts_Per_fb= [      0  ,            0 ,          0   ,            0 ,                0 ,          0 ,            0  ,             0  ,        0 ,         0,         0,        0,       0,     0,      0,     0,        0,        0,         0];
generated_PDF_set =     [LHAPDF_reweighting_sets,229800,229800, 10042,            10042 ,      229800,         10042 ,          10042 ,    10042 ,     10042,     10042,    10042,   10042, 10042,  10042, 10042,    10042,    10042,     10042];
generated_PDF_member =  [LHAPDF_reweighting_members,0 ,       0 ,   0,                0 ,          0 ,             0 ,              0 ,        0 ,         0,         0,        0,       0,     0,      0,     0,        0,        0,        0 ];
gen_mass_value_MeV  =   [  0  ,  80398 ,        80398 ,         80419,            91188 ,       91188,         91188 ,              0 ,        0 ,         0,         0,        0,       0,     0,      0,     0,        0,        0,        0 ];
contains_LHE_weights =  [  0  ,      1 ,            1 ,             0,                0 ,           1,             0 ,              0 ,        0 ,         0,         0,        0,       0,     0,      0,     0,        0,        0,        0 ];
nsamples=len(sample);

if(use_LHE_weights==0):
  for i in range(len(contains_LHE_weights)):
    contains_LHE_weights[i] = 0

### FROM THE POWHEG CONFIGURATION FILE ###
# ZMassCentral_MeV = "91.188"; # 91.1876
# WMassCentral_MeV = "80419"; # 80385
# WMassNSteps
Zmass_Steps = []
Wmass_Steps = []

dummy_deltaM_MeV = []
dummy_deltaM_MeV_central_Index = 0
counter=0

for x in xrange(-302,-102,4):
  dummy_mass_step = float(x)
  dummy_deltaM_MeV.insert(counter,"%.0f" % dummy_mass_step)
  # print counter, x, dummy_mass_step, dummy_deltaM_MeV[counter]
  counter=counter+1

for x in xrange(-102,102,2):
  dummy_mass_step = float(x)
  if(dummy_mass_step==0): dummy_deltaM_MeV_central_Index = counter
  dummy_deltaM_MeV.insert(counter,"%.0f" % dummy_mass_step)
  # print counter, x, dummy_mass_step, dummy_deltaM_MeV[counter]
  counter=counter+1

for x in xrange(102,302,4):
  dummy_mass_step = float(x)
  dummy_deltaM_MeV.insert(counter,"%.0f" % dummy_mass_step)
  # print counter, x, dummy_mass_step, dummy_deltaM_MeV[counter]
  counter=counter+1

# print dummy_deltaM_MeV
# print dummy_deltaM_MeV_central_Index

Wmass_values_array = ""
Zmass_values_array = ""
if(WMassSkipNSteps=="0"): WMassSkipNSteps = "1"
counter=0

for i in xrange(-int(WMassNSteps),int(WMassNSteps)+1):
  WmassJoin_string = str(gen_mass_value_MeV[WJetsPowPlus]+int(round(float(dummy_deltaM_MeV[dummy_deltaM_MeV_central_Index+(int(WMassSkipNSteps))*i]))))
  if(counter>0): Wmass_values_array = ''.join((Wmass_values_array, ","))
  Wmass_values_array = ''.join((Wmass_values_array, WmassJoin_string))
  ZmassJoin_string = str(gen_mass_value_MeV[DYJetsPow]+int(round(float(dummy_deltaM_MeV[dummy_deltaM_MeV_central_Index+(int(WMassSkipNSteps))*i]))))
  if(counter>0): Zmass_values_array = ''.join((Zmass_values_array, ","))
  Zmass_values_array = ''.join((Zmass_values_array, ZmassJoin_string))
  counter = counter+1

# print Wmass_values_array
# print Zmass_values_array
# sys.exit()

##################################################
### TEMP: WAITING TO RECOVER THE FULL DATASET ####
##################################################
Nevts[DYJetsPow] /= 2
##################################################

fWana_str = [
  ntuple_folder+"DATA/WTreeProducer_tree_RecoSkimmed.root",
  ntuple_folder+"WPlusPOWHEG/WTreeProducer_tree.root",
  ntuple_folder+"WMinusPOWHEG/WTreeProducer_tree.root",
  ntuple_folder+"WJetsLL/WTreeProducer_tree_SignalRecoSkimmed.root",
  ntuple_folder+"WJetsLL/WTreeProducer_tree_FakeRecoSkimmed.root",
  ntuple_folder+"DYJetsMM/WTreeProducer_tree_SignalRecoSkimmed.root",
  ntuple_folder+"DYJetsLL/WTreeProducer_tree_SignalRecoSkimmed.root",
  ntuple_folder+"DYJetsLL/WTreeProducer_tree_FakeRecoSkimmed.root",
  ntuple_folder+"TTJets/WTreeProducer_tree.root",
  ntuple_folder+"VVJets/ZZ/WTreeProducer_tree.root",
  ntuple_folder+"VVJets/WW/WTreeProducer_tree.root",
  ntuple_folder+"VVJets/WZ/WTreeProducer_tree.root",
  ntuple_folder+"QCD/QCD20Mu15/WTreeProducer_tree.root",
  ntuple_folder+"SingleTop/T_s/WTreeProducer_tree.root",
  ntuple_folder+"SingleTop/T_t/WTreeProducer_tree.root",
  ntuple_folder+"SingleTop/T_tW/WTreeProducer_tree.root",
  ntuple_folder+"SingleTop/Tbar_s/WTreeProducer_tree.root",
  ntuple_folder+"SingleTop/Tbar_t/WTreeProducer_tree.root",
  ntuple_folder+"SingleTop/Tbar_tW/WTreeProducer_tree.root"
];  
  
fZana_str = [
#  ntuple_folder_8TeV_ABC+"DATA_Run2012ABCD/ZTreeProducer_tree.root", # this is the 8TeV data contain also the tkmetABC
  ntuple_folder+"DATA/ZTreeProducer_tree_RecoSkimmed.root",
  ntuple_folder+"WJetsLL/ZTreeProducer_tree_SignalRecoSkimmed.root",
  ntuple_folder+"WJetsLL/ZTreeProducer_tree_SignalRecoSkimmed.root",
  ntuple_folder+"WJetsLL/ZTreeProducer_tree_SignalRecoSkimmed.root",
  ntuple_folder+"WJetsLL/ZTreeProducer_tree_FakeRecoSkimmed.root",
  ntuple_folder+"DYJetsMM/ZTreeProducer_tree_SignalRecoSkimmed.root",
  # ntuple_folder+"DYJetsMM/InclWeights/ZTreeProducer_tree.root",
  # ntuple_folder+"DYJetsMM/allEvts/ZTreeProducer_tree.root",
#  ntuple_folder_8TeV_ABC+"DYJetsLL/ZTreeProducer_tree_tkmetABC.root",  # this is the 8TeV DYJetsLL contains also the tkmetABC
  ntuple_folder+"DYJetsLL/ZTreeProducer_tree_SignalRecoSkimmed.root",
  ntuple_folder+"DYJetsLL/ZTreeProducer_tree_FakeRecoSkimmed.root",
  ntuple_folder+"TTJets/ZTreeProducer_tree.root",
  ntuple_folder+"VVJets/ZZ/ZTreeProducer_tree.root",
  ntuple_folder+"VVJets/WW/ZTreeProducer_tree.root",
  ntuple_folder+"VVJets/WZ/ZTreeProducer_tree.root",
  ntuple_folder+"QCD/QCD20Mu15/ZTreeProducer_tree.root",
  ntuple_folder+"SingleTop/T_s/ZTreeProducer_tree.root",
  ntuple_folder+"SingleTop/T_t/ZTreeProducer_tree.root",
  ntuple_folder+"SingleTop/T_tW/ZTreeProducer_tree.root",
  ntuple_folder+"SingleTop/Tbar_s/ZTreeProducer_tree.root",
  ntuple_folder+"SingleTop/Tbar_t/ZTreeProducer_tree.root",
  ntuple_folder+"SingleTop/Tbar_tW/ZTreeProducer_tree.root"
];

print os.getcwd()
print ".! cp "+os.path.basename(__file__)+" JobOutputs/"+foldername;
file_dest="JobOutputs/"+foldername+"/"+os.path.basename(__file__);
if not os.path.exists("JobOutputs/"+foldername):
    os.makedirs("JobOutputs/"+foldername)
shutil.copyfile(os.path.basename(__file__), file_dest)

# os.system("source /afs/cern.ch/sw/lcg/app/releases/ROOT/5.34.24/x86_64-slc6-gcc47-opt/root/bin/thisroot.sh")

if(runWanalysis or runZanalysis or run_BuildEvByEvTemplates or runPhiStarEta):
    
    if(useLHAPDF and os.environ.get('LHAPATH') == lhapdf_folder+"share/lhapdf/PDFsets"):
        print "ENVIRONMENT VARIABLES OK"
    else:
        print "REMEMBER TO SET ENVIRONMENT VARIABLES (MUST RUN ON LXPLUS):"
        # print "/afs/cern.ch/project/eos/installation/0.2.30/bin/eos.select -b fuse mount ~/eos"
        # print "source /afs/cern.ch/sw/lcg/external/gcc/4.3.2/x86_64-slc5/setup.sh"
        # print "source /afs/cern.ch/sw/lcg/app/releases/ROOT/5.34.05/x86_64-slc5-gcc43-opt/root/bin/thisroot.sh"
        if(useLHAPDF):
          print ("export PATH="+lhapdf_folder+"bin/:$PATH")
          print ("export LD_LIBRARY_PATH="+lhapdf_folder+"lib/:$LD_LIBRARY_PATH")
          print ("export LHAPATH="+lhapdf_folder+"share/lhapdf/PDFsets")
          sys.exit()
  
    counter=0
    for i in range(0, nsamples):
        
        if (resumbit_sample!=""):
            if not sample[i] in resumbit_sample: 
                print "skipping ",sample[i]," which is not",resumbit_sample;
                continue;
          
        counter=counter+1
        
        if(IS_MC_CLOSURE_TEST and (sample[i]!="WJetsMadSig" and sample[i]!="DYJetsPow" and sample[i]!="DYJetsMadSig")): continue; # TEMPORARY
        jobID= "test_numbers_"+sample[i];
        
        print ''    
        print "ANALYZING jobID= ", jobID ;
        
        WfileDATA= fWana_str[i];
        ZfileDATA= fZana_str[i];
        if( ("WJetsMadSig" in sample[i] or "WJetsPow" in sample[i]) and useAlsoGenPforSig): WfileDATA.replace("_SignalRecoSkimmed","");
        else:
            if( ("DYJetsPow" in sample[i]  or "DYJetsMadSig" in sample[i]) and useAlsoGenPforSig): ZfileDATA.replace("_SignalRecoSkimmed","");

        tot_N_evts = Nevts[i];

        if(CS_pb[i] >0): int_lumi_fb[i] = Nevts[i]/CS_pb[i]/1e3;
        
        # if IS_MC_CLOSURE_TEST:
            # if indip_normalization_lumi_MC:
                # WfileDATA_lumi_SF = intLumi_MC_fb/int_lumi_fb[i]
            # else: 
                # WfileDATA_lumi_SF = 1
        # else:
            # WfileDATA_lumi_SF = int_lumi_fb[DATA]/int_lumi_fb[i]
        # if IS_MC_CLOSURE_TEST:

        if indip_normalization_lumi_MC:
            WfileDATA_lumi_SF = intLumi_MC_fb/int_lumi_fb[i]
        else:
            WfileDATA_lumi_SF = int_lumi_fb[DATA]/int_lumi_fb[i]
        
        ZfileDATA_lumi_SF = WfileDATA_lumi_SF
        
        # WfileDATA_lumi_SF = ((intLumi_MC_fb/int_lumi_fb[i]) if indip_normalization_lumi_MC==1 else 1) if IS_MC_CLOSURE_TEST==1 else int_lumi_fb[DATA]/int_lumi_fb[i];
        # ZfileDATA_lumi_SF = ((intLumi_MC_fb/int_lumi_fb[i]) if indip_normalization_lumi_MC==1 else 1) if IS_MC_CLOSURE_TEST==1 else int_lumi_fb[DATA]/int_lumi_fb[i];
        print "lumi_SF= ",ZfileDATA_lumi_SF

        #########################################/
        ## END OF STEERING PARAMETERS
        #########################################/
        
        ## RUNNING CODE

        if(jobID==""): outputdir="dummytest";
        else: outputdir=jobID;
        filename_outputdir = "JobOutputs/"+foldername+'/'+outputdir+'/';
        
        # print working directory
        print "starting nsamples loop ", os.getcwd()

        print "checking directory "+filename_outputdir
        ## check if the outputfolder is already existing
        # make the outputfolder even if is already existing (nothing happens)
        dir_check = 0
        if not os.path.exists(filename_outputdir):
            print "doesn't exists, making directory ",filename_outputdir
            os.makedirs(filename_outputdir)
            dir_check = 1
        
        NPDF_sets = LHAPDF_reweighting_sets.count(',')+1
        if(LHAPDF_reweighting_sets!=""):
          PAR_PDF_SETS = LHAPDF_reweighting_sets
          PAR_PDF_MEMBERS = LHAPDF_reweighting_members
        else:
          PAR_PDF_SETS = "-1"
          PAR_PDF_MEMBERS = "1"
          
        if( dir_check ==0 ): # if the output folder existed use the same common.h
            print "using JobOutputs/"+foldername+"/"+outputdir+"/common.h"
            shutil.copyfile(("JobOutputs/"+foldername+"/"+outputdir+"/common.h"), "includes/common.h")
        else: # otherwise build it from this cfg
            print "creating JobOutputs/"+foldername+"/"+outputdir+"/common.h from includes/common.h.bkp"
            shutil.copyfile("includes/common.h.bkp", "includes/common.h");
            os.system("sh "+os.getcwd()+"/manipulate_parameters.sh "+ZMassCentral_MeV+" "+WMassCentral_MeV+" "+WMassSkipNSteps+" "+WMassNSteps+" "+etaMuonNSteps+" \""+etaMaxMuons+"\" "+str(NPDF_sets)+" "+str(PAR_PDF_SETS)+" "+str(PAR_PDF_MEMBERS)+" "+str(RecoilCorrNVarAll)+" "+Wmass_values_array+" "+Zmass_values_array+" "+str(dummy_deltaM_MeV_central_Index)+" "+str(usePtSF)+" "+str(MuonCorrToys))
            shutil.copyfile("includes/common.h","JobOutputs/"+foldername+"/"+outputdir+"/common.h");
            # sys.exit()
        os.chdir("AnalysisCode/");


        if parallelize and (runWanalysis or runZanalysis or runPhiStarEta) and counter>1:
            print "waiting 10 sec to 20 sec (if W and Z are launched) before to proceed with the next sample to let the compilation finish"
            if(not useBatch): os.system("sleep 3");
        
        if(runWanalysis):
            
            wstring="\""+WfileDATA+"\","+str(WfileDATA_lumi_SF)+",\""+sample[i]+"\","+str(useAlsoGenPforSig)+","+str(IS_MC_CLOSURE_TEST)+","+str(isMCorDATA[i])+",\""+filename_outputdir+"\","+str(useMomentumCorr)+","+str(GlobalSscaleMuonCorrNsigma)+","+str(useEffSF)+","+str(usePtSF)+","+str(usePileupSF)+","+str(controlplots)+","+str(generated_PDF_set[i])+""+","+str(generated_PDF_member[i])+","+str(contains_LHE_weights[i])+","+str(usePhiMETCorr)+","+str(useRecoilCorr)+","+str(RecoilCorrNonClosure)+","+str(RecoilCorrVarDiagoParSigmas)+","+str(RecoilCorrVarDiagoParU1orU2fromDATAorMC)+","+str(use_PForNoPUorTKmet)+","+str(syst_ewk_Alcaraz)+","+str(gen_mass_value_MeV[i])+","+str(contains_LHE_weights[i])
            if(counter<2):
                if(useLHAPDF):
                    os.system("sed -i 's/.*\#define\ LHAPDF_ON.*/\#define\ LHAPDF_ON/' Wanalysis.C")
                    print("c++ -o runWanalysis.o `root-config --glibs --libs --cflags`  -I "+lhapdf_folder+"/include -L "+lhapdf_folder+"/lib -lLHAPDF  -L $ROOFITSYS/lib -lRooFit -lRooStats -lRooFit -lRooFitCore -lFoam -lMathMore -I$ROOFITSYS/include   -lm Wanalysis.C rochcor_44X_v3.C common_stuff.C RecoilCorrector.cc KalmanCalibrator.cc PdfDiagonalizer.cc runWanalysis.C")
                    os.system("rm runWanalysis.o; c++ -o runWanalysis.o `root-config --glibs --libs --cflags`  -I "+lhapdf_folder+"/include -L "+lhapdf_folder+"/lib -lLHAPDF  -L $ROOFITSYS/lib -lRooFit -lRooStats -lRooFit -lRooFitCore -lFoam -lMathMore -I$ROOFITSYS/include   -lm Wanalysis.C rochcor_44X_v3.C common_stuff.C RecoilCorrector.cc KalmanCalibrator.cc PdfDiagonalizer.cc runWanalysis.C")
                else:
                    os.system("sed -i 's/.*\#define\ LHAPDF_ON.*/\/\/\#define\ LHAPDF_ON/' Wanalysis.C")
                    print("c++ -o runWanalysis.o `root-config --glibs --libs --cflags`   -L $ROOFITSYS/lib -lRooFit -lRooStats -lRooFit -lRooFitCore -lFoam -lMathMore -I$ROOFITSYS/include -lm Wanalysis.C rochcor_44X_v3.C common_stuff.C RecoilCorrector.cc KalmanCalibrator.cc PdfDiagonalizer.cc runWanalysis.C")
                    os.system("rm runWanalysis.o; c++ -o runWanalysis.o `root-config --glibs --libs --cflags`   -L $ROOFITSYS/lib -lRooFit -lRooStats -lRooFit -lRooFitCore -lFoam -lMathMore -I$ROOFITSYS/include  -lm Wanalysis.C common_stuff.C rochcor_44X_v3.C RecoilCorrector.cc KalmanCalibrator.cc PdfDiagonalizer.cc runWanalysis.C")
            
            print " "
            line = os.popen("./runWanalysis.o -1,0,0,"+wstring).read()
            nEntries = [int(s) for s in line.split() if s.isdigit()][0]
            # print wstring
            if not parallelize:
                os.system("./runWanalysis.o 0,0,"+str(nEntries)+","+wstring)
            else:
                nevents = 2e5
                # if (("DYJetsMadSig" in sample[i]  or "DYJetsPow" in sample[i]) and float(LHAPDF_reweighting_members)>1):
                # if ("WJetsMadSig" in sample[i]  or "WJetsPow" in sample[i]):
                  # nevents = 3e4
                if ("DATA" in sample[i]):
                  nevents = 5e5  
                # if (WMassNSteps=="0"):
                  # nevents = 1e6  
                  
                nChuncks =  int(nEntries/nevents)+2
                start_dir = os.getcwd()
                os.chdir(os.getcwd()+"/../"+filename_outputdir)
                text_file = open("Wanalysis_nChuncks.log", "w")
                text_file.write(str(nChuncks-1))
                text_file.close()
                os.chdir(start_dir)
               
                if(nChuncks>2 or useBatch): print "nChuncks ",nChuncks-1
                if useBatch or (nChuncks>2  and (("WJetsMadSig" in sample[i]  or "WJetsPow" in sample[i]) or ("DATA" in sample[i]) or (("TTJets" in sample[i]) and WMassNSteps=="0"))):
                  for x in xrange(1, nChuncks):
                    ev_ini=int(nevents*(x-1))
                    ev_fin= nEntries 
                    if (x<nChuncks-1):
                      ev_fin= int(nevents*(x)-1)
                    print x,ev_ini,ev_fin
                    if(not useBatch):
                      os.system("./runWanalysis.o "+str(x)+","+str(ev_ini)+","+str(ev_fin)+","+wstring+" > ../"+filename_outputdir+"Wlog_"+str(x)+".log 2>&1 &")
                    else:
                      start_dir = os.getcwd()
                      os.chdir(os.getcwd()+"/../"+filename_outputdir)
                      if not resubmit:
                        text_file = open("runWanalysis_"+sample[i]+"_"+str(x)+".sh", "w")
                        text_file.write("cd "+os.getcwd()+"\n")
                        text_file.write("eval `scramv1 runtime -sh`\n")
                        # text_file.write("source /afs/cern.ch/sw/lcg/contrib/gcc/4.6/x86_64-slc6-gcc46-opt/setup.sh \n")
                        text_file.write("source /afs/cern.ch/sw/lcg/app/releases/ROOT/5.34.24/x86_64-slc6-gcc47-opt/root/bin/thisroot.sh \n")
                        text_file.write("cd "+start_dir+"\n")
                        text_file.write("./runWanalysis.o "+str(x)+","+str(ev_ini)+","+str(ev_fin)+","+wstring)
                        text_file.close()
                        # print 'file created, launching bsub'
                        os.system("chmod 755 runWanalysis_"+sample[i]+"_"+str(x)+".sh")
                      if not resubmit or not os.path.isfile("Wanalysis_chunk"+str(x)+".root"):
                        os.system("rm core.*")
                        print ("bsub -C 0 -q "+batchQueue+" -J runWanalysis runWanalysis_"+sample[i]+"_"+str(x)+".sh")
                        os.system("bsub -C 0 -u pippo123 -o ./ -q "+batchQueue+" -J runWanalysis runWanalysis_"+sample[i]+"_"+str(x)+".sh")
                      os.chdir(start_dir)
                      
                    if(WMassNSteps=="0" and not useBatch): os.system("sleep 1");
                    elif(not useBatch): os.system("sleep 3");
                else:
                    os.system("./runWanalysis.o 0,0,"+str(nEntries)+","+wstring+" > ../"+filename_outputdir+"Wlog.log 2>&1 &")
                
                if(not useBatch): os.system("sleep 3");
                else: os.system("usleep 100000");

        if(runZanalysis):

            zstring="\""+ZfileDATA+"\","+str(ZfileDATA_lumi_SF)+",\""+sample[i]+"\","+str(useAlsoGenPforSig)+","+str(IS_MC_CLOSURE_TEST)+","+str(isMCorDATA[i])+",\""+filename_outputdir+"\","+str(useMomentumCorr)+","+str(GlobalSscaleMuonCorrNsigma)+","+str(useEffSF)+","+str(usePtSF)+","+str(usePileupSF)+","+str(0)+","+str(controlplots)+","+str(generated_PDF_set[i])+""+","+str(generated_PDF_member[i])+","+str(contains_LHE_weights[i])+","+str(usePhiMETCorr)+","+str(useRecoilCorr)+","+str(RecoilCorrNonClosure)+","+str(RecoilCorrVarDiagoParSigmas)+","+str(RecoilCorrVarDiagoParU1orU2fromDATAorMC)+","+str(use_PForNoPUorTKmet)+","+str(syst_ewk_Alcaraz)+","+str(gen_mass_value_MeV[i])+","+str(contains_LHE_weights[i])
            
            if(counter<2 and not resubmit):
                if(useLHAPDF):
                    os.system("sed -i 's/.*\#define\ LHAPDF_ON.*/\#define\ LHAPDF_ON/' Zanalysis.C")
                    print("c++ -o runZanalysis.o `root-config --glibs --libs --cflags`  -I "+lhapdf_folder+"/include -L "+lhapdf_folder+"/lib -lLHAPDF  -L $ROOFITSYS/lib -lRooFit -lRooStats -lRooFit -lRooFitCore -lFoam -lMathMore -I$ROOFITSYS/include   -lm Zanalysis.C rochcor_44X_v3.C common_stuff.C ../includes/common.h RecoilCorrector.cc KalmanCalibrator.cc PdfDiagonalizer.cc runZanalysis.C")
                    os.system("rm runZanalysis.o; c++ -o runZanalysis.o `root-config --glibs --libs --cflags`  -I "+lhapdf_folder+"/include -L "+lhapdf_folder+"/lib -lLHAPDF  -L $ROOFITSYS/lib -lRooFit -lRooStats -lRooFit -lRooFitCore -lFoam -lMathMore -I$ROOFITSYS/include   -lm Zanalysis.C rochcor_44X_v3.C common_stuff.C ../includes/common.h RecoilCorrector.cc KalmanCalibrator.cc PdfDiagonalizer.cc runZanalysis.C")                    
                else:
                    os.system("sed -i 's/.*\#define\ LHAPDF_ON.*/\/\/\#define\ LHAPDF_ON/' Zanalysis.C")
                    print("c++ -o runZanalysis.o `root-config --glibs --libs --cflags`   -L $ROOFITSYS/lib -lRooFit -lRooStats -lRooFit -lRooFitCore -lFoam -lMathMore -I$ROOFITSYS/include  -lm Zanalysis.C rochcor_44X_v3.C common_stuff.C ../includes/common.h RecoilCorrector.cc KalmanCalibrator.cc PdfDiagonalizer.cc runZanalysis.C")
                    os.system("rm runZanalysis.o; c++ -o runZanalysis.o `root-config --glibs --libs --cflags`   -L $ROOFITSYS/lib -lRooFit -lRooStats -lRooFit -lRooFitCore -lFoam -lMathMore -I$ROOFITSYS/include  -lm Zanalysis.C rochcor_44X_v3.C common_stuff.C ../includes/common.h RecoilCorrector.cc KalmanCalibrator.cc PdfDiagonalizer.cc runZanalysis.C")
                os.system("cp runZanalysis.o ../"+filename_outputdir+"../")
                os.system("chmod 755 ../"+filename_outputdir+"../runZanalysis.o")
                
            print " "
            line = os.popen("./runZanalysis.o -1,0,0,"+zstring).read();
            nEntries = [int(s) for s in line.split() if s.isdigit()][0]
            if not parallelize:
                os.system("./runZanalysis.o 0,0,"+str(nEntries)+","+zstring)
            else:
                nevents = 1e5
                if ("DYJetsMadSig" in sample[i]  or "DYJetsPow" in sample[i]):
                  nevents = 2.5e4
                  if useRecoilCorr>0 and int(RecoilCorrVarDiagoParSigmas)>0:
                    nevents = 1e4
                if ("DATA" in sample[i]):
                  nevents = 2e5  
                  if (MuonCorrToys>1):
                    nevents = nevents/5  
                # if (WMassNSteps=="0"):
                  # nevents = 1e6  
                  
                nChuncks =  int(nEntries/nevents)+2
                start_dir = os.getcwd()
                os.chdir(os.getcwd()+"/../"+filename_outputdir)
                text_file = open("Zanalysis_nChuncks.log", "w")
                text_file.write(str(nChuncks-1))
                text_file.close()
                os.chdir(start_dir)                
                
                if(nChuncks>2 or useBatch): print "nChuncks ",nChuncks-1
                if useBatch or (nChuncks>2  and (("DYJetsPow" in sample[i] or "DYJetsMadSig" in sample[i]) or ("DATA" in sample[i]))):
                  for x in xrange(1, nChuncks):
                    ev_ini=int(nevents*(x-1))
                    ev_fin= nEntries 
                    if (x<nChuncks-1):
                      ev_fin= int(nevents*(x)-1)
                    print x,ev_ini,ev_fin
                    if(not useBatch):
                      os.system("./runZanalysis.o "+str(x)+","+str(ev_ini)+","+str(ev_fin)+","+zstring+" > ../"+filename_outputdir+"Zlog_"+str(x)+".log 2>&1 &")
                    else:
                      start_dir = os.getcwd()
                      os.chdir(os.getcwd()+"/../"+filename_outputdir)
                      if not resubmit:
                        text_file = open("runZanalysis_"+sample[i]+"_"+str(x)+".sh", "w")
                        text_file.write("cd "+os.getcwd()+"\n")
                        text_file.write("eval `scramv1 runtime -sh`\n")
                        # text_file.write("source /afs/cern.ch/sw/lcg/contrib/gcc/4.6/x86_64-slc6-gcc46-opt/setup.sh \n")
                        text_file.write("source /afs/cern.ch/sw/lcg/app/releases/ROOT/5.34.24/x86_64-slc6-gcc47-opt/root/bin/thisroot.sh \n")
                        text_file.write("cd "+start_dir+"\n")
                        # text_file.write("../"+filename_outputdir+"../runZanalysis.o "+str(x)+","+str(ev_ini)+","+str(ev_fin)+","+zstring)
                        text_file.write("./runZanalysis.o "+str(x)+","+str(ev_ini)+","+str(ev_fin)+","+zstring)
                        text_file.close()
                        # print 'file created, launching bsub'
                        os.system("chmod 755 runZanalysis_"+sample[i]+"_"+str(x)+".sh")
                      # print 'checking file',"Zanalysis_chunk"+str(x)+".root",'path is',os.getcwd(),'check is',os.path.isfile("Zanalysis_chunk"+str(x)+".root")
                      if not resubmit or not os.path.isfile("Zanalysis_chunk"+str(x)+".root"):
                        os.system("rm core.*")
                        print ("bsub -C 0 -q "+batchQueue+" -J runZanalysis runZanalysis_"+sample[i]+"_"+str(x)+".sh")
                        os.system("bsub -C 0 -u pippo123 -o ./ -q "+batchQueue+" -J runZanalysis runZanalysis_"+sample[i]+"_"+str(x)+".sh")
                      os.chdir(start_dir)
                    
                    if(WMassNSteps=="0" and not useBatch): os.system("sleep 1");
                    elif(not useBatch): os.system("sleep 3");
                else:
                    os.system("./runZanalysis.o 0,0,"+str(nEntries)+","+zstring+" > ../"+filename_outputdir+"Zlog.log 2>&1 &")
                    
                if(not useBatch): os.system("sleep 3");
                else: os.system("usleep 100000");

            
        if(runPhiStarEta):

            zstring="\""+ZfileDATA+"\","+str(ZfileDATA_lumi_SF)+",\""+sample[i]+"\","+str(useAlsoGenPforSig)+","+str(IS_MC_CLOSURE_TEST)+","+str(isMCorDATA[i])+",\""+filename_outputdir+"\","+str(useMomentumCorr)+","+str(GlobalSscaleMuonCorrNsigma)+","+str(useEffSF)+","+str(usePtSF)+","+str(usePileupSF)+","+str(0)+","+str(controlplots)+","+str(generated_PDF_set[i])+""+","+str(generated_PDF_member[i])+","+str(contains_LHE_weights[i])+","+str(usePhiMETCorr)+","+str(useRecoilCorr)+","+str(RecoilCorrNonClosure)+","+str(RecoilCorrVarDiagoParSigmas)
            
            if(counter<2):
                if(useLHAPDF):
                    os.system("sed -i 's/.*\#define\ LHAPDF_ON.*/\#define\ LHAPDF_ON/' runPhiStarEtaAnalysis.C")
                    print("c++ -o PhiStarEtaAnalysis.o `root-config --glibs --libs --cflags`  -I "+lhapdf_folder+"/include -L "+lhapdf_folder+"/lib -lLHAPDF  -L $ROOFITSYS/lib -lRooFit -lRooStats -lRooFit -lRooFitCore -lFoam -lMathMore -I$ROOFITSYS/include   -lm runPhiStarEtaAnalysis.C rochcor_44X_v3.C common_stuff.C ../includes/common.h RecoilCorrector.cc KalmanCalibrator.cc PdfDiagonalizer.cc HTransformToHelicityFrame.c PhiStarEtaAnalysis.C")
                    os.system("rm PhiStarEtaAnalysis.o; c++ -o PhiStarEtaAnalysis.o `root-config --glibs --libs --cflags`  -I "+lhapdf_folder+"/include -L "+lhapdf_folder+"/lib -lLHAPDF  -L $ROOFITSYS/lib -lRooFit -lRooStats -lRooFit -lRooFitCore -lFoam -lMathMore -I$ROOFITSYS/include   -lm runPhiStarEtaAnalysis.C rochcor_44X_v3.C common_stuff.C ../includes/common.h RecoilCorrector.cc KalmanCalibrator.cc PdfDiagonalizer.cc HTransformToHelicityFrame.c PhiStarEtaAnalysis.C")                    
                else:
                    os.system("sed -i 's/.*\#define\ LHAPDF_ON.*/\/\/\#define\ LHAPDF_ON/' runPhiStarEtaAnalysis.C")
                    print("c++ -o PhiStarEtaAnalysis.o `root-config --glibs --libs --cflags`   -L $ROOFITSYS/lib -lRooFit -lRooStats -lRooFit -lRooFitCore -lFoam -lMathMore -I$ROOFITSYS/include  -lm runPhiStarEtaAnalysis.C rochcor_44X_v3.C common_stuff.C ../includes/common.h RecoilCorrector.cc KalmanCalibrator.cc PdfDiagonalizer.cc HTransformToHelicityFrame.c PhiStarEtaAnalysis.C")
                    os.system("rm PhiStarEtaAnalysis.o; c++ -o PhiStarEtaAnalysis.o `root-config --glibs --libs --cflags`   -L $ROOFITSYS/lib -lRooFit -lRooStats -lRooFit -lRooFitCore -lFoam -lMathMore -I$ROOFITSYS/include  -lm runPhiStarEtaAnalysis.C rochcor_44X_v3.C common_stuff.C ../includes/common.h RecoilCorrector.cc KalmanCalibrator.cc PdfDiagonalizer.cc HTransformToHelicityFrame.c PhiStarEtaAnalysis.C")

            print zstring
            if not parallelize:
                os.system("./PhiStarEtaAnalysis.o "+zstring)

            else:
                if(runWanalysis): os.system("sleep 3");
                os.system("./PhiStarEtaAnalysis.o "+zstring+" > ../"+filename_outputdir+"Zlog.log 2>&1 &")

        if(run_BuildEvByEvTemplates):
            zTemplstring="\""+ZfileDATA+"\","+str(ZfileDATA_lumi_SF)+",\""+sample[i]+"\","+str(useAlsoGenPforSig)+","+str(IS_MC_CLOSURE_TEST)+","+str(isMCorDATA[i])+",\""+filename_outputdir+"\","+str(useMomentumCorr)+","+str(GlobalSscaleMuonCorrNsigma)+","+str(useEffSF)+","+str(usePtSF)+","+str(usePileupSF)+","+str(run_BuildEvByEvTemplates)+","+str(usePhiMETCorr)+","+str(useRecoilCorr)+","+str(RecoilCorrNonClosure)+","+str(RecoilCorrVarDiagoParSigmas)+","+str(use_PForNoPUorTKmet)+","+str(syst_ewk_Alcaraz)
            if not parallelize:
                os.system("root -l -b -q \'runZanalysis.C("+zTemplstring+")\'");
            else:
                if(runWanalysis): os.system("sleep 3");
                os.system("root -l -b -q \'runZanalysis.C("+zTemplstring+")\' > ../"+filename_outputdir+"/ZEvByEvTemplog.log 2>&1 &");
                
        os.chdir("../");
        
if (ExtractNumbers or run_BuildSimpleTemplates):
    for dir in os.listdir("JobOutputs/"+foldername):
        if os.path.isdir("JobOutputs/"+foldername+"/"+dir) and ("test_numbers_" in dir) :
            dataset_item = dir.replace("test_numbers_","");

            if(ExtractNumbers):
                os.chdir("AnalysisCode/");
                isample = -1
                if (dataset_item in sample): isample = sample.index(dataset_item)
                if isample > -1: tot_N_evts = Nevts[isample];
                else: tot_N_evts =1
                
                print "root -l -b -q \'R_WdivZ.C(\"../JobOutputs/"+foldername+"/"+dir+"\",1,"+str(tot_N_evts)+")\' > ../JobOutputs/"+foldername+"/"+dir+"/numbers.txt";
                os.system("root -l -b -q \'R_WdivZ.C(\"../JobOutputs/"+foldername+"/"+dir+"\",1,"+str(tot_N_evts)+")\' > ../JobOutputs/"+foldername+"/"+dir+"/numbers.txt");
                shutil.copyfile("R_WdivZ.C","../JobOutputs/"+foldername+"/"+dir+"/R_WdivZ.C");
                os.chdir("../");
                
            if(run_BuildSimpleTemplates):
                os.chdir("AnalysisCode/");
                os.system("root -l -b -q \' BuildSimpleTemplates.C( \"../JobOutputs/"+foldername+"/"+dir+"\" ) \' ");
                os.chdir("../");
            
if(mergeSigEWKbkg):
    os.chdir("utils/");
    os.system("sh merge_MC.sh \"../JobOutputs/"+foldername+"/\" "+str(resubmit)+" "+str(batchQueue));
    os.chdir("../");


if(runR_WdivZ):
    os.chdir("AnalysisCode/");
    os.system("eval `scramv1 runtime -sh`")
    os.system("root -l -b -q \'R_WdivZ.C(\"../JobOutputs/"+foldername+"\",0,1,"+str(LHAPDF_reweighting_sets)+")\'");
    os.system("mv *.root ../JobOutputs/"+foldername+"/");
    os.system("cp R_WdivZ.C ../JobOutputs/"+foldername+"/");
    os.chdir("../");

if(runPrepareDataCards):
    os.chdir("AnalysisCode/");
    if not os.path.exists("../JobOutputs/"+foldername+"/DataCards"): os.makedirs("../JobOutputs/"+foldername+"/DataCards")
    print "running .x prepareDatacards.C++(\"../JobOutputs/"+foldername+"\",\"../JobOutputs/"+DataCards_systFromFolder+"\",\"\",1,1,\""+str(fit_W_or_Z)+"\")\'"
    os.system("root -l -b -q \'prepareDatacards.C++(\"../JobOutputs/"+foldername+"\",\"../JobOutputs/"+DataCards_systFromFolder+"\",\"\",1,1,\""+str(fit_W_or_Z)+"\")\'")
    os.chdir("../");

if(runPrepareDataCardsFast):
    if(DataCards_systFromFolder!=""):
      common1 = str(os.popen("ls JobOutputs/"+DataCards_systFromFolder+"/test_numbers_*/common.h |head -n1").read()).replace('\n','')
      shutil.copyfile(common1,"includes/common2.h");
    else:
      common1 = str(os.popen("ls JobOutputs/"+foldername+"/test_numbers_*/common.h |head -n1").read()).replace('\n','')
      shutil.copyfile(common1,"includes/common2.h");
    common2 = str(os.popen("ls JobOutputs/"+foldername+"/test_numbers_*/common.h |head -n1").read()).replace('\n','')
    shutil.copyfile(common2,"includes/common.h");
    os.system("sed -i 's/.*namespace WMass{.*/namespace WMass2{/' includes/common2.h")
    
    os.chdir("AnalysisCode/");
    if not os.path.exists("../JobOutputs/"+foldername+"/DataCards"): os.makedirs("../JobOutputs/"+foldername+"/DataCards")
    print "running .x prepareDatacardsFast.C++(\"../JobOutputs/"+foldername+"\",\"../JobOutputs/"+DataCards_systFromFolder+"\",\""+usePowOrMadForSig+"\",1,1,\""+str(fit_W_or_Z)+"\")\'"
    os.system("root -l -b -q \'prepareDatacardsFast.C++(\"../JobOutputs/"+foldername+"\",\"../JobOutputs/"+DataCards_systFromFolder+"\",\""+usePowOrMadForSig+"\",1,1,\""+str(fit_W_or_Z)+"\")\'")
    os.chdir("../");

if(runDataCardsParametrization):
    os.chdir("AnalysisCode/");
    print "running .x DataCardsParametrization.C(\"../JobOutputs/"+foldername+"\",\"\")"
    os.system("root -l -b -q \'DataCardsParametrization.C(\"../JobOutputs/"+foldername+"\",\"\")\'")
    os.chdir("../");


if(runClosureTestLikeLihoodRatioAnsMergeResults):
    if(DataCards_systFromFolder!=""):
      common1 = str(os.popen("ls JobOutputs/"+DataCards_systFromFolder+"/test_numbers_*/common.h |head -n1").read()).replace('\n','')
      shutil.copyfile(common1,"includes/common2.h");
    else:
      common1 = str(os.popen("ls JobOutputs/"+foldername+"/test_numbers_*/common.h |head -n1").read()).replace('\n','')
      shutil.copyfile(common1,"includes/common2.h");
    common2 = str(os.popen("ls JobOutputs/"+foldername+"/test_numbers_*/common.h |head -n1").read()).replace('\n','')
    shutil.copyfile(common2,"includes/common.h");
    os.system("sed -i 's/.*namespace WMass{.*/namespace WMass2{/' includes/common2.h")

    # os.system("rm "+os.getcwd()+"/ClosureTest_fits.C")
    shutil.copyfile("AnalysisCode/ClosureTest_fits_likelihoodratio.C","JobOutputs/"+foldername+"/DataCards/ClosureTest_fits.C");
    os.chdir("JobOutputs/"+foldername+"/DataCards");
    print os.getcwd()
    os.system("rm "+os.getcwd()+"/ClosureTest_fits_C.*")
    os.system("cd /afs/cern.ch/work/p/perrozzi/private/CMSSW_6_1_1/src; SCRAM_ARCH=slc5_amd64_gcc462;eval `scramv1 runtime -sh`; cd -; source /afs/cern.ch/sw/lcg/contrib/gcc/4.6/x86_64-slc6-gcc46-opt/setup.sh; root -l -b -q \'ClosureTest_fits.C++(1,0,\""+str(fit_W_or_Z)+"\","+str(useBatch)+",\""+os.getcwd()+"\","+RecoilCorrVarDiagoParU1orU2fromDATAorMC+")\'")
    # proc=subprocess.Popen("ls "+os.getcwd()+"/submit_datacard_*", shell=True, stdout=subprocess.PIPE, )
    # a = proc.communicate()[0].rstrip().split('\n')
    # print a
    # os.system("cd /afs/cern.ch/work/p/perrozzi/private/CMSSW_6_1_1/src; SCRAM_ARCH=slc5_amd64_gcc462;eval `scramv1 runtime -sh`; cd -; source /afs/cern.ch/sw/lcg/app/releases/ROOT/5.34.24/x86_64-slc6-gcc47-opt/root/bin/thisroot.sh; root -l -b -q \'ClosureTest_fits.C++(1,0,\""+str(fit_W_or_Z)+"\")\'")
    os.chdir("../../../");

if((runClosureTestLikeLihoodRatioAnsMergeResults and useBatch==0) or mergeResults):
    if(DataCards_systFromFolder!=""):
      common1 = str(os.popen("ls JobOutputs/"+DataCards_systFromFolder+"/test_numbers_*/common.h |head -n1").read()).replace('\n','')
      shutil.copyfile(common1,"includes/common2.h");
    else:
      common1 = str(os.popen("ls JobOutputs/"+foldername+"/test_numbers_*/common.h |head -n1").read()).replace('\n','')
      shutil.copyfile(common1,"includes/common2.h");
    common2 = str(os.popen("ls JobOutputs/"+foldername+"/test_numbers_*/common.h |head -n1").read()).replace('\n','')
    shutil.copyfile(common2,"includes/common.h");
    os.system("sed -i 's/.*namespace WMass{.*/namespace WMass2{/' includes/common2.h")
    
    # print "ciao"
    os.system("cp AnalysisCode/merge_results.C JobOutputs/"+foldername+"/DataCards/merge_results.C");
    os.chdir("JobOutputs/"+foldername+"/DataCards");
    print os.getcwd();
    os.system("rm -rf LSF*; rm output_W*.root");
    os.system("root -l -b -q \'merge_results.C++(1,0,\""+str(fit_W_or_Z)+"\")\'");
    os.chdir("../");


if(run_Z_MCandDATAcomparisons_stack):
    os.chdir("PlottingCode/");  
    if not os.path.exists("../JobOutputs/"+foldername+"/ZcomparisonPlots_MCvsDATA"): os.makedirs("../JobOutputs/"+foldername+"/ZcomparisonPlots_MCvsDATA")
    jobIDMCsig= "../JobOutputs/"+foldername+"/test_numbers_"+sample[DYJetsPow]
    jobIDMCEWK= "../JobOutputs/"+foldername+"/test_numbers_EWK"
    jobIDMCTT= "../JobOutputs/"+foldername+"/test_numbers_"+sample[TTJets]
    jobIDMCQCD= "../JobOutputs/"+foldername+"/test_numbers_"+sample[QCD]
    jobIDDATA= "../JobOutputs/"+foldername+"/test_numbers_"+sample[DATA]
    os.system("root -l -b -q \'PlotZdistributionsMCvsDATA_stack.C(\""+jobIDMCsig+"/\",\""+jobIDMCEWK+"/\",\""+jobIDMCTT+"/\",\""+jobIDMCQCD+"/\",\""+jobIDDATA+"/\")\' ");
    os.system("mv *.png ../JobOutputs/"+foldername+"/ZcomparisonPlots_MCvsDATA");
    os.system("cp PlotZdistributionsMCvsDATA_stack.C ../JobOutputs/"+foldername+"/ZcomparisonPlots_MCvsDATA");

if(run_W_MCandDATAcomparisons_stack):
    os.chdir("PlottingCode/");  
    if not os.path.exists("../JobOutputs/"+foldername+"/WcomparisonPlots_MCvsDATA"): os.makedirs("../JobOutputs/"+foldername+"/WcomparisonPlots_MCvsDATA")
    jobIDMCsig= "../JobOutputs/"+foldername+"/test_numbers_"+sample[WJetsMadSig]
    jobIDMCEWK= "../JobOutputs/"+foldername+"/test_numbers_EWK"
    jobIDMCTT= "../JobOutputs/"+foldername+"/test_numbers_"+sample[TTJets]
    jobIDMCQCD= "../JobOutputs/"+foldername+"/test_numbers_"+sample[QCD]
    jobIDDATA= "../JobOutputs/"+foldername+"/test_numbers_"+sample[DATA]
    os.system("root -l -b -q \'PlotWdistributionsMCvsDATA_stack.C(\""+jobIDMCsig+"/\",\""+jobIDMCEWK+"/\",\""+jobIDMCTT+"/\",\""+jobIDMCQCD+"/\",\""+jobIDDATA+"/\")\' ");
    os.system("mv *.png ../JobOutputs/"+foldername+"/WcomparisonPlots_MCvsDATA");
    os.system("cp PlotWdistributionsMCvsDATA_stack.C ../JobOutputs/"+foldername+"/WcomparisonPlots_MCvsDATA");

if(run_PhiStarEta_MCandDATAcomparisons_stack):
    os.chdir("PlottingCode/");  
    if not os.path.exists("../JobOutputs/"+foldername+"/PhiStarEtacomparisonPlots_MCvsDATA"): os.makedirs("../JobOutputs/"+foldername+"/PhiStarEtacomparisonPlots_MCvsDATA")
    jobIDMCsig= "../JobOutputs/"+foldername+"/test_numbers_"+sample[DYJetsPow]
    jobIDMCEWK= "../JobOutputs/"+foldername+"/test_numbers_EWK"
    jobIDMCTT= "../JobOutputs/"+foldername+"/test_numbers_"+sample[TTJets]
    jobIDMCQCD= "../JobOutputs/"+foldername+"/test_numbers_"+sample[QCD]
    jobIDDATA= "../JobOutputs/"+foldername+"/test_numbers_"+sample[DATA]
    os.system("root -l -b -q \'PlotPhiStarEtadistributionsMCvsDATA_stack.C(\""+jobIDMCsig+"/\",\""+jobIDMCEWK+"/\",\""+jobIDMCTT+"/\",\""+jobIDMCQCD+"/\",\""+jobIDDATA+"/\")\' ");
    os.system("mv *.png ../JobOutputs/"+foldername+"/PhiStarEtacomparisonPlots_MCvsDATA");
    os.system("cp PlotPhiStarEtadistributionsMCvsDATA_stack.C ../JobOutputs/"+foldername+"/PhiStarEtacomparisonPlots_MCvsDATA");

if(runWSigBkgFit):
      os.chdir("SignalExtraction/");  
      os.system("source /afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00h/x86_64-slc5-gcc43-opt/root/bin/thisroot.sh; root -l -b -q rootlogon.C fitWm.C+\(\\\""+foldername+"/\\\"\)");
      os.chdir("../");  

if(runZSigBkgFit):
    os.chdir("SignalExtraction/");  
    print ("source /afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00h/x86_64-slc5-gcc43-opt/root/bin/thisroot.sh; root -l -b -q rootlogon.C fitZmm.C+\(\\\""+foldername+"/\\\"\)");
    os.system("source /afs/cern.ch/sw/lcg/app/releases/ROOT/5.28.00h/x86_64-slc5-gcc43-opt/root/bin/thisroot.sh; root -l -b -q rootlogon.C fitZmm.C+\(\\\""+foldername+"/\\\"\)");
    os.chdir("../");  




print ''
