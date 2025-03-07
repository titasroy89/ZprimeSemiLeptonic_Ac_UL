# EFT Structure Constants and Plotting

This directory contains scripts for calculating structure constants from ROOT files and creating plots for EFT analysis.

## Overview

The main workflow consists of:

1. Calculating structure constants for each ROOT file
2. Creating histograms for various kinematic variables (DeltaYreco, Delta_phi, Sigma_phi)
3. Creating ratio plots comparing EFT to SM distributions

## Scripts

- `calc_structure_constants.py`: Calculates structure constants for a single ROOT file
- `process_all_samples.py`: Enhanced script that processes multiple ROOT files and creates combined plots
- `plot_deltaY_shape.py`: Creates plots for DeltaYreco (now integrated into process_all_samples.py)
- `plot_deltaPhi_sigmaPhi.py`: Creates plots for Delta_phi and Sigma_phi (now integrated into process_all_samples.py)

## Usage

### Main Script: `process_all_samples.py`

This script processes ROOT files to calculate structure constants and create plots.

#### Usage

```bash
python process_all_samples.py [options]
```

#### Options

- `--input-dir PATH`: Directory containing ROOT files to process (default: predefined path)
- `--output-dir PATH`: Directory to store output files (default: 'results')
- `--calc-only`: Only calculate structure constants, skip plotting
- `--plot-only`: Only create plots, skip structure constant calculation
- `--combined-only`: Only create combined ratio plots, skip individual plots
- `--variables VAR1 VAR2 ...`: Variables to plot (default: DeltaYreco Delta_phi Sigma_phi)
- `--custom-wc`: Use custom Wilson coefficient values defined in the script
- `--merge-plots`: Create merged plots from all files
- `--file-pattern PATTERN`: Pattern to match ROOT files (default: *.root)

#### Examples

Process all ROOT files in a directory:
```bash
python process_all_samples.py --input-dir /path/to/root/files --output-dir results --merge-plots
```

Process only files matching a specific pattern:
```bash
python process_all_samples.py --input-dir /path/to/root/files --file-pattern "uhh2.AnalysisModuleRunner.MC.TTbar_*.root" --merge-plots
```

Calculate structure constants only:
```bash
python process_all_samples.py --input-dir /path/to/root/files --calc-only
```

Create plots using existing structure constants:
```bash
python process_all_samples.py --input-dir /path/to/root/files --plot-only --merge-plots
```

### Batch Processing: `submit_batch_jobs.py`

This script submits batch jobs to process multiple ROOT files in parallel using HTCondor.

#### Usage

```bash
python submit_batch_jobs.py [options]
```

#### Options

- `--input-dir PATH`: Directory containing ROOT files to process (required)
- `--output-dir PATH`: Directory to store output files (default: 'results')
- `--calc-only`: Only calculate structure constants, skip plotting
- `--plot-only`: Only create plots, skip structure constant calculation
- `--variables VAR1 VAR2 ...`: Variables to plot (default: DeltaYreco Delta_phi Sigma_phi)
- `--custom-wc`: Use custom Wilson coefficient values defined in the script
- `--file-pattern PATTERN`: Pattern to match ROOT files (default: *.root)

#### Examples

Submit jobs for all ROOT files:
```bash
python submit_batch_jobs.py --input-dir /path/to/root/files --output-dir results
```

Submit jobs for files matching a specific pattern:
```bash
python submit_batch_jobs.py --input-dir /path/to/root/files --file-pattern "uhh2.AnalysisModuleRunner.MC.TTbar_*.root"
```

After all jobs complete, run the generated merge script to combine results:
```bash
./merge_results.sh
```

### Output

The script creates the following outputs:

1. Structure constants for each ROOT file (saved as numpy arrays)
2. Individual plots for each variable and ROOT file
3. Combined plots showing all samples together (if --merge-plots is used)

The plots include:
- SM and EFT distributions
- Ratio plots (EFT/SM)
- Combined ratio plots from all samples

## Customizing Wilson Coefficient Values

To use custom Wilson coefficient values, use the `--custom-wc` flag. The default values are defined in the script and can be modified as needed:

```python
wc_values = {
    "ctGRe": 1.0,
    "ctGIm": 0.0,
    "cQj18": 0.0,
    # ... other coefficients
}
```

## Adding New Variables

To add new variables to plot, simply include them in the `--variables` argument. The script will automatically create histograms and ratio plots for each variable. 