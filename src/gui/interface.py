from tkinter import *
import sys
import os.path
import tkinter.filedialog
from algorithms.data import load_from_xls
from algorithms.graph import (
    inbreed_calculate,
    relation_calculate,
    generate_data,
    draw_graph,
)

textMain = "\n• First, load the pedigree file in .xlsx or .xls format. You can check how your file should look like by clicking in the question mark.\n• You can also check how this calculator works using sample data by clicking 'Load sample data'.\n• To calculate the coefficient of inbreeding, select one person on the list.\n• To calculate the coefficient of relationship, select two people on the list.\n• Finally click the appropriate button.\n• After choosing data, it is possible to draw a family tree.\n\n"
subjects = []


def parse_path(name):
    if os.name == "nt":
        relative_path = "assets\\" + name
    else:
        relative_path = "assets/" + name
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def open_file(window, listbox, txt_field):
    listbox.delete("0", "end")
    subjects[:] = []
    filename = tkinter.filedialog.askopenfilename(
        title="Select file",
        filetypes=(
            ("xlsx files", "*.xlsx"),
            ("xls files", "*.xls"),
            ("all files", "*.*"),
        ),
    )
    try:
        load_from_xls(subjects, filename)
        txt_field.configure(foreground="black", text="")
    except Exception as e:
        txt_field.configure(
            foreground="red", text="Error while opening file! Please try again."
        )
    for i in subjects:
        listbox.insert(END, i.name)
    generate_data(subjects)


def show_inbreed(txt_field, idx):
    if len(idx) != 1:
        txt_field.configure(
            foreground="red",
            text=" Error: Select only one person to count its coefficient of inbreeding!",
        )
        return
    results = inbreed_calculate(subjects[idx[0]])
    txt = (
        "\n• Coefficient of inbreeding for %s: %f.\n• This means that about %.2f%% of the total number of %s loci are pairs of genes identical by origin."
        % (
            subjects[idx[0]].name,
            round(results, 6),
            round(results * 100, 2),
            subjects[idx[0]].name,
        )
    )
    txt_field.configure(foreground="black", text=txt)


def show_relation(txt_field, idx):
    if len(idx) != 2:
        txt_field.configure(
            foreground="red",
            text="Error: Select two person to count their coefficient of relationship!",
        )
        return
    results = relation_calculate(subjects[idx[0]], subjects[idx[1]])
    txt = (
        "\n• Coefficient of relationship for %s and %s: %f.\n• The probability that the allele at the %s locus is identical to the %s allele at the same locus is %.2f%%. "
        % (
            subjects[idx[0]].name,
            subjects[idx[1]].name,
            results,
            subjects[idx[0]].name,
            subjects[idx[1]].name,
            results * 100,
        )
    )
    txt_field.configure(foreground="black", text=txt)


def create_hint_window():
    hint_window = Toplevel()
    canvas2 = Canvas(hint_window, width=618, height=406)
    img = PhotoImage(file=parse_path("example.png"))
    infoTxt = "Your .xlsx / .xls file should look like this:"
    info = Message(
        hint_window, text=infoTxt, anchor=W, width=400, font=("Helvetica", 16)
    )

    infoTxt2 = "Name, birth year and death year are required. Names should be unique, and for the same person occuring in column mother or father names should be exactly the same (only trailing and leading spaces are deleted, names are case sensitive)."
    info2 = Message(
        hint_window, text=infoTxt2, anchor=W, width=600, font=("Helvetica", 16)
    )

    close_button = Button(
        hint_window,
        text="Close window",
        width=20,
        command=lambda: hint_window.destroy(),
    )

    info.pack()
    canvas2.pack()
    canvas2.create_image(0, 0, image=img, anchor=NW)
    canvas2.image = img
    info2.pack()
    close_button.pack()


def open_sample_data(window, listbox, txt_field):
    listbox.delete("0", "end")
    subjects[:] = []
    try:
        load_from_xls(subjects, parse_path("sample_data.xlsx"))
        txt_field.configure(foreground="black", text="")
    except Exception as e:
        txt_field.configure(
            foreground="red", text="Error while opening file! Please try again."
        )
    for i in subjects:
        listbox.insert(END, i.name)
    generate_data(subjects)


def create_window():
    window = Tk()
    window.title("IRcoeff Calc")
    window.geometry("700x700")

    canvas = Canvas(window, width=500, height=80)
    canvas.pack()
    img = PhotoImage(file=parse_path("logo.png"))
    canvas.create_image(20, 20, anchor=NW, image=img)

    scrollbar = Scrollbar(window)
    scrollbar.pack(side=LEFT, fill=Y)
    listbox = Listbox(
        window, yscrollcommand=scrollbar.set, width=30, selectmode="multiple"
    )

    listbox.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=listbox.yview)

    mainText = Message(window, text=textMain, anchor=W, width=400)
    mainText.pack()

    resultInbred = Message(window, text="", anchor=W, width=400)
    resultRel = Message(window, text="", anchor=W, width=400)
    inbred_button = Button(
        window,
        text="Coefficient of inbreeding",
        width=20,
        command=lambda: show_inbreed(resultInbred, listbox.curselection()),
    )
    relation_button = Button(
        window,
        text="Coefficient of relationship",
        width=20,
        command=lambda: show_relation(resultRel, listbox.curselection()),
    )
    draw_button = Button(
        window, text="Draw a family tree", width=20, command=lambda: draw_graph()
    )

    frame = Frame(window, width=20)

    load_button = Button(
        frame,
        text="Load file",
        width=16,
        command=lambda: open_file(window, listbox, resultInbred),
    )
    question_mark = PhotoImage(file=parse_path("question.png")).subsample(5, 5)
    question_icon = Button(
        frame, image=question_mark, command=lambda: create_hint_window()
    )

    sample_data_button = Button(
        window,
        text="Load sample data",
        width=20,
        command=lambda: open_sample_data(window, listbox, resultInbred),
    )
    inbred_button.pack()
    relation_button.pack()
    draw_button.pack()
    load_button.pack(side="left")
    sample_data_button.pack()
    frame.pack()
    resultInbred.pack()
    resultRel.pack()
    label = Label(window, text="Klaudia Faltyn, 2020", anchor=S)
    label.pack(side=BOTTOM, fill=X)
    question_icon.pack(side="right")
    window.mainloop()
