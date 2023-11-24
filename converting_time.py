
def convert24(time_str): 
	
	# Checking if last two elements of time 
	# is AM and first two elements are 12 
	if time_str[-2:] == "AM" and time_str[:2] == "12": 
		return "00" + time_str[2:-2] 
		
	# remove the AM	 
	elif time_str[-2:] == "AM": 
		return time_str[:-2] 
	
	# Checking if last two elements of time 
	# is PM and first two elements are 12 
	elif time_str[-2:] == "PM" and time_str[:2] == "12": 
		return time_str[:-2] 
		
	else: 
		
		# add 12 to hours and remove PM 
		return str(int(time_str[:2]) + 12) + time_str[2:8] 
	 
