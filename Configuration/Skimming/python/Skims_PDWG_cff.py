import FWCore.ParameterSet.Config as cms

from DPGAnalysis.Skims.Skims_DPG_cff import skimContent


from Configuration.EventContent.EventContent_cff import RECOEventContent
skimRecoContent = RECOEventContent.clone()
skimRecoContent.outputCommands.append("drop *_MEtoEDMConverter_*_*")
skimRecoContent.outputCommands.append("drop *_*_*_SKIM")


#####################


from Configuration.Skimming.ChiB_SD_cff import *
upsilonHLTPath = cms.Path(upsilonHLT)
SKIMStreamChiB = cms.FilteredStream(
    responsible = 'BPH',
    name = 'ChiB',
    paths = (upsilonHLTPath),
    content = skimRecoContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('RECO') 
    )


#####################


from Configuration.Skimming.PDWG_EXODisplacedPhoton_cff import *
EXODisplacedPhotonPath = cms.Path(EXODisplacedPhoton)
SKIMStreamEXODisplacedPhoton = cms.FilteredStream(
    responsible = 'EXO',
    name = 'EXODisplacedPhoton',
    paths = (EXODisplacedPhotonPath),
    content = skimRecoContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('RECO') 
    )

#####################

from Configuration.Skimming.PDWG_TauSkim_cff import *
tauSkimBy1Path = cms.Path( tauSkim1Sequence )
tauSkimBy2Path = cms.Path( tauSkim2Sequence )
mutauSkimPath  = cms.Path( mutauSkimSequence )
mutauMETSkimPath  = cms.Path( mutauMETSkimSequence )
#SKIMStreamTau = cms.FilteredStream(
#    responsible = 'PDWG',
#    name = 'Tau',
#    paths = (tauSkimBy1Path),
#    content = skimContent.outputCommands,
#    selectEvents = cms.untracked.PSet(),
#    dataTier = cms.untracked.string('RAW-RECO')
#    )
SKIMStreamDiTau = cms.FilteredStream(
    responsible = 'Tau POG',
    name = 'DiTau',
    paths = (tauSkimBy2Path),
    content = skimContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('RAW-RECO')
    )
SKIMStreamMuTau = cms.FilteredStream(
    responsible = 'Tau POG',
    name = 'MuTau',
    paths = (mutauSkimPath),
    content = skimContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('RAW-RECO')
    )
SKIMStreamMuTauMET = cms.FilteredStream(
    responsible = 'Tau POG',
    name = 'MuTauMET',
    paths = (mutauMETSkimPath),
    content = skimContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('RAW-RECO')
    )



from Configuration.EventContent.EventContent_cff import AODEventContent
skimAodContent = AODEventContent.clone()
skimAodContent.outputCommands.append("drop *_MEtoEDMConverter_*_*")
skimAodContent.outputCommands.append("drop *_*_*_SKIM")

#####################

from Configuration.Skimming.PDWG_EXOHSCP_cff import *
EXOHSCPPath = cms.Path(exoticaHSCPSeq)
EXOHSCPDEDXPath = cms.Path(exoticaHSCPdEdxSeq)
SKIMStreamEXOHSCP = cms.FilteredStream(
    responsible = 'EXO',
    name = 'EXOHSCP',
    paths = (EXOHSCPPath,EXOHSCPDEDXPath),
    content = EXOHSCPSkim_EventContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('USER')
    )


#####################


from Configuration.Skimming.PDWG_TOPElePlusJets_cff import *
TOPElePlusJetsPath = cms.Path(TOPElePlusJets)
SKIMStreamTOPElePlusJets = cms.FilteredStream(
    responsible = 'TOP',
    name = 'TOPElePlusJets',
    paths = (TOPElePlusJetsPath),              
    content = skimAodContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('AOD')
    )

#####################


from Configuration.Skimming.PDWG_TOPMuPlusJets_cff import *
TOPMuPlusJetsPath = cms.Path(TOPMuPlusJets)
SKIMStreamTOPMuPlusJets = cms.FilteredStream(
    responsible = 'TOP',
    name = 'TOPMuPlusJets',
    paths = (TOPMuPlusJetsPath),              
    content = skimAodContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('AOD')
    )

#####################


from Configuration.Skimming.PDWG_HZZSkim_cff import *
SKIMStreamHZZ = cms.FilteredStream(
        responsible = 'PDWG',
        name = 'HZZ',
        paths = HZZPaths,
        content = skimAodContent.outputCommands,
        selectEvents = cms.untracked.PSet(),
        dataTier = cms.untracked.string('AOD')
        )

#####################

# file name "PDWG_HLTZEROBIASSIG_SD" inherited from 2011 - it's actually a filter on HLT_Physics bit
from Configuration.Skimming.PDWG_HLTZEROBIASSIG_SD_cff import *
HLTZEROBIASSIGSDPath = cms.Path(HLTZEROBIASSIGSD)
SKIMStreamHLTPhysics = cms.FilteredStream(
    responsible = 'TSG',
    name = 'HLTPhysics',
    paths = (HLTZEROBIASSIGSDPath),
    content = skimContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('RAW-RECO') 
    )

#####################

from Configuration.Skimming.PDWG_MonoPhoton_cff import *
EXOMonoPhotonPath = cms.Path(monophotonSkimSequence)
SKIMStreamEXOMonoPhoton = cms.FilteredStream(
    responsible = 'EXO',
    name = 'EXOMonoPhoton',
    paths = (EXOMonoPhotonPath),
    content = skimContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('RAW-RECO') 
    )


#####################
# Jan 15th 2013 - The skims defined below should be used only for
# pPb run (2013).
# This pPb run uses the standard pp scenario, and for this reason the
# skims where included in this area 
#####################


## for the Dilepton group #########################

## PsiMuMu

from Configuration.Skimming.pA_DiLeptonSkim_cff import *
psiPath = cms.Path( psiCandidateSequence )
SKIMStreamPsiMuMuPA = cms.FilteredStream(
                    responsible = 'HIN PAG',
                    name = 'PsiMuMuPA',
                    paths = (psiPath),
                    content = skimRecoContent.outputCommands,
                    selectEvents = cms.untracked.PSet(),
                    dataTier = cms.untracked.string('RECO')
                    )

## UpsMuMu
from Configuration.Skimming.pA_DiLeptonSkim_cff import *
upsPath = cms.Path( upsCandidateSequence )
SKIMStreamUpsMuMuPA = cms.FilteredStream(
                    responsible = 'HIN PAG',
                    name = 'UpsMuMuPA',
                    paths = (upsPath),
                    content = skimRecoContent.outputCommands,
                    selectEvents = cms.untracked.PSet(),
                    dataTier = cms.untracked.string('RECO')
                    )

## ZMuMu
from Configuration.Skimming.pA_DiLeptonSkim_cff import *
ZPath = cms.Path( ZCandidateSequence )
SKIMStreamZMuMuPA = cms.FilteredStream(
                    responsible = 'HIN PAG',
                    name = 'ZMuMuPA',
                    paths = (ZPath),
                    content = skimRecoContent.outputCommands,
                    selectEvents = cms.untracked.PSet(),
                    dataTier = cms.untracked.string('RECO')
                    )

## for the Flow/correlation  group #########################

from Configuration.Skimming.pA_FlowCorrSkim_cff import *
FlowCorrPath = cms.Path( flowCorrCandidateSequence )
SKIMStreamFlowCorrPA = cms.FilteredStream(
                                       responsible = 'HIN PAG',
                                       name = 'FlowCorrPA',
                                       paths = (FlowCorrPath),
                                       content = skimRecoContent.outputCommands,
                                       selectEvents = cms.untracked.PSet(),
                                       dataTier = cms.untracked.string('RECO')
                                       )

## for the High Pt group #########################

from Configuration.Skimming.pA_HighPtSkim_cff import *
HighPtPath = cms.Path( HighPtCandidateSequence )
SKIMStreamHighPtPA = cms.FilteredStream(
                                        responsible = 'HIN PAG',
                                        name = 'HighPtPA',
                                        paths = (HighPtPath),
                                        content = skimRecoContent.outputCommands,
                                        selectEvents = cms.untracked.PSet(),
                                        dataTier = cms.untracked.string('RECO')
                                        )


"""
#####################
# For the Data on Data Mixing in TSG
from HLTrigger.Configuration.HLT_FULL_cff import hltGtDigis
hltGtDigisPath=cms.Path(hltGtDigis)

# The events to be used as PileUp
from Configuration.Skimming.PDWG_HLTZEROBIASPU_SD_cff import *
HLTZEROBIASPUSDPath = cms.Path(HLTZEROBIASPUSD)
SKIMStreamHLTZEROBIASPUSD = cms.FilteredStream(
    responsible = 'PDWG',
    name = 'HLTZEROBIASPUSD',
    paths = (HLTZEROBIASPUSDPath),
    content = skimRecoContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('RAW') # for the moment, it could be DIGI in the future
    )

####################
"""   

#####################

#from Configuration.Skimming.PDWG_HSCP_SD_cff import *
#HSCPSDPath = cms.Path(HSCPSD)
#SKIMStreamHSCPSD = cms.FilteredStream(
#    responsible = 'PDWG',
#    name = 'HSCPSD',
#    paths = (HSCPSDPath),
#    content = skimRecoContent.outputCommands,
#    selectEvents = cms.untracked.PSet(),
#    dataTier = cms.untracked.string('RECO')
#    )

#####################

#from Configuration.Skimming.PDWG_DiJetAODSkim_cff import *
#diJetAveSkimPath = cms.Path(DiJetAveSkim_Trigger)
#SKIMStreamDiJet = cms.FilteredStream(
#    responsible = 'PDWG',
#    name = 'DiJet',
#    paths = (diJetAveSkimPath),
#    content = DiJetAveSkim_EventContent.outputCommands,
#    selectEvents = cms.untracked.PSet(),
#    dataTier = cms.untracked.string('USER')
#    )

#####################

#from Configuration.Skimming.PDWG_DiPhoton_SD_cff import *
#CaloIdIsoPhotonPairsPath = cms.Path(CaloIdIsoPhotonPairsFilter)
#R9IdPhotonPairsPath = cms.Path(R9IdPhotonPairsFilter)
#MixedCaloR9IdPhotonPairsPath = cms.Path(MixedCaloR9IdPhotonPairsFilter)
#MixedR9CaloIdPhotonPairsPath = cms.Path(MixedR9CaloIdPhotonPairsFilter)
#
#SKIMStreamDiPhoton = cms.FilteredStream(
#    responsible = 'PDWG',
#    name = 'DiPhoton',
#    paths = (CaloIdIsoPhotonPairsPath,R9IdPhotonPairsPath,MixedCaloR9IdPhotonPairsPath,MixedR9CaloIdPhotonPairsPath),
#    content = skimContent.outputCommands,
#    selectEvents = cms.untracked.PSet(),
#    dataTier = cms.untracked.string('RAW-RECO')
#    )

#####################

#from Configuration.Skimming.PDWG_HWWSkim_cff import *
#HWWmmPath = cms.Path(diMuonSequence)
#HWWeePath = cms.Path(diElectronSequence)
#HWWemPath = cms.Path(EleMuSequence)
#SKIMStreamHWW = cms.FilteredStream(
#        responsible = 'PDWG',
#        name = 'HWW',
#        paths = (HWWmmPath,HWWeePath,HWWemPath),
#        content = skimAodContent.outputCommands,
#        selectEvents = cms.untracked.PSet(),
#        dataTier = cms.untracked.string('AOD')
#        )

#####################

#from Configuration.Skimming.PDWG_EXOHPTE_cff import *
#exoHPTEPath = cms.Path(exoDiHPTESequence)
#SKIMStreamEXOHPTE = cms.FilteredStream(
#    responsible = 'PDWG',
#    name = 'EXOHPTE',
#    paths = (exoHPTEPath),
#    content = skimAodContent.outputCommands,
#    selectEvents = cms.untracked.PSet(),
#    dataTier = cms.untracked.string('AOD')
#    )

#####################

#from Configuration.Skimming.PDWG_DoublePhotonSkim_cff import *
#diphotonSkimPath = cms.Path(diphotonSkimSequence)
#SKIMStreamDoublePhoton = cms.FilteredStream(
#    responsible = 'PDWG',
#    name = 'DoublePhoton',
#    paths = (diphotonSkimPath),
#    content = skimAodContent.outputCommands,
#    selectEvents = cms.untracked.PSet(),
#    dataTier = cms.untracked.string('AOD')
#    )


"""
from SUSYBSMAnalysis.Skimming.EXOLLResSkim_cff import *
exoLLResmmPath = cms.Path(exoLLResdiMuonSequence)
exoLLReseePath = cms.Path(exoLLResdiElectronSequence)
exoLLResemPath = cms.Path(exoLLResEleMuSequence)
SKIMStreamEXOLLRes = cms.FilteredStream(
        responsible = 'EXO',
        name = 'EXOLLRes',
        paths = (exoLLResmmPath,exoLLReseePath,exoLLResemPath),
        content = skimAodContent.outputCommands,
        selectEvents = cms.untracked.PSet(),
        dataTier = cms.untracked.string('AOD')
        )

from SUSYBSMAnalysis.Skimming.EXOEle_cff import *
exoElePath = cms.Path(exoEleLowetSeqReco)
SKIMStreamEXOEle = cms.FilteredStream(
    responsible = 'EXO',
    name = 'EXOEle',
    paths = (exoElePath),
    content = skimAodContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('AOD')
    )

from SUSYBSMAnalysis.Skimming.EXOMu_cff import *
exoMuPath = cms.Path(exoMuSequence)
SKIMStreamEXOMu = cms.FilteredStream(
    responsible = 'EXO',
    name = "EXOMu",
    paths = (exoMuPath),
    content = skimAodContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('AOD')
    )

from SUSYBSMAnalysis.Skimming.EXOTriLepton_cff import *
exoTriMuPath = cms.Path(exoTriMuonSequence)
SKIMStreamEXOTriMu = cms.FilteredStream(
    responsible = 'EXO',
    name = 'EXOTriMu',
    paths = (exoTriMuPath),
    content = skimAodContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('AOD')
    )
exoTriElePath = cms.Path(exoTriElectronSequence)
SKIMStreamEXOTriEle = cms.FilteredStream(
    responsible = 'EXO',
    name = 'EXOTriEle',
    paths = (exoTriElePath),
    content = skimAodContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('AOD')
    )
exo1E2MuPath = cms.Path(exo1E2MuSequence)
SKIMStreamEXO1E2Mu = cms.FilteredStream(
    responsible = 'EXO',
    name = 'EXO1E2Mu',
    paths = (exo1E2MuPath),
    content = skimAodContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('AOD')
    )

from SUSYBSMAnalysis.Skimming.EXODiLepton_cff import *
exoDiMuPath = cms.Path(exoDiMuSequence)
exoDiElePath = cms.Path(exoDiMuSequence)
exoEMuPath = cms.Path(exoEMuSequence)
SKIMStreamEXODiMu = cms.FilteredStream(
    responsible = 'EXO',
    name = 'EXODiMu',
    paths = (exoDiMuPath),
    content = skimAodContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('AOD')
    )
SKIMStreamEXODiEle = cms.FilteredStream(
    responsible = 'EXO',
    name = 'EXODiEle',
    paths = (exoDiElePath),
    content = skimAodContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('AOD')
    )
SKIMStreamEXOEMu = cms.FilteredStream(
    responsible = 'EXO',
    name = 'EXOEMu',
    paths = (exoEMuPath),
    content = skimAodContent.outputCommands,
    selectEvents = cms.untracked.PSet(),
    dataTier = cms.untracked.string('AOD')
    )
"""
