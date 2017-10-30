# Import
from ctypes import *
import os

# ============= Load DLL=============
path_to_dll = os.path.dirname(os.path.realpath(__file__)) + "/../bin/OpenUPSLib.dll"
openups = cdll.LoadLibrary(path_to_dll)

# UPSOpenDevice
# Open UPS via HID (opens fist one if more connected)
# timer - timeperiod for requests (millisecond)
# Example: timer = 1000 will trigger three HID requests at ~300 msecond, ~600 msecond and ~1000 msecond.
#			This value is not accurate - based on Sleep(5) period.
#			It is provided only to finetune a different request period depending on the user's needs.
ups_open_device = openups.UPSOpenDevice
ups_open_device.restype = c_ubyte
ups_open_device.argtypes = [c_uint]
# UPSCloseDevice
ups_close_device = openups.UPSCloseDevice
ups_close_device.restype = None
# isUPSConnected
is_ups_connected = openups.isUPSConnected
is_ups_connected.restype = c_ubyte

# getUPSVIN
get_ups_vin = openups.getUPSVIN
get_ups_vin.restype = c_float
# getUPSVBat
get_ups_vbat = openups.getUPSVBat
get_ups_vbat.restype = c_float
# getUPSVOut
get_ups_vout = openups.getUPSVOut
get_ups_vout.restype = c_float
# getUPSCCharge
get_ups_ccharge = openups.getUPSCCharge
get_ups_ccharge.restype = c_float
# getUPSCDischarge
get_ups_cdischarge = openups.getUPSCDischarge
get_ups_cdischarge.restype = c_float
# getUPSCIn
get_ups_cin = openups.getUPSCIn
get_ups_cin.restype = c_float
# getUPSVCell
get_ups_vcell = openups.getUPSVCell
get_ups_vcell.restype = c_float
get_ups_vcell.argtypes = [c_int]
# getUPSTemperature
get_ups_temperature = openups.getUPSTemperature
get_ups_temperature.restype = c_float
# getUPSVerMajor
get_ups_ver_major = openups.getUPSVerMajor
get_ups_ver_major.restype = c_ubyte
# getUPSVerMinor
get_ups_ver_minor = openups.getUPSVerMinor
get_ups_ver_minor.restype = c_ubyte
# getUPSState
get_ups_state = openups.getUPSState
get_ups_state.restype = c_ubyte

# UPS States
BATTERY_STATE = 1
VIN_STATE = 2
USB_STATE = 3

# getUPSYear
get_ups_year = openups.getUPSYear
get_ups_year.restype = c_ubyte
# getUPSMonth
get_ups_month = openups.getUPSMonth
get_ups_month.restype = c_ubyte
# getUPSDay
get_ups_day = openups.getUPSDay
get_ups_day.restype = c_ubyte
# getUPSHour
get_ups_hour = openups.getUPSHour
get_ups_hour.restype = c_ubyte
# getUPSMinute
get_ups_minute = openups.getUPSMinute
get_ups_minute.restype = c_ubyte
# getUPSSecond
get_ups_second = openups.getUPSSecond
get_ups_second.restype = c_ubyte
# getUPSRemainingCapacity
get_ups_remaining_capacity = openups.getUPSRemainingCapacity
get_ups_remaining_capacity.restype = c_ubyte
# getUPSRTE
#if  getUPSRTE > 0xFFFF, then RTE not known, else RTE = minutes;
get_ups_rte = openups.getUPSRTE
get_ups_rte.restype = c_uint 

#getUPSOutputPower
get_ups_output_power = openups.getUPSOutputPower
get_ups_output_power.restype = c_float

