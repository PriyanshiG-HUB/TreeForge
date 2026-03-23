# 🌲 TreeForge

> **Forge your entire project structure from a simple tree diagram — instantly.**

TreeForge is a lightweight Python CLI tool that reads a folder/file tree (the kind you'd sketch in a README) and materializes it into a real project on disk — complete with starter file contents.

---

## ✨ Features

- 📋 **Paste & Go** — just paste any tree-style structure and hit Enter
- 📁 **Auto-creates folders** — nested directories handled automatically
- 📄 **Generates starter files** — `.py`, `.jsx`, `.js`, `.html`, `.css`, `.md`, `.json` all get sensible boilerplate
- 🌿 **Smart depth parsing** — correctly handles any level of nesting using `│` characters
- 🖨️ **Live progress log** — see every file and folder created in real time
- ⚡ **Zero dependencies** — pure Python standard library, no installs needed

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/treeforge.git
cd treeforge
```

### 2. Run it

```bash
python treeforge.py
```

### 3. Enter your base path

```
Enter base path (e.g. D:\Projects): D:\Projects
```

### 4. Paste your tree structure and press Enter twice

```
Paste your project structure (press ENTER twice to finish):

my-app/
├── backend/
│   ├── app.py
│   ├── models.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   └── src/
│       └── main.jsx
└── README.md
```

### ✅ Done!

```
  📂 backend/
  📄 backend/app.py
  📄 backend/models.py
  📄 backend/requirements.txt
  📂 frontend/
  📄 frontend/index.html
  📂 frontend/src/
  📄 frontend/src/main.jsx
  📄 README.md

✅ Project created successfully at:
   D:\Projects\my-app
```

---

## 📦 Starter File Contents

TreeForge doesn't create empty files — each type gets a meaningful starting point:

| Extension   | Starter Content                              |
|-------------|----------------------------------------------|
| `.py`       | `# Python file`                              |
| `.jsx`      | A named functional React component           |
| `.js`       | `// JS file`                                 |
| `.html`     | Full HTML5 boilerplate                       |
| `.css`      | `/* CSS */`                                  |
| `.md`       | `# Project` heading with placeholder text    |
| `.json`     | Empty `{}`                                   |
| `.txt`      | Empty file                                   |
| everything else | Empty file                              |

---

## 🗂️ Project Structure

```
treeforge/
└── treeforge.py      # The entire tool — single file, no deps
```

---

## 🧠 How It Works

TreeForge parses each line of your tree by counting `│` characters before the `├──` or `└──` marker to determine nesting depth. It maintains a path stack and builds the full path for each file or folder.

```
│   ├── app.py
│            ^── one │ = depth 2 (inside backend/ inside root)
```

Files are detected by the presence of a `.` in the name (e.g. `app.py`, `index.html`). Everything else is treated as a folder.

---

## 🛠️ Requirements

- Python **3.6+**
- No external packages needed

---

## 📋 Supported Tree Symbols

TreeForge works with standard tree diagram notation:

| Symbol | Meaning              |
|--------|----------------------|
| `├──`  | Item (not last)      |
| `└──`  | Item (last in group) |
| `│`    | Vertical connector   |

You can generate these from tools like the `tree` command, VS Code file tree extensions, or write them manually.

---

## 💡 Tips

- Trailing `/` on folder names is optional — TreeForge handles both `backend` and `backend/`
- Works with deeply nested structures (10+ levels)
- You can reuse the same structure multiple times — existing folders won't be overwritten, but files will be recreated

---

## 🤝 Contributing

Pull requests are welcome! If you find a tree format that TreeForge doesn't parse correctly, open an issue with the example structure.

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

<p align="center">Made with 🌲 by TreeForge</p>
