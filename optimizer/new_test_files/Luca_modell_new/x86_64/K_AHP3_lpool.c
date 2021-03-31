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
 
#define nrn_init _nrn_init__K_AHP3_lpool
#define _nrn_initial _nrn_initial__K_AHP3_lpool
#define nrn_cur _nrn_cur__K_AHP3_lpool
#define _nrn_current _nrn_current__K_AHP3_lpool
#define nrn_jacob _nrn_jacob__K_AHP3_lpool
#define nrn_state _nrn_state__K_AHP3_lpool
#define _net_receive _net_receive__K_AHP3_lpool 
#define settables settables__K_AHP3_lpool 
#define states states__K_AHP3_lpool 
 
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
#define minf _p[2]
#define mtau _p[3]
#define m _p[4]
#define ek _p[5]
#define ik _p[6]
#define cali _p[7]
#define Dm _p[8]
#define v _p[9]
#define _g _p[10]
#define _ion_ek	*_ppvar[0]._pval
#define _ion_ik	*_ppvar[1]._pval
#define _ion_dikdv	*_ppvar[2]._pval
#define _ion_cali	*_ppvar[3]._pval
 
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
 static void _hoc_settables(void);
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
 "setdata_K_AHP3_lpool", _hoc_setdata,
 "settables_K_AHP3_lpool", _hoc_settables,
 0, 0
};
 /* declare global and static user variables */
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "gmax_K_AHP3_lpool", "S/cm2",
 "gion_K_AHP3_lpool", "S/cm2",
 "mtau_K_AHP3_lpool", "ms",
 0,0
};
 static double delta_t = 0.01;
 static double m0 = 0;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
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
 
#define _cvode_ieq _ppvar[4]._i
 static void _ode_matsol_instance1(_threadargsproto_);
 /* connect range variables in _p that hoc is supposed to know about */
 static const char *_mechanism[] = {
 "7.7.0",
"K_AHP3_lpool",
 "gmax_K_AHP3_lpool",
 0,
 "gion_K_AHP3_lpool",
 "minf_K_AHP3_lpool",
 "mtau_K_AHP3_lpool",
 0,
 "m_K_AHP3_lpool",
 0,
 0};
 static Symbol* _k_sym;
 static Symbol* _cal_sym;
 
extern Prop* need_memb(Symbol*);

static void nrn_alloc(Prop* _prop) {
	Prop *prop_ion;
	double *_p; Datum *_ppvar;
 	_p = nrn_prop_data_alloc(_mechtype, 11, _prop);
 	/*initialize range parameters*/
 	gmax = 0.002;
 	_prop->param = _p;
 	_prop->param_size = 11;
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 5, _prop);
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 prop_ion = need_memb(_k_sym);
 nrn_promote(prop_ion, 0, 1);
 	_ppvar[0]._pval = &prop_ion->param[0]; /* ek */
 	_ppvar[1]._pval = &prop_ion->param[3]; /* ik */
 	_ppvar[2]._pval = &prop_ion->param[4]; /* _ion_dikdv */
 prop_ion = need_memb(_cal_sym);
 nrn_promote(prop_ion, 1, 0);
 	_ppvar[3]._pval = &prop_ion->param[1]; /* cali */
 
}
 static void _initlists();
  /* some states have an absolute tolerance */
 static Symbol** _atollist;
 static HocStateTolerance _hoc_state_tol[] = {
 0,0
};
 static void _thread_mem_init(Datum*);
 static void _thread_cleanup(Datum*);
 static void _update_ion_pointer(Datum*);
 extern Symbol* hoc_lookup(const char*);
extern void _nrn_thread_reg(int, int, void(*)(Datum*));
extern void _nrn_thread_table_reg(int, void(*)(double*, Datum*, Datum*, _NrnThread*, int));
extern void hoc_register_tolerance(int, HocStateTolerance*, Symbol***);
extern void _cvode_abstol( Symbol**, double*, int);

 void _K_AHP3_lpool_reg() {
	int _vectorized = 1;
  _initlists();
 	ion_reg("k", 1.0);
 	ion_reg("cal", 2.0);
 	_k_sym = hoc_lookup("k_ion");
 	_cal_sym = hoc_lookup("cal_ion");
 	register_mech(_mechanism, nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init, hoc_nrnpointerindex, 5);
  _extcall_thread = (Datum*)ecalloc(4, sizeof(Datum));
  _thread_mem_init(_extcall_thread);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
     _nrn_setdata_reg(_mechtype, _setdata);
     _nrn_thread_reg(_mechtype, 1, _thread_mem_init);
     _nrn_thread_reg(_mechtype, 0, _thread_cleanup);
     _nrn_thread_reg(_mechtype, 2, _update_ion_pointer);
 #if NMODL_TEXT
  hoc_reg_nmodl_text(_mechtype, nmodl_file_text);
  hoc_reg_nmodl_filename(_mechtype, nmodl_filename);
#endif
  hoc_register_prop_size(_mechtype, 11, 5);
  hoc_register_dparam_semantics(_mechtype, 0, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 1, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 2, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 3, "cal_ion");
  hoc_register_dparam_semantics(_mechtype, 4, "cvodeieq");
 	hoc_register_cvode(_mechtype, _ode_count, _ode_map, _ode_spec, _ode_matsol);
 	hoc_register_tolerance(_mechtype, _hoc_state_tol, &_atollist);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 K_AHP3_lpool /home/mohacsi/Desktop/optimizer/optimizer/new_test_files/Luca_modell_new/K_AHP3_lpool.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
static int _reset;
static char *modelname = "Channel: K_AHP";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
static int settables(_threadargsprotocomma_ double, double);
 
#define _deriv1_advance _thread[0]._i
#define _dith1 1
#define _recurse _thread[2]._i
#define _newtonspace1 _thread[3]._pvoid
extern void* nrn_cons_newtonspace(int);
 
static int _ode_spec1(_threadargsproto_);
/*static int _ode_matsol1(_threadargsproto_);*/
 static int _slist2[1];
  static int _slist1[1], _dlist1[1];
 static int states(_threadargsproto_);
 
/*CVODE*/
 static int _ode_spec1 (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {int _reset = 0; {
   settables ( _threadargscomma_ v , cali ) ;
   Dm = ( minf - m ) / mtau ;
   }
 return _reset;
}
 static int _ode_matsol1 (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
 settables ( _threadargscomma_ v , cali ) ;
 Dm = Dm  / (1. - dt*( ( ( ( - 1.0 ) ) ) / mtau )) ;
  return 0;
}
 /*END CVODE*/
 
static int states (double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {int _reset=0; int error = 0;
 { double* _savstate1 = _thread[_dith1]._pval;
 double* _dlist2 = _thread[_dith1]._pval + 1;
 int _counte = -1;
 if (!_recurse) {
 _recurse = 1;
 {int _id; for(_id=0; _id < 1; _id++) { _savstate1[_id] = _p[_slist1[_id]];}}
 error = nrn_newton_thread(_newtonspace1, 1,_slist2, _p, states, _dlist2, _ppvar, _thread, _nt);
 _recurse = 0; if(error) {abort_run(error);}}
 {
   settables ( _threadargscomma_ v , cali ) ;
   Dm = ( minf - m ) / mtau ;
   {int _id; for(_id=0; _id < 1; _id++) {
if (_deriv1_advance) {
 _dlist2[++_counte] = _p[_dlist1[_id]] - (_p[_slist1[_id]] - _savstate1[_id])/dt;
 }else{
_dlist2[++_counte] = _p[_slist1[_id]] - _savstate1[_id];}}}
 } }
 return _reset;}
 
static int  settables ( _threadargsprotocomma_ double _lv , double _lcai ) {
   double _lalpha , _lbeta , _ltau , _linf , _lgamma , _lzeta , _lconc , _ltemp_adj_m , _lA_alpha_m , _lB_alpha_m , _lVhalf_alpha_m , _lA_beta_m , _lB_beta_m , _lVhalf_beta_m ;
  _ltemp_adj_m = 1.0 ;
   _lconc = cali ;
   _lv = _lv * 0.0010 ;
   if ( _lconc < 50.0 ) {
     _lalpha = 0.2 * _lconc ;
     }
   else {
     _lalpha = 10.0 ;
     }
   _lalpha = _lalpha * 0.0010 ;
   _lbeta = 1.0 ;
   _lbeta = _lbeta * 0.0010 ;
   _lv = _lv * 1000.0 ;
   mtau = 1.0 / ( _ltemp_adj_m * ( _lalpha + _lbeta ) ) ;
   minf = _lalpha / ( _lalpha + _lbeta ) ;
    return 0; }
 
static void _hoc_settables(void) {
  double _r;
   double* _p; Datum* _ppvar; Datum* _thread; _NrnThread* _nt;
   if (_extcall_prop) {_p = _extcall_prop->param; _ppvar = _extcall_prop->dparam;}else{ _p = (double*)0; _ppvar = (Datum*)0; }
  _thread = _extcall_thread;
  _nt = nrn_threads;
 _r = 1.;
 settables ( _p, _ppvar, _thread, _nt, *getarg(1) , *getarg(2) );
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
  cali = _ion_cali;
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
  cali = _ion_cali;
 _ode_matsol_instance1(_threadargs_);
 }}
 
static void _thread_mem_init(Datum* _thread) {
   _thread[_dith1]._pval = (double*)ecalloc(2, sizeof(double));
   _newtonspace1 = nrn_cons_newtonspace(1);
 }
 
static void _thread_cleanup(Datum* _thread) {
   free((void*)(_thread[_dith1]._pval));
   nrn_destroy_newtonspace(_newtonspace1);
 }
 extern void nrn_update_ion_pointer(Symbol*, Datum*, int, int);
 static void _update_ion_pointer(Datum* _ppvar) {
   nrn_update_ion_pointer(_k_sym, _ppvar, 0, 0);
   nrn_update_ion_pointer(_k_sym, _ppvar, 1, 3);
   nrn_update_ion_pointer(_k_sym, _ppvar, 2, 4);
   nrn_update_ion_pointer(_cal_sym, _ppvar, 3, 1);
 }

static void initmodel(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt) {
  int _i; double _save;{
  m = m0;
 {
   ek = - 80.0 ;
   settables ( _threadargscomma_ v , cali ) ;
   m = minf ;
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
  ek = _ion_ek;
  cali = _ion_cali;
 initmodel(_p, _ppvar, _thread, _nt);
 }
}

static double _nrn_current(double* _p, Datum* _ppvar, Datum* _thread, _NrnThread* _nt, double _v){double _current=0.;v=_v;{ {
   gion = gmax * ( pow( ( 1.0 * m ) , 1.0 ) ) ;
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
  cali = _ion_cali;
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
double _dtsav = dt;
if (secondorder) { dt *= 0.5; }
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
  cali = _ion_cali;
 {  _deriv1_advance = 1;
 derivimplicit_thread(1, _slist1, _dlist1, _p, states, _ppvar, _thread, _nt);
_deriv1_advance = 0;
     if (secondorder) {
    int _i;
    for (_i = 0; _i < 1; ++_i) {
      _p[_slist1[_i]] += dt*_p[_dlist1[_i]];
    }}
 } }}
 dt = _dtsav;
}

static void terminal(){}

static void _initlists(){
 double _x; double* _p = &_x;
 int _i; static int _first = 1;
  if (!_first) return;
 _slist1[0] = &(m) - _p;  _dlist1[0] = &(Dm) - _p;
 _slist2[0] = &(m) - _p;
_first = 0;
}

#if defined(__cplusplus)
} /* extern "C" */
#endif

#if NMODL_TEXT
static const char* nmodl_filename = "/home/mohacsi/Desktop/optimizer/optimizer/new_test_files/Luca_modell_new/K_AHP3_lpool.mod";
static const char* nmodl_file_text = 
  "COMMENT\n"
  "\n"
  "   **************************************************\n"
  "   File generated by: neuroConstruct v1.5.1 \n"
  "   **************************************************\n"
  "\n"
  "   This file holds the implementation in NEURON of the Cell Mechanism:\n"
  "   K_AHP (Type: Channel mechanism, Model: ChannelML based process)\n"
  "\n"
  "   with parameters: \n"
  "   /channelml/@units = SI Units \n"
  "   /channelml/notes = A channel from Maex, R and De Schutter, E. Synchronization of Golgi and Granule Cell Firing in a     Detailed Network Model of the Cerebellar Granule  ... \n"
  "   /channelml/channel_type/@name = K_AHP \n"
  "   /channelml/channel_type/@density = yes \n"
  "   /channelml/channel_type/current_voltage_relation/@cond_law = ohmic \n"
  "   /channelml/channel_type/current_voltage_relation/@ion = k \n"
  "   /channelml/channel_type/current_voltage_relation/@default_gmax = 20 \n"
  "   /channelml/channel_type/current_voltage_relation/@default_erev = -0.08 \n"
  "   /channelml/channel_type/current_voltage_relation/conc_dependence/@name = Calcium \n"
  "   /channelml/channel_type/current_voltage_relation/conc_dependence/@ion = ca \n"
  "   /channelml/channel_type/current_voltage_relation/conc_dependence/@charge = 2 \n"
  "   /channelml/channel_type/current_voltage_relation/conc_dependence/@variable_name = conc \n"
  "   /channelml/channel_type/current_voltage_relation/conc_dependence/@min_conc = 0 \n"
  "   /channelml/channel_type/current_voltage_relation/conc_dependence/@max_conc = 1000 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/@name = m \n"
  "   /channelml/channel_type/current_voltage_relation/gate/@instances = 1 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/closed_state/@id = m0 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/open_state/@id = m \n"
  "   /channelml/channel_type/current_voltage_relation/gate/open_state/@fraction = 1 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[1]/@name = alpha \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[1]/@from = m0 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[1]/@to = m \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[1]/@expr_form = generic \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[1]/@expr = conc &lt; 500 ? 0.02*conc : 10.0 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[2]/@name = beta \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[2]/@from = m \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[2]/@to = m0 \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[2]/@expr_form = generic \n"
  "   /channelml/channel_type/current_voltage_relation/gate/transition[2]/@expr = conc &lt; 500 ? -0.02*conc + 1.0 : -9.0 \n"
  "   /channelml/channel_type/impl_prefs/table_settings/@max_v = 0.05 \n"
  "   /channelml/channel_type/impl_prefs/table_settings/@min_v = -0.1 \n"
  "   /channelml/channel_type/impl_prefs/table_settings/@table_divisions = 300 \n"
  "\n"
  "// File from which this was generated: /home/kali/nC_projects/CA1_NEURON/cellMechanisms/K_AHP/K_AHP.xml\n"
  "\n"
  "// XSL file with mapping to simulator: /home/kali/nC_projects/CA1_NEURON/cellMechanisms/K_AHP/ChannelML_v1.8.1_NEURONmod.xsl\n"
  "\n"
  "ENDCOMMENT\n"
  "\n"
  "\n"
  "?  This is a NEURON mod file generated from a ChannelML file\n"
  "\n"
  "?  Unit system of original ChannelML file: SI Units\n"
  "\n"
  "COMMENT\n"
  "    A channel from Maex, R and De Schutter, E. Synchronization of Golgi and Granule Cell Firing in a\n"
  "    Detailed Network Model of the Cerebellar Granule Cell Layer\n"
  "ENDCOMMENT\n"
  "\n"
  "TITLE Channel: K_AHP\n"
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
  "    SUFFIX K_AHP3_lpool\n"
  "    USEION k READ ek WRITE ik VALENCE 1  ? reversal potential of ion is read, outgoing current is written\n"
  "           \n"
  "        \n"
  "    USEION cal READ cali VALENCE 2 ? internal concentration of ion is read\n"
  "\n"
  "    \n"
  "    RANGE gmax, gion\n"
  "    \n"
  "    RANGE minf, mtau\n"
  "    \n"
  "}\n"
  "\n"
  "PARAMETER { \n"
  "      \n"
  "\n"
  "    gmax = 0.0020 (S/cm2)  ? default value, should be overwritten when conductance placed on cell\n"
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
  "          \n"
  "\n"
  "    ? The internal concentration of ion: ca is used in the rate equations...\n"
  "    cali (mM)   \n"
  "    \n"
  "    \n"
  "    gion (S/cm2)\n"
  "    minf\n"
  "    mtau (ms)\n"
  "    \n"
  "}\n"
  "\n"
  "BREAKPOINT { SOLVE states METHOD derivimplicit     \n"
  "\n"
  "    gion = gmax*((1*m)^1)      \n"
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
  "    settables(v,cali)\n"
  "    m = minf\n"
  "        \n"
  "    \n"
  "}\n"
  "    \n"
  "STATE {\n"
  "    m\n"
  "    \n"
  "}\n"
  "\n"
  "DERIVATIVE states {\n"
  "    settables(v,cali)\n"
  "    m' = (minf - m)/mtau\n"
  "    \n"
  "}\n"
  "\n"
  "PROCEDURE settables(v(mV), cai(mM)) {  \n"
  "    \n"
  "    ? Note: not all of these may be used, depending on the form of rate equations\n"
  "    LOCAL  alpha, beta, tau, inf, gamma, zeta, conc, temp_adj_m, A_alpha_m, B_alpha_m, Vhalf_alpha_m, A_beta_m, B_beta_m, Vhalf_beta_m\n"
  "    \n"
  "    \n"
  "    UNITSOFF\n"
  "    temp_adj_m = 1\n"
  "    \n"
  "    ? Gate depends on the concentration of ca\n"
  "    conc = cali ? In NEURON, the variable for the concentration  of ca is cali\n"
  "    \n"
  "            \n"
  "                \n"
  "           \n"
  "\n"
  "        \n"
  "    ?      ***  Adding rate equations for gate: m  ***\n"
  "         \n"
  "    ? Found a generic form of the rate equation for alpha, using expression: conc < 500 ? 0.02*conc : 10.0\n"
  "    \n"
  "    ? Note: Equation (and all ChannelML file values) in SI Units so need to convert v first...\n"
  "    \n"
  "    v = v * 0.0010   ? temporarily set v to units of equation...\n"
  "            \n"
  "    \n"
  "    \n"
  "    if (conc < 50 ) {\n"
  "        alpha =  0.2*conc \n"
  "    } else {\n"
  "        alpha =  10.0\n"
  "    }\n"
  "    ? Set correct units of alpha for NEURON\n"
  "    alpha = alpha * 0.0010 \n"
  "    \n"
  "    beta =  1.0\n"
  "\n"
  "    ? Set correct units of beta for NEURON\n"
  "    beta = beta * 0.0010 \n"
  "    \n"
  "    v = v * 1000   ? reset v\n"
  "        \n"
  "    mtau = 1/(temp_adj_m*(alpha + beta))\n"
  "    minf = alpha/(alpha + beta)\n"
  "          \n"
  "       \n"
  "    \n"
  "    ?     *** Finished rate equations for gate: m ***\n"
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
