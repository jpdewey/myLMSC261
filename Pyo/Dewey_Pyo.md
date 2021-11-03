# Pyo Homework Assignment

## Initial Pyo Installation Troubleshooting

While writing the code, in the final step of installing the pyo module, the error message:

```
"include/ad_portaudio.h:25:10: fatal error: 'portaudio.h' file not found
#include "portaudio.h"
         ^~~~~~~~~~~~~
1 error generated.
error: command '/usr/bin/gcc' failed with exit code 1"
```

A collective solution was being worked on (from the mouth of Rachel), so I waited patiently

I then installed the four libraries from the https://github.com/belangeo/pyo/issues/77 link
I utilized the four libraries from user "ziggear" and then finished it with the last piece of code from Rachel's directions and it was successful!

## Homework:

Utilizing the code found in "dulcimerplayer.py," I copied and pasted this code into IDLE to test it, which resulted in a syntax error:
```
from pyo import *
s = Server().boot()
s.start()
snd = SndTable("/Users/rrome/Documents/GitHub/lmsc261sp21/110Debugging/dulcimer.aiff")
env = HannTable()
pos = Phasor(freq=snd.getRate()*.25, mul=snd.getSize())
dur = Noise(mul=.001, add=.1)
g = Granulator(snd, env, [1, 1.001], pos, dur, 32, mul=.1).out()
SyntaxError: multiple statements found while compiling a single statement
```
To solve this simple syntax error, I think that the * is the result of the markdown file, since the use of * in python does not apply to this action in code

The result:
```
from pyo import
s = Server().boot()
s.start()
snd = SndTable("/Users/rrome/Documents/GitHub/lmsc261sp21/110Debugging/dulcimer.aiff")
env = HannTable()
pos = Phasor(freq=snd.getRate()*.25, mul=snd.getSize())
dur = Noise(mul=.001, add=.1)
g = Granulator(snd, env, [1, 1.001], pos, dur, 32, mul=.1).out()
SyntaxError: invalid syntax
```
This resulted in a new syntax error, which occurs in the same spot
My next theory is that a : is required to introduce the rest of the code

The result:
```
from pyo import:
s = Server().boot()
s.start()
snd = SndTable("/Users/rrome/Documents/GitHub/lmsc261sp21/110Debugging/dulcimer.aiff")
env = HannTable()
pos = Phasor(freq=snd.getRate()*.25, mul=snd.getSize())
dur = Noise(mul=.001, add=.1)
g = Granulator(snd, env, [1, 1.001], pos, dur, 32, mul=.1).out()
SyntaxError: invalid syntax
```
Invalid syntax on the colon (grrr)

Next I will try reopening IDLE, since maybe IDE's run like DAW's where they need to be restarted after new VST installations? I will include the * since who am I to question Rachel?

This failed again, with the exact same error as before

After a brief conversation with Rachel, I found my pyo in the josephdewey user (which is where it should be?)

Then Rachel came to assist and ran the melodies file directly from the .py file, not from the copied code in github.
- This was successful!!

I then attempted to run the dulcimerplayer file, but to no avail, with the following error message:
```
= RESTART: /Users/josephdewey/Documents/GitHub/lmsc261fa21/110Debugging/Assignment-Pyo/dulcimerplayer.py

WxPython is not found for the current python version.
Pyo will use a minimal GUI toolkit written with Tkinter (if available).
This toolkit has limited functionnalities and is no more
maintained or updated. If you want to use all of pyo's
GUI features, you should install WxPython, available here:
http://www.wxpython.org/

Pyo warning: Portaudio input device `MacBook Pro Microphone` has fewer channels (1) than requested (2).
Traceback (most recent call last):
  File "/Users/josephdewey/Documents/GitHub/lmsc261fa21/110Debugging/Assignment-Pyo/dulcimerplayer.py", line 4, in <module>
    snd = SndTable("/Users/rrome/Documents/GitHub/lmsc261sp21/110Debugging/dulcimer.aiff")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pyo-1.0.4-py3.9-macosx-10.9-x86_64.egg/pyo/lib/tables.py", line 1650, in __init__
    _size, _dur, _snd_sr, _snd_chnls, _format, _type = sndinfo(p)
TypeError: cannot unpack non-iterable NoneType object

```
I thought that the issue may have stemmed from the place where python was calling the .aiff file from, so I adjusted the fourth line to include "/Assignment-pyo" but I forgot to re-route it to "jdewey." This was the result:
```
= RESTART: /Users/josephdewey/Documents/GitHub/lmsc261fa21/110Debugging/Assignment-Pyo/dulcimerplayer.py

WxPython is not found for the current python version.
Pyo will use a minimal GUI toolkit written with Tkinter (if available).
This toolkit has limited functionnalities and is no more
maintained or updated. If you want to use all of pyo's
GUI features, you should install WxPython, available here:
http://www.wxpython.org/

Pyo warning: Portaudio input device `MacBook Pro Microphone` has fewer channels (1) than requested (2).
Traceback (most recent call last):
  File "/Users/josephdewey/Documents/GitHub/lmsc261fa21/110Debugging/Assignment-Pyo/dulcimerplayer.py", line 4, in <module>
    snd = SndTable("/Users/rrome/Documents/GitHub/lmsc261sp21/110Debugging/Assignment-Pyo/dulcimer.aiff")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pyo-1.0.4-py3.9-macosx-10.9-x86_64.egg/pyo/lib/tables.py", line 1650, in __init__
    _size, _dur, _snd_sr, _snd_chnls, _format, _type = sndinfo(p)
TypeError: cannot unpack non-iterable NoneType object
>>>
```
I then tried readjusting all the bounds to include the correct file location.
The result was the same:
```
= RESTART: /Users/josephdewey/Documents/GitHub/lmsc261fa21/110Debugging/Assignment-Pyo/dulcimerplayer.py

WxPython is not found for the current python version.
Pyo will use a minimal GUI toolkit written with Tkinter (if available).
This toolkit has limited functionnalities and is no more
maintained or updated. If you want to use all of pyo's
GUI features, you should install WxPython, available here:
http://www.wxpython.org/

Pyo warning: Portaudio input device `MacBook Pro Microphone` has fewer channels (1) than requested (2).
Traceback (most recent call last):
  File "/Users/josephdewey/Documents/GitHub/lmsc261fa21/110Debugging/Assignment-Pyo/dulcimerplayer.py", line 4, in <module>
    snd = SndTable("/Users/jdewey/Documents/GitHub/lmsc261fa21/110Debugging/Assignment-Pyo/dulcimer.aiff")
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pyo-1.0.4-py3.9-macosx-10.9-x86_64.egg/pyo/lib/tables.py", line 1650, in __init__
    _size, _dur, _snd_sr, _snd_chnls, _format, _type = sndinfo(p)
TypeError: cannot unpack non-iterable NoneType object
```
