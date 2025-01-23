import tkinter as tk
import webbrowser   # Import Necessary Modules #
import os

def generate_webpage():
    user_input = text_entry.get()
    html_content = f"<!DOCTYPE html>\n<html>\n<head><title>User Page</title></head>\n<body>{user_input}</body>\n</html>"
    file_path = 'user_page.html'
    with open(file_path, 'w') as file: # Generate a 'User Input' WebPage that allows Custom Text Field #in GUI and opens a New Browser Window #
        file.write(html_content)
    webbrowser.open('file://' + os.path.realpath(file_path))

app = tk.Tk()  
app.title('Web Page Generator') # Dimensions + Title of GUI Window #
app.geometry('300x200')  

text_label = tk.Label(app, text='Enter CUSTOM TEXT Here:') # Custom Text Entry Field #
text_label.pack()  
text_entry = tk.Entry(app)
text_entry.pack()  

generate_button = tk.Button(app, text='Create Your Very Page!', command=generate_webpage) # Message telling user to create their own webpage # 
generate_button.pack()  


def generate_webpage2():
    user_input = text_entry.get()
    html_content = f"<!DOCTYPE html>\n<html>\n<head><title>User Page</title></head>\n<body>{'STAY TUNED FOR OUR AMAZING SUMMER SALE... STARTS NOW!!!'}</body>\n</html>"
    file_path = 'index.html' 
    with open(file_path, 'w') as file: # Replicate 1st Function(generate_webpage) and Modify to be a fixed message for "Summer Sale" that is Displayed as Default HTML Page when Clicked #
        file.write(html_content)
    webbrowser.open('file:///Users/reeddecker/Desktop/index.html')

generate_button = tk.Button(app, text='Default HTML Webpage', command=generate_webpage2)
generate_button.pack()
        


app.mainloop()  
