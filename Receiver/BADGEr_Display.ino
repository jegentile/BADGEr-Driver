/*****

For use with the BADGEr eInk Display

For proper use:
Arduino v. 1.0.05
Arduino Pro Mini 3.3V 8MHz

*****/

#include <SPI.h>
#include <SD.h>
#include <inttypes.h>
#include <ctype.h>
#include "EPD.h"
#include "S5813A.h"
#include "EReader.h"

char line;
char highlight;
char buffer[50];
boolean hl;


void setup()
{
  Serial.begin(9600);
  ereader.setup(EPD_2_7);
}


void loop()
{
  
  if(Serial.available() > 0)
  { 
    memset(buffer, 0, sizeof(buffer));   
    line = Serial.read();
 
    
    Serial.readBytesUntil('\n', buffer, 128);
    ereader.spi_attach();
    
    highlight=buffer[0];
    hl = true;
    if(highlight=='1'){
        hl=false;
    }
    
    if (line == '1')
      ereader.put_ascii(10, 0, &buffer[1], hl);
    else if (line == '2')
      ereader.put_ascii(10, 16, &buffer[1], hl);
    else if (line == '3')
      ereader.put_ascii(10, 32, &buffer[1], hl);
    else if (line == '4')
      ereader.put_ascii(10, 48, &buffer[1], hl);
    else if (line == '5')
      ereader.put_ascii(10, 64, &buffer[1], hl);
    else if (line == '6')
      ereader.put_ascii(10, 80, &buffer[1], hl);
    else if (line == '7')
      ereader.put_ascii(10, 96, &buffer[1], hl);
    else if (line == '8')
      ereader.put_ascii(10, 112, &buffer[1], hl);
    else if (line == '9')
      ereader.put_ascii(10, 128, &buffer[1], hl);
    else if (line == 'A')
      ereader.put_ascii(10, 144, &buffer[1], hl);
    else if (line == 'B')
      ereader.put_ascii(10, 160, &buffer[1], hl);
      
    else if (line == 'C')
    {
      ereader.show();
      ereader.spi_detach();
    }
  }
}

