import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import cv2
import numpy as np
from rembg import remove
from PIL import Image, ImageTk

import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Modern dark mode
root = ctk.CTk()
root.title("AI Background Remover")
root.geometry("500x400")

# Function to remove background with high quality
def remove_background():
    images = file_paths.get()

    if not images:
        messagebox.showerror("Error", "Please select images or a folder!")
        return

    output_folder = os.path.join(os.path.dirname(images[0]), "output_images")
    os.makedirs(output_folder, exist_ok=True)

    progress["value"] = 0
    progress["maximum"] = len(images)

    for idx, img_path in enumerate(images):
        output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(img_path))[0] + "_no_bg.png")

        # Open image
        input_image = Image.open(img_path).convert("RGBA")

        # Remove background
        output_image = remove(
            input_image,
            alpha_matting=True,  # Enable matting for better accuracy
            alpha_matting_foreground_threshold=220,  
            alpha_matting_background_threshold=20,  
            alpha_matting_erode_size=3  
        )

        # Increase resolution (2x upscale)
        output_image = output_image.resize((input_image.width * 2, input_image.height * 2), Image.LANCZOS)

        # Convert to OpenCV format for additional enhancements
        output_np = np.array(output_image)
        output_np = cv2.cvtColor(output_np, cv2.COLOR_RGBA2BGRA)

        # Apply Gaussian Blur for smooth edges
        blurred = cv2.GaussianBlur(output_np, (3, 3), 0)

        # Save final high-quality output
        cv2.imwrite(output_path, blurred)

        progress["value"] = idx + 1
        root.update_idletasks()

    messagebox.showinfo("Success", f"✅ Background removed for {len(images)} images!\nCheck 'output_images' in the selected folder.")

# Function to select files
def select_files():
    files = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    file_paths.set(files)

# Function to select folder
def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        images = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(('png', 'jpg', 'jpeg'))]
        file_paths.set(images)

# GUI Setup
root = tk.Tk()
root.title("High-Quality Background Remover")
root.geometry("450x350")
root.resizable(False, False)

file_paths = tk.Variable()

# UI Components
tk.Label(root, text="Select Images or a Folder:", font=("Arial", 12)).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Select Files", command=select_files).pack(side=tk.LEFT, padx=10)
tk.Button(frame, text="Select Folder", command=select_folder).pack(side=tk.RIGHT, padx=10)

tk.Button(root, text="Remove Background", font=("Arial", 12), bg="green", fg="white", command=remove_background).pack(pady=20)

progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=10)

# Run GUI
root.mainloop()