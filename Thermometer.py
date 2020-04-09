#!/usr/bin/env python3
########################################################################
# Filename    : Thermometer.py
# Description : DIY Termometro
# Author      : antonio2709
# modification: 2020/04/09
########################################################################
import RPi.GPIO as GPIO
import smbus
import time
import math
address = 0x48
bus=smbus.SMBus(1)
cmd=0x40
def analogRead(chn):
    value = bus.read_byte_data(address,cmd+chn)
    return value    
def analogWrite(value):
    bus.write_byte_data(address,cmd,value)      
def setup():
    GPIO.setmode(GPIO.BOARD)    
def loop():
    while True:
        value = analogRead(0)       # leer ADC valor pin A0 
        voltage = value / 255.0 * 3.3       # calcular voltaje
        Rt = 10 * voltage / (3.3 - voltage) # calcular valor resistencia de termistor 
        tempK = 1/(1/(273.15 + 25) + math.log(Rt/10)/3950.0) # calcular temperatura (Kelvin)
        tempC = tempK -273.15       # calcular temperatura (Celsius)
       # print ('Valor ADC : %d, Voltaje : %.2f, Temperatura(ªC) : %.2f,Temperatura(K) : %.2f'%(value,voltage,tempC,tempK))
        print("Valor ADC : %d"%(value),"Voltaje :%.3f"%(voltage),"Temperatura : %.2f"%(tempC),"ºC","temperatura : %.1f"%(tempK),"ºK")
        time.sleep(2)
def destroy():
    GPIO.cleanup()
    
if __name__ == '__main__':  # Program entrance
    print ('EL programa esta arrancado ... ')
    print ('Presione CONTROL+C para finalizar el programa')
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()