#!/usr/bin/python3


import jk_flexdata



x = jk_flexdata.FlexObject({
	"a": [
		{
			"b": "c"
		}
	]
})

print("****************")

print(">>0")
print(x)
print(">>1")
print(x.a[0])
print(">>2")
print(x.a[0].b)
print(">>3")
print(x.b)
print(">>4")

print("****************")

print(">>4")
x.a[0] = 5
print(">>5")
print(x.a[0])
print(">>6")
print(x)
print(">>7")
x.b = 3
print(">>8")
print(x)
print(">>9")
print(x._toDict())
print(">>10")

print("****************")








