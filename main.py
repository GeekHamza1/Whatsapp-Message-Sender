import pywhatkit as kit

# Phone number in international format (e.g., +1234567890)
phone_number = '+1234567890'

# The message you want to send
message = 'Hello, this is a test message sent using pywhatkit!'

# Send message (time is set to now, but pywhatkit requires a time in the future)
kit.sendwhatmsg(phone_number, message, 0, 0)  # The time is set to 00:00 for "now"
