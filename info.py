import os
# Bot information
API_ID = os.getenv('API_ID', "26992030")
API_HASH = os.getenv('API_HASH', "4da7d71c6bc4512a886e41aca83a5ee3")
BOT_TOKEN = os.getenv('BOT_TOKEN', "7861489855:AAHsF6S5n_3y7VO7RMwXL62oG2e_d_Qvwsc")

# stream vars
PORT = int(os.getenv('PORT', '5050'))
BIN_CHANNEL = os.getenv("BIN_CHANNEL", "-1002494241960") #Log Channel
URL = os.getenv("URL", "") #App URL not MongoDB URL
