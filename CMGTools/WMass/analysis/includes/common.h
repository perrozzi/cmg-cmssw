#include <TFile.h>
#include <TH2.h>
#include <TH1.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <TMath.h>
#include <TString.h>

namespace WMass{

  static const int ZMassCentral_MeV = PAR_ZMASS_CENTRAL;
  static const int WMassCentral_MeV = PAR_WMASS_CENTRAL;
  
  static const int WMassSkipNSteps = PAR_WMASS_STEP;
  static const int WMassNSteps = PAR_WMASS_NSTEPS;
  
  static const int Wmass_values_array[2*WMassNSteps+1] = {PAR_WMASS_VALUES_ARRAY};
  static const int Zmass_values_array[2*WMassNSteps+1] = {PAR_ZMASS_VALUES_ARRAY};
  
  static const int PtSFNSteps = PAR_PTSF_NSTEP;
  static const int PtSFtype[PtSFNSteps] = { PAR_PTSF_STEPS };
  
  static const double etaMaxMuons = PAR_ETA_CUT;
  
  static const int efficiency_toys = PAR_EFF_TOYS; // 0=No, >1=Yes

  static const int nSigOrQCD = 2;
  TString nSigOrQCD_str[nSigOrQCD] = {"Sig","QCD"};

  static const int NFitVar = 3;
  TString FitVar_str[] = {"Pt","Mt","MET","MtLin"};

  static const int PDF_sets = PAR_PDF_SETS;
  static const int PDF_members = PAR_PDF_MEMBERS;
  static const int NVarRecoilCorr = 1; // not used in main chain anymore
  
  static const int WlikeCharge = PAR_WLIKE_CHARGE;
  
  static const int WpTcut = 15;
  
  static const int KalmanNvariations = PAR_KALMAN_VARIATIONS; // 1 or 45
  
  // static const double sel_xmin[3]={30,  60, 30};
  static const double sel_xmin[NFitVar]={30,  60, 30/* ,  60 */};
  static const double sel_xmax[NFitVar]={55, 100, 55/* , 100 */};
  
  static const double fit_xmin[NFitVar]={32,  65, 32/* ,  65 */};
  static const double fit_xmax[NFitVar]={45,  90, 45/* ,  90 */};

  static const int LHE_mass_central_index = PAR_DELTAM_MEV_CENTRAL_INDEX;
  // 209 #w,ren,fac,pdf,mW,mZ 1.0 1.0 1.0 229800 80.398 91.1876               <------------ NNPDF2.3 NLO
  static const int LHE_NNPDF2p3_NLO_central_index = 209; // 100 members
  // 309 #w,ren,fac,pdf,mW,mZ 0.995244555969 1.0 1.0 11000 80.398 91.1876     <------------ CT10 NLO
  static const int LHE_CT10_NLO_central_index = 309;     // 53 members
  // 362 #w,ren,fac,pdf,mW,mZ 1.01129558613 1.0 1.0 232000 80.398 91.1876      <------------ NNPDF2.3 NNLO
  static const int LHE_NNPDF2p3_NNLO_central_index = 362; // 100 members
  
  // static const int RecoilCorrVarDiagoParU1orU2fromDATAorMC_[] = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  1,  1,  1,  1,  1,  1,  1,  1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,  2,  2 };
  // static const int RecoilCorrVarDiagoParN_[]                  = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 };
  
  static const int RecoilCorrIniVarDiagoParU1orU2fromDATAorMC_[] = {0, 0,  9,  0, 0,  9,  0, 0,  9,  0, 0,  9,  0,   0};
  static const int RecoilCorrNVarDiagoParU1orU2fromDATAorMC_[]   = {1, 9, 21, 15, 9, 21, 15, 9, 21, 15, 9, 21, 15, 100};
  
  // static const int RecoilCorrNVarDiagoParU1orU2fromDATAorMC_[] = {1, 18, 12, 18, 12 };
  static const int RecoilCorrVarDiagoParN_[]                  = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 };
  

}
