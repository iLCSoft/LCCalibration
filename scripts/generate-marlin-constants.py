#!/usr/bin/python

""" Generate a steering file for Marlin, containing only a set of constants.
    @author Remi Ete, DESY
"""

import os
import sys
import argparse
from calibration.XmlTools import *

def find(f, seq):
  """Return first item in sequence where f(item) == True."""
  for item in seq:
    if f(item): 
      return item

# command line parsing
parser = argparse.ArgumentParser("Replace Marlin steering file parameters after calibration:",
                                     formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("--inputFile", action="store", default="",
                        help="The XML input calibration file", required = True)

parser.add_argument("--constantsFile", action="store", default="",
                        help="Write output in a Marlin constants file", required = False)

parser.add_argument("--parameterFile", action="store",
                        help="A python file containing the parameter list to write as constants", required = True)

parsed = parser.parse_args()

outputFile = parsed.constantsFile

# open calibration and marlin xml files
xmlParser = createXMLParser()
calibrationXmlTree = etree.parse(parsed.inputFile, xmlParser)

try:
    execfile(parsed.parameterFile)
    userParameters = list(calibrationParameters)
except NameError as e:
    print "Couldn't find user parameters in input python file. Definition of 'calibrationParameter' variable is required !"
    raise e
except:
    raise RuntimeError("Error while import user python file !")

constants = []

for parameter in calibrationXmlTree.xpath("//input/parameter"):
    processor = parameter.get("processor")
    name = parameter.get("name")
    value = parameter.text
    
    constant = find(lambda userParameter: userParameter[0] == processor and userParameter[1] == name, userParameters)
    
    if constant is None:
        continue
    
    constant = constant[2]
    constants.append( [constant, value] )

for parameter in calibrationXmlTree.xpath("//step/output/parameter"):

    processor = parameter.get("processor")
    name = parameter.get("name")
    value = parameter.text
    
    constant = find(lambda userParameter: userParameter[0] == processor and userParameter[1] == name, userParameters)
    
    if constant is None:
        continue
    
    constant = constant[2]
    constantFind = find(lambda c: c[0] == constant, constants)
    
    if constantFind is None:
        constants.append( [constant, value] )
    else:
        constantFind[1] = value

marlinConstantsOutput = open(outputFile, 'w')

for constant in constants:
    marlinConstantsOutput.write('<constant name="{0}">{1}</constant>\n'.format(constant[0], constant[1]))

marlinConstantsOutput.close()


#
