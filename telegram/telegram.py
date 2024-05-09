from telethon.sync import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
import time

api_id = 'API_ID'
api_hash = 'API_HASH'

target_number = '+90-------------'


def send_message(api_id, api_hash, phone, message):
    client = TelegramClient('session', api_id, api_hash)

    with client:
        client.send_message(phone, message)

message = "babubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabubabu"

message_count = 250

for i in range(message_count):
    print(f"Mesaj {i+1}/{message_count} gönderiliyor...")
    send_message(api_id, api_hash, target_number, message)
    time.sleep(1)
