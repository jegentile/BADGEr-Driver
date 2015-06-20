__author__ = 'jegentile'

import serial
import time
import sys
from subprocess import call

class PagePrint:

    def __init__(self,device):
        try:
            call(["stty", "-F", device, "-hupcl"])
            self.__serial_connection = serial.Serial(device,9600)

        except ValueError:
            print "Error opening BADGEr device",device
            print "Please verify that the /dev/ is correct."

        time.sleep(1.0)
        self.__serial_connection.write('1 \n')

        self.__last_page = []
        self.__this_page = []

        for i in range(0,12):
            self.__last_page.append('')
            self.__this_page.append('')

    def println(self,string,line_number=1,highlight=False):
        if line_number:
            if line_number == 10:
                line_number='A'
            if line_number == 11:
                line_number='B'
        h = '0'
        if highlight:
            h = '1'

        self.__this_page[line_number] = string

        print 'Sending::', str(line_number)+h+string+'\n::'
        self.__serial_connection.write(str(line_number)+h+string+'\n')
        sys.stdout.flush()
        time.sleep(0.5)

    def fflush(self):
        """
        This function sends the command for BADGEr to commit the page and refresh
        :return:
        """
        diff = 0
        for i in range(0,12):
            if not self.__last_page[i] == self.__this_page[i]:
                diff +=1

        if diff == 0:
            return

        self.__serial_connection.write('C\n')
        sys.stdout.flush()
        time.sleep(1.5)
        self.__serial_connection.write('1 \n')
        time.sleep(0.5)


        for i in range(0,12):
            self.__last_page[i] = self.__this_page[i]
            self.__this_page[i] = ''


