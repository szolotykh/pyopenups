pyopenups
=======================

pyopenups is a python wrap for Mini-Box OpenUPS API. OpenUPS is uninterruptible power supply module designed by Mini-Box for small computers. Current version of the module supports only Windows.
OpenUPS product page: http://www.mini-box.com/OpenUPS?sc=8&category=1264

Functions:
* UPSOpenDevice
* UPSCloseDevice
* is_ups_Connected
* get_ups_VIN
* get_ups_VBat
* get_ups_VOut
* get_ups_CCharge
* get_ups_CDischarge
* get_ups_CIn
* get_ups_VCell
* get_ups_Temperature
* get_ups_VerMajor
* get_ups_VerMinor
* get_ups_State
* get_ups_Year
* get_ups_Month
* get_ups_Day
* get_ups_Hour
* get_ups_Minute
* get_ups_Second
* get_ups_RemainingCapacity
* get_ups_RTE
* get_ups_OutputPower

UPS States:
* BATTERY_STATE
* VIN_STATE
* USB_STATE

Install:
```
$ python setup.py install
```

vsreality