import sys
import os
import subprocess
if(sys.argv[1]=='-c'):
	if(sys.argv[2]):
		os.system(sys.argv[2])
elif(sys.argv[1]==-h):
	print("Press -c or cmd")
else:
	print("wrong input")

