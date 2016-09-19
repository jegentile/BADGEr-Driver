__author__ = 'jegentile'

import BADGEr

def main():

    pp = BADGEr.PagePrint('/dev/cu.usbserial-A1048KD0')
    
    pp.println('Hello World')
    pp.println('Line 7, highlighted',7,True)
    pp.fflush()

if __name__ == '__main__':
    main()
