import keyboard
import time
import pyautogui
import google.generativeai as genai
from PIL import Image
import tkinter as tk  # Using the full name for clarit

genai.configure(api_key="YOUR-API-KEY-HERE")
model = genai.GenerativeModel('gemini-pro-vision')
def my_function():
    print("Hotkey pressed! Executing actions...")

    # Capture a screenshot, wait briefly for UI updates
    time.sleep(3)
    im = pyautogui.screenshot()
    im.save("SS1.jpg")

    # Generate a response using Gemini Pro Vision
    question = Image.open("SS1.jpg")
    prompt = "Can you identify the text inside the image and solve the maths problem :"
    response = model.generate_content(
        contents=[prompt, question]
    )

    # Display the response in a popup window
    message_to_print = response.text
    show_popup(message_to_print)

def show_popup(message):
    """Creates and displays a pop-up window with the given message."""
    root = tk.Tk()  # Create the main window
    root.title("Popup Message")  # Set the window title

    # Create a label to display the message
    label = tk.Label(root, text=message)
    label.pack(padx=10, pady=10)  # Add padding for better appearance

    # Keep the window open until manually closed
    root.mainloop()

keyboard.add_hotkey('/', my_function)  # Assign my_function to the hotkey
keyboard.wait('esc')  # Keep listening for hotkeys until Esc is pressed
