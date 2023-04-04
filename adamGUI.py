import tkinter
import tkinter.messagebox
import customtkinter
#import adamTestFile
#import adamV2
#import tkthread; tkthread.patch()
import sys
import time
import threading

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        self.number = 0
        super().__init__()

        # configure window
        self.title("ADAM")
        self.geometry(f"{1920}x{1080}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="ADAM NLP", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.startButton = customtkinter.CTkButton(self.sidebar_frame, command=self.startButtonEvent)
        self.startButton.grid(row=1, column=0, padx=20, pady=10)
        self.endButton = customtkinter.CTkButton(self.sidebar_frame, command=self.endProgramEvent)
        self.endButton.grid(row=2, column=0, padx=20, pady=10)
        self.adminButton = customtkinter.CTkButton(self.sidebar_frame, command=self.adminButtonEvent)
        self.adminButton.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Type me information here")
        self.entry.grid(row=3, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(text="Submit", master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.entryRequest)
        self.main_button_1.grid(row=3, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.grid(row=0, column=1, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")


        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1,columnspan=2, padx=(20, 20), pady=(10, 10), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, columnspan=2, padx=(20, 20), pady=(10, 10), sticky="ew")

        # set default values
        self.startButton.configure(state="enabled", text="START")
        self.endButton.configure(state="disabled", text="TERMINATE")
        self.adminButton.configure(state="enabled", text="ADMIN ACCESS")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()

    def insert_slow(self, str, t):
        self.textbox.insert("0.0", "\n")
        for letter in str:
            self.textbox.insert("0.0", letter)
            self.update()
            time.sleep(t)
        self.textbox.insert("0.0", "\n")


    '''def handleInsertSlow(self):
        startThread = self.insert_slow("TEST")
        startThread.start()
        self.monitor(startThread)'''

    '''def monitor(self, thread):
        if thread.is_alive():
            # check the thread every 100ms
            self.after(100, lambda: self.monitor(thread))
        else:
            self.textbox.insert'''

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="PASSWORD: ", title="ADMIN ACCESS")
        adminPassword = dialog.get_input()
        if adminPassword == "Password":
            str = "".join(reversed("ADMIN ACCESS GRANTED"))
            self.insertText(str, 0.02)
        else:
            str = "".join(reversed("ADMIN ACCESS DENIED"))
            self.insertText(str, 0.02)
            self.adminButton.configure(state="disabled")

    def insertText(self, str, t2):
        print(str)
        self.tspacer(str)
        self.insert_slow(str, t2)
        self.bspacer(str)
    def reverse(str):
        i = len(str) - 1
        out = ""
        while i>-1:
            out+= str[i-1, i]
            i -= 1;
    def tspacer(self, str):
        self.textbox.insert("0.0", "-"*(len(str)*2) + "\n\n")
    def bspacer(self, str):
        self.textbox.insert("0.0", "\n\n" + "-"*(len(str)*2))
    
    def entryRequest(self):
        self.textbox.insert("0.0", "ENTRY RECIEVED \n")
        self.textbox.insert("0.0", self.entry.get() + "\n")
        self.progressbar_1.stop()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def printText(self, statement):
        self.textbox.insert("0.0", statement)

    def startButtonEvent(self):
        self.startButton.configure(state="disabled")
        self.endButton.configure(state="enabled")
        str = "".join(reversed("PROGRAM STARTED"))
        self.insertText(str, 0.02)
        self.number += 1
        self.update()
        print(self.number)
        #adamV2.AdamStart()

    def endProgramEvent(self):
        print("TERMINATE BUTTON CLICKED")
        self.endButton.configure(state="disabled")
        self.startButton.configure(state="enabled")
        str = "".join(reversed("PROGRAM TERMINATED"))
        self.insertText(str, 0.02)
        #adamV2.exit()

    def adminButtonEvent(self):
        print("ADMIN BUTTON PRESSED")
        self.open_input_dialog_event()

