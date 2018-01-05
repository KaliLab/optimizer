#include <stdio.h>
#include "hocdec.h"
extern int nrnmpi_myid;
extern int nrn_nobanner_;

extern void _CaL_reg(void);
extern void _CaN_reg(void);
extern void _CaR_reg(void);
extern void _CaT_reg(void);
extern void _Ca_conc_dend2_reg(void);
extern void _Ca_conc_dend2a_reg(void);
extern void _Ca_conc_dend3_reg(void);
extern void _Ca_conc_dend4_reg(void);
extern void _Ca_conc_dend5_reg(void);
extern void _Ca_conc_soma_reg(void);
extern void _H_CA1pyr_dist_reg(void);
extern void _H_CA1pyr_prox_reg(void);
extern void _K_AHP_reg(void);
extern void _K_A_dist_reg(void);
extern void _K_A_prox_reg(void);
extern void _K_C_1D_reg(void);
extern void _K_DR_reg(void);
extern void _K_M_reg(void);
extern void _Leak_pyr_reg(void);
extern void _Na_dend_reg(void);
extern void _Na_soma_reg(void);

void modl_reg(){
  if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
    fprintf(stderr, "Additional mechanisms from files\n");

    fprintf(stderr," CaL.mod");
    fprintf(stderr," CaN.mod");
    fprintf(stderr," CaR.mod");
    fprintf(stderr," CaT.mod");
    fprintf(stderr," Ca_conc_dend2.mod");
    fprintf(stderr," Ca_conc_dend2a.mod");
    fprintf(stderr," Ca_conc_dend3.mod");
    fprintf(stderr," Ca_conc_dend4.mod");
    fprintf(stderr," Ca_conc_dend5.mod");
    fprintf(stderr," Ca_conc_soma.mod");
    fprintf(stderr," H_CA1pyr_dist.mod");
    fprintf(stderr," H_CA1pyr_prox.mod");
    fprintf(stderr," K_AHP.mod");
    fprintf(stderr," K_A_dist.mod");
    fprintf(stderr," K_A_prox.mod");
    fprintf(stderr," K_C_1D.mod");
    fprintf(stderr," K_DR.mod");
    fprintf(stderr," K_M.mod");
    fprintf(stderr," Leak_pyr.mod");
    fprintf(stderr," Na_dend.mod");
    fprintf(stderr," Na_soma.mod");
    fprintf(stderr, "\n");
  }
  _CaL_reg();
  _CaN_reg();
  _CaR_reg();
  _CaT_reg();
  _Ca_conc_dend2_reg();
  _Ca_conc_dend2a_reg();
  _Ca_conc_dend3_reg();
  _Ca_conc_dend4_reg();
  _Ca_conc_dend5_reg();
  _Ca_conc_soma_reg();
  _H_CA1pyr_dist_reg();
  _H_CA1pyr_prox_reg();
  _K_AHP_reg();
  _K_A_dist_reg();
  _K_A_prox_reg();
  _K_C_1D_reg();
  _K_DR_reg();
  _K_M_reg();
  _Leak_pyr_reg();
  _Na_dend_reg();
  _Na_soma_reg();
}
