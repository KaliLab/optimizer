/* Created by Language version: 7.7.0 */
/* NOT VECTORIZED */
#define NRN_VECTORIZED 0
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
 
#define nrn_init _nrn_init__sKCa
#define _nrn_initial _nrn_initial__sKCa
#define nrn_cur _nrn_cur__sKCa
#define _nrn_current _nrn_current__sKCa
#define nrn_jacob _nrn_jacob__sKCa
#define nrn_state _nrn_state__sKCa
#define _net_receive _net_receive__sKCa 
#define integrate integrate__sKCa 
#define setinf setinf__sKCa 
 
#define _threadargscomma_ /**/
#define _threadargsprotocomma_ /**/
#define _threadargs_ /**/
#define _threadargsproto_ /**/
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 static double *_p; static Datum *_ppvar;
 
#define t nrn_threads->_t
#define dt nrn_threads->_dt
#define gk _p[0]
#define isKCa _p[1]
#define w _p[2]
#define ek _p[3]
#define ki _p[4]
#define cai _p[5]
#define ica _p[6]
#define ik _p[7]
#define winf _p[8]
#define wtau _p[9]
#define Dw _p[10]
#define _g _p[11]
#define _ion_cai	*_ppvar[0]._pval
#define _ion_ki	*_ppvar[1]._pval
#define _ion_ek	*_ppvar[2]._pval
#define _ion_ik	*_ppvar[3]._pval
#define _ion_dikdv	*_ppvar[4]._pval
 
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
 /* external NEURON variables */
 extern double celsius;
 /* declaration of user functions */
 static void _hoc_llog(void);
 static void _hoc_setinf(void);
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
 _p = _prop->param; _ppvar = _prop->dparam;
 }
 static void _hoc_setdata() {
 Prop *_prop, *hoc_getdata_range(int);
 _prop = hoc_getdata_range(_mechtype);
   _setdata(_prop);
 hoc_retpushx(1.);
}
 /* connect user functions to hoc names */
 static VoidFunc hoc_intfunc[] = {
 "setdata_sKCa", _hoc_setdata,
 "llog_sKCa", _hoc_llog,
 "setinf_sKCa", _hoc_setinf,
 0, 0
};
#define llog llog_sKCa
 extern double llog( double );
 /* declare global and static user variables */
#define Q10 Q10_sKCa
 double Q10 = 1.5;
#define activate_Q10 activate_Q10_sKCa
 double activate_Q10 = 1;
#define gmax_k gmax_k_sKCa
 double gmax_k = 0;
#define gmaxQ10 gmaxQ10_sKCa
 double gmaxQ10 = 1.5;
#define rate_k rate_k_sKCa
 double rate_k = 0;
#define sKCatau sKCatau_sKCa
 double sKCatau = 23.6533;
#define tempb tempb_sKCa
 double tempb = 23;
#define temp2 temp2_sKCa
 double temp2 = 29;
#define temp1 temp1_sKCa
 double temp1 = 19;
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "sKCatau_sKCa", "ms",
 "temp1_sKCa", "degC",
 "temp2_sKCa", "degC",
 "tempb_sKCa", "degC",
 "gk_sKCa", "mho/cm2",
 "isKCa_sKCa", "mA/cm2",
 0,0
};
 static double delta_t = 0.01;
 static double v = 0;
 static double w0 = 0;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 "sKCatau_sKCa", &sKCatau_sKCa,
 "activate_Q10_sKCa", &activate_Q10_sKCa,
 "Q10_sKCa", &Q10_sKCa,
 "gmaxQ10_sKCa", &gmaxQ10_sKCa,
 "temp1_sKCa", &temp1_sKCa,
 "temp2_sKCa", &temp2_sKCa,
 "tempb_sKCa", &tempb_sKCa,
 "rate_k_sKCa", &rate_k_sKCa,
 "gmax_k_sKCa", &gmax_k_sKCa,
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
 
#define _cvode_ieq _ppvar[5]._i
 static void _ode_matsol_instance1(_threadargsproto_);
 /* connect range variables in _p that hoc is supposed to know about */
 static const char *_mechanism[] = {
 "7.7.0",
"sKCa",
 "gk_sKCa",
 "isKCa_sKCa",
 0,
 0,
 "w_sKCa",
 0,
 0};
 static Symbol* _ca_sym;
 static Symbol* _k_sym;
 
extern Prop* need_memb(Symbol*);

static void nrn_alloc(Prop* _prop) {
	Prop *prop_ion;
	double *_p; Datum *_ppvar;
 	_p = nrn_prop_data_alloc(_mechtype, 12, _prop);
 	/*initialize range parameters*/
 	gk = 0.0001;
 	isKCa = 0;
 	_prop->param = _p;
 	_prop->param_size = 12;
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 6, _prop);
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 prop_ion = need_memb(_ca_sym);
 nrn_promote(prop_ion, 1, 0);
 	_ppvar[0]._pval = &prop_ion->param[1]; /* cai */
 prop_ion = need_memb(_k_sym);
 nrn_promote(prop_ion, 1, 1);
 	_ppvar[1]._pval = &prop_ion->param[1]; /* ki */
 	_ppvar[2]._pval = &prop_ion->param[0]; /* ek */
 	_ppvar[3]._pval = &prop_ion->param[3]; /* ik */
 	_ppvar[4]._pval = &prop_ion->param[4]; /* _ion_dikdv */
 
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

 void _sKCa_reg() {
	int _vectorized = 0;
  _initlists();
 	ion_reg("ca", -10000.);
 	ion_reg("k", -10000.);
 	_ca_sym = hoc_lookup("ca_ion");
 	_k_sym = hoc_lookup("k_ion");
 	register_mech(_mechanism, nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init, hoc_nrnpointerindex, 0);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
     _nrn_setdata_reg(_mechtype, _setdata);
     _nrn_thread_reg(_mechtype, 2, _update_ion_pointer);
 #if NMODL_TEXT
  hoc_reg_nmodl_text(_mechtype, nmodl_file_text);
  hoc_reg_nmodl_filename(_mechtype, nmodl_filename);
#endif
  hoc_register_prop_size(_mechtype, 12, 6);
  hoc_register_dparam_semantics(_mechtype, 0, "ca_ion");
  hoc_register_dparam_semantics(_mechtype, 1, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 2, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 3, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 4, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 5, "cvodeieq");
 	hoc_register_cvode(_mechtype, _ode_count, _ode_map, _ode_spec, _ode_matsol);
 	hoc_register_tolerance(_mechtype, _hoc_state_tol, &_atollist);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 sKCa /home/mohacsi/Desktop/optimizer/optimizer/new_test_files/Luca_modell_new/sKCa.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
 static double F = 96485.3;
static int _reset;
static char *modelname = "small conductance calcium activated potassium channels";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
static int setinf(double);
 
static int _ode_spec1(_threadargsproto_);
/*static int _ode_matsol1(_threadargsproto_);*/
 static int _slist1[1], _dlist1[1];
 static int integrate(_threadargsproto_);
 
/*CVODE*/
 static int _ode_spec1 () {_reset=0;
 {
   setinf ( _threadargscomma_ cai ) ;
   Dw = ( winf - w ) / wtau ;
   }
 return _reset;
}
 static int _ode_matsol1 () {
 setinf ( _threadargscomma_ cai ) ;
 Dw = Dw  / (1. - dt*( ( ( ( - 1.0 ) ) ) / wtau )) ;
  return 0;
}
 /*END CVODE*/
 static int integrate () {_reset=0;
 {
   setinf ( _threadargscomma_ cai ) ;
    w = w + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / wtau)))*(- ( ( ( winf ) ) / wtau ) / ( ( ( ( - 1.0 ) ) ) / wtau ) - w) ;
   }
  return 0;
}
 
static int  setinf (  double _lcai ) {
   double _lwcai ;
 _lwcai = _lcai * 1000.0 ;
   winf = 0.81 / ( 1.0 + exp ( ( llog ( _threadargscomma_ _lwcai ) + 0.3 ) / - 0.46 ) ) ;
   wtau = sKCatau / rate_k ;
    return 0; }
 
static void _hoc_setinf(void) {
  double _r;
   _r = 1.;
 setinf (  *getarg(1) );
 hoc_retpushx(_r);
}
 
double llog (  double _lx ) {
   double _lllog;
 if ( _lx > 1e-11 ) {
     _lllog = log ( _lx ) ;
     }
   else {
     _lllog = 0.0 ;
     }
   
return _lllog;
 }
 
static void _hoc_llog(void) {
  double _r;
   _r =  llog (  *getarg(1) );
 hoc_retpushx(_r);
}
 
static int _ode_count(int _type){ return 1;}
 
static void _ode_spec(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
  cai = _ion_cai;
  ki = _ion_ki;
  ek = _ion_ek;
     _ode_spec1 ();
  }}
 
static void _ode_map(int _ieq, double** _pv, double** _pvdot, double* _pp, Datum* _ppd, double* _atol, int _type) { 
 	int _i; _p = _pp; _ppvar = _ppd;
	_cvode_ieq = _ieq;
	for (_i=0; _i < 1; ++_i) {
		_pv[_i] = _pp + _slist1[_i];  _pvdot[_i] = _pp + _dlist1[_i];
		_cvode_abstol(_atollist, _atol, _i);
	}
 }
 
static void _ode_matsol_instance1(_threadargsproto_) {
 _ode_matsol1 ();
 }
 
static void _ode_matsol(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
  cai = _ion_cai;
  ki = _ion_ki;
  ek = _ion_ek;
 _ode_matsol_instance1(_threadargs_);
 }}
 extern void nrn_update_ion_pointer(Symbol*, Datum*, int, int);
 static void _update_ion_pointer(Datum* _ppvar) {
   nrn_update_ion_pointer(_ca_sym, _ppvar, 0, 1);
   nrn_update_ion_pointer(_k_sym, _ppvar, 1, 1);
   nrn_update_ion_pointer(_k_sym, _ppvar, 2, 0);
   nrn_update_ion_pointer(_k_sym, _ppvar, 3, 3);
   nrn_update_ion_pointer(_k_sym, _ppvar, 4, 4);
 }

static void initmodel() {
  int _i; double _save;_ninits++;
 _save = t;
 t = 0.0;
{
  w = w0;
 {
   double _lktemp , _lktempb , _lktemp1 , _lktemp2 ;
 if ( activate_Q10 > 0.0 ) {
     rate_k = pow( Q10 , ( ( celsius - tempb ) / 10.0 ) ) ;
     gmax_k = pow( gmaxQ10 , ( ( celsius - tempb ) / 10.0 ) ) ;
     }
   else {
     rate_k = 1.0 ;
     gmax_k = 1.0 ;
     }
   setinf ( _threadargscomma_ cai ) ;
   w = winf ;
   }
  _sav_indep = t; t = _save;

}
}

static void nrn_init(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
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
  ki = _ion_ki;
  ek = _ion_ek;
 initmodel();
 }}

static double _nrn_current(double _v){double _current=0.;v=_v;{ {
   ik = ( gk * gmax_k ) * w * ( v - ek ) ;
   isKCa = ik ;
   }
 _current += ik;

} return _current;
}

static void nrn_cur(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; int* _ni; double _rhs, _v; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
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
  cai = _ion_cai;
  ki = _ion_ki;
  ek = _ion_ek;
 _g = _nrn_current(_v + .001);
 	{ double _dik;
  _dik = ik;
 _rhs = _nrn_current(_v);
  _ion_dikdv += (_dik - ik)/.001 ;
 	}
 _g = (_g - _rhs)/.001;
  _ion_ik += ik ;
#if CACHEVEC
  if (use_cachevec) {
	VEC_RHS(_ni[_iml]) -= _rhs;
  }else
#endif
  {
	NODERHS(_nd) -= _rhs;
  }
 
}}

static void nrn_jacob(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
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
 
}}

static void nrn_state(_NrnThread* _nt, _Memb_list* _ml, int _type){
Node *_nd; double _v = 0.0; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
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
  ki = _ion_ki;
  ek = _ion_ek;
 { error =  integrate();
 if(error){fprintf(stderr,"at line 67 in file sKCa.mod:\n	SOLVE integrate METHOD cnexp\n"); nrn_complain(_p); abort_run(error);}
 } }}

}

static void terminal(){}

static void _initlists() {
 int _i; static int _first = 1;
  if (!_first) return;
 _slist1[0] = &(w) - _p;  _dlist1[0] = &(Dw) - _p;
_first = 0;
}

#if NMODL_TEXT
static const char* nmodl_filename = "/home/mohacsi/Desktop/optimizer/optimizer/new_test_files/Luca_modell_new/sKCa.mod";
static const char* nmodl_file_text = 
  "TITLE small conductance calcium activated potassium channels\n"
  "\n"
  "COMMENT\n"
  " sKCa - kinetics from Hirschberg (1998), at room temperature\n"
  " (22-24degC).\n"
  "\n"
  " How the q10 works: There is a q10 for the rates (alpha and beta's)\n"
  " called Q10 and a Q10 for the maximum conductance called gmaxQ10.  The\n"
  " q10s should have been measured at specific temperatures temp1 and\n"
  " temp2 (that are 10degC apart). Ideally, as Q10 is temperature\n"
  " dependant, we should know these two temperatures.  We used to\n"
  " follow the more formal Arrhenius derived Q10 approach.  The\n"
  " temperature at which this channel's kinetics were recorded is tempb\n"
  " (base temperature).  What we then need to calculate is the desired\n"
  " rate scale for now working at temperature celsius (rate_k).  This was\n"
  " given by the empirical Arrhenius equation, using the Q10, but now is \n"
  " using the quick Q10 approximation. \n"
  "ENDCOMMENT\n"
  "\n"
  "NEURON {\n"
  "	SUFFIX sKCa\n"
  "	USEION ca READ cai\n"
  "	USEION k READ ki,ek WRITE ik\n"
  "	RANGE  gk,isKCa\n"
  "	GLOBAL sKCatau,activate_Q10,Q10,gmaxQ10,rate_k,gmax_k,temp1,temp2,tempb\n"
  "}\n"
  "\n"
  "UNITS {\n"
  "	(mM) = (milli/liter)\n"
  "	(mA) = (milliamp)\n"
  "	F = (faraday) (coulombs)	: Faradays constant \n"
  "}\n"
  "\n"
  "PARAMETER {\n"
  "        v (mV)\n"
  "	dt (ms)\n"
  "	gk = 0.0001 (mho/cm2)\n"
  "        isKCa = 0.0 (mA/cm2)\n"
  "	sKCatau = 2.365325544e+01 (ms)\n"
  "	ek \n"
  "	ki\n"
  "	cai\n"
  "	celsius\n"
  "	\n"
  "	activate_Q10 = 1\n"
  "	Q10 = 1.5\n"
  "	gmaxQ10 = 1.5\n"
  "	temp1 = 19.0 (degC)\n"
  "	temp2 = 29.0 (degC)\n"
  "	tempb = 23.0 (degC)\n"
  "}\n"
  "\n"
  "ASSIGNED {\n"
  "	ica (mA/cm2)\n"
  "        ik (mA/cm2)\n"
  "        winf \n"
  "	wtau (ms)\n"
  "	rate_k\n"
  "	gmax_k\n"
  "}\n"
  "\n"
  "STATE {\n"
  "        w\n"
  "}\n"
  "\n"
  "BREAKPOINT {\n"
  "	SOLVE integrate METHOD cnexp\n"
  "	ik = (gk*gmax_k)*w*(v-ek)\n"
  "	isKCa = ik\n"
  "}\n"
  "\n"
  "\n"
  "UNITSOFF\n"
  "\n"
  "INITIAL {\n"
  "	LOCAL ktemp,ktempb,ktemp1,ktemp2\n"
  "	if (activate_Q10>0) {\n"
  "	  rate_k = Q10^((celsius-tempb)/10)\n"
  "          gmax_k = gmaxQ10^((celsius-tempb)/10)\n"
  "	}else{\n"
  "	  rate_k = 1.0\n"
  "	  gmax_k = 1.0\n"
  "	}\n"
  "	setinf(cai)\n"
  "	w = winf\n"
  "}\n"
  "\n"
  "DERIVATIVE integrate {\n"
  "        setinf(cai)\n"
  "	w' = (winf - w)/wtau\n"
  "}\n"
  "\n"
  "PROCEDURE setinf(cai) {\n"
  "	LOCAL wcai\n"
  "	: these equations are for micro Molar\n"
  "	wcai = cai*1000\n"
  "	winf = 0.81/(1+exp((llog(wcai)+0.3)/ -0.46))\n"
  "	wtau = sKCatau/rate_k\n"
  "}\n"
  "\n"
  "FUNCTION llog(x) {  :returns log of x, but error checks first\n"
  "        if (x>1e-11) {\n"
  "                llog = log(x)\n"
  "	}else{\n"
  "	        llog=0\n"
  "        }\n"
  "}\n"
  "\n"
  "UNITSON\n"
  "\n"
  "\n"
  "\n"
  "\n"
  "\n"
  "\n"
  ;
#endif
