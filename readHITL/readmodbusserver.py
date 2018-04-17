#!/usr/bin/env python
"""
Pymodbus Server With Updating Thread
--------------------------------------------------------------------------
This is an example of having a background thread updating the
context while the server is operating. This can also be done with
a python thread::
    from threading import Thread
    thread = Thread(target=updating_writer, args=(context,))
    thread.start()
"""
# --------------------------------------------------------------------------- #
# import the modbus libraries we need
# --------------------------------------------------------------------------- #
from pymodbus.server.async import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer

# --------------------------------------------------------------------------- #
# import the twisted libraries we need
# --------------------------------------------------------------------------- #
from twisted.internet.task import LoopingCall

# --------------------------------------------------------------------------- #
# import struct libraries we need to unpuck two integers to a floating type
# --------------------------------------------------------------------------- #
from struct import *

# --------------------------------------------------------------------------- #
# import path libraries we need to write the floating type numbers to SE code
# --------------------------------------------------------------------------- #
import os.path

# --------------------------------------------------------------------------- #
# import datetime libraries we need to add a timestamp on the historian file
# --------------------------------------------------------------------------- #
import datetime

# --------------------------------------------------------------------------- #
# configure the service logging
# --------------------------------------------------------------------------- #
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.ERROR)

# --------------------------------------------------------------------------- #
# define your callback process
# --------------------------------------------------------------------------- #


def updating_writer(a):
    """ A worker process that runs every so often and
    updates live values of the context. It should be noted
    that there is a race condition for the update.
    :param arguments: The input arguments to the call
    """
    log.debug("updating the context")
    context = a[0]
    register = 3
    slave_id = 0x02
    address = 0x00
    values = context[slave_id].getValues(register, address, count=84)
    #log.debug("values: " + str(values))
    #print("{}".format(str(values)))
    #context[slave_id].setValues(register, address, values)
    
    # Two integers (modbus registers) to a floating point conversion
    i1 = values[0]
    i2 = values[1]
    i3 = values[2]
    i4 = values[3]
    i5 = values[4]
    i6 = values[5]
    i7 = values[6]
    i8 = values[7]
    i9 = values[8]
    i10 = values[9]
    i11 = values[10]
    i12 = values[11]
    i13 = values[12]
    i14 = values[13]
    i15 = values[14]
    i16 = values[15]
    i17 = values[16]
    i18 = values[17]
    i19 = values[18]
    i20 = values[19]
    i21 = values[20]
    i22 = values[21]
    i23 = values[22]
    i24 = values[23]
    i25 = values[24]
    i26 = values[25]
    i27 = values[26]
    i28 = values[27]
    i29 = values[28]
    i30 = values[29]
    i31 = values[30]
    i32 = values[31]
    i33 = values[32]
    i34 = values[33]
    i35 = values[34]
    i36 = values[35]
    i37 = values[36]
    i38 = values[37]
    i39 = values[38]
    i40 = values[39]
    i41 = values[40]
    i42 = values[41]
    i43 = values[42]
    i44 = values[43]
    i45 = values[44]
    i46 = values[45]
    i47 = values[46]
    i48 = values[47]
    i49 = values[48]
    i50 = values[49]
    i51 = values[50]
    i52 = values[51]
    i53 = values[52]
    i54 = values[53]
    i55 = values[54]
    i56 = values[55]
    i57 = values[56]
    i58 = values[57]
    i59 = values[58]
    i60 = values[59]
    i61 = values[60]
    i62 = values[61]
    i63 = values[62]
    i64 = values[63]
    i65 = values[64]
    i66 = values[65]
    i67 = values[66]
    i68 = values[67]
    i69 = values[68]
    i70 = values[69]
    i71 = values[70]
    i72 = values[71]
    i73 = values[72]
    i74 = values[73]
    i75 = values[74]
    i76 = values[75]
    i77 = values[76]
    i78 = values[77]
    i79 = values[78]
    i80 = values[79]
    i81 = values[80]
    i82 = values[81]
    i83 = values[82]
    i84 = values[83]
    

    f1 = unpack('f',pack('<HH',i2,i1))[0]    
    f2 = unpack('f',pack('<HH',i4,i3))[0]
    f3 = unpack('f',pack('<HH',i6,i5))[0]
    f4 = unpack('f',pack('<HH',i8,i7))[0]
    f5 = unpack('f',pack('<HH',i10,i9))[0]
    f6 = unpack('f',pack('<HH',i12,i11))[0]
    f7 = unpack('f',pack('<HH',i14,i13))[0]
    f8 = unpack('f',pack('<HH',i16,i15))[0]
    f9 = unpack('f',pack('<HH',i18,i17))[0]
    f10 = unpack('f',pack('<HH',i20,i19))[0]
    f11 = unpack('f',pack('<HH',i22,i21))[0]    
    f12 = unpack('f',pack('<HH',i24,i23))[0]
    f13 = unpack('f',pack('<HH',i26,i25))[0]
    f14 = unpack('f',pack('<HH',i28,i27))[0]
    f15 = unpack('f',pack('<HH',i30,i29))[0]
    f16 = unpack('f',pack('<HH',i32,i31))[0]
    f17 = unpack('f',pack('<HH',i34,i33))[0]
    f18 = unpack('f',pack('<HH',i36,i35))[0]
    f19 = unpack('f',pack('<HH',i38,i37))[0]
    f20 = unpack('f',pack('<HH',i40,i39))[0]
    f21 = unpack('f',pack('<HH',i42,i41))[0]    
    f22 = unpack('f',pack('<HH',i44,i43))[0]
    f23 = unpack('f',pack('<HH',i46,i45))[0]
    f24 = unpack('f',pack('<HH',i48,i47))[0]
    f25 = unpack('f',pack('<HH',i50,i49))[0]
    f26 = unpack('f',pack('<HH',i52,i51))[0]
    f27 = unpack('f',pack('<HH',i54,i53))[0]
    f28 = unpack('f',pack('<HH',i56,i55))[0]
    f29 = unpack('f',pack('<HH',i58,i57))[0]
    f30 = unpack('f',pack('<HH',i60,i59))[0]
    f31 = unpack('f',pack('<HH',i62,i61))[0]    
    f32 = unpack('f',pack('<HH',i64,i63))[0]
    f33 = unpack('f',pack('<HH',i66,i65))[0]
    f34 = unpack('f',pack('<HH',i68,i67))[0]
    f35 = unpack('f',pack('<HH',i70,i69))[0]
    f36 = unpack('f',pack('<HH',i72,i71))[0]
    f37 = unpack('f',pack('<HH',i74,i73))[0]
    f38 = unpack('f',pack('<HH',i76,i75))[0]
    f39 = unpack('f',pack('<HH',i78,i77))[0]
    f40 = unpack('f',pack('<HH',i80,i79))[0]
    f41 = unpack('f',pack('<HH',i82,i81))[0]    
    f42 = unpack('f',pack('<HH',i84,i83))[0]

    #print (f1,f2)
    x = ' ';
    # Write registers to file for the SE code
    f = open('../files/input9.txt','w')
    # f.write('{}, {}, {}, {}, {}, {}, {}, {} , {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {} , {}, {}, {}, {}, {}, {}, {}, {}, {}, {} , {}, {}, {}, {}\n'.format(f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36, f37, f38, f39, f40, f41, f42)) 
    f.write('1{}1{}{}{}1{}0{}9e-4\n'.format(5*x,5*x,f1,5*x,5*x,5*x))
    f.write('2{}2{}{}{}1{}0{}1e-4\n'.format(5*x,5*x,f3,5*x,5*x,5*x))
    f.write('3{}3{}{}{}1{}0{}1e-4\n'.format(5*x,5*x,f4,5*x,5*x,5*x))
    f.write('4{}1{}{}{}2{}0{}9e-4\n'.format(5*x,5*x,f5,5*x,5*x,5*x))
    f.write('5{}2{}{}{}2{}0{}1e-4\n'.format(5*x,5*x,f7,5*x,5*x,5*x))
    f.write('6{}3{}{}{}2{}0{}1e-4\n'.format(5*x,5*x,f8,5*x,5*x,5*x))
    f.write('7{}1{}{}{}3{}0{}9e-4\n'.format(5*x,5*x,f9,5*x,5*x,5*x))
    f.write('8{}2{}{}{}3{}0{}1e-4\n'.format(5*x,5*x,f11,5*x,5*x,5*x))
    f.write('9{}3{}{}{}3{}0{}1e-4\n'.format(5*x,5*x,f12,5*x,5*x,5*x))
    f.write('10{}1{}{}{}4{}0{}9e-4\n'.format(5*x,5*x,f13,5*x,5*x,5*x))
    f.write('11{}4{}{}{}4{}5{}64e-6\n'.format(5*x,5*x,f15,5*x,5*x,5*x))
    f.write('12{}5{}{}{}4{}5{}64e-6\n'.format(5*x,5*x,f16,5*x,5*x,5*x))
    f.write('13{}4{}{}{}4{}6{}64e-6\n'.format(5*x,5*x,f17,5*x,5*x,5*x))
    f.write('14{}5{}{}{}4{}6{}64e-6\n'.format(5*x,5*x,f18,5*x,5*x,5*x))
    f.write('15{}1{}{}{}5{}0{}9e-4\n'.format(5*x,5*x,f19,5*x,5*x,5*x))
    f.write('16{}2{}{}{}5{}0{}1e-4\n'.format(5*x,5*x,f21,5*x,5*x,5*x))
    f.write('17{}3{}{}{}5{}0{}1e-4\n'.format(5*x,5*x,f22,5*x,5*x,5*x))
    f.write('18{}1{}{}{}6{}0{}9e-4\n'.format(5*x,5*x,f23,5*x,5*x,5*x))
    f.write('19{}2{}{}{}6{}0{}1e-4\n'.format(5*x,5*x,f25,5*x,5*x,5*x))
    f.write('20{}3{}{}{}6{}0{}1e-4\n'.format(5*x,5*x,f26,5*x,5*x,5*x))
    f.write('21{}1{}{}{}7{}0{}9e-4\n'.format(5*x,5*x,f27,5*x,5*x,5*x))
    f.write('22{}4{}{}{}7{}8{}64e-6\n'.format(5*x,5*x,f29,5*x,5*x,5*x))
    f.write('23{}5{}{}{}7{}8{}64e-6\n'.format(5*x,5*x,f30,5*x,5*x,5*x))
    f.write('24{}4{}{}{}7{}5{}64e-6\n'.format(5*x,5*x,f31,5*x,5*x,5*x))
    f.write('25{}5{}{}{}7{}5{}64e-6\n'.format(5*x,5*x,f32,5*x,5*x,5*x))
    f.write('26{}1{}{}{}8{}0{}9e-4\n'.format(5*x,5*x,f33,5*x,5*x,5*x))
    f.write('27{}2{}{}{}8{}0{}1e-4\n'.format(5*x,5*x,f35,5*x,5*x,5*x))
    f.write('28{}3{}{}{}8{}0{}1e-4\n'.format(5*x,5*x,f36,5*x,5*x,5*x))
    f.write('29{}1{}{}{}9{}0{}9e-4\n'.format(5*x,5*x,f37,5*x,5*x,5*x))
    f.write('30{}4{}{}{}9{}8{}64e-6\n'.format(5*x,5*x,f39,5*x,5*x,5*x))
    f.write('31{}5{}{}{}9{}8{}64e-6\n'.format(5*x,5*x,f40,5*x,5*x,5*x))
    f.write('32{}4{}{}{}9{}6{}64e-6\n'.format(5*x,5*x,f41,5*x,5*x,5*x))
    f.write('33{}5{}{}{}9{}6{}64e-6\n'.format(5*x,5*x,f42,5*x,5*x,5*x))
    f.close()

    # Write registers to historian file with timestamp
    f = open('../files/historian','a+')
    time = datetime.datetime.now()
    f.write('{}, {}, {}, {}, {}, {}, {}, {}, {} , {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {} , {}, {}, {}, {}, {}, {}, {}, {}, {}, {} , {}, {}, {}, {}\n'.format(time, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36, f37, f38, f39, f40, f41, f42)) 
    f.close()

    # Write registers to modbus/SCADA from a file of SE code
    f = open('../files/output','r')
    if f.mode == 'r':
        valuesString =f.read()
        valuesSE = valuesString.split(',')
        list (valuesSE)        
        #  Floating point numbers to 2 integers conversion and transmit on Modbus registers
        f1SE = float(valuesSE[0])
        print (f1SE)
        #  Note: Swap registers for Edian purposes 
        i2SE, i1SE = unpack('<HH',pack('f',f1SE))
        valuesSEt = list((i1SE,i2SE))
        context[slave_id].setValues(register, 100, valuesSEt)
    
def run_updating_server():
    # ----------------------------------------------------------------------- # 
    # initialize your data store
    # ----------------------------------------------------------------------- # 
    
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [17]*100),
        co=ModbusSequentialDataBlock(0, [17]*100),
        hr=ModbusSequentialDataBlock(0, [17]*100),
        ir=ModbusSequentialDataBlock(0, [17]*100))
    context = ModbusServerContext(slaves=store, single=True)
    
    # ----------------------------------------------------------------------- # 
    # initialize the server information
    # ----------------------------------------------------------------------- # 
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'pymodbus'
    identity.ProductCode = 'PM'
    identity.VendorUrl = 'http://github.com/bashwork/pymodbus/'
    identity.ProductName = 'pymodbus Server'
    identity.ModelName = 'pymodbus Server'
    identity.MajorMinorRevision = '1.0'
    
    # ----------------------------------------------------------------------- # 
    # run the server you want
    # ----------------------------------------------------------------------- # 
    time = 1  # 1 seconds delay
    loop = LoopingCall(f=updating_writer, a=(context,))
    loop.start(time, now=False) # initially delay by time
    StartTcpServer(context, identity=identity, address=("192.168.1.3", 502))


if __name__ == "__main__":
    run_updating_server()
