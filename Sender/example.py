__author__ = 'jgentile'

import BADGEr

def main():

    pp = BADGEr.PagePrint('/dev/tty.usbserial-A5047MW8')
    
    pp.println('Hello World')
    pp.println('Line 7, highlighted',7,True)
    pp.fflush()

if __name__ == '__main__':
    main()