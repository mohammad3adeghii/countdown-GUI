import tkinter as tk

app = tk.Tk()
app.title("countdown")
app.configure(bg="lightblue")

text_var = tk.StringVar()
text_var.set("enter the time: ")

init_text = tk.Label(app,textvariable=text_var)
init_text.pack(padx=10, pady=10)

input_text = tk.Entry(app)
input_text.pack(padx=10, pady=10)

text_var1 = tk.StringVar()
def countdown(t):
    if t>=0:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins,secs)

        text_var.set(timer)
        app.after(1000,countdown,t-1)


def start_countdown():
    try:
        t = int(input_text.get())
        countdown(t)
    except ValueError:
        print("Error", ValueError)

start_countdown = tk.Button(app, text="start", command=start_countdown)
start_countdown.pack(padx=10, pady=10)

app.mainloop()