# RᴇɢᴀʟJᴜᴍᴘᴇʀ: a custom reduction pipeline for JWST/NIRSpec IFU

This repository contains a set of Jupyter notebooks and Python scripts to perform data reduction of **NIRSpec** observations from the **JWST**.

## Overview

The notebooks in this repository demonstrate how to apply various stages of data reduction to NIRSpec spectra, such as:

- **1_Run_Stage_1.ipynb**: This notebook shows how to extract the raw data using the detector pipeline and produce rate images.
- **2_Clean_CR.ipynb**: This notebook cleans outliers and cosmic rays.
- **3_Run_NSClean.ipynb**: This notebook shows how to apply a custom routine to remove $1/f$ noise from the rate images using the `NSClean` package. This step needs some preliminary \*.cal files that can either be downloaded from the MAST server, or can be obtained by running *"4_Run_Stage_2.ipynb"* on the output files from the previous notebook. This notebook uses *"nrs1_trace_mask.fits"*, a hand-drawn mask over the traces on the detector for a more robust cleaning.
- **4_Run_Stage_2.ipynb**: This notebook shows how to produce the calibrated cal images using the spec2 pipeline. The leakcal exposures are subtracted in this stage.
- **5_Run_Stage_3.ipynb**: This notebook shows how to combine multiple exposures of the same source into a single datacube using the spec3 pipeline.