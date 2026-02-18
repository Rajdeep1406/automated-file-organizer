# 📁 Automated File Organizer

### 🧠 Smart Python Automation for Clean & Structured Directories

Transform messy folders into perfectly organized storage — automatically ⚡

A powerful **CLI-based Python automation tool** that scans, classifies, and organizes files into categorized folders using clean architecture and modular design.

---

## 🚀 Project Preview

✨ From Chaos → To Structure in Seconds

```
Downloads/
│
├── Images/
├── Documents/
├── Videos/
├── Music/
└── Others/
```

No manual sorting. No wasted time. Just automation magic 🪄

---

## 🧠 Architecture Overview

This project follows a **Layered + Functional Architecture**:

```
👤 User (Terminal)
        ↓
🎮 Main Controller (Entry Point)
        ↓
🧠 File System Logic (Core Modules)
        ↓
💻 OS / File System
```

### 🔄 Execution Flow

```
Scan → Classify → Create Folders → Move Files → Report
```

Clean. Modular. Scalable.

---

## ✨ Features

🌟 Smart file categorization
📂 Automatic folder creation
🔍 Extension-based detection
📦 Safe file moving
🧠 Edge case handling
♻️ Duplicate file renaming
🛡️ Permission-safe execution
⚡ Fast & lightweight

---

## 🏗️ Repository Structure

```
automated-file-organizer/
│
├── organizer/
│   ├── __init__.py
│   ├── config.py      ⚙️ Extension mapping
│   ├── scanner.py     📂 Directory reader
│   ├── sorter.py      🧠 Category logic
│   ├── mover.py       📦 File mover
│
├── main.py            🎮 Entry point
├── requirements.txt  📜 Dependencies
├── README.md         📖 Documentation
└── .gitignore        🚫 Ignored files
```

Structured like production tools — not beginner scripts 💼

---

## ⚙️ How It Works

1️⃣ User runs script via CLI
2️⃣ Directory gets scanned
3️⃣ File extensions extracted
4️⃣ Categories determined
5️⃣ Folders created (if missing)
6️⃣ Files moved safely
7️⃣ Status logs displayed

---

## 🧩 Core Modules Explained

### 🎮 `main.py` — Entry Point

Responsibilities:

* Accept folder path
* Control workflow
* Handle errors
* Display logs

---

### ⚙️ `config.py` — Configuration Hub

```python
FILE_CATEGORIES = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
}
```

✅ Easy to extend
✅ No hardcoding
✅ Config-driven design

---

### 📂 `scanner.py` — Directory Scanner

Functions:

* Reads directory
* Filters files only
* Ignores subfolders

Concepts used:

* `os.listdir()`
* `os.path.isfile()`

---

### 🧠 `sorter.py` — Decision Engine

Logic:

```
Extension → Category → Fallback (Others)
```

Pure business logic module.

---

### 📦 `mover.py` — File Operations

Handles:

* Folder creation
* Duplicate filenames
* Safe file moving

Key APIs:

* `os.makedirs(exist_ok=True)`
* `shutil.move()`

---

## ⚠️ Edge Case Handling

Real utility ≠ toy script 💪

### ✔ Ignore Folders

```python
if not os.path.isfile(path):
    continue
```

---

### ✔ Duplicate Files

```
file.txt → file_1.txt
```

No overwriting ❌

---

### ✔ Unknown Extensions

Moved to:

```
Others/
```

---

### ✔ Permission Errors

Handled via `try-except` 🛡️

---

## 🧪 How To Run

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/automated-file-organizer.git
cd automated-file-organizer
```

---

### 2️⃣ Execute Script

```bash
python main.py /path/to/folder
```

Example:

```bash
python main.py C:/Users/Manas/Downloads
```

---

## 🖥️ Sample Output

```
📂 Scanning directory...
🔍 Found 42 files

🧠 Organizing...

✔ photo.jpg → Images/
✔ resume.pdf → Documents/
✔ song.mp3 → Music/

✅ Completed Successfully
```

---

## 🚀 Future Enhancements

🔮 GUI Version (Tkinter / PyQt)
📅 Date-wise sorting
📏 File size categorization
🕒 Auto scheduler (Cron / Task Scheduler)
📝 Logging system
🌐 Cloud sync support

---

## 📚 Learning Outcomes

> This project strengthened my understanding of Python scripting, OS-level file handling, modular architecture, and automation workflows — building a strong foundation for backend frameworks like Django.

---

## 🛠️ Tech Stack

🐍 Python 3.x
📁 OS Module
📦 Shutil Module
💻 CLI Interface

---

## 🤝 Contributing

Contributions are welcome 🙌
Open an issue or submit a pull request.

---

## 📜 License

Licensed under the **MIT License** 📄

---

## ⭐ Support

If you found this useful:

⭐ Star the repo
🍴 Fork it
📢 Share with others

---

### 💡 Built with automation mindset + clean code architecture
