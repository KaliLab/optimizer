/* Created by Language version: 7.7.0 */
/* VECTORIZED */
#define NRN_VECTORIZED 1
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "scoplib_ansi.h"
#undef PI
#define nil 0
#include "md1redef.h"
#include "section.h"
#include "nrniv_mf.h"
#include "md2redef.h"
 
#if METHOD3
extern int _method3;
#endif

#if !NRNGPU
#undef exp
#define exp hoc_Exp
extern double hoc_Exp(double);
#endif
 
#define nrn_init _nrn_init__D1_LTP_time_window_Luca_cai_initials
#define _nrn_initial _nrn_initial__D1_LTP_time_window_Luca_cai_initials
#define nrn_cur _nrn_cur__D1_LTP_time_window_Luca_cai_initials
#define _nrn_current _nrn_current__D1_LTP_time_window_Luca_cai_initials
#define nrn_jacob _nrn_jacob__D1_LTP_time_window_Luca_cai_initials
#define nrn_state _nrn_state__D1_LTP_time_window_Luca_cai_initials
#define _net_receive _net_receive__D1_LTP_time_window_Luca_cai_initials 
#define assign_calculated_values assign_calculated_values__D1_LTP_time_window_Luca_cai_initials 
#define observables_func observables_func__D1_LTP_time_window_Luca_cai_initials 
#define ode ode__D1_LTP_time_window_Luca_cai_initials 
 
#define _threadargscomma_ _p, _ppvar, _thread, _nt,
#define _threadargsprotocomma_ double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt,
#define _threadargs_ _p, _ppvar, _thread, _nt
#define _threadargsproto_ double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 /* Thread safe. No static _p or _ppvar. */
 
#define t _nt->_t
#define dt _nt->_dt
#define DA_start _p[0]
#define DA_max _p[1]
#define ATP_expression _p[2]
#define Ca_expression _p[3]
#define DA_expression _p[4]
#define AMP _p[5]
#define ATP _p[6]
#define Ca _p[7]
#define DA _p[8]
#define pSubstrate_out _p[9]
#define PP1_out _p[10]
#define CaM_out _p[11]
#define D32_out _p[12]
#define total_CaMKII_activated_out _p[13]
#define AC5 _p[14]
#define AC5_ATP _p[15]
#define AC5_Ca _p[16]
#define AC5_Ca_ATP _p[17]
#define AC5_Ca_GaolfGTP _p[18]
#define AC5_Ca_GaolfGTP_ATP _p[19]
#define AC5_GaolfGTP _p[20]
#define AC5_GaolfGTP_ATP _p[21]
#define B56PP2A _p[22]
#define B56PP2A_D32p75 _p[23]
#define B56PP2A_pARPP21 _p[24]
#define B56PP2Ap _p[25]
#define B56PP2Ap_D32p75 _p[26]
#define B56PP2Ap_pARPP21 _p[27]
#define B72PP2A _p[28]
#define B72PP2A_D32p34 _p[29]
#define B72PP2A_D32p75 _p[30]
#define B72PP2A_pARPP21 _p[31]
#define B72PP2A_Ca_D32p34 _p[32]
#define B72PP2A_Ca_D32p75 _p[33]
#define B72PP2A_Ca _p[34]
#define B72PP2A_Ca_pARPP21 _p[35]
#define CaM _p[36]
#define CaM_Ca2 _p[37]
#define CaM_Ca4 _p[38]
#define CaM_Ca4_pARPP21 _p[39]
#define CaMKII _p[40]
#define CaMKII_CaM_Ca4 _p[41]
#define CaMKII_CaM _p[42]
#define CaMKII_CaM_Ca2 _p[43]
#define CaMKII_CaM_Ca2_psd _p[44]
#define CaMKII_CaM_psd _p[45]
#define CaMKII_CaM_Ca4_psd _p[46]
#define CaMKII_psd _p[47]
#define cAMP _p[48]
#define Substrate _p[49]
#define CDK5 _p[50]
#define CDK5_D32 _p[51]
#define D1R _p[52]
#define D1R_DA _p[53]
#define D1R_Golf_DA _p[54]
#define D1R_Golf _p[55]
#define D32p34 _p[56]
#define D32p75 _p[57]
#define D32 _p[58]
#define GaolfGDP _p[59]
#define GaolfGTP _p[60]
#define Gbgolf _p[61]
#define Golf _p[62]
#define pCaMKII _p[63]
#define pCaMKII_CaM_Ca4 _p[64]
#define pCaMKII_CaM _p[65]
#define pCaMKII_CaM_Ca2 _p[66]
#define pCaMKII_CaM_Ca2_psd _p[67]
#define pCaMKII_CaM_psd _p[68]
#define pCaMKII_CaM_Ca4_psd _p[69]
#define pCaMKII_psd _p[70]
#define pSubstrate _p[71]
#define PDE4 _p[72]
#define PDE4_cAMP _p[73]
#define PDE10r _p[74]
#define PDE10r_cAMP _p[75]
#define PDE10c _p[76]
#define PDE10c_cAMP _p[77]
#define PKA _p[78]
#define PKAc _p[79]
#define PKAc_B56PP2A _p[80]
#define PKAc_D32 _p[81]
#define PKAc_ARPP21 _p[82]
#define PKA_Ca2MP _p[83]
#define PKA_Ca4MP _p[84]
#define PKAc_D32p75 _p[85]
#define PKAreg _p[86]
#define PP1 _p[87]
#define PP1_pCaMKII_psd _p[88]
#define PP1_pSubstrate _p[89]
#define PP1_D32p34 _p[90]
#define CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd _p[91]
#define pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd _p[92]
#define CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 _p[93]
#define pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 _p[94]
#define PP2B _p[95]
#define PP2Bc _p[96]
#define PP2Bc_D32p34 _p[97]
#define PP2B_CaM _p[98]
#define PP2B_CaM_Ca2 _p[99]
#define pARPP21 _p[100]
#define ARPP21 _p[101]
#define pCaMKII_psd_Substrate _p[102]
#define pCaMKII_CaM_psd_Substrate _p[103]
#define pCaMKII_CaM_Ca2_psd_Substrate _p[104]
#define pCaMKII_CaM_Ca4_psd_Substrate _p[105]
#define CaMKII_CaM_psd_Substrate _p[106]
#define CaMKII_CaM_Ca2_psd_Substrate _p[107]
#define CaMKII_CaM_Ca4_psd_Substrate _p[108]
#define total_CaMKII_activated _p[109]
#define cai _p[110]
#define time _p[111]
#define ReactionFlux0 _p[112]
#define ReactionFlux1 _p[113]
#define ReactionFlux2 _p[114]
#define ReactionFlux3 _p[115]
#define ReactionFlux4 _p[116]
#define ReactionFlux5 _p[117]
#define ReactionFlux6 _p[118]
#define ReactionFlux7 _p[119]
#define ReactionFlux8 _p[120]
#define ReactionFlux9 _p[121]
#define ReactionFlux10 _p[122]
#define ReactionFlux11 _p[123]
#define ReactionFlux12 _p[124]
#define ReactionFlux13 _p[125]
#define ReactionFlux14 _p[126]
#define ReactionFlux15 _p[127]
#define ReactionFlux16 _p[128]
#define ReactionFlux17 _p[129]
#define ReactionFlux18 _p[130]
#define ReactionFlux19 _p[131]
#define ReactionFlux20 _p[132]
#define ReactionFlux21 _p[133]
#define ReactionFlux22 _p[134]
#define ReactionFlux23 _p[135]
#define ReactionFlux24 _p[136]
#define ReactionFlux25 _p[137]
#define ReactionFlux26 _p[138]
#define ReactionFlux27 _p[139]
#define ReactionFlux28 _p[140]
#define ReactionFlux29 _p[141]
#define ReactionFlux30 _p[142]
#define ReactionFlux31 _p[143]
#define ReactionFlux32 _p[144]
#define ReactionFlux33 _p[145]
#define ReactionFlux34 _p[146]
#define ReactionFlux35 _p[147]
#define ReactionFlux36 _p[148]
#define ReactionFlux37 _p[149]
#define ReactionFlux38 _p[150]
#define ReactionFlux39 _p[151]
#define ReactionFlux40 _p[152]
#define ReactionFlux41 _p[153]
#define ReactionFlux42 _p[154]
#define ReactionFlux43 _p[155]
#define ReactionFlux44 _p[156]
#define ReactionFlux45 _p[157]
#define ReactionFlux46 _p[158]
#define ReactionFlux47 _p[159]
#define ReactionFlux48 _p[160]
#define ReactionFlux49 _p[161]
#define ReactionFlux50 _p[162]
#define ReactionFlux51 _p[163]
#define ReactionFlux52 _p[164]
#define ReactionFlux53 _p[165]
#define ReactionFlux54 _p[166]
#define ReactionFlux55 _p[167]
#define ReactionFlux56 _p[168]
#define ReactionFlux57 _p[169]
#define ReactionFlux58 _p[170]
#define ReactionFlux59 _p[171]
#define ReactionFlux60 _p[172]
#define ReactionFlux61 _p[173]
#define ReactionFlux62 _p[174]
#define ReactionFlux63 _p[175]
#define ReactionFlux64 _p[176]
#define ReactionFlux65 _p[177]
#define ReactionFlux66 _p[178]
#define ReactionFlux67 _p[179]
#define ReactionFlux68 _p[180]
#define ReactionFlux69 _p[181]
#define ReactionFlux70 _p[182]
#define ReactionFlux71 _p[183]
#define ReactionFlux72 _p[184]
#define ReactionFlux73 _p[185]
#define ReactionFlux74 _p[186]
#define ReactionFlux75 _p[187]
#define ReactionFlux76 _p[188]
#define ReactionFlux77 _p[189]
#define ReactionFlux78 _p[190]
#define ReactionFlux79 _p[191]
#define ReactionFlux80 _p[192]
#define ReactionFlux81 _p[193]
#define ReactionFlux82 _p[194]
#define ReactionFlux83 _p[195]
#define ReactionFlux84 _p[196]
#define ReactionFlux85 _p[197]
#define ReactionFlux86 _p[198]
#define ReactionFlux87 _p[199]
#define ReactionFlux88 _p[200]
#define ReactionFlux89 _p[201]
#define ReactionFlux90 _p[202]
#define ReactionFlux91 _p[203]
#define ReactionFlux92 _p[204]
#define ReactionFlux93 _p[205]
#define ReactionFlux94 _p[206]
#define ReactionFlux95 _p[207]
#define ReactionFlux96 _p[208]
#define ReactionFlux97 _p[209]
#define ReactionFlux98 _p[210]
#define ReactionFlux99 _p[211]
#define ReactionFlux100 _p[212]
#define ReactionFlux101 _p[213]
#define ReactionFlux102 _p[214]
#define ReactionFlux103 _p[215]
#define ReactionFlux104 _p[216]
#define ReactionFlux105 _p[217]
#define ReactionFlux106 _p[218]
#define ReactionFlux107 _p[219]
#define ReactionFlux108 _p[220]
#define ReactionFlux109 _p[221]
#define ReactionFlux110 _p[222]
#define ReactionFlux111 _p[223]
#define ReactionFlux112 _p[224]
#define ReactionFlux113 _p[225]
#define ReactionFlux114 _p[226]
#define ReactionFlux115 _p[227]
#define ReactionFlux116 _p[228]
#define ReactionFlux117 _p[229]
#define ReactionFlux118 _p[230]
#define ReactionFlux119 _p[231]
#define ReactionFlux120 _p[232]
#define ReactionFlux121 _p[233]
#define ReactionFlux122 _p[234]
#define ReactionFlux123 _p[235]
#define ReactionFlux124 _p[236]
#define ReactionFlux125 _p[237]
#define ReactionFlux126 _p[238]
#define ReactionFlux127 _p[239]
#define ReactionFlux128 _p[240]
#define ReactionFlux129 _p[241]
#define ReactionFlux130 _p[242]
#define ReactionFlux131 _p[243]
#define ReactionFlux132 _p[244]
#define ReactionFlux133 _p[245]
#define ReactionFlux134 _p[246]
#define ReactionFlux135 _p[247]
#define ReactionFlux136 _p[248]
#define ReactionFlux137 _p[249]
#define DAC5 _p[250]
#define DAC5_ATP _p[251]
#define DAC5_Ca _p[252]
#define DAC5_Ca_ATP _p[253]
#define DAC5_Ca_GaolfGTP _p[254]
#define DAC5_Ca_GaolfGTP_ATP _p[255]
#define DAC5_GaolfGTP _p[256]
#define DAC5_GaolfGTP_ATP _p[257]
#define DB56PP2A _p[258]
#define DB56PP2A_D32p75 _p[259]
#define DB56PP2A_pARPP21 _p[260]
#define DB56PP2Ap _p[261]
#define DB56PP2Ap_D32p75 _p[262]
#define DB56PP2Ap_pARPP21 _p[263]
#define DB72PP2A _p[264]
#define DB72PP2A_D32p34 _p[265]
#define DB72PP2A_D32p75 _p[266]
#define DB72PP2A_pARPP21 _p[267]
#define DB72PP2A_Ca_D32p34 _p[268]
#define DB72PP2A_Ca_D32p75 _p[269]
#define DB72PP2A_Ca _p[270]
#define DB72PP2A_Ca_pARPP21 _p[271]
#define DCaM _p[272]
#define DCaM_Ca2 _p[273]
#define DCaM_Ca4 _p[274]
#define DCaM_Ca4_pARPP21 _p[275]
#define DCaMKII _p[276]
#define DCaMKII_CaM_Ca4 _p[277]
#define DCaMKII_CaM _p[278]
#define DCaMKII_CaM_Ca2 _p[279]
#define DCaMKII_CaM_Ca2_psd _p[280]
#define DCaMKII_CaM_psd _p[281]
#define DCaMKII_CaM_Ca4_psd _p[282]
#define DCaMKII_psd _p[283]
#define DcAMP _p[284]
#define DSubstrate _p[285]
#define DCDK5 _p[286]
#define DCDK5_D32 _p[287]
#define DD1R _p[288]
#define DD1R_DA _p[289]
#define DD1R_Golf_DA _p[290]
#define DD1R_Golf _p[291]
#define DD32p34 _p[292]
#define DD32p75 _p[293]
#define DD32 _p[294]
#define DGaolfGDP _p[295]
#define DGaolfGTP _p[296]
#define DGbgolf _p[297]
#define DGolf _p[298]
#define DpCaMKII _p[299]
#define DpCaMKII_CaM_Ca4 _p[300]
#define DpCaMKII_CaM _p[301]
#define DpCaMKII_CaM_Ca2 _p[302]
#define DpCaMKII_CaM_Ca2_psd _p[303]
#define DpCaMKII_CaM_psd _p[304]
#define DpCaMKII_CaM_Ca4_psd _p[305]
#define DpCaMKII_psd _p[306]
#define DpSubstrate _p[307]
#define DPDE4 _p[308]
#define DPDE4_cAMP _p[309]
#define DPDE10r _p[310]
#define DPDE10r_cAMP _p[311]
#define DPDE10c _p[312]
#define DPDE10c_cAMP _p[313]
#define DPKA _p[314]
#define DPKAc _p[315]
#define DPKAc_B56PP2A _p[316]
#define DPKAc_D32 _p[317]
#define DPKAc_ARPP21 _p[318]
#define DPKA_Ca2MP _p[319]
#define DPKA_Ca4MP _p[320]
#define DPKAc_D32p75 _p[321]
#define DPKAreg _p[322]
#define DPP1 _p[323]
#define DPP1_pCaMKII_psd _p[324]
#define DPP1_pSubstrate _p[325]
#define DPP1_D32p34 _p[326]
#define DCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd _p[327]
#define DpCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd _p[328]
#define DCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 _p[329]
#define DpCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 _p[330]
#define DPP2B _p[331]
#define DPP2Bc _p[332]
#define DPP2Bc_D32p34 _p[333]
#define DPP2B_CaM _p[334]
#define DPP2B_CaM_Ca2 _p[335]
#define DpARPP21 _p[336]
#define DARPP21 _p[337]
#define DpCaMKII_psd_Substrate _p[338]
#define DpCaMKII_CaM_psd_Substrate _p[339]
#define DpCaMKII_CaM_Ca2_psd_Substrate _p[340]
#define DpCaMKII_CaM_Ca4_psd_Substrate _p[341]
#define DCaMKII_CaM_psd_Substrate _p[342]
#define DCaMKII_CaM_Ca2_psd_Substrate _p[343]
#define DCaMKII_CaM_Ca4_psd_Substrate _p[344]
#define Dtotal_CaMKII_activated _p[345]
#define v _p[346]
#define _g _p[347]
#define _ion_cai	*_ppvar[0]._pval
 
#if MAC
#if !defined(v)
#define v _mlhv
#endif
#if !defined(h)
#define h _mlhh
#endif
#endif
 
#if defined(__cplusplus)
extern "C" {
#endif
 static int hoc_nrnpointerindex =  -1;
 static Datum* _extcall_thread;
 static Prop* _extcall_prop;
 /* external NEURON variables */
 /* declaration of user functions */
 static void _hoc_assign_calculated_values(void);
 static void _hoc_observables_func(void);
 static int _mechtype;
extern void _nrn_cacheloop_reg(int, int);
extern void hoc_register_prop_size(int, int, int);
extern void hoc_register_limits(int, HocParmLimits*);
extern void hoc_register_units(int, HocParmUnits*);
extern void nrn_promote(Prop*, int, int);
extern Memb_func* memb_func;
 
#define NMODL_TEXT 1
#if NMODL_TEXT
static const char* nmodl_file_text;
static const char* nmodl_filename;
extern void hoc_reg_nmodl_text(int, const char*);
extern void hoc_reg_nmodl_filename(int, const char*);
#endif

 extern void _nrn_setdata_reg(int, void(*)(Prop*));
 static void _setdata(Prop* _prop) {
 _extcall_prop = _prop;
 }
 static void _hoc_setdata() {
 Prop *_prop, *hoc_getdata_range(int);
 _prop = hoc_getdata_range(_mechtype);
   _setdata(_prop);
 hoc_retpushx(1.);
}
 /* connect user functions to hoc names */
 static VoidFunc hoc_intfunc[] = {
 "setdata_D1_LTP_time_window_Luca_cai_initials", _hoc_setdata,
 "assign_calculated_values_D1_LTP_time_window_Luca_cai_initials", _hoc_assign_calculated_values,
 "observables_func_D1_LTP_time_window_Luca_cai_initials", _hoc_observables_func,
 0, 0
};
 /* declare global and static user variables */
#define kf_R137 kf_R137_D1_LTP_time_window_Luca_cai_initials
 double kf_R137 = 10;
#define kr_R136 kr_R136_D1_LTP_time_window_Luca_cai_initials
 double kr_R136 = 0.00540008;
#define kf_R136 kf_R136_D1_LTP_time_window_Luca_cai_initials
 double kf_R136 = 1.10002e-06;
#define kf_R135 kf_R135_D1_LTP_time_window_Luca_cai_initials
 double kf_R135 = 0.00390032;
#define kr_R134 kr_R134_D1_LTP_time_window_Luca_cai_initials
 double kr_R134 = 0.0229985;
#define kf_R134 kf_R134_D1_LTP_time_window_Luca_cai_initials
 double kf_R134 = 3.59998e-07;
#define kf_R133 kf_R133_D1_LTP_time_window_Luca_cai_initials
 double kf_R133 = 10;
#define kr_R132 kr_R132_D1_LTP_time_window_Luca_cai_initials
 double kr_R132 = 0.00540008;
#define kf_R132 kf_R132_D1_LTP_time_window_Luca_cai_initials
 double kf_R132 = 1.10002e-06;
#define kf_R131 kf_R131_D1_LTP_time_window_Luca_cai_initials
 double kf_R131 = 0.00390032;
#define kr_R130 kr_R130_D1_LTP_time_window_Luca_cai_initials
 double kr_R130 = 0.0229985;
#define kf_R130 kf_R130_D1_LTP_time_window_Luca_cai_initials
 double kf_R130 = 3.59998e-07;
#define kr_R129 kr_R129_D1_LTP_time_window_Luca_cai_initials
 double kr_R129 = 0.000500035;
#define kf_R129 kf_R129_D1_LTP_time_window_Luca_cai_initials
 double kf_R129 = 1e-06;
#define kr_R128 kr_R128_D1_LTP_time_window_Luca_cai_initials
 double kr_R128 = 0.000500035;
#define kf_R128 kf_R128_D1_LTP_time_window_Luca_cai_initials
 double kf_R128 = 0.000500035;
#define kr_R127 kr_R127_D1_LTP_time_window_Luca_cai_initials
 double kr_R127 = 0.000500035;
#define kf_R127 kf_R127_D1_LTP_time_window_Luca_cai_initials
 double kf_R127 = 0.000500035;
#define kr_R126 kr_R126_D1_LTP_time_window_Luca_cai_initials
 double kr_R126 = 0.000500035;
#define kf_R126 kf_R126_D1_LTP_time_window_Luca_cai_initials
 double kf_R126 = 0.000500035;
#define kr_R125 kr_R125_D1_LTP_time_window_Luca_cai_initials
 double kr_R125 = 0.000500035;
#define kf_R125 kf_R125_D1_LTP_time_window_Luca_cai_initials
 double kf_R125 = 0.000500035;
#define kr_R124 kr_R124_D1_LTP_time_window_Luca_cai_initials
 double kr_R124 = 0.00199986;
#define kf_R124 kf_R124_D1_LTP_time_window_Luca_cai_initials
 double kf_R124 = 6.00067e-06;
#define kr_R123 kr_R123_D1_LTP_time_window_Luca_cai_initials
 double kr_R123 = 0.1;
#define kf_R123 kf_R123_D1_LTP_time_window_Luca_cai_initials
 double kf_R123 = 0.0001;
#define kr_R122 kr_R122_D1_LTP_time_window_Luca_cai_initials
 double kr_R122 = 4;
#define kf_R122 kf_R122_D1_LTP_time_window_Luca_cai_initials
 double kf_R122 = 0.0001;
#define kr_R121 kr_R121_D1_LTP_time_window_Luca_cai_initials
 double kr_R121 = 0.4;
#define kf_R121 kf_R121_D1_LTP_time_window_Luca_cai_initials
 double kf_R121 = 0.0001;
#define kr_R120 kr_R120_D1_LTP_time_window_Luca_cai_initials
 double kr_R120 = 0.0400037;
#define kf_R120 kf_R120_D1_LTP_time_window_Luca_cai_initials
 double kf_R120 = 0.0001;
#define kf_R119 kf_R119_D1_LTP_time_window_Luca_cai_initials
 double kf_R119 = 0.000500035;
#define kf_R118 kf_R118_D1_LTP_time_window_Luca_cai_initials
 double kf_R118 = 0.001;
#define kr_R117 kr_R117_D1_LTP_time_window_Luca_cai_initials
 double kr_R117 = 0.001;
#define kf_R117 kf_R117_D1_LTP_time_window_Luca_cai_initials
 double kf_R117 = 8.00018e-07;
#define kr_R116 kr_R116_D1_LTP_time_window_Luca_cai_initials
 double kr_R116 = 0.01;
#define kf_R116 kf_R116_D1_LTP_time_window_Luca_cai_initials
 double kf_R116 = 0.0001;
#define kr_R115 kr_R115_D1_LTP_time_window_Luca_cai_initials
 double kr_R115 = 0.00199986;
#define kf_R115 kf_R115_D1_LTP_time_window_Luca_cai_initials
 double kf_R115 = 6.00067e-06;
#define kr_R114 kr_R114_D1_LTP_time_window_Luca_cai_initials
 double kr_R114 = 0.4;
#define kf_R114 kf_R114_D1_LTP_time_window_Luca_cai_initials
 double kf_R114 = 0.0001;
#define kr_R113 kr_R113_D1_LTP_time_window_Luca_cai_initials
 double kr_R113 = 0.0400037;
#define kf_R113 kf_R113_D1_LTP_time_window_Luca_cai_initials
 double kf_R113 = 0.0001;
#define kr_R112 kr_R112_D1_LTP_time_window_Luca_cai_initials
 double kr_R112 = 0.000400037;
#define kf_R112 kf_R112_D1_LTP_time_window_Luca_cai_initials
 double kf_R112 = 0.0001;
#define kr_R111 kr_R111_D1_LTP_time_window_Luca_cai_initials
 double kr_R111 = 1e-06;
#define kf_R111 kf_R111_D1_LTP_time_window_Luca_cai_initials
 double kf_R111 = 0.000500035;
#define kr_R110 kr_R110_D1_LTP_time_window_Luca_cai_initials
 double kr_R110 = 1e-06;
#define kf_R110 kf_R110_D1_LTP_time_window_Luca_cai_initials
 double kf_R110 = 0.000500035;
#define kr_R109 kr_R109_D1_LTP_time_window_Luca_cai_initials
 double kr_R109 = 1e-06;
#define kf_R109 kf_R109_D1_LTP_time_window_Luca_cai_initials
 double kf_R109 = 0.000500035;
#define kr_R108 kr_R108_D1_LTP_time_window_Luca_cai_initials
 double kr_R108 = 1e-06;
#define kf_R108 kf_R108_D1_LTP_time_window_Luca_cai_initials
 double kf_R108 = 0.000500035;
#define kf_R107 kf_R107_D1_LTP_time_window_Luca_cai_initials
 double kf_R107 = 0.01;
#define kr_R106 kr_R106_D1_LTP_time_window_Luca_cai_initials
 double kr_R106 = 0.01;
#define kf_R106 kf_R106_D1_LTP_time_window_Luca_cai_initials
 double kf_R106 = 5.00035e-07;
#define kf_R105 kf_R105_D1_LTP_time_window_Luca_cai_initials
 double kf_R105 = 0.01;
#define kr_R104 kr_R104_D1_LTP_time_window_Luca_cai_initials
 double kr_R104 = 0.01;
#define kf_R104 kf_R104_D1_LTP_time_window_Luca_cai_initials
 double kf_R104 = 5.00035e-07;
#define kf_R103 kf_R103_D1_LTP_time_window_Luca_cai_initials
 double kf_R103 = 0.01;
#define kr_R102 kr_R102_D1_LTP_time_window_Luca_cai_initials
 double kr_R102 = 0.01;
#define kf_R102 kf_R102_D1_LTP_time_window_Luca_cai_initials
 double kf_R102 = 5.00035e-07;
#define kf_R101 kf_R101_D1_LTP_time_window_Luca_cai_initials
 double kf_R101 = 0.01;
#define kr_R100 kr_R100_D1_LTP_time_window_Luca_cai_initials
 double kr_R100 = 0.01;
#define kf_R100 kf_R100_D1_LTP_time_window_Luca_cai_initials
 double kf_R100 = 5.00035e-07;
#define kf_R99 kf_R99_D1_LTP_time_window_Luca_cai_initials
 double kf_R99 = 0.01;
#define kr_R98 kr_R98_D1_LTP_time_window_Luca_cai_initials
 double kr_R98 = 0.01;
#define kf_R98 kf_R98_D1_LTP_time_window_Luca_cai_initials
 double kf_R98 = 5.00035e-07;
#define kf_R97 kf_R97_D1_LTP_time_window_Luca_cai_initials
 double kf_R97 = 0.01;
#define kr_R96 kr_R96_D1_LTP_time_window_Luca_cai_initials
 double kr_R96 = 0.01;
#define kf_R96 kf_R96_D1_LTP_time_window_Luca_cai_initials
 double kf_R96 = 5.00035e-07;
#define kf_R95 kf_R95_D1_LTP_time_window_Luca_cai_initials
 double kf_R95 = 0.0001;
#define kf_R94 kf_R94_D1_LTP_time_window_Luca_cai_initials
 double kf_R94 = 0.01;
#define kr_R93 kr_R93_D1_LTP_time_window_Luca_cai_initials
 double kr_R93 = 0.01;
#define kf_R93 kf_R93_D1_LTP_time_window_Luca_cai_initials
 double kf_R93 = 5.00035e-07;
#define kf_R92 kf_R92_D1_LTP_time_window_Luca_cai_initials
 double kf_R92 = 0.01;
#define kr_R91 kr_R91_D1_LTP_time_window_Luca_cai_initials
 double kr_R91 = 0.001;
#define kf_R91 kf_R91_D1_LTP_time_window_Luca_cai_initials
 double kf_R91 = 5.00035e-07;
#define kr_R90 kr_R90_D1_LTP_time_window_Luca_cai_initials
 double kr_R90 = 0.1;
#define kf_R90 kf_R90_D1_LTP_time_window_Luca_cai_initials
 double kf_R90 = 4.00037e-06;
#define kf_R89 kf_R89_D1_LTP_time_window_Luca_cai_initials
 double kf_R89 = 0.001;
#define kr_R88 kr_R88_D1_LTP_time_window_Luca_cai_initials
 double kr_R88 = 0.1;
#define kf_R88 kf_R88_D1_LTP_time_window_Luca_cai_initials
 double kf_R88 = 7.00003e-06;
#define kf_R87 kf_R87_D1_LTP_time_window_Luca_cai_initials
 double kf_R87 = 0.01;
#define kr_R86 kr_R86_D1_LTP_time_window_Luca_cai_initials
 double kr_R86 = 0.1;
#define kf_R86 kf_R86_D1_LTP_time_window_Luca_cai_initials
 double kf_R86 = 4.00037e-06;
#define kf_R85 kf_R85_D1_LTP_time_window_Luca_cai_initials
 double kf_R85 = 0.001;
#define kr_R84 kr_R84_D1_LTP_time_window_Luca_cai_initials
 double kr_R84 = 0.1;
#define kf_R84 kf_R84_D1_LTP_time_window_Luca_cai_initials
 double kf_R84 = 7.00003e-06;
#define kf_R83 kf_R83_D1_LTP_time_window_Luca_cai_initials
 double kf_R83 = 0.01;
#define kr_R82 kr_R82_D1_LTP_time_window_Luca_cai_initials
 double kr_R82 = 0.01;
#define kf_R82 kf_R82_D1_LTP_time_window_Luca_cai_initials
 double kf_R82 = 0.000500035;
#define kf_R81 kf_R81_D1_LTP_time_window_Luca_cai_initials
 double kf_R81 = 0.01;
#define kr_R80 kr_R80_D1_LTP_time_window_Luca_cai_initials
 double kr_R80 = 0.2;
#define kf_R80 kf_R80_D1_LTP_time_window_Luca_cai_initials
 double kf_R80 = 4.49987e-05;
#define kr_R79 kr_R79_D1_LTP_time_window_Luca_cai_initials
 double kr_R79 = 0.4;
#define kf_R79 kf_R79_D1_LTP_time_window_Luca_cai_initials
 double kf_R79 = 0.0001;
#define kr_R78 kr_R78_D1_LTP_time_window_Luca_cai_initials
 double kr_R78 = 0.0400037;
#define kf_R78 kf_R78_D1_LTP_time_window_Luca_cai_initials
 double kf_R78 = 0.0001;
#define kr_R77 kr_R77_D1_LTP_time_window_Luca_cai_initials
 double kr_R77 = 0.000400037;
#define kf_R77 kf_R77_D1_LTP_time_window_Luca_cai_initials
 double kf_R77 = 0.0001;
#define kr_R76 kr_R76_D1_LTP_time_window_Luca_cai_initials
 double kr_R76 = 0.00199986;
#define kf_R76 kf_R76_D1_LTP_time_window_Luca_cai_initials
 double kf_R76 = 6.00067e-06;
#define kr_R75 kr_R75_D1_LTP_time_window_Luca_cai_initials
 double kr_R75 = 0.01;
#define kf_R75 kf_R75_D1_LTP_time_window_Luca_cai_initials
 double kf_R75 = 0.0001;
#define kr_R74 kr_R74_D1_LTP_time_window_Luca_cai_initials
 double kr_R74 = 0.00199986;
#define kf_R74 kf_R74_D1_LTP_time_window_Luca_cai_initials
 double kf_R74 = 6.00067e-06;
#define kr_R73 kr_R73_D1_LTP_time_window_Luca_cai_initials
 double kr_R73 = 0.1;
#define kf_R73 kf_R73_D1_LTP_time_window_Luca_cai_initials
 double kf_R73 = 0.0001;
#define kr_R72 kr_R72_D1_LTP_time_window_Luca_cai_initials
 double kr_R72 = 4;
#define kf_R72 kf_R72_D1_LTP_time_window_Luca_cai_initials
 double kf_R72 = 0.0001;
#define kr_R71 kr_R71_D1_LTP_time_window_Luca_cai_initials
 double kr_R71 = 0.4;
#define kf_R71 kf_R71_D1_LTP_time_window_Luca_cai_initials
 double kf_R71 = 0.0001;
#define kr_R70 kr_R70_D1_LTP_time_window_Luca_cai_initials
 double kr_R70 = 0.0400037;
#define kf_R70 kf_R70_D1_LTP_time_window_Luca_cai_initials
 double kf_R70 = 0.0001;
#define kr_R69 kr_R69_D1_LTP_time_window_Luca_cai_initials
 double kr_R69 = 0.00199986;
#define kf_R69 kf_R69_D1_LTP_time_window_Luca_cai_initials
 double kf_R69 = 0.0001;
#define kr_R68 kr_R68_D1_LTP_time_window_Luca_cai_initials
 double kr_R68 = 0.25;
#define kf_R68 kf_R68_D1_LTP_time_window_Luca_cai_initials
 double kf_R68 = 6.00067e-05;
#define kr_R67 kr_R67_D1_LTP_time_window_Luca_cai_initials
 double kr_R67 = 0.25;
#define kf_R67 kf_R67_D1_LTP_time_window_Luca_cai_initials
 double kf_R67 = 6.00067e-05;
#define kf_R66 kf_R66_D1_LTP_time_window_Luca_cai_initials
 double kf_R66 = 0.001;
#define kf_R65 kf_R65_D1_LTP_time_window_Luca_cai_initials
 double kf_R65 = 0.001;
#define kf_R64 kf_R64_D1_LTP_time_window_Luca_cai_initials
 double kf_R64 = 0.001;
#define kf_R63 kf_R63_D1_LTP_time_window_Luca_cai_initials
 double kf_R63 = 0.001;
#define kf_R62 kf_R62_D1_LTP_time_window_Luca_cai_initials
 double kf_R62 = 0.00064998;
#define kf_R61 kf_R61_D1_LTP_time_window_Luca_cai_initials
 double kf_R61 = 0.0249977;
#define kf_R60 kf_R60_D1_LTP_time_window_Luca_cai_initials
 double kf_R60 = 7.50067e-07;
#define kf_R59 kf_R59_D1_LTP_time_window_Luca_cai_initials
 double kf_R59 = 0.000500035;
#define kf_R58 kf_R58_D1_LTP_time_window_Luca_cai_initials
 double kf_R58 = 1.99986e-06;
#define kf_R57 kf_R57_D1_LTP_time_window_Luca_cai_initials
 double kf_R57 = 0.001;
#define kf_R56 kf_R56_D1_LTP_time_window_Luca_cai_initials
 double kf_R56 = 0.00254976;
#define kf_R55 kf_R55_D1_LTP_time_window_Luca_cai_initials
 double kf_R55 = 0.0500035;
#define kr_R54 kr_R54_D1_LTP_time_window_Luca_cai_initials
 double kr_R54 = 0.01;
#define kf_R54 kf_R54_D1_LTP_time_window_Luca_cai_initials
 double kf_R54 = 1e-06;
#define kr_R53 kr_R53_D1_LTP_time_window_Luca_cai_initials
 double kr_R53 = 0.001;
#define kf_R53 kf_R53_D1_LTP_time_window_Luca_cai_initials
 double kf_R53 = 0.01;
#define kr_R52 kr_R52_D1_LTP_time_window_Luca_cai_initials
 double kr_R52 = 0.001;
#define kf_R52 kf_R52_D1_LTP_time_window_Luca_cai_initials
 double kf_R52 = 0.01;
#define kr_R51 kr_R51_D1_LTP_time_window_Luca_cai_initials
 double kr_R51 = 0.001;
#define kf_R51 kf_R51_D1_LTP_time_window_Luca_cai_initials
 double kf_R51 = 1.29987e-06;
#define kr_R50 kr_R50_D1_LTP_time_window_Luca_cai_initials
 double kr_R50 = 0.001;
#define kf_R50 kf_R50_D1_LTP_time_window_Luca_cai_initials
 double kf_R50 = 7.50067e-08;
#define kr_R49 kr_R49_D1_LTP_time_window_Luca_cai_initials
 double kr_R49 = 0.001;
#define kf_R49 kf_R49_D1_LTP_time_window_Luca_cai_initials
 double kf_R49 = 1e-07;
#define kr_R48 kr_R48_D1_LTP_time_window_Luca_cai_initials
 double kr_R48 = 0.001;
#define kf_R48 kf_R48_D1_LTP_time_window_Luca_cai_initials
 double kf_R48 = 2.54976e-06;
#define kf_R47 kf_R47_D1_LTP_time_window_Luca_cai_initials
 double kf_R47 = 0.1;
#define kf_R46 kf_R46_D1_LTP_time_window_Luca_cai_initials
 double kf_R46 = 0.01;
#define kr_R45 kr_R45_D1_LTP_time_window_Luca_cai_initials
 double kr_R45 = 0.00199986;
#define kf_R45 kf_R45_D1_LTP_time_window_Luca_cai_initials
 double kf_R45 = 0.0001;
#define kf_R44 kf_R44_D1_LTP_time_window_Luca_cai_initials
 double kf_R44 = 0.00299985;
#define kr_R43 kr_R43_D1_LTP_time_window_Luca_cai_initials
 double kr_R43 = 0.001;
#define kf_R43 kf_R43_D1_LTP_time_window_Luca_cai_initials
 double kf_R43 = 1e-09;
#define kf_R42 kf_R42_D1_LTP_time_window_Luca_cai_initials
 double kf_R42 = 0.00249977;
#define kr_R41 kr_R41_D1_LTP_time_window_Luca_cai_initials
 double kr_R41 = 0.001;
#define kf_R41 kf_R41_D1_LTP_time_window_Luca_cai_initials
 double kf_R41 = 2.99985e-05;
#define kr_R40 kr_R40_D1_LTP_time_window_Luca_cai_initials
 double kr_R40 = 2.99985e-05;
#define kf_R40 kf_R40_D1_LTP_time_window_Luca_cai_initials
 double kf_R40 = 0.0500035;
#define kr_R39 kr_R39_D1_LTP_time_window_Luca_cai_initials
 double kr_R39 = 0.0500035;
#define kf_R39 kf_R39_D1_LTP_time_window_Luca_cai_initials
 double kf_R39 = 3.46019e-05;
#define kr_R38 kr_R38_D1_LTP_time_window_Luca_cai_initials
 double kr_R38 = 0.350002;
#define kf_R38 kf_R38_D1_LTP_time_window_Luca_cai_initials
 double kf_R38 = 2.60016e-05;
#define kf_R37 kf_R37_D1_LTP_time_window_Luca_cai_initials
 double kf_R37 = 8.00018e-06;
#define kf_R36 kf_R36_D1_LTP_time_window_Luca_cai_initials
 double kf_R36 = 0.00120005;
#define kr_R35 kr_R35_D1_LTP_time_window_Luca_cai_initials
 double kr_R35 = 0.001;
#define kf_R35 kf_R35_D1_LTP_time_window_Luca_cai_initials
 double kf_R35 = 5.00035e-07;
#define kr_R34 kr_R34_D1_LTP_time_window_Luca_cai_initials
 double kr_R34 = 0.001;
#define kf_R34 kf_R34_D1_LTP_time_window_Luca_cai_initials
 double kf_R34 = 5.00035e-07;
#define kf_R33 kf_R33_D1_LTP_time_window_Luca_cai_initials
 double kf_R33 = 0.00299985;
#define kf_R32 kf_R32_D1_LTP_time_window_Luca_cai_initials
 double kf_R32 = 0.00299985;
#define kf_R31 kf_R31_D1_LTP_time_window_Luca_cai_initials
 double kf_R31 = 0.00150003;
#define kr_R30 kr_R30_D1_LTP_time_window_Luca_cai_initials
 double kr_R30 = 0.1;
#define kf_R30 kf_R30_D1_LTP_time_window_Luca_cai_initials
 double kf_R30 = 8.00018e-06;
#define kr_R29 kr_R29_D1_LTP_time_window_Luca_cai_initials
 double kr_R29 = 0.001;
#define kf_R29 kf_R29_D1_LTP_time_window_Luca_cai_initials
 double kf_R29 = 0.01;
#define kr_R28 kr_R28_D1_LTP_time_window_Luca_cai_initials
 double kr_R28 = 0.01;
#define kf_R28 kf_R28_D1_LTP_time_window_Luca_cai_initials
 double kf_R28 = 1e-06;
#define kr_R27 kr_R27_D1_LTP_time_window_Luca_cai_initials
 double kr_R27 = 2.99985e-05;
#define kf_R27 kf_R27_D1_LTP_time_window_Luca_cai_initials
 double kf_R27 = 0.0001;
#define kr_R26 kr_R26_D1_LTP_time_window_Luca_cai_initials
 double kr_R26 = 0.1;
#define kf_R26 kf_R26_D1_LTP_time_window_Luca_cai_initials
 double kf_R26 = 0.0001;
#define kr_R25 kr_R25_D1_LTP_time_window_Luca_cai_initials
 double kr_R25 = 1.99986e-07;
#define kf_R25 kf_R25_D1_LTP_time_window_Luca_cai_initials
 double kf_R25 = 6.00067e-06;
#define kr_R24 kr_R24_D1_LTP_time_window_Luca_cai_initials
 double kr_R24 = 1;
#define kf_R24 kf_R24_D1_LTP_time_window_Luca_cai_initials
 double kf_R24 = 0.0001;
#define kr_R23 kr_R23_D1_LTP_time_window_Luca_cai_initials
 double kr_R23 = 0.0001;
#define kf_R23 kf_R23_D1_LTP_time_window_Luca_cai_initials
 double kf_R23 = 0.00129987;
#define kf_R22 kf_R22_D1_LTP_time_window_Luca_cai_initials
 double kf_R22 = 0.00800018;
#define kf_R21 kf_R21_D1_LTP_time_window_Luca_cai_initials
 double kf_R21 = 0.00150003;
#define kf_R20 kf_R20_D1_LTP_time_window_Luca_cai_initials
 double kf_R20 = 0.00800018;
#define kr_R19 kr_R19_D1_LTP_time_window_Luca_cai_initials
 double kr_R19 = 0.1;
#define kf_R19 kf_R19_D1_LTP_time_window_Luca_cai_initials
 double kf_R19 = 1.50003e-05;
#define kr_R18 kr_R18_D1_LTP_time_window_Luca_cai_initials
 double kr_R18 = 0.1;
#define kf_R18 kf_R18_D1_LTP_time_window_Luca_cai_initials
 double kf_R18 = 8.00018e-06;
#define kr_R17 kr_R17_D1_LTP_time_window_Luca_cai_initials
 double kr_R17 = 0.1;
#define kf_R17 kf_R17_D1_LTP_time_window_Luca_cai_initials
 double kf_R17 = 1.50003e-05;
#define kr_R16 kr_R16_D1_LTP_time_window_Luca_cai_initials
 double kr_R16 = 0.01;
#define kf_R16 kf_R16_D1_LTP_time_window_Luca_cai_initials
 double kf_R16 = 1e-05;
#define kr_R15 kr_R15_D1_LTP_time_window_Luca_cai_initials
 double kr_R15 = 0.1;
#define kf_R15 kf_R15_D1_LTP_time_window_Luca_cai_initials
 double kf_R15 = 0.0001;
#define kf_R14 kf_R14_D1_LTP_time_window_Luca_cai_initials
 double kf_R14 = 0.01;
#define kr_R13 kr_R13_D1_LTP_time_window_Luca_cai_initials
 double kr_R13 = 0.1;
#define kf_R13 kf_R13_D1_LTP_time_window_Luca_cai_initials
 double kf_R13 = 1e-06;
#define kr_R12 kr_R12_D1_LTP_time_window_Luca_cai_initials
 double kr_R12 = 0.00150003;
#define kf_R12 kf_R12_D1_LTP_time_window_Luca_cai_initials
 double kf_R12 = 0.001;
#define kf_R11 kf_R11_D1_LTP_time_window_Luca_cai_initials
 double kf_R11 = 0.000199986;
#define kr_R10 kr_R10_D1_LTP_time_window_Luca_cai_initials
 double kr_R10 = 0.000299985;
#define kf_R10 kf_R10_D1_LTP_time_window_Luca_cai_initials
 double kf_R10 = 1e-06;
#define kf_R9 kf_R9_D1_LTP_time_window_Luca_cai_initials
 double kf_R9 = 0.01;
#define kr_R8 kr_R8_D1_LTP_time_window_Luca_cai_initials
 double kr_R8 = 0.2;
#define kf_R8 kf_R8_D1_LTP_time_window_Luca_cai_initials
 double kf_R8 = 1e-05;
#define kr_R7 kr_R7_D1_LTP_time_window_Luca_cai_initials
 double kr_R7 = 2.99985e-06;
#define kf_R7 kf_R7_D1_LTP_time_window_Luca_cai_initials
 double kf_R7 = 0.0001;
#define kr_R6 kr_R6_D1_LTP_time_window_Luca_cai_initials
 double kr_R6 = 2.99999;
#define kf_R6 kf_R6_D1_LTP_time_window_Luca_cai_initials
 double kf_R6 = 0.0001;
#define kr_R5 kr_R5_D1_LTP_time_window_Luca_cai_initials
 double kr_R5 = 0.0199986;
#define kf_R5 kf_R5_D1_LTP_time_window_Luca_cai_initials
 double kf_R5 = 6.00067e-06;
#define kr_R4 kr_R4_D1_LTP_time_window_Luca_cai_initials
 double kr_R4 = 0.001;
#define kf_R4 kf_R4_D1_LTP_time_window_Luca_cai_initials
 double kf_R4 = 0.01;
#define kr_R3 kr_R3_D1_LTP_time_window_Luca_cai_initials
 double kr_R3 = 0.25;
#define kf_R3 kf_R3_D1_LTP_time_window_Luca_cai_initials
 double kf_R3 = 5.00035e-05;
#define kr_R2 kr_R2_D1_LTP_time_window_Luca_cai_initials
 double kr_R2 = 0.25;
#define kf_R2 kf_R2_D1_LTP_time_window_Luca_cai_initials
 double kf_R2 = 5.00035e-05;
#define kf_R1 kf_R1_D1_LTP_time_window_Luca_cai_initials
 double kf_R1 = 0.0150003;
#define kf_R0 kf_R0_D1_LTP_time_window_Luca_cai_initials
 double kf_R0 = 0.0299985;
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "kf_R0_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R1_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R2_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R2_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R3_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R3_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R4_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R4_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R5_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R5_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R6_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R6_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R7_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R7_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R8_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R8_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R9_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R10_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R10_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R11_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R12_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R12_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R13_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R13_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R14_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R15_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R15_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R16_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R16_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R17_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R17_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R18_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R18_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R19_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R19_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R20_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R21_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R22_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R23_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R23_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R24_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R24_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R25_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R25_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R26_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R26_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R27_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R27_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R28_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R28_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R29_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R29_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R30_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R30_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R31_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R32_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R33_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R34_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R34_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R35_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R35_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R36_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R37_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R38_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R38_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R39_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R39_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R40_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kr_R40_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kf_R41_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R41_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R42_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R43_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter^2-millisecond",
 "kr_R43_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R44_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R45_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R45_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R46_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R47_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kf_R48_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R48_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R49_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R49_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R50_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R50_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R51_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R51_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R52_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R52_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R53_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R53_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R54_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R54_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R55_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R56_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kf_R57_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R58_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kf_R59_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R60_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kf_R61_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R62_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kf_R63_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R64_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R65_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R66_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R67_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R67_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R68_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R68_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R69_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R69_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R70_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R70_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R71_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R71_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R72_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R72_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R73_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R73_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R74_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R74_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R75_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R75_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R76_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R76_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R77_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R77_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R78_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R78_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R79_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R79_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R80_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R80_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R81_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R82_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R82_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R83_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R84_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R84_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R85_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R86_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R86_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R87_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R88_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R88_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R89_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R90_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R90_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R91_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R91_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R92_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R93_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R93_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R94_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R95_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R96_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R96_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R97_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R98_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R98_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R99_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R100_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R100_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R101_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R102_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R102_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R103_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R104_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R104_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R105_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R106_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R106_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R107_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R108_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kr_R108_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R109_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kr_R109_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R110_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kr_R110_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R111_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kr_R111_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R112_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R112_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R113_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R113_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R114_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R114_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R115_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R115_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R116_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R116_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R117_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R117_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R118_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R119_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R120_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R120_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R121_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R121_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R122_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R122_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R123_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R123_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R124_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R124_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R125_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kr_R125_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R126_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kr_R126_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R127_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kr_R127_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R128_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kr_R128_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R129_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kr_R129_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R130_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R130_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R131_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R132_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R132_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R133_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R134_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R134_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R135_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R136_D1_LTP_time_window_Luca_cai_initials", "/nanomole/liter-millisecond",
 "kr_R136_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "kf_R137_D1_LTP_time_window_Luca_cai_initials", "/millisecond",
 "DA_start_D1_LTP_time_window_Luca_cai_initials", "millisecond",
 "DA_max_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "AC5_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "AC5_ATP_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "AC5_Ca_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "AC5_Ca_ATP_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "AC5_Ca_GaolfGTP_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "AC5_Ca_GaolfGTP_ATP_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "AC5_GaolfGTP_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "AC5_GaolfGTP_ATP_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "B56PP2A_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "B56PP2A_D32p75_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "B56PP2A_pARPP21_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "B56PP2Ap_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "B56PP2Ap_D32p75_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "B56PP2Ap_pARPP21_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "B72PP2A_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "B72PP2A_D32p34_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "B72PP2A_D32p75_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "B72PP2A_pARPP21_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "B72PP2A_Ca_D32p34_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "B72PP2A_Ca_D32p75_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "B72PP2A_Ca_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "B72PP2A_Ca_pARPP21_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaM_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaM_Ca2_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaM_Ca4_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaM_Ca4_pARPP21_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaMKII_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaMKII_CaM_Ca4_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaMKII_CaM_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaMKII_CaM_Ca2_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaMKII_CaM_Ca2_psd_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaMKII_CaM_psd_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaMKII_CaM_Ca4_psd_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaMKII_psd_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "cAMP_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "Substrate_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CDK5_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CDK5_D32_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "D1R_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "D1R_DA_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "D1R_Golf_DA_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "D1R_Golf_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "D32p34_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "D32p75_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "D32_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "GaolfGDP_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "GaolfGTP_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "Gbgolf_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "Golf_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pCaMKII_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pCaMKII_CaM_Ca4_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pCaMKII_CaM_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pCaMKII_CaM_Ca2_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pCaMKII_CaM_Ca2_psd_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pCaMKII_CaM_psd_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pCaMKII_CaM_Ca4_psd_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pCaMKII_psd_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pSubstrate_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PDE4_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PDE4_cAMP_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PDE10r_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PDE10r_cAMP_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PDE10c_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PDE10c_cAMP_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PKA_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PKAc_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PKAc_B56PP2A_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PKAc_D32_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PKAc_ARPP21_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PKA_Ca2MP_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PKA_Ca4MP_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PKAc_D32p75_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PKAreg_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PP1_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PP1_pCaMKII_psd_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PP1_pSubstrate_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PP1_D32p34_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaMKII_CaM_Ca4_CaMKII_CaM_Ca4_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PP2B_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PP2Bc_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PP2Bc_D32p34_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PP2B_CaM_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "PP2B_CaM_Ca2_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pARPP21_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "ARPP21_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pCaMKII_psd_Substrate_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pCaMKII_CaM_psd_Substrate_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pCaMKII_CaM_Ca2_psd_Substrate_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "pCaMKII_CaM_Ca4_psd_Substrate_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaMKII_CaM_psd_Substrate_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaMKII_CaM_Ca2_psd_Substrate_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "CaMKII_CaM_Ca4_psd_Substrate_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 "total_CaMKII_activated_D1_LTP_time_window_Luca_cai_initials", "nanomole/liter",
 0,0
};
 static double ARPP210 = 0;
 static double AC5_GaolfGTP_ATP0 = 0;
 static double AC5_GaolfGTP0 = 0;
 static double AC5_Ca_GaolfGTP_ATP0 = 0;
 static double AC5_Ca_GaolfGTP0 = 0;
 static double AC5_Ca_ATP0 = 0;
 static double AC5_Ca0 = 0;
 static double AC5_ATP0 = 0;
 static double AC50 = 0;
 static double B72PP2A_Ca_pARPP210 = 0;
 static double B72PP2A_Ca0 = 0;
 static double B72PP2A_Ca_D32p750 = 0;
 static double B72PP2A_Ca_D32p340 = 0;
 static double B72PP2A_pARPP210 = 0;
 static double B72PP2A_D32p750 = 0;
 static double B72PP2A_D32p340 = 0;
 static double B72PP2A0 = 0;
 static double B56PP2Ap_pARPP210 = 0;
 static double B56PP2Ap_D32p750 = 0;
 static double B56PP2Ap0 = 0;
 static double B56PP2A_pARPP210 = 0;
 static double B56PP2A_D32p750 = 0;
 static double B56PP2A0 = 0;
 static double CaMKII_CaM_Ca4_psd_Substrate0 = 0;
 static double CaMKII_CaM_Ca2_psd_Substrate0 = 0;
 static double CaMKII_CaM_psd_Substrate0 = 0;
 static double CaMKII_CaM_Ca4_CaMKII_CaM_Ca40 = 0;
 static double CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd0 = 0;
 static double CDK5_D320 = 0;
 static double CDK50 = 0;
 static double CaMKII_psd0 = 0;
 static double CaMKII_CaM_Ca4_psd0 = 0;
 static double CaMKII_CaM_psd0 = 0;
 static double CaMKII_CaM_Ca2_psd0 = 0;
 static double CaMKII_CaM_Ca20 = 0;
 static double CaMKII_CaM0 = 0;
 static double CaMKII_CaM_Ca40 = 0;
 static double CaMKII0 = 0;
 static double CaM_Ca4_pARPP210 = 0;
 static double CaM_Ca40 = 0;
 static double CaM_Ca20 = 0;
 static double CaM0 = 0;
 static double D320 = 0;
 static double D32p750 = 0;
 static double D32p340 = 0;
 static double D1R_Golf0 = 0;
 static double D1R_Golf_DA0 = 0;
 static double D1R_DA0 = 0;
 static double D1R0 = 0;
 static double Golf0 = 0;
 static double Gbgolf0 = 0;
 static double GaolfGTP0 = 0;
 static double GaolfGDP0 = 0;
 static double PP2B_CaM_Ca20 = 0;
 static double PP2B_CaM0 = 0;
 static double PP2Bc_D32p340 = 0;
 static double PP2Bc0 = 0;
 static double PP2B0 = 0;
 static double PP1_D32p340 = 0;
 static double PP1_pSubstrate0 = 0;
 static double PP1_pCaMKII_psd0 = 0;
 static double PP10 = 0;
 static double PKAreg0 = 0;
 static double PKAc_D32p750 = 0;
 static double PKA_Ca4MP0 = 0;
 static double PKA_Ca2MP0 = 0;
 static double PKAc_ARPP210 = 0;
 static double PKAc_D320 = 0;
 static double PKAc_B56PP2A0 = 0;
 static double PKAc0 = 0;
 static double PKA0 = 0;
 static double PDE10c_cAMP0 = 0;
 static double PDE10c0 = 0;
 static double PDE10r_cAMP0 = 0;
 static double PDE10r0 = 0;
 static double PDE4_cAMP0 = 0;
 static double PDE40 = 0;
 static double Substrate0 = 0;
 static double cAMP0 = 0;
 static double delta_t = 0.01;
 static double pCaMKII_CaM_Ca4_psd_Substrate0 = 0;
 static double pCaMKII_CaM_Ca2_psd_Substrate0 = 0;
 static double pCaMKII_CaM_psd_Substrate0 = 0;
 static double pCaMKII_psd_Substrate0 = 0;
 static double pARPP210 = 0;
 static double pCaMKII_CaM_Ca4_CaMKII_CaM_Ca40 = 0;
 static double pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd0 = 0;
 static double pSubstrate0 = 0;
 static double pCaMKII_psd0 = 0;
 static double pCaMKII_CaM_Ca4_psd0 = 0;
 static double pCaMKII_CaM_psd0 = 0;
 static double pCaMKII_CaM_Ca2_psd0 = 0;
 static double pCaMKII_CaM_Ca20 = 0;
 static double pCaMKII_CaM0 = 0;
 static double pCaMKII_CaM_Ca40 = 0;
 static double pCaMKII0 = 0;
 static double total_CaMKII_activated0 = 0;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 "kf_R0_D1_LTP_time_window_Luca_cai_initials", &kf_R0_D1_LTP_time_window_Luca_cai_initials,
 "kf_R1_D1_LTP_time_window_Luca_cai_initials", &kf_R1_D1_LTP_time_window_Luca_cai_initials,
 "kf_R2_D1_LTP_time_window_Luca_cai_initials", &kf_R2_D1_LTP_time_window_Luca_cai_initials,
 "kr_R2_D1_LTP_time_window_Luca_cai_initials", &kr_R2_D1_LTP_time_window_Luca_cai_initials,
 "kf_R3_D1_LTP_time_window_Luca_cai_initials", &kf_R3_D1_LTP_time_window_Luca_cai_initials,
 "kr_R3_D1_LTP_time_window_Luca_cai_initials", &kr_R3_D1_LTP_time_window_Luca_cai_initials,
 "kf_R4_D1_LTP_time_window_Luca_cai_initials", &kf_R4_D1_LTP_time_window_Luca_cai_initials,
 "kr_R4_D1_LTP_time_window_Luca_cai_initials", &kr_R4_D1_LTP_time_window_Luca_cai_initials,
 "kf_R5_D1_LTP_time_window_Luca_cai_initials", &kf_R5_D1_LTP_time_window_Luca_cai_initials,
 "kr_R5_D1_LTP_time_window_Luca_cai_initials", &kr_R5_D1_LTP_time_window_Luca_cai_initials,
 "kf_R6_D1_LTP_time_window_Luca_cai_initials", &kf_R6_D1_LTP_time_window_Luca_cai_initials,
 "kr_R6_D1_LTP_time_window_Luca_cai_initials", &kr_R6_D1_LTP_time_window_Luca_cai_initials,
 "kf_R7_D1_LTP_time_window_Luca_cai_initials", &kf_R7_D1_LTP_time_window_Luca_cai_initials,
 "kr_R7_D1_LTP_time_window_Luca_cai_initials", &kr_R7_D1_LTP_time_window_Luca_cai_initials,
 "kf_R8_D1_LTP_time_window_Luca_cai_initials", &kf_R8_D1_LTP_time_window_Luca_cai_initials,
 "kr_R8_D1_LTP_time_window_Luca_cai_initials", &kr_R8_D1_LTP_time_window_Luca_cai_initials,
 "kf_R9_D1_LTP_time_window_Luca_cai_initials", &kf_R9_D1_LTP_time_window_Luca_cai_initials,
 "kf_R10_D1_LTP_time_window_Luca_cai_initials", &kf_R10_D1_LTP_time_window_Luca_cai_initials,
 "kr_R10_D1_LTP_time_window_Luca_cai_initials", &kr_R10_D1_LTP_time_window_Luca_cai_initials,
 "kf_R11_D1_LTP_time_window_Luca_cai_initials", &kf_R11_D1_LTP_time_window_Luca_cai_initials,
 "kf_R12_D1_LTP_time_window_Luca_cai_initials", &kf_R12_D1_LTP_time_window_Luca_cai_initials,
 "kr_R12_D1_LTP_time_window_Luca_cai_initials", &kr_R12_D1_LTP_time_window_Luca_cai_initials,
 "kf_R13_D1_LTP_time_window_Luca_cai_initials", &kf_R13_D1_LTP_time_window_Luca_cai_initials,
 "kr_R13_D1_LTP_time_window_Luca_cai_initials", &kr_R13_D1_LTP_time_window_Luca_cai_initials,
 "kf_R14_D1_LTP_time_window_Luca_cai_initials", &kf_R14_D1_LTP_time_window_Luca_cai_initials,
 "kf_R15_D1_LTP_time_window_Luca_cai_initials", &kf_R15_D1_LTP_time_window_Luca_cai_initials,
 "kr_R15_D1_LTP_time_window_Luca_cai_initials", &kr_R15_D1_LTP_time_window_Luca_cai_initials,
 "kf_R16_D1_LTP_time_window_Luca_cai_initials", &kf_R16_D1_LTP_time_window_Luca_cai_initials,
 "kr_R16_D1_LTP_time_window_Luca_cai_initials", &kr_R16_D1_LTP_time_window_Luca_cai_initials,
 "kf_R17_D1_LTP_time_window_Luca_cai_initials", &kf_R17_D1_LTP_time_window_Luca_cai_initials,
 "kr_R17_D1_LTP_time_window_Luca_cai_initials", &kr_R17_D1_LTP_time_window_Luca_cai_initials,
 "kf_R18_D1_LTP_time_window_Luca_cai_initials", &kf_R18_D1_LTP_time_window_Luca_cai_initials,
 "kr_R18_D1_LTP_time_window_Luca_cai_initials", &kr_R18_D1_LTP_time_window_Luca_cai_initials,
 "kf_R19_D1_LTP_time_window_Luca_cai_initials", &kf_R19_D1_LTP_time_window_Luca_cai_initials,
 "kr_R19_D1_LTP_time_window_Luca_cai_initials", &kr_R19_D1_LTP_time_window_Luca_cai_initials,
 "kf_R20_D1_LTP_time_window_Luca_cai_initials", &kf_R20_D1_LTP_time_window_Luca_cai_initials,
 "kf_R21_D1_LTP_time_window_Luca_cai_initials", &kf_R21_D1_LTP_time_window_Luca_cai_initials,
 "kf_R22_D1_LTP_time_window_Luca_cai_initials", &kf_R22_D1_LTP_time_window_Luca_cai_initials,
 "kf_R23_D1_LTP_time_window_Luca_cai_initials", &kf_R23_D1_LTP_time_window_Luca_cai_initials,
 "kr_R23_D1_LTP_time_window_Luca_cai_initials", &kr_R23_D1_LTP_time_window_Luca_cai_initials,
 "kf_R24_D1_LTP_time_window_Luca_cai_initials", &kf_R24_D1_LTP_time_window_Luca_cai_initials,
 "kr_R24_D1_LTP_time_window_Luca_cai_initials", &kr_R24_D1_LTP_time_window_Luca_cai_initials,
 "kf_R25_D1_LTP_time_window_Luca_cai_initials", &kf_R25_D1_LTP_time_window_Luca_cai_initials,
 "kr_R25_D1_LTP_time_window_Luca_cai_initials", &kr_R25_D1_LTP_time_window_Luca_cai_initials,
 "kf_R26_D1_LTP_time_window_Luca_cai_initials", &kf_R26_D1_LTP_time_window_Luca_cai_initials,
 "kr_R26_D1_LTP_time_window_Luca_cai_initials", &kr_R26_D1_LTP_time_window_Luca_cai_initials,
 "kf_R27_D1_LTP_time_window_Luca_cai_initials", &kf_R27_D1_LTP_time_window_Luca_cai_initials,
 "kr_R27_D1_LTP_time_window_Luca_cai_initials", &kr_R27_D1_LTP_time_window_Luca_cai_initials,
 "kf_R28_D1_LTP_time_window_Luca_cai_initials", &kf_R28_D1_LTP_time_window_Luca_cai_initials,
 "kr_R28_D1_LTP_time_window_Luca_cai_initials", &kr_R28_D1_LTP_time_window_Luca_cai_initials,
 "kf_R29_D1_LTP_time_window_Luca_cai_initials", &kf_R29_D1_LTP_time_window_Luca_cai_initials,
 "kr_R29_D1_LTP_time_window_Luca_cai_initials", &kr_R29_D1_LTP_time_window_Luca_cai_initials,
 "kf_R30_D1_LTP_time_window_Luca_cai_initials", &kf_R30_D1_LTP_time_window_Luca_cai_initials,
 "kr_R30_D1_LTP_time_window_Luca_cai_initials", &kr_R30_D1_LTP_time_window_Luca_cai_initials,
 "kf_R31_D1_LTP_time_window_Luca_cai_initials", &kf_R31_D1_LTP_time_window_Luca_cai_initials,
 "kf_R32_D1_LTP_time_window_Luca_cai_initials", &kf_R32_D1_LTP_time_window_Luca_cai_initials,
 "kf_R33_D1_LTP_time_window_Luca_cai_initials", &kf_R33_D1_LTP_time_window_Luca_cai_initials,
 "kf_R34_D1_LTP_time_window_Luca_cai_initials", &kf_R34_D1_LTP_time_window_Luca_cai_initials,
 "kr_R34_D1_LTP_time_window_Luca_cai_initials", &kr_R34_D1_LTP_time_window_Luca_cai_initials,
 "kf_R35_D1_LTP_time_window_Luca_cai_initials", &kf_R35_D1_LTP_time_window_Luca_cai_initials,
 "kr_R35_D1_LTP_time_window_Luca_cai_initials", &kr_R35_D1_LTP_time_window_Luca_cai_initials,
 "kf_R36_D1_LTP_time_window_Luca_cai_initials", &kf_R36_D1_LTP_time_window_Luca_cai_initials,
 "kf_R37_D1_LTP_time_window_Luca_cai_initials", &kf_R37_D1_LTP_time_window_Luca_cai_initials,
 "kf_R38_D1_LTP_time_window_Luca_cai_initials", &kf_R38_D1_LTP_time_window_Luca_cai_initials,
 "kr_R38_D1_LTP_time_window_Luca_cai_initials", &kr_R38_D1_LTP_time_window_Luca_cai_initials,
 "kf_R39_D1_LTP_time_window_Luca_cai_initials", &kf_R39_D1_LTP_time_window_Luca_cai_initials,
 "kr_R39_D1_LTP_time_window_Luca_cai_initials", &kr_R39_D1_LTP_time_window_Luca_cai_initials,
 "kf_R40_D1_LTP_time_window_Luca_cai_initials", &kf_R40_D1_LTP_time_window_Luca_cai_initials,
 "kr_R40_D1_LTP_time_window_Luca_cai_initials", &kr_R40_D1_LTP_time_window_Luca_cai_initials,
 "kf_R41_D1_LTP_time_window_Luca_cai_initials", &kf_R41_D1_LTP_time_window_Luca_cai_initials,
 "kr_R41_D1_LTP_time_window_Luca_cai_initials", &kr_R41_D1_LTP_time_window_Luca_cai_initials,
 "kf_R42_D1_LTP_time_window_Luca_cai_initials", &kf_R42_D1_LTP_time_window_Luca_cai_initials,
 "kf_R43_D1_LTP_time_window_Luca_cai_initials", &kf_R43_D1_LTP_time_window_Luca_cai_initials,
 "kr_R43_D1_LTP_time_window_Luca_cai_initials", &kr_R43_D1_LTP_time_window_Luca_cai_initials,
 "kf_R44_D1_LTP_time_window_Luca_cai_initials", &kf_R44_D1_LTP_time_window_Luca_cai_initials,
 "kf_R45_D1_LTP_time_window_Luca_cai_initials", &kf_R45_D1_LTP_time_window_Luca_cai_initials,
 "kr_R45_D1_LTP_time_window_Luca_cai_initials", &kr_R45_D1_LTP_time_window_Luca_cai_initials,
 "kf_R46_D1_LTP_time_window_Luca_cai_initials", &kf_R46_D1_LTP_time_window_Luca_cai_initials,
 "kf_R47_D1_LTP_time_window_Luca_cai_initials", &kf_R47_D1_LTP_time_window_Luca_cai_initials,
 "kf_R48_D1_LTP_time_window_Luca_cai_initials", &kf_R48_D1_LTP_time_window_Luca_cai_initials,
 "kr_R48_D1_LTP_time_window_Luca_cai_initials", &kr_R48_D1_LTP_time_window_Luca_cai_initials,
 "kf_R49_D1_LTP_time_window_Luca_cai_initials", &kf_R49_D1_LTP_time_window_Luca_cai_initials,
 "kr_R49_D1_LTP_time_window_Luca_cai_initials", &kr_R49_D1_LTP_time_window_Luca_cai_initials,
 "kf_R50_D1_LTP_time_window_Luca_cai_initials", &kf_R50_D1_LTP_time_window_Luca_cai_initials,
 "kr_R50_D1_LTP_time_window_Luca_cai_initials", &kr_R50_D1_LTP_time_window_Luca_cai_initials,
 "kf_R51_D1_LTP_time_window_Luca_cai_initials", &kf_R51_D1_LTP_time_window_Luca_cai_initials,
 "kr_R51_D1_LTP_time_window_Luca_cai_initials", &kr_R51_D1_LTP_time_window_Luca_cai_initials,
 "kf_R52_D1_LTP_time_window_Luca_cai_initials", &kf_R52_D1_LTP_time_window_Luca_cai_initials,
 "kr_R52_D1_LTP_time_window_Luca_cai_initials", &kr_R52_D1_LTP_time_window_Luca_cai_initials,
 "kf_R53_D1_LTP_time_window_Luca_cai_initials", &kf_R53_D1_LTP_time_window_Luca_cai_initials,
 "kr_R53_D1_LTP_time_window_Luca_cai_initials", &kr_R53_D1_LTP_time_window_Luca_cai_initials,
 "kf_R54_D1_LTP_time_window_Luca_cai_initials", &kf_R54_D1_LTP_time_window_Luca_cai_initials,
 "kr_R54_D1_LTP_time_window_Luca_cai_initials", &kr_R54_D1_LTP_time_window_Luca_cai_initials,
 "kf_R55_D1_LTP_time_window_Luca_cai_initials", &kf_R55_D1_LTP_time_window_Luca_cai_initials,
 "kf_R56_D1_LTP_time_window_Luca_cai_initials", &kf_R56_D1_LTP_time_window_Luca_cai_initials,
 "kf_R57_D1_LTP_time_window_Luca_cai_initials", &kf_R57_D1_LTP_time_window_Luca_cai_initials,
 "kf_R58_D1_LTP_time_window_Luca_cai_initials", &kf_R58_D1_LTP_time_window_Luca_cai_initials,
 "kf_R59_D1_LTP_time_window_Luca_cai_initials", &kf_R59_D1_LTP_time_window_Luca_cai_initials,
 "kf_R60_D1_LTP_time_window_Luca_cai_initials", &kf_R60_D1_LTP_time_window_Luca_cai_initials,
 "kf_R61_D1_LTP_time_window_Luca_cai_initials", &kf_R61_D1_LTP_time_window_Luca_cai_initials,
 "kf_R62_D1_LTP_time_window_Luca_cai_initials", &kf_R62_D1_LTP_time_window_Luca_cai_initials,
 "kf_R63_D1_LTP_time_window_Luca_cai_initials", &kf_R63_D1_LTP_time_window_Luca_cai_initials,
 "kf_R64_D1_LTP_time_window_Luca_cai_initials", &kf_R64_D1_LTP_time_window_Luca_cai_initials,
 "kf_R65_D1_LTP_time_window_Luca_cai_initials", &kf_R65_D1_LTP_time_window_Luca_cai_initials,
 "kf_R66_D1_LTP_time_window_Luca_cai_initials", &kf_R66_D1_LTP_time_window_Luca_cai_initials,
 "kf_R67_D1_LTP_time_window_Luca_cai_initials", &kf_R67_D1_LTP_time_window_Luca_cai_initials,
 "kr_R67_D1_LTP_time_window_Luca_cai_initials", &kr_R67_D1_LTP_time_window_Luca_cai_initials,
 "kf_R68_D1_LTP_time_window_Luca_cai_initials", &kf_R68_D1_LTP_time_window_Luca_cai_initials,
 "kr_R68_D1_LTP_time_window_Luca_cai_initials", &kr_R68_D1_LTP_time_window_Luca_cai_initials,
 "kf_R69_D1_LTP_time_window_Luca_cai_initials", &kf_R69_D1_LTP_time_window_Luca_cai_initials,
 "kr_R69_D1_LTP_time_window_Luca_cai_initials", &kr_R69_D1_LTP_time_window_Luca_cai_initials,
 "kf_R70_D1_LTP_time_window_Luca_cai_initials", &kf_R70_D1_LTP_time_window_Luca_cai_initials,
 "kr_R70_D1_LTP_time_window_Luca_cai_initials", &kr_R70_D1_LTP_time_window_Luca_cai_initials,
 "kf_R71_D1_LTP_time_window_Luca_cai_initials", &kf_R71_D1_LTP_time_window_Luca_cai_initials,
 "kr_R71_D1_LTP_time_window_Luca_cai_initials", &kr_R71_D1_LTP_time_window_Luca_cai_initials,
 "kf_R72_D1_LTP_time_window_Luca_cai_initials", &kf_R72_D1_LTP_time_window_Luca_cai_initials,
 "kr_R72_D1_LTP_time_window_Luca_cai_initials", &kr_R72_D1_LTP_time_window_Luca_cai_initials,
 "kf_R73_D1_LTP_time_window_Luca_cai_initials", &kf_R73_D1_LTP_time_window_Luca_cai_initials,
 "kr_R73_D1_LTP_time_window_Luca_cai_initials", &kr_R73_D1_LTP_time_window_Luca_cai_initials,
 "kf_R74_D1_LTP_time_window_Luca_cai_initials", &kf_R74_D1_LTP_time_window_Luca_cai_initials,
 "kr_R74_D1_LTP_time_window_Luca_cai_initials", &kr_R74_D1_LTP_time_window_Luca_cai_initials,
 "kf_R75_D1_LTP_time_window_Luca_cai_initials", &kf_R75_D1_LTP_time_window_Luca_cai_initials,
 "kr_R75_D1_LTP_time_window_Luca_cai_initials", &kr_R75_D1_LTP_time_window_Luca_cai_initials,
 "kf_R76_D1_LTP_time_window_Luca_cai_initials", &kf_R76_D1_LTP_time_window_Luca_cai_initials,
 "kr_R76_D1_LTP_time_window_Luca_cai_initials", &kr_R76_D1_LTP_time_window_Luca_cai_initials,
 "kf_R77_D1_LTP_time_window_Luca_cai_initials", &kf_R77_D1_LTP_time_window_Luca_cai_initials,
 "kr_R77_D1_LTP_time_window_Luca_cai_initials", &kr_R77_D1_LTP_time_window_Luca_cai_initials,
 "kf_R78_D1_LTP_time_window_Luca_cai_initials", &kf_R78_D1_LTP_time_window_Luca_cai_initials,
 "kr_R78_D1_LTP_time_window_Luca_cai_initials", &kr_R78_D1_LTP_time_window_Luca_cai_initials,
 "kf_R79_D1_LTP_time_window_Luca_cai_initials", &kf_R79_D1_LTP_time_window_Luca_cai_initials,
 "kr_R79_D1_LTP_time_window_Luca_cai_initials", &kr_R79_D1_LTP_time_window_Luca_cai_initials,
 "kf_R80_D1_LTP_time_window_Luca_cai_initials", &kf_R80_D1_LTP_time_window_Luca_cai_initials,
 "kr_R80_D1_LTP_time_window_Luca_cai_initials", &kr_R80_D1_LTP_time_window_Luca_cai_initials,
 "kf_R81_D1_LTP_time_window_Luca_cai_initials", &kf_R81_D1_LTP_time_window_Luca_cai_initials,
 "kf_R82_D1_LTP_time_window_Luca_cai_initials", &kf_R82_D1_LTP_time_window_Luca_cai_initials,
 "kr_R82_D1_LTP_time_window_Luca_cai_initials", &kr_R82_D1_LTP_time_window_Luca_cai_initials,
 "kf_R83_D1_LTP_time_window_Luca_cai_initials", &kf_R83_D1_LTP_time_window_Luca_cai_initials,
 "kf_R84_D1_LTP_time_window_Luca_cai_initials", &kf_R84_D1_LTP_time_window_Luca_cai_initials,
 "kr_R84_D1_LTP_time_window_Luca_cai_initials", &kr_R84_D1_LTP_time_window_Luca_cai_initials,
 "kf_R85_D1_LTP_time_window_Luca_cai_initials", &kf_R85_D1_LTP_time_window_Luca_cai_initials,
 "kf_R86_D1_LTP_time_window_Luca_cai_initials", &kf_R86_D1_LTP_time_window_Luca_cai_initials,
 "kr_R86_D1_LTP_time_window_Luca_cai_initials", &kr_R86_D1_LTP_time_window_Luca_cai_initials,
 "kf_R87_D1_LTP_time_window_Luca_cai_initials", &kf_R87_D1_LTP_time_window_Luca_cai_initials,
 "kf_R88_D1_LTP_time_window_Luca_cai_initials", &kf_R88_D1_LTP_time_window_Luca_cai_initials,
 "kr_R88_D1_LTP_time_window_Luca_cai_initials", &kr_R88_D1_LTP_time_window_Luca_cai_initials,
 "kf_R89_D1_LTP_time_window_Luca_cai_initials", &kf_R89_D1_LTP_time_window_Luca_cai_initials,
 "kf_R90_D1_LTP_time_window_Luca_cai_initials", &kf_R90_D1_LTP_time_window_Luca_cai_initials,
 "kr_R90_D1_LTP_time_window_Luca_cai_initials", &kr_R90_D1_LTP_time_window_Luca_cai_initials,
 "kf_R91_D1_LTP_time_window_Luca_cai_initials", &kf_R91_D1_LTP_time_window_Luca_cai_initials,
 "kr_R91_D1_LTP_time_window_Luca_cai_initials", &kr_R91_D1_LTP_time_window_Luca_cai_initials,
 "kf_R92_D1_LTP_time_window_Luca_cai_initials", &kf_R92_D1_LTP_time_window_Luca_cai_initials,
 "kf_R93_D1_LTP_time_window_Luca_cai_initials", &kf_R93_D1_LTP_time_window_Luca_cai_initials,
 "kr_R93_D1_LTP_time_window_Luca_cai_initials", &kr_R93_D1_LTP_time_window_Luca_cai_initials,
 "kf_R94_D1_LTP_time_window_Luca_cai_initials", &kf_R94_D1_LTP_time_window_Luca_cai_initials,
 "kf_R95_D1_LTP_time_window_Luca_cai_initials", &kf_R95_D1_LTP_time_window_Luca_cai_initials,
 "kf_R96_D1_LTP_time_window_Luca_cai_initials", &kf_R96_D1_LTP_time_window_Luca_cai_initials,
 "kr_R96_D1_LTP_time_window_Luca_cai_initials", &kr_R96_D1_LTP_time_window_Luca_cai_initials,
 "kf_R97_D1_LTP_time_window_Luca_cai_initials", &kf_R97_D1_LTP_time_window_Luca_cai_initials,
 "kf_R98_D1_LTP_time_window_Luca_cai_initials", &kf_R98_D1_LTP_time_window_Luca_cai_initials,
 "kr_R98_D1_LTP_time_window_Luca_cai_initials", &kr_R98_D1_LTP_time_window_Luca_cai_initials,
 "kf_R99_D1_LTP_time_window_Luca_cai_initials", &kf_R99_D1_LTP_time_window_Luca_cai_initials,
 "kf_R100_D1_LTP_time_window_Luca_cai_initials", &kf_R100_D1_LTP_time_window_Luca_cai_initials,
 "kr_R100_D1_LTP_time_window_Luca_cai_initials", &kr_R100_D1_LTP_time_window_Luca_cai_initials,
 "kf_R101_D1_LTP_time_window_Luca_cai_initials", &kf_R101_D1_LTP_time_window_Luca_cai_initials,
 "kf_R102_D1_LTP_time_window_Luca_cai_initials", &kf_R102_D1_LTP_time_window_Luca_cai_initials,
 "kr_R102_D1_LTP_time_window_Luca_cai_initials", &kr_R102_D1_LTP_time_window_Luca_cai_initials,
 "kf_R103_D1_LTP_time_window_Luca_cai_initials", &kf_R103_D1_LTP_time_window_Luca_cai_initials,
 "kf_R104_D1_LTP_time_window_Luca_cai_initials", &kf_R104_D1_LTP_time_window_Luca_cai_initials,
 "kr_R104_D1_LTP_time_window_Luca_cai_initials", &kr_R104_D1_LTP_time_window_Luca_cai_initials,
 "kf_R105_D1_LTP_time_window_Luca_cai_initials", &kf_R105_D1_LTP_time_window_Luca_cai_initials,
 "kf_R106_D1_LTP_time_window_Luca_cai_initials", &kf_R106_D1_LTP_time_window_Luca_cai_initials,
 "kr_R106_D1_LTP_time_window_Luca_cai_initials", &kr_R106_D1_LTP_time_window_Luca_cai_initials,
 "kf_R107_D1_LTP_time_window_Luca_cai_initials", &kf_R107_D1_LTP_time_window_Luca_cai_initials,
 "kf_R108_D1_LTP_time_window_Luca_cai_initials", &kf_R108_D1_LTP_time_window_Luca_cai_initials,
 "kr_R108_D1_LTP_time_window_Luca_cai_initials", &kr_R108_D1_LTP_time_window_Luca_cai_initials,
 "kf_R109_D1_LTP_time_window_Luca_cai_initials", &kf_R109_D1_LTP_time_window_Luca_cai_initials,
 "kr_R109_D1_LTP_time_window_Luca_cai_initials", &kr_R109_D1_LTP_time_window_Luca_cai_initials,
 "kf_R110_D1_LTP_time_window_Luca_cai_initials", &kf_R110_D1_LTP_time_window_Luca_cai_initials,
 "kr_R110_D1_LTP_time_window_Luca_cai_initials", &kr_R110_D1_LTP_time_window_Luca_cai_initials,
 "kf_R111_D1_LTP_time_window_Luca_cai_initials", &kf_R111_D1_LTP_time_window_Luca_cai_initials,
 "kr_R111_D1_LTP_time_window_Luca_cai_initials", &kr_R111_D1_LTP_time_window_Luca_cai_initials,
 "kf_R112_D1_LTP_time_window_Luca_cai_initials", &kf_R112_D1_LTP_time_window_Luca_cai_initials,
 "kr_R112_D1_LTP_time_window_Luca_cai_initials", &kr_R112_D1_LTP_time_window_Luca_cai_initials,
 "kf_R113_D1_LTP_time_window_Luca_cai_initials", &kf_R113_D1_LTP_time_window_Luca_cai_initials,
 "kr_R113_D1_LTP_time_window_Luca_cai_initials", &kr_R113_D1_LTP_time_window_Luca_cai_initials,
 "kf_R114_D1_LTP_time_window_Luca_cai_initials", &kf_R114_D1_LTP_time_window_Luca_cai_initials,
 "kr_R114_D1_LTP_time_window_Luca_cai_initials", &kr_R114_D1_LTP_time_window_Luca_cai_initials,
 "kf_R115_D1_LTP_time_window_Luca_cai_initials", &kf_R115_D1_LTP_time_window_Luca_cai_initials,
 "kr_R115_D1_LTP_time_window_Luca_cai_initials", &kr_R115_D1_LTP_time_window_Luca_cai_initials,
 "kf_R116_D1_LTP_time_window_Luca_cai_initials", &kf_R116_D1_LTP_time_window_Luca_cai_initials,
 "kr_R116_D1_LTP_time_window_Luca_cai_initials", &kr_R116_D1_LTP_time_window_Luca_cai_initials,
 "kf_R117_D1_LTP_time_window_Luca_cai_initials", &kf_R117_D1_LTP_time_window_Luca_cai_initials,
 "kr_R117_D1_LTP_time_window_Luca_cai_initials", &kr_R117_D1_LTP_time_window_Luca_cai_initials,
 "kf_R118_D1_LTP_time_window_Luca_cai_initials", &kf_R118_D1_LTP_time_window_Luca_cai_initials,
 "kf_R119_D1_LTP_time_window_Luca_cai_initials", &kf_R119_D1_LTP_time_window_Luca_cai_initials,
 "kf_R120_D1_LTP_time_window_Luca_cai_initials", &kf_R120_D1_LTP_time_window_Luca_cai_initials,
 "kr_R120_D1_LTP_time_window_Luca_cai_initials", &kr_R120_D1_LTP_time_window_Luca_cai_initials,
 "kf_R121_D1_LTP_time_window_Luca_cai_initials", &kf_R121_D1_LTP_time_window_Luca_cai_initials,
 "kr_R121_D1_LTP_time_window_Luca_cai_initials", &kr_R121_D1_LTP_time_window_Luca_cai_initials,
 "kf_R122_D1_LTP_time_window_Luca_cai_initials", &kf_R122_D1_LTP_time_window_Luca_cai_initials,
 "kr_R122_D1_LTP_time_window_Luca_cai_initials", &kr_R122_D1_LTP_time_window_Luca_cai_initials,
 "kf_R123_D1_LTP_time_window_Luca_cai_initials", &kf_R123_D1_LTP_time_window_Luca_cai_initials,
 "kr_R123_D1_LTP_time_window_Luca_cai_initials", &kr_R123_D1_LTP_time_window_Luca_cai_initials,
 "kf_R124_D1_LTP_time_window_Luca_cai_initials", &kf_R124_D1_LTP_time_window_Luca_cai_initials,
 "kr_R124_D1_LTP_time_window_Luca_cai_initials", &kr_R124_D1_LTP_time_window_Luca_cai_initials,
 "kf_R125_D1_LTP_time_window_Luca_cai_initials", &kf_R125_D1_LTP_time_window_Luca_cai_initials,
 "kr_R125_D1_LTP_time_window_Luca_cai_initials", &kr_R125_D1_LTP_time_window_Luca_cai_initials,
 "kf_R126_D1_LTP_time_window_Luca_cai_initials", &kf_R126_D1_LTP_time_window_Luca_cai_initials,
 "kr_R126_D1_LTP_time_window_Luca_cai_initials", &kr_R126_D1_LTP_time_window_Luca_cai_initials,
 "kf_R127_D1_LTP_time_window_Luca_cai_initials", &kf_R127_D1_LTP_time_window_Luca_cai_initials,
 "kr_R127_D1_LTP_time_window_Luca_cai_initials", &kr_R127_D1_LTP_time_window_Luca_cai_initials,
 "kf_R128_D1_LTP_time_window_Luca_cai_initials", &kf_R128_D1_LTP_time_window_Luca_cai_initials,
 "kr_R128_D1_LTP_time_window_Luca_cai_initials", &kr_R128_D1_LTP_time_window_Luca_cai_initials,
 "kf_R129_D1_LTP_time_window_Luca_cai_initials", &kf_R129_D1_LTP_time_window_Luca_cai_initials,
 "kr_R129_D1_LTP_time_window_Luca_cai_initials", &kr_R129_D1_LTP_time_window_Luca_cai_initials,
 "kf_R130_D1_LTP_time_window_Luca_cai_initials", &kf_R130_D1_LTP_time_window_Luca_cai_initials,
 "kr_R130_D1_LTP_time_window_Luca_cai_initials", &kr_R130_D1_LTP_time_window_Luca_cai_initials,
 "kf_R131_D1_LTP_time_window_Luca_cai_initials", &kf_R131_D1_LTP_time_window_Luca_cai_initials,
 "kf_R132_D1_LTP_time_window_Luca_cai_initials", &kf_R132_D1_LTP_time_window_Luca_cai_initials,
 "kr_R132_D1_LTP_time_window_Luca_cai_initials", &kr_R132_D1_LTP_time_window_Luca_cai_initials,
 "kf_R133_D1_LTP_time_window_Luca_cai_initials", &kf_R133_D1_LTP_time_window_Luca_cai_initials,
 "kf_R134_D1_LTP_time_window_Luca_cai_initials", &kf_R134_D1_LTP_time_window_Luca_cai_initials,
 "kr_R134_D1_LTP_time_window_Luca_cai_initials", &kr_R134_D1_LTP_time_window_Luca_cai_initials,
 "kf_R135_D1_LTP_time_window_Luca_cai_initials", &kf_R135_D1_LTP_time_window_Luca_cai_initials,
 "kf_R136_D1_LTP_time_window_Luca_cai_initials", &kf_R136_D1_LTP_time_window_Luca_cai_initials,
 "kr_R136_D1_LTP_time_window_Luca_cai_initials", &kr_R136_D1_LTP_time_window_Luca_cai_initials,
 "kf_R137_D1_LTP_time_window_Luca_cai_initials", &kf_R137_D1_LTP_time_window_Luca_cai_initials,
 0,0
};
 static DoubVec hoc_vdoub[] = {
 0,0,0
};
 static double _sav_indep;
 static void nrn_alloc(Prop*);
static void  nrn_init(_NrnThread*, _Memb_list*, int);
static void nrn_state(_NrnThread*, _Memb_list*, int);
 static void nrn_cur(_NrnThread*, _Memb_list*, int);
static void  nrn_jacob(_NrnThread*, _Memb_list*, int);
 
static int _ode_count(int);
static void _ode_map(int, double**, double**, double*, Datum*, double*, int);
static void _ode_spec(_NrnThread*, _Memb_list*, int);
static void _ode_matsol(_NrnThread*, _Memb_list*, int);
 
#define _cvode_ieq _ppvar[1]._i
 static void _ode_matsol_instance1(_threadargsproto_);
 /* connect range variables in _p that hoc is supposed to know about */
 static const char *_mechanism[] = {
 "7.7.0",
"D1_LTP_time_window_Luca_cai_initials",
 "DA_start_D1_LTP_time_window_Luca_cai_initials",
 "DA_max_D1_LTP_time_window_Luca_cai_initials",
 0,
 "ATP_expression_D1_LTP_time_window_Luca_cai_initials",
 "Ca_expression_D1_LTP_time_window_Luca_cai_initials",
 "DA_expression_D1_LTP_time_window_Luca_cai_initials",
 "AMP_D1_LTP_time_window_Luca_cai_initials",
 "ATP_D1_LTP_time_window_Luca_cai_initials",
 "Ca_D1_LTP_time_window_Luca_cai_initials",
 "DA_D1_LTP_time_window_Luca_cai_initials",
 "pSubstrate_out_D1_LTP_time_window_Luca_cai_initials",
 "PP1_out_D1_LTP_time_window_Luca_cai_initials",
 "CaM_out_D1_LTP_time_window_Luca_cai_initials",
 "D32_out_D1_LTP_time_window_Luca_cai_initials",
 "total_CaMKII_activated_out_D1_LTP_time_window_Luca_cai_initials",
 0,
 "AC5_D1_LTP_time_window_Luca_cai_initials",
 "AC5_ATP_D1_LTP_time_window_Luca_cai_initials",
 "AC5_Ca_D1_LTP_time_window_Luca_cai_initials",
 "AC5_Ca_ATP_D1_LTP_time_window_Luca_cai_initials",
 "AC5_Ca_GaolfGTP_D1_LTP_time_window_Luca_cai_initials",
 "AC5_Ca_GaolfGTP_ATP_D1_LTP_time_window_Luca_cai_initials",
 "AC5_GaolfGTP_D1_LTP_time_window_Luca_cai_initials",
 "AC5_GaolfGTP_ATP_D1_LTP_time_window_Luca_cai_initials",
 "B56PP2A_D1_LTP_time_window_Luca_cai_initials",
 "B56PP2A_D32p75_D1_LTP_time_window_Luca_cai_initials",
 "B56PP2A_pARPP21_D1_LTP_time_window_Luca_cai_initials",
 "B56PP2Ap_D1_LTP_time_window_Luca_cai_initials",
 "B56PP2Ap_D32p75_D1_LTP_time_window_Luca_cai_initials",
 "B56PP2Ap_pARPP21_D1_LTP_time_window_Luca_cai_initials",
 "B72PP2A_D1_LTP_time_window_Luca_cai_initials",
 "B72PP2A_D32p34_D1_LTP_time_window_Luca_cai_initials",
 "B72PP2A_D32p75_D1_LTP_time_window_Luca_cai_initials",
 "B72PP2A_pARPP21_D1_LTP_time_window_Luca_cai_initials",
 "B72PP2A_Ca_D32p34_D1_LTP_time_window_Luca_cai_initials",
 "B72PP2A_Ca_D32p75_D1_LTP_time_window_Luca_cai_initials",
 "B72PP2A_Ca_D1_LTP_time_window_Luca_cai_initials",
 "B72PP2A_Ca_pARPP21_D1_LTP_time_window_Luca_cai_initials",
 "CaM_D1_LTP_time_window_Luca_cai_initials",
 "CaM_Ca2_D1_LTP_time_window_Luca_cai_initials",
 "CaM_Ca4_D1_LTP_time_window_Luca_cai_initials",
 "CaM_Ca4_pARPP21_D1_LTP_time_window_Luca_cai_initials",
 "CaMKII_D1_LTP_time_window_Luca_cai_initials",
 "CaMKII_CaM_Ca4_D1_LTP_time_window_Luca_cai_initials",
 "CaMKII_CaM_D1_LTP_time_window_Luca_cai_initials",
 "CaMKII_CaM_Ca2_D1_LTP_time_window_Luca_cai_initials",
 "CaMKII_CaM_Ca2_psd_D1_LTP_time_window_Luca_cai_initials",
 "CaMKII_CaM_psd_D1_LTP_time_window_Luca_cai_initials",
 "CaMKII_CaM_Ca4_psd_D1_LTP_time_window_Luca_cai_initials",
 "CaMKII_psd_D1_LTP_time_window_Luca_cai_initials",
 "cAMP_D1_LTP_time_window_Luca_cai_initials",
 "Substrate_D1_LTP_time_window_Luca_cai_initials",
 "CDK5_D1_LTP_time_window_Luca_cai_initials",
 "CDK5_D32_D1_LTP_time_window_Luca_cai_initials",
 "D1R_D1_LTP_time_window_Luca_cai_initials",
 "D1R_DA_D1_LTP_time_window_Luca_cai_initials",
 "D1R_Golf_DA_D1_LTP_time_window_Luca_cai_initials",
 "D1R_Golf_D1_LTP_time_window_Luca_cai_initials",
 "D32p34_D1_LTP_time_window_Luca_cai_initials",
 "D32p75_D1_LTP_time_window_Luca_cai_initials",
 "D32_D1_LTP_time_window_Luca_cai_initials",
 "GaolfGDP_D1_LTP_time_window_Luca_cai_initials",
 "GaolfGTP_D1_LTP_time_window_Luca_cai_initials",
 "Gbgolf_D1_LTP_time_window_Luca_cai_initials",
 "Golf_D1_LTP_time_window_Luca_cai_initials",
 "pCaMKII_D1_LTP_time_window_Luca_cai_initials",
 "pCaMKII_CaM_Ca4_D1_LTP_time_window_Luca_cai_initials",
 "pCaMKII_CaM_D1_LTP_time_window_Luca_cai_initials",
 "pCaMKII_CaM_Ca2_D1_LTP_time_window_Luca_cai_initials",
 "pCaMKII_CaM_Ca2_psd_D1_LTP_time_window_Luca_cai_initials",
 "pCaMKII_CaM_psd_D1_LTP_time_window_Luca_cai_initials",
 "pCaMKII_CaM_Ca4_psd_D1_LTP_time_window_Luca_cai_initials",
 "pCaMKII_psd_D1_LTP_time_window_Luca_cai_initials",
 "pSubstrate_D1_LTP_time_window_Luca_cai_initials",
 "PDE4_D1_LTP_time_window_Luca_cai_initials",
 "PDE4_cAMP_D1_LTP_time_window_Luca_cai_initials",
 "PDE10r_D1_LTP_time_window_Luca_cai_initials",
 "PDE10r_cAMP_D1_LTP_time_window_Luca_cai_initials",
 "PDE10c_D1_LTP_time_window_Luca_cai_initials",
 "PDE10c_cAMP_D1_LTP_time_window_Luca_cai_initials",
 "PKA_D1_LTP_time_window_Luca_cai_initials",
 "PKAc_D1_LTP_time_window_Luca_cai_initials",
 "PKAc_B56PP2A_D1_LTP_time_window_Luca_cai_initials",
 "PKAc_D32_D1_LTP_time_window_Luca_cai_initials",
 "PKAc_ARPP21_D1_LTP_time_window_Luca_cai_initials",
 "PKA_Ca2MP_D1_LTP_time_window_Luca_cai_initials",
 "PKA_Ca4MP_D1_LTP_time_window_Luca_cai_initials",
 "PKAc_D32p75_D1_LTP_time_window_Luca_cai_initials",
 "PKAreg_D1_LTP_time_window_Luca_cai_initials",
 "PP1_D1_LTP_time_window_Luca_cai_initials",
 "PP1_pCaMKII_psd_D1_LTP_time_window_Luca_cai_initials",
 "PP1_pSubstrate_D1_LTP_time_window_Luca_cai_initials",
 "PP1_D32p34_D1_LTP_time_window_Luca_cai_initials",
 "CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd_D1_LTP_time_window_Luca_cai_initials",
 "pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd_D1_LTP_time_window_Luca_cai_initials",
 "CaMKII_CaM_Ca4_CaMKII_CaM_Ca4_D1_LTP_time_window_Luca_cai_initials",
 "pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4_D1_LTP_time_window_Luca_cai_initials",
 "PP2B_D1_LTP_time_window_Luca_cai_initials",
 "PP2Bc_D1_LTP_time_window_Luca_cai_initials",
 "PP2Bc_D32p34_D1_LTP_time_window_Luca_cai_initials",
 "PP2B_CaM_D1_LTP_time_window_Luca_cai_initials",
 "PP2B_CaM_Ca2_D1_LTP_time_window_Luca_cai_initials",
 "pARPP21_D1_LTP_time_window_Luca_cai_initials",
 "ARPP21_D1_LTP_time_window_Luca_cai_initials",
 "pCaMKII_psd_Substrate_D1_LTP_time_window_Luca_cai_initials",
 "pCaMKII_CaM_psd_Substrate_D1_LTP_time_window_Luca_cai_initials",
 "pCaMKII_CaM_Ca2_psd_Substrate_D1_LTP_time_window_Luca_cai_initials",
 "pCaMKII_CaM_Ca4_psd_Substrate_D1_LTP_time_window_Luca_cai_initials",
 "CaMKII_CaM_psd_Substrate_D1_LTP_time_window_Luca_cai_initials",
 "CaMKII_CaM_Ca2_psd_Substrate_D1_LTP_time_window_Luca_cai_initials",
 "CaMKII_CaM_Ca4_psd_Substrate_D1_LTP_time_window_Luca_cai_initials",
 "total_CaMKII_activated_D1_LTP_time_window_Luca_cai_initials",
 0,
 0};
 static Symbol* _ca_sym;
 
extern Prop* need_memb(Symbol*);

static void nrn_alloc(Prop* _prop) {
	Prop *prop_ion;
	double *_p; Datum *_ppvar;
 	_p = nrn_prop_data_alloc(_mechtype, 348, _prop);
 	/*initialize range parameters*/
 	DA_start = 100;
 	DA_max = 1480;
 	_prop->param = _p;
 	_prop->param_size = 348;
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 2, _prop);
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 prop_ion = need_memb(_ca_sym);
 nrn_promote(prop_ion, 1, 0);
 	_ppvar[0]._pval = &prop_ion->param[1]; /* cai */
 
}
 static void _initlists();
  /* some states have an absolute tolerance */
 static Symbol** _atollist;
 static HocStateTolerance _hoc_state_tol[] = {
 0,0
};
 static void _update_ion_pointer(Datum*);
 extern Symbol* hoc_lookup(const char*);
extern void _nrn_thread_reg(int, int, void(*)(Datum*));
extern void _nrn_thread_table_reg(int, void(*)(double*, Datum*, Datum*, _NrnThread*, int));
extern void hoc_register_tolerance(int, HocStateTolerance*, Symbol***);
extern void _cvode_abstol( Symbol**, double*, int);

 void _D1_LTP_time_window_Luca_cai_initials_reg() {
	int _vectorized = 1;
  _initlists();
 	ion_reg("ca", 2.0);
 	_ca_sym = hoc_lookup("ca_ion");
 	register_mech(_mechanism, nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init, hoc_nrnpointerindex, 1);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
     _nrn_setdata_reg(_mechtype, _setdata);
     _nrn_thread_reg(_mechtype, 2, _update_ion_pointer);
 #if NMODL_TEXT
  hoc_reg_nmodl_text(_mechtype, nmodl_file_text);
  hoc_reg_nmodl_filename(_mechtype, nmodl_filename);
#endif
  hoc_register_prop_size(_mechtype, 348, 2);
  hoc_register_dparam_semantics(_mechtype, 0, "ca_ion");
  hoc_register_dparam_semantics(_mechtype, 1, "cvodeieq");
 	hoc_register_cvode(_mechtype, _ode_count, _ode_map, _ode_spec, _ode_matsol);
 	hoc_register_tolerance(_mechtype, _hoc_state_tol, &_atollist);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 D1_LTP_time_window_Luca_cai_initials /home/mohacsi/Desktop/optimizer/optimizer/new_test_files/Luca_modell_new/D1_LTP_time_window_Luca_cai_initials.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
 static double tau_DA1 = 34.979;
 static double tau_DA2 = 420;
 static double DA_basal = 20;
 static double Ca_basal = 60;
static int _reset;
static char *modelname = "D1_LTP_time_window";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
static int assign_calculated_values(_threadargsproto_);
static int observables_func(_threadargsproto_);
 
static int _ode_spec1(_threadargsproto_);
/*static int _ode_matsol1(_threadargsproto_);*/
 static int _slist1[96], _dlist1[96];
 static int ode(_threadargsproto_);
 
static int  assign_calculated_values ( _threadargsproto_ ) {
   time = t ;
   ATP_expression = 5000000.0 ;
   Ca_expression = 0.0 ;
   DA_expression = DA_basal + ( 1.0 / ( 1.0 + exp ( ( - 10E+10 ) * ( time - DA_start ) ) ) * ( DA_max / ( exp ( - tau_DA1 * tau_DA2 / ( tau_DA2 - tau_DA1 ) * log ( tau_DA2 / tau_DA1 ) / tau_DA1 ) - exp ( - tau_DA1 * tau_DA2 / ( tau_DA2 - tau_DA1 ) * log ( tau_DA2 / tau_DA1 ) / tau_DA2 ) ) * ( exp ( - ( time - DA_start ) / tau_DA1 ) - exp ( - ( time - DA_start ) / tau_DA2 ) ) ) ) ;
   AMP = 0.0 ;
   ATP = 5e+06 ;
   Ca = cai * ( 1e6 ) ;
   DA = DA_expression ;
   ReactionFlux0 = kf_R0 * GaolfGTP ;
   ReactionFlux1 = kf_R1 * D1R_Golf_DA ;
   ReactionFlux2 = kf_R2 * D1R_Golf * DA - kr_R2 * D1R_Golf_DA ;
   ReactionFlux3 = kf_R3 * D1R * DA - kr_R3 * D1R_DA ;
   ReactionFlux4 = kf_R4 * AC5 * GaolfGTP - kr_R4 * AC5_GaolfGTP ;
   ReactionFlux5 = kf_R5 * CaM * Ca - kr_R5 * CaM_Ca2 ;
   ReactionFlux6 = kf_R6 * PP2B * CaM - kr_R6 * PP2B_CaM ;
   ReactionFlux7 = kf_R7 * CaM_Ca4 * PP2B - kr_R7 * PP2Bc ;
   ReactionFlux8 = kf_R8 * PKAc * D32 - kr_R8 * PKAc_D32 ;
   ReactionFlux9 = kf_R9 * PKAc_D32 ;
   ReactionFlux10 = kf_R10 * PKAc * B56PP2A - kr_R10 * PKAc_B56PP2A ;
   ReactionFlux11 = kf_R11 * PKAc_B56PP2A ;
   ReactionFlux12 = kf_R12 * D32p34 * PP1 - kr_R12 * PP1_D32p34 ;
   ReactionFlux13 = kf_R13 * CDK5 * D32 - kr_R13 * CDK5_D32 ;
   ReactionFlux14 = kf_R14 * CDK5_D32 ;
   ReactionFlux15 = kf_R15 * D32p75 * PKAc - kr_R15 * PKAc_D32p75 ;
   ReactionFlux16 = kf_R16 * B72PP2A * Ca - kr_R16 * B72PP2A_Ca ;
   ReactionFlux17 = kf_R17 * B56PP2Ap * D32p75 - kr_R17 * B56PP2Ap_D32p75 ;
   ReactionFlux18 = kf_R18 * B72PP2A * D32p75 - kr_R18 * B72PP2A_D32p75 ;
   ReactionFlux19 = kf_R19 * D32p75 * B72PP2A_Ca - kr_R19 * B72PP2A_Ca_D32p75 ;
   ReactionFlux20 = kf_R20 * B56PP2Ap_D32p75 ;
   ReactionFlux21 = kf_R21 * B72PP2A_D32p75 ;
   ReactionFlux22 = kf_R22 * B72PP2A_Ca_D32p75 ;
   ReactionFlux23 = kf_R23 * D32p34 * PP2Bc - kr_R23 * PP2Bc_D32p34 ;
   ReactionFlux24 = kf_R24 * CaM_Ca2 * Ca - kr_R24 * CaM_Ca4 ;
   ReactionFlux25 = kf_R25 * Ca * PP2B_CaM - kr_R25 * PP2B_CaM_Ca2 ;
   ReactionFlux26 = kf_R26 * Ca * PP2B_CaM_Ca2 - kr_R26 * PP2Bc ;
   ReactionFlux27 = kf_R27 * CaM_Ca2 * PP2B - kr_R27 * PP2B_CaM_Ca2 ;
   ReactionFlux28 = kf_R28 * AC5 * Ca - kr_R28 * AC5_Ca ;
   ReactionFlux29 = kf_R29 * AC5_Ca * GaolfGTP - kr_R29 * AC5_Ca_GaolfGTP ;
   ReactionFlux30 = kf_R30 * D32p75 * B56PP2A - kr_R30 * B56PP2A_D32p75 ;
   ReactionFlux31 = kf_R31 * B56PP2A_D32p75 ;
   ReactionFlux32 = kf_R32 * B72PP2A_Ca_D32p34 ;
   ReactionFlux33 = kf_R33 * B72PP2A_D32p34 ;
   ReactionFlux34 = kf_R34 * D32p34 * B72PP2A_Ca - kr_R34 * B72PP2A_Ca_D32p34 ;
   ReactionFlux35 = kf_R35 * D32p34 * B72PP2A - kr_R35 * B72PP2A_D32p34 ;
   ReactionFlux36 = kf_R36 * PP2Bc_D32p34 ;
   ReactionFlux37 = kf_R37 * B56PP2Ap ;
   ReactionFlux38 = kf_R38 * cAMP * PKA - kr_R38 * PKA_Ca2MP ;
   ReactionFlux39 = kf_R39 * cAMP * PKA_Ca2MP - kr_R39 * PKA_Ca4MP ;
   ReactionFlux40 = kf_R40 * PKA_Ca4MP - kr_R40 * PKAc * PKAreg ;
   ReactionFlux41 = kf_R41 * cAMP * PDE4 - kr_R41 * PDE4_cAMP ;
   ReactionFlux42 = kf_R42 * PDE4_cAMP ;
   ReactionFlux43 = kf_R43 * PDE10r * pow( cAMP , 2.0 ) - kr_R43 * PDE10c ;
   ReactionFlux44 = kf_R44 * PDE10r_cAMP ;
   ReactionFlux45 = kf_R45 * cAMP * PDE10r - kr_R45 * PDE10r_cAMP ;
   ReactionFlux46 = kf_R46 * PDE10c_cAMP ;
   ReactionFlux47 = kf_R47 * GaolfGDP * Gbgolf ;
   ReactionFlux48 = kf_R48 * AC5_GaolfGTP * ATP - kr_R48 * AC5_GaolfGTP_ATP ;
   ReactionFlux49 = kf_R49 * AC5 * ATP - kr_R49 * AC5_ATP ;
   ReactionFlux50 = kf_R50 * AC5_Ca * ATP - kr_R50 * AC5_Ca_ATP ;
   ReactionFlux51 = kf_R51 * AC5_Ca_GaolfGTP * ATP - kr_R51 * AC5_Ca_GaolfGTP_ATP ;
   ReactionFlux52 = kf_R52 * GaolfGTP * AC5_ATP - kr_R52 * AC5_GaolfGTP_ATP ;
   ReactionFlux53 = kf_R53 * GaolfGTP * AC5_Ca_ATP - kr_R53 * AC5_Ca_GaolfGTP_ATP ;
   ReactionFlux54 = kf_R54 * Ca * AC5_ATP - kr_R54 * AC5_Ca_ATP ;
   ReactionFlux55 = kf_R55 * AC5_GaolfGTP_ATP ;
   ReactionFlux56 = kf_R56 * cAMP * AC5_GaolfGTP ;
   ReactionFlux57 = kf_R57 * AC5_ATP ;
   ReactionFlux58 = kf_R58 * cAMP * AC5 ;
   ReactionFlux59 = kf_R59 * AC5_Ca_ATP ;
   ReactionFlux60 = kf_R60 * cAMP * AC5_Ca ;
   ReactionFlux61 = kf_R61 * AC5_Ca_GaolfGTP_ATP ;
   ReactionFlux62 = kf_R62 * cAMP * AC5_Ca_GaolfGTP ;
   ReactionFlux63 = kf_R63 * AC5_GaolfGTP ;
   ReactionFlux64 = kf_R64 * AC5_Ca_GaolfGTP ;
   ReactionFlux65 = kf_R65 * AC5_GaolfGTP_ATP ;
   ReactionFlux66 = kf_R66 * AC5_Ca_GaolfGTP_ATP ;
   ReactionFlux67 = kf_R67 * D1R * Golf - kr_R67 * D1R_Golf ;
   ReactionFlux68 = kf_R68 * Golf * D1R_DA - kr_R68 * D1R_Golf_DA ;
   ReactionFlux69 = kf_R69 * cAMP * PDE10c - kr_R69 * PDE10c_cAMP ;
   ReactionFlux70 = kf_R70 * CaMKII * CaM_Ca4 - kr_R70 * CaMKII_CaM_Ca4 ;
   ReactionFlux71 = kf_R71 * CaM_Ca2 * CaMKII - kr_R71 * CaMKII_CaM_Ca2 ;
   ReactionFlux72 = kf_R72 * CaM * CaMKII - kr_R72 * CaMKII_CaM ;
   ReactionFlux73 = kf_R73 * CaMKII_CaM_Ca2 * Ca - kr_R73 * CaMKII_CaM_Ca4 ;
   ReactionFlux74 = kf_R74 * CaMKII_CaM * Ca - kr_R74 * CaMKII_CaM_Ca2 ;
   ReactionFlux75 = kf_R75 * pCaMKII_CaM_Ca2 * Ca - kr_R75 * pCaMKII_CaM_Ca4 ;
   ReactionFlux76 = kf_R76 * pCaMKII_CaM * Ca - kr_R76 * pCaMKII_CaM_Ca2 ;
   ReactionFlux77 = kf_R77 * pCaMKII * CaM_Ca4 - kr_R77 * pCaMKII_CaM_Ca4 ;
   ReactionFlux78 = kf_R78 * pCaMKII * CaM_Ca2 - kr_R78 * pCaMKII_CaM_Ca2 ;
   ReactionFlux79 = kf_R79 * pCaMKII * CaM - kr_R79 * pCaMKII_CaM ;
   ReactionFlux80 = kf_R80 * ARPP21 * PKAc - kr_R80 * PKAc_ARPP21 ;
   ReactionFlux81 = kf_R81 * PKAc_ARPP21 ;
   ReactionFlux82 = kf_R82 * pARPP21 * CaM_Ca4 - kr_R82 * CaM_Ca4_pARPP21 ;
   ReactionFlux83 = kf_R83 * B72PP2A_Ca_pARPP21 ;
   ReactionFlux84 = kf_R84 * pARPP21 * B72PP2A_Ca - kr_R84 * B72PP2A_Ca_pARPP21 ;
   ReactionFlux85 = kf_R85 * B72PP2A_pARPP21 ;
   ReactionFlux86 = kf_R86 * pARPP21 * B72PP2A - kr_R86 * B72PP2A_pARPP21 ;
   ReactionFlux87 = kf_R87 * B56PP2Ap_pARPP21 ;
   ReactionFlux88 = kf_R88 * pARPP21 * B56PP2Ap - kr_R88 * B56PP2Ap_pARPP21 ;
   ReactionFlux89 = kf_R89 * B56PP2A_pARPP21 ;
   ReactionFlux90 = kf_R90 * pARPP21 * B56PP2A - kr_R90 * B56PP2A_pARPP21 ;
   ReactionFlux91 = kf_R91 * pSubstrate * PP1 - kr_R91 * PP1_pSubstrate ;
   ReactionFlux92 = kf_R92 * PP1_pSubstrate ;
   ReactionFlux93 = kf_R93 * Substrate * pCaMKII_psd - kr_R93 * pCaMKII_psd_Substrate ;
   ReactionFlux94 = kf_R94 * pCaMKII_psd_Substrate ;
   ReactionFlux95 = kf_R95 * pCaMKII ;
   ReactionFlux96 = kf_R96 * Substrate * pCaMKII_CaM_psd - kr_R96 * pCaMKII_CaM_psd_Substrate ;
   ReactionFlux97 = kf_R97 * pCaMKII_CaM_psd_Substrate ;
   ReactionFlux98 = kf_R98 * Substrate * pCaMKII_CaM_Ca2_psd - kr_R98 * pCaMKII_CaM_Ca2_psd_Substrate ;
   ReactionFlux99 = kf_R99 * pCaMKII_CaM_Ca2_psd_Substrate ;
   ReactionFlux100 = kf_R100 * Substrate * pCaMKII_CaM_Ca4_psd - kr_R100 * pCaMKII_CaM_Ca4_psd_Substrate ;
   ReactionFlux101 = kf_R101 * pCaMKII_CaM_Ca4_psd_Substrate ;
   ReactionFlux102 = kf_R102 * Substrate * CaMKII_CaM_psd - kr_R102 * CaMKII_CaM_psd_Substrate ;
   ReactionFlux103 = kf_R103 * CaMKII_CaM_psd_Substrate ;
   ReactionFlux104 = kf_R104 * Substrate * CaMKII_CaM_Ca2_psd - kr_R104 * CaMKII_CaM_Ca2_psd_Substrate ;
   ReactionFlux105 = kf_R105 * CaMKII_CaM_Ca2_psd_Substrate ;
   ReactionFlux106 = kf_R106 * Substrate * CaMKII_CaM_Ca4_psd - kr_R106 * CaMKII_CaM_Ca4_psd_Substrate ;
   ReactionFlux107 = kf_R107 * CaMKII_CaM_Ca4_psd_Substrate ;
   ReactionFlux108 = kf_R108 * pCaMKII_CaM_Ca4 - kr_R108 * pCaMKII_CaM_Ca4_psd ;
   ReactionFlux109 = kf_R109 * pCaMKII_CaM_Ca2 - kr_R109 * pCaMKII_CaM_Ca2_psd ;
   ReactionFlux110 = kf_R110 * pCaMKII_CaM - kr_R110 * pCaMKII_CaM_psd ;
   ReactionFlux111 = kf_R111 * pCaMKII - kr_R111 * pCaMKII_psd ;
   ReactionFlux112 = kf_R112 * CaM_Ca4 * pCaMKII_psd - kr_R112 * pCaMKII_CaM_Ca4_psd ;
   ReactionFlux113 = kf_R113 * pCaMKII_psd * CaM_Ca2 - kr_R113 * pCaMKII_CaM_Ca2_psd ;
   ReactionFlux114 = kf_R114 * CaM * pCaMKII_psd - kr_R114 * pCaMKII_CaM_psd ;
   ReactionFlux115 = kf_R115 * pCaMKII_CaM_psd * Ca - kr_R115 * pCaMKII_CaM_Ca2_psd ;
   ReactionFlux116 = kf_R116 * pCaMKII_CaM_Ca2_psd * Ca - kr_R116 * pCaMKII_CaM_Ca4_psd ;
   ReactionFlux117 = kf_R117 * pCaMKII_psd * PP1 - kr_R117 * PP1_pCaMKII_psd ;
   ReactionFlux118 = kf_R118 * PP1_pCaMKII_psd ;
   ReactionFlux119 = kf_R119 * CaMKII_psd ;
   ReactionFlux120 = kf_R120 * CaM_Ca4 * CaMKII_psd - kr_R120 * CaMKII_CaM_Ca4_psd ;
   ReactionFlux121 = kf_R121 * CaM_Ca2 * CaMKII_psd - kr_R121 * CaMKII_CaM_Ca2_psd ;
   ReactionFlux122 = kf_R122 * CaM * CaMKII_psd - kr_R122 * CaMKII_CaM_psd ;
   ReactionFlux123 = kf_R123 * CaMKII_CaM_Ca2_psd * Ca - kr_R123 * CaMKII_CaM_Ca4_psd ;
   ReactionFlux124 = kf_R124 * CaMKII_CaM_psd * Ca - kr_R124 * CaMKII_CaM_Ca2_psd ;
   ReactionFlux125 = kf_R125 * CaMKII_CaM - kr_R125 * CaMKII_CaM_psd ;
   ReactionFlux126 = kf_R126 * CaMKII_CaM_Ca2 - kr_R126 * CaMKII_CaM_Ca2_psd ;
   ReactionFlux127 = kf_R127 * CaMKII_CaM_Ca4 - kr_R127 * CaMKII_CaM_Ca4_psd ;
   ReactionFlux128 = kf_R128 * CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd - kr_R128 * CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 ;
   ReactionFlux129 = kf_R129 * pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd - kr_R129 * pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 ;
   ReactionFlux130 = kf_R130 * CaMKII_CaM_Ca4 * CaMKII_CaM_Ca4 - kr_R130 * CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 ;
   ReactionFlux131 = kf_R131 * CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 ;
   ReactionFlux132 = kf_R132 * pCaMKII_CaM_Ca4 * CaMKII_CaM_Ca4 - kr_R132 * pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 ;
   ReactionFlux133 = kf_R133 * pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 ;
   ReactionFlux134 = kf_R134 * CaMKII_CaM_Ca4_psd * CaMKII_CaM_Ca4_psd - kr_R134 * CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd ;
   ReactionFlux135 = kf_R135 * CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd ;
   ReactionFlux136 = kf_R136 * pCaMKII_CaM_Ca4_psd * CaMKII_CaM_Ca4_psd - kr_R136 * pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd ;
   ReactionFlux137 = kf_R137 * pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd ;
   total_CaMKII_activated = pCaMKII_CaM_Ca4_psd + pCaMKII_CaM_Ca2_psd + pCaMKII_CaM_psd + pCaMKII_psd + CaMKII_CaM_Ca4_psd + CaMKII_CaM_Ca2_psd + CaMKII_CaM_Ca4_psd_Substrate + CaMKII_CaM_psd_Substrate + CaMKII_CaM_Ca2_psd_Substrate + pCaMKII_psd_Substrate + pCaMKII_CaM_psd_Substrate + pCaMKII_CaM_Ca2_psd_Substrate + pCaMKII_CaM_Ca4_psd_Substrate ;
    return 0; }
 
static void _hoc_assign_calculated_values(void) {
  double _r;
   double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   if (_extcall_prop) {_p = _extcall_prop->param; _ppvar = _extcall_prop->dparam;}else{ _p = (double*)0; _ppvar = (Datum*)0; }
  _thread = _extcall_thread;
  _nt = nrn_threads;
 _r = 1.;
 assign_calculated_values ( _p, _ppvar, _thread, _nt );
 hoc_retpushx(_r);
}
 
/*CVODE*/
 static int _ode_spec1 (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {int _reset = 0; {
   DAC5 = - ReactionFlux4 - ReactionFlux28 - ReactionFlux49 + ReactionFlux57 - ReactionFlux58 + ReactionFlux63 ;
   DAC5_ATP = ReactionFlux49 - ReactionFlux52 - ReactionFlux54 - ReactionFlux57 + ReactionFlux58 + ReactionFlux65 ;
   DAC5_Ca = ReactionFlux28 - ReactionFlux29 - ReactionFlux50 + ReactionFlux59 - ReactionFlux60 + ReactionFlux64 ;
   DAC5_Ca_ATP = ReactionFlux50 - ReactionFlux53 + ReactionFlux54 - ReactionFlux59 + ReactionFlux60 + ReactionFlux66 ;
   DAC5_Ca_GaolfGTP = ReactionFlux29 - ReactionFlux51 + ReactionFlux61 - ReactionFlux62 - ReactionFlux64 ;
   DAC5_Ca_GaolfGTP_ATP = ReactionFlux51 + ReactionFlux53 - ReactionFlux61 + ReactionFlux62 - ReactionFlux66 ;
   DAC5_GaolfGTP = ReactionFlux4 - ReactionFlux48 + ReactionFlux55 - ReactionFlux56 - ReactionFlux63 ;
   DAC5_GaolfGTP_ATP = ReactionFlux48 + ReactionFlux52 - ReactionFlux55 + ReactionFlux56 - ReactionFlux65 ;
   DB56PP2A = - ReactionFlux10 - ReactionFlux30 + ReactionFlux31 + ReactionFlux37 + ReactionFlux89 - ReactionFlux90 ;
   DB56PP2A_D32p75 = ReactionFlux30 - ReactionFlux31 ;
   DB56PP2A_pARPP21 = - ReactionFlux89 + ReactionFlux90 ;
   DB56PP2Ap = ReactionFlux11 - ReactionFlux17 + ReactionFlux20 - ReactionFlux37 + ReactionFlux87 - ReactionFlux88 ;
   DB56PP2Ap_D32p75 = ReactionFlux17 - ReactionFlux20 ;
   DB56PP2Ap_pARPP21 = - ReactionFlux87 + ReactionFlux88 ;
   DB72PP2A = - ReactionFlux16 - ReactionFlux18 + ReactionFlux21 + ReactionFlux33 - ReactionFlux35 + ReactionFlux85 - ReactionFlux86 ;
   DB72PP2A_D32p34 = - ReactionFlux33 + ReactionFlux35 ;
   DB72PP2A_D32p75 = ReactionFlux18 - ReactionFlux21 ;
   DB72PP2A_pARPP21 = - ReactionFlux85 + ReactionFlux86 ;
   DB72PP2A_Ca_D32p34 = - ReactionFlux32 + ReactionFlux34 ;
   DB72PP2A_Ca_D32p75 = ReactionFlux19 - ReactionFlux22 ;
   DB72PP2A_Ca = ReactionFlux16 - ReactionFlux19 + ReactionFlux22 + ReactionFlux32 - ReactionFlux34 + ReactionFlux83 - ReactionFlux84 ;
   DB72PP2A_Ca_pARPP21 = - ReactionFlux83 + ReactionFlux84 ;
   DCaM = - ReactionFlux5 - ReactionFlux6 - ReactionFlux72 - ReactionFlux79 - ReactionFlux114 - ReactionFlux122 ;
   DCaM_Ca2 = ReactionFlux5 - ReactionFlux24 - ReactionFlux27 - ReactionFlux71 - ReactionFlux78 - ReactionFlux113 - ReactionFlux121 ;
   DCaM_Ca4 = - ReactionFlux7 + ReactionFlux24 - ReactionFlux70 - ReactionFlux77 - ReactionFlux82 - ReactionFlux112 - ReactionFlux120 ;
   DCaM_Ca4_pARPP21 = ReactionFlux82 ;
   DCaMKII = - ReactionFlux70 - ReactionFlux71 - ReactionFlux72 + ReactionFlux95 + ReactionFlux119 ;
   DCaMKII_CaM_Ca4 = ReactionFlux70 + ReactionFlux73 - ReactionFlux127 - ReactionFlux130 - ReactionFlux130 + ReactionFlux131 - ReactionFlux132 ;
   DCaMKII_CaM = ReactionFlux72 - ReactionFlux74 - ReactionFlux125 ;
   DCaMKII_CaM_Ca2 = ReactionFlux71 - ReactionFlux73 + ReactionFlux74 - ReactionFlux126 ;
   DCaMKII_CaM_Ca2_psd = - ReactionFlux104 + ReactionFlux105 + ReactionFlux121 - ReactionFlux123 + ReactionFlux124 + ReactionFlux126 ;
   DCaMKII_CaM_psd = - ReactionFlux102 + ReactionFlux103 + ReactionFlux122 - ReactionFlux124 + ReactionFlux125 ;
   DCaMKII_CaM_Ca4_psd = - ReactionFlux106 + ReactionFlux107 + ReactionFlux120 + ReactionFlux123 + ReactionFlux127 - ReactionFlux134 - ReactionFlux134 + ReactionFlux135 - ReactionFlux136 ;
   DCaMKII_psd = ReactionFlux118 - ReactionFlux119 - ReactionFlux120 - ReactionFlux121 - ReactionFlux122 ;
   DcAMP = - ReactionFlux38 - ReactionFlux39 - ReactionFlux41 - 2.0 * ReactionFlux43 - ReactionFlux45 + ReactionFlux55 - ReactionFlux56 + ReactionFlux57 - ReactionFlux58 + ReactionFlux59 - ReactionFlux60 + ReactionFlux61 - ReactionFlux62 - ReactionFlux69 ;
   DSubstrate = ReactionFlux92 - ReactionFlux93 - ReactionFlux96 - ReactionFlux98 - ReactionFlux100 - ReactionFlux102 - ReactionFlux104 - ReactionFlux106 ;
   DCDK5 = - ReactionFlux13 + ReactionFlux14 ;
   DCDK5_D32 = ReactionFlux13 - ReactionFlux14 ;
   DD1R = - ReactionFlux3 - ReactionFlux67 ;
   DD1R_DA = ReactionFlux1 + ReactionFlux3 - ReactionFlux68 ;
   DD1R_Golf_DA = - ReactionFlux1 + ReactionFlux2 + ReactionFlux68 ;
   DD1R_Golf = - ReactionFlux2 + ReactionFlux67 ;
   DD32p34 = ReactionFlux9 - ReactionFlux12 - ReactionFlux23 - ReactionFlux34 - ReactionFlux35 ;
   DD32p75 = ReactionFlux14 - ReactionFlux15 - ReactionFlux17 - ReactionFlux18 - ReactionFlux19 - ReactionFlux30 ;
   DD32 = - ReactionFlux8 - ReactionFlux13 + ReactionFlux20 + ReactionFlux21 + ReactionFlux22 + ReactionFlux31 + ReactionFlux32 + ReactionFlux33 + ReactionFlux36 ;
   DGaolfGDP = ReactionFlux0 - ReactionFlux47 + ReactionFlux63 + ReactionFlux64 + ReactionFlux65 + ReactionFlux66 ;
   DGaolfGTP = - ReactionFlux0 + ReactionFlux1 - ReactionFlux4 - ReactionFlux29 - ReactionFlux52 - ReactionFlux53 ;
   DGbgolf = ReactionFlux1 - ReactionFlux47 ;
   DGolf = ReactionFlux47 - ReactionFlux67 - ReactionFlux68 ;
   DpCaMKII = - ReactionFlux77 - ReactionFlux78 - ReactionFlux79 - ReactionFlux95 - ReactionFlux111 ;
   DpCaMKII_CaM_Ca4 = ReactionFlux75 + ReactionFlux77 - ReactionFlux108 + ReactionFlux131 - ReactionFlux132 + ReactionFlux133 + ReactionFlux133 ;
   DpCaMKII_CaM = - ReactionFlux76 + ReactionFlux79 - ReactionFlux110 ;
   DpCaMKII_CaM_Ca2 = - ReactionFlux75 + ReactionFlux76 + ReactionFlux78 - ReactionFlux109 ;
   DpCaMKII_CaM_Ca2_psd = - ReactionFlux98 + ReactionFlux99 + ReactionFlux109 + ReactionFlux113 + ReactionFlux115 - ReactionFlux116 ;
   DpCaMKII_CaM_psd = - ReactionFlux96 + ReactionFlux97 + ReactionFlux110 + ReactionFlux114 - ReactionFlux115 ;
   DpCaMKII_CaM_Ca4_psd = - ReactionFlux100 + ReactionFlux101 + ReactionFlux108 + ReactionFlux112 + ReactionFlux116 + ReactionFlux135 - ReactionFlux136 + ReactionFlux137 + ReactionFlux137 ;
   DpCaMKII_psd = - ReactionFlux93 + ReactionFlux94 + ReactionFlux111 - ReactionFlux112 - ReactionFlux113 - ReactionFlux114 - ReactionFlux117 ;
   DpSubstrate = - ReactionFlux91 + ReactionFlux94 + ReactionFlux97 + ReactionFlux99 + ReactionFlux101 + ReactionFlux103 + ReactionFlux105 + ReactionFlux107 ;
   DPDE4 = - ReactionFlux41 + ReactionFlux42 ;
   DPDE4_cAMP = ReactionFlux41 - ReactionFlux42 ;
   DPDE10r = - ReactionFlux43 + ReactionFlux44 - ReactionFlux45 ;
   DPDE10r_cAMP = - ReactionFlux44 + ReactionFlux45 ;
   DPDE10c = ReactionFlux43 + ReactionFlux46 - ReactionFlux69 ;
   DPDE10c_cAMP = - ReactionFlux46 + ReactionFlux69 ;
   DPKA = - ReactionFlux38 ;
   DPKAc = - ReactionFlux8 + ReactionFlux9 - ReactionFlux10 + ReactionFlux11 - ReactionFlux15 + ReactionFlux40 - ReactionFlux80 + ReactionFlux81 ;
   DPKAc_B56PP2A = ReactionFlux10 - ReactionFlux11 ;
   DPKAc_D32 = ReactionFlux8 - ReactionFlux9 ;
   DPKAc_ARPP21 = ReactionFlux80 - ReactionFlux81 ;
   DPKA_Ca2MP = ReactionFlux38 - ReactionFlux39 ;
   DPKA_Ca4MP = ReactionFlux39 - ReactionFlux40 ;
   DPKAc_D32p75 = ReactionFlux15 ;
   DPKAreg = ReactionFlux40 ;
   DPP1 = - ReactionFlux12 - ReactionFlux91 + ReactionFlux92 - ReactionFlux117 + ReactionFlux118 ;
   DPP1_pCaMKII_psd = ReactionFlux117 - ReactionFlux118 ;
   DPP1_pSubstrate = ReactionFlux91 - ReactionFlux92 ;
   DPP1_D32p34 = ReactionFlux12 ;
   DCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd = - ReactionFlux128 + ReactionFlux134 - ReactionFlux135 ;
   DpCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd = - ReactionFlux129 + ReactionFlux136 - ReactionFlux137 ;
   DCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 = ReactionFlux128 + ReactionFlux130 - ReactionFlux131 ;
   DpCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 = ReactionFlux129 + ReactionFlux132 - ReactionFlux133 ;
   DPP2B = - ReactionFlux6 - ReactionFlux7 - ReactionFlux27 ;
   DPP2Bc = ReactionFlux7 - ReactionFlux23 + ReactionFlux26 + ReactionFlux36 ;
   DPP2Bc_D32p34 = ReactionFlux23 - ReactionFlux36 ;
   DPP2B_CaM = ReactionFlux6 - ReactionFlux25 ;
   DPP2B_CaM_Ca2 = ReactionFlux25 - ReactionFlux26 + ReactionFlux27 ;
   DpARPP21 = ReactionFlux81 - ReactionFlux82 - ReactionFlux84 - ReactionFlux86 - ReactionFlux88 - ReactionFlux90 ;
   DARPP21 = - ReactionFlux80 + ReactionFlux83 + ReactionFlux85 + ReactionFlux87 + ReactionFlux89 ;
   DpCaMKII_psd_Substrate = ReactionFlux93 - ReactionFlux94 ;
   DpCaMKII_CaM_psd_Substrate = ReactionFlux96 - ReactionFlux97 ;
   DpCaMKII_CaM_Ca2_psd_Substrate = ReactionFlux98 - ReactionFlux99 ;
   DpCaMKII_CaM_Ca4_psd_Substrate = ReactionFlux100 - ReactionFlux101 ;
   DCaMKII_CaM_psd_Substrate = ReactionFlux102 - ReactionFlux103 ;
   DCaMKII_CaM_Ca2_psd_Substrate = ReactionFlux104 - ReactionFlux105 ;
   DCaMKII_CaM_Ca4_psd_Substrate = ReactionFlux106 - ReactionFlux107 ;
   Dtotal_CaMKII_activated = DpCaMKII_CaM_Ca4_psd + DpCaMKII_CaM_Ca2_psd + DpCaMKII_CaM_psd + DpCaMKII_psd + DCaMKII_CaM_Ca4_psd + DCaMKII_CaM_Ca2_psd + DCaMKII_CaM_Ca4_psd_Substrate + DCaMKII_CaM_psd_Substrate + DCaMKII_CaM_Ca2_psd_Substrate + DpCaMKII_psd_Substrate + DpCaMKII_CaM_psd_Substrate + DpCaMKII_CaM_Ca2_psd_Substrate + DpCaMKII_CaM_Ca4_psd_Substrate ;
   }
 return _reset;
}
 static int _ode_matsol1 (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
 DAC5 = DAC5  / (1. - dt*( 0.0 )) ;
 DAC5_ATP = DAC5_ATP  / (1. - dt*( 0.0 )) ;
 DAC5_Ca = DAC5_Ca  / (1. - dt*( 0.0 )) ;
 DAC5_Ca_ATP = DAC5_Ca_ATP  / (1. - dt*( 0.0 )) ;
 DAC5_Ca_GaolfGTP = DAC5_Ca_GaolfGTP  / (1. - dt*( 0.0 )) ;
 DAC5_Ca_GaolfGTP_ATP = DAC5_Ca_GaolfGTP_ATP  / (1. - dt*( 0.0 )) ;
 DAC5_GaolfGTP = DAC5_GaolfGTP  / (1. - dt*( 0.0 )) ;
 DAC5_GaolfGTP_ATP = DAC5_GaolfGTP_ATP  / (1. - dt*( 0.0 )) ;
 DB56PP2A = DB56PP2A  / (1. - dt*( 0.0 )) ;
 DB56PP2A_D32p75 = DB56PP2A_D32p75  / (1. - dt*( 0.0 )) ;
 DB56PP2A_pARPP21 = DB56PP2A_pARPP21  / (1. - dt*( 0.0 )) ;
 DB56PP2Ap = DB56PP2Ap  / (1. - dt*( 0.0 )) ;
 DB56PP2Ap_D32p75 = DB56PP2Ap_D32p75  / (1. - dt*( 0.0 )) ;
 DB56PP2Ap_pARPP21 = DB56PP2Ap_pARPP21  / (1. - dt*( 0.0 )) ;
 DB72PP2A = DB72PP2A  / (1. - dt*( 0.0 )) ;
 DB72PP2A_D32p34 = DB72PP2A_D32p34  / (1. - dt*( 0.0 )) ;
 DB72PP2A_D32p75 = DB72PP2A_D32p75  / (1. - dt*( 0.0 )) ;
 DB72PP2A_pARPP21 = DB72PP2A_pARPP21  / (1. - dt*( 0.0 )) ;
 DB72PP2A_Ca_D32p34 = DB72PP2A_Ca_D32p34  / (1. - dt*( 0.0 )) ;
 DB72PP2A_Ca_D32p75 = DB72PP2A_Ca_D32p75  / (1. - dt*( 0.0 )) ;
 DB72PP2A_Ca = DB72PP2A_Ca  / (1. - dt*( 0.0 )) ;
 DB72PP2A_Ca_pARPP21 = DB72PP2A_Ca_pARPP21  / (1. - dt*( 0.0 )) ;
 DCaM = DCaM  / (1. - dt*( 0.0 )) ;
 DCaM_Ca2 = DCaM_Ca2  / (1. - dt*( 0.0 )) ;
 DCaM_Ca4 = DCaM_Ca4  / (1. - dt*( 0.0 )) ;
 DCaM_Ca4_pARPP21 = DCaM_Ca4_pARPP21  / (1. - dt*( 0.0 )) ;
 DCaMKII = DCaMKII  / (1. - dt*( 0.0 )) ;
 DCaMKII_CaM_Ca4 = DCaMKII_CaM_Ca4  / (1. - dt*( 0.0 )) ;
 DCaMKII_CaM = DCaMKII_CaM  / (1. - dt*( 0.0 )) ;
 DCaMKII_CaM_Ca2 = DCaMKII_CaM_Ca2  / (1. - dt*( 0.0 )) ;
 DCaMKII_CaM_Ca2_psd = DCaMKII_CaM_Ca2_psd  / (1. - dt*( 0.0 )) ;
 DCaMKII_CaM_psd = DCaMKII_CaM_psd  / (1. - dt*( 0.0 )) ;
 DCaMKII_CaM_Ca4_psd = DCaMKII_CaM_Ca4_psd  / (1. - dt*( 0.0 )) ;
 DCaMKII_psd = DCaMKII_psd  / (1. - dt*( 0.0 )) ;
 DcAMP = DcAMP  / (1. - dt*( 0.0 )) ;
 DSubstrate = DSubstrate  / (1. - dt*( 0.0 )) ;
 DCDK5 = DCDK5  / (1. - dt*( 0.0 )) ;
 DCDK5_D32 = DCDK5_D32  / (1. - dt*( 0.0 )) ;
 DD1R = DD1R  / (1. - dt*( 0.0 )) ;
 DD1R_DA = DD1R_DA  / (1. - dt*( 0.0 )) ;
 DD1R_Golf_DA = DD1R_Golf_DA  / (1. - dt*( 0.0 )) ;
 DD1R_Golf = DD1R_Golf  / (1. - dt*( 0.0 )) ;
 DD32p34 = DD32p34  / (1. - dt*( 0.0 )) ;
 DD32p75 = DD32p75  / (1. - dt*( 0.0 )) ;
 DD32 = DD32  / (1. - dt*( 0.0 )) ;
 DGaolfGDP = DGaolfGDP  / (1. - dt*( 0.0 )) ;
 DGaolfGTP = DGaolfGTP  / (1. - dt*( 0.0 )) ;
 DGbgolf = DGbgolf  / (1. - dt*( 0.0 )) ;
 DGolf = DGolf  / (1. - dt*( 0.0 )) ;
 DpCaMKII = DpCaMKII  / (1. - dt*( 0.0 )) ;
 DpCaMKII_CaM_Ca4 = DpCaMKII_CaM_Ca4  / (1. - dt*( 0.0 )) ;
 DpCaMKII_CaM = DpCaMKII_CaM  / (1. - dt*( 0.0 )) ;
 DpCaMKII_CaM_Ca2 = DpCaMKII_CaM_Ca2  / (1. - dt*( 0.0 )) ;
 DpCaMKII_CaM_Ca2_psd = DpCaMKII_CaM_Ca2_psd  / (1. - dt*( 0.0 )) ;
 DpCaMKII_CaM_psd = DpCaMKII_CaM_psd  / (1. - dt*( 0.0 )) ;
 DpCaMKII_CaM_Ca4_psd = DpCaMKII_CaM_Ca4_psd  / (1. - dt*( 0.0 )) ;
 DpCaMKII_psd = DpCaMKII_psd  / (1. - dt*( 0.0 )) ;
 DpSubstrate = DpSubstrate  / (1. - dt*( 0.0 )) ;
 DPDE4 = DPDE4  / (1. - dt*( 0.0 )) ;
 DPDE4_cAMP = DPDE4_cAMP  / (1. - dt*( 0.0 )) ;
 DPDE10r = DPDE10r  / (1. - dt*( 0.0 )) ;
 DPDE10r_cAMP = DPDE10r_cAMP  / (1. - dt*( 0.0 )) ;
 DPDE10c = DPDE10c  / (1. - dt*( 0.0 )) ;
 DPDE10c_cAMP = DPDE10c_cAMP  / (1. - dt*( 0.0 )) ;
 DPKA = DPKA  / (1. - dt*( 0.0 )) ;
 DPKAc = DPKAc  / (1. - dt*( 0.0 )) ;
 DPKAc_B56PP2A = DPKAc_B56PP2A  / (1. - dt*( 0.0 )) ;
 DPKAc_D32 = DPKAc_D32  / (1. - dt*( 0.0 )) ;
 DPKAc_ARPP21 = DPKAc_ARPP21  / (1. - dt*( 0.0 )) ;
 DPKA_Ca2MP = DPKA_Ca2MP  / (1. - dt*( 0.0 )) ;
 DPKA_Ca4MP = DPKA_Ca4MP  / (1. - dt*( 0.0 )) ;
 DPKAc_D32p75 = DPKAc_D32p75  / (1. - dt*( 0.0 )) ;
 DPKAreg = DPKAreg  / (1. - dt*( 0.0 )) ;
 DPP1 = DPP1  / (1. - dt*( 0.0 )) ;
 DPP1_pCaMKII_psd = DPP1_pCaMKII_psd  / (1. - dt*( 0.0 )) ;
 DPP1_pSubstrate = DPP1_pSubstrate  / (1. - dt*( 0.0 )) ;
 DPP1_D32p34 = DPP1_D32p34  / (1. - dt*( 0.0 )) ;
 DCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd = DCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd  / (1. - dt*( 0.0 )) ;
 DpCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd = DpCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd  / (1. - dt*( 0.0 )) ;
 DCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 = DCaMKII_CaM_Ca4_CaMKII_CaM_Ca4  / (1. - dt*( 0.0 )) ;
 DpCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 = DpCaMKII_CaM_Ca4_CaMKII_CaM_Ca4  / (1. - dt*( 0.0 )) ;
 DPP2B = DPP2B  / (1. - dt*( 0.0 )) ;
 DPP2Bc = DPP2Bc  / (1. - dt*( 0.0 )) ;
 DPP2Bc_D32p34 = DPP2Bc_D32p34  / (1. - dt*( 0.0 )) ;
 DPP2B_CaM = DPP2B_CaM  / (1. - dt*( 0.0 )) ;
 DPP2B_CaM_Ca2 = DPP2B_CaM_Ca2  / (1. - dt*( 0.0 )) ;
 DpARPP21 = DpARPP21  / (1. - dt*( 0.0 )) ;
 DARPP21 = DARPP21  / (1. - dt*( 0.0 )) ;
 DpCaMKII_psd_Substrate = DpCaMKII_psd_Substrate  / (1. - dt*( 0.0 )) ;
 DpCaMKII_CaM_psd_Substrate = DpCaMKII_CaM_psd_Substrate  / (1. - dt*( 0.0 )) ;
 DpCaMKII_CaM_Ca2_psd_Substrate = DpCaMKII_CaM_Ca2_psd_Substrate  / (1. - dt*( 0.0 )) ;
 DpCaMKII_CaM_Ca4_psd_Substrate = DpCaMKII_CaM_Ca4_psd_Substrate  / (1. - dt*( 0.0 )) ;
 DCaMKII_CaM_psd_Substrate = DCaMKII_CaM_psd_Substrate  / (1. - dt*( 0.0 )) ;
 DCaMKII_CaM_Ca2_psd_Substrate = DCaMKII_CaM_Ca2_psd_Substrate  / (1. - dt*( 0.0 )) ;
 DCaMKII_CaM_Ca4_psd_Substrate = DCaMKII_CaM_Ca4_psd_Substrate  / (1. - dt*( 0.0 )) ;
 Dtotal_CaMKII_activated = Dtotal_CaMKII_activated  / (1. - dt*( 0.0 )) ;
  return 0;
}
 /*END CVODE*/
 static int ode (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) { {
    AC5 = AC5 - dt*(- ( - ReactionFlux4 - ReactionFlux28 - ReactionFlux49 + ReactionFlux57 - ReactionFlux58 + ReactionFlux63 ) ) ;
    AC5_ATP = AC5_ATP - dt*(- ( ReactionFlux49 - ReactionFlux52 - ReactionFlux54 - ReactionFlux57 + ReactionFlux58 + ReactionFlux65 ) ) ;
    AC5_Ca = AC5_Ca - dt*(- ( ReactionFlux28 - ReactionFlux29 - ReactionFlux50 + ReactionFlux59 - ReactionFlux60 + ReactionFlux64 ) ) ;
    AC5_Ca_ATP = AC5_Ca_ATP - dt*(- ( ReactionFlux50 - ReactionFlux53 + ReactionFlux54 - ReactionFlux59 + ReactionFlux60 + ReactionFlux66 ) ) ;
    AC5_Ca_GaolfGTP = AC5_Ca_GaolfGTP - dt*(- ( ReactionFlux29 - ReactionFlux51 + ReactionFlux61 - ReactionFlux62 - ReactionFlux64 ) ) ;
    AC5_Ca_GaolfGTP_ATP = AC5_Ca_GaolfGTP_ATP - dt*(- ( ReactionFlux51 + ReactionFlux53 - ReactionFlux61 + ReactionFlux62 - ReactionFlux66 ) ) ;
    AC5_GaolfGTP = AC5_GaolfGTP - dt*(- ( ReactionFlux4 - ReactionFlux48 + ReactionFlux55 - ReactionFlux56 - ReactionFlux63 ) ) ;
    AC5_GaolfGTP_ATP = AC5_GaolfGTP_ATP - dt*(- ( ReactionFlux48 + ReactionFlux52 - ReactionFlux55 + ReactionFlux56 - ReactionFlux65 ) ) ;
    B56PP2A = B56PP2A - dt*(- ( - ReactionFlux10 - ReactionFlux30 + ReactionFlux31 + ReactionFlux37 + ReactionFlux89 - ReactionFlux90 ) ) ;
    B56PP2A_D32p75 = B56PP2A_D32p75 - dt*(- ( ReactionFlux30 - ReactionFlux31 ) ) ;
    B56PP2A_pARPP21 = B56PP2A_pARPP21 - dt*(- ( - ReactionFlux89 + ReactionFlux90 ) ) ;
    B56PP2Ap = B56PP2Ap - dt*(- ( ReactionFlux11 - ReactionFlux17 + ReactionFlux20 - ReactionFlux37 + ReactionFlux87 - ReactionFlux88 ) ) ;
    B56PP2Ap_D32p75 = B56PP2Ap_D32p75 - dt*(- ( ReactionFlux17 - ReactionFlux20 ) ) ;
    B56PP2Ap_pARPP21 = B56PP2Ap_pARPP21 - dt*(- ( - ReactionFlux87 + ReactionFlux88 ) ) ;
    B72PP2A = B72PP2A - dt*(- ( - ReactionFlux16 - ReactionFlux18 + ReactionFlux21 + ReactionFlux33 - ReactionFlux35 + ReactionFlux85 - ReactionFlux86 ) ) ;
    B72PP2A_D32p34 = B72PP2A_D32p34 - dt*(- ( - ReactionFlux33 + ReactionFlux35 ) ) ;
    B72PP2A_D32p75 = B72PP2A_D32p75 - dt*(- ( ReactionFlux18 - ReactionFlux21 ) ) ;
    B72PP2A_pARPP21 = B72PP2A_pARPP21 - dt*(- ( - ReactionFlux85 + ReactionFlux86 ) ) ;
    B72PP2A_Ca_D32p34 = B72PP2A_Ca_D32p34 - dt*(- ( - ReactionFlux32 + ReactionFlux34 ) ) ;
    B72PP2A_Ca_D32p75 = B72PP2A_Ca_D32p75 - dt*(- ( ReactionFlux19 - ReactionFlux22 ) ) ;
    B72PP2A_Ca = B72PP2A_Ca - dt*(- ( ReactionFlux16 - ReactionFlux19 + ReactionFlux22 + ReactionFlux32 - ReactionFlux34 + ReactionFlux83 - ReactionFlux84 ) ) ;
    B72PP2A_Ca_pARPP21 = B72PP2A_Ca_pARPP21 - dt*(- ( - ReactionFlux83 + ReactionFlux84 ) ) ;
    CaM = CaM - dt*(- ( - ReactionFlux5 - ReactionFlux6 - ReactionFlux72 - ReactionFlux79 - ReactionFlux114 - ReactionFlux122 ) ) ;
    CaM_Ca2 = CaM_Ca2 - dt*(- ( ReactionFlux5 - ReactionFlux24 - ReactionFlux27 - ReactionFlux71 - ReactionFlux78 - ReactionFlux113 - ReactionFlux121 ) ) ;
    CaM_Ca4 = CaM_Ca4 - dt*(- ( - ReactionFlux7 + ReactionFlux24 - ReactionFlux70 - ReactionFlux77 - ReactionFlux82 - ReactionFlux112 - ReactionFlux120 ) ) ;
    CaM_Ca4_pARPP21 = CaM_Ca4_pARPP21 - dt*(- ( ReactionFlux82 ) ) ;
    CaMKII = CaMKII - dt*(- ( - ReactionFlux70 - ReactionFlux71 - ReactionFlux72 + ReactionFlux95 + ReactionFlux119 ) ) ;
    CaMKII_CaM_Ca4 = CaMKII_CaM_Ca4 - dt*(- ( ReactionFlux70 + ReactionFlux73 - ReactionFlux127 - ReactionFlux130 - ReactionFlux130 + ReactionFlux131 - ReactionFlux132 ) ) ;
    CaMKII_CaM = CaMKII_CaM - dt*(- ( ReactionFlux72 - ReactionFlux74 - ReactionFlux125 ) ) ;
    CaMKII_CaM_Ca2 = CaMKII_CaM_Ca2 - dt*(- ( ReactionFlux71 - ReactionFlux73 + ReactionFlux74 - ReactionFlux126 ) ) ;
    CaMKII_CaM_Ca2_psd = CaMKII_CaM_Ca2_psd - dt*(- ( - ReactionFlux104 + ReactionFlux105 + ReactionFlux121 - ReactionFlux123 + ReactionFlux124 + ReactionFlux126 ) ) ;
    CaMKII_CaM_psd = CaMKII_CaM_psd - dt*(- ( - ReactionFlux102 + ReactionFlux103 + ReactionFlux122 - ReactionFlux124 + ReactionFlux125 ) ) ;
    CaMKII_CaM_Ca4_psd = CaMKII_CaM_Ca4_psd - dt*(- ( - ReactionFlux106 + ReactionFlux107 + ReactionFlux120 + ReactionFlux123 + ReactionFlux127 - ReactionFlux134 - ReactionFlux134 + ReactionFlux135 - ReactionFlux136 ) ) ;
    CaMKII_psd = CaMKII_psd - dt*(- ( ReactionFlux118 - ReactionFlux119 - ReactionFlux120 - ReactionFlux121 - ReactionFlux122 ) ) ;
    cAMP = cAMP - dt*(- ( - ReactionFlux38 - ReactionFlux39 - ReactionFlux41 - ( 2.0 )*( ReactionFlux43 ) - ReactionFlux45 + ReactionFlux55 - ReactionFlux56 + ReactionFlux57 - ReactionFlux58 + ReactionFlux59 - ReactionFlux60 + ReactionFlux61 - ReactionFlux62 - ReactionFlux69 ) ) ;
    Substrate = Substrate - dt*(- ( ReactionFlux92 - ReactionFlux93 - ReactionFlux96 - ReactionFlux98 - ReactionFlux100 - ReactionFlux102 - ReactionFlux104 - ReactionFlux106 ) ) ;
    CDK5 = CDK5 - dt*(- ( - ReactionFlux13 + ReactionFlux14 ) ) ;
    CDK5_D32 = CDK5_D32 - dt*(- ( ReactionFlux13 - ReactionFlux14 ) ) ;
    D1R = D1R - dt*(- ( - ReactionFlux3 - ReactionFlux67 ) ) ;
    D1R_DA = D1R_DA - dt*(- ( ReactionFlux1 + ReactionFlux3 - ReactionFlux68 ) ) ;
    D1R_Golf_DA = D1R_Golf_DA - dt*(- ( - ReactionFlux1 + ReactionFlux2 + ReactionFlux68 ) ) ;
    D1R_Golf = D1R_Golf - dt*(- ( - ReactionFlux2 + ReactionFlux67 ) ) ;
    D32p34 = D32p34 - dt*(- ( ReactionFlux9 - ReactionFlux12 - ReactionFlux23 - ReactionFlux34 - ReactionFlux35 ) ) ;
    D32p75 = D32p75 - dt*(- ( ReactionFlux14 - ReactionFlux15 - ReactionFlux17 - ReactionFlux18 - ReactionFlux19 - ReactionFlux30 ) ) ;
    D32 = D32 - dt*(- ( - ReactionFlux8 - ReactionFlux13 + ReactionFlux20 + ReactionFlux21 + ReactionFlux22 + ReactionFlux31 + ReactionFlux32 + ReactionFlux33 + ReactionFlux36 ) ) ;
    GaolfGDP = GaolfGDP - dt*(- ( ReactionFlux0 - ReactionFlux47 + ReactionFlux63 + ReactionFlux64 + ReactionFlux65 + ReactionFlux66 ) ) ;
    GaolfGTP = GaolfGTP - dt*(- ( - ReactionFlux0 + ReactionFlux1 - ReactionFlux4 - ReactionFlux29 - ReactionFlux52 - ReactionFlux53 ) ) ;
    Gbgolf = Gbgolf - dt*(- ( ReactionFlux1 - ReactionFlux47 ) ) ;
    Golf = Golf - dt*(- ( ReactionFlux47 - ReactionFlux67 - ReactionFlux68 ) ) ;
    pCaMKII = pCaMKII - dt*(- ( - ReactionFlux77 - ReactionFlux78 - ReactionFlux79 - ReactionFlux95 - ReactionFlux111 ) ) ;
    pCaMKII_CaM_Ca4 = pCaMKII_CaM_Ca4 - dt*(- ( ReactionFlux75 + ReactionFlux77 - ReactionFlux108 + ReactionFlux131 - ReactionFlux132 + ReactionFlux133 + ReactionFlux133 ) ) ;
    pCaMKII_CaM = pCaMKII_CaM - dt*(- ( - ReactionFlux76 + ReactionFlux79 - ReactionFlux110 ) ) ;
    pCaMKII_CaM_Ca2 = pCaMKII_CaM_Ca2 - dt*(- ( - ReactionFlux75 + ReactionFlux76 + ReactionFlux78 - ReactionFlux109 ) ) ;
    pCaMKII_CaM_Ca2_psd = pCaMKII_CaM_Ca2_psd - dt*(- ( - ReactionFlux98 + ReactionFlux99 + ReactionFlux109 + ReactionFlux113 + ReactionFlux115 - ReactionFlux116 ) ) ;
    pCaMKII_CaM_psd = pCaMKII_CaM_psd - dt*(- ( - ReactionFlux96 + ReactionFlux97 + ReactionFlux110 + ReactionFlux114 - ReactionFlux115 ) ) ;
    pCaMKII_CaM_Ca4_psd = pCaMKII_CaM_Ca4_psd - dt*(- ( - ReactionFlux100 + ReactionFlux101 + ReactionFlux108 + ReactionFlux112 + ReactionFlux116 + ReactionFlux135 - ReactionFlux136 + ReactionFlux137 + ReactionFlux137 ) ) ;
    pCaMKII_psd = pCaMKII_psd - dt*(- ( - ReactionFlux93 + ReactionFlux94 + ReactionFlux111 - ReactionFlux112 - ReactionFlux113 - ReactionFlux114 - ReactionFlux117 ) ) ;
    pSubstrate = pSubstrate - dt*(- ( - ReactionFlux91 + ReactionFlux94 + ReactionFlux97 + ReactionFlux99 + ReactionFlux101 + ReactionFlux103 + ReactionFlux105 + ReactionFlux107 ) ) ;
    PDE4 = PDE4 - dt*(- ( - ReactionFlux41 + ReactionFlux42 ) ) ;
    PDE4_cAMP = PDE4_cAMP - dt*(- ( ReactionFlux41 - ReactionFlux42 ) ) ;
    PDE10r = PDE10r - dt*(- ( - ReactionFlux43 + ReactionFlux44 - ReactionFlux45 ) ) ;
    PDE10r_cAMP = PDE10r_cAMP - dt*(- ( - ReactionFlux44 + ReactionFlux45 ) ) ;
    PDE10c = PDE10c - dt*(- ( ReactionFlux43 + ReactionFlux46 - ReactionFlux69 ) ) ;
    PDE10c_cAMP = PDE10c_cAMP - dt*(- ( - ReactionFlux46 + ReactionFlux69 ) ) ;
    PKA = PKA - dt*(- ( - ReactionFlux38 ) ) ;
    PKAc = PKAc - dt*(- ( - ReactionFlux8 + ReactionFlux9 - ReactionFlux10 + ReactionFlux11 - ReactionFlux15 + ReactionFlux40 - ReactionFlux80 + ReactionFlux81 ) ) ;
    PKAc_B56PP2A = PKAc_B56PP2A - dt*(- ( ReactionFlux10 - ReactionFlux11 ) ) ;
    PKAc_D32 = PKAc_D32 - dt*(- ( ReactionFlux8 - ReactionFlux9 ) ) ;
    PKAc_ARPP21 = PKAc_ARPP21 - dt*(- ( ReactionFlux80 - ReactionFlux81 ) ) ;
    PKA_Ca2MP = PKA_Ca2MP - dt*(- ( ReactionFlux38 - ReactionFlux39 ) ) ;
    PKA_Ca4MP = PKA_Ca4MP - dt*(- ( ReactionFlux39 - ReactionFlux40 ) ) ;
    PKAc_D32p75 = PKAc_D32p75 - dt*(- ( ReactionFlux15 ) ) ;
    PKAreg = PKAreg - dt*(- ( ReactionFlux40 ) ) ;
    PP1 = PP1 - dt*(- ( - ReactionFlux12 - ReactionFlux91 + ReactionFlux92 - ReactionFlux117 + ReactionFlux118 ) ) ;
    PP1_pCaMKII_psd = PP1_pCaMKII_psd - dt*(- ( ReactionFlux117 - ReactionFlux118 ) ) ;
    PP1_pSubstrate = PP1_pSubstrate - dt*(- ( ReactionFlux91 - ReactionFlux92 ) ) ;
    PP1_D32p34 = PP1_D32p34 - dt*(- ( ReactionFlux12 ) ) ;
    CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd = CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd - dt*(- ( - ReactionFlux128 + ReactionFlux134 - ReactionFlux135 ) ) ;
    pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd = pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd - dt*(- ( - ReactionFlux129 + ReactionFlux136 - ReactionFlux137 ) ) ;
    CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 = CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 - dt*(- ( ReactionFlux128 + ReactionFlux130 - ReactionFlux131 ) ) ;
    pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 = pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 - dt*(- ( ReactionFlux129 + ReactionFlux132 - ReactionFlux133 ) ) ;
    PP2B = PP2B - dt*(- ( - ReactionFlux6 - ReactionFlux7 - ReactionFlux27 ) ) ;
    PP2Bc = PP2Bc - dt*(- ( ReactionFlux7 - ReactionFlux23 + ReactionFlux26 + ReactionFlux36 ) ) ;
    PP2Bc_D32p34 = PP2Bc_D32p34 - dt*(- ( ReactionFlux23 - ReactionFlux36 ) ) ;
    PP2B_CaM = PP2B_CaM - dt*(- ( ReactionFlux6 - ReactionFlux25 ) ) ;
    PP2B_CaM_Ca2 = PP2B_CaM_Ca2 - dt*(- ( ReactionFlux25 - ReactionFlux26 + ReactionFlux27 ) ) ;
    pARPP21 = pARPP21 - dt*(- ( ReactionFlux81 - ReactionFlux82 - ReactionFlux84 - ReactionFlux86 - ReactionFlux88 - ReactionFlux90 ) ) ;
    ARPP21 = ARPP21 - dt*(- ( - ReactionFlux80 + ReactionFlux83 + ReactionFlux85 + ReactionFlux87 + ReactionFlux89 ) ) ;
    pCaMKII_psd_Substrate = pCaMKII_psd_Substrate - dt*(- ( ReactionFlux93 - ReactionFlux94 ) ) ;
    pCaMKII_CaM_psd_Substrate = pCaMKII_CaM_psd_Substrate - dt*(- ( ReactionFlux96 - ReactionFlux97 ) ) ;
    pCaMKII_CaM_Ca2_psd_Substrate = pCaMKII_CaM_Ca2_psd_Substrate - dt*(- ( ReactionFlux98 - ReactionFlux99 ) ) ;
    pCaMKII_CaM_Ca4_psd_Substrate = pCaMKII_CaM_Ca4_psd_Substrate - dt*(- ( ReactionFlux100 - ReactionFlux101 ) ) ;
    CaMKII_CaM_psd_Substrate = CaMKII_CaM_psd_Substrate - dt*(- ( ReactionFlux102 - ReactionFlux103 ) ) ;
    CaMKII_CaM_Ca2_psd_Substrate = CaMKII_CaM_Ca2_psd_Substrate - dt*(- ( ReactionFlux104 - ReactionFlux105 ) ) ;
    CaMKII_CaM_Ca4_psd_Substrate = CaMKII_CaM_Ca4_psd_Substrate - dt*(- ( ReactionFlux106 - ReactionFlux107 ) ) ;
    total_CaMKII_activated = total_CaMKII_activated - dt*(- ( DpCaMKII_CaM_Ca4_psd + DpCaMKII_CaM_Ca2_psd + DpCaMKII_CaM_psd + DpCaMKII_psd + DCaMKII_CaM_Ca4_psd + DCaMKII_CaM_Ca2_psd + DCaMKII_CaM_Ca4_psd_Substrate + DCaMKII_CaM_psd_Substrate + DCaMKII_CaM_Ca2_psd_Substrate + DpCaMKII_psd_Substrate + DpCaMKII_CaM_psd_Substrate + DpCaMKII_CaM_Ca2_psd_Substrate + DpCaMKII_CaM_Ca4_psd_Substrate ) ) ;
   }
  return 0;
}
 
static int  observables_func ( _threadargsproto_ ) {
   pSubstrate_out = pSubstrate ;
   PP1_out = PP1 ;
   CaM_out = CaM ;
   D32_out = D32 ;
   total_CaMKII_activated_out = total_CaMKII_activated ;
    return 0; }
 
static void _hoc_observables_func(void) {
  double _r;
   double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   if (_extcall_prop) {_p = _extcall_prop->param; _ppvar = _extcall_prop->dparam;}else{ _p = (double*)0; _ppvar = (Datum*)0; }
  _thread = _extcall_thread;
  _nt = nrn_threads;
 _r = 1.;
 observables_func ( _p, _ppvar, _thread, _nt );
 hoc_retpushx(_r);
}
 
static int _ode_count(int _type){ return 96;}
 
static void _ode_spec(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
  cai = _ion_cai;
     _ode_spec1 (_p, _ppvar, _thread, _nt);
 }}
 
static void _ode_map(int _ieq, double** _pv, double** _pvdot, double* _pp, Datum* _ppd, double* _atol, int _type) { 
	double* _p; Datum* _ppvar;
 	int _i; _p = _pp; _ppvar = _ppd;
	_cvode_ieq = _ieq;
	for (_i=0; _i < 96; ++_i) {
		_pv[_i] = _pp + _slist1[_i];  _pvdot[_i] = _pp + _dlist1[_i];
		_cvode_abstol(_atollist, _atol, _i);
	}
 }
 
static void _ode_matsol_instance1(_threadargsproto_) {
 _ode_matsol1 (_p, _ppvar, _thread, _nt);
 }
 
static void _ode_matsol(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
  cai = _ion_cai;
 _ode_matsol_instance1(_threadargs_);
 }}
 extern void nrn_update_ion_pointer(Symbol*, Datum*, int, int);
 static void _update_ion_pointer(Datum* _ppvar) {
   nrn_update_ion_pointer(_ca_sym, _ppvar, 0, 1);
 }

static void initmodel(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
  int _i; double _save;{
  ARPP21 = ARPP210;
  AC5_GaolfGTP_ATP = AC5_GaolfGTP_ATP0;
  AC5_GaolfGTP = AC5_GaolfGTP0;
  AC5_Ca_GaolfGTP_ATP = AC5_Ca_GaolfGTP_ATP0;
  AC5_Ca_GaolfGTP = AC5_Ca_GaolfGTP0;
  AC5_Ca_ATP = AC5_Ca_ATP0;
  AC5_Ca = AC5_Ca0;
  AC5_ATP = AC5_ATP0;
  AC5 = AC50;
  B72PP2A_Ca_pARPP21 = B72PP2A_Ca_pARPP210;
  B72PP2A_Ca = B72PP2A_Ca0;
  B72PP2A_Ca_D32p75 = B72PP2A_Ca_D32p750;
  B72PP2A_Ca_D32p34 = B72PP2A_Ca_D32p340;
  B72PP2A_pARPP21 = B72PP2A_pARPP210;
  B72PP2A_D32p75 = B72PP2A_D32p750;
  B72PP2A_D32p34 = B72PP2A_D32p340;
  B72PP2A = B72PP2A0;
  B56PP2Ap_pARPP21 = B56PP2Ap_pARPP210;
  B56PP2Ap_D32p75 = B56PP2Ap_D32p750;
  B56PP2Ap = B56PP2Ap0;
  B56PP2A_pARPP21 = B56PP2A_pARPP210;
  B56PP2A_D32p75 = B56PP2A_D32p750;
  B56PP2A = B56PP2A0;
  CaMKII_CaM_Ca4_psd_Substrate = CaMKII_CaM_Ca4_psd_Substrate0;
  CaMKII_CaM_Ca2_psd_Substrate = CaMKII_CaM_Ca2_psd_Substrate0;
  CaMKII_CaM_psd_Substrate = CaMKII_CaM_psd_Substrate0;
  CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 = CaMKII_CaM_Ca4_CaMKII_CaM_Ca40;
  CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd = CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd0;
  CDK5_D32 = CDK5_D320;
  CDK5 = CDK50;
  CaMKII_psd = CaMKII_psd0;
  CaMKII_CaM_Ca4_psd = CaMKII_CaM_Ca4_psd0;
  CaMKII_CaM_psd = CaMKII_CaM_psd0;
  CaMKII_CaM_Ca2_psd = CaMKII_CaM_Ca2_psd0;
  CaMKII_CaM_Ca2 = CaMKII_CaM_Ca20;
  CaMKII_CaM = CaMKII_CaM0;
  CaMKII_CaM_Ca4 = CaMKII_CaM_Ca40;
  CaMKII = CaMKII0;
  CaM_Ca4_pARPP21 = CaM_Ca4_pARPP210;
  CaM_Ca4 = CaM_Ca40;
  CaM_Ca2 = CaM_Ca20;
  CaM = CaM0;
  D32 = D320;
  D32p75 = D32p750;
  D32p34 = D32p340;
  D1R_Golf = D1R_Golf0;
  D1R_Golf_DA = D1R_Golf_DA0;
  D1R_DA = D1R_DA0;
  D1R = D1R0;
  Golf = Golf0;
  Gbgolf = Gbgolf0;
  GaolfGTP = GaolfGTP0;
  GaolfGDP = GaolfGDP0;
  PP2B_CaM_Ca2 = PP2B_CaM_Ca20;
  PP2B_CaM = PP2B_CaM0;
  PP2Bc_D32p34 = PP2Bc_D32p340;
  PP2Bc = PP2Bc0;
  PP2B = PP2B0;
  PP1_D32p34 = PP1_D32p340;
  PP1_pSubstrate = PP1_pSubstrate0;
  PP1_pCaMKII_psd = PP1_pCaMKII_psd0;
  PP1 = PP10;
  PKAreg = PKAreg0;
  PKAc_D32p75 = PKAc_D32p750;
  PKA_Ca4MP = PKA_Ca4MP0;
  PKA_Ca2MP = PKA_Ca2MP0;
  PKAc_ARPP21 = PKAc_ARPP210;
  PKAc_D32 = PKAc_D320;
  PKAc_B56PP2A = PKAc_B56PP2A0;
  PKAc = PKAc0;
  PKA = PKA0;
  PDE10c_cAMP = PDE10c_cAMP0;
  PDE10c = PDE10c0;
  PDE10r_cAMP = PDE10r_cAMP0;
  PDE10r = PDE10r0;
  PDE4_cAMP = PDE4_cAMP0;
  PDE4 = PDE40;
  Substrate = Substrate0;
  cAMP = cAMP0;
  pCaMKII_CaM_Ca4_psd_Substrate = pCaMKII_CaM_Ca4_psd_Substrate0;
  pCaMKII_CaM_Ca2_psd_Substrate = pCaMKII_CaM_Ca2_psd_Substrate0;
  pCaMKII_CaM_psd_Substrate = pCaMKII_CaM_psd_Substrate0;
  pCaMKII_psd_Substrate = pCaMKII_psd_Substrate0;
  pARPP21 = pARPP210;
  pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 = pCaMKII_CaM_Ca4_CaMKII_CaM_Ca40;
  pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd = pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd0;
  pSubstrate = pSubstrate0;
  pCaMKII_psd = pCaMKII_psd0;
  pCaMKII_CaM_Ca4_psd = pCaMKII_CaM_Ca4_psd0;
  pCaMKII_CaM_psd = pCaMKII_CaM_psd0;
  pCaMKII_CaM_Ca2_psd = pCaMKII_CaM_Ca2_psd0;
  pCaMKII_CaM_Ca2 = pCaMKII_CaM_Ca20;
  pCaMKII_CaM = pCaMKII_CaM0;
  pCaMKII_CaM_Ca4 = pCaMKII_CaM_Ca40;
  pCaMKII = pCaMKII0;
  total_CaMKII_activated = total_CaMKII_activated0;
 {
   AC5 = 2.6579740648536387 ;
   AC5_ATP = 664.5955722158345 ;
   AC5_Ca = 0.011455491216440293 ;
   AC5_Ca_ATP = 2.8642831776146602 ;
   AC5_Ca_GaolfGTP = 0.0005087730491145609 ;
   AC5_Ca_GaolfGTP_ATP = 0.1276760000022537 ;
   AC5_GaolfGTP = 0.11762328938669141 ;
   AC5_GaolfGTP_ATP = 29.624906977591287 ;
   B56PP2A = 891.3882782297828 ;
   B56PP2A_D32p75 = 773.8986890359638 ;
   B56PP2A_pARPP21 = 22.004569833130333 ;
   B56PP2Ap = 119.83225503696232 ;
   B56PP2Ap_D32p75 = 183.32968907852563 ;
   B56PP2Ap_pARPP21 = 4.752784515174912 ;
   B72PP2A = 998.1762288155527 ;
   B72PP2A_D32p34 = 0.029586434857564403 ;
   B72PP2A_D32p75 = 866.6114349644631 ;
   B72PP2A_pARPP21 = 24.640708285240002 ;
   B72PP2A_Ca_D32p34 = 0.001275120308719799 ;
   B72PP2A_Ca_D32p75 = 65.81498998111533 ;
   B72PP2A_Ca = 43.01953875726838 ;
   B72PP2A_Ca_pARPP21 = 1.706240090303376 ;
   CaM = 3271.1613030579483 ;
   CaM_Ca2 = 42.30197029468885 ;
   CaM_Ca4 = 0.18232282358259608 ;
   CaM_Ca4_pARPP21 = 5.682096670017442 ;
   CaMKII = 16861.31022167976 ;
   CaMKII_CaM_Ca4 = 7.653695787280561 ;
   CaMKII_CaM = 1378.7438408069913 ;
   CaMKII_CaM_Ca2 = 178.1085180682959 ;
   CaMKII_CaM_Ca2_psd = 15.344587294726768 ;
   CaMKII_CaM_psd = 117.20636345254225 ;
   CaMKII_CaM_Ca4_psd = 0.6836514096472648 ;
   CaMKII_psd = 1431.2784425994976 ;
   cAMP = 38.077478703814286 ;
   Substrate = 2898.4324981645364 ;
   CDK5 = 1354.5983328435307 ;
   CDK5_D32 = 445.4016679783238 ;
   D1R = 1476.965276006024 ;
   D1R_DA = 5.959513286613785 ;
   D1R_Golf_DA = 2.0091697499991463 ;
   D1R_Golf = 515.0660409549953 ;
   D32p34 = 0.23709844962796384 ;
   D32p75 = 11014.977244009184 ;
   D32 = 36168.79062206558 ;
   GaolfGDP = 0.010083118413574194 ;
   GaolfGTP = 0.008914911110695258 ;
   Gbgolf = 29.889710469343125 ;
   Golf = 1453.0350762349071 ;
   pCaMKII = 0.0026152322826163694 ;
   pCaMKII_CaM_Ca4 = 0.00041326366874510956 ;
   pCaMKII_CaM = 0.0021363473128570283 ;
   pCaMKII_CaM_Ca2 = 0.0003364074902532764 ;
   pCaMKII_CaM_Ca2_psd = 0.00029964701372417826 ;
   pCaMKII_CaM_psd = 0.00223880855203415 ;
   pCaMKII_CaM_Ca4_psd = 0.00015640795348060934 ;
   pCaMKII_psd = 0.002734310759402372 ;
   pSubstrate = 82.25679040587481 ;
   PDE4 = 1507.8595078954654 ;
   PDE4_cAMP = 492.1404908824553 ;
   PDE10r = 396.93707251699345 ;
   PDE10r_cAMP = 302.30479218857784 ;
   PDE10c = 0.5755168324209912 ;
   PDE10c_cAMP = 0.1826207133266763 ;
   PKA = 1143.825553233938 ;
   PKAc = 2.6887584775003255 ;
   PKAc_B56PP2A = 4.793733616212578 ;
   PKAc_D32 = 4.630911543143565 ;
   PKAc_ARPP21 = 11.123552417073366 ;
   PKA_Ca2MP = 3.235620105419139 ;
   PKA_Ca4MP = 0.08525605875534487 ;
   PKAc_D32p75 = 29.616613444303574 ;
   PKAreg = 52.85356959978496 ;
   PP1 = 2582.1938739416964 ;
   PP1_pCaMKII_psd = 0.0028242717416327636 ;
   PP1_pSubstrate = 9.655356749304744 ;
   PP1_D32p34 = 408.14794647416636 ;
   CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd = 2.019451923560302e-05 ;
   pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd = 1.1773379671332063e-11 ;
   CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 = 0.0007700483148596818 ;
   pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 = 3.4773054620114007e-10 ;
   PP2B = 26.730674733834796 ;
   PP2Bc = 162.45364687157698 ;
   PP2Bc_D32p34 = 38.512174821299965 ;
   PP2B_CaM = 2.9146880204369956 ;
   PP2B_CaM_Ca2 = 3769.3888179670294 ;
   pARPP21 = 623.2570162577764 ;
   ARPP21 = 19306.833014960313 ;
   pCaMKII_psd_Substrate = 0.00019814424825483155 ;
   pCaMKII_CaM_psd_Substrate = 0.00016223724242164732 ;
   pCaMKII_CaM_Ca2_psd_Substrate = 2.1714185950523916e-05 ;
   pCaMKII_CaM_Ca4_psd_Substrate = 1.133424072480528e-05 ;
   CaMKII_CaM_psd_Substrate = 8.493462821347531 ;
   CaMKII_CaM_Ca2_psd_Substrate = 1.11195909383754 ;
   CaMKII_CaM_Ca4_psd_Substrate = 0.04954140423400814 ;
   total_CaMKII_activated = pCaMKII_CaM_Ca4_psd + pCaMKII_CaM_Ca2_psd + pCaMKII_CaM_psd + pCaMKII_psd + CaMKII_CaM_Ca4_psd + CaMKII_CaM_Ca2_psd + CaMKII_CaM_Ca4_psd_Substrate + CaMKII_CaM_psd_Substrate + CaMKII_CaM_Ca2_psd_Substrate + pCaMKII_psd_Substrate + pCaMKII_CaM_psd_Substrate + pCaMKII_CaM_Ca2_psd_Substrate + pCaMKII_CaM_Ca4_psd_Substrate ;
   }
 
}
}

static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v = _v;
  cai = _ion_cai;
 initmodel(_p, _ppvar, _thread, _nt);
}
}

static double _nrn_current(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, double _v){double _current=0.;v=_v;{
} return _current;
}

static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; double _rhs, _v; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 
}
 
}

static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml];
#if CACHEVEC
  if (use_cachevec) {
	VEC_D(_ni[_iml]) += _g;
  }else
#endif
  {
     _nd = _ml->_nodelist[_iml];
	NODED(_nd) += _g;
  }
 
}
 
}

static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v = 0.0; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
 _nd = _ml->_nodelist[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v=_v;
{
  cai = _ion_cai;
 {   ode(_p, _ppvar, _thread, _nt);
  } {
   assign_calculated_values ( _threadargs_ ) ;
   }
}}

}

static void terminal(){}

static void _initlists(){
 double _x; double* _p = &_x;
 int _i; static int _first = 1;
  if (!_first) return;
 _slist1[0] = &(AC5) - _p;  _dlist1[0] = &(DAC5) - _p;
 _slist1[1] = &(AC5_ATP) - _p;  _dlist1[1] = &(DAC5_ATP) - _p;
 _slist1[2] = &(AC5_Ca) - _p;  _dlist1[2] = &(DAC5_Ca) - _p;
 _slist1[3] = &(AC5_Ca_ATP) - _p;  _dlist1[3] = &(DAC5_Ca_ATP) - _p;
 _slist1[4] = &(AC5_Ca_GaolfGTP) - _p;  _dlist1[4] = &(DAC5_Ca_GaolfGTP) - _p;
 _slist1[5] = &(AC5_Ca_GaolfGTP_ATP) - _p;  _dlist1[5] = &(DAC5_Ca_GaolfGTP_ATP) - _p;
 _slist1[6] = &(AC5_GaolfGTP) - _p;  _dlist1[6] = &(DAC5_GaolfGTP) - _p;
 _slist1[7] = &(AC5_GaolfGTP_ATP) - _p;  _dlist1[7] = &(DAC5_GaolfGTP_ATP) - _p;
 _slist1[8] = &(B56PP2A) - _p;  _dlist1[8] = &(DB56PP2A) - _p;
 _slist1[9] = &(B56PP2A_D32p75) - _p;  _dlist1[9] = &(DB56PP2A_D32p75) - _p;
 _slist1[10] = &(B56PP2A_pARPP21) - _p;  _dlist1[10] = &(DB56PP2A_pARPP21) - _p;
 _slist1[11] = &(B56PP2Ap) - _p;  _dlist1[11] = &(DB56PP2Ap) - _p;
 _slist1[12] = &(B56PP2Ap_D32p75) - _p;  _dlist1[12] = &(DB56PP2Ap_D32p75) - _p;
 _slist1[13] = &(B56PP2Ap_pARPP21) - _p;  _dlist1[13] = &(DB56PP2Ap_pARPP21) - _p;
 _slist1[14] = &(B72PP2A) - _p;  _dlist1[14] = &(DB72PP2A) - _p;
 _slist1[15] = &(B72PP2A_D32p34) - _p;  _dlist1[15] = &(DB72PP2A_D32p34) - _p;
 _slist1[16] = &(B72PP2A_D32p75) - _p;  _dlist1[16] = &(DB72PP2A_D32p75) - _p;
 _slist1[17] = &(B72PP2A_pARPP21) - _p;  _dlist1[17] = &(DB72PP2A_pARPP21) - _p;
 _slist1[18] = &(B72PP2A_Ca_D32p34) - _p;  _dlist1[18] = &(DB72PP2A_Ca_D32p34) - _p;
 _slist1[19] = &(B72PP2A_Ca_D32p75) - _p;  _dlist1[19] = &(DB72PP2A_Ca_D32p75) - _p;
 _slist1[20] = &(B72PP2A_Ca) - _p;  _dlist1[20] = &(DB72PP2A_Ca) - _p;
 _slist1[21] = &(B72PP2A_Ca_pARPP21) - _p;  _dlist1[21] = &(DB72PP2A_Ca_pARPP21) - _p;
 _slist1[22] = &(CaM) - _p;  _dlist1[22] = &(DCaM) - _p;
 _slist1[23] = &(CaM_Ca2) - _p;  _dlist1[23] = &(DCaM_Ca2) - _p;
 _slist1[24] = &(CaM_Ca4) - _p;  _dlist1[24] = &(DCaM_Ca4) - _p;
 _slist1[25] = &(CaM_Ca4_pARPP21) - _p;  _dlist1[25] = &(DCaM_Ca4_pARPP21) - _p;
 _slist1[26] = &(CaMKII) - _p;  _dlist1[26] = &(DCaMKII) - _p;
 _slist1[27] = &(CaMKII_CaM_Ca4) - _p;  _dlist1[27] = &(DCaMKII_CaM_Ca4) - _p;
 _slist1[28] = &(CaMKII_CaM) - _p;  _dlist1[28] = &(DCaMKII_CaM) - _p;
 _slist1[29] = &(CaMKII_CaM_Ca2) - _p;  _dlist1[29] = &(DCaMKII_CaM_Ca2) - _p;
 _slist1[30] = &(CaMKII_CaM_Ca2_psd) - _p;  _dlist1[30] = &(DCaMKII_CaM_Ca2_psd) - _p;
 _slist1[31] = &(CaMKII_CaM_psd) - _p;  _dlist1[31] = &(DCaMKII_CaM_psd) - _p;
 _slist1[32] = &(CaMKII_CaM_Ca4_psd) - _p;  _dlist1[32] = &(DCaMKII_CaM_Ca4_psd) - _p;
 _slist1[33] = &(CaMKII_psd) - _p;  _dlist1[33] = &(DCaMKII_psd) - _p;
 _slist1[34] = &(cAMP) - _p;  _dlist1[34] = &(DcAMP) - _p;
 _slist1[35] = &(Substrate) - _p;  _dlist1[35] = &(DSubstrate) - _p;
 _slist1[36] = &(CDK5) - _p;  _dlist1[36] = &(DCDK5) - _p;
 _slist1[37] = &(CDK5_D32) - _p;  _dlist1[37] = &(DCDK5_D32) - _p;
 _slist1[38] = &(D1R) - _p;  _dlist1[38] = &(DD1R) - _p;
 _slist1[39] = &(D1R_DA) - _p;  _dlist1[39] = &(DD1R_DA) - _p;
 _slist1[40] = &(D1R_Golf_DA) - _p;  _dlist1[40] = &(DD1R_Golf_DA) - _p;
 _slist1[41] = &(D1R_Golf) - _p;  _dlist1[41] = &(DD1R_Golf) - _p;
 _slist1[42] = &(D32p34) - _p;  _dlist1[42] = &(DD32p34) - _p;
 _slist1[43] = &(D32p75) - _p;  _dlist1[43] = &(DD32p75) - _p;
 _slist1[44] = &(D32) - _p;  _dlist1[44] = &(DD32) - _p;
 _slist1[45] = &(GaolfGDP) - _p;  _dlist1[45] = &(DGaolfGDP) - _p;
 _slist1[46] = &(GaolfGTP) - _p;  _dlist1[46] = &(DGaolfGTP) - _p;
 _slist1[47] = &(Gbgolf) - _p;  _dlist1[47] = &(DGbgolf) - _p;
 _slist1[48] = &(Golf) - _p;  _dlist1[48] = &(DGolf) - _p;
 _slist1[49] = &(pCaMKII) - _p;  _dlist1[49] = &(DpCaMKII) - _p;
 _slist1[50] = &(pCaMKII_CaM_Ca4) - _p;  _dlist1[50] = &(DpCaMKII_CaM_Ca4) - _p;
 _slist1[51] = &(pCaMKII_CaM) - _p;  _dlist1[51] = &(DpCaMKII_CaM) - _p;
 _slist1[52] = &(pCaMKII_CaM_Ca2) - _p;  _dlist1[52] = &(DpCaMKII_CaM_Ca2) - _p;
 _slist1[53] = &(pCaMKII_CaM_Ca2_psd) - _p;  _dlist1[53] = &(DpCaMKII_CaM_Ca2_psd) - _p;
 _slist1[54] = &(pCaMKII_CaM_psd) - _p;  _dlist1[54] = &(DpCaMKII_CaM_psd) - _p;
 _slist1[55] = &(pCaMKII_CaM_Ca4_psd) - _p;  _dlist1[55] = &(DpCaMKII_CaM_Ca4_psd) - _p;
 _slist1[56] = &(pCaMKII_psd) - _p;  _dlist1[56] = &(DpCaMKII_psd) - _p;
 _slist1[57] = &(pSubstrate) - _p;  _dlist1[57] = &(DpSubstrate) - _p;
 _slist1[58] = &(PDE4) - _p;  _dlist1[58] = &(DPDE4) - _p;
 _slist1[59] = &(PDE4_cAMP) - _p;  _dlist1[59] = &(DPDE4_cAMP) - _p;
 _slist1[60] = &(PDE10r) - _p;  _dlist1[60] = &(DPDE10r) - _p;
 _slist1[61] = &(PDE10r_cAMP) - _p;  _dlist1[61] = &(DPDE10r_cAMP) - _p;
 _slist1[62] = &(PDE10c) - _p;  _dlist1[62] = &(DPDE10c) - _p;
 _slist1[63] = &(PDE10c_cAMP) - _p;  _dlist1[63] = &(DPDE10c_cAMP) - _p;
 _slist1[64] = &(PKA) - _p;  _dlist1[64] = &(DPKA) - _p;
 _slist1[65] = &(PKAc) - _p;  _dlist1[65] = &(DPKAc) - _p;
 _slist1[66] = &(PKAc_B56PP2A) - _p;  _dlist1[66] = &(DPKAc_B56PP2A) - _p;
 _slist1[67] = &(PKAc_D32) - _p;  _dlist1[67] = &(DPKAc_D32) - _p;
 _slist1[68] = &(PKAc_ARPP21) - _p;  _dlist1[68] = &(DPKAc_ARPP21) - _p;
 _slist1[69] = &(PKA_Ca2MP) - _p;  _dlist1[69] = &(DPKA_Ca2MP) - _p;
 _slist1[70] = &(PKA_Ca4MP) - _p;  _dlist1[70] = &(DPKA_Ca4MP) - _p;
 _slist1[71] = &(PKAc_D32p75) - _p;  _dlist1[71] = &(DPKAc_D32p75) - _p;
 _slist1[72] = &(PKAreg) - _p;  _dlist1[72] = &(DPKAreg) - _p;
 _slist1[73] = &(PP1) - _p;  _dlist1[73] = &(DPP1) - _p;
 _slist1[74] = &(PP1_pCaMKII_psd) - _p;  _dlist1[74] = &(DPP1_pCaMKII_psd) - _p;
 _slist1[75] = &(PP1_pSubstrate) - _p;  _dlist1[75] = &(DPP1_pSubstrate) - _p;
 _slist1[76] = &(PP1_D32p34) - _p;  _dlist1[76] = &(DPP1_D32p34) - _p;
 _slist1[77] = &(CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd) - _p;  _dlist1[77] = &(DCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd) - _p;
 _slist1[78] = &(pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd) - _p;  _dlist1[78] = &(DpCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd) - _p;
 _slist1[79] = &(CaMKII_CaM_Ca4_CaMKII_CaM_Ca4) - _p;  _dlist1[79] = &(DCaMKII_CaM_Ca4_CaMKII_CaM_Ca4) - _p;
 _slist1[80] = &(pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4) - _p;  _dlist1[80] = &(DpCaMKII_CaM_Ca4_CaMKII_CaM_Ca4) - _p;
 _slist1[81] = &(PP2B) - _p;  _dlist1[81] = &(DPP2B) - _p;
 _slist1[82] = &(PP2Bc) - _p;  _dlist1[82] = &(DPP2Bc) - _p;
 _slist1[83] = &(PP2Bc_D32p34) - _p;  _dlist1[83] = &(DPP2Bc_D32p34) - _p;
 _slist1[84] = &(PP2B_CaM) - _p;  _dlist1[84] = &(DPP2B_CaM) - _p;
 _slist1[85] = &(PP2B_CaM_Ca2) - _p;  _dlist1[85] = &(DPP2B_CaM_Ca2) - _p;
 _slist1[86] = &(pARPP21) - _p;  _dlist1[86] = &(DpARPP21) - _p;
 _slist1[87] = &(ARPP21) - _p;  _dlist1[87] = &(DARPP21) - _p;
 _slist1[88] = &(pCaMKII_psd_Substrate) - _p;  _dlist1[88] = &(DpCaMKII_psd_Substrate) - _p;
 _slist1[89] = &(pCaMKII_CaM_psd_Substrate) - _p;  _dlist1[89] = &(DpCaMKII_CaM_psd_Substrate) - _p;
 _slist1[90] = &(pCaMKII_CaM_Ca2_psd_Substrate) - _p;  _dlist1[90] = &(DpCaMKII_CaM_Ca2_psd_Substrate) - _p;
 _slist1[91] = &(pCaMKII_CaM_Ca4_psd_Substrate) - _p;  _dlist1[91] = &(DpCaMKII_CaM_Ca4_psd_Substrate) - _p;
 _slist1[92] = &(CaMKII_CaM_psd_Substrate) - _p;  _dlist1[92] = &(DCaMKII_CaM_psd_Substrate) - _p;
 _slist1[93] = &(CaMKII_CaM_Ca2_psd_Substrate) - _p;  _dlist1[93] = &(DCaMKII_CaM_Ca2_psd_Substrate) - _p;
 _slist1[94] = &(CaMKII_CaM_Ca4_psd_Substrate) - _p;  _dlist1[94] = &(DCaMKII_CaM_Ca4_psd_Substrate) - _p;
 _slist1[95] = &(total_CaMKII_activated) - _p;  _dlist1[95] = &(Dtotal_CaMKII_activated) - _p;
_first = 0;
}

#if defined(__cplusplus)
} /* extern "C" */
#endif

#if NMODL_TEXT
static const char* nmodl_filename = "/home/mohacsi/Desktop/optimizer/optimizer/new_test_files/Luca_modell_new/D1_LTP_time_window_Luca_cai_initials.mod";
static const char* nmodl_file_text = 
  "TITLE D1_LTP_time_window\n"
  "COMMENT\n"
  "	automatically generated from an SBtab file\n"
  "	date: Fri Apr 03 16:29:37 2020\n"
  "ENDCOMMENT\n"
  "NEURON {\n"
  "	SUFFIX D1_LTP_time_window_Luca_cai_initials : OR perhaps POINT_PROCESS ?\n"
  "	RANGE DA_start, DA_max : input\n"
  "	RANGE pSubstrate_out, PP1_out, CaM_out, D32_out, total_CaMKII_activated_out : output\n"
  "	RANGE ATP_expression : assigned\n"
  "	RANGE Ca_expression : assigned\n"
  "	RANGE DA_expression : assigned\n"
  "	RANGE AMP : assigned\n"
  "	RANGE ATP : assigned\n"
  "	RANGE Ca : assigned\n"
  "	RANGE DA : assigned\n"
  "	RANGE AC5 : compound\n"
  "	RANGE AC5_ATP : compound\n"
  "	RANGE AC5_Ca : compound\n"
  "	RANGE AC5_Ca_ATP : compound\n"
  "	RANGE AC5_Ca_GaolfGTP : compound\n"
  "	RANGE AC5_Ca_GaolfGTP_ATP : compound\n"
  "	RANGE AC5_GaolfGTP : compound\n"
  "	RANGE AC5_GaolfGTP_ATP : compound\n"
  "	RANGE B56PP2A : compound\n"
  "	RANGE B56PP2A_D32p75 : compound\n"
  "	RANGE B56PP2A_pARPP21 : compound\n"
  "	RANGE B56PP2Ap : compound\n"
  "	RANGE B56PP2Ap_D32p75 : compound\n"
  "	RANGE B56PP2Ap_pARPP21 : compound\n"
  "	RANGE B72PP2A : compound\n"
  "	RANGE B72PP2A_D32p34 : compound\n"
  "	RANGE B72PP2A_D32p75 : compound\n"
  "	RANGE B72PP2A_pARPP21 : compound\n"
  "	RANGE B72PP2A_Ca_D32p34 : compound\n"
  "	RANGE B72PP2A_Ca_D32p75 : compound\n"
  "	RANGE B72PP2A_Ca : compound\n"
  "	RANGE B72PP2A_Ca_pARPP21 : compound\n"
  "	RANGE CaM : compound\n"
  "	RANGE CaM_Ca2 : compound\n"
  "	RANGE CaM_Ca4 : compound\n"
  "	RANGE CaM_Ca4_pARPP21 : compound\n"
  "	RANGE CaMKII : compound\n"
  "	RANGE CaMKII_CaM_Ca4 : compound\n"
  "	RANGE CaMKII_CaM : compound\n"
  "	RANGE CaMKII_CaM_Ca2 : compound\n"
  "	RANGE CaMKII_CaM_Ca2_psd : compound\n"
  "	RANGE CaMKII_CaM_psd : compound\n"
  "	RANGE CaMKII_CaM_Ca4_psd : compound\n"
  "	RANGE CaMKII_psd : compound\n"
  "	RANGE cAMP : compound\n"
  "	RANGE Substrate : compound\n"
  "	RANGE CDK5 : compound\n"
  "	RANGE CDK5_D32 : compound\n"
  "	RANGE D1R : compound\n"
  "	RANGE D1R_DA : compound\n"
  "	RANGE D1R_Golf_DA : compound\n"
  "	RANGE D1R_Golf : compound\n"
  "	RANGE D32p34 : compound\n"
  "	RANGE D32p75 : compound\n"
  "	RANGE D32 : compound\n"
  "	RANGE GaolfGDP : compound\n"
  "	RANGE GaolfGTP : compound\n"
  "	RANGE Gbgolf : compound\n"
  "	RANGE Golf : compound\n"
  "	RANGE pCaMKII : compound\n"
  "	RANGE pCaMKII_CaM_Ca4 : compound\n"
  "	RANGE pCaMKII_CaM : compound\n"
  "	RANGE pCaMKII_CaM_Ca2 : compound\n"
  "	RANGE pCaMKII_CaM_Ca2_psd : compound\n"
  "	RANGE pCaMKII_CaM_psd : compound\n"
  "	RANGE pCaMKII_CaM_Ca4_psd : compound\n"
  "	RANGE pCaMKII_psd : compound\n"
  "	RANGE pSubstrate : compound\n"
  "	RANGE PDE4 : compound\n"
  "	RANGE PDE4_cAMP : compound\n"
  "	RANGE PDE10r : compound\n"
  "	RANGE PDE10r_cAMP : compound\n"
  "	RANGE PDE10c : compound\n"
  "	RANGE PDE10c_cAMP : compound\n"
  "	RANGE PKA : compound\n"
  "	RANGE PKAc : compound\n"
  "	RANGE PKAc_B56PP2A : compound\n"
  "	RANGE PKAc_D32 : compound\n"
  "	RANGE PKAc_ARPP21 : compound\n"
  "	RANGE PKA_Ca2MP : compound\n"
  "	RANGE PKA_Ca4MP : compound\n"
  "	RANGE PKAc_D32p75 : compound\n"
  "	RANGE PKAreg : compound\n"
  "	RANGE PP1 : compound\n"
  "	RANGE PP1_pCaMKII_psd : compound\n"
  "	RANGE PP1_pSubstrate : compound\n"
  "	RANGE PP1_D32p34 : compound\n"
  "	RANGE CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd : compound\n"
  "	RANGE pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd : compound\n"
  "	RANGE CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : compound\n"
  "	RANGE pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : compound\n"
  "	RANGE PP2B : compound\n"
  "	RANGE PP2Bc : compound\n"
  "	RANGE PP2Bc_D32p34 : compound\n"
  "	RANGE PP2B_CaM : compound\n"
  "	RANGE PP2B_CaM_Ca2 : compound\n"
  "	RANGE pARPP21 : compound\n"
  "	RANGE ARPP21 : compound\n"
  "	RANGE pCaMKII_psd_Substrate : compound\n"
  "	RANGE pCaMKII_CaM_psd_Substrate : compound\n"
  "	RANGE pCaMKII_CaM_Ca2_psd_Substrate : compound\n"
  "	RANGE pCaMKII_CaM_Ca4_psd_Substrate : compound\n"
  "	RANGE CaMKII_CaM_psd_Substrate : compound\n"
  "	RANGE CaMKII_CaM_Ca2_psd_Substrate : compound\n"
  "	RANGE CaMKII_CaM_Ca4_psd_Substrate : compound\n"
  "	RANGE total_CaMKII_activated : compound\n"
  "        USEION ca READ cai VALENCE 2 : sth. like this may be needed for ions you have in your model\n"
  "}\n"
  "CONSTANT {\n"
  "	tau_DA1 = 34.979 (millisecond) : a constant\n"
  "	tau_DA2 = 420 (millisecond) : a constant\n"
  "	DA_basal = 20 (nanomole/liter) : a constant\n"
  "	Ca_basal = 60 (nanomole/liter) : a constant\n"
  "}\n"
  "PARAMETER {\n"
  "	kf_R0 = 0.0299985 (/millisecond): a kinetic parameter\n"
  "	kf_R1 = 0.0150003 (/millisecond): a kinetic parameter\n"
  "	kf_R2 = 5.00035e-05 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R2 = 0.25 (/millisecond): a kinetic parameter\n"
  "	kf_R3 = 5.00035e-05 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R3 = 0.25 (/millisecond): a kinetic parameter\n"
  "	kf_R4 = 0.01 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R4 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R5 = 6.00067e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R5 = 0.0199986 (/millisecond): a kinetic parameter\n"
  "	kf_R6 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R6 = 2.99999 (/millisecond): a kinetic parameter\n"
  "	kf_R7 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R7 = 2.99985e-06 (/millisecond): a kinetic parameter\n"
  "	kf_R8 = 1e-05 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R8 = 0.2 (/millisecond): a kinetic parameter\n"
  "	kf_R9 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R10 = 1e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R10 = 0.000299985 (/millisecond): a kinetic parameter\n"
  "	kf_R11 = 0.000199986 (/millisecond): a kinetic parameter\n"
  "	kf_R12 = 0.001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R12 = 0.00150003 (/millisecond): a kinetic parameter\n"
  "	kf_R13 = 1e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R13 = 0.1 (/millisecond): a kinetic parameter\n"
  "	kf_R14 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R15 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R15 = 0.1 (/millisecond): a kinetic parameter\n"
  "	kf_R16 = 1e-05 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R16 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R17 = 1.50003e-05 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R17 = 0.1 (/millisecond): a kinetic parameter\n"
  "	kf_R18 = 8.00018e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R18 = 0.1 (/millisecond): a kinetic parameter\n"
  "	kf_R19 = 1.50003e-05 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R19 = 0.1 (/millisecond): a kinetic parameter\n"
  "	kf_R20 = 0.00800018 (/millisecond): a kinetic parameter\n"
  "	kf_R21 = 0.00150003 (/millisecond): a kinetic parameter\n"
  "	kf_R22 = 0.00800018 (/millisecond): a kinetic parameter\n"
  "	kf_R23 = 0.00129987 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R23 = 0.0001 (/millisecond): a kinetic parameter\n"
  "	kf_R24 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R24 = 1 (/millisecond): a kinetic parameter\n"
  "	kf_R25 = 6.00067e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R25 = 1.99986e-07 (/millisecond): a kinetic parameter\n"
  "	kf_R26 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R26 = 0.1 (/millisecond): a kinetic parameter\n"
  "	kf_R27 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R27 = 2.99985e-05 (/millisecond): a kinetic parameter\n"
  "	kf_R28 = 1e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R28 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R29 = 0.01 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R29 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R30 = 8.00018e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R30 = 0.1 (/millisecond): a kinetic parameter\n"
  "	kf_R31 = 0.00150003 (/millisecond): a kinetic parameter\n"
  "	kf_R32 = 0.00299985 (/millisecond): a kinetic parameter\n"
  "	kf_R33 = 0.00299985 (/millisecond): a kinetic parameter\n"
  "	kf_R34 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R34 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R35 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R35 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R36 = 0.00120005 (/millisecond): a kinetic parameter\n"
  "	kf_R37 = 8.00018e-06 (/millisecond): a kinetic parameter\n"
  "	kf_R38 = 2.60016e-05 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R38 = 0.350002 (/millisecond): a kinetic parameter\n"
  "	kf_R39 = 3.46019e-05 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R39 = 0.0500035 (/millisecond): a kinetic parameter\n"
  "	kf_R40 = 0.0500035 (/millisecond): a kinetic parameter\n"
  "	kr_R40 = 2.99985e-05 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kf_R41 = 2.99985e-05 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R41 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R42 = 0.00249977 (/millisecond): a kinetic parameter\n"
  "	kf_R43 = 1e-09 (/nanomole/liter^2-millisecond): a kinetic parameter\n"
  "	kr_R43 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R44 = 0.00299985 (/millisecond): a kinetic parameter\n"
  "	kf_R45 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R45 = 0.00199986 (/millisecond): a kinetic parameter\n"
  "	kf_R46 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R47 = 0.1 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kf_R48 = 2.54976e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R48 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R49 = 1e-07 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R49 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R50 = 7.50067e-08 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R50 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R51 = 1.29987e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R51 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R52 = 0.01 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R52 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R53 = 0.01 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R53 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R54 = 1e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R54 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R55 = 0.0500035 (/millisecond): a kinetic parameter\n"
  "	kf_R56 = 0.00254976 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kf_R57 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R58 = 1.99986e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kf_R59 = 0.000500035 (/millisecond): a kinetic parameter\n"
  "	kf_R60 = 7.50067e-07 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kf_R61 = 0.0249977 (/millisecond): a kinetic parameter\n"
  "	kf_R62 = 0.00064998 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kf_R63 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R64 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R65 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R66 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R67 = 6.00067e-05 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R67 = 0.25 (/millisecond): a kinetic parameter\n"
  "	kf_R68 = 6.00067e-05 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R68 = 0.25 (/millisecond): a kinetic parameter\n"
  "	kf_R69 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R69 = 0.00199986 (/millisecond): a kinetic parameter\n"
  "	kf_R70 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R70 = 0.0400037 (/millisecond): a kinetic parameter\n"
  "	kf_R71 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R71 = 0.4 (/millisecond): a kinetic parameter\n"
  "	kf_R72 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R72 = 4 (/millisecond): a kinetic parameter\n"
  "	kf_R73 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R73 = 0.1 (/millisecond): a kinetic parameter\n"
  "	kf_R74 = 6.00067e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R74 = 0.00199986 (/millisecond): a kinetic parameter\n"
  "	kf_R75 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R75 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R76 = 6.00067e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R76 = 0.00199986 (/millisecond): a kinetic parameter\n"
  "	kf_R77 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R77 = 0.000400037 (/millisecond): a kinetic parameter\n"
  "	kf_R78 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R78 = 0.0400037 (/millisecond): a kinetic parameter\n"
  "	kf_R79 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R79 = 0.4 (/millisecond): a kinetic parameter\n"
  "	kf_R80 = 4.49987e-05 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R80 = 0.2 (/millisecond): a kinetic parameter\n"
  "	kf_R81 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R82 = 0.000500035 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R82 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R83 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R84 = 7.00003e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R84 = 0.1 (/millisecond): a kinetic parameter\n"
  "	kf_R85 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R86 = 4.00037e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R86 = 0.1 (/millisecond): a kinetic parameter\n"
  "	kf_R87 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R88 = 7.00003e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R88 = 0.1 (/millisecond): a kinetic parameter\n"
  "	kf_R89 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R90 = 4.00037e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R90 = 0.1 (/millisecond): a kinetic parameter\n"
  "	kf_R91 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R91 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R92 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R93 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R93 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R94 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R95 = 0.0001 (/millisecond): a kinetic parameter\n"
  "	kf_R96 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R96 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R97 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R98 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R98 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R99 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R100 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R100 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R101 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R102 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R102 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R103 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R104 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R104 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R105 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R106 = 5.00035e-07 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R106 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R107 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R108 = 0.000500035 (/millisecond): a kinetic parameter\n"
  "	kr_R108 = 1e-06 (/millisecond): a kinetic parameter\n"
  "	kf_R109 = 0.000500035 (/millisecond): a kinetic parameter\n"
  "	kr_R109 = 1e-06 (/millisecond): a kinetic parameter\n"
  "	kf_R110 = 0.000500035 (/millisecond): a kinetic parameter\n"
  "	kr_R110 = 1e-06 (/millisecond): a kinetic parameter\n"
  "	kf_R111 = 0.000500035 (/millisecond): a kinetic parameter\n"
  "	kr_R111 = 1e-06 (/millisecond): a kinetic parameter\n"
  "	kf_R112 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R112 = 0.000400037 (/millisecond): a kinetic parameter\n"
  "	kf_R113 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R113 = 0.0400037 (/millisecond): a kinetic parameter\n"
  "	kf_R114 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R114 = 0.4 (/millisecond): a kinetic parameter\n"
  "	kf_R115 = 6.00067e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R115 = 0.00199986 (/millisecond): a kinetic parameter\n"
  "	kf_R116 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R116 = 0.01 (/millisecond): a kinetic parameter\n"
  "	kf_R117 = 8.00018e-07 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R117 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R118 = 0.001 (/millisecond): a kinetic parameter\n"
  "	kf_R119 = 0.000500035 (/millisecond): a kinetic parameter\n"
  "	kf_R120 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R120 = 0.0400037 (/millisecond): a kinetic parameter\n"
  "	kf_R121 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R121 = 0.4 (/millisecond): a kinetic parameter\n"
  "	kf_R122 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R122 = 4 (/millisecond): a kinetic parameter\n"
  "	kf_R123 = 0.0001 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R123 = 0.1 (/millisecond): a kinetic parameter\n"
  "	kf_R124 = 6.00067e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R124 = 0.00199986 (/millisecond): a kinetic parameter\n"
  "	kf_R125 = 0.000500035 (/millisecond): a kinetic parameter\n"
  "	kr_R125 = 0.000500035 (/millisecond): a kinetic parameter\n"
  "	kf_R126 = 0.000500035 (/millisecond): a kinetic parameter\n"
  "	kr_R126 = 0.000500035 (/millisecond): a kinetic parameter\n"
  "	kf_R127 = 0.000500035 (/millisecond): a kinetic parameter\n"
  "	kr_R127 = 0.000500035 (/millisecond): a kinetic parameter\n"
  "	kf_R128 = 0.000500035 (/millisecond): a kinetic parameter\n"
  "	kr_R128 = 0.000500035 (/millisecond): a kinetic parameter\n"
  "	kf_R129 = 1e-06 (/millisecond): a kinetic parameter\n"
  "	kr_R129 = 0.000500035 (/millisecond): a kinetic parameter\n"
  "	kf_R130 = 3.59998e-07 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R130 = 0.0229985 (/millisecond): a kinetic parameter\n"
  "	kf_R131 = 0.00390032 (/millisecond): a kinetic parameter\n"
  "	kf_R132 = 1.10002e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R132 = 0.00540008 (/millisecond): a kinetic parameter\n"
  "	kf_R133 = 10 (/millisecond): a kinetic parameter\n"
  "	kf_R134 = 3.59998e-07 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R134 = 0.0229985 (/millisecond): a kinetic parameter\n"
  "	kf_R135 = 0.00390032 (/millisecond): a kinetic parameter\n"
  "	kf_R136 = 1.10002e-06 (/nanomole/liter-millisecond): a kinetic parameter\n"
  "	kr_R136 = 0.00540008 (/millisecond): a kinetic parameter\n"
  "	kf_R137 = 10 (/millisecond): a kinetic parameter\n"
  "	DA_start  = 100 (millisecond) : an input\n"
  "	DA_max  = 1480 (nanomole/liter) : an input\n"
  "}\n"
  "ASSIGNED {\n"
  "	cai (millimolarity): Ca concentration from NMDA channels \n"
  "	time (millisecond) : alias for t\n"
  "	ATP_expression : a pre-defined algebraic expression\n"
  "	Ca_expression : a pre-defined algebraic expression\n"
  "	DA_expression : a pre-defined algebraic expression\n"
  "	AMP : a pre-defined algebraic expression\n"
  "	ATP : a pre-defined algebraic expression\n"
  "	Ca : a pre-defined algebraic expression\n"
  "	DA : a pre-defined algebraic expression\n"
  "	ReactionFlux0 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux1 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux2 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux3 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux4 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux5 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux6 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux7 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux8 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux9 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux10 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux11 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux12 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux13 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux14 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux15 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux16 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux17 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux18 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux19 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux20 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux21 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux22 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux23 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux24 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux25 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux26 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux27 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux28 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux29 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux30 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux31 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux32 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux33 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux34 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux35 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux36 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux37 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux38 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux39 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux40 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux41 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux42 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux43 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux44 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux45 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux46 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux47 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux48 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux49 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux50 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux51 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux52 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux53 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux54 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux55 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux56 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux57 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux58 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux59 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux60 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux61 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux62 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux63 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux64 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux65 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux66 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux67 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux68 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux69 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux70 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux71 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux72 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux73 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux74 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux75 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux76 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux77 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux78 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux79 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux80 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux81 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux82 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux83 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux84 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux85 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux86 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux87 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux88 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux89 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux90 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux91 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux92 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux93 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux94 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux95 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux96 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux97 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux98 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux99 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux100 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux101 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux102 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux103 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux104 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux105 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux106 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux107 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux108 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux109 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux110 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux111 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux112 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux113 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux114 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux115 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux116 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux117 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux118 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux119 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux120 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux121 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux122 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux123 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux124 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux125 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux126 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux127 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux128 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux129 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux130 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux131 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux132 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux133 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux134 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux135 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux136 : a flux, for use in DERIVATIVE mechanism\n"
  "	ReactionFlux137 : a flux, for use in DERIVATIVE mechanism\n"
  "	pSubstrate_out : an observable\n"
  "	PP1_out : an observable\n"
  "	CaM_out : an observable\n"
  "	D32_out : an observable\n"
  "	total_CaMKII_activated_out : an observable\n"
  "}\n"
  "PROCEDURE assign_calculated_values() {\n"
  "	time = t : an alias for the time variable, if needed.\n"
  "	ATP_expression = 5000000 : assignment for expression EX0\n"
  "	Ca_expression = 0 : assignment for expression EX1\n"
  "	DA_expression = DA_basal+(1/(1+exp((-10E+10)*(time-DA_start)))*(DA_max/(exp(-tau_DA1*tau_DA2/(tau_DA2-tau_DA1)*log(tau_DA2/tau_DA1)/tau_DA1)-exp(-tau_DA1*tau_DA2/(tau_DA2-tau_DA1)*log(tau_DA2/tau_DA1)/tau_DA2))*(exp(-(time-DA_start)/tau_DA1)-exp(-(time-DA_start)/tau_DA2)))) : assignment for expression EX2\n"
  "	AMP = 0 : assignment for expression S8\n"
  "	ATP = 5e+06 : assignment for expression S9\n"
  "	Ca = cai*(1e6) : assignment for expression S24\n"
  "	DA = DA_expression : assignment for expression S47\n"
  "	ReactionFlux0 = kf_R0*GaolfGTP : flux expression R0\n"
  "	ReactionFlux1 = kf_R1*D1R_Golf_DA : flux expression R1\n"
  "	ReactionFlux2 = kf_R2*D1R_Golf*DA-kr_R2*D1R_Golf_DA : flux expression R2\n"
  "	ReactionFlux3 = kf_R3*D1R*DA-kr_R3*D1R_DA : flux expression R3\n"
  "	ReactionFlux4 = kf_R4*AC5*GaolfGTP-kr_R4*AC5_GaolfGTP : flux expression R4\n"
  "	ReactionFlux5 = kf_R5*CaM*Ca-kr_R5*CaM_Ca2 : flux expression R5\n"
  "	ReactionFlux6 = kf_R6*PP2B*CaM-kr_R6*PP2B_CaM : flux expression R6\n"
  "	ReactionFlux7 = kf_R7*CaM_Ca4*PP2B-kr_R7*PP2Bc : flux expression R7\n"
  "	ReactionFlux8 = kf_R8*PKAc*D32-kr_R8*PKAc_D32 : flux expression R8\n"
  "	ReactionFlux9 = kf_R9*PKAc_D32 : flux expression R9\n"
  "	ReactionFlux10 = kf_R10*PKAc*B56PP2A-kr_R10*PKAc_B56PP2A : flux expression R10\n"
  "	ReactionFlux11 = kf_R11*PKAc_B56PP2A : flux expression R11\n"
  "	ReactionFlux12 = kf_R12*D32p34*PP1-kr_R12*PP1_D32p34 : flux expression R12\n"
  "	ReactionFlux13 = kf_R13*CDK5*D32-kr_R13*CDK5_D32 : flux expression R13\n"
  "	ReactionFlux14 = kf_R14*CDK5_D32 : flux expression R14\n"
  "	ReactionFlux15 = kf_R15*D32p75*PKAc-kr_R15*PKAc_D32p75 : flux expression R15\n"
  "	ReactionFlux16 = kf_R16*B72PP2A*Ca-kr_R16*B72PP2A_Ca : flux expression R16\n"
  "	ReactionFlux17 = kf_R17*B56PP2Ap*D32p75-kr_R17*B56PP2Ap_D32p75 : flux expression R17\n"
  "	ReactionFlux18 = kf_R18*B72PP2A*D32p75-kr_R18*B72PP2A_D32p75 : flux expression R18\n"
  "	ReactionFlux19 = kf_R19*D32p75*B72PP2A_Ca-kr_R19*B72PP2A_Ca_D32p75 : flux expression R19\n"
  "	ReactionFlux20 = kf_R20*B56PP2Ap_D32p75 : flux expression R20\n"
  "	ReactionFlux21 = kf_R21*B72PP2A_D32p75 : flux expression R21\n"
  "	ReactionFlux22 = kf_R22*B72PP2A_Ca_D32p75 : flux expression R22\n"
  "	ReactionFlux23 = kf_R23*D32p34*PP2Bc-kr_R23*PP2Bc_D32p34 : flux expression R23\n"
  "	ReactionFlux24 = kf_R24*CaM_Ca2*Ca-kr_R24*CaM_Ca4 : flux expression R24\n"
  "	ReactionFlux25 = kf_R25*Ca*PP2B_CaM-kr_R25*PP2B_CaM_Ca2 : flux expression R25\n"
  "	ReactionFlux26 = kf_R26*Ca*PP2B_CaM_Ca2-kr_R26*PP2Bc : flux expression R26\n"
  "	ReactionFlux27 = kf_R27*CaM_Ca2*PP2B-kr_R27*PP2B_CaM_Ca2 : flux expression R27\n"
  "	ReactionFlux28 = kf_R28*AC5*Ca-kr_R28*AC5_Ca : flux expression R28\n"
  "	ReactionFlux29 = kf_R29*AC5_Ca*GaolfGTP-kr_R29*AC5_Ca_GaolfGTP : flux expression R29\n"
  "	ReactionFlux30 = kf_R30*D32p75*B56PP2A-kr_R30*B56PP2A_D32p75 : flux expression R30\n"
  "	ReactionFlux31 = kf_R31*B56PP2A_D32p75 : flux expression R31\n"
  "	ReactionFlux32 = kf_R32*B72PP2A_Ca_D32p34 : flux expression R32\n"
  "	ReactionFlux33 = kf_R33*B72PP2A_D32p34 : flux expression R33\n"
  "	ReactionFlux34 = kf_R34*D32p34*B72PP2A_Ca-kr_R34*B72PP2A_Ca_D32p34 : flux expression R34\n"
  "	ReactionFlux35 = kf_R35*D32p34*B72PP2A-kr_R35*B72PP2A_D32p34 : flux expression R35\n"
  "	ReactionFlux36 = kf_R36*PP2Bc_D32p34 : flux expression R36\n"
  "	ReactionFlux37 = kf_R37*B56PP2Ap : flux expression R37\n"
  "	ReactionFlux38 = kf_R38*cAMP*PKA-kr_R38*PKA_Ca2MP : flux expression R38\n"
  "	ReactionFlux39 = kf_R39*cAMP*PKA_Ca2MP-kr_R39*PKA_Ca4MP : flux expression R39\n"
  "	ReactionFlux40 = kf_R40*PKA_Ca4MP-kr_R40*PKAc*PKAreg : flux expression R40\n"
  "	ReactionFlux41 = kf_R41*cAMP*PDE4-kr_R41*PDE4_cAMP : flux expression R41\n"
  "	ReactionFlux42 = kf_R42*PDE4_cAMP : flux expression R42\n"
  "	ReactionFlux43 = kf_R43*PDE10r*cAMP^2-kr_R43*PDE10c : flux expression R43\n"
  "	ReactionFlux44 = kf_R44*PDE10r_cAMP : flux expression R44\n"
  "	ReactionFlux45 = kf_R45*cAMP*PDE10r-kr_R45*PDE10r_cAMP : flux expression R45\n"
  "	ReactionFlux46 = kf_R46*PDE10c_cAMP : flux expression R46\n"
  "	ReactionFlux47 = kf_R47*GaolfGDP*Gbgolf : flux expression R47\n"
  "	ReactionFlux48 = kf_R48*AC5_GaolfGTP*ATP-kr_R48*AC5_GaolfGTP_ATP : flux expression R48\n"
  "	ReactionFlux49 = kf_R49*AC5*ATP-kr_R49*AC5_ATP : flux expression R49\n"
  "	ReactionFlux50 = kf_R50*AC5_Ca*ATP-kr_R50*AC5_Ca_ATP : flux expression R50\n"
  "	ReactionFlux51 = kf_R51*AC5_Ca_GaolfGTP*ATP-kr_R51*AC5_Ca_GaolfGTP_ATP : flux expression R51\n"
  "	ReactionFlux52 = kf_R52*GaolfGTP*AC5_ATP-kr_R52*AC5_GaolfGTP_ATP : flux expression R52\n"
  "	ReactionFlux53 = kf_R53*GaolfGTP*AC5_Ca_ATP-kr_R53*AC5_Ca_GaolfGTP_ATP : flux expression R53\n"
  "	ReactionFlux54 = kf_R54*Ca*AC5_ATP-kr_R54*AC5_Ca_ATP : flux expression R54\n"
  "	ReactionFlux55 = kf_R55*AC5_GaolfGTP_ATP : flux expression R55\n"
  "	ReactionFlux56 = kf_R56*cAMP*AC5_GaolfGTP : flux expression R56\n"
  "	ReactionFlux57 = kf_R57*AC5_ATP : flux expression R57\n"
  "	ReactionFlux58 = kf_R58*cAMP*AC5 : flux expression R58\n"
  "	ReactionFlux59 = kf_R59*AC5_Ca_ATP : flux expression R59\n"
  "	ReactionFlux60 = kf_R60*cAMP*AC5_Ca : flux expression R60\n"
  "	ReactionFlux61 = kf_R61*AC5_Ca_GaolfGTP_ATP : flux expression R61\n"
  "	ReactionFlux62 = kf_R62*cAMP*AC5_Ca_GaolfGTP : flux expression R62\n"
  "	ReactionFlux63 = kf_R63*AC5_GaolfGTP : flux expression R63\n"
  "	ReactionFlux64 = kf_R64*AC5_Ca_GaolfGTP : flux expression R64\n"
  "	ReactionFlux65 = kf_R65*AC5_GaolfGTP_ATP : flux expression R65\n"
  "	ReactionFlux66 = kf_R66*AC5_Ca_GaolfGTP_ATP : flux expression R66\n"
  "	ReactionFlux67 = kf_R67*D1R*Golf-kr_R67*D1R_Golf : flux expression R67\n"
  "	ReactionFlux68 = kf_R68*Golf*D1R_DA-kr_R68*D1R_Golf_DA : flux expression R68\n"
  "	ReactionFlux69 = kf_R69*cAMP*PDE10c-kr_R69*PDE10c_cAMP : flux expression R69\n"
  "	ReactionFlux70 = kf_R70*CaMKII*CaM_Ca4-kr_R70*CaMKII_CaM_Ca4 : flux expression R70\n"
  "	ReactionFlux71 = kf_R71*CaM_Ca2*CaMKII-kr_R71*CaMKII_CaM_Ca2 : flux expression R71\n"
  "	ReactionFlux72 = kf_R72*CaM*CaMKII-kr_R72*CaMKII_CaM : flux expression R72\n"
  "	ReactionFlux73 = kf_R73*CaMKII_CaM_Ca2*Ca-kr_R73*CaMKII_CaM_Ca4 : flux expression R73\n"
  "	ReactionFlux74 = kf_R74*CaMKII_CaM*Ca-kr_R74*CaMKII_CaM_Ca2 : flux expression R74\n"
  "	ReactionFlux75 = kf_R75*pCaMKII_CaM_Ca2*Ca-kr_R75*pCaMKII_CaM_Ca4 : flux expression R75\n"
  "	ReactionFlux76 = kf_R76*pCaMKII_CaM*Ca-kr_R76*pCaMKII_CaM_Ca2 : flux expression R76\n"
  "	ReactionFlux77 = kf_R77*pCaMKII*CaM_Ca4-kr_R77*pCaMKII_CaM_Ca4 : flux expression R77\n"
  "	ReactionFlux78 = kf_R78*pCaMKII*CaM_Ca2-kr_R78*pCaMKII_CaM_Ca2 : flux expression R78\n"
  "	ReactionFlux79 = kf_R79*pCaMKII*CaM-kr_R79*pCaMKII_CaM : flux expression R79\n"
  "	ReactionFlux80 = kf_R80*ARPP21*PKAc-kr_R80*PKAc_ARPP21 : flux expression R80\n"
  "	ReactionFlux81 = kf_R81*PKAc_ARPP21 : flux expression R81\n"
  "	ReactionFlux82 = kf_R82*pARPP21*CaM_Ca4-kr_R82*CaM_Ca4_pARPP21 : flux expression R82\n"
  "	ReactionFlux83 = kf_R83*B72PP2A_Ca_pARPP21 : flux expression R83\n"
  "	ReactionFlux84 = kf_R84*pARPP21*B72PP2A_Ca-kr_R84*B72PP2A_Ca_pARPP21 : flux expression R84\n"
  "	ReactionFlux85 = kf_R85*B72PP2A_pARPP21 : flux expression R85\n"
  "	ReactionFlux86 = kf_R86*pARPP21*B72PP2A-kr_R86*B72PP2A_pARPP21 : flux expression R86\n"
  "	ReactionFlux87 = kf_R87*B56PP2Ap_pARPP21 : flux expression R87\n"
  "	ReactionFlux88 = kf_R88*pARPP21*B56PP2Ap-kr_R88*B56PP2Ap_pARPP21 : flux expression R88\n"
  "	ReactionFlux89 = kf_R89*B56PP2A_pARPP21 : flux expression R89\n"
  "	ReactionFlux90 = kf_R90*pARPP21*B56PP2A-kr_R90*B56PP2A_pARPP21 : flux expression R90\n"
  "	ReactionFlux91 = kf_R91*pSubstrate*PP1-kr_R91*PP1_pSubstrate : flux expression R91\n"
  "	ReactionFlux92 = kf_R92*PP1_pSubstrate : flux expression R92\n"
  "	ReactionFlux93 = kf_R93*Substrate*pCaMKII_psd-kr_R93*pCaMKII_psd_Substrate : flux expression R93\n"
  "	ReactionFlux94 = kf_R94*pCaMKII_psd_Substrate : flux expression R94\n"
  "	ReactionFlux95 = kf_R95*pCaMKII : flux expression R95\n"
  "	ReactionFlux96 = kf_R96*Substrate*pCaMKII_CaM_psd-kr_R96*pCaMKII_CaM_psd_Substrate : flux expression R96\n"
  "	ReactionFlux97 = kf_R97*pCaMKII_CaM_psd_Substrate : flux expression R97\n"
  "	ReactionFlux98 = kf_R98*Substrate*pCaMKII_CaM_Ca2_psd-kr_R98*pCaMKII_CaM_Ca2_psd_Substrate : flux expression R98\n"
  "	ReactionFlux99 = kf_R99*pCaMKII_CaM_Ca2_psd_Substrate : flux expression R99\n"
  "	ReactionFlux100 = kf_R100*Substrate*pCaMKII_CaM_Ca4_psd-kr_R100*pCaMKII_CaM_Ca4_psd_Substrate : flux expression R100\n"
  "	ReactionFlux101 = kf_R101*pCaMKII_CaM_Ca4_psd_Substrate : flux expression R101\n"
  "	ReactionFlux102 = kf_R102*Substrate*CaMKII_CaM_psd-kr_R102*CaMKII_CaM_psd_Substrate : flux expression R102\n"
  "	ReactionFlux103 = kf_R103*CaMKII_CaM_psd_Substrate : flux expression R103\n"
  "	ReactionFlux104 = kf_R104*Substrate*CaMKII_CaM_Ca2_psd-kr_R104*CaMKII_CaM_Ca2_psd_Substrate : flux expression R104\n"
  "	ReactionFlux105 = kf_R105*CaMKII_CaM_Ca2_psd_Substrate : flux expression R105\n"
  "	ReactionFlux106 = kf_R106*Substrate*CaMKII_CaM_Ca4_psd-kr_R106*CaMKII_CaM_Ca4_psd_Substrate : flux expression R106\n"
  "	ReactionFlux107 = kf_R107*CaMKII_CaM_Ca4_psd_Substrate : flux expression R107\n"
  "	ReactionFlux108 = kf_R108*pCaMKII_CaM_Ca4-kr_R108*pCaMKII_CaM_Ca4_psd : flux expression R108\n"
  "	ReactionFlux109 = kf_R109*pCaMKII_CaM_Ca2-kr_R109*pCaMKII_CaM_Ca2_psd : flux expression R109\n"
  "	ReactionFlux110 = kf_R110*pCaMKII_CaM-kr_R110*pCaMKII_CaM_psd : flux expression R110\n"
  "	ReactionFlux111 = kf_R111*pCaMKII-kr_R111*pCaMKII_psd : flux expression R111\n"
  "	ReactionFlux112 = kf_R112*CaM_Ca4*pCaMKII_psd-kr_R112*pCaMKII_CaM_Ca4_psd : flux expression R112\n"
  "	ReactionFlux113 = kf_R113*pCaMKII_psd*CaM_Ca2-kr_R113*pCaMKII_CaM_Ca2_psd : flux expression R113\n"
  "	ReactionFlux114 = kf_R114*CaM*pCaMKII_psd-kr_R114*pCaMKII_CaM_psd : flux expression R114\n"
  "	ReactionFlux115 = kf_R115*pCaMKII_CaM_psd*Ca-kr_R115*pCaMKII_CaM_Ca2_psd : flux expression R115\n"
  "	ReactionFlux116 = kf_R116*pCaMKII_CaM_Ca2_psd*Ca-kr_R116*pCaMKII_CaM_Ca4_psd : flux expression R116\n"
  "	ReactionFlux117 = kf_R117*pCaMKII_psd*PP1-kr_R117*PP1_pCaMKII_psd : flux expression R117\n"
  "	ReactionFlux118 = kf_R118*PP1_pCaMKII_psd : flux expression R118\n"
  "	ReactionFlux119 = kf_R119*CaMKII_psd : flux expression R119\n"
  "	ReactionFlux120 = kf_R120*CaM_Ca4*CaMKII_psd-kr_R120*CaMKII_CaM_Ca4_psd : flux expression R120\n"
  "	ReactionFlux121 = kf_R121*CaM_Ca2*CaMKII_psd-kr_R121*CaMKII_CaM_Ca2_psd : flux expression R121\n"
  "	ReactionFlux122 = kf_R122*CaM*CaMKII_psd-kr_R122*CaMKII_CaM_psd : flux expression R122\n"
  "	ReactionFlux123 = kf_R123*CaMKII_CaM_Ca2_psd*Ca-kr_R123*CaMKII_CaM_Ca4_psd : flux expression R123\n"
  "	ReactionFlux124 = kf_R124*CaMKII_CaM_psd*Ca-kr_R124*CaMKII_CaM_Ca2_psd : flux expression R124\n"
  "	ReactionFlux125 = kf_R125*CaMKII_CaM-kr_R125*CaMKII_CaM_psd : flux expression R125\n"
  "	ReactionFlux126 = kf_R126*CaMKII_CaM_Ca2-kr_R126*CaMKII_CaM_Ca2_psd : flux expression R126\n"
  "	ReactionFlux127 = kf_R127*CaMKII_CaM_Ca4-kr_R127*CaMKII_CaM_Ca4_psd : flux expression R127\n"
  "	ReactionFlux128 = kf_R128*CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd-kr_R128*CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : flux expression R128\n"
  "	ReactionFlux129 = kf_R129*pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd-kr_R129*pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : flux expression R129\n"
  "	ReactionFlux130 = kf_R130*CaMKII_CaM_Ca4*CaMKII_CaM_Ca4-kr_R130*CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : flux expression R130\n"
  "	ReactionFlux131 = kf_R131*CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : flux expression R131\n"
  "	ReactionFlux132 = kf_R132*pCaMKII_CaM_Ca4*CaMKII_CaM_Ca4-kr_R132*pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : flux expression R132\n"
  "	ReactionFlux133 = kf_R133*pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 : flux expression R133\n"
  "	ReactionFlux134 = kf_R134*CaMKII_CaM_Ca4_psd*CaMKII_CaM_Ca4_psd-kr_R134*CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd : flux expression R134\n"
  "	ReactionFlux135 = kf_R135*CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd : flux expression R135\n"
  "	ReactionFlux136 = kf_R136*pCaMKII_CaM_Ca4_psd*CaMKII_CaM_Ca4_psd-kr_R136*pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd : flux expression R136\n"
  "	ReactionFlux137 = kf_R137*pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd : flux expression R137\n"
  "	total_CaMKII_activated = pCaMKII_CaM_Ca4_psd + pCaMKII_CaM_Ca2_psd + pCaMKII_CaM_psd + pCaMKII_psd + CaMKII_CaM_Ca4_psd + CaMKII_CaM_Ca2_psd + CaMKII_CaM_Ca4_psd_Substrate + CaMKII_CaM_psd_Substrate + CaMKII_CaM_Ca2_psd_Substrate + pCaMKII_psd_Substrate + pCaMKII_CaM_psd_Substrate + pCaMKII_CaM_Ca2_psd_Substrate + pCaMKII_CaM_Ca4_psd_Substrate\n"
  "\n"
  "}\n"
  "STATE {\n"
  "	AC5 (nanomole/liter) : a state variable\n"
  "	AC5_ATP (nanomole/liter) : a state variable\n"
  "	AC5_Ca (nanomole/liter) : a state variable\n"
  "	AC5_Ca_ATP (nanomole/liter) : a state variable\n"
  "	AC5_Ca_GaolfGTP (nanomole/liter) : a state variable\n"
  "	AC5_Ca_GaolfGTP_ATP (nanomole/liter) : a state variable\n"
  "	AC5_GaolfGTP (nanomole/liter) : a state variable\n"
  "	AC5_GaolfGTP_ATP (nanomole/liter) : a state variable\n"
  "	B56PP2A (nanomole/liter) : a state variable\n"
  "	B56PP2A_D32p75 (nanomole/liter) : a state variable\n"
  "	B56PP2A_pARPP21 (nanomole/liter) : a state variable\n"
  "	B56PP2Ap (nanomole/liter) : a state variable\n"
  "	B56PP2Ap_D32p75 (nanomole/liter) : a state variable\n"
  "	B56PP2Ap_pARPP21 (nanomole/liter) : a state variable\n"
  "	B72PP2A (nanomole/liter) : a state variable\n"
  "	B72PP2A_D32p34 (nanomole/liter) : a state variable\n"
  "	B72PP2A_D32p75 (nanomole/liter) : a state variable\n"
  "	B72PP2A_pARPP21 (nanomole/liter) : a state variable\n"
  "	B72PP2A_Ca_D32p34 (nanomole/liter) : a state variable\n"
  "	B72PP2A_Ca_D32p75 (nanomole/liter) : a state variable\n"
  "	B72PP2A_Ca (nanomole/liter) : a state variable\n"
  "	B72PP2A_Ca_pARPP21 (nanomole/liter) : a state variable\n"
  "	CaM (nanomole/liter) : a state variable\n"
  "	CaM_Ca2 (nanomole/liter) : a state variable\n"
  "	CaM_Ca4 (nanomole/liter) : a state variable\n"
  "	CaM_Ca4_pARPP21 (nanomole/liter) : a state variable\n"
  "	CaMKII (nanomole/liter) : a state variable\n"
  "	CaMKII_CaM_Ca4 (nanomole/liter) : a state variable\n"
  "	CaMKII_CaM (nanomole/liter) : a state variable\n"
  "	CaMKII_CaM_Ca2 (nanomole/liter) : a state variable\n"
  "	CaMKII_CaM_Ca2_psd (nanomole/liter) : a state variable\n"
  "	CaMKII_CaM_psd (nanomole/liter) : a state variable\n"
  "	CaMKII_CaM_Ca4_psd (nanomole/liter) : a state variable\n"
  "	CaMKII_psd (nanomole/liter) : a state variable\n"
  "	cAMP (nanomole/liter) : a state variable\n"
  "	Substrate (nanomole/liter) : a state variable\n"
  "	CDK5 (nanomole/liter) : a state variable\n"
  "	CDK5_D32 (nanomole/liter) : a state variable\n"
  "	D1R (nanomole/liter) : a state variable\n"
  "	D1R_DA (nanomole/liter) : a state variable\n"
  "	D1R_Golf_DA (nanomole/liter) : a state variable\n"
  "	D1R_Golf (nanomole/liter) : a state variable\n"
  "	D32p34 (nanomole/liter) : a state variable\n"
  "	D32p75 (nanomole/liter) : a state variable\n"
  "	D32 (nanomole/liter) : a state variable\n"
  "	GaolfGDP (nanomole/liter) : a state variable\n"
  "	GaolfGTP (nanomole/liter) : a state variable\n"
  "	Gbgolf (nanomole/liter) : a state variable\n"
  "	Golf (nanomole/liter) : a state variable\n"
  "	pCaMKII (nanomole/liter) : a state variable\n"
  "	pCaMKII_CaM_Ca4 (nanomole/liter) : a state variable\n"
  "	pCaMKII_CaM (nanomole/liter) : a state variable\n"
  "	pCaMKII_CaM_Ca2 (nanomole/liter) : a state variable\n"
  "	pCaMKII_CaM_Ca2_psd (nanomole/liter) : a state variable\n"
  "	pCaMKII_CaM_psd (nanomole/liter) : a state variable\n"
  "	pCaMKII_CaM_Ca4_psd (nanomole/liter) : a state variable\n"
  "	pCaMKII_psd (nanomole/liter) : a state variable\n"
  "	pSubstrate (nanomole/liter) : a state variable\n"
  "	PDE4 (nanomole/liter) : a state variable\n"
  "	PDE4_cAMP (nanomole/liter) : a state variable\n"
  "	PDE10r (nanomole/liter) : a state variable\n"
  "	PDE10r_cAMP (nanomole/liter) : a state variable\n"
  "	PDE10c (nanomole/liter) : a state variable\n"
  "	PDE10c_cAMP (nanomole/liter) : a state variable\n"
  "	PKA (nanomole/liter) : a state variable\n"
  "	PKAc (nanomole/liter) : a state variable\n"
  "	PKAc_B56PP2A (nanomole/liter) : a state variable\n"
  "	PKAc_D32 (nanomole/liter) : a state variable\n"
  "	PKAc_ARPP21 (nanomole/liter) : a state variable\n"
  "	PKA_Ca2MP (nanomole/liter) : a state variable\n"
  "	PKA_Ca4MP (nanomole/liter) : a state variable\n"
  "	PKAc_D32p75 (nanomole/liter) : a state variable\n"
  "	PKAreg (nanomole/liter) : a state variable\n"
  "	PP1 (nanomole/liter) : a state variable\n"
  "	PP1_pCaMKII_psd (nanomole/liter) : a state variable\n"
  "	PP1_pSubstrate (nanomole/liter) : a state variable\n"
  "	PP1_D32p34 (nanomole/liter) : a state variable\n"
  "	CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd (nanomole/liter) : a state variable\n"
  "	pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd (nanomole/liter) : a state variable\n"
  "	CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 (nanomole/liter) : a state variable\n"
  "	pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 (nanomole/liter) : a state variable\n"
  "	PP2B (nanomole/liter) : a state variable\n"
  "	PP2Bc (nanomole/liter) : a state variable\n"
  "	PP2Bc_D32p34 (nanomole/liter) : a state variable\n"
  "	PP2B_CaM (nanomole/liter) : a state variable\n"
  "	PP2B_CaM_Ca2 (nanomole/liter) : a state variable\n"
  "	pARPP21 (nanomole/liter) : a state variable\n"
  "	ARPP21 (nanomole/liter) : a state variable\n"
  "	pCaMKII_psd_Substrate (nanomole/liter) : a state variable\n"
  "	pCaMKII_CaM_psd_Substrate (nanomole/liter) : a state variable\n"
  "	pCaMKII_CaM_Ca2_psd_Substrate (nanomole/liter) : a state variable\n"
  "	pCaMKII_CaM_Ca4_psd_Substrate (nanomole/liter) : a state variable\n"
  "	CaMKII_CaM_psd_Substrate (nanomole/liter) : a state variable\n"
  "	CaMKII_CaM_Ca2_psd_Substrate (nanomole/liter) : a state variable\n"
  "	CaMKII_CaM_Ca4_psd_Substrate (nanomole/liter) : a state variable\n"
  "	total_CaMKII_activated (nanomole/liter) : a state variable\n"
  "}\n"
  "INITIAL {\n"
  "     AC5 = 2.6579740648536387\n"
  " 	 AC5_ATP = 664.5955722158345\n"
  "	 AC5_Ca = 0.011455491216440293\n"
  "	 AC5_Ca_ATP = 2.8642831776146602 \n"
  "	 AC5_Ca_GaolfGTP = 0.0005087730491145609 \n"
  "	 AC5_Ca_GaolfGTP_ATP = 0.1276760000022537\n"
  "	 AC5_GaolfGTP = 0.11762328938669141 \n"
  "	 AC5_GaolfGTP_ATP = 29.624906977591287 \n"
  "	 B56PP2A = 891.3882782297828 \n"
  "	 B56PP2A_D32p75 = 773.8986890359638 \n"
  "	 B56PP2A_pARPP21 = 22.004569833130333 \n"
  "	 B56PP2Ap = 119.83225503696232\n"
  "	 B56PP2Ap_D32p75 = 183.32968907852563 \n"
  "	 B56PP2Ap_pARPP21 = 4.752784515174912\n"
  "	 B72PP2A = 998.1762288155527\n"
  "	 B72PP2A_D32p34 = 0.029586434857564403\n"
  "	 B72PP2A_D32p75 = 866.6114349644631\n"
  "	 B72PP2A_pARPP21 = 24.640708285240002\n"
  "	 B72PP2A_Ca_D32p34 = 0.001275120308719799\n"
  "	 B72PP2A_Ca_D32p75 = 65.81498998111533\n"
  "	 B72PP2A_Ca = 43.01953875726838\n"
  "	 B72PP2A_Ca_pARPP21 = 1.706240090303376\n"
  "	 CaM = 3271.1613030579483\n"
  "	 CaM_Ca2 = 42.30197029468885\n"
  "	 CaM_Ca4 = 0.18232282358259608 \n"
  "	 CaM_Ca4_pARPP21 = 5.682096670017442\n"
  "	 CaMKII = 16861.31022167976\n"
  "	 CaMKII_CaM_Ca4 = 7.653695787280561\n"
  "	 CaMKII_CaM = 1378.7438408069913 \n"
  "	 CaMKII_CaM_Ca2 = 178.1085180682959\n"
  "	 CaMKII_CaM_Ca2_psd = 15.344587294726768\n"
  "	 CaMKII_CaM_psd = 117.20636345254225 \n"
  "	 CaMKII_CaM_Ca4_psd = 0.6836514096472648 \n"
  "	 CaMKII_psd = 1431.2784425994976\n"
  "	 cAMP = 38.077478703814286\n"
  "	 Substrate = 2898.4324981645364\n"
  "	 CDK5 = 1354.5983328435307 \n"
  "	 CDK5_D32 = 445.4016679783238\n"
  "	 D1R = 1476.965276006024\n"
  "	 D1R_DA = 5.959513286613785\n"
  "	 D1R_Golf_DA = 2.0091697499991463\n"
  "	 D1R_Golf = 515.0660409549953\n"
  "	 D32p34 = 0.23709844962796384\n"
  "	 D32p75 = 11014.977244009184\n"
  "	 D32 = 36168.79062206558\n"
  "	 GaolfGDP = 0.010083118413574194\n"
  "	 GaolfGTP = 0.008914911110695258\n"
  "	 Gbgolf = 29.889710469343125\n"
  "	 Golf = 1453.0350762349071\n"
  "	 pCaMKII = 0.0026152322826163694\n"
  "	 pCaMKII_CaM_Ca4 = 0.00041326366874510956\n"
  "	 pCaMKII_CaM = 0.0021363473128570283\n"
  "	 pCaMKII_CaM_Ca2 = 0.0003364074902532764\n"
  "	 pCaMKII_CaM_Ca2_psd = 0.00029964701372417826\n"
  "	 pCaMKII_CaM_psd = 0.00223880855203415 \n"
  "	 pCaMKII_CaM_Ca4_psd = 0.00015640795348060934\n"
  "	 pCaMKII_psd = 0.002734310759402372\n"
  "	 pSubstrate = 82.25679040587481 \n"
  "	 PDE4 = 1507.8595078954654\n"
  "	 PDE4_cAMP = 492.1404908824553\n"
  "	 PDE10r = 396.93707251699345 \n"
  "	 PDE10r_cAMP = 302.30479218857784\n"
  " 	 PDE10c = 0.5755168324209912 \n"
  "	 PDE10c_cAMP = 0.1826207133266763\n"
  "	 PKA = 1143.825553233938\n"
  "	 PKAc = 2.6887584775003255 \n"
  "	 PKAc_B56PP2A = 4.793733616212578 \n"
  "	 PKAc_D32 = 4.630911543143565\n"
  "	 PKAc_ARPP21 = 11.123552417073366\n"
  "	 PKA_Ca2MP = 3.235620105419139 \n"
  "	 PKA_Ca4MP = 0.08525605875534487\n"
  "	 PKAc_D32p75 = 29.616613444303574 \n"
  "	 PKAreg = 52.85356959978496 \n"
  "	 PP1 = 2582.1938739416964 \n"
  "	 PP1_pCaMKII_psd = 0.0028242717416327636\n"
  "	 PP1_pSubstrate = 9.655356749304744\n"
  "	 PP1_D32p34 = 408.14794647416636\n"
  "	 CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd = 2.019451923560302e-05\n"
  "	 pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd = 1.1773379671332063e-11 \n"
  "	 CaMKII_CaM_Ca4_CaMKII_CaM_Ca4 = 0.0007700483148596818\n"
  "	 pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4 = 3.4773054620114007e-10\n"
  "	 PP2B = 26.730674733834796\n"
  "	 PP2Bc = 162.45364687157698\n"
  "	 PP2Bc_D32p34 = 38.512174821299965\n"
  "	 PP2B_CaM = 2.9146880204369956\n"
  "	 PP2B_CaM_Ca2 = 3769.3888179670294\n"
  "	 pARPP21 = 623.2570162577764\n"
  "	 ARPP21 = 19306.833014960313\n"
  "	 pCaMKII_psd_Substrate = 0.00019814424825483155\n"
  "	 pCaMKII_CaM_psd_Substrate = 0.00016223724242164732\n"
  "	 pCaMKII_CaM_Ca2_psd_Substrate = 2.1714185950523916e-05\n"
  "	 pCaMKII_CaM_Ca4_psd_Substrate = 1.133424072480528e-05\n"
  "	 CaMKII_CaM_psd_Substrate = 8.493462821347531 \n"
  "	 CaMKII_CaM_Ca2_psd_Substrate = 1.11195909383754\n"
  "	 CaMKII_CaM_Ca4_psd_Substrate = 0.04954140423400814\n"
  "	 total_CaMKII_activated = pCaMKII_CaM_Ca4_psd + pCaMKII_CaM_Ca2_psd + pCaMKII_CaM_psd + pCaMKII_psd + CaMKII_CaM_Ca4_psd + CaMKII_CaM_Ca2_psd + CaMKII_CaM_Ca4_psd_Substrate + CaMKII_CaM_psd_Substrate + CaMKII_CaM_Ca2_psd_Substrate + pCaMKII_psd_Substrate + pCaMKII_CaM_psd_Substrate + pCaMKII_CaM_Ca2_psd_Substrate + pCaMKII_CaM_Ca4_psd_Substrate\n"
  "\n"
  "}\n"
  "BREAKPOINT {\n"
  "	SOLVE ode METHOD cnexp\n"
  "	assign_calculated_values() : procedure\n"
  "}\n"
  "DERIVATIVE ode {\n"
  "	AC5' = -ReactionFlux4-ReactionFlux28-ReactionFlux49+ReactionFlux57-ReactionFlux58+ReactionFlux63 : affects compound with ID S0\n"
  "	AC5_ATP' = ReactionFlux49-ReactionFlux52-ReactionFlux54-ReactionFlux57+ReactionFlux58+ReactionFlux65 : affects compound with ID S1\n"
  "	AC5_Ca' = ReactionFlux28-ReactionFlux29-ReactionFlux50+ReactionFlux59-ReactionFlux60+ReactionFlux64 : affects compound with ID S2\n"
  "	AC5_Ca_ATP' = ReactionFlux50-ReactionFlux53+ReactionFlux54-ReactionFlux59+ReactionFlux60+ReactionFlux66 : affects compound with ID S3\n"
  "	AC5_Ca_GaolfGTP' = ReactionFlux29-ReactionFlux51+ReactionFlux61-ReactionFlux62-ReactionFlux64 : affects compound with ID S4\n"
  "	AC5_Ca_GaolfGTP_ATP' = ReactionFlux51+ReactionFlux53-ReactionFlux61+ReactionFlux62-ReactionFlux66 : affects compound with ID S5\n"
  "	AC5_GaolfGTP' = ReactionFlux4-ReactionFlux48+ReactionFlux55-ReactionFlux56-ReactionFlux63 : affects compound with ID S6\n"
  "	AC5_GaolfGTP_ATP' = ReactionFlux48+ReactionFlux52-ReactionFlux55+ReactionFlux56-ReactionFlux65 : affects compound with ID S7\n"
  "	B56PP2A' = -ReactionFlux10-ReactionFlux30+ReactionFlux31+ReactionFlux37+ReactionFlux89-ReactionFlux90 : affects compound with ID S10\n"
  "	B56PP2A_D32p75' = ReactionFlux30-ReactionFlux31 : affects compound with ID S11\n"
  "	B56PP2A_pARPP21' = -ReactionFlux89+ReactionFlux90 : affects compound with ID S12\n"
  "	B56PP2Ap' = ReactionFlux11-ReactionFlux17+ReactionFlux20-ReactionFlux37+ReactionFlux87-ReactionFlux88 : affects compound with ID S13\n"
  "	B56PP2Ap_D32p75' = ReactionFlux17-ReactionFlux20 : affects compound with ID S14\n"
  "	B56PP2Ap_pARPP21' = -ReactionFlux87+ReactionFlux88 : affects compound with ID S15\n"
  "	B72PP2A' = -ReactionFlux16-ReactionFlux18+ReactionFlux21+ReactionFlux33-ReactionFlux35+ReactionFlux85-ReactionFlux86 : affects compound with ID S16\n"
  "	B72PP2A_D32p34' = -ReactionFlux33+ReactionFlux35 : affects compound with ID S17\n"
  "	B72PP2A_D32p75' = ReactionFlux18-ReactionFlux21 : affects compound with ID S18\n"
  "	B72PP2A_pARPP21' = -ReactionFlux85+ReactionFlux86 : affects compound with ID S19\n"
  "	B72PP2A_Ca_D32p34' = -ReactionFlux32+ReactionFlux34 : affects compound with ID S20\n"
  "	B72PP2A_Ca_D32p75' = ReactionFlux19-ReactionFlux22 : affects compound with ID S21\n"
  "	B72PP2A_Ca' = ReactionFlux16-ReactionFlux19+ReactionFlux22+ReactionFlux32-ReactionFlux34+ReactionFlux83-ReactionFlux84 : affects compound with ID S22\n"
  "	B72PP2A_Ca_pARPP21' = -ReactionFlux83+ReactionFlux84 : affects compound with ID S23\n"
  "	CaM' = -ReactionFlux5-ReactionFlux6-ReactionFlux72-ReactionFlux79-ReactionFlux114-ReactionFlux122 : affects compound with ID S25\n"
  "	CaM_Ca2' = ReactionFlux5-ReactionFlux24-ReactionFlux27-ReactionFlux71-ReactionFlux78-ReactionFlux113-ReactionFlux121 : affects compound with ID S26\n"
  "	CaM_Ca4' = -ReactionFlux7+ReactionFlux24-ReactionFlux70-ReactionFlux77-ReactionFlux82-ReactionFlux112-ReactionFlux120 : affects compound with ID S27\n"
  "	CaM_Ca4_pARPP21' = ReactionFlux82 : affects compound with ID S28\n"
  "	CaMKII' = -ReactionFlux70-ReactionFlux71-ReactionFlux72+ReactionFlux95+ReactionFlux119 : affects compound with ID S29\n"
  "	CaMKII_CaM_Ca4' = ReactionFlux70+ReactionFlux73-ReactionFlux127-ReactionFlux130-ReactionFlux130+ReactionFlux131-ReactionFlux132 : affects compound with ID S30\n"
  "	CaMKII_CaM' = ReactionFlux72-ReactionFlux74-ReactionFlux125 : affects compound with ID S31\n"
  "	CaMKII_CaM_Ca2' = ReactionFlux71-ReactionFlux73+ReactionFlux74-ReactionFlux126 : affects compound with ID S32\n"
  "	CaMKII_CaM_Ca2_psd' = -ReactionFlux104+ReactionFlux105+ReactionFlux121-ReactionFlux123+ReactionFlux124+ReactionFlux126 : affects compound with ID S33\n"
  "	CaMKII_CaM_psd' = -ReactionFlux102+ReactionFlux103+ReactionFlux122-ReactionFlux124+ReactionFlux125 : affects compound with ID S34\n"
  "	CaMKII_CaM_Ca4_psd' = -ReactionFlux106+ReactionFlux107+ReactionFlux120+ReactionFlux123+ReactionFlux127-ReactionFlux134-ReactionFlux134+ReactionFlux135-ReactionFlux136 : affects compound with ID S35\n"
  "	CaMKII_psd' = ReactionFlux118-ReactionFlux119-ReactionFlux120-ReactionFlux121-ReactionFlux122 : affects compound with ID S36\n"
  "	cAMP' = -ReactionFlux38-ReactionFlux39-ReactionFlux41-2*ReactionFlux43-ReactionFlux45+ReactionFlux55-ReactionFlux56+ReactionFlux57-ReactionFlux58+ReactionFlux59-ReactionFlux60+ReactionFlux61-ReactionFlux62-ReactionFlux69 : affects compound with ID S37\n"
  "	Substrate' = ReactionFlux92-ReactionFlux93-ReactionFlux96-ReactionFlux98-ReactionFlux100-ReactionFlux102-ReactionFlux104-ReactionFlux106 : affects compound with ID S38\n"
  "	CDK5' = -ReactionFlux13+ReactionFlux14 : affects compound with ID S39\n"
  "	CDK5_D32' = ReactionFlux13-ReactionFlux14 : affects compound with ID S40\n"
  "	D1R' = -ReactionFlux3-ReactionFlux67 : affects compound with ID S41\n"
  "	D1R_DA' = ReactionFlux1+ReactionFlux3-ReactionFlux68 : affects compound with ID S42\n"
  "	D1R_Golf_DA' = -ReactionFlux1+ReactionFlux2+ReactionFlux68 : affects compound with ID S43\n"
  "	D1R_Golf' = -ReactionFlux2+ReactionFlux67 : affects compound with ID S44\n"
  "	D32p34' = ReactionFlux9-ReactionFlux12-ReactionFlux23-ReactionFlux34-ReactionFlux35 : affects compound with ID S45\n"
  "	D32p75' = ReactionFlux14-ReactionFlux15-ReactionFlux17-ReactionFlux18-ReactionFlux19-ReactionFlux30 : affects compound with ID S46\n"
  "	D32' = -ReactionFlux8-ReactionFlux13+ReactionFlux20+ReactionFlux21+ReactionFlux22+ReactionFlux31+ReactionFlux32+ReactionFlux33+ReactionFlux36 : affects compound with ID S48\n"
  "	GaolfGDP' = ReactionFlux0-ReactionFlux47+ReactionFlux63+ReactionFlux64+ReactionFlux65+ReactionFlux66 : affects compound with ID S49\n"
  "	GaolfGTP' = -ReactionFlux0+ReactionFlux1-ReactionFlux4-ReactionFlux29-ReactionFlux52-ReactionFlux53 : affects compound with ID S50\n"
  "	Gbgolf' = ReactionFlux1-ReactionFlux47 : affects compound with ID S51\n"
  "	Golf' = ReactionFlux47-ReactionFlux67-ReactionFlux68 : affects compound with ID S52\n"
  "	pCaMKII' = -ReactionFlux77-ReactionFlux78-ReactionFlux79-ReactionFlux95-ReactionFlux111 : affects compound with ID S53\n"
  "	pCaMKII_CaM_Ca4' = ReactionFlux75+ReactionFlux77-ReactionFlux108+ReactionFlux131-ReactionFlux132+ReactionFlux133+ReactionFlux133 : affects compound with ID S54\n"
  "	pCaMKII_CaM' = -ReactionFlux76+ReactionFlux79-ReactionFlux110 : affects compound with ID S55\n"
  "	pCaMKII_CaM_Ca2' = -ReactionFlux75+ReactionFlux76+ReactionFlux78-ReactionFlux109 : affects compound with ID S56\n"
  "	pCaMKII_CaM_Ca2_psd' = -ReactionFlux98+ReactionFlux99+ReactionFlux109+ReactionFlux113+ReactionFlux115-ReactionFlux116 : affects compound with ID S57\n"
  "	pCaMKII_CaM_psd' = -ReactionFlux96+ReactionFlux97+ReactionFlux110+ReactionFlux114-ReactionFlux115 : affects compound with ID S58\n"
  "	pCaMKII_CaM_Ca4_psd' = -ReactionFlux100+ReactionFlux101+ReactionFlux108+ReactionFlux112+ReactionFlux116+ReactionFlux135-ReactionFlux136+ReactionFlux137+ReactionFlux137 : affects compound with ID S59\n"
  "	pCaMKII_psd' = -ReactionFlux93+ReactionFlux94+ReactionFlux111-ReactionFlux112-ReactionFlux113-ReactionFlux114-ReactionFlux117 : affects compound with ID S60\n"
  "	pSubstrate' = -ReactionFlux91+ReactionFlux94+ReactionFlux97+ReactionFlux99+ReactionFlux101+ReactionFlux103+ReactionFlux105+ReactionFlux107 : affects compound with ID S61\n"
  "	PDE4' = -ReactionFlux41+ReactionFlux42 : affects compound with ID S62\n"
  "	PDE4_cAMP' = ReactionFlux41-ReactionFlux42 : affects compound with ID S63\n"
  "	PDE10r' = -ReactionFlux43+ReactionFlux44-ReactionFlux45 : affects compound with ID S64\n"
  "	PDE10r_cAMP' = -ReactionFlux44+ReactionFlux45 : affects compound with ID S65\n"
  "	PDE10c' = ReactionFlux43+ReactionFlux46-ReactionFlux69 : affects compound with ID S66\n"
  "	PDE10c_cAMP' = -ReactionFlux46+ReactionFlux69 : affects compound with ID S67\n"
  "	PKA' = -ReactionFlux38 : affects compound with ID S68\n"
  "	PKAc' = -ReactionFlux8+ReactionFlux9-ReactionFlux10+ReactionFlux11-ReactionFlux15+ReactionFlux40-ReactionFlux80+ReactionFlux81 : affects compound with ID S69\n"
  "	PKAc_B56PP2A' = ReactionFlux10-ReactionFlux11 : affects compound with ID S70\n"
  "	PKAc_D32' = ReactionFlux8-ReactionFlux9 : affects compound with ID S71\n"
  "	PKAc_ARPP21' = ReactionFlux80-ReactionFlux81 : affects compound with ID S72\n"
  "	PKA_Ca2MP' = ReactionFlux38-ReactionFlux39 : affects compound with ID S73\n"
  "	PKA_Ca4MP' = ReactionFlux39-ReactionFlux40 : affects compound with ID S74\n"
  "	PKAc_D32p75' = ReactionFlux15 : affects compound with ID S75\n"
  "	PKAreg' = ReactionFlux40 : affects compound with ID S76\n"
  "	PP1' = -ReactionFlux12-ReactionFlux91+ReactionFlux92-ReactionFlux117+ReactionFlux118 : affects compound with ID S77\n"
  "	PP1_pCaMKII_psd' = ReactionFlux117-ReactionFlux118 : affects compound with ID S78\n"
  "	PP1_pSubstrate' = ReactionFlux91-ReactionFlux92 : affects compound with ID S79\n"
  "	PP1_D32p34' = ReactionFlux12 : affects compound with ID S80\n"
  "	CaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd' = -ReactionFlux128+ReactionFlux134-ReactionFlux135 : affects compound with ID S81\n"
  "	pCaMKII_CaM_Ca4_psd_CaMKII_CaM_Ca4_psd' = -ReactionFlux129+ReactionFlux136-ReactionFlux137 : affects compound with ID S82\n"
  "	CaMKII_CaM_Ca4_CaMKII_CaM_Ca4' = ReactionFlux128+ReactionFlux130-ReactionFlux131 : affects compound with ID S83\n"
  "	pCaMKII_CaM_Ca4_CaMKII_CaM_Ca4' = ReactionFlux129+ReactionFlux132-ReactionFlux133 : affects compound with ID S84\n"
  "	PP2B' = -ReactionFlux6-ReactionFlux7-ReactionFlux27 : affects compound with ID S85\n"
  "	PP2Bc' = ReactionFlux7-ReactionFlux23+ReactionFlux26+ReactionFlux36 : affects compound with ID S86\n"
  "	PP2Bc_D32p34' = ReactionFlux23-ReactionFlux36 : affects compound with ID S87\n"
  "	PP2B_CaM' = ReactionFlux6-ReactionFlux25 : affects compound with ID S88\n"
  "	PP2B_CaM_Ca2' = ReactionFlux25-ReactionFlux26+ReactionFlux27 : affects compound with ID S89\n"
  "	pARPP21' = ReactionFlux81-ReactionFlux82-ReactionFlux84-ReactionFlux86-ReactionFlux88-ReactionFlux90 : affects compound with ID S90\n"
  "	ARPP21' = -ReactionFlux80+ReactionFlux83+ReactionFlux85+ReactionFlux87+ReactionFlux89 : affects compound with ID S91\n"
  "	pCaMKII_psd_Substrate' = ReactionFlux93-ReactionFlux94 : affects compound with ID S92\n"
  "	pCaMKII_CaM_psd_Substrate' = ReactionFlux96-ReactionFlux97 : affects compound with ID S93\n"
  "	pCaMKII_CaM_Ca2_psd_Substrate' = ReactionFlux98-ReactionFlux99 : affects compound with ID S94\n"
  "	pCaMKII_CaM_Ca4_psd_Substrate' = ReactionFlux100-ReactionFlux101 : affects compound with ID S95\n"
  "	CaMKII_CaM_psd_Substrate' = ReactionFlux102-ReactionFlux103 : affects compound with ID S96\n"
  "	CaMKII_CaM_Ca2_psd_Substrate' = ReactionFlux104-ReactionFlux105 : affects compound with ID S97\n"
  "	CaMKII_CaM_Ca4_psd_Substrate' = ReactionFlux106-ReactionFlux107 : affects compound with ID S98\n"
  "	total_CaMKII_activated' = pCaMKII_CaM_Ca4_psd' + pCaMKII_CaM_Ca2_psd' + pCaMKII_CaM_psd' + pCaMKII_psd' + CaMKII_CaM_Ca4_psd' + CaMKII_CaM_Ca2_psd' + CaMKII_CaM_Ca4_psd_Substrate' + CaMKII_CaM_psd_Substrate' + CaMKII_CaM_Ca2_psd_Substrate' + pCaMKII_psd_Substrate' + pCaMKII_CaM_psd_Substrate' + pCaMKII_CaM_Ca2_psd_Substrate' + pCaMKII_CaM_Ca4_psd_Substrate'\n"
  "\n"
  "}\n"
  "PROCEDURE observables_func() {\n"
  "	pSubstrate_out = pSubstrate : Output ID Y0\n"
  "	PP1_out = PP1 : Output ID Y1\n"
  "	CaM_out = CaM : Output ID Y2\n"
  "	D32_out = D32 : Output ID Y3\n"
  "	total_CaMKII_activated_out = total_CaMKII_activated\n"
  "	\n"
  "}\n"
  ;
#endif
