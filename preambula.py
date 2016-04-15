##! /usr/bin/python
import os, string
cmd = 'hg id -n -i'
fpipe = os.popen(cmd)
piperesult = fpipe.read()
fpipe.close()
results = piperesult.split()
out = 'HG Mercurial revision hash of this document is '+results[0]+', revision number is '+results[1]
FileName='instruction.tex'
fout=open(FileName,'w')
fout.write(out)
fout.close()

