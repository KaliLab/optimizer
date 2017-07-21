// genesis

//
// paramfuncs.g: helper functions for parameter searches.
//

// This function adjusts the Rm of all compartments

function adjust_Rm(table, i, path)
    str   table
    int   i
    str   path
    int compt
    float old_Rm,new_Rm

    for(compt=1; compt < 6; compt = compt + 1)
	old_Rm = {getfield {path}/{compt} Rm}
	new_Rm = {old_Rm} * {getfield {table} current[{i}]}
	setfield {path}/{compt} Rm {new_Rm}
    end
end

// This function adjusts the Cm of all compartments

function adjust_Cm(table, i, path)
    str   table
    int   i
    str   path
    int compt
    float old_Cm,new_Cm
    
    for(compt=1; compt < 6; compt = compt + 1)
	old_Cm = {getfield {path}/{compt} Cm}
	new_Cm = {old_Cm} * {getfield {table} current[{i}]}
	setfield {path}/{compt} Cm {new_Cm}
    end
end

// This function adjusts the ratio of the membrane area of a compartment
// compared to the soma

function adjust_area_ratio(table, i, path)
    str   table
    int   i
    str   path, chname

    float old_area_ratio = {{getfield {path}/../1 Rm} / {getfield {path} Rm}}
    float new_area_ratio = {old_area_ratio} * {getfield {table} current[{i}]}
    float new_Rm = {{getfield {path}/../1 Rm} / {new_area_ratio}}
    float new_Cm = {{getfield {path}/../1 Cm} * {new_area_ratio}}
    setfield {path} Rm {new_Rm}
    setfield {path} Cm {new_Cm}
    float old_Caconc = {getfield {path}/Ca_conc B}
    float new_Caconc = old_Caconc / {getfield {table} current[{i}]}
    setfield {path}/Ca_conc B {new_Caconc}
    foreach chname ({el {path}/#[CLASS=channel]})
	if ({exists {chname} Gbar})
	    float old_Gbar = {getfield {chname} Gbar}
	    float new_Gbar = old_Gbar * {getfield {table} current[{i}]}
	    setfield {chname} Gbar {new_Gbar}
	end
    end

end

// This function adjusts the axial resistance of a (dendritic) compartment

function adjust_Ra(table, i, path)
    str   table
    int   i
    str   path

    float old_Ra = {getfield {path} Ra}
    float new_Ra = {old_Ra} * {getfield {table} current[{i}]}
    setfield {path} Ra {new_Ra}
end

// This function adjusts the maximal conductance of a channel:

function adjust_Gbar(table, i, path)
    str   table
    int   i
    str   path

    float old_Gbar = {getfield {path} Gbar}
    float new_Gbar = old_Gbar * {getfield {table} current[{i}]}
    setfield {path} Gbar {new_Gbar}
end


// This function adjusts the midpoint of an activation curve:

function adjust_minf(table, i, gate, path)
    str   table
    int   i
    str   gate
    str   path

    float offset = {getfield {table} current[{i}]}

    if ({strcmp {gate} "X"} == 0)
        scaletabchan {path} X minf 1.0 1.0 {offset} 0.0
    elif ({strcmp {gate} "Y"} == 0)
        scaletabchan {path} Y minf 1.0 1.0 {offset} 0.0
    elif ({strcmp {gate} "Z"} == 0)
        scaletabchan {path} Z minf 1.0 1.0 {offset} 0.0
    end
end


// This function scales the tau(V) values of a channel
// activation curve by some amount.

function adjust_tau(table, i, gate, path)
    str   table
    int   i
    str   gate
    str   path

    float scale = {getfield {table} current[{i}]}

    if ({strcmp {gate} "X"} == 0)
         scaletabchan {path} X tau 1.0 {scale} 0.0 0.0
    elif ({strcmp {gate} "Y"} == 0)
        scaletabchan {path} Y tau 1.0 {scale} 0.0 0.0
    elif ({strcmp {gate} "Z"} == 0)
        scaletabchan {path} Z tau 1.0 {scale} 0.0 0.0
    end
end


