
import json

import jk_jsoncfghelper2

from .flexdata import FlexObject





#
# Load data from a file and check it against the structure <c>checkerName</c> defined in <c>scmgr</c>.
#
# @param	str filePath										The path of the file to load.
# @param	jk_jsoncfghelper2.StructureCheckerManager scmgr		The structure checker manager that holds the verification schemas
# @param	str structureTypeName								The name of the structure type the data should be conform to
# @return	FlexObject		A <c>FlexObject</c>.
#
def loadFromFile(filePath:str, scmgr:jk_jsoncfghelper2.StructureCheckerManager = None, structureTypeName:str = None) -> FlexObject:
	assert isinstance(filePath, str)
	if scmgr or structureTypeName:
		assert isinstance(scmgr, jk_jsoncfghelper2.StructureCheckerManager)
		assert isinstance(structureTypeName, str)

	with open(filePath, "r") as f:
		data = json.load(f)
	assert isinstance(data, dict)

	if scmgr or structureTypeName:
		checker = scmgr.get(structureTypeName)
		if checker.checkB(scmgr, data):
			return FlexObject(data)
		else:
			raise Exception("Data does not match type " + repr(structureTypeName))	# TODO
	else:
		return FlexObject(data)
#

#
# Convert the data and check it against the structure <c>checkerName</c> defined in <c>scmgr</c>.
#
# @param	dict data											The data.
# @param	jk_jsoncfghelper2.StructureCheckerManager scmgr		The structure checker manager that holds the verification schemas
# @param	str structureTypeName								The name of the structure type the data should be conform to
# @return	FlexObject		A <c>FlexObject</c>.
#
def createFromData(data:dict, scmgr:jk_jsoncfghelper2.StructureCheckerManager = None, structureTypeName:str = None) -> FlexObject:
	if scmgr or structureTypeName:
		assert isinstance(scmgr, jk_jsoncfghelper2.StructureCheckerManager)
		assert isinstance(structureTypeName, str)

	assert isinstance(data, dict)

	if scmgr or structureTypeName:
		checker = scmgr.get(structureTypeName)
		if checker.checkB(scmgr, data):
			return FlexObject(data)
		else:
			raise Exception("Data does not match type " + repr(structureTypeName))	# TODO
	else:
		return FlexObject(data)
#





__version__ = "0.2019.8.22"



