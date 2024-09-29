import keyboard
import os
from datetime import datetime

# Define the directory and log file path
log_dir = os.path.expanduser("~/Desktop/sus_logs")
log_file = os.path.join(log_dir, "sus_log.txt")

# Create the directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)


# Function to log key events
def log_event(event_type, event_name):
    current_time = datetime.now()
    log_message = f"[{current_time.strftime('%Y-%m-%d %H:%M:%S')}] {event_type}: {event_name}\n"

    with open(log_file, "a") as f:
        f.write(log_message)
    print(log_message.strip())  # Debug print


# Function to handle key events
def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        log_event("Key pressed", event.name)
    elif event.event_type == keyboard.KEY_UP:
        log_event("Key released", event.name)


# Set up key listener
keyboard.hook(on_key_event)

print(f"Recording keybinds. Press 'esc' to stop.")
print(f"Logs will be saved to: {log_file}")
keyboard.wait('esc')  # Stop the program when 'esc' is pressed

# Clean up
keyboard.unhook_all()
print("Logging stopped.")