import os

# Update to a path in your system (see details below at "Reference files")
os.environ["CRDS_PATH"] = "/Users/ajshajib/Research/1131_JWST/CRDS/"
os.environ["CRDS_SERVER_URL"] = "https://jwst-crds.stsci.edu"

import glob

import jwst
import stcal

print("# JWST pipe version = {0:s}".format(jwst.__version__))
print("# STCAL version = {0:s}".format(stcal.__version__))

# Packages that allow us to get information about objects:
import asdf

# Astropy tools:
from astropy.io import fits

# JWST data models
from jwst import datamodels

# The entire calwebb_spec2 pipeline
from jwst.pipeline import Detector1Pipeline
from jwst.pipeline.calwebb_spec2 import Spec2Pipeline
from jwst.pipeline.calwebb_spec3 import Spec3Pipeline
from jwst.associations.asn_from_list import asn_from_list
from jwst.associations.lib.rules_level2_base import DMSLevel2bBase
from jwst.associations.lib.rules_level3_base import DMS_Level3_Base

# Individual steps that make up calwebb_spec2 and datamodels
from jwst.assign_wcs.assign_wcs_step import AssignWcsStep
from jwst.background.background_step import BackgroundStep
from jwst.imprint.imprint_step import ImprintStep
from jwst.msaflagopen.msaflagopen_step import MSAFlagOpenStep
from jwst.extract_2d.extract_2d_step import Extract2dStep
from jwst.srctype.srctype_step import SourceTypeStep
from jwst.master_background.master_background_step import MasterBackgroundStep
from jwst.wavecorr.wavecorr_step import WavecorrStep
from jwst.flatfield.flat_field_step import FlatFieldStep
from jwst.straylight.straylight_step import StraylightStep
from jwst.fringe.fringe_step import FringeStep
from jwst.pathloss.pathloss_step import PathLossStep
from jwst.barshadow.barshadow_step import BarShadowStep
from jwst.wfss_contam import WfssContamStep
from jwst.photom.photom_step import PhotomStep
from jwst.resample import ResampleSpecStep
from jwst.cube_build.cube_build_step import CubeBuildStep
from jwst.extract_1d.extract_1d_step import Extract1dStep

# Arrange our directory structure.
# All 16 uncal_directory files should be in the `uncal_files' folder.
# We will place the outputs of each pipeline stage in new folders, easier to keep track of.
here = os.getcwd()
parent_directory = os.path.abspath(os.path.join(here, os.pardir))

uncal_directory = parent_directory + "/data/uncal/"
stage1_directory = parent_directory + "/data/stage1/"
stage1_processed_directory = parent_directory + "/data/stage1_processed/"
stage1_nsclean_directory = parent_directory + "/data/stage1_nsclean/"
stage2_directory = parent_directory + "/data/stage2/"
stage2_processed_directory = parent_directory + "/data/stage2_processed/"
stage2_nsclean_directory = parent_directory + "/data/stage2_nsclean/"
stage3_directory = parent_directory + "/data/stage3/"
stage3_processed_directory = parent_directory + "/data/stage3_processed/"  # For post-pipeline processing

# Create above folders if they don't already exist
for folder in [uncal_directory, stage1_directory, stage2_directory, stage3_directory, stage3_processed_directory]:
    if not os.path.exists(folder):
        os.makedirs(folder)