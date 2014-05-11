// genesis

//
// match_iclamp.g: sum of squares loss function
//

// This function calculates the sum of squared difference between simulated
// clamp current output and target data

function diff_comp
    int i
    float diff
    float match

    setfield /current_c table =-=/idata_c/table
    call /current_c TABOP S
    match = 1e9*{getfield /current_c output}

    return {match}
end
