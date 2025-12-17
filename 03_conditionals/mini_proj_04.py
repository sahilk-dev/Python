# Task: You're building a smart thermostat alert system.
    # * If the device_status is "active"
        # * And tempreture > 35 -> Warn: "High tempreture alert!"
        # * Else: "Tempreture normal"
    # * if device is off -> "Device is offline"

device_status = "active"
temprature = 38

if device_status == "active":
    if temprature > 35:
        print("High tempreture alert!")
    else:
        print("Tempreture is normal")
else:
    print("Device if offline")