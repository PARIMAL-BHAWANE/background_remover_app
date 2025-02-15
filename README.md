# Background Remover Application

This project is a background remover application that utilizes AI to remove backgrounds from images. It provides a user-friendly GUI built with tkinter and customtkinter, allowing users to easily select images or folders and process them to remove backgrounds.

## Features

- Select multiple images or an entire folder for background removal.
- High-quality background removal using the `rembg` library.
- Progress tracking during the processing of images.
- Output images are saved in a dedicated folder.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/PARIMAL-BHAWANE/background_remover_app
   cd background_remover_app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/remove_bg_gui.py
   ```

2. Use the "Select Files" button to choose individual images or the "Select Folder" button to choose a folder containing images.

3. Click the "Remove Background" button to start the background removal process.

4. The processed images will be saved in an `output_images` folder within the selected directory.

## Dependencies

- rembg
- tkinter
- customtkinter
- opencv-python
- Pillow

## License

This project is licensed under the MIT License. See the LICENSE file for more details.