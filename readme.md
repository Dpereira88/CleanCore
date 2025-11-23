# CleanCore

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![CustomTkinter](https://img.shields.io/badge/customtkinter-5.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

**CleanCore** is a powerful text parsing and extraction tool with a modern dark-mode GUI. Parse large text dumps, highlight specific patterns, and extract clean values with ease.

Created by **@Nao_funciona_** • November 2025

---

## ✨ Features

- 🎨 **Modern Dark UI** - Clean, professional interface with customtkinter
- 📝 **Dual-Panel Layout** - Config editor + text dump area with live line numbers
- 🔍 **Smart Pattern Matching** - Parse text by line number and partial string matching
- ✂️ **Prefix/Suffix Trimming** - Automatically clean extracted values
- 💾 **Multi-Config Support** - Save and switch between multiple parsing configurations
- 📋 **One-Click Extraction** - Copy unique values to clipboard instantly
- 🎯 **Syntax Validation** - Real-time error highlighting in config editor
- 🔤 **Adjustable Font Size** - A+/A- controls for comfortable viewing
- 👤 **Multi-User Support** - Per-user settings automatically saved
- 💪 **Motivational Messages** - Random inspiring phrases on startup
- ⌨️ **Keyboard Shortcuts** - Ctrl+Z/Ctrl+Y undo/redo support

---

## 🚀 Quick Start

### Prerequisites

```bash
pip install customtkinter
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cleancore.git
cd cleancore
```

2. Run the application:
```bash
python cleancore.py
```

---

## 📖 How It Works

### 1. **Config Editor** (Left Panel)

Define parsing rules with this syntax:

```
line_number; "partial_string"; "prefix_to_remove"; "suffix_to_remove"
```

**Example:**
```
4; "0203."; ""; ""
15; "token"; "pre_"; "_end"
```

- Comments start with `##`
- Invalid syntax is highlighted in red
- Supports Ctrl+Z/Ctrl+Y for undo/redo

### 2. **Text Dump Area** (Right Panel)

- Paste large text dumps (supports 1000+ lines)
- Live line numbers that sync with scrolling
- Horizontal scrolling for wide content
- Right-click context menu (Cut/Copy/Paste)

### 3. **Execute & Extract**

1. **EXECUTE** - Finds matching patterns and highlights them in **bright green**
2. **EXTRACT** - Copies all highlighted values to clipboard (removes duplicates)

---

## 🎯 Real-World Example

### Input Text (line 4):
```
50 20    3   1 20  0203.3BB     Ra
```

### Config:
```
4; "0203."
```

### Result:
- Segments split by 2+ spaces: `50 20`, `3`, `1 20`, `0203.3BB`, `Ra`
- Matches segment containing "0203.": `0203.3BB`
- **Highlights**: `0203.3BB` (in bright green)

### With Prefix/Suffix Removal:
```
4; "0203."; "0203."; "BB"
```
**Extracts**: `3` (cleaned from `0203.3BB`)

---

## 📁 File Structure

```
cleancore/
├── cleancore.py              # Main application
├── CleanCore_Data/           # Auto-created data folder
│   ├── config.json          # Saved parsing configurations
│   ├── user_settings.json   # Per-user window positions & preferences
│   └── phrases.json         # Customizable motivational phrases
└── README.md
```

---

## ⚙️ Configuration Files

### `config.json`
Stores all your parsing configurations:

```json
{
  "configs": {
    "default": [
      {
        "line": 4,
        "partial": "0203.",
        "prefix": "",
        "suffix": ""
      }
    ],
    "myproject": [
      {
        "line": 10,
        "partial": "token",
        "prefix": "pre_",
        "suffix": "_end"
      }
    ]
  }
}
```

### `user_settings.json`
Per-user preferences (auto-saved on exit):

```json
{
  "john": {
    "width": 1200,
    "height": 800,
    "x": 100,
    "y": 50,
    "font_size": 13
  },
  "alice": {
    "width": 900,
    "height": 600,
    "x": 200,
    "y": 100,
    "font_size": 11
  }
}
```

### `phrases.json`
Customize motivational messages:

```json
{
  "phrases": [
    "Keep going, you're doing great!",
    "Coffee first, code second ☕",
    "Your only limit is the one you set for yourself.",
    "Add your own phrases here!"
  ]
}
```

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Z` | Undo (Config Editor) |
| `Ctrl+Y` | Redo (Config Editor) |
| `Ctrl+V` | Paste (Text Area) |
| `Ctrl+C` | Copy (Text Area) |
| `Ctrl+X` | Cut (Text Area) |
| `Ctrl+A` | Select All (Text Area) |

---

## 🎨 UI Controls

### Top Bar
- **Config Dropdown** - Select saved configuration
- **+ Button** - Create new configuration
- **Save Button** - Save current config to file
- **EXECUTE** - Parse and highlight matches
- **EXTRACT** - Copy unique values to clipboard

### Config Editor
- **A+** - Increase font size
- **A-** - Decrease font size

---

## 🔧 Advanced Usage

### Multi-Line Parsing

Parse multiple lines in one config:

```
## === PROJECT_X ===
4; "0203."
10; "token"; "start_"; "_end"
25; "value"
```

### Segment Detection

CleanCore splits text by **2 or more spaces**:

```
Text: "AA BB    CC DD    EE"
Segments: ["AA BB", "CC DD", "EE"]
```

Values with 0-1 spaces stay together as one unit.

---

## 🐛 Troubleshooting

### Line numbers not syncing?
- The scroll sync happens with a 10ms delay for performance
- If issues persist, try reducing the text area content

### Config syntax errors?
- Lines with invalid syntax are highlighted in **red**
- Valid format: `line; "partial"; "prefix"; "suffix"`
- Quotes are required around all string values

### Extract returns nothing?
- Ensure EXECUTE was clicked first to highlight text
- Check that your partial string matches the target segment

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**@Nao_funciona_**
- Created: November 2025
- Version: 1.3

---

## 🌟 Acknowledgments

- Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Inspired by the need for efficient text parsing workflows
- Thanks to all users for feedback and suggestions!

---

## 📸 Screenshots

### Main Interface
![Main Interface](docs/screenshot-main.png)
*Config editor (left) and text dump area with line numbers (right)*

### Pattern Matching
![Pattern Matching](docs/screenshot-highlight.png)
*Matched segments highlighted in bright green*

### Multi-Config Support
![Configs](docs/screenshot-configs.png)
*Switch between multiple saved configurations*

---

## 🔮 Roadmap

- [ ] Export results to CSV/JSON
- [ ] Regex pattern support
- [ ] Batch processing mode
- [ ] Dark/Light theme toggle
- [ ] Custom color schemes
- [ ] Search & replace in dump area
- [ ] Import configs from file

---

## 🆕 Latest update (2025-11-23)

- README updated with instructions for creating and activating a Python virtual environment for local development on Windows.

What I added:

- Quick commands to create a venv in the repository root and activate it in PowerShell.
- A short note to add `.venv/` to `.gitignore` and a recommended VS Code workspace setting to point to the venv interpreter.

How to create and use the virtual environment (PowerShell):

```powershell
# from the repository root (for example: c:\Users\diogo\Desktop\Git)
python -m venv .venv

# activate the venv in the current PowerShell session
.\.venv\Scripts\Activate.ps1

# if activation is blocked by execution policy, run this for the current process
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process; .\.venv\Scripts\Activate.ps1

# when done, deactivate:
deactivate
```

Recommended additions (optional):

- Add `.venv/` to your `.gitignore`:

```
.venv/
```

- For VS Code, create or update `.vscode/settings.json` to point to the interpreter:

```json
{
  "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe"
}
```

This makes it easy for the editor to pick up the correct interpreter.

---

**Made with ❤️ by @Nao_funciona_ • Keep parsing, keep winning! 🚀**