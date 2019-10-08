# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# AddonisWorkflow_02.py
# Created on: 2019-10-08 16:44:40.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: AddonisWorkflow_02 <Prog_001> <Barriers> 
# Description: 
# ---------------------------------------------------------------------------

# Set the necessary product code
import arceditor


# Import arcpy module
import arcpy

# Script arguments
Prog_001 = arcpy.GetParameterAsText(0)
if Prog_001 == '#' or not Prog_001:
    Prog_001 = "C:\\Users\\mpanozzo\\Downloads\\WORK_STAND\\WORK.gdb\\Prog_001" # provide a default value if unspecified

Barriers = arcpy.GetParameterAsText(1)
if Barriers == '#' or not Barriers:
    Barriers = "Selected_Sites" # provide a default value if unspecified

# Local variables:
GeomNetwork = "C:\\Users\\mpanozzo\\Downloads\\WORK_STAND\\WORK.gdb\\Prog_001\\GeomNetwork"
GeomNetwork__2_ = GeomNetwork
Flow_Option = "WITH_DIGITIZED_DIRECTION"
USER_CLICK = ""
GeomTrace = "GeomTrace"
Accumulation_Cost = "-1"

# Process: Create Geometric Network
arcpy.CreateGeometricNetwork_management(Prog_001, "GeomNetwork", "", "", "", "", "", "PRESERVE_ENABLED")

# Process: Set Flow Direction
arcpy.SetFlowDirection_management(GeomNetwork, Flow_Option)

# Process: Trace Geometric Network
arcpy.TraceGeometricNetwork_management(GeomNetwork__2_, GeomTrace, USER_CLICK, "FIND_CONNECTED", Barriers, "", "", "", "", "NO_TRACE_ENDS", "NO_TRACE_INDETERMINATE_FLOW", "", "", "AS_IS", "", "", "", "AS_IS")

