// genesis

//
// match_vmax.g: sum of squares loss function
//

// This function calculates the sum of squared difference between current
// model voltage output and target data

function diff_comp
    int i
    float diff
    float match

    setfield /voltage_c table =-=/vdata_c/table
    call /voltage_c TABOP S
    match = 1000*{getfield /voltage_c output}

    return {match}
end
