import tkinter as tk

class TextRedirector(object):
    def __init__(self, widget):
        self.widget = widget

    def write(self, str):
        self.widget.insert(tk.END, str)
        self.widget.see(tk.END)

def run_click():
    output['state'] = 'normal'  # Enable editing
    output.delete(1.0, tk.END)  # Clear existing text
    text = memo.get(1.0, tk.END)
    print(text)
    with open('file.txt', 'w') as file:
        file.write(text)
    output.insert(tk.END, text)  # Insert the text from the memo widget
    output['state'] = 'disabled'  # Disable editing


def close_click():
    window.destroy()

window = tk.Tk()
window.geometry('800x800')

# Create a menu bar
menu = tk.Menu(window)
window.config(menu=menu)

# Create the 'File' menu
filemenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=filemenu)

# Add commands to the 'File' menu
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=close_click)

# Create the 'Help' menu
helpmenu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=helpmenu)

# Add commands to the 'Help' menu
helpmenu.add_command(label='About')

memo = tk.Text(window, width=100, height=35)
scroll = tk.Scrollbar(window, command=memo.yview)
memo['yscrollcommand'] = scroll.set

# Grid method used for more control
memo.grid(row=0, column=0, sticky='nsew')
scroll.grid(row=0, column=1, sticky='ns')

# Create a frame to act as a 50-pixel spacer
spacer = tk.Frame(window, height=50)
spacer.grid(row=1, column=0, sticky='nsew')

# Create the console output area
output = tk.Text(window, width=100, height=10, state='disabled', bg='black', fg='white')
output.grid(row=2, column=0, sticky='nsew')

# Create a frame for the buttons
button_frame = tk.Frame(window, width=150)
button_frame.grid(row=0, column=2, rowspan=5, sticky='ns')

# Create the buttons
run_button = tk.Button(button_frame, text="Run", command=run_click)
close_button = tk.Button(button_frame, text="Stop", command=close_click)

buttonY = 20
buttonYSize = 60
buttonYClose = buttonY + buttonYSize
# Place the buttons with specific dimensions and margins
run_button.place(x=25, y=buttonY, width=100, height=50)
close_button.place(x=25, y=buttonYClose, width=100, height=50)

# Configure grid to expand properly
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

window.mainloop()
