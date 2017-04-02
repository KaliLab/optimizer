// genesis

//
// paramfuncs.g: helper functions for parameter searches.
//

// This function adjusts the maximal conductance of a channel:

function adjust_weight(table, i, path)
    str   table       // index of table for this generation
    int   i           // index of parameter
    str   path

    float old_W = {getfield {path} synapse[0].weight}
    float new_W = old_W * {getfield {table} current[{i}]}
    setfield {path} synapse[0].weight {new_W}
end

function adjust_delay(table, i, path)
    str   table       // index of table for this generation
    int   i           // index of parameter
    str   path

    float old_delay = {getfield {path} synapse[0].delay}
    float new_delay = old_delay * {getfield {table} current[{i}]}
    setfield {path} synapse[0].delay {new_delay}
end

function adjust_tau1(table, i, path)
    str   table       // index of table for this generation
    int   i           // index of parameter
    str   path

    float old_tau1 = {getfield {path} tau1}
    float new_tau1 = old_tau1 * {getfield {table} current[{i}]}
    setfield {path} tau1 {new_tau1}
end

function adjust_tau2(table, i, path)
    str   table       // index of table for this generation
    int   i           // index of parameter
    str   path

    float old_tau2 = {getfield {path} tau2}
    float new_tau2 = old_tau2 * {getfield {table} current[{i}]}
    setfield {path} tau2 {new_tau2}
end

