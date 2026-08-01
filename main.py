from config.settings import APPLICATION_NAME, PLC_IP, PLC_PORT
from services.startup import display_startup_message

display_startup_message()

print(f"PLC IP   : {PLC_IP}")
print(f"PLC PORT : {PLC_PORT}")
