def calc_PD(teeth_Z, modules): 
    PD = []
    for i in range(0, len(teeth_Z)): 
        a = float(teeth_Z[i]) * float(modules)
        PD.append(a)
    return (PD)

## Objective 3

def calc_CD(pitch_dia): 
    CD = 0 
    CD += (pitch_dia[0]/2) + (pitch_dia[-1]/2)
    for i in range(1, len(pitch_dia) - 1):
        CD += int(pitch_dia[i])
    return (CD)
