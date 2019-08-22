

import jk_json
import jk_jsoncfghelper2



class _FlexNone(object):

	def __init__(self):
		pass
	#

	def __eq__(self, v):
		return v is None
	#

	def __ne__(self, v):
		return v is not None
	#

	def __getitem__(self, key):
		return self
	#

	def __getattr__(self, key):
		return self
	#

#

NONE = _FlexNone()



class FlexObject(object):

	def __init__(self, data:dict):
		assert isinstance(data, dict)
		self.__data = data

		for key, value in list(data.items()):
			if isinstance(value, dict):
				data[key] = FlexObject(value)
			elif isinstance(value, (list, tuple)):
				_ = []
				for item in value:
					if isinstance(item, dict):
						_.append(FlexObject(item))
					else:
						_.append(item)
				data[key] = _
	#

	def __str__(self):
		s = "F{ " + ", ".join([ ("\"" + x + "\"") for x in sorted(self.__data.keys()) ]) + " }"
		return s
	#

	def __repr__(self):
		s = "F{ " + ", ".join([ ("\"" + x + "\"") for x in sorted(self.__data.keys()) ]) + " }"
		return s
	#

	def __getitem__(self, key):
		v = self.__data.get(key)
		if v is None:
			return NONE
		else:
			return v
	#

	def __getattr__(self, key):
		v = self.__data.get(key)
		if v is None:
			return NONE
		else:
			return v
	#

#





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

	data = jk_json.loadFromFile(filePath)
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







