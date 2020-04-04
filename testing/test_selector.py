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
	[	"|a",		list			],
	[	"|a|*|b",	str,	"cc"	],
	[	"|a|*|e",	str,	"ff"	],
	[	"|c|d",		int,	123		],

	[	"|c|x",		None,			],
	[	"|a|x",		None,			],
	[	"|x",		None,			],
	[	"|c|d|e",	None,			],
	[	"|c|*",		None,			],
	[	"|c|*|d",	None,			],
	[	"|a|b",		None,			],
]


for p in PATTERNS:
	if len(p) == 2:
		spath, result = FlexDataSelector(p[0]).getOne(dataTree)
		if p[1] is None:
			Assert.isNone(result)
		else:
			Assert.isInstance(result, p[1])
	elif len(p) == 3:
		spath, result = FlexDataSelector(p[0]).getOne(dataTree)
		if p[1] is None:
			Assert.isNone(result)
		else:
			Assert.isInstance(result, p[1])
			Assert.isEqual(result, p[2])
	else:
		raise Exception()


























