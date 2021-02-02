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
 
#define nrn_init _nrn_init__K_DR
#define _nrn_initial _nrn_initial__K_DR
#define nrn_cur _nrn_cur__K_DR
#define _nrn_current _nrn_current__K_DR
#define nrn_jacob _nrn_jacob__K_DR
#define nrn_state _nrn_state__K_DR
#define _net_receive _net_receive__K_DR 
#define _f_rates _f_rates__K_DR 
#define rates rates__K_DR 
#define states states__K_DR 
 
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
#define gmax _p[0]
#define gion _p[1]
#define Xinf _p[2]
#define Xtau _p[3]
#define X _p[4]
#define ek _p[5]
#define ik _p[6]
#define DX _p[7]
#define v _p[8]
#define _g _p[9]
#define _ion_ek	*_ppvar[0]._pval
#define _ion_ik	*_ppvar[1]._pval
#define _ion_dikdv	*_ppvar[2]._pval
 
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
 extern double celsius;
 /* declaration of user functions */
 static void _hoc_rates(void);
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
 "setdata_K_DR", _hoc_setdata,
 "rates_K_DR", _hoc_rates,
 0, 0
};
 
static void _check_rates(double*, Datum*, Datum*, _NrnThread*); 
static void _check_table_thread(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, int _type) {
   _check_rates(_p, _ppvar, _thread, _nt);
 }
 /* declare global and static user variables */
#define usetable usetable_K_DR
 double usetable = 1;
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 "usetable_K_DR", 0, 1,
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "gmax_K_DR", "S/cm2",
 "gion_K_DR", "S/cm2",
 "Xtau_K_DR", "ms",
 0,0
};
 static double X0 = 0;
 static double delta_t = 0.01;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 "usetable_K_DR", &usetable_K_DR,
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
 
#define _cvode_ieq _ppvar[3]._i
 static void _ode_matsol_instance1(_threadargsproto_);
 /* connect range variables in _p that hoc is supposed to know about */
 static const char *_mechanism[] = {
 "7.7.0",
"K_DR",
 "gmax_K_DR",
 0,
 "gion_K_DR",
 "Xinf_K_DR",
 "Xtau_K_DR",
 0,
 "X_K_DR",
 0,
 0};
 static Symbol* _k_sym;
 
extern Prop* need_memb(Symbol*);

static void nrn_alloc(Prop* _prop) {
	Prop *prop_ion;
	double *_p; Datum *_ppvar;
 	_p = nrn_prop_data_alloc(_mechtype, 10, _prop);
 	/*initialize range parameters*/
 	gmax = 0.009;
 	_prop->param = _p;
 	_prop->param_size = 10;
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 4, _prop);
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 prop_ion = need_memb(_k_sym);
 nrn_promote(prop_ion, 0, 1);
 	_ppvar[0]._pval = &prop_ion->param[0]; /* ek */
 	_ppvar[1]._pval = &prop_ion->param[3]; /* ik */
 	_ppvar[2]._pval = &prop_ion->param[4]; /* _ion_dikdv */
 
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

 void _K_DR_reg() {
	int _vectorized = 1;
  _initlists();
 	ion_reg("k", 1.0);
 	_k_sym = hoc_lookup("k_ion");
 	register_mech(_mechanism, nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init, hoc_nrnpointerindex, 1);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
     _nrn_setdata_reg(_mechtype, _setdata);
     _nrn_thread_reg(_mechtype, 2, _update_ion_pointer);
     _nrn_thread_table_reg(_mechtype, _check_table_thread);
 #if NMODL_TEXT
  hoc_reg_nmodl_text(_mechtype, nmodl_file_text);
  hoc_reg_nmodl_filename(_mechtype, nmodl_filename);
#endif
  hoc_register_prop_size(_mechtype, 10, 4);
  hoc_register_dparam_semantics(_mechtype, 0, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 1, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 2, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 3, "cvodeieq");
 	hoc_register_cvode(_mechtype, _ode_count, _ode_map, _ode_spec, _ode_matsol);
 	hoc_register_tolerance(_mechtype, _hoc_state_tol, &_atollist);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 K_DR /home/mohacsi/work/optimizer/optimizer/new_test_files/ca1_pc_simplification/mod_files/K_DR.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
 static double *_t_Xinf;
 static double *_t_Xtau;
static int _reset;
static char *modelname = "Channel: K_DR";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
static int _f_rates(_threadargsprotocomma_ double);
static int rates(_threadargsprotocomma_ double);
 
static int _ode_spec1(_threadargsproto_);
/*static int _ode_matsol1(_threadargsproto_);*/
 static void _n_rates(_threadargsprotocomma_ double _lv);
 static int _slist1[1], _dlist1[1];
 static int states(_threadargsproto_);
 
/*CVODE*/
 static int _ode_spec1 (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {int _reset = 0; {
   rates ( _threadargscomma_ v ) ;
   DX = ( Xinf - X ) / Xtau ;
   }
 return _reset;
}
 static int _ode_matsol1 (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
 rates ( _threadargscomma_ v ) ;
 DX = DX  / (1. - dt*( ( ( ( - 1.0 ) ) ) / Xtau )) ;
  return 0;
}
 /*END CVODE*/
 static int states (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) { {
   rates ( _threadargscomma_ v ) ;
    X = X + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / Xtau)))*(- ( ( ( Xinf ) ) / Xtau ) / ( ( ( ( - 1.0 ) ) ) / Xtau ) - X) ;
   }
  return 0;
}
 static double _mfac_rates, _tmin_rates;
  static void _check_rates(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
  static int _maktable=1; int _i, _j, _ix = 0;
  double _xi, _tmax;
  static double _sav_celsius;
  if (!usetable) {return;}
  if (_sav_celsius != celsius) { _maktable = 1;}
  if (_maktable) { double _x, _dx; _maktable=0;
   _tmin_rates =  - 100.0 ;
   _tmax =  50.0 ;
   _dx = (_tmax - _tmin_rates)/3000.; _mfac_rates = 1./_dx;
   for (_i=0, _x=_tmin_rates; _i < 3001; _x += _dx, _i++) {
    _f_rates(_p, _ppvar, _thread, _nt, _x);
    _t_Xinf[_i] = Xinf;
    _t_Xtau[_i] = Xtau;
   }
   _sav_celsius = celsius;
  }
 }

 static int rates(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, double _lv) { 
#if 0
_check_rates(_p, _ppvar, _thread, _nt);
#endif
 _n_rates(_p, _ppvar, _thread, _nt, _lv);
 return 0;
 }

 static void _n_rates(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, double _lv){ int _i, _j;
 double _xi, _theta;
 if (!usetable) {
 _f_rates(_p, _ppvar, _thread, _nt, _lv); return; 
}
 _xi = _mfac_rates * (_lv - _tmin_rates);
 if (isnan(_xi)) {
  Xinf = _xi;
  Xtau = _xi;
  return;
 }
 if (_xi <= 0.) {
 Xinf = _t_Xinf[0];
 Xtau = _t_Xtau[0];
 return; }
 if (_xi >= 3000.) {
 Xinf = _t_Xinf[3000];
 Xtau = _t_Xtau[3000];
 return; }
 _i = (int) _xi;
 _theta = _xi - (double)_i;
 Xinf = _t_Xinf[_i] + _theta*(_t_Xinf[_i+1] - _t_Xinf[_i]);
 Xtau = _t_Xtau[_i] + _theta*(_t_Xtau[_i+1] - _t_Xtau[_i]);
 }

 
static int  _f_rates ( _threadargsprotocomma_ double _lv ) {
   double _lalpha , _lbeta , _ltau , _linf , _lgamma , _lzeta , _ltemp_adj_X , _lA_alpha_X , _lB_alpha_X , _lVhalf_alpha_X , _lA_beta_X , _lB_beta_X , _lVhalf_beta_X ;
  _ltemp_adj_X = 1.0 ;
   _lA_alpha_X = 50.0 ;
   _lB_alpha_X = 0.0111111 ;
   _lVhalf_alpha_X = 0.007 ;
   _lA_alpha_X = _lA_alpha_X * 0.0010 ;
   _lB_alpha_X = _lB_alpha_X * 1000.0 ;
   _lVhalf_alpha_X = _lVhalf_alpha_X * 1000.0 ;
   _lalpha = _lA_alpha_X * exp ( ( _lv - _lVhalf_alpha_X ) / _lB_alpha_X ) ;
   _lA_beta_X = 50.0 ;
   _lB_beta_X = - 0.1 ;
   _lVhalf_beta_X = 0.007 ;
   _lA_beta_X = _lA_beta_X * 0.0010 ;
   _lB_beta_X = _lB_beta_X * 1000.0 ;
   _lVhalf_beta_X = _lVhalf_beta_X * 1000.0 ;
   _lbeta = _lA_beta_X * exp ( ( _lv - _lVhalf_beta_X ) / _lB_beta_X ) ;
   Xtau = 1.0 / ( _ltemp_adj_X * ( _lalpha + _lbeta ) ) ;
   Xinf = _lalpha / ( _lalpha + _lbeta ) ;
    return 0; }
 
static void _hoc_rates(void) {
  double _r;
   double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   if (_extcall_prop) {_p = _extcall_prop->param; _ppvar = _extcall_prop->dparam;}else{ _p = (double*)0; _ppvar = (Datum*)0; }
  _thread = _extcall_thread;
  _nt = nrn_threads;
 
#if 1
 _check_rates(_p, _ppvar, _thread, _nt);
#endif
 _r = 1.;
 rates ( _p, _ppvar, _thread, _nt, *getarg(1) );
 hoc_retpushx(_r);
}
 
static int _ode_count(int _type){ return 1;}
 
static void _ode_spec(_NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
  ek = _ion_ek;
     _ode_spec1 (_p, _ppvar, _thread, _nt);
  }}
 
static void _ode_map(int _ieq, double** _pv, double** _pvdot, double* _pp, Datum* _ppd, double* _atol, int _type) { 
	double* _p; Datum* _ppvar;
 	int _i; _p = _pp; _ppvar = _ppd;
	_cvode_ieq = _ieq;
	for (_i=0; _i < 1; ++_i) {
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
  ek = _ion_ek;
 _ode_matsol_instance1(_threadargs_);
 }}
 extern void nrn_update_ion_pointer(Symbol*, Datum*, int, int);
 static void _update_ion_pointer(Datum* _ppvar) {
   nrn_update_ion_pointer(_k_sym, _ppvar, 0, 0);
   nrn_update_ion_pointer(_k_sym, _ppvar, 1, 3);
   nrn_update_ion_pointer(_k_sym, _ppvar, 2, 4);
 }

static void initmodel(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
  int _i; double _save;{
  X = X0;
 {
   ek = - 80.0 ;
   rates ( _threadargscomma_ v ) ;
   X = Xinf ;
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

#if 0
 _check_rates(_p, _ppvar, _thread, _nt);
#endif
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
  ek = _ion_ek;
 initmodel(_p, _ppvar, _thread, _nt);
 }
}

static double _nrn_current(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, double _v){double _current=0.;v=_v;{ {
   gion = gmax * ( pow( ( X ) , 2.0 ) ) ;
   ik = gion * ( v - ek ) ;
   }
 _current += ik;

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
  ek = _ion_ek;
 _g = _nrn_current(_p, _ppvar, _thread, _nt, _v + .001);
 	{ double _dik;
  _dik = ik;
 _rhs = _nrn_current(_p, _ppvar, _thread, _nt, _v);
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
  ek = _ion_ek;
 {   states(_p, _ppvar, _thread, _nt);
  } }}

}

static void terminal(){}

static void _initlists(){
 double _x; double* _p = &_x;
 int _i; static int _first = 1;
  if (!_first) return;
 _slist1[0] = &(X) - _p;  _dlist1[0] = &(DX) - _p;
   _t_Xinf = makevector(3001*sizeof(double));
   _t_Xtau = makevector(3001*sizeof(double));
_first = 0;
}

#if defined(__cplusplus)
} /* extern "C" */
#endif

#if NMODL_TEXT
static const char* nmodl_filename = "/home/mohacsi/work/optimizer/optimizer/new_test_files/ca1_pc_simplification/mod_files/K_DR.mod";
static const char* nmodl_file_text = 
  "COMMENT\n"
  "\n"
  "   **************************************************\n"
  "   File generated by: neuroConstruct v1.5.1 \n"
  "   **************************************************\n"
  "\n"
  "   This file holds the implementation in NEURON of the Cell Mechanism:\n"
  "   K_DR (Type: Channel mechanism, Model: ChannelML based process)\n"
  "\n"
  "   with parameters: \n"
  "   /channelml/@units = SI Units \n"
  "   /channelml/notes = ChannelML file containing a single Channel description \n"
  "   /channelml/channel_type/@name = K_DR \n"
  "   /channelml/channel_type/status/@value = stable \n"
  "   /channelml/channel_type/status/comment = Equations adapted from Kali, based on Golomb et al. \n"
  "   /channelml/channel_type/status/contributor/name = Bogl\n"
  "rka Sz?ke \n"
  "   /channelml/channel_type/notes = K delayed rectifier channel for fast pyramidneurons \n"
  "   /channelml/channel_type/authorList/modelTranslator/name = Bogl\n"
  "rka Sz?ke \n"
  "   /channelml/channel_type/authorList/modelTranslator/institution = PPKE-ITK \n"
  "   /channelml/channel_type/authorList/modelTranslator/email = szoboce - at - digitus.itk.ppke.hu \n"
  "   /channelml/channel_type/current_voltage_relation/@cond_law = ohmic \n"
  "   /channelml/channel_type/current_voltage_relation/@ion = k \n"
  "   /channelml/channel_type/current_voltage_relation/@default_gmax = 90 \n"
  "   /channelml/channel_type/current_voltage_relation/@default_erev = -0.080 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/@name = X \n"
  "   /channelml/channel_type/current_voltage_relation/gate/@instances = 2 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/closed_state/@id = X0 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/open_state/@id = X \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[1]/@name = alpha \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[1]/@from = X0 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[1]/@to = X \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[1]/@expr_form = exponential \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[1]/@rate = 50 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[1]/@scale = 0.0111111 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[1]/@midpoint = 0.007 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[2]/@name = beta \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[2]/@from = X \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[2]/@to = X0 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[2]/@expr_form = exponential \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[2]/@rate = 50 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[2]/@scale = -0.1 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[2]/@midpoint = 0.007 \n"
  "   /channelml/channel_type/impl_prefs/table_settings/@max_v = 0.05 \n"
  "   /channelml/channel_type/impl_prefs/table_settings/@min_v = -0.1 \n"
  "   /channelml/channel_type/impl_prefs/table_settings/@table_divisions = 3000 \n"
  "\n"
  "// File from which this was generated: /home/kali/nC_projects/CA1_NEURON/cellMechanisms/K_DR/K_DR.xml\n"
  "\n"
  "// XSL file with mapping to simulator: /home/kali/nC_projects/CA1_NEURON/cellMechanisms/K_DR/ChannelML_v1.8.1_NEURONmod.xsl\n"
  "\n"
  "ENDCOMMENT\n"
  "\n"
  "\n"
  "?  This is a NEURON mod file generated from a ChannelML file\n"
  "\n"
  "?  Unit system of original ChannelML file: SI Units\n"
  "\n"
  "COMMENT\n"
  "    ChannelML file containing a single Channel description\n"
  "ENDCOMMENT\n"
  "\n"
  "TITLE Channel: K_DR\n"
  "\n"
  "COMMENT\n"
  "    K delayed rectifier channel for fast pyramidneurons\n"
  "ENDCOMMENT\n"
  "\n"
  "\n"
  "UNITS {\n"
  "    (mA) = (milliamp)\n"
  "    (mV) = (millivolt)\n"
  "    (S) = (siemens)\n"
  "    (um) = (micrometer)\n"
  "    (molar) = (1/liter)\n"
  "    (mM) = (millimolar)\n"
  "    (l) = (liter)\n"
  "}\n"
  "\n"
  "\n"
  "    \n"
  "NEURON {\n"
  "      \n"
  "\n"
  "    SUFFIX K_DR\n"
  "    USEION k READ ek WRITE ik VALENCE 1  ? reversal potential of ion is read, outgoing current is written\n"
  "           \n"
  "        \n"
  "    RANGE gmax, gion\n"
  "    \n"
  "    RANGE Xinf, Xtau\n"
  "    \n"
  "}\n"
  "\n"
  "PARAMETER { \n"
  "      \n"
  "\n"
  "    gmax = 0.0090 (S/cm2)  ? default value, should be overwritten when conductance placed on cell\n"
  "    \n"
  "}\n"
  "\n"
  "\n"
  "\n"
  "ASSIGNED {\n"
  "      \n"
  "\n"
  "    v (mV)\n"
  "    \n"
  "    celsius (degC)\n"
  "          \n"
  "\n"
  "    ? Reversal potential of k\n"
  "    ek (mV)\n"
  "    ? The outward flow of ion: k calculated by rate equations...\n"
  "    ik (mA/cm2)\n"
  "    \n"
  "    \n"
  "    gion (S/cm2)\n"
  "    Xinf\n"
  "    Xtau (ms)\n"
  "    \n"
  "}\n"
  "\n"
  "BREAKPOINT { \n"
  "                        \n"
  "    SOLVE states METHOD cnexp\n"
  "         \n"
  "\n"
  "    gion = gmax*((X)^2)      \n"
  "\n"
  "    ik = gion*(v - ek)\n"
  "            \n"
  "\n"
  "}\n"
  "\n"
  "\n"
  "\n"
  "INITIAL {\n"
  "    \n"
  "    ek = -80\n"
  "        \n"
  "    rates(v)\n"
  "    X = Xinf\n"
  "        \n"
  "    \n"
  "}\n"
  "    \n"
  "STATE {\n"
  "    X\n"
  "    \n"
  "}\n"
  "\n"
  "DERIVATIVE states {\n"
  "    rates(v)\n"
  "    X' = (Xinf - X)/Xtau\n"
  "    \n"
  "}\n"
  "\n"
  "PROCEDURE rates(v(mV)) {  \n"
  "    \n"
  "    ? Note: not all of these may be used, depending on the form of rate equations\n"
  "    LOCAL  alpha, beta, tau, inf, gamma, zeta, temp_adj_X, A_alpha_X, B_alpha_X, Vhalf_alpha_X, A_beta_X, B_beta_X, Vhalf_beta_X\n"
  "        \n"
  "    TABLE Xinf, Xtau\n"
  " DEPEND celsius\n"
  " FROM -100 TO 50 WITH 3000\n"
  "    \n"
  "    \n"
  "    UNITSOFF\n"
  "    temp_adj_X = 1\n"
  "    \n"
  "            \n"
  "                \n"
  "           \n"
  "\n"
  "        \n"
  "    ?      ***  Adding rate equations for gate: X  ***\n"
  "        \n"
  "    ? Found a parameterised form of rate equation for alpha, using expression: A*exp((v-Vhalf)/B)\n"
  "    A_alpha_X = 50\n"
  "    B_alpha_X = 0.0111111\n"
  "    Vhalf_alpha_X = 0.007   \n"
  "    \n"
  "    ? Unit system in ChannelML file is SI units, therefore need to convert these to NEURON quanities...\n"
  "    \n"
  "    A_alpha_X = A_alpha_X * 0.0010   ? 1/ms\n"
  "    B_alpha_X = B_alpha_X * 1000   ? mV\n"
  "    Vhalf_alpha_X = Vhalf_alpha_X * 1000   ? mV\n"
  "          \n"
  "                     \n"
  "    alpha = A_alpha_X * exp((v - Vhalf_alpha_X) / B_alpha_X)\n"
  "    \n"
  "    \n"
  "    ? Found a parameterised form of rate equation for beta, using expression: A*exp((v-Vhalf)/B)\n"
  "    A_beta_X = 50\n"
  "    B_beta_X = -0.1\n"
  "    Vhalf_beta_X = 0.007   \n"
  "    \n"
  "    ? Unit system in ChannelML file is SI units, therefore need to convert these to NEURON quanities...\n"
  "    \n"
  "    A_beta_X = A_beta_X * 0.0010   ? 1/ms\n"
  "    B_beta_X = B_beta_X * 1000   ? mV\n"
  "    Vhalf_beta_X = Vhalf_beta_X * 1000   ? mV\n"
  "          \n"
  "                     \n"
  "    beta = A_beta_X * exp((v - Vhalf_beta_X) / B_beta_X)\n"
  "    \n"
  "    Xtau = 1/(temp_adj_X*(alpha + beta))\n"
  "    Xinf = alpha/(alpha + beta)\n"
  "          \n"
  "       \n"
  "    \n"
  "    ?     *** Finished rate equations for gate: X ***\n"
  "    \n"
  "\n"
  "         \n"
  "\n"
  "}\n"
  "\n"
  "\n"
  "UNITSON\n"
  "\n"
  "\n"
  ;
#endif
