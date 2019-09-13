#!/usr/bin/python3


import jk_flexdata



x = {
	"a": [
		{
			"b": "c"
		}
	]
}

print("****************")

f = jk_flexdata.createFromData(x)

print("****************")

print(f._toDict())

print("****************")








