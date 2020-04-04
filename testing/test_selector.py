#!/usr/bin/python3


from jk_flexdata import *
from jk_testing import Assert




dataTree = FlexObject({
	"a": [
		{
			"b": "cc"
		},
		{
			"e": "ff"
		}
	],
	"c": {
		"d": 123
	}
})










PATTERNS = [
	[	"|a",		list,			[ "|a", 	]	],
	[	"|a|*|b",	str,	"cc",	[ "|a|0|b", ]	],
	[	"|a|*|e",	str,	"ff",	[ "|a|1|e", ]	],
	[	"|c|d",		int,	123,	[ "|c|d", 	]	],

	[	"|c|x",		None,			[  ]	],
	[	"|a|x",		None,			[  ]	],
	[	"|x",		None,			[  ]	],
	[	"|c|d|e",	None,			[  ]	],
	[	"|c|*",		None,			[  ]	],
	[	"|c|*|d",	None,			[  ]	],
	[	"|a|b",		None,			[  ]	],
]


for p in PATTERNS:
	if len(p) == 3:
		spath, result = FlexDataSelector(p[0]).getOne(dataTree)
		if p[1] is None:
			Assert.isNone(result)
			Assert.isNone(spath)
		else:
			Assert.isInstance(result, p[1])
			Assert.isInstance(spath, str)
			Assert.isIn(spath, p[2])
	elif len(p) == 4:
		spath, result = FlexDataSelector(p[0]).getOne(dataTree)
		if p[1] is None:
			Assert.isNone(spath)
			Assert.isNone(result)
		else:
			Assert.isInstance(result, p[1])
			Assert.isEqual(result, p[2])
			Assert.isInstance(spath, str)
			Assert.isIn(spath, p[3])
	else:
		raise Exception()


























