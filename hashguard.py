"""HashGuard: offline file integrity checker for Windows."""
from __future__ import annotations
import hashlib
import re
import threading
import tkinter as tk
from pathlib import Path
from tkinter import ttk,filedialog,messagebox

VERSION="1.0.0"

def sha256_file(filename, chunk_size=1024*1024):
    h=hashlib.sha256()
    with open(filename,"rb") as f:
        while True:
            part=f.read(chunk_size)
            if not part:break
            h.update(part)
    return h.hexdigest()

def verify_digest(actual,expected):
    expected=expected.strip().lower()
    if not re.fullmatch("[0-9a-f]{64}",expected):
        raise ValueError("Expected SHA-256 must have 64 hexadecimal characters.")
    return actual.lower()==expected

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("HashGuard "+VERSION)
        self.geometry("760x290")
        self.path=tk.StringVar()
        self.digest=tk.StringVar()
        self.expected=tk.StringVar()
        self.status=tk.StringVar(value="All file hashes are computed offline.")
        pane=ttk.Frame(self,padding=15);pane.pack(fill="both",expand=True)
        def row(n,label,var,action,callback):
            ttk.Label(pane,text=label).grid(row=n,column=0,sticky="w",pady=12)
            ttk.Entry(pane,textvariable=var).grid(row=n,column=1,sticky="ew")
            ttk.Button(pane,text=action,command=callback).grid(row=n,column=2,padx=6)
        row(0,"File",self.path,"Browse",self.browse)
        row(1,"SHA-256",self.digest,"Copy",self.copy)
        row(2,"Expected",self.expected,"Verify",self.verify)
        ttk.Button(pane,text="Calculate SHA-256",command=self.calculate).grid(row=3,column=1,sticky="w",pady=8)
        ttk.Label(pane,textvariable=self.status).grid(row=4,column=0,columnspan=3,sticky="w")
        pane.columnconfigure(1,weight=1)
    def browse(self):
        path=filedialog.askopenfilename()
        if path:self.path.set(path);self.digest.set("")
    def calculate(self):
        path=Path(self.path.get())
        if not path.is_file():messagebox.showerror("HashGuard","Select an existing file.");return
        self.status.set("Working...")
        def worker():
            try:
                result=sha256_file(path)
                self.after(0,lambda:self.finish(result))
            except Exception as exc:
                self.after(0,lambda s=str(exc):messagebox.showerror("HashGuard",s))
        threading.Thread(target=worker,daemon=True).start()
    def finish(self,digest):
        self.digest.set(digest);self.status.set("Hash ready.")
    def verify(self):
        if not self.digest.get():messagebox.showinfo("HashGuard","Calculate a hash first.");return
        try:
            good=verify_digest(self.digest.get(),self.expected.get())
            self.status.set("MATCH: identical SHA-256." if good else "MISMATCH: file differs!")
        except ValueError as exc:messagebox.showerror("HashGuard",str(exc))
    def copy(self):
        if self.digest.get():
            self.clipboard_clear();self.clipboard_append(self.digest.get())
            self.status.set("Copied.")

if __name__=="__main__":App().mainloop()
