# 🪄 Watermark Wizard

**Author**: Anvith N (2025A7PS0916H)  
A command-line tool to batch apply text or logo watermarks to images using Python and Pillow.  

---

## ✨ Features
- Batch processing of `.jpg` and `.png` images
- Supports **text watermark** or **logo watermark**
- Adjustable **opacity** (0–255)
- Multiple placement options:
  - `top-left`
  - `top-right`
  - `bottom-left`
  - `bottom-right`
  - `center`
- Automatically creates the output folder if it doesn’t exist

---

## 🛠️ Installation

### 1. Clone this repository

git clone https://github.com/<your-username>/watermark-wizard.git
cd watermark-wizard
2. Create a virtual environment (recommended)
bash
Copy code
python3 -m venv venv
source venv/bin/activate   # Fedora/Linux/Mac
venv\Scripts\activate      # Windows

3. Install dependencies

pip install -r requirements.txt
▶️ Usage
General Syntax
bash
Copy code
python watermark_wizard.py <input_folder> <output_folder> [options]
Options
--text "<string>" → watermark text (default: "Watermark")

--position <pos> → watermark position (top-left, top-right, bottom-left, bottom-right, center)
(default: bottom-right)

--opacity <0-255> → transparency level (default: 128)

--logo <logo.png> → path to logo image (overrides text watermark)

Examples
1. Apply a text watermark

python watermark_wizard.py input_images output_images --text "Confidential" --position bottom-right --opacity 180

2. Apply a logo watermark

python watermark_wizard.py input_images output_images --logo logo.png --position center --opacity 200

3. Use default settings

python watermark_wizard.py input_images output_images
This will apply the default "Watermark" text in the bottom-right corner at 50% opacity.

📂 Project Structure

watermark-wizard/
├── watermark_wizard.py   # Main script
├── requirements.txt      # Python dependencies
├── README.md             # Documentation
└── input_images/         # Example input folder (user-provided)

📦 Dependencies
Python 3.9+
Pillow (pip install pillow)
All dependencies are listed in requirements.txt.

🧑‍💻 Development Notes
Code follows PEP 8 guidelines.

Meaningful Git commits are encouraged, e.g.:

feat: implement text watermark support

feat: add logo watermark option

fix: correct opacity scaling

Tested on Fedora Linux (Python 3.12).

📜 License
This project is for academic use only. Please do not plagiarize.
