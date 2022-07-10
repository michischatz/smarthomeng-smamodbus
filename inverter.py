import logging

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusTcpClient as ModBusClient

class Inverter:

    def __init__(self,sh,ip,port,unitid,timeout,logger):
        self.logger = logger
        self.unitid = unitid
        # https://stackoverflow.com/questions/23887184/pymodbus-tcpclient-timeout
        Endian.Timeout = timeout
        try:
            self._client = ModBusClient(ip, port)
        except:
            self.logger.error("Cannot establish a connection with IP '{}' and port '{}' to the inverter.".format(ip,port))
        else:
            self.logger.info("Retreived data from inverter with IP '{}' and port '{}'.".format(ip,port))
        
        return

    def __del__(self):
        del self._client
        del self._device_unit
    
    def readreg(self,addr,count,datatyp):
        '''
        Read a register
        '''
        self._regaddr = int(addr)
        self._regcount = int(count)
        self._regdatatyp = datatyp
        self._device_unit =  int(self.unitid)
        self.logger.debug("Read register with register '{}' datatype '{}' and unit id '{}'".format(self._regaddr,self._regdatatyp,self._device_unit))
        
        # Switch case instead of elseif, but dont have enough python skills to code that
        #datatypes = {
        #    'S16': self.__read_S16(),
        #    'S32': self.__read_S32(),
        #    'STR32': self.__read_STR32(),
        #    'U16': self.__read_U16(),
        #    'U32': self.__read_U32(),
        #    'U32u24bit': self.__read_U32u24bit(),
        #    'U64': self.__read_U64()
        #}    
        #self._resultdata = datatypes.get(self._regdatatyp, False)
        
        if self._regdatatyp == 'S16':
            self._resultdata = self.__read_S16()
        elif self._regdatatyp == 'S32':
            self._resultdata = self.__read_S32()
        elif self._regdatatyp == 'U16':
            self._resultdata = self.__read_U16()
        elif self._regdatatyp == 'U32':
            self._resultdata = self.__read_U32()
        elif self._regdatatyp == 'U64':
            self._resultdata = self.__read_U64()
        else:
            self.logger.error("Unknown datatype '{}'".format(self._regdatatyp))
        
        return self._resultdata
    
    def __read_S16(self):
        #S16 A signed word (16-bit) / Vorzeichenbehaftetes Wort (16 Bit) 0x8000
        self.logger.debug("Call datatype '{}' (function S16) with Params register address '{}' count '{}' unit id '{}'".format(self._regdatatyp,self._regaddr,self._regcount,self._device_unit))
        self._read = self._client.read_holding_registers(self._regaddr, self._regcount, unit=self._device_unit)
        self._decoder = BinaryPayloadDecoder.fromRegisters(self._read.registers, byteorder=Endian.Big, wordorder=Endian.Big)
        self._data = self._decoder.decode_16bit_int()
        self.logger.debug("Decoded data: '{}'".format(self._data))
        return self._data
    
    def __read_S32(self):
        #S32 A signed double word (32-bit) / Vorzeichenbehaftetes Doppelwort (32 Bit) 0x8000 0000
        self.logger.debug("Call datatype '{}' (function S32) with Params register address '{}' count '{}' unit id '{}'".format(self._regdatatyp,self._regaddr,self._regcount,self._device_unit))
        self._read = self._client.read_holding_registers(self._regaddr, self._regcount, unit=self._device_unit)
        self._decoder = BinaryPayloadDecoder.fromRegisters(self._read.registers, byteorder=Endian.Big, wordorder=Endian.Big)
        self._data = self._decoder.decode_32bit_int()
        self.logger.debug("Decoded data: '{}'".format(self._data))
        return self._data
    
    def __read_STR32(self):
        #STR32 32 byte data field, in UTF8 format / 32-Byte-Datenfeld, im Format UTF8 NULL
        return
    
    def __read_U16(self):
        #U16 A word (16-bit) / Ein Wort (16 Bit) 0xFFFF
        self.logger.debug("Call datatype '{}' (function U16) with Params register address '{}' count '{}' unit id '{}'".format(self._regdatatyp,self._regaddr,self._regcount,self._device_unit))
        self._read = self._client.read_holding_registers(self._regaddr, self._regcount, unit=self._device_unit)
        self._decoder = BinaryPayloadDecoder.fromRegisters(self._read.registers, byteorder=Endian.Big, wordorder=Endian.Big)
        self._data = self._decoder.decode_16bit_uint()
        self.logger.debug("Decoded data: '{}'".format(self._data))
        return self._data
    
    def __read_U32(self):
        #U32 A double word (32-bit) / Ein Doppelwort (32 Bit) 0xFFFF FFFF
        #not tested: U32 For status values, only the lower 24 bits of a double word (32-bit) are used. / Für Statuswerte werden nur die unteren 24 Bit eines Doppelworts (32 Bit) verwendet 0xFFFF FD
        self.logger.debug("Call datatype '{}' (function U32) with Params register address '{}' count '{}' unit id '{}'".format(self._regdatatyp,self._regaddr,self._regcount,self._device_unit))
        self._read = self._client.read_holding_registers(self._regaddr, self._regcount, unit=self._device_unit)
        self._decoder = BinaryPayloadDecoder.fromRegisters(self._read.registers, byteorder=Endian.Big, wordorder=Endian.Big)
        self._data = self._decoder.decode_32bit_uint()
        self.logger.debug("Decoded data: '{}'".format(self._data))
        return self._data
    
    def __read_U64(self):
        #U64 A quadruple word (64-bit) / Ein Vierfachwort (64 Bit) 0xFF
        self.logger.debug("Call datatype '{}' (function U64) with Params register address '{}' count '{}' unit id '{}'".format(self._regdatatyp,self._regaddr,self._regcount,self._device_unit))
        self._read = self._client.read_holding_registers(self._regaddr, self._regcount, unit=self._device_unit)
        self._decoder = BinaryPayloadDecoder.fromRegisters(self._read.registers, byteorder=Endian.Big, wordorder=Endian.Big)
        self._data = self._decoder.decode_64bit_uint()
        self.logger.debug("Decoded data: '{}'".format(self._data))
        return self._data
    