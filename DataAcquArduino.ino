// EmonLibrary examples openenergymonitor.org, Licence GNU GPL V3

#include "EmonLib.h"             // Include Emon Library
EnergyMonitor emon1;             // Create an instance
char dataString[50] = {0};
void setup()
{  
  Serial.begin(9600);
  
  emon1.voltage(A0, 234.26, 1.7);  // Voltage: input pin, calibration, phase_shift
  emon1.current(A5, 100.1);       // Current: input pin, calibration.
}

void loop()
{
  emon1.calcVI(20,2000);         // Calculate all. No.of half wavelengths (crossings), time-out
  emon1.serialprint();           // Print out all variables (realpower, apparent power, Vrms, Irms, power factor)
  
  float realPower       = emon1.realPower;        //extract Real Power into variable
  float apparentPower   = emon1.apparentPower;    //extract Apparent Power into variable
  float powerFActor     = emon1.powerFactor;      //extract Power Factor into Variable
  float supplyVoltage   = emon1.Vrms;             //extract Vrms into Variable
  float Irms            = emon1.Irms;             //extract Irms into Variable
//sprintf(dataString,"%f , %f , %f , %f , %f",realPower,apparentPower,powerFActor,supplyVoltage,Irms);

//Serial.println(dataString);
Serial.print(realPower);
Serial.print(" , ");
Serial.print(apparentPower);
Serial.print(" , ");
Serial.print(powerFActor);
Serial.print(" , ");
Serial.print(supplyVoltage);
Serial.print(" , ");
Serial.println(Irms);


delay(200);
}
