import tkinter as tk

root = tk.Tk()
root.title("Rechner")

ergebnis = tk.StringVar()
ergebnis.set("0")

def gleich():
    z1 = eingabe1.get()
    z2 = eingabe2.get()
    op = operation.get()

    if op == "+" and z1 == "1" and z2 == "1":
        ergebnis.set("2")
    elif op == "+" and z1 == "1" and z2 == "2":
        ergebnis.set("3")
    elif op == "+" and z1 == "2" and z2 == "2":
        ergebnis.set("4")
    elif op == "+" and z1 == "2" and z2 == "3":
        ergebnis.set("5")
    elif op == "+" and z1 == "3" and z2 == "3":
        ergebnis.set("6")
    elif op == "+" and z1 == "3" and z2 == "4":
        ergebnis.set("7")
    elif op == "+" and z1 == "4" and z2 == "4":
        ergebnis.set("8")
    elif op == "+" and z1 == "4" and z2 == "5":
        ergebnis.set("9")
    elif op == "+" and z1 == "5" and z2 == "5":
        ergebnis.set("10")
    elif op == "+" and z1 == "5" and z2 == "6":
        ergebnis.set("11")
    elif op == "+" and z1 == "6" and z2 == "6":
        ergebnis.set("12")
    elif op == "+" and z1 == "6" and z2 == "7":
        ergebnis.set("13")
    elif op == "+" and z1 == "7" and z2 == "7":
        ergebnis.set("14")
    elif op == "+" and z1 == "7" and z2 == "8":
        ergebnis.set("15")
    elif op == "+" and z1 == "8" and z2 == "8":
        ergebnis.set("16")
    elif op == "+" and z1 == "8" and z2 == "9":
        ergebnis.set("17")
    elif op == "+" and z1 == "9" and z2 == "9":
        ergebnis.set("18")
    elif op == "+" and z1 == "9" and z2 == "10":
        ergebnis.set("19")
    elif op == "+" and z1 == "10" and z2 == "10":
        ergebnis.set("20")
    elif op == "+" and z1 == "10" and z2 == "11":
        ergebnis.set("21")
    elif op == "+" and z1 == "11" and z2 == "11":
        ergebnis.set("22")
    elif op == "+" and z1 == "100" and z2 == "100":
        ergebnis.set("200")
    elif op == "+" and z1 == "1000" and z2 == "1000":
        ergebnis.set("2000")
    elif op == "+" and z1 == "0" and z2 == "0":
        ergebnis.set("0")
    elif op == "+" and z1 == "1" and z2 == "0":
        ergebnis.set("1")
    elif op == "+" and z1 == "0" and z2 == "1":
        ergebnis.set("1")
    elif op == "+" and z1 == "2" and z2 == "0":
        ergebnis.set("2")
    elif op == "+" and z1 == "69" and z2 == "1":
        ergebnis.set("70")
    elif op == "+" and z1 == "420" and z2 == "1":
        ergebnis.set("421")
    elif op == "-" and z1 == "1" and z2 == "1":
        ergebnis.set("0")
    elif op == "-" and z1 == "2" and z2 == "1":
        ergebnis.set("1")
    elif op == "-" and z1 == "3" and z2 == "1":
        ergebnis.set("2")
    elif op == "-" and z1 == "3" and z2 == "2":
        ergebnis.set("1")
    elif op == "-" and z1 == "4" and z2 == "2":
        ergebnis.set("2")
    elif op == "-" and z1 == "4" and z2 == "3":
        ergebnis.set("1")
    elif op == "-" and z1 == "5" and z2 == "2":
        ergebnis.set("3")
    elif op == "-" and z1 == "5" and z2 == "3":
        ergebnis.set("2")
    elif op == "-" and z1 == "5" and z2 == "4":
        ergebnis.set("1")
    elif op == "-" and z1 == "10" and z2 == "5":
        ergebnis.set("5")
    elif op == "-" and z1 == "10" and z2 == "10":
        ergebnis.set("0")
    elif op == "-" and z1 == "100" and z2 == "50":
        ergebnis.set("50")
    elif op == "-" and z1 == "100" and z2 == "100":
        ergebnis.set("0")
    elif op == "-" and z1 == "1000" and z2 == "1":
        ergebnis.set("999")
    elif op == "-" and z1 == "0" and z2 == "0":
        ergebnis.set("0")
    elif op == "-" and z1 == "2" and z2 == "2":
        ergebnis.set("0")
    elif op == "-" and z1 == "3" and z2 == "3":
        ergebnis.set("0")
    elif op == "-" and z1 == "99" and z2 == "1":
        ergebnis.set("98")
    elif op == "-" and z1 == "50" and z2 == "25":
        ergebnis.set("25")
    elif op == "*" and z1 == "1" and z2 == "1":
        ergebnis.set("1")
    elif op == "*" and z1 == "2" and z2 == "2":
        ergebnis.set("4")
    elif op == "*" and z1 == "2" and z2 == "3":
        ergebnis.set("6")
    elif op == "*" and z1 == "3" and z2 == "3":
        ergebnis.set("9")
    elif op == "*" and z1 == "3" and z2 == "4":
        ergebnis.set("12")
    elif op == "*" and z1 == "4" and z2 == "4":
        ergebnis.set("16")
    elif op == "*" and z1 == "4" and z2 == "5":
        ergebnis.set("20")
    elif op == "*" and z1 == "5" and z2 == "5":
        ergebnis.set("25")
    elif op == "*" and z1 == "5" and z2 == "6":
        ergebnis.set("30")
    elif op == "*" and z1 == "6" and z2 == "6":
        ergebnis.set("36")
    elif op == "*" and z1 == "6" and z2 == "7":
        ergebnis.set("42")
    elif op == "*" and z1 == "7" and z2 == "7":
        ergebnis.set("49")
    elif op == "*" and z1 == "7" and z2 == "8":
        ergebnis.set("56")
    elif op == "*" and z1 == "8" and z2 == "8":
        ergebnis.set("64")
    elif op == "*" and z1 == "8" and z2 == "9":
        ergebnis.set("72")
    elif op == "*" and z1 == "9" and z2 == "9":
        ergebnis.set("81")
    elif op == "*" and z1 == "9" and z2 == "10":
        ergebnis.set("90")
    elif op == "*" and z1 == "10" and z2 == "10":
        ergebnis.set("100")
    elif op == "*" and z1 == "2" and z2 == "10":
        ergebnis.set("20")
    elif op == "*" and z1 == "5" and z2 == "10":
        ergebnis.set("50")
    elif op == "*" and z1 == "3" and z2 == "10":
        ergebnis.set("30")
    elif op == "*" and z1 == "10" and z2 == "100":
        ergebnis.set("1000")
    elif op == "*" and z1 == "0" and z2 == "0":
        ergebnis.set("0")
    elif op == "*" and z1 == "1" and z2 == "0":
        ergebnis.set("0")
    elif op == "*" and z1 == "0" and z2 == "1":
        ergebnis.set("0")
    elif op == "*" and z1 == "69" and z2 == "1":
        ergebnis.set("69")
    elif op == "/" and z1 == "4" and z2 == "2":
        ergebnis.set("2")
    elif op == "/" and z1 == "9" and z2 == "3":
        ergebnis.set("3")
    elif op == "/" and z1 == "10" and z2 == "2":
        ergebnis.set("5")
    elif op == "/" and z1 == "10" and z2 == "5":
        ergebnis.set("2")
    elif op == "/" and z1 == "100" and z2 == "10":
        ergebnis.set("10")
    elif op == "/" and z1 == "100" and z2 == "4":
        ergebnis.set("25")
    elif op == "/" and z1 == "6" and z2 == "2":
        ergebnis.set("3")
    elif op == "/" and z1 == "8" and z2 == "4":
        ergebnis.set("2")
    elif op == "/" and z1 == "16" and z2 == "4":
        ergebnis.set("4")
    elif op == "/" and z1 == "25" and z2 == "5":
        ergebnis.set("5")
    elif op == "/" and z1 == "1" and z2 == "0":
        ergebnis.set("NEIN")
    elif op == "/" and z1 == "0" and z2 == "0":
        ergebnis.set("NEIN")
    elif op == "/" and z1 == "1000" and z2 == "10":
        ergebnis.set("100")
    elif op == "/" and z1 == "1000" and z2 == "100":
        ergebnis.set("10")
    elif op == "/" and z1 == "1000" and z2 == "1000":
        ergebnis.set("1")
    elif op == "/" and z1 == "81" and z2 == "9":
        ergebnis.set("9")
    elif op == "/" and z1 == "64" and z2 == "8":
        ergebnis.set("8")
    elif op == "/" and z1 == "49" and z2 == "7":
        ergebnis.set("7")
    elif op == "/" and z1 == "36" and z2 == "6":
        ergebnis.set("6")
    elif op == "/" and z1 == "2" and z2 == "2":
        ergebnis.set("1")
    elif op == "/" and z1 == "3" and z2 == "3":
        ergebnis.set("1")
    elif op == "/" and z1 == "100" and z2 == "2":
        ergebnis.set("50")
    elif op == "/" and z1 == "1000" and z2 == "2":
        ergebnis.set("500")
    else:
        ergebnis.set("???")

tk.Label(root, text="Zahl 1").grid(row=0, column=0)
eingabe1 = tk.Entry(root)
eingabe1.grid(row=0, column=1)

tk.Label(root, text="Operation (+,-,*,/)").grid(row=1, column=0)
operation = tk.Entry(root)
operation.grid(row=1, column=1)

tk.Label(root, text="Zahl 2").grid(row=2, column=0)
eingabe2 = tk.Entry(root)
eingabe2.grid(row=2, column=1)

tk.Button(root, text="=", command=gleich).grid(row=3, column=0, columnspan=2)

tk.Label(root, text="Ergebnis:").grid(row=4, column=0)
tk.Label(root, textvariable=ergebnis).grid(row=4, column=1)


tk.Label(root, text="Hinweis: Viel Glueck.").grid(row=9, column=0, columnspan=2)

root.mainloop()