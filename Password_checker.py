import re
import tkinter as tk
from tkinter import ttk

class GreenMatchPasswordChecker:
    def __init__(self, root):
        self.root = root
        self.root.title("Orange Vault - Password Analyzer")
        self.root.geometry("480x520")
        self.root.configure(bg="#141414") 
        

        self.bg_dark = "#141414"
        self.bg_card = "#1F1F1F"
        self.orange_accent = "#FF5500" 
        self.green_success = "#00CC66"      
        self.text_white = "#FFFFFF"
        self.text_dim = "#757575"
        
        self.hide_password = True
        
        self.build_ui()

    def build_ui(self):

        header_frame = tk.Frame(self.root, bg=self.bg_dark)
        header_frame.pack(pady=(30, 20), fill="x", padx=40)
        
        title = tk.Label(
            header_frame, text="SECURITY VAULT PASSWORD CHECKER", font=("Courier New", 20, "bold"),
            fg=self.orange_accent, bg=self.bg_dark
        )
        title.pack(anchor="w")
        
        subtitle = tk.Label(
            header_frame, text="Real-time Password strength assessment.",
            font=("Helvetica", 9), fg=self.text_dim, bg=self.bg_dark
        )
        subtitle.pack(anchor="w", pady=(2, 0))

        card = tk.Frame(self.root, bg=self.bg_card, bd=0)
        card.pack(fill="x", padx=40, pady=10, ipady=15)

        input_header = tk.Frame(card, bg=self.bg_card)
        input_header.pack(fill="x", padx=20, pady=(15, 5))

        tk.Label(
            input_header, text="Target Password", font=("Helvetica", 10, "bold"),
            fg=self.text_white, bg=self.bg_card
        ).pack(side="left")


        input_row = tk.Frame(card, bg=self.bg_card)
        input_row.pack(fill="x", padx=20, pady=5)

        self.pass_var = tk.StringVar()
        self.pass_var.trace_add("write", self.analyze_password)
        
        self.entry = tk.Entry(
            input_row, textvariable=self.pass_var, show="•",
            font=("Consolas", 13), bg="#2B2B2B", fg=self.text_white,
            bd=0, insertbackground=self.orange_accent, highlightthickness=1,
            highlightbackground="#3A3A3A", highlightcolor=self.orange_accent
        )
        self.entry.pack(side="left", fill="x", expand=True, ipady=6)

  
        self.view_btn = tk.Button(
            input_row, text="👁", font=("Helvetica", 12), bg="#2B2B2B", fg=self.text_dim,
            activebackground="#3A3A3A", activeforeground=self.orange_accent,
            bd=0, cursor="hand2", command=self.toggle_visibility, width=3
        )
        self.view_btn.pack(side="left", padx=(5, 0), ipady=3)


        self.meter_canvas = tk.Canvas(
            self.root, width=400, height=4, bg="#2B2B2B", bd=0, highlightthickness=0
        )
        self.meter_canvas.pack(pady=(15, 5))
        self.fill_bar = self.meter_canvas.create_rectangle(0, 0, 0, 4, fill=self.orange_accent, width=0)

        self.status_label = tk.Label(
            self.root, text="SYSTEM IDLE", font=("Helvetica", 11, "bold"),
            fg=self.text_dim, bg=self.bg_dark
        )
        self.status_label.pack(pady=5)


        self.check_frame = tk.LabelFrame(
            self.root, text=" Security Parameters ", font=("Helvetica", 9, "bold"),
            bg=self.bg_dark, fg=self.orange_accent, bd=1, relief="solid"
        )
        self.check_frame.pack(fill="both", expand=True, padx=40, pady=(15, 30), ipady=10)
        
        self.requirements = [
            {"label": "○ Contains 12+ Characters", "regex": r".{12,}"},
            {"label": "○ Contains Uppercase Letter", "regex": r"[A-Z]"},
            {"label": "○ Contains Lowercase Letter", "regex": r"[a-z]"},
            {"label": "○ Contains Numeric Digit", "regex": r"\d"},
            {"label": "○ Contains Special Character", "regex": r"[!@#$%^&*(),.?\":{}|<>]"}
        ]
        
        self.req_labels = []
        for req in self.requirements:
            lbl = tk.Label(
                self.check_frame, text=req["label"], font=("Consolas", 10),
                fg=self.text_dim, bg=self.bg_dark, anchor="w"
            )
            lbl.pack(fill="x", padx=20, pady=3)
            self.req_labels.append(lbl)

    def toggle_visibility(self):
        if self.hide_password:
            self.entry.config(show="")
            self.view_btn.config(fg=self.orange_accent, text="⚡")
            self.hide_password = False
        else:
            self.entry.config(show="•")
            self.view_btn.config(fg=self.text_dim, text="👁‍🗨")
            self.hide_password = True
    def analyze_password(self, *args):
        password = self.pass_var.get()
        
        if not password:
            self.meter_canvas.coords(self.fill_bar, 0, 0, 0, 4)
            self.status_label.config(text="SYSTEM IDLE", fg=self.text_dim)
            for lbl, req in zip(self.req_labels, self.requirements):
                lbl.config(text=req["label"].replace("●", "○"), fg=self.text_dim)
            return

        passed_rules = 0
        

        for i, req in enumerate(self.requirements):
            if re.search(req["regex"], password):
                passed_rules += 1

                self.req_labels[i].config(
                    text=req["label"].replace("○", "●"), fg=self.green_success
                )
            else:

                self.req_labels[i].config(
                    text=req["label"].replace("●", "○"), fg=self.text_dim
                )

        target_width = int((passed_rules / 5) * 400)
        self.meter_canvas.coords(self.fill_bar, 0, 0, target_width, 4)


        if passed_rules <= 2:
            self.status_label.config(text="CRITICAL SECURITY RISK", fg="#FF3333")
            self.meter_canvas.itemconfig(self.fill_bar, fill="#FF3333")
        elif passed_rules <= 4:
            self.status_label.config(text="STANDARD SECURITY", fg=self.orange_accent)
            self.meter_canvas.itemconfig(self.fill_bar, fill=self.orange_accent)
        else:
            self.status_label.config(text="ULTRA ADVANCE PASSWORD STRENGTH", fg=self.green_success)
            self.meter_canvas.itemconfig(self.fill_bar, fill=self.green_success)

if __name__ == "__main__":
    root = tk.Tk()
    app = GreenMatchPasswordChecker(root)
    root.mainloop()
