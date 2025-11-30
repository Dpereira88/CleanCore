# CleanCore

![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![CustomTkinter](https://img.shields.io/badge/customtkinter-5.2%2B-9cf.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Downloads](https://img.shields.io/github/downloads/Dpereira88/CleanCore/total?color=green)

**The fastest, smartest and cleanest data extractor ever built.**  
Created by **@Nao_funciona_** • November 2025  

---

## What's New (2025)

- Window position saved **per monitor layout** (1 screen ≠ 2 screens ≠ 3 screens)  
- Built-in **image tutorial** (click the **?** button) with infinite loop slideshow  
- Looping next/previous navigation – never gets stuck  
- Improved prefix/suffix handling + real-time syntax validation  
- Automatic recovery when a monitor is disconnected  
- 100 % offline • Portable .exe ready  

---

## Features

- Modern dark UI built with **CustomTkinter**  
- Dual-panel layout: config editor + dump area with live line numbers  
- Smart column detection (splits on **2+ spaces**)  
- Full **prefix / suffix** trimming  
- Named configs – create (+), rename (Edit), delete (−)  
- Real-time syntax highlighting (invalid lines → red)  
- **EXECUTE & SAVE** → green highlight → **EXTRACT** (clean copy)  
- Adjustable font size (A+ / A-)  
- Per-user settings (size, position, font)  
- Random motivational quotes on startup  
- Works perfectly as a **single .exe** (PyInstaller)  

---

## Quick Start

### Option 1 – Portable .exe (recommended)
Download the latest release → unzip → double-click `CleanCore.exe`  
[Releases](https://github.com/Dpereira88/CleanCore/releases)

### Option 2 – Run from source
```bash
git clone https://github.com/Dpereira88/CleanCore.git
cd CleanCore
pip install customtkinter pillow
python CleanCore.py