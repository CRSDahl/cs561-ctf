import sys
from random import *
offset=38

if len(sys.argv) < 2:
    print("No number given. Give a number as parameter.")
    sys.exit(1)

num = int(sys.argv[1])
if num > offset:
    print("Number too high.")
    sys.exit(1)

if num < offset:
    print("Number too low.")
    sys.exit(1)

print("CTF_SDaT{XXoq9JWY$Y}")