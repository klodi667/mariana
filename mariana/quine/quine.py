import os
import sys
import shutil
cwd = os.getcwd()
if(os.path.isdir(cwd + '/quine')):
    shutil.rmtree(cwd + '/quine')
os.makedirs(cwd + '/quine')
f = open('quine/quine.py', 'w')
quine = [
  "import os",
  "import sys",
  "import shutil",
  "cwd = os.getcwd()",
  "if(os.path.isdir(cwd + '/quine')):",
  "    shutil.rmtree(cwd + '/quine')",
  "os.makedirs(cwd + '/quine')",
  "f = open('quine/quine.py', 'w')",
  "quine = [",
  "  ",
  "]",
  "for i in range(0,9):",
  "    print(quine[i], file=f)",
  "for i in range(0,len(quine)):",
  "    print(quine[9] + chr(34) + quine[i] + chr(34) + ',', file=f)",
  "for i in range(10, len(quine)):",
  "    print(quine[i], file=f)",
  "f.close()",
  "os.chdir(cwd +'/quine')",
  "os.system('quine.py')"
]
for i in range(0,9):
    print(quine[i], file=f)
for i in range(0,len(quine)):
    print(quine[9] + chr(34) + quine[i] + chr(34) + ',', file=f)
for i in range(10, len(quine)):
    print(quine[i], file=f)
f.close()
os.chdir(cwd +'/quine')
os.system('quine.py')
