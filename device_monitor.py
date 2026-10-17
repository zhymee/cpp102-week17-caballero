def get_initial_readings():
	"""Return the starting device readings."""
	return [28, 31, 35, 37, 29]


def is_whole_number(text):
	"""Check whether text contains a whole number."""
	if text == "":
		return False

	position = 0
	for character in text:
		if character == "-" and position == 0:
			position = position + 1
		elif character in "0123456789":
			position = position + 1
		else:
			return False

	if text == "-":
		return False
	return True


def add_reading(readings, lowest, highest):
	"""Validate and add one reading to the list."""
	text = input("Enter new reading: ")

	if text == "":
		print("Invalid input. The reading cannot be empty.")
	elif not is_whole_number(text):
		print("Invalid input. Enter a whole number only.")
	else:
		reading = int(text)
		if reading < lowest or reading > highest:
			print("Invalid reading. Enter a value from 0 to 100.")
		else:
			readings.append(reading)
			print("Reading added successfully.")


def classify_reading(reading, warning_limit, critical_limit):
	"""Return the category for one temperature reading."""
	if reading < warning_limit:
		return "NORMAL"
	elif reading <= critical_limit:  # 35 is still WARNING.
		return "WARNING"
	else:
		return "CRITICAL"


def compute_total(readings):
	"""Add and return all readings."""
	total = 0
	for reading in readings:
		total = total + reading
	return total


def compute_average(readings):
	"""Return the average of the readings."""
	return compute_total(readings) / len(readings)


def find_minimum(readings):
	"""Find and return the smallest reading."""
	minimum = readings[0]
	for reading in readings:
		if reading < minimum:
			minimum = reading
	return minimum


def find_maximum(readings):
	"""Find and return the largest reading."""
	maximum = readings[0]
	for reading in readings:
		if reading > maximum:
			maximum = reading
	return maximum


def count_category(readings, warning_limit, critical_limit, category):
	"""Count readings that match a category."""
	count = 0
	for reading in readings:
		if classify_reading(reading, warning_limit, critical_limit) == category:
			count = count + 1
	return count


def determine_overall_status(warning_count, critical_count):
	"""Return the overall status from category counts."""
	if critical_count >= 1:
		return "ATTENTION REQUIRED"
	elif warning_count >= 1:
		return "MONITOR"
	else:
		return "NORMAL"


def display_menu():
	"""Show the system menu."""
	print("SIMULATED DEVICE MONITORING SYSTEM")
	print("----------------------------------")
	print("[1] View Readings")
	print("[2] Add Reading")
	print("[3] Classify Readings")
	print("[4] Generate Summary")
	print("[5] Exit")


def display_readings(readings):
	"""Display each current reading."""
	print("CURRENT READINGS")
	print("----------------")
	position = 1
	for reading in readings:
		print(f"Reading {position}: {reading} °C")
		position = position + 1


def display_classification(readings, warning_limit, critical_limit):
	"""Display the category of each reading."""
	print("READING CLASSIFICATION")
	print("----------------------")
	for reading in readings:
		category = classify_reading(reading, warning_limit, critical_limit)
		print(f"{reading} °C -> {category}")


def display_summary(readings, warning_limit, critical_limit):
	"""Calculate and display the monitoring summary."""
	normal_count = count_category(readings, warning_limit, critical_limit, "NORMAL")
	warning_count = count_category(readings, warning_limit, critical_limit, "WARNING")
	critical_count = count_category(readings, warning_limit, critical_limit, "CRITICAL")
	number_of_readings = len(readings)
	normal_percent = normal_count / number_of_readings * 100
	warning_percent = warning_count / number_of_readings * 100
	critical_percent = critical_count / number_of_readings * 100
	status = determine_overall_status(warning_count, critical_count)

	print("MONITORING SUMMARY")
	print("------------------")
	print(f"Number of readings  : {number_of_readings}")
	print(f"Total of readings   : {compute_total(readings)}")
	print(f"Average temperature : {compute_average(readings):.2f} °C")
	print(f"Minimum temperature : {find_minimum(readings)} °C")
	print(f"Maximum temperature : {find_maximum(readings)} °C")
	print()
	print(f"NORMAL   : {normal_count} ({normal_percent:.2f}%)")
	print(f"WARNING  : {warning_count} ({warning_percent:.2f}%)")
	print(f"CRITICAL : {critical_count} ({critical_percent:.2f}%)")
	print()
	print(f"Overall Status: {status}")


def main():
	"""Run the device monitoring menu."""
	readings = get_initial_readings()
	warning_limit = 30
	critical_limit = 35
	choice = ""

	while choice != "5":
		display_menu()
		choice = input("Enter choice: ")

		if choice == "1":
			display_readings(readings)
		elif choice == "2":
			add_reading(readings, 0, 100)
		elif choice == "3":
			display_classification(readings, warning_limit, critical_limit)
		elif choice == "4":
			display_summary(readings, warning_limit, critical_limit)
		elif choice == "5":
			print("Thank you for using the Device Monitoring System.")
		else:
			print("Invalid choice. Please enter a number from 1 to 5.")


main()
