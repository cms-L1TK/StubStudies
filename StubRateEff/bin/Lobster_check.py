import subprocess
import sys
import os

infiles = sys.argv[3:]
val = sys.argv[1:3]
text = ''
text += '    TChain* ch    = new TChain("L1TrackNtuple/eventTree") ;\n'
for fn in infiles:
    a, b = fn.split(':')
    text += '    ch ->Add("' +  b + '");\n'
text += '    MyAnalysis t1(ch);\n'
text += '    t1.Loop("ANoutput.root",' + val[0] + ',"' + val[1] +  '");\n'
SHNAME1 = 'main.C'
SHFILE1='#include "MyAnalysis.h"\n' +\
'int main(){\n' +\
text +\
'}'


open(SHNAME1, 'wt').write(SHFILE1)
#os.system("echo '" + SHFILE1+ "' > main.C && ls -l && cat main.C && root  -b -q -l main.so main.C && ls -l")
#os.system('echo ' + SHFILE1+ ' > main.C && ls -l && cat main.C && root -l main.so main.C && ls -l')
#os.system('cat main.C')
os.system('root -b -q -l main.so main.C')
