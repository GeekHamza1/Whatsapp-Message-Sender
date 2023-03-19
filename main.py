import pywhatkit

# Phone number of the recipient in international format (with country code, but without any leading zeros or plus sign)
phone_number = "+1**********"

# Message you want to send
message = "Hello Word"

# Hour and minute at which you want to send the message (optional)
hour = 4
minute = 15

# Send the message using sendwhatmsg() function
pywhatkit.sendwhatmsg(phone_number, message, hour, minute)