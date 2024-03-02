import keyboard

def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        print(f"Key {event.name} was pressed")
    #elif event.event_type == keyboard.KEY_UP:
       #print(f"Key {event.name} was released")

keyboard.on_press(on_key_event)
#keyboard.on_release(on_key_event)

print("Listening for keyboard events. Press 'Esc' to quit.")
keyboard.wait("esc")  # This will wait until the 'Esc' key is pressed;

# import keyboard

# def print_array(array: list[str]):
#     print(f"""
#     +---+---+---+
#     | {array[0]} | {array[1]} | {array[2]} |
#     +---+---+---+
#     | {array[3]} | {array[4]} | {array[5]} |
#     +---+---+---+
#     | {array[6]} | {array[7]} | {array[8]} |
#     +---+---+---+
#     """)

# while True:
#     if keyboard.read_key() == "p":
#         print("p")

# array: list[str] = [
#     "0", "O", " ",
#     "0", "O", " ",
#     "0", "O", " ",
# ]

# print_array(array)

# array[0] = "/"

# print_array(array)
