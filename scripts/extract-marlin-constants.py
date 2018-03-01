#!/usr/bin/python

""" Extract, from Marlin steering file, constants that will be used for running the calibration chain
    @author Remi Ete, DESY
"""

import os
import sys
from shutil import copyfile
import argparse
from calibration.XmlTools import *

def getConstant(tree, name):
    elt = tree.xpath("//constants/constant[@name='{0}']".format(name))
    if not elt:
        raise RuntimeError("Constant '{0}' not found in xml file".format(name))
    return elt[0].text

def createCalibrationParameter(tree, processor, name, constant):
    param = getConstant(tree, constant)
    element = etree.Element("parameter", processor=processor, name=name)
    element.text = param
    return element

parser = argparse.ArgumentParser("Extract Marlin steering file constants for calibration purpose:",
                                     formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("--parameterFile", action="store",
                        help="A python file containing the parameter list to extract from Marlin xml file", required = True)

parser.add_argument("--constantFile", action="store",
                        help="The Marlin steering file containing only constants", required = True)

parser.add_argument("--outputFile", action="store",
                        help="The XML output calibration file", required = True)

parsed = parser.parse_args()

userParameters = []

try:
    execfile(parsed.parameterFile)
    userParameters = list(calibrationParameters)
except NameError as e:
    print "Couldn't find user parameters in input python file. Definition of 'calibrationParameter' variable is required !"
    raise e
except:
    raise RuntimeError("Error while import user python file !")
    
# Requires special parsing since the constant file has 
# no root element but is just a list of <constant> elements
# We have to parse the constant file manually, line by line ...
constantFile = open(parsed.constantFile, 'r')
constants = etree.Element("constants")

for line in constantFile:
    if len(line.strip()) > 0 and not line.strip().startswith("<?") and not line.strip().startswith("<!--") and (line.find("</constant>") > 0 or line.strip().endswith("/>")):
        constant = etree.XML(line.strip())
        constants.append(constant)

constantFile.close()
xmlTree = etree.ElementTree(constants)

rootOutput = etree.Element("calibration")
inputElement = etree.Element("input")
rootOutput.append(inputElement)

for param in userParameters:
    processor = param[0]
    parameter = param[1]
    constant = param[2]
    try:
        inputElement.append(createCalibrationParameter(xmlTree, processor, parameter, constant))
    except RuntimeError as e:
        print "!!WARNING!! Constant '{0}' not found in Marlin constants xml file. Skipping ...".format(constant)

# write to output file
outputTree = etree.ElementTree(rootOutput)
outputTree.write(parsed.outputFile, pretty_print=True)

#
