# CleanCore v1.3 - FINAL LEGENDARY EDITION
# @Nao_funciona_ • Portugal/Germany • 21 November 2025
# THE TOOL THE WORLD WAS WAITING FOR

import customtkinter as ctk
import json
import os
import re
import random
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# === DATA FOLDER (always next to the script) ===
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(SCRIPT_DIR, "CleanCore_Data")
os.makedirs(DATA_FOLDER, exist_ok=True)

CONFIG_FILE = os.path.join(DATA_FOLDER, "config.json")
USER_SETTINGS_FILE = os.path.join(DATA_FOLDER, "user_settings.json")
PHRASES_FILE = os.path.join(DATA_FOLDER, "phrases.json")


def get_current_username():
    try:
        username = os.getlogin()
    except:
        username = os.getenv('USER') or os.getenv('USERNAME') or "default_user"
    return "".join(c for c in username if c.isalnum() or c in "_-")


def load_phrases():
    default_phrases = [
        "Every sunrise is a new chance to chase your dreams!",
        "Your only limit is the one you set for yourself.",
        "Keep going—the view from the top is worth the climb!",
        "Small steps today lead to giant leaps tomorrow.",
        "You are stronger than yesterday and braver than you know",
        "Believe in yourself even when no one else does.",
        "The best time to start was yesterday. The next best time is now!",
        "Turn your wounds into wisdom and your setbacks into comebacks.",
        "You don't have to be great to start, but you have to start to be great.",
        "Difficult roads often lead to beautiful destinations",
        "Fall seven times, stand up eight.",
        "Your future is created by what you do today, not tomorrow.",
        "Be the energy you want to attract",
        "Progress, not perfection—keep moving forward!",
        "The comeback is always stronger than the setback.",
        "You were born to make an impact, so go out and do it!",
        "Doubt kills more dreams than failure ever will—keep believing.",
        "Inhale confidence, exhale doubt",
        "You're one decision away from a totally different life.",
        "Stay patient and trust your journey—everything is falling into place"
    ]
    if not os.path.exists(PHRASES_FILE):
        with open(PHRASES_FILE, 'w', encoding='utf-8') as f:
            json.dump({"phrases": default_phrases}, f, indent=2, ensure_ascii=False)
    try:
        with open(PHRASES_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("phrases", default_phrases)
    except:
        return default_phrases


def detect_system_theme():
    try:
        import platform
        if platform.system() == "Windows":
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            winreg.CloseKey(key)
            return "light" if value == 1 else "dark"
    except:
        pass
    return "dark"


def dark_messagebox(title, message):
    theme = detect_system_theme()
    try:
        is_maximized = app.winfo_width() >= app.winfo_screenwidth() or app.winfo_height() >= app.winfo_screenheight()
    except:
        is_maximized = False

    popup = ctk.CTkToplevel()
    popup.title(title)
    popup.geometry("800x300" if is_maximized else "540x220")
    bg = "#1e1e1e" if theme == "dark" else "#f0f0f0"
    fg = "#ffffff" if theme == "dark" else "#000000"
    popup.configure(fg_color=bg)
    popup.resizable(False, False)
    popup.transient(app)
    popup.grab_set()
    popup.lift()

    popup.update_idletasks()
    x = (popup.winfo_screenwidth() // 2) - (popup.winfo_width() // 2)
    y = (popup.winfo_screenheight() // 2) - (popup.winfo_height() // 2)
    popup.geometry(f"+{x}+{y}")

    ctk.CTkLabel(popup, text=message, font=("Consolas", 14 if is_maximized else 12),
                 text_color=fg, wraplength=750 if is_maximized else 500, justify="center").pack(pady=50)
    ctk.CTkButton(popup, text="OK", width=140, height=40, command=popup.destroy).pack(pady=10)
    popup.wait_window()


class LineNumberText(ctk.CTkFrame):
    def __init__(self, master, font_size=11, **kwargs):
        super().__init__(master, fg_color="transparent")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.font_size = font_size
        self.base_font = ctk.CTkFont("Consolas", self.font_size)

        self.line_numbers = ctk.CTkTextbox(
            self, width=60, font=self.base_font,
            fg_color="#1a1a1a", text_color="#606060", activate_scrollbars=False
        )
        self.line_numbers.grid(row=0, column=0, sticky="nsew")
        self.line_numbers.configure(state="disabled")

        self.text = ctk.CTkTextbox(
            self, font=self.base_font, undo=True, wrap="none", **kwargs
        )
        self.text.grid(row=0, column=1, sticky="nsew")

        self.h_scroll = ctk.CTkScrollbar(self, orientation="horizontal", command=self.text._textbox.xview)
        self.h_scroll.grid(row=1, column=1, sticky="ew")
        self.text._textbox.configure(xscrollcommand=self.h_scroll.set)

        self.text._textbox.tag_configure("bold",
            font=ctk.CTkFont("Consolas", self.font_size, weight="bold"), foreground="#00ff00")

        self.text._textbox.bind("<<Modified>>", lambda e: self.after(10, self._update_line_numbers))
        self.text._textbox.bind("<KeyRelease>", lambda e: self.after(10, self._update_line_numbers))
        self.text._textbox.bind("<MouseWheel>", lambda e: self.after(10, self._sync_scroll))
        self.text._textbox.bind("<Button-4>", lambda e: self.after(10, self._sync_scroll))
        self.text._textbox.bind("<Button-5>", lambda e: self.after(10, self._sync_scroll))
        self.text._textbox.config(yscrollcommand=self._on_text_scroll)

        self._setup_context_menu()
        self._update_line_numbers()

    def update_font_size(self, delta):
        self.font_size = max(8, min(28, self.font_size + delta))
        new_font = ctk.CTkFont("Consolas", self.font_size)
        self.line_numbers.configure(font=new_font)
        self.text.configure(font=new_font)
        bold_font = ctk.CTkFont("Consolas", self.font_size, weight="bold")
        self.text._textbox.tag_configure("bold", font=bold_font, foreground="#00ff00")
        self._update_line_numbers()

    def _setup_context_menu(self):
        menu = ctk.CTkFrame(self.text, fg_color="#2b2b2b", border_width=1)
        items = [("Cut", "<<Cut>>"), ("Copy", "<<Copy>>"), ("Paste", "<<Paste>>"),
                 ("Select All", lambda: self.text._textbox.tag_add("sel", "1.0", "end"))]
        for text, cmd in items:
            ctk.CTkButton(menu, text=text, width=100, height=25, fg_color="transparent", hover_color="#3a3a3a",
                          command=lambda c=cmd: (self.text._textbox.event_generate(c) if isinstance(c, str) else c(), menu.place_forget())).pack(pady=1)
        self.text._textbox.bind("<Button-3>", lambda e: menu.place(x=e.x_root-self.winfo_rootx(), y=e.y_root-self.winfo_rooty()))
        self.text._textbox.bind("<Button-1>", lambda e: menu.place_forget())

    def _on_text_scroll(self, *args):
        self.after(10, self._sync_scroll)

    def _sync_scroll(self, *args):
        try:
            self.line_numbers._textbox.yview_moveto(self.text._textbox.yview()[0])
        except:
            pass

    def _update_line_numbers(self):
        self.line_numbers.configure(state="normal")
        self.line_numbers.delete("1.0", "end")
        n = len(self.text.get("1.0", "end-1c").splitlines())
        self.line_numbers.insert("1.0", "\n".join(str(i) for i in range(1, n + 1)))
        self.line_numbers.configure(state="disabled")

    def get(self, s, e=None):
        return self.text.get(s) if e is None else self.text.get(s, e)


class CleanCore(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.username = get_current_username()
        self.phrases = load_phrases()
        self.title("CleanCore v1.3 - @Nao_funciona_")
        self.load_user_config()
        self.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

        self.configs = self._load_configs()
        self.current_config = "default"
        self.font_size = self.user_cfg.get("font_size", 11)

        self._setup_ui()
        self._load_first_config()
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_user_config(self):
        default = {"width": 900, "height": 600, "x": 200, "y": 100, "font_size": 11}
        if os.path.exists(USER_SETTINGS_FILE):
            try:
                with open(USER_SETTINGS_FILE, 'r', encoding='utf-8') as f:
                    all_users = json.load(f)
                    user_data = all_users.get(self.username, {})
                    default.update(user_data)
            except:
                pass
        self.width = default["width"]
        self.height = default["height"]
        self.x = default["x"]
        self.y = default["y"]
        self.font_size = default.get("font_size", 11)
        self.user_cfg = default

    def save_user_config(self):
        all_users = {}
        if os.path.exists(USER_SETTINGS_FILE):
            try:
                with open(USER_SETTINGS_FILE, 'r', encoding='utf-8') as f:
                    all_users = json.load(f)
            except:
                pass
        all_users[self.username] = {
            "width": self.winfo_width(),
            "height": self.winfo_height(),
            "x": self.winfo_x(),
            "y": self.winfo_y(),
            "font_size": self.font_size
        }
        with open(USER_SETTINGS_FILE, 'w', encoding='utf-8') as f:
            json.dump(all_users, f, indent=2)

    def on_close(self):
        self.save_user_config()
        self.destroy()

    def _load_configs(self):
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    configs = {}
                    for name, cfg in data.get("configs", {}).items():
                        if isinstance(cfg, list):
                            configs[name] = {"entries": cfg, "raw_lines": []}
                        else:
                            configs[name] = cfg
                    return configs
            except:
                pass
        return {"default": {"entries": [], "raw_lines": []}}

    def _save_configs(self):
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump({"configs": self.configs}, f, indent=2, ensure_ascii=False)

    def _setup_ui(self):
        top = ctk.CTkFrame(self, height=70, fg_color="#1a1a1a")
        top.pack(fill="x", padx=20, pady=20)
        top.pack_propagate(False)

        ctk.CTkLabel(top, text="Config:", font=("Arial", 15, "bold")).pack(side="left", padx=10)
        self.combo = ctk.CTkComboBox(top, values=list(self.configs.keys()), command=self._on_config_change, width=220)
        self.combo.pack(side="left", padx=5)

        ctk.CTkButton(top, text="+", width=40, fg_color="green", hover_color="#006400",
                     command=self._add_config).pack(side="left", padx=5)
        ctk.CTkButton(top, text="EXECUTE & SAVE", width=180, fg_color="#1f538d", hover_color="#0f3d6e",
                     font=("Arial", 12, "bold"), command=self._save_and_execute).pack(side="left", padx=10)
        ctk.CTkButton(top, text="EXTRACT", width=150, fg_color="#b0632d", hover_color="#8d4d1f",
                     command=self._extract).pack(side="left", padx=5)

        main = ctk.CTkFrame(self)
        main.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        main.grid_columnconfigure(0, minsize=350, weight=0)
        main.grid_columnconfigure(1, weight=1)
        main.grid_rowconfigure(0, weight=1)

        left = ctk.CTkFrame(main)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

        header = ctk.CTkFrame(left, fg_color="transparent")
        header.pack(fill="x", pady=10, padx=15)
        ctk.CTkLabel(header, text="Config Editor", font=("Consolas", 12, "bold")).pack(side="left")
        ctk.CTkButton(header, text="A-", width=30, command=lambda: self._change_font(-1)).pack(side="right", padx=2)
        ctk.CTkButton(header, text="A+", width=30, command=lambda: self._change_font(+1)).pack(side="right")

        ctk.CTkLabel(left, text='line; "partial"; "prefix"; "suffix"   |   ## \\n = blank line', 
                     font=("Consolas", 10), text_color="#888888").pack(pady=(0,5))

        self.config_text = ctk.CTkTextbox(left, font=("Consolas", self.font_size), undo=True)
        self.config_text.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        self.config_text._textbox.tag_configure("error", background="#4d1a1a")
        self.config_text._textbox.bind("<<Modified>>", self._validate_config_syntax)
        self.config_text._textbox.bind("<KeyRelease>", self._validate_config_syntax)

        right = ctk.CTkFrame(main)
        right.grid(row=0, column=1, sticky="nsew", padx=(5, 0))
        ctk.CTkLabel(right, text="DUMP AREA – NO WRAP + H-SCROLL", font=("Arial", 16, "bold")).pack(pady=15)
        self.text_area = LineNumberText(right, font_size=self.font_size)
        self.text_area.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        random_phrase = random.choice(self.phrases)
        ctk.CTkLabel(self, text=f"Hi {self.username} • {random_phrase}",
                     text_color="#aaaaaa", font=("Consolas", 15, "bold"), justify="center").pack(pady=(0, 2))
        ctk.CTkLabel(self, text="CleanCore v1.3 © @Nao_funciona_ • Nov 2025",
                     text_color="#888888", font=("Consolas", 13), justify="center").pack(pady=(0, 15))

    def _validate_config_syntax(self, event=None):
        self.config_text._textbox.edit_modified(False)
        self.config_text._textbox.tag_remove("error", "1.0", "end")
        for i, line in enumerate(self.config_text.get("1.0", "end-1c").splitlines(), 1):
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            if not re.match(r'^\s*\d+\s*;\s*"[^"]*"(?:\s*;\s*"[^"]*")?(?:\s*;\s*"[^"]*")?\s*$', s):
                self.config_text._textbox.tag_add("error", f"{i}.0", f"{i}.end")

    def _change_font(self, delta):
        self.font_size = max(8, min(28, self.font_size + delta))
        new_font = ctk.CTkFont("Consolas", self.font_size)
        self.config_text.configure(font=new_font)
        self.text_area.update_font_size(delta)

    def _load_first_config(self):
        if self.configs:
            first = list(self.configs.keys())[0]
            self.combo.set(first)
            self._on_config_change(first)

    def _on_config_change(self, name):
        self.current_config = name
        cfg = self.configs.get(name, {"entries": [], "raw_lines": []})
        if cfg.get("raw_lines"):
            text = "\n".join(cfg["raw_lines"])
        else:
            text = f"## === {name.upper()} ===\n"
            text += f"## {datetime.now().strftime('%d.%m.%Y %H:%M')} • @Nao_funciona_\n\n"
            for e in cfg.get("entries", []):
                if isinstance(e, str):
                    text += e + "\n"
                else:
                    l = e.get("line", 1)
                    p = e.get("partial", "")
                    pre = e.get("prefix", "")
                    suf = e.get("suffix", "")
                    line = f'{l}; "{p}"'
                    if pre: line += f'; "{pre}"'
                    if suf: line += f'; "{suf}"'
                    text += line + "\n"
        self.config_text.delete("1.0", "end")
        self.config_text.insert("1.0", text)

    def _add_config(self):
        dialog = ctk.CTkInputDialog(text="Enter new config name:", title="CleanCore – New Config")
        dialog.geometry("400x200")
        dialog.configure(fg_color="#1e1e1e")
        name = dialog.get_input()
        if not name or not name.strip():
            dark_messagebox("Error", "Name cannot be empty!")
            return
        name = name.strip()
        if name in self.configs:
            dark_messagebox("Error", "Config already exists!")
            return

        self.current_config = name
        self.configs[name] = {
            "entries": [],
            "raw_lines": [
                f"## === {name.upper()} ===",
                f"## Created {datetime.now().strftime('%d.%m.%Y %H:%M')}",
                '## line; "partial"; "prefix_to_cut"; "suffix_to_cut"',
                '## Use ## \\n for blank line in extract',
                ""
            ]
        }
        self._save_configs()
        self.combo.configure(values=list(self.configs.keys()))
        self.combo.set(name)
        self.config_text.delete("1.0", "end")
        self.config_text.insert("1.0", "\n".join(self.configs[name]["raw_lines"]))
        dark_messagebox("Success", f"Config '{name}' created!")

    def _save_current_config(self, silent=False):
        raw_lines = self.config_text.get("1.0", "end-1c").splitlines()
        entries = []
        for raw in raw_lines:
            s = raw.strip()
            if not s or s.startswith("#"):
                continue
            m = re.match(r'^\s*(\d+)\s*;\s*"([^"]*)"(?:\s*;\s*"([^"]*)")?(?:\s*;\s*"([^"]*)")?\s*$', s)
            if m:
                entries.append({
                    "line": int(m.group(1)),
                    "partial": m.group(2),
                    "prefix": (m.group(3) or "").strip(),
                    "suffix": (m.group(4) or "").strip(),
                    "raw": raw
                })
        self.configs[self.current_config] = {"entries": entries, "raw_lines": raw_lines}
        self._save_configs()
        if not silent:
            dark_messagebox("CleanCore", f"Config '{self.current_config}' saved!")

    def _save_and_execute(self):
        self._save_current_config(silent=True)
        self._execute()

    def _execute(self):
        self.text_area.text._textbox.tag_remove("bold", "1.0", "end")
        dump_lines = self.text_area.get("1.0", "end-1c").splitlines()
        entries = []
        cfg = self.configs.get(self.current_config, {})
        raw_entries = cfg.get("entries", []) if isinstance(cfg, dict) else cfg

        for entry in raw_entries:
            if isinstance(entry, str):
                m = re.match(r'^\s*(\d+)\s*;\s*"([^"]*)"(?:\s*;\s*"([^"]*)")?(?:\s*;\s*"([^"]*)")?\s*$', entry.strip())
                if not m: continue
                ln, p, pre, suf = int(m.group(1)), m.group(2), (m.group(3) or "").strip(), (m.group(4) or "").strip()
            else:
                ln = entry.get("line", 1)
                p = entry.get("partial", "")
                pre = entry.get("prefix", "")
                suf = entry.get("suffix", "")
            if not p: continue
            entries.append((ln, p, pre, suf))

        for line_num, partial, prefix, suffix in entries:
            if line_num > len(dump_lines): continue
            line = dump_lines[line_num - 1]
            segments = [s.strip() for s in re.split(r'\s{2,}', line) if s.strip()]
            for seg in segments:
                if partial not in seg: continue
                cleaned = seg
                offset = 0
                if prefix and seg.startswith(prefix):
                    cleaned = cleaned[len(prefix):]
                    offset = len(prefix)
                if suffix and cleaned.endswith(suffix):
                    cleaned = cleaned[:-len(suffix)]
                if not cleaned: continue
                start = line.find(seg)
                self.text_area.text._textbox.tag_add("bold",
                    f"{line_num}.{start + offset}", f"{line_num}.{start + offset + len(cleaned)}")
                break

    def _extract(self):
        """Extract EXACTLY one value per config line (first match only) — NO TUPLE ERRORS"""
        result = []
        used_tags = set()  # Use string representation (safe for sets)

        # Collect all bold ranges with position info
        bold_ranges = []
        ranges = self.text_area.text._textbox.tag_ranges("bold")
        for i in range(0, len(ranges), 2):
            start = ranges[i]
            end = ranges[i + 1]
            line_num = int(str(start).split('.')[0])
            text = self.text_area.text._textbox.get(start, end).strip()
            if text:
                bold_ranges.append((line_num, text, str(start), str(end)))  # str() makes it hashable

        # Sort by line and position
        bold_ranges.sort(key=lambda x: (x[0], x[2]))  # sort by line_num and start pos

        # Process config line by line
        for raw_line in self.config_text.get("1.0", "end-1c").splitlines():
            s = raw_line.strip()

            # Blank line separator
            if s in ("## \\n", "##\\n", "## \\n "):
                result.append("")
                continue

            if not s or s.startswith("#"):
                continue

            m = re.match(r'^\s*(\d+)\s*;\s*"([^"]*)"', s)
            if not m:
                continue

            target_line = int(m.group(1))

            # Find FIRST unused bold segment on this line
            found = False
            for line_num, text, start_str, end_str in bold_ranges:
                if line_num == target_line and (start_str, end_str) not in used_tags:
                    result.append(text)
                    used_tags.add((start_str, end_str))  # str tuples are hashable!
                    found = True
                    break

            # If no match on this rule → add nothing (keeps count exact)

        # Copy result
        if result:
            output = "\n".join(result)
            self.clipboard_clear()
            self.clipboard_append(output)
            self.update()
            count = len([x for x in result if x])
            dark_messagebox("CleanCore", f"EXACTLY {count} values copied (1 per config line)!")
        else:
            dark_messagebox("CleanCore", "No bold text found")



if __name__ == "__main__":
    app = CleanCore()
    app.mainloop()
