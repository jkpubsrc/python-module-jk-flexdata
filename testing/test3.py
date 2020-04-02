#!/usr/bin/python3


import jk_flexdata



#
# This test checks for a bug. It this program terminates and does not get into an endless loop, everything is okay.
#





x = jk_flexdata.FlexObject({
	"a": [
	]
})

print("****************")

print(type(x.a))
for a in x.a:
	print(a)

print("****************")

print(type(x.b))
for a in x.b:
	print(a)

print("****************")








