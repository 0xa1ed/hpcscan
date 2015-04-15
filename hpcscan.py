import os, sys, profiles
from profiles import *

print "Modules loaded:",
for word in profiles.__all__:
    print word,

print ""

vir = flashcache.flashcache()
print vir.greet
