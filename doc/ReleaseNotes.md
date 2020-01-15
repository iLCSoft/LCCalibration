# v00-00

* 2018-04-10 Ete Remi ([PR#19](https://github.com/iLCSoft/LCCalibration/pull/19))
  - Implemented new geometry interface DDGeometryInterface
      - Use DDRec python library to deal with geometry
  - Removed Gear function calls from all calibration steps
  - Overhauled ILD and SiD calibration runner scripts to deal only with DD4hep
  - print-cos-theta-ranges.py script
      - Print both Gear and DD4hep implementation of cos theta range for cross check
  - Added empty ReleaseNotes.md for future releases

* 2018-03-07 Ete Remi ([PR#17](https://github.com/iLCSoft/LCCalibration/pull/17))
  - New grid scripts allowing to run ILD calibration all-in-one
     - Run ddsim calibration for all particle types all-in-one
     - Run full calibration all-in-one
  - Grid scripts documentation updated

* 2018-03-02 Ete Remi ([PR#16](https://github.com/iLCSoft/LCCalibration/pull/16))
  - CalibrationStep:
    - Added setter to specify processors to turnoff
  - All calibration steps turn off specified list of processors if any
  - ILD calibration runner: 
    - Removed REC and DST processors setter for Pandora step (superseded by CalibrationStep new method)
    - Turn off REC and DST processors in all calibration steps to avoid un-necessary disk space usage

* 2018-03-01 Ete Remi ([PR#15](https://github.com/iLCSoft/LCCalibration/pull/15))
  - Added --pandoraSettings argument to cmd line. 
  - Argument required by all Pandora calibration steps
    - Pandora EM scale step
    - Pandora Had scale step 
    - Pandora software compensation step

* 2018-03-01 Ete Remi ([PR#14](https://github.com/iLCSoft/LCCalibration/pull/14))
  - extract-marlin-constants.py:
    - adjusted to find `<constant>` xml elements with end tag `</constant>` or `/>` on same line

* 2018-03-01 Ete Remi ([PR#13](https://github.com/iLCSoft/LCCalibration/pull/13))
  - ILD calibration runner: 
    - Changed MySimpleMuonDigi to MyDDSimpleMuonDigi

* 2018-03-01 Ete Remi ([PR#12](https://github.com/iLCSoft/LCCalibration/pull/12))
  - ILD calibration parameters:
    - Updated MySimpleMuonDigi to MyDDSimpleMuonDigi

* 2018-02-08 Ete Remi ([PR#10](https://github.com/iLCSoft/LCCalibration/pull/10))
  - Removed include element parsing from XMLParser
  - Requires to have a pre-processed Marlin XML file to run properly the calibration
  - Documentation updated

* 2018-02-07 Ete Remi ([PR#9](https://github.com/iLCSoft/LCCalibration/pull/9))
  - Removed unused scripts
     - calibrate-software-compensation.py 
     - replace-software-compensation-parameters.py 
     - run-single-particle.py
  - Improved init.sh script : can be sourced from any place
  - Updated documentation

* 2017-11-22 Ete Remi ([PR#7](https://github.com/iLCSoft/LCCalibration/pull/7))
  - Added extract-marlin-constants.py script to get calibration constants from Marlin constants file instead of top level steering file

* 2017-11-22 Ete Remi ([PR#6](https://github.com/iLCSoft/LCCalibration/pull/6))
  - Removed exception throw in case a processor parameter or global parameter doesn't exists and warn instead

* 2017-11-22 Ete Remi ([PR#5](https://github.com/iLCSoft/LCCalibration/pull/5))
  - Added option in Pandora steps (EM and Had scale) to remove the execution of REC and DST files
  - Set MyLCIOOutputProcessor and DSTOutput processor to be removed for the ILD calibration

* 2017-11-21 Ete Remi ([PR#4](https://github.com/iLCSoft/LCCalibration/pull/4))
  - Deal with Marlin constants section : 
    - Added script to generate a Marlin constants file from calibration parameters and calibration XML file
    - Modified ILD and SiD calibration parameter script to deal with this script

* 2017-11-13 Dan Protopopescu ([PR#3](https://github.com/iLCSoft/LCCalibration/pull/3))
  - Changed incorrect MySimpleMuonDigi to MyDDSimpleMuonDigi

* 2017-11-10 Dan Protopopescu ([PR#1](https://github.com/iLCSoft/LCCalibration/pull/1))
  - Updated python script with the corrects processors, and Gear plugin
  - Added compatibility comments