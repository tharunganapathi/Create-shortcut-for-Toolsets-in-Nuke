
import os
user = (os.path.expanduser("~"))
print user


fullPath = user + '\.nuke\ToolSets\\'
print '\n'
print ('fullPath = '+fullPath)
print fullPath


finalPath = fullPath + 'CG_COMP.nk'
print finalPath




nuke.menu('Nodes').addCommand("CG",'nuke.loadToolset("C:\Users\CSS\.nuke\ToolSets\CG_COMP.nk")')
