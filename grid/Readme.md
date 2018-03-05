
## Running calibration on grid

The bunch of scripts is designed to run calibration **from scratch** using the grid.
The default scripts run with qsub but can be easily reshuffled to use another job submission interface.

2 different scripts are provided to run the full calibration
- One for the single particle simulation submission
- One for the full calibration

A default steering file for job submission is provided in *steering/default-settings.cfg*. You can copy it and redefined all variables as you need for your job submission. All variables defined in this configuration file are documentation inside the file.

**!! Warning !!** 

When you submit a bunch a jobs with these files, make sure you start your job in a directory where you have enough space for storage.

### Run ddsim simulation

```shell
grid/jobs/qsub-ddsim-single-particle-jobs your-settings-file.cfg
```

and wait for jobs to be finished before going to the next step. This will produce all the simulation samples needed for your calibration.

### Run the main calibration

```shell
./nafhh/calibration/qsub-full-calibration-jobs your-settings-file.cfg
```

and wait for jobs to be finished before going to the next step. This will run the full calibration and save some output in your pool directory (see config file). Here after, an example of files you can find after processing the full calibration :

- calibration-sv01-19-05-GILD_l5_o1_v02-ILDCalibration.xml: The final xml output containing the new calibration constants for your detector
- Calibration-sv01-19-05-GILD_l5_o1_v02-ILDCalibration_constants.xml: The final Marlin xml file containing the final calibration constants. This file can be included using the include mechanism of MarlinXML.
- A bunch of root files, used for the software compensation training
  - MarlinSoftwareCompensation-sv01-19-05-GILD_l5_o1_v02-Pkaon0L-E10-calibration-combined.root
  - MarlinSoftwareCompensation-sv01-19-05-GILD_l5_o1_v02-Pkaon0L-E20-calibration-combined.root
  - MarlinSoftwareCompensation-sv01-19-05-GILD_l5_o1_v02-Pkaon0L-E30-calibration-combined.root
  - ...
- the directory *checkPlots-sv01-19-05-GILD_l5_o1_v02/* contains check plots output from different calibration steps, in root macros (.C) and image formats (.png).

