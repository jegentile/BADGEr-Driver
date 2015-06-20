### **Library**

This is a Python module that can drive BADGEr through a PagePrint object. 
```
import BADGEr
pp = BADGEr.PagePrint('/dev/tty.usbserial-A5047MW8')
pp.println('Hello World')
pp.println('Line 7, highlighted',7,True)
pp.fflush()
```

The constructor connects to the TTY device and lines are printed using the ```println``` function. Optional arguments to this function are the line number and a highlight flag. If the highlight flag is set, the line will be printed in negative (white text and black background). 

Each ```println``` caches a line on a page but BADGEr does not display the content until the ```fflush``` function is called. This will toggle BADGEr's pixels and display the new page. 

### **How to Use**

First, The Arduino sketch (Receiver/BADGEr_Display.ino) needs to be loaded on BADGEr. Second, locate the UART device connected to BADEGEr in ```/dev/`` and instantiate a ```PagePrint``` object.

### **Repository**


#### *Timing*

The ```println``` and ```fflush``` functions have a 0.5s and 2s delay respectively.

#### *Credits*

I'd like ot recognize a blog post by [_www.jeremyblum.com_](http://www.jeremyblum.com/2014/01/06/epaper-weather-station/)