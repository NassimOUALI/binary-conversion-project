import customtkinter as ctk
import tkinter as tk


# Function to navigate to project1
def navigate_to_project1():
    enable_all_buttons()
    nav1.configure(state="disabled")
    disable_all_frames()
    frame1.pack(expand="true", fill="both")
    disable_all_options()
    option1.pack(expand="true", fill="both")


# Function to navigate to project2
def navigate_to_project2():
    enable_all_buttons()
    nav2.configure(state="disabled")
    disable_all_frames()
    frame2.pack(expand="true", fill="both")
    disable_all_options()
    option2.pack(expand="true", fill="both")


# Function to navigate to project3
def navigate_to_project3():
    enable_all_buttons()
    nav3.configure(state="disabled")
    disable_all_frames()
    frame3.pack(expand="true", fill="both")
    disable_all_options()
    option3.pack(expand="true", fill="both")


# Function to enable all navigation buttons
def enable_all_buttons():
    nav1.configure(state="normal")
    nav2.configure(state="normal")
    nav3.configure(state="normal")


def disable_all_frames():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()


def disable_all_options():
    option1.pack_forget()
    option2.pack_forget()
    option3.pack_forget()


def switch_app():
    global ui_dark
    if ui_dark:
        ctk.set_appearance_mode("light")
        ui_dark = False
        light_mode1.select()
        light_mode2.select()
        light_mode3.select()

    else:
        ctk.set_appearance_mode("dark")
        ui_dark = True
        light_mode1.deselect()
        light_mode2.deselect()
        light_mode3.deselect()


def DBorBD1(Choice):
    if Choice == "int → bin":
        Entry2.configure(placeholder_text="donner un entier...")
        Button2.configure(command=lambda: proj21(Entry2.get(), methode.get(), bit.get()))
    else:
        Entry2.configure(placeholder_text="donner un code bin...")
        Button2.configure(command=lambda: proj22(Entry2.get(), methode.get()))


def DBorBD2(char):
    global choice1
    global choice2

    if choice1.get() == "int → bin":
        Entry3.configure(placeholder_text="donner un entier...")
        if choice2.get() == "Fixe":
            Button3.configure(command=lambda: fixeFB(float(Entry3.get())))
            print(char)
        else:
            Button3.configure(command=lambda: IEEEFB(float(Entry3.get()), '32'))
            print(char)

    else:
        Entry3.configure(placeholder_text="donner un code bin...")
        if choice2.get() == "Fixe":
            Button3.configure(command=lambda: fixeBF(Entry3.get()))
            print(char)
        else:
            Button3.configure(command=lambda: IEEEBF(Entry3.get(), '32'))
            print(char)
    return


def convert(A, B, X):
    # making sure 2<A<16 :

    if int(A) < 2 or int(A) > 16:
        results1.configure(text="ERROR (001) : A n'est pas entre 2 et 16", text_color="red")
        print(100 * "-")
        print("\033[91m ERROR:001 \033[0m")
        print("\033[91m A n'est pas entre 2 et 16\033[0m")
        return
    # making sure 2<B<16 :

    if int(B) < 2 or int(B) > 16:
        results1.configure(text="ERROR (002) : B n'est pas entre 2 et 16", text_color="red")
        print(100 * "-")
        print("\033[91m\n -ERROR:002 \033[0m")
        print("\033[91m  B n'est pas entre 2 et 16\033[0m\n")
        return

    # inputing the binary number and checking that X is in the A base :

    Xcheck = True

    X = X.upper()

    for i in range(len(X)):
        if ord("0") <= ord(X[i]) <= ord("9"):
            if int(X[i]) >= int(A):
                Xcheck = False
                results1.configure(text="ERROR (003) : X n'est pas entre dans la base " + str(A), text_color="red")
                print(100 * "-")
                print("\033[91m -ERROR:003\n X n'est pas de la base " + str(A) + "\033[0m")

        elif ord("F") >= ord(X[i]) >= ord("A"):
            if ord(X[i]) >= (ord("A") + int(A) - 10):
                Xcheck = False
                results1.configure(text="ERROR (003) : X n'est pas entre dans la base " + str(A), text_color="red")
                print(100 * "-")
                print("\033[91m -ERROR:003\n X n'est pas de la base " + str(A) + "\033[0m")

            else:
                Xcheck = True
        else:
            Xcheck = False
            results1.configure(text="ERROR (003) : X n'est pas entre dans la base " + str(A), text_color="red")
            print(100 * "-")
            print("\033[91m -ERROR:003\n X n'est pas de la base " + str(A) + "\033[0m")

    if not Xcheck:
        return
    # converting from base A to base 10 :

    base10 = 0

    for i in range(0, len(X)):
        if ord("0") <= ord(X[i]) <= ord("9"):
            base10 += int(X[i]) * (int(A) ** (len(X) - 1 - i))
        elif ord("F") >= ord(X[i]) >= ord("A"):
            base10 += int(ord(X[i]) - ord("A") + 10) * (int(A) ** (len(X) - 1 - i))

    # converting from base 10 to base B :

    if base10 == 0:
        solution = "0"
    else:
        solution = ""
        while base10 > 0:
            remainder = base10 % int(B)

            if remainder >= 10:
                # --Ord gives the unicode of a char
                solution += chr(ord("A") + remainder - 10)
            else:
                solution += str(remainder)

            base10 //= int(B)

    # --reverse the order
    solution = solution[::-1]

    print("\nbase " + str(A) + " : " + X + " --> " + "base " + str(B) + " : " + solution)
    results1.configure(text="base " + str(A) + " : " + X + "   →   " + "base " + str(B) + " : " + solution,
                       text_color="#808080")
    return str(solution)


def vsDB(x, precison):
    if x >= 0:
        signe = "0"
    else:
        signe = "1"
        x = -x

    if x == 0:
        solution = "0"
    else:
        solution = ""
        while x > 0:
            remainder = x % 2
            solution += str(remainder)

            x //= 2
    if precison != "AUTO":
        for i in range(len(solution), int(precison) - 1):
            solution = solution + "0"
    else:
        # --complete the 8 or 4 bits
        if len(solution) < 4:
            for i in range(len(solution), 3):
                solution = solution + "0"
        elif len(solution) < 8:
            for i in range(len(solution), 7):
                solution = solution + "0"
        elif len(solution) < 16:
            for i in range(len(solution), 15):
                solution = solution + "0"

    # --reverse the order
    solution = solution + signe
    solution = solution[::-1]

    return str(solution)


# ------------------------------------------------------------------------


def ca1DB(x, precision):
    if x < 0:
        negatif = True
        x = -x
    else:
        negatif = False

    if x == 0:
        temp = "0"
    else:
        temp = ""
        while x > 0:
            remainder = x % 2
            temp += str(remainder)

            x //= 2
    print(temp)
    if precision != "AUTO":
        for i in range(len(temp), int(precision)):
            temp = temp + "0"
    else:
        if len(temp) < 4:
            for i in range(len(temp), 4):
                temp = temp + "0"
        elif len(temp) < 8:
            for i in range(len(temp), 8):
                temp = temp + "0"
        elif len(temp) < 16:
            for i in range(len(temp), 16):
                temp = temp + "0"
    temp = temp[::-1]
    if negatif:
        temp = temp.replace("0", "2").replace("1", "0").replace("2", "1")
    return str(temp)


# -----------------------------------------------------------------------------------------


def ca2DB(x, p):
    if x < 0:
        negatif = True
        x = -x
    else:
        negatif = False

    temp = vsDB(x, p)
    temp = str(temp)

    if negatif:
        temp = temp.replace("0", "2").replace("1", "0").replace("2", "1")
        temp = list(temp)
        temp = temp[::-1]
        for i in range(0, len(temp)):
            if temp[i] == "1":
                temp[i] = "0"
            elif temp[i] == "0":
                temp[i] = "1"
                break
        # pour la rendre une chaine de charactere
        temp = temp[::-1]
    temp = ''.join(temp)
    return str(temp)


# -----------------------------------------------------------------------------------------

def proj21(y, m, p):
    if (y[0] == '-' and y[1:].isdigit()) or y.isdigit():
        if m == "VS":
            Results2.configure(text="En utilsant VS on a : " + vsDB(int(y), p), text_color="#808080")
        elif m == "CA1":
            Results2.configure(text="En utilsant CA1 on a : " + ca1DB(int(y), p), text_color="#808080")
        elif m == "CA2":
            Results2.configure(text="En utilsant CA2 on a : " + ca2DB(int(y), p), text_color="#808080")
        elif m == "NULL":
            Results2.configure(text="Selectionez une methode", text_color="red")
    else:
        Results2.configure(text="Saisie incorrect", text_color="red")


# -----------------------------------------------------------------------------------------

def vsBD(bin_str):
    sign = 1
    if bin_str[0] == '1':
        sign = -1
    bin_str = bin_str[1:]
    solution = int(bin_str, 2)
    solution *= sign
    return str(solution)


# ------------------------------------------------------------------------------------------
def ca1BD(bin_str):
    sign = 1
    if bin_str[0] == '1':
        sign = -1
        bin_str = ''.join(['1' if Bit == '0' else '0' for Bit in bin_str])

    bin_str = bin_str[1:]

    solution = int(bin_str, 2)
    solution *= sign
    return str(solution)


# ------------------------------------------------------------------------------------------
def ca2BD(bin_string):
    bin = list(bin_string)
    if bin[0] == '1':
        bin = bin[1::]
        bin = bin[::-1]
        for i in range(len(bin)):
            if bin[i] == '0':
                bin[i] = '1'
            else:
                bin[i] = '0'
                break
        bin = bin[::-1]
        signe = -1
        for i in range(len(bin)):
            if bin[i] == '0':
                bin[i] = '1'
            else:
                bin[i] = '0'
    else:
        return vsBD(bin_string)
    base10 = 0

    for i in range(0, len(bin)):
        if ord("0") <= ord(bin[i]) <= ord("9"):
            base10 += int(bin[i]) * (2 ** (len(bin) - 1 - i))
        elif ord("F") >= ord(bin[i]) >= ord("A"):
            base10 += int(ord(bin[i]) - ord("A") + 10) * (2 ** (len(bin) - 1 - i))
    return str(base10 * signe)


# ------------------------------------------------------------------------------------------

def proj22(y, m):
    Xcheck = True
    if len(y) < 2:
        Xcheck = False
    for char in y:
        if char not in ('0', '1'):
            Xcheck = False

    if Xcheck:
        if m == "VS":
            Results2.configure(text="En utilsant VS on a : " + vsBD(str(y)), text_color="#808080")
        elif m == "CA1":
            Results2.configure(text="En utilsant CA1 on a : " + ca1BD(str(y)), text_color="#808080")
        elif m == "CA2":
            Results2.configure(text="En utilsant CA2 on a : " + ca2BD(str(y)), text_color="#808080")
        elif m == "NULL":
            Results2.configure(text="Selectionez une methode", text_color="red")
    else:
        Results2.configure(text="Saisie incorrect", text_color="red")


# ------------------------------------------------------------------------------------------

def fixeFB(F):
    i = 0
    D = int(F)
    F -= D
    if F < 0:
        signe = "1"
    else:
        signe = "0"
    Solution = vsDB(D, "7")
    Solution2 = ['0'] * 8

    while i < 8:
        F *= 2
        if int(F) == 1 or int(F) == -1:
            F -= int(F)
            Solution2[i] = '1'
        else:
            F -= int(F)
            Solution2[i] = '0'
        i += 1

    temp = ''.join(signe) + ''.join(Solution) + ''.join(Solution2)
    Results3.configure(text="En utilisant la methode fixe : " + temp,
                       text_color="#808080")
    print(temp)


# ------------------------------------------------------------------------------------------


def fixeBF(X):
    Bin1 = X[:8]
    S1 = int(vsBD(Bin1))

    Bin2 = X[8:]
    Bin2 = Bin2[::-1]

    if '1' in Bin2:
        F = 1
        index = Bin2.index('1')
        Bin2 = Bin2[index:]  # Remove leading zeros
        F = F / 2
        for i in range(1, len(Bin2)):
            if Bin2[i] == '1':
                F += 1
            F = F / 2

        if S1 < 0:
            F = -F
    else:
        F = 0

    Results3.configure(text="En utilisant la methode fixe BD : " + str(F + S1),
                       text_color="#808080")
    print(F + S1)


# ------------------------------------------------------------------------------------------

def IEEEFB(F, p):
    if p == '32':
        manlen = 23
        explen = 8
    else:
        manlen = 52
        explen = 11
    if F < 0:
        sign = '1'
        F = -F
    else:
        sign = '0'
    Results = '' + sign
    D = int(F)
    F = F - D
    bin1 = convert(10, 2, str(D))
    bin2 = ''
    i = 0
    while F > 0 and i < 20:
        F *= 2
        bin2 += str(int(F))
        if F >= 1:
            F -= 1
    if len(bin1) != 1 and bin1[0] != '0':
        exp = len(bin1) - 1 + 127
    else:
        exp = 127 - bin2.index('1') - 1
    print('exp : ' + str(exp))
    bin3 = convert(10, 2, str(exp))
    for i in range(len(bin3), explen):
        Results += '0'
    Results += bin3
    print("bin3 : " + Results + " " + str(len(bin3)))
    man1 = bin1 + bin2
    man = man1[man1.index('1') + 1:]
    Results += man
    for i in range(len(Results), 1 + manlen + explen):
        Results += '0'
    print(man)
    print(Results)
    Results3.configure(text="En utilisant la methode IEEE 754 DB : " + Results,
                       text_color="#808080")


# ------------------------------------------------------------------------------------------

def IEEEBF(X, p):
    if p == '32':
        explen = 8
    else:
        explen = 11

    if X[0] == '1':
        Resultats = -1
        sign = -1
    else:
        Resultats = 1
        sign = 1

    X = X[1::]
    bin1 = X[:explen:]
    exp = int(bin1, 2) - 127
    X = X[explen - 1:]
    if exp < 0:
        X = X.replace('0', '1', 1)
    X = X[::-1]
    X = X[X.find('1'):][::-1]

    if exp < 0:
        bin2 = ''
        bin2 += '0' * (-exp - 1)
        bin2 += X[exp + 1:exp + len(X) + 1]
        bin3 = '0'
    else:
        bin3 = X[:exp + 1]
        bin2 = X[exp + 1:exp + len(X) + 1]

    Resultats = Resultats * int(bin3, 2)
    S = 0
    bin2 = bin2[::-1]
    for i in range(len(bin2)):
        if bin2[i] == '1':
            S += 1
        S = S / 2

    Resultats += sign * S

    Results3.configure(text="En utilisant la methode IEEE 754 BD : " + str(Resultats),
                       text_color="#808080")


ui_dark = True
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("800x450")
root.title("Projet AO")
root.resizable(False, False)

# Create the navigation bar
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=40)

root.columnconfigure(0, weight=4)
root.columnconfigure(1, weight=1)

navBar = ctk.CTkFrame(root)
navBar.grid(row=0, column=0, columnspan=2, sticky="nswe")

font_nav = ctk.CTkFont(family='terminal', size=15)

# Create navigation buttons
nav1 = ctk.CTkButton(navBar, text="project1", corner_radius=3, font=font_nav, state="disabled",
                     command=navigate_to_project1, height=35)
nav2 = ctk.CTkButton(navBar, text="project2", corner_radius=3, font=font_nav, command=navigate_to_project2, height=35)
nav3 = ctk.CTkButton(navBar, text="project3", corner_radius=3, font=font_nav, command=navigate_to_project3, height=35)

nav1.pack(side="left", fill="both", expand="true")
nav2.pack(side="left", fill="both", expand="true")
nav3.pack(side="left", fill="both", expand="true")

# Create the main frame
main_frame = ctk.CTkFrame(root)
main_frame.grid(row=1, column=0, sticky="nswe", pady=6, padx=(6, 3))

# Create the option frame
optionFrame = ctk.CTkFrame(root)
optionFrame.grid(row=1, column=1, sticky="nswe", pady=6, padx=(3, 6))
ctk.CTkLabel(optionFrame, text="Options", font=("classic", 20), pady=15).pack(fill="x")

#  Create frame1
# ---------------

frame1 = ctk.CTkFrame(main_frame)
frame1.pack(expand="true", fill="both")
option1 = ctk.CTkFrame(optionFrame)
option1.pack(expand="true", fill="both")
#  Create frame2
# ---------------

frame2 = ctk.CTkFrame(main_frame)
option2 = ctk.CTkFrame(optionFrame)

#  Create frame3
# ---------------
#
frame3 = ctk.CTkFrame(main_frame)
option3 = ctk.CTkFrame(optionFrame)

# frame1 content
# --------------
# define grid
frame1.rowconfigure(0, weight=1)
frame1.rowconfigure(1, weight=1)
frame1.rowconfigure(2, weight=2)
frame1.rowconfigure(3, weight=2)
frame1.rowconfigure(4, weight=2)
frame1.rowconfigure(5, weight=2)

frame1.columnconfigure(0, weight=2)
frame1.columnconfigure(1, weight=1)
frame1.columnconfigure(2, weight=2)

Arrow1 = ctk.CTkLabel(frame1, text="→", font=("Arial", 30))
Title1 = ctk.CTkLabel(frame1, text="Project1 : Conversion des nombres", font=("Arial", 25, "bold"), pady=20)
Description1 = ctk.CTkLabel(frame1,
                            text="Un programme permettant de convertir un nombre d'une base A vers une base B\n"
                                 "(A et B compris entre 2 et 16).",
                            font=("classic", 13))
valueA = ctk.CTkEntry(frame1, placeholder_text="base A...")
valueB = ctk.CTkEntry(frame1, placeholder_text="base B...")
V = ctk.CTkEntry(frame1, placeholder_text="valeur a convertir...")
Button1 = ctk.CTkButton(frame1, text="convertir", command=lambda: convert(valueA.get(), valueB.get(), V.get()))
results1 = ctk.CTkLabel(frame1, text="--results--", font=("classic", 15))

Title1.grid(row=0, column=0, columnspan=4)
Description1.grid(row=1, column=0, columnspan=4)
valueA.grid(row=2, column=0, sticky="ew", padx=20)
Arrow1.grid(row=2, column=1)
valueB.grid(row=2, column=2, sticky="ew", padx=20)
V.grid(row=3, column=1)
Button1.grid(row=4, column=1)
results1.grid(row=5, column=0, columnspan=3, padx=10, pady=5)

# options
option1.rowconfigure(0, weight=1)
option1.rowconfigure(1, weight=1)
option1.rowconfigure(2, weight=2)
option1.rowconfigure(3, weight=2)
option1.rowconfigure(4, weight=2)
option1.rowconfigure(5, weight=2)

option1.columnconfigure(0, weight=1)

light_mode1 = ctk.CTkCheckBox(option1, text="Light mode", command=switch_app)

light_mode1.grid(row=0)

# frame2 content
# --------------
# define grid
frame2.rowconfigure(0, weight=1)
frame2.rowconfigure(1, weight=1)
frame2.rowconfigure(2, weight=2)
frame2.rowconfigure(3, weight=2)
frame2.rowconfigure(4, weight=2)
frame2.rowconfigure(5, weight=2)

frame2.columnconfigure(0, weight=2)
frame2.columnconfigure(1, weight=2)
frame2.columnconfigure(2, weight=1)

Title2 = ctk.CTkLabel(frame2, text="Project2 : Représentation des entiers signés", font=("Arial", 25, "bold"), pady=20)
Description2 = ctk.CTkLabel(frame2,
                            text="Un programme permettant de représenter les entiers signés en utilisant les 3 méthodes :\n"
                                 "VS, CA1, CA2. ",
                            font=("classic", 13))
Entry2 = ctk.CTkEntry(frame2, placeholder_text="donner un entier...")
Button2 = ctk.CTkButton(frame2, text="convertir", command=lambda: proj21(Entry2.get(), methode.get(), bit.get()))
Results2 = ctk.CTkLabel(frame2, text="--results--", font=("classic", 15))

Title2.grid(row=0, column=0, columnspan=3)
Description2.grid(row=1, column=0, columnspan=3)
Entry2.grid(row=3, column=0, columnspan=2, padx=15, sticky="ewn")
Button2.grid(row=3, column=2, columnspan=1, sticky="n")
Results2.grid(row=4, column=0, columnspan=3)

# Options 2:
# ----------
methode = tk.StringVar()
methode.set("NULL")

option2.rowconfigure(0, weight=1)
option2.rowconfigure(1, weight=1)
option2.rowconfigure(2, weight=1)
option2.rowconfigure(3, weight=1)
option2.rowconfigure(4, weight=1)
option2.rowconfigure(5, weight=1)
option2.rowconfigure(6, weight=1)
option2.rowconfigure(7, weight=1)
option2.rowconfigure(8, weight=1)
option2.rowconfigure(9, weight=1)
option2.rowconfigure(10, weight=1)

option2.columnconfigure(0, weight=1)

choice = ctk.StringVar(value="int → bin")
bit = ctk.StringVar(value="AUTO")
light_mode2 = ctk.CTkCheckBox(option2, text="Light mode", command=switch_app)
radio1 = ctk.CTkRadioButton(option2, text="VS", variable=methode, value="VS")
radio2 = ctk.CTkRadioButton(option2, text="Ca1", variable=methode, value="CA1")
radio3 = ctk.CTkRadioButton(option2, text="Ca2", variable=methode, value="CA2")
DB_BD1 = ctk.CTkOptionMenu(option2,
                           values=["int → bin", "bin → int"],
                           width=100,
                           variable=choice,
                           command=DBorBD1
                           )

nbDeBit = ctk.CTkOptionMenu(option2,
                            values=["AUTO", "4", "8", "16"],
                            width=100,
                            variable=bit,
                            )

light_mode2.grid(row=0)
DB_BD1.grid(row=1)
nbDeBit.grid(row=2)
radio1.grid(row=3)
radio2.grid(row=4)
radio3.grid(row=5)

# frame 3 content
# ---------------

frame3.rowconfigure(0, weight=1)
frame3.rowconfigure(1, weight=1)
frame3.rowconfigure(2, weight=2)
frame3.rowconfigure(3, weight=2)
frame3.rowconfigure(4, weight=2)
frame3.rowconfigure(5, weight=2)

frame3.columnconfigure(0, weight=3)
frame3.columnconfigure(1, weight=3)
frame3.columnconfigure(2, weight=1)

Title3 = ctk.CTkLabel(frame3, text="Project3 : Représentation des nombres réels", font=("Arial", 25, "bold"), pady=20)
Description3 = ctk.CTkLabel(frame3,
                            text="Un programme permettant de représenter par le codage IEEE 754 les nombres à virgule\n"
                                 " fixe et virgule flottante.",
                            font=("classic", 13))
Entry3 = ctk.CTkEntry(frame3, placeholder_text="donner un entier...")
Button3 = ctk.CTkButton(frame3, text="convertir", command=lambda: fixeFB(float(Entry3.get())))
Results3 = ctk.CTkLabel(frame3, text="--results--", font=("classic", 15))

Title3.grid(row=0, column=0, columnspan=3)
Description3.grid(row=1, column=0, columnspan=3)
Entry3.grid(row=3, column=0, columnspan=2, padx=15, sticky="ewn")
Button3.grid(row=3, column=2, columnspan=1, sticky="n")
Results3.grid(row=4, column=0, columnspan=3)

# Options 3:
# ----------

option3.rowconfigure(0, weight=1)
option3.rowconfigure(1, weight=1)
option3.rowconfigure(2, weight=1)
option3.rowconfigure(3, weight=1)
option3.rowconfigure(4, weight=1)
option3.rowconfigure(5, weight=1)
option3.rowconfigure(6, weight=1)
option3.rowconfigure(7, weight=1)
option3.rowconfigure(8, weight=1)
option3.rowconfigure(9, weight=1)
option3.rowconfigure(10, weight=1)

option3.columnconfigure(0, weight=1)

light_mode3 = ctk.CTkCheckBox(option3, text="Light mode", command=switch_app)
choice1 = ctk.StringVar(value="int → bin")
DB_BD2 = ctk.CTkOptionMenu(option3,
                           values=["int → bin", "bin → int"],
                           width=100,
                           variable=choice1,
                           command=DBorBD2
                           )
choice2 = ctk.StringVar(value="Fixe")
Float_Fix = ctk.CTkOptionMenu(option3,
                              values=["Fixe", "IEEE 754"],
                              width=100,
                              variable=choice2,
                              command=DBorBD2
                              )

light_mode3.grid(row=0, column=0)
DB_BD2.grid(row=1, column=0)
Float_Fix.grid(row=2, column=0)

root.mainloop()
