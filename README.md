# NIRSpec Reduction Pipeline

This repository contains a set of Jupyter notebooks and Python scripts to perform 
data reduction of **NIRSpec** observations from the **JWST**.

## Overview

The notebooks in this repository demonstrate how to apply various stages of data reduction to NIRSpec spectra, such as:

- **Stage 1 reduction**: This notebook shows how to extract the raw data using the 
 detector pipeline and produce rate images.
- **Stage 2 reduction**: This notebook shows how to produce the calibrated cal 
  images using the spec2 pipeline.
- **Run NSClean**: This notebook shows how to apply a custom routine to pattern noise 
  from the calibrated cal images using the `NSClean` pacakage.
- **Stage 3 reduction**: This notebook shows how to combine multiple exposures of 
  the same source into a single datacube using the spec3 pipeline.
- **Clean up SFLAT**: This notebook is a Python script that performs a custom clean 
  up of the SFLAT (spectral flat field) reference file.

Run the notebooks in the following order:

1. Stage 1 reduction
2. Stage 2 reduction (on stage 1 output, not necessary if cal files are downloaded from MAST) 
3. Run NSClean
4. Stage 2 reduction (on NSClean-ed stage 1 output)
5. Stage 3 reduction (on NSClean-ed stage 2 output)
