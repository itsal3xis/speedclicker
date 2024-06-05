import time
import pyautogui
import tkinter as tk

root = tk.Tk()
root.title('Speed Clicker')


texteMenu = tk.Label(root, text='====Speed clicker====', font=('Arial', 16))
texteMenu2 = tk.Label(root, text='by itsal3xis', font=('Arial', 12))

texteMenu.pack()
texteMenu2.pack()

# ----------------------------------------------------------------


texteMenuNfois = tk.Label(root, text='Number of clicks:', font=('Arial', 14))

var = tk.IntVar()

radio_btn_1 = tk.Radiobutton(root, variable=var, text="50", value=50)
radio_btn_2 = tk.Radiobutton(root, variable=var, text="100", value=100)
radio_btn_3 = tk.Radiobutton(root, variable=var, text="500", value=500)


texteMenuNfois.pack()
radio_btn_1.pack()
radio_btn_2.pack()
radio_btn_3.pack()

nfois = var.get()

# -----------------------------------------------------------------

texteInt = tk.Label(root, text='Secondes between clicks:', font=('Arial', 14))

var2 = tk.IntVar()

radio_btn_4 = tk.Radiobutton(root, variable=var2, text="None", value=0)
radio_btn_5 = tk.Radiobutton(root, variable=var2, text="0.25", value=0.25)
radio_btn_6 = tk.Radiobutton(root, variable=var2, text="0.5", value=0.5)



texteInt.pack()
radio_btn_4.pack()
radio_btn_5.pack()
radio_btn_6.pack()


def on():
    fois = var.get()
    sec = var2.get()
    for i in range(0, fois):
        pyautogui.click()
        time.sleep(int(sec))
    root.destroy()
    quit()

btnOn = tk.Button(root, text='Start', command=on)
btnQuit = tk.Button(root, text='Quit', command=root.destroy)

btnOn.pack()
btnQuit.pack()








root.mainloop()





#on()