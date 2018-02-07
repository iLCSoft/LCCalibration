#!/bin/bash

scriptDirectory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export LCCALIBRATION_DIR=${scriptDirectory}
export PYTHONPATH=$LCCALIBRATION_DIR:$PYTHONPATH
