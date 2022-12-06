# mergeModeShortcut
Command to change the mode of the selected merges node in Nuke more easy.

Autor: Jorge Hernandez

Web: https://www.linkedin.com/in/jorgehi-vfx/

# Installation
The way you can use this command is storing the mergeOperations.py in a directory that is been reading by nuke and adding these lines in your menu.py

import mergeOperations
mergeOperations.installCommands()

You can change the shotcut editing the installCommands function if your prefer other than ctrl + Arrows Up and Down. For example you can use alt+Up and alt+Down too.

If you don´t know how to do this, here i let you a basic instalation steps:

1. Go to this path C:\Users\[username]\.nuke where username is your windows username.
2. If you don´t have a menu.py file here, create it with a basic text editor.
3. In your menu.py file add these lines: 

  import nuke
  
  import mergeOperations
  
  mergeOperations.installCommands()
  
4. Add the mergeOperations.py file in this path C:\Users[username].nuke\mergeOperations.py
5. Open Nuke, now you can use ctrl+Up and ctrl+Down to change the mode of your selected merge nodes.
