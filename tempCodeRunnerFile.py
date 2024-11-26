stall pyperclip

# Step 1: Click on the icon at coordinates (590, 750)
pyautogui.moveTo(590, 750)  # Move to the icon
pyautogui.click()           # Perform a click

# Wait for a moment to ensure the application responds
time.sleep(1)

# Step 2: Drag to select text from (512, 175) to (1274, 690)
pyautogui.moveTo(512, 175)  # Move to the start position
pyautogui.mouseDown()       # Press and hold the mouse button
pyautogui.moveTo(1274, 690, duration=1)  # Drag to the end position
pyautogui.mouseUp()         # Release the mouse button

# Wait briefly to ensure selection is registered
time.sleep(0.5)

# Step 3: Copy the selected text to the clipboard (Ctrl+C)
pyautogui.hotkey('ctrl', 'c')

# Wait for clipboard to update
time.sleep(0.5)

# Step 4: Retrieve the text from the clipboard into a variable
text = pyperclip.paste()

# Step 5: Print the copied text (optional)
print("Copied Text:", text)
