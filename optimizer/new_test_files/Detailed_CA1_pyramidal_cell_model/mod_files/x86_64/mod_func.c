#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _cacum_reg(void);
extern void _H_CA1pyr_dist_reg(void);
extern void _H_CA1pyr_prox_reg(void);
extern void _K_A_dist_reg(void);
extern void _K_A_prox_reg(void);
extern void _kd_params3_reg(void);
extern void _K_DRS4_params_voltage_dep_reg(void);
extern void _km_q10_2_reg(void);
extern void _Leak_pyr_reg(void);
extern void _Na_BG_axon_reg(void);
extern void _Na_BG_dend_reg(void);
extern void _Na_BG_soma_reg(void);
extern void _vecevent_reg(void);
extern void _vmax_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," \"cacum.mod\"");
    fprintf(stderr," \"H_CA1pyr_dist.mod\"");
    fprintf(stderr," \"H_CA1pyr_prox.mod\"");
    fprintf(stderr," \"K_A_dist.mod\"");
    fprintf(stderr," \"K_A_prox.mod\"");
    fprintf(stderr," \"kd_params3.mod\"");
    fprintf(stderr," \"K_DRS4_params_voltage_dep.mod\"");
    fprintf(stderr," \"km_q10_2.mod\"");
    fprintf(stderr," \"Leak_pyr.mod\"");
    fprintf(stderr," \"Na_BG_axon.mod\"");
    fprintf(stderr," \"Na_BG_dend.mod\"");
    fprintf(stderr," \"Na_BG_soma.mod\"");
    fprintf(stderr," \"vecevent.mod\"");
    fprintf(stderr," \"vmax.mod\"");
    fprintf(stderr, "\n");
  }
  _cacum_reg();
  _H_CA1pyr_dist_reg();
  _H_CA1pyr_prox_reg();
  _K_A_dist_reg();
  _K_A_prox_reg();
  _kd_params3_reg();
  _K_DRS4_params_voltage_dep_reg();
  _km_q10_2_reg();
  _Leak_pyr_reg();
  _Na_BG_axon_reg();
  _Na_BG_dend_reg();
  _Na_BG_soma_reg();
  _vecevent_reg();
  _vmax_reg();
}
