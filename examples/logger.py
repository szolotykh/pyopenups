# OpenUPS CSV Logger
from pyopenups import *
from time import sleep, localtime, strftime
import csv

sempling_interval = 10 #sec

if ups_open_device(1000):
	sleep(0.5)
	try:
		with open('log.csv', 'w') as csvfile:
			fieldnames = ["Time", "State", "POut", "VIN", "VBAT", "VOut", "ACharge", "ADischg", "AIn", "Temp"]
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',', quotechar='|', lineterminator='\n')

			writer.writeheader()
			while True:
				state = get_ups_state()
				
				log_data = {
					"Time": strftime("%d %b %Y %H:%M:%S", localtime()),
					"State": get_ups_state(),
					"POut": get_ups_output_power(),
					"VIN": get_ups_vin(),
					"VBAT": get_ups_vbat(),
					"VOut": get_ups_vout(),
					"ACharge": get_ups_ccharge(),
					"ADischg": get_ups_cdischarge(),
					"AIn": get_ups_cin(),
					"Temp": get_ups_temperature()}
				writer.writerow(log_data)
				print log_data
				sleep(sempling_interval)
				
	except:
		ups_close_device()