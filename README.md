# SmartHomeng SMA Modbus plugin
This plugin for SmartHomeNG reads data from the SMA modbus interface.
It is a multi instance plugin and can be used for on or more inverters.

## Installation
Download the latest release and place it in your plugin folder of the SmartHomeNG installation. Restart SmartHomeNG service.
Follow up the next step.

## Requierments
- pymodbus >= 2.3.0
- modbus interface must be enabled on the inverter (privileged access is requiered)
- modbus unit id on the inverter must be set

## Configuration
The following parameters are requiered to get plugin running:
* IP or hostname
* Port of the modbus interface, default 502
* Unit id, default 3
* cycle, default 60
* instance name, e.g. battery 

After the configuration is done, the plugin must be activated, than it should work an receive data from your inverter.

## Usage

Items need a new attribute to receive the data.
If you use this plugin for more than one inverter, you need to work with the @.

```smamodbus@<inverter-instance-name>: <Register adresse SMA>-<Number of contguous SMA register>-<Data type SMA>```
  

```yaml
PV:
    Typenschild:
        Seriennummer:
            name: Seriennummer
            type: num
            smamodbus@pv: 30005-2-U32
```
