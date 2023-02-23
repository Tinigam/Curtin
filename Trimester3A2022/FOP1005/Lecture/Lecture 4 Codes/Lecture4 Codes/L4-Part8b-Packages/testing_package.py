#
# testing_package.py – test program for fun package
#
import fun.textfun as tfun
import fun.numfun as nfun

testString = 'helloHELLO'
print(tfun.novowels(testString))
print(tfun.reverseupper(testString))

r = nfun.sum(1, 2)
print(r)

r = nfun.average(1, 2)
print(r)

r = nfun.average(2, 3)
print(r)
