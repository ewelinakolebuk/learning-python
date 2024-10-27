import tkinter
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=50, pady=20)

label_is_equal_to = tkinter.Label(text="is equal to ")
label_is_equal_to.grid(column=0, row=1)
label_is_equal_to.config(padx=10, pady=10)

label_miles=tkinter.Label(text="Miles")
label_miles.grid(column=2, row=0)
label_miles.config(padx=10, pady=10)

label_km=tkinter.Label(text="Km")
label_km.grid(column=2, row=1)

label_result=tkinter.Label(text=" ")
label_result.grid(column=1, row=1)

def button_clicked():
    result=int(input.get())*1.609
    label_result.config(text=result)


calculate_button=tkinter.Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

input = tkinter.Entry(width=10)
input.get()
input.grid(column=1, row=0)

window.mainloop()