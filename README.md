# tkbpmmshz
tkinter bpm / milliseconds / hertz calculator

![screenshot](https://github.com/dustractor/tkbpmmshz/blob/main/Screenshot.png)

notes:

This script uses tkinter for it's GUI.  Unfortunately, not every python distribution comes with tkinter anymore. I use the Anaconda python distribution which does.

The python script does not depend on any particular python distribution but if you use anaconda on windows, there are two extra scripts included which provide a way for windows users to launch the script without having to open a terminal and manually type the command ``python tkbpmmshz.py``.  The command file (``tkbpmmshz.cmd``) runs the python script and the visual basic script file (``tkbpmmshz.vbs``) launches the command file without creating an extra window. It's insane that in 2024, you have to resort to such a convoluted approach just to run a tkinter app without an extra window but AFAIK Microsoft 
provides no other way to do this.

Pinning the .vbs file directly to the taskbar is also not an option but the workaround is to right-click the vbs file, use the "send to..." menu to create a shortcut on the desktop, rename the shortcut -- change the extension from .lnk to .exe, then you can pin that, rename the shortcut back to the .lnk extension, then shift-click the pinned icon on the taskbar to get to the properties dialog and change the target field to point back to the re-renamed shortcut. Yikes but it works.

If you use the GitHub app to clone the repo to the default location which is a folder named GitHub inside your Documents folder, then the launchers should work out of the box but otherwise if you ``git clone`` to some other location you will have to edit the paths in the cmd & vbs scripts to point to the correct location.
