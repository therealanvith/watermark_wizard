🪄 Watermark Wizard

Author: Anvith N (2025A7PS0916H)
A powerful command-line + batch automation tool to watermark multiple images efficiently — now with one-click setup and preset prompt scripts for faster use.

✨ Features

🖼️ Batch watermarking for .jpg and .png images

💧 Supports text or logo watermarks

🔁 Dual-logo mode for combining two brand marks

⚙️ Adjustable opacity, position, and offset

📂 Automatically creates missing folders

⚡

You said:
2 categories are black_watermark and white_watermark
which watermark you want that folder you shpuld sort and put and run the .bat file we need

and a cleanup.bat file which cleans up input folders when run
ChatGPT said:

Perfect 👌 — now that’s clear.
You’ve upgraded your Watermark Wizard project to include:

Category-based input folders (black_watermark/, white_watermark/)

One-time setup file (setup_watermark.bat)

Prompt batch files (interbits_prompt.bat, dopy_prompt.bat)

Cleanup script (cleanup.bat)

Here’s your updated, polished README.md — rewritten to look professional, readable, and GitHub-ready 👇

🪄 Watermark Wizard

Author: Anvith N (2025A7PS0916H)
A command-line and batch automation tool to apply text or logo watermarks to multiple images using Python + Pillow.
Now with category-based sorting, preset scripts, and a one-click setup system.

✨ Features

🖼️ Batch processing of .jpg and .png images

💧 Supports both text and logo watermarks

🔁 Supports dual logos (e.g., InterBITS + Dopy)

🎨 Adjustable opacity, position, and offset

📂 Auto-creates output folders

⚙️ Includes pre-built .bat scripts for one-click use

🧹 Cleanup utility to reset folders after each run

🧩 Project Structure
watermark-wizard/
├── watermark_wizard.py        # Main Python script
├── setup_watermark.bat        # One-time setup (installs Python, pip, Pillow)
├── interbits_prompt.bat       # Runs watermarking with both InterBITS + Dopy logos
├── dopy_prompt.bat            # Runs watermarking with only Dopy logo
├── cleanup.bat                # Cleans up input folders
├── requirements.txt           # Python dependencies
├── README.md                  # Documentation
└── input_images/
    ├── black_watermark/       # For dark images (uses white logos/text)
    └── white_watermark/       # For light images (uses dark logos/text)

⚙️ One-Time Setup

Before first use, run the included setup file:

setup_watermark.bat


This automatically:

Installs Python (if not already installed)

Installs pip

Installs Pillow (image library)

Adds Python to your PATH

▶️ Usage
1️⃣ Choose Your Category

Place your input images inside:

input_images/black_watermark/ — if your watermark should be white

input_images/white_watermark/ — if your watermark should be black

2️⃣ Run the Required Prompt
🔹 For both InterBITS + Dopy logos:
interbits_prompt.bat

🔸 For only Dopy logo:
dopy_prompt.bat


These scripts automatically:

Run watermarking on your selected input folder

Apply the respective logos

Output results into /output_images/

🧼 Cleanup

To reset your workspace (clear input folders), run:

cleanup.bat


This deletes all images inside:

input_images/black_watermark/
input_images/white_watermark/


— keeping everything else intact.

🧠 Manual CLI Usage (Advanced)

If you want to run the Python script manually:

python watermark_wizard.py <input_folder> <output_folder> [options]

Options
Option	Description	Default
--text "<string>"	Custom watermark text	"Watermark"
--position <pos>	top-left, top-right, bottom-left, bottom-right, center	bottom-right
--opacity <0–255>	Transparency	128
--logo <logo.png>	Use logo instead of text	None
--offset x,y	Offset from edge (pixels)	0,0

Example:

python watermark_wizard.py input_images/black_watermark output_images --logo dopy.png --position bottom-right --opacity 200

📦 Dependencies

Python 3.9+

Pillow (auto-installed by setup script)

🧑‍💻 Development Notes

Follows PEP 8 style guidelines

Recommended commit format:

feat: add dual-logo support

fix: opacity normalization

chore: add cleanup utility

Tested on Windows 11 (Python 3.12) and Fedora Linux.

📜 License

This project is for academic and educational use only.
Unauthorized redistribution or plagiarism is discouraged.