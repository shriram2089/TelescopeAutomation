# TelescopeAutomation
Automated a manual 10-inch telescope by integrating live latitude, longitude, and time zone data, using a stepper motor attached to its base for precise tracking of celestial objects.


Components:
Hardware:

10-inch Manual Telescope: The primary instrument for observing celestial objects.
Stepper Motor: Controls the base rotation for accurate alignment and tracking.
ESP32 Microcontroller: Manages the stepper motor and processes live GPS data.
GPS Module: Provides real-time latitude, longitude, and time zone information.
Power Supply: Powers the stepper motor and ESP32.
Software:

ESP32 Firmware: Controls the stepper motor based on GPS data and calculates the necessary adjustments for tracking.
Python Interface: Facilitates communication between the user and the telescope system, allowing for real-time adjustments and monitoring.
Methodology:
1. Hardware Setup:
Mounting: Attach the stepper motor to the telescope’s base for rotational control.
Connections: Connect the stepper motor, GPS module, and power supply to the ESP32 microcontroller.
2. ESP32 Firmware:
GPS Data Acquisition: Implement functions to read latitude, longitude, and time zone from the GPS module.
Motor Control: Develop algorithms to adjust the stepper motor based on the current GPS data for precise tracking.
Communication: Use serial or Wi-Fi for remote control and status monitoring.
