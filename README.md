# SmartHomeng SMA Modbus plugin
This plugin for SmartHomeNG reads data from an [SMA](https://www.sma.de) inverter via modbus interface and write the values to an item.
It is a multi instance plugin and can be used for one or more inverters.

For example, it could be used for an photovoltaic invertert and also for an battery inverter.

German description / Deutsche Beschreibung auf [mschatz.net](https://www.mschatz.net/smarthome/shng/smamodbus)

## Installation
Download the latest release and place it in your plugin folder of the SmartHomeNG installation. Restart SmartHomeNG service.
Follow up the next step.

**Important:**
The modbus interface needs to be activated at the inverter. For activation, privileged access is requiered.

## Requirements
- [PyModbus](https://pymodbus.readthedocs.io/en/latest/readme.html) >= 2.3.0
- modbus interface must be enabled on the inverter (privileged access is requiered)
- modbus unit id on the inverter must be set

## Configuration
The following parameters are requiered to get plugin running:
* IP or hostname
* Port of the modbus interface, default 502
* Unit id, default 3
* timeout, default 10
* cycle, default 60
* instance name, e.g. battery 

After the configuration is done, the plugin must be activated, than it should work an receive data from your inverter.

## Usage

Items need a new attribute to receive the data.
If you use this plugin for more than one inverter, you need to work with the @.

Please refere to your inverter specification SMA modbuslist.

```smamodbus@<inverter-instance-name>: <Register adresse SMA>-<Number of contguous SMA register>-<Data type SMA>```
DE: 

```smamodbus@<inverter-instance-name>: <Registeradresse SMA>-<Anzahl zusammenhängender SMA register>-<Datentyp SMA>```

### Example 1

You can read the serial number from the inverter.
The instance name of the plugin in this example is "pv" and the used specification is for a SUNNY TRIPOWER 8.0 "MODBUS-HTML_STP8.0-10.0-3AV-40_GG10_V10" (Firmware version 1.1.18.R), see the folder "specs" for further information.

```yaml
PV:
    Typelable:
        serialnumber:
            name: serial number
            type: num
            smamodbus@pv: 30005-2-U32
```

### Example 2

This example will receive the battery charge level of the SUNNY ISLAND 4.4M-13 inverter, see the specs MODBUS-HTML_SI44M-80H-13_32009R_V10.
The instance name here is battery.

```yaml
ChargeLevel:
    name: Current battery charge level
    type: num
    smamodbus@battery: 30845-2-U32
```

