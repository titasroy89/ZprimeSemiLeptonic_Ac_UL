# EFT Reweighting Tools

This directory contains tools for calculating and applying EFT reweighting using structure constants.

## Overview

The workflow consists of two main steps:

1. Calculate structure constants from the EFT weights in a ROOT file
2. Use these structure constants to calculate reweighted distributions for different Wilson coefficient values

## Scripts

### 1. `calc_structure_constants.py`

This script calculates the structure constants from the EFT weights in a ROOT file.

```bash
python calc_structure_constants.py <input.root> <output.npy>
```

Example:
```bash
python calc_structure_constants.py /path/to/your/file.root structure_constants.npy
```

### 2. `plot_deltaY_shape.py`

This script uses the structure constants to calculate reweighted distributions for different Wilson coefficient values.

#### Usage

```bash
python plot_deltaY_shape.py <structure_constants.npy> <root_file> [--custom-wc] [--print-only]
```

#### Options

- `--custom-wc`: Use custom Wilson coefficient values defined in the script
- `--print-only`: Just print weights for the first 10 events instead of making plots

#### Examples

1. Default mode (sets one Wilson coefficient to 10, all others to 0):
   ```bash
   python plot_deltaY_shape.py structure_constants.npy myfile.root
   ```

2. Use custom Wilson coefficient values and create plots:
   ```bash
   python plot_deltaY_shape.py structure_constants.npy myfile.root --custom-wc
   ```

3. Use custom Wilson coefficient values and just print weights without plotting:
   ```bash
   python plot_deltaY_shape.py structure_constants.npy myfile.root --custom-wc --print-only
   ```

## Setting Custom Wilson Coefficient Values

To set custom Wilson coefficient values, edit the `CUSTOM_WC_VALUES` dictionary at the top of the `plot_deltaY_shape.py` script:

```python
# Define your custom Wilson coefficient values here
# Modify these values as needed for your analysis
CUSTOM_WC_VALUES = {
    "ctGRe": 5.0,
    "ctGIm": 5.0,
    # Add more as needed
    # "cQj18": 0.0,
    # "cQj38": 0.0,
    # etc.
}
```

For example, to set `ctGRe=3.0` and `cQj11=2.0`, change it to:

```python
CUSTOM_WC_VALUES = {
    "ctGRe": 3.0,
    "cQj11": 2.0
}
```

## Available Wilson Coefficients

The following Wilson coefficients are available:

- `ctGRe` (index 0)
- `ctGIm` (index 1)
- `cQj18` (index 2)
- `cQj38` (index 3)
- `cQj11` (index 4)
- `cQj31` (index 5)
- `ctu8` (index 6)
- `ctd8` (index 7)
- `ctj8` (index 8)
- `cQu8` (index 9)
- `cQd8` (index 10)
- `ctu1` (index 11)
- `ctd1` (index 12)
- `ctj1` (index 13)
- `cQu1` (index 14)
- `cQd1` (index 15)

## Example Workflow

1. Calculate structure constants:
   ```bash
   python calc_structure_constants.py /path/to/your/file.root structure_constants.npy
   ```

2. Edit the `CUSTOM_WC_VALUES` dictionary in `plot_deltaY_shape.py` to set your desired Wilson coefficient values.

3. Run the plotting script with custom values:
   ```bash
   python plot_deltaY_shape.py structure_constants.npy /path/to/your/file.root --custom-wc
   ```

4. Or just print the weights for the first 10 events:
   ```bash
   python plot_deltaY_shape.py structure_constants.npy /path/to/your/file.root --custom-wc --print-only
   ```

## Output

When using the `--print-only` option, you'll see output like this:

```
Using Wilson coefficient configuration:
  ctGRe = 5
  ctGIm = 5

Weights for the first 10 events:
Event      SM Weight        EFT Weight       Ratio (EFT/SM)  
------------------------------------------------------------
0          1.00057         1.12345          1.12281         
1          0.998765        1.23456          1.23609         
2          1.00123         0.987654         0.986456        
...
```

When creating plots, the output filenames will include the WC configuration, making it easy to identify which plots correspond to which configuration. For example:

```
DeltaY_reco_EFT_vs_SM_normalized_overlay_ctGRe_5_ctGIm_5.pdf
```
