import pywhatkit
import time

message = "sagopakajmer"
target_number = "+90-----------"
message_count = 250

for i in range(message_count):
    print(f"Mesaj {i+1}/{message_count} gönderiliyor...")
    pywhatkit.sendwhatmsg(target_number, message, int(time.strftime("%H")) , int(time.strftime("%M")) + 1 + i, wait_time=1)
    time.sleep(2)




