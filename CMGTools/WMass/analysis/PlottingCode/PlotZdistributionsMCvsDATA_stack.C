#include "../common.h"
#include "../../../AnalysisCode/common_stuff.C"

void PlotZdistributionsMCvsDATA_stack(TString folderMCsig="",TString folderMCEWK="",TString folderMCTT="",TString folderMCQCD="",TString folderDATA=""){

  gStyle->SetOptTitle(0);
  gStyle->SetOptStat(0);
  
  cout << "PlotWZdistributionsDATA.C working dir: " << gSystem->WorkingDirectory() << endl;


  TFile *fMCsig=new TFile(Form("%s/ZanalysisOnDATA.root",folderMCsig.Data()));
  TFile *fMCEWK=new TFile(Form("%s/ZanalysisOnDATA.root",folderMCEWK.Data()));
  TFile *fMCTT=new TFile(Form("%s/ZanalysisOnDATA.root",folderMCTT.Data()));
  TFile *fMCQCD=new TFile(Form("%s/ZanalysisOnDATA.root",folderMCQCD.Data()));
  TFile *fDATA=new TFile(Form("%s/ZanalysisOnDATA.root",folderDATA.Data()));
  
  fMCsig->Print();
  fMCEWK->Print();
  fMCTT->Print();
  fDATA->Print();

  // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"Zmass_zoomed_Sig_eta2p1",0,0,0,1,";Z mass [GeV];Counts",80,100,10);
  // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"Zmass_Sig_eta2p1",0,0,0,1,";Z mass [GeV];Counts",50,-1,1);
  // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"Zmass_QCD_eta2p1",0,1,0,1,";Z mass [GeV];Counts",50,-1,1);
  // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hpfMET_WlikePos_Sig_eta2p1",0,1,0,1,";WlikePos MET [GeV];Counts",25,-1,1);
  // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hpfMET_WlikePos_QCD_eta2p1",0,1,0,1,";WlikePos MET [GeV];Counts",25,-1,1);
  // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hpfMET_WlikePos_QCD_eta2p1",0,1,0,1,";WlikePos MET [GeV];Counts",25,-1,1);
  // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hWlikePos_mt_Sig_eta2p1",0,1,0,1,";WlikePos m_{T} [GeV];Counts",50,-1,1);
  // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hWlikePos_mt_QCD_eta2p1",0,1,0,1,";WlikePos m_{T} [GeV];Counts",50,-1,1);
  // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hWlikePos_mt_Sig_eta2p1",0,1,0,1,";WlikePos m_{T} [GeV];Counts",50,-1,1);
  // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hMupt_WlikePos_Sig_eta2p1",0,1,0,1,";WlikePos muon p_{T} [GeV];Counts",20,-1,1);
  // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hMueta_WlikePos_Sig_eta2p1",0,0,0,1,";WlikePos muon p_{T} [GeV];Counts",20,-1,1);
  // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hnvtx_Sig_eta2p1",0,0,0,1,";number of vertices;Counts",-1,-1,1);
  // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hu1_WlikePos_Sig_eta2p1",0,1,0,1,";u1 (GeV);Counts",-1,-1,1);
  // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hu2_WlikePos_Sig_eta2p1",0,1,0,1,";u2 (GeV);Counts",-1,-1,1);

  TString MuCharge_str[2] = {"Pos" ,"Neg"};
  
  TString LegendEvTypeTeX=Form("WlikePos#rightarrow#mu#nu");
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hnvtx_WlikePos_8_JetCut_Sig_eta0p9_91188"),0,0,0,1,Form(";Number of vertices;Counts"),70,110,1,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("Zmass_WlikePos_8_JetCut_Sig_eta0p9_91188"),0,0,0,1,Form(";Dimuon mass [GeV];Counts"),70,110,1,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("Zmass_zoomed_WlikePos_8_JetCut_Sig_eta0p9_91188"),0,0,0,1,Form(";Dimuon mass [GeV];Counts"),70,110,20,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("Zrap_WlikePos_8_JetCut_Sig_eta0p9_91188"),0,0,0,1,Form(";Dimuon rapidity;Counts"),-1,-1,1,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hWlikePos_Zmass_8_JetCut_pdf229800-0_eta0p9_91188"),0,0,0,1,Form(";Dimuon mass [GeV];Counts"),70,110,1,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("ZDeltaEtaMuNegJet_WlikePos_8_JetCut_Sig_eta0p9_91188"),0,1,0,1,Form(";#eta_{#mu-}-#eta_{leading jet};Counts"),-1,-1,1,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("ZDeltaPhiMuNegJet_WlikePos_8_JetCut_Sig_eta0p9_91188"),0,1,0,1,Form(";#phi_{#mu-}-#phi_{leading jet} [rad];Counts"),-1,-1,1,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("ZDeltaEtaMuPosJet_WlikePos_8_JetCut_Sig_eta0p9_91188"),0,1,0,1,Form(";#eta_{#mu+}-#eta_{leading jet};Counts"),-1,-1,1,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("ZDeltaPhiMuPosJet_WlikePos_8_JetCut_Sig_eta0p9_91188"),0,1,0,1,Form(";#phi_{#mu+}-#phi_{leading jet} [rad];Counts"),-1,-1,1,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("ZlepDeltaEta_WlikePos_8_JetCut_Sig_eta0p9_91188"),0,0,0,1,Form(";#eta_{#mu+}-#eta_{#mu-};Counts"),-1,-1,1,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("ZlepDeltaPhi_WlikePos_8_JetCut_Sig_eta0p9_91188"),0,1,0,1,Form(";#phi_{#mu+}-#phi_{#mu-} [rad];Counts"),-1,-1,1,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("ZlepDeltaPt_WlikePos_8_JetCut_Sig_eta0p9_91188"),0,0,0,1,Form(";pT_{#mu+}-pT_{#mu-} [GeV];Counts"),-1,-1,1,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("ZlepDeltaR_WlikePos_8_JetCut_Sig_eta0p9_91188"),0,1,0,1,Form(";#Delta R(#mu+,#mu-);Counts"),1.6,4.4,2,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hJeteta_WlikePos_8_JetCut_Sig_eta0p9_91188"),0,0,0,1,Form(";Leading jet #eta;Counts"),-1,-1,1,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hMuMETeta_WlikePos_8_JetCut_Sig_eta0p9_91188"),0,0,0,1,Form(";#eta_{#mu-};Counts"),-1,-1,1,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hMueta_WlikePos_8_JetCut_Sig_eta0p9_91188"),0,0,0,1,Form(";#eta_{#mu+};Counts"),-1,-1,1,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hWlikePos_Recoil_8_JetCut_pdf229800-0_eta0p9_91188"),0,0,0,1,Form(";Recoil [GeV];Counts"),-1,-1,1,1);
  common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hWlikePos_ZpT_8_JetCut_pdf229800-0_eta0p9_91188"),0,0,0,1,Form(";Z pT [GeV];Counts"),0,50,1,1);
  
  TString string = "closure"; //"_8_JetCut"
  
  for(int i=1;i<21;i++){ // recoil plots binnined in nvtx
    common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("h_%s_met_VTX%d_tk",string.Data(),i),0,0,0,1,Form(";MET [GeV] for nvtx=%d;Counts",i),0,50,2,1);
    common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("h_%s_metphi_VTX%d_tk",string.Data(),i),0,0,0,1,Form(";MET #phi [rad] for nvtx=%d;Counts",i),-1,-1,4,1);
    common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("h_%s_ptZ_VTX%d_tk",string.Data(),i),0,0,0,1,Form(";Z pT [GeV] for nvtx=%d;Counts",i),-1,-1,2,1);
    common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("h_%s_u_VTX%d_tk",string.Data(),i),0,0,0,1,Form(";Recoil [GeV] for nvtx=%d ;Counts",i),-1,-1,2,1);
    common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("h_%s_u1_VTX%d_tk",string.Data(),i),0,0,0,1,Form(";u1 [GeV] for nvtx=%d;Counts",i),-30,30,2,1);
    common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("h_%s_u2_VTX%d_tk",string.Data(),i),0,0,0,1,Form(";u2 [GeV] for nvtx=%d;Counts",i),-30,30,2,1);
  }
  TString zpt_range_name[13] = {"[0,2]","[10,12]","[12,14]","[14,16]","[16,18]","[18,20]","[20,30]","[2,4]","[4,6]","[6,8]","[8,10]","[30,50]","[50,inf]"};
  TString zpt_range[13] = {"02","1012","1214","1416","1618","1820","2030","24","46","68","810","3050","50"};
  // for(int i=0;i<13;i++){ // commented out after Zpt<30
  for(int i=0;i<11;i++){ // recoil plots binnined in Zpt
    common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("h_%s_met_Zpt%s_tk",string.Data(),zpt_range[i].Data()),0,0,0,1,Form(";MET [GeV] for Z pT=%s;Counts",zpt_range_name[i].Data()),0,50,1,1);
    common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("h_%s_u_Zpt%s_tk",string.Data(),zpt_range[i].Data()),0,0,0,1,Form(";Recoil [rad] for Z pT=%s;Counts",zpt_range_name[i].Data()),-1,-1,1,1);
    common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("h_%s_u1_Zpt%s_tk",string.Data(),zpt_range[i].Data()),0,0,0,1,Form(";u1 [GeV] for Z pT=%s;Counts",zpt_range_name[i].Data()),-30,30,1,1);
    common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("h_%s_u2_Zpt%s_tk",string.Data(),zpt_range[i].Data()),0,0,0,1,Form(";u2 [GeV] for Z pT=%s;Counts",zpt_range_name[i].Data()),-30,30,1,1);
  }
  TString zy_range_name[8] = {"[0.0,0.5]","[-0.5,0.0]","[0.5,1.0]","[1.0,0.5]","[1.0,1.5]","[1.5,1.0]","[1.5,2.0]","[2.0,1.5]"};
  TString zy_range[8] = {"0005","0500","0510","1005","1015","1510","1520","2015"};
  // for(int i=0;i<8;i++){ // commented out after Zpt<30
  for(int i=0;i<6;i++){// recoil plots binnined in Z rapidity
    common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("h_%s_met_Zy%s_tk",string.Data(),zy_range[i].Data()),0,0,0,1,Form(";MET [GeV] for Z rapidity=%s;Counts",zy_range_name[i].Data()),0,50,1,1);
    common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("h_%s_u_Zy%s_tk",string.Data(),zy_range[i].Data()),0,0,0,1,Form(";Recoil [rad] for Z rapidity=%s;Counts",zy_range_name[i].Data()),-1,-1,1,1);
    common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("h_%s_u1_Zy%s_tk",string.Data(),zy_range[i].Data()),0,0,0,1,Form(";u1 [GeV] for Z rapidity=%s;Counts",zy_range_name[i].Data()),-30,30,1,1);
    common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("h_%s_u2_Zy%s_tk",string.Data(),zy_range[i].Data()),0,0,0,1,Form(";u2 [GeV] for Z rapidity=%s;Counts",zy_range_name[i].Data()),-30,30,1,1);
  }
  for(int i=0;i<2;i++){ // polarization plots binnined in Z rapidity
    for(int j=0;j<7;j++){ // polarization plots binnined in Z pT
      // if(j>4) continue; // commented out after Zpt<30
      if(j>2) continue;
      // if(i==1 && j==6) continue;
      common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("costh_CS_rapbin%d_ptbin%d_WlikePos_8_JetCut_pdf229800-0_kalman_eta0p9_91188",i,j),0,0,0,1,Form(";#cos{#theta^{*}_{CS}} for Z rapidity bin %d, Z pT bin %d;Counts",i,j),-1,-1,1,1);
      common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("phi_CS_rapbin%d_ptbin%d_WlikePos_8_JetCut_pdf229800-0_kalman_eta0p9_91188",i,j),0,0,0,1,Form(";#phi^{*}_{CS} [rad] for Z rapidity bin %d, Z pT bin %d;Counts;Counts",i,j),-1,-1,1,1);
    }
  }
  
  // for(int c=0; c<1; c++){
    // TString LegendEvTypeTeX=Form("Wlike%s#rightarrow#mu#nu",MuCharge_str[c].Data());
    
    // for(int i=0; i<WMass::etaMuonNSteps; i++){
      // TString eta_str = Form("%.1f",WMass::etaMaxMuons[i]); eta_str.ReplaceAll(".","p");
      // for(int j=0; j<2*WMass::WMassNSteps+1; j++){
        // int jWmass = WMass::WMassCentral_MeV-(WMass::WMassNSteps-j)*WMass::ZMassCentral_MeV;

        // for(int k=0;k<WMass::NFitVar;k++){
          // common_stuff::plotAndSaveHisto1D_stack(LegendEvTypeTeX,fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hWlike%s_%sNonScaled_8_JetCut_pdf%d-%d%s_eta%s_%d",MuCharge_str[c].Data(),WMass::FitVar_str[k].Data(),WMass::PDF_sets,0,"",eta_str.Data(),jWmass),0,0,0,1,Form(";%s [GeV];Counts",WMass::FitVar_str[k].Data()),-1,-1,1,1);
          
        // }
        // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("Zmass_Sig_eta%s_%d",eta_str.Data(),jWmass),0,0,0,1,";Z mass [GeV];Counts",50,-1,1);
        // // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("Zmass_QCD_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";Z mass [GeV];Counts",50,-1,1);
        // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hpfMET_WlikePos_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";WlikePos MET [GeV];Counts",25,-1,1);
        // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hpfMET_WlikePos_QCD_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";WlikePos MET [GeV];Counts",25,-1,1);
        // // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hpfMET_WlikePos_QCD_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";WlikePos MET [GeV];Counts",25,-1,1);
        // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hWlikePos_mt_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";WlikePos m_{T} [GeV];Counts",50,-1,1);
        // // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hWlikePos_mt_QCD_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";WlikePos m_{T} [GeV];Counts",50,-1,1);
        // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hWlikePos_mt_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";WlikePos m_{T} [GeV];Counts",50,-1,1);
        // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hMupt_WlikePos_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";WlikePos muon p_{T} [GeV];Counts",20,-1,1);
        // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hMueta_WlikePos_Sig_eta%s_%d",eta_str.Data(),jWmass),0,0,0,1,";WlikePos muon p_{T} [GeV];Counts",20,-1,1);
        // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hnvtx_Sig_eta%s_%d",eta_str.Data(),jWmass),0,0,0,1,";number of vertices;Counts",-1,-1,1);
        // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hu1_WlikePos_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";u1 (GeV);Counts",-1,-1,1);
        // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,Form("hu2_WlikePos_Sig_eta%s_%d",eta_str.Data(),jWmass),0,1,0,1,";u2 (GeV);Counts",-1,-1,1);

      // }
      // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"Zmass_Sig_eta0p6",0,0,0,1,";Z mass [GeV];Counts",50,-1,1);
      // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"Zmass_zoomed_Sig_eta0p6",0,0,0,1,";Z mass [GeV];Counts",80,100,10);
      // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hpfMET_WlikePos_Sig_eta0p6",0,1,0,1,";WlikePos MET [GeV];Counts",25,-1,1);
      // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hpfMET_WlikePos_QCD_eta0p6",0,1,0,1,";WlikePos MET [GeV];Counts",25,-1,1);
      // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hWlikePos_mt_Sig_eta0p6",0,1,0,1,";WlikePos m_{T} [GeV];Counts",50,-1,1);
      // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hWlikePos_mt_Sig_eta0p6",0,1,0,1,";WlikePos m_{T} [GeV];Counts",50,-1,1);
      // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hMupt_WlikePos_Sig_eta0p6",0,1,0,1,";WlikePos muon p_{T} [GeV];Counts",20,-1,1);
      // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hMueta_WlikePos_Sig_eta0p6",0,0,0,1,";WlikePos muon p_{T} [GeV];Counts",20,-1,1);
      // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hu1_WlikePos_Sig_eta0p6",0,1,0,1,";u1 (GeV);Counts",-1,-1,1);
      // // common_stuff::plotAndSaveHisto1D_stack(fMCsig,fMCEWK,fMCTT,fMCQCD,fDATA,"hu2_WlikePos_Sig_eta0p6",0,1,0,1,";u2 (GeV);Counts",-1,-1,1);

    // }
  // }
  // return;
  






  
  // common_stuff::plotAndSaveHisto1D(fMC,"Zmass_eta2p1",fDATA,"Zmass_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"ZlepDeltaEta_eta2p1",fDATA,"ZlepDeltaEta_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  
  // TCanvas*cZlepEta1VsEta2_MC=new TCanvas("cZlepEta1VsEta2_MC","cZlepEta1VsEta2_MC");
  // TH2D*ZlepEta1VsEta2_MC=(TH2D*)fMC->Get("ZlepEta1VsEta2_eta2p1");
  // ZlepEta1VsEta2_MC->Draw("colz");
  // cZlepEta1VsEta2_MC->SaveAs("ZlepEta1VsEta2_MC.png");
  
  // TCanvas*cZlepEta1VsEta2_DATA=new TCanvas("cZlepEta1VsEta2_DATA","cZlepEta1VsEta2_DATA");
  // TH2D*ZlepEta1VsEta2_DATA=(TH2D*)fDATA->Get("ZlepEta1VsEta2_eta2p1");
  // ZlepEta1VsEta2_DATA->Draw("colz");
  // cZlepEta1VsEta2_DATA->SaveAs("ZlepEta1VsEta2_DATA.png");
  
  // common_stuff::plotAndSaveHisto1D(fMC,"ZlepDeltaPt_eta2p1",fDATA,"ZlepDeltaPt_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);

  
  // TCanvas*cZlepPt1VsPt2_MC=new TCanvas("cZlepPt1VsPt2_MC","cZlepPt1VsPt2_MC");
  // TH2D*ZlepPt1VsPt2_MC=(TH2D*)fMC->Get("ZlepPt1VsPt2_eta2p1");
  // ZlepPt1VsPt2_MC->GetXaxis()->SetRangeUser(30,80);
  // ZlepPt1VsPt2_MC->GetYaxis()->SetRangeUser(0,80);
  // ZlepPt1VsPt2_MC->DrawNormalized("colz");
  // cZlepPt1VsPt2_MC->SetLogz();
  // cZlepPt1VsPt2_MC->SaveAs("ZlepPt1VsPt2_MC.png");
  
  // TCanvas*cZlepPt1VsPt2_DATA=new TCanvas("cZlepPt1VsPt2_DATA","cZlepPt1VsPt2_DATA");
  // TH2D*ZlepPt1VsPt2_DATA=(TH2D*)fDATA->Get("ZlepPt1VsPt2_eta2p1");
  // ZlepPt1VsPt2_DATA->GetXaxis()->SetRangeUser(30,80);
  // ZlepPt1VsPt2_DATA->GetYaxis()->SetRangeUser(0,80);
  // ZlepPt1VsPt2_DATA->DrawNormalized("colz");
  // cZlepPt1VsPt2_DATA->SetLogz();
  // cZlepPt1VsPt2_DATA->SaveAs("ZlepPt1VsPt2_DATA.png");
  
  // common_stuff::plotAndSaveHisto1D(fMC,"hpfMET_Z_eta2p1",fDATA,"hpfMET_Z_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);

  // common_stuff::plotAndSaveHisto1D(fMC,"hpfMET_WlikePos_eta2p1",fDATA,"hpfMET_WlikePos_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  
  // // TCanvas*chpfMETphi_Z=new TCanvas("chpfMETphi_Z","chpfMETphi_Z");
  // // TH1D*ZhpfMETphi_Z=(TH1D*)fMC->Get("hpfMETphi_Z");
  // // ZhpfMETphi_Z->SetLineColor(2);
  // // TH1D*WPoshpfMETphi_Z=(TH1D*)fDATA->Get("hpfMETphi_WPos");
  // // WPoshpfMETphi_Z->GetYaxis()->SetRangeUser(0,WPoshpfMETphi_Z->GetMaximum()*1.2);
  // // if(WPoshpfMETphi_Z->GetMaximum() > ZhpfMETphi_Z->GetMaximum()){
  // // WPoshpfMETphi_Z->DrawNormalized();
  // // ZhpfMETphi_Z->DrawNormalized("same");
  // // }else{
  // // ZhpfMETphi_Z->DrawNormalized("");
  // // WPoshpfMETphi_Z->DrawNormalized("same");
  // // }
  // // chpfMETphi_Z->SaveAs("hpfMETphi_V.png");

  // common_stuff::plotAndSaveHisto1D(fMC,"hpfMETphi_WlikePos_eta2p1",fDATA,"hpfMETphi_WlikePos_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  
  // common_stuff::plotAndSaveHisto1D(fMC,"hZ_pt_eta2p1",fDATA,"hZ_pt_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hZ_phi_eta2p1",fDATA,"hZ_phi_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hZ_mt_eta2p1",fDATA,"hZ_mt_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hWlikePos_pt_eta2p1",fDATA,"hWlikePos_pt_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hWlikePos_phi_eta2p1",fDATA,"hWlikePos_phi_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hWlikePos_mt_eta2p1",fDATA,"hWlikePos_mt_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hMupt_WlikePos_eta2p1",fDATA,"hMupt_WlikePos_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hMueta_WlikePos_eta2p1",fDATA,"hMueta_WlikePos_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hMuphi_WlikePos_eta2p1",fDATA,"hMuphi_WlikePos_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hMuMETpt_WlikePos_eta2p1",fDATA,"hMuMETpt_WlikePos_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hMuMETeta_WlikePos_eta2p1",fDATA,"hMuMETeta_WlikePos_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hMuMETphi_WlikePos_eta2p1",fDATA,"hMuMETphi_WlikePos_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hJetpt_WPos_eta2p1",fDATA,"hJetpt_WPos_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hJeteta_WPos_eta2p1",fDATA,"hJeteta_WPos_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hJetphi_WPos_eta2p1",fDATA,"hJetphi_WPos_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hu1_WPos_eta2p1",fDATA,"hu1_WPos_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  // common_stuff::plotAndSaveHisto1D(fMC,"hu2_WPos_eta2p1",fDATA,"hu2_WPos_eta2p1", /*logxyz*/ 0,1,0, /*scaleMCtoDATA*/ 1);
  
  // // TH2D *hZ_ptVsmt=new TH2D("hZ_ptVsmt","hZ_ptVsmt",150,50,200,100,0,25);
  // return;

  // // TCanvas*chrecoil1=new TCanvas("chrecoil1","chrecoil1");
  // // TH1D*Zhrecoil1=(TH1D*)fMC->Get("hu1_WPos");
  // // Zhrecoil1->Draw("");
  // // chrecoil1->SaveAs("hZrecoil1.png");

  // // TCanvas*chrecoil2=new TCanvas("chrecoil2","chrecoil2");
  // // TH1D*Zhrecoil2=(TH1D*)fMC->Get("hu2_WPos");
  // // Zhrecoil2->Draw("");
  // // chrecoil2->SaveAs("hZrecoil2.png");
  
}

