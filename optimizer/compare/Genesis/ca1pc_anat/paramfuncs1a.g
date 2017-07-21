// genesis

//
// paramfuncs.g: helper functions for parameter searches.
//

// This function adjusts the Rm of all compartments

function adjust_Rm(table, i, path)
    str   table
    int   i
    str   path,compt
    float old_Rm,new_Rm

    foreach compt ({el {path}/#[ISA=compartment]})
	old_Rm = {getfield {compt} Rm}
	new_Rm = {old_Rm} * {getfield {table} current[{i}]}
	setfield {compt} Rm {new_Rm}
    end
end

// This function adjusts the Cm of all compartments

function adjust_Cm(table, i, path)
    str   table
    int   i
    str   path,compt
    float old_Cm,new_Cm
    
    foreach compt ({el {path}/#[ISA=compartment]})
	old_Cm = {getfield {compt} Cm}
	new_Cm = {old_Cm} * {getfield {table} current[{i}]}
	setfield {compt} Cm {new_Cm}
    end
end

// This function adjusts the axial resistance of all compartments

function adjust_Ra(table, i, path)
    str   table
    int   i
    str   path,compt
    float old_Ra,new_Ra

    foreach compt ({el {path}/#[ISA=compartment]})
        old_Ra = {getfield {compt} Ra}
        new_Ra = {old_Ra} * {getfield {table} current[{i}]}
        setfield {compt} Ra {new_Ra}
    end
end

