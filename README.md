# GearCalc

## Overview

GearCalc is a Python module designed to perform calculations related to gear design and analysis. It provides functions for computing parameters such as Pitch Diameter (PD) and Center Distance (CD) based on given inputs.

## Functions

#### calc_PD(teeth_Z, modules)

This function calculates the Pitch Diameter (PD) for each gear in a gear system based on the number of teeth and the module.

### Parameters

- teeth_Z: List of integers representing the number of teeth for each gear.
- modules: The module value for the gear system.
  
### Returns
- A list containing the calculated Pitch Diameter for each gear.
  
#### calc_CD(pitch_dia)
This function computes the Center Distance (CD) for a gear system based on the pitch diameters of the gears.

### Parameters
pitch_dia: List of floats representing the pitch diameter for each gear.

### Returns
The Center Distance (CD) for the gear system.

## Example Usage

```python
# Import the GearCalc module
from gearcalc import calc_PD, calc_CD

# Define input parameters
teeth_Z = [20, 30, 40]  # Number of teeth for each gear
module = 1.5            # Module value

# Calculate Pitch Diameter (PD)
pd_values = calc_PD(teeth_Z, module)
print("Pitch Diameter (PD) for each gear:", pd_values)

# Calculate Center Distance (CD)
cd_value = calc_CD(pd_values)
print("Center Distance (CD) for the gear system:", cd_value)
```

## Installation

You can install GearCalc using pip:

```
pip install gearcalc
```


