import time
from pyopenups import *

if ups_open_device(1000):
	time.sleep(0.5)
	print " Firmware: {0}.{1}".format(get_ups_ver_major(), get_ups_ver_minor())
	state = get_ups_state()
	if state == BATTERY_STATE:
		state_str = "Battery"
	elif state == VIN_STATE:
		state_str = "VIn"
	elif state == USB_STATE:
		state_str = "USB"
	else:
		state_str = "Error"
	print " State: {}".format(state_str)
	
	print " POut: {}".format(get_ups_output_power())
	print " VIN: {}".format(get_ups_vin())
	print " VBAT: {}".format(get_ups_vbat())
	print " VOut: {}".format(get_ups_vout())
	print " ACharge: {}".format(get_ups_ccharge())
	print " ADischg: {}".format(get_ups_cdischarge())
	print " AIn: {}".format(get_ups_cin())
	print " Temp: {}".format(get_ups_temperature())
	print " VCell{"
	for i in range(0,6):
		print "  [{0}] = {1}".format(i ,get_ups_vcell(i))
	print " }"
	
	ups_close_device();