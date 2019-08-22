#!/usr/bin/python3


import jk_flexdata


x = jk_flexdata.FlexObject({
	"a": [
		{
			"b": "c"
		}
	]
})

print(x.a[0])
print(x.a[0].b)






