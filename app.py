import tkinter as tk
import customtkinter as ctk

from PIL import ImageTk
from authtoken import auth_token

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

app = tk.Tk()
app.geometry("532x662")
app.title("Text2Image")
ctk.set_appearance_mode("dark")

prompt = ctk.CTkEntry(height=40, width=512, text_font=("Arial", 20), text_color="black", fg_color="white")
prompt.place(x=10, y=10)


app.mainloop()