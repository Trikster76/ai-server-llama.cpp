import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess
import threading
import os
import traceback
import json
import webbrowser
import shlex  # Для правильного парсинга сырых аргументов

# ==================================================================================================
# I18N - Локализация
# ==================================================================================================
TRANSLATIONS = {
    "app_title": {
        "ru": "Neural Core: AI Server Launcher", 
        "en": "Neural Core: AI Server Launcher",
        "uk": "Neural Core: AI Сервер Лаунчер"
    },
    "file_menu": {
        "ru": "Файл", 
        "en": "File",
        "uk": "Файл"
    },
    "exit_menu": {
        "ru": "Выход", 
        "en": "Exit",
        "uk": "Вихід"
    },
    "settings_menu": {
        "ru": "Настройки", 
        "en": "Settings",
        "uk": "Налаштування"
    },
    "language_menu": {
        "ru": "Язык", 
        "en": "Language",
        "uk": "Мова"
    },
    "theme_menu": {
        "ru": "Тема", 
        "en": "Theme",
        "uk": "Тема"
    },
    "theme_neural": {
        "ru": "Neural Core (Cyberpunk)", 
        "en": "Neural Core (Cyberpunk)",
        "uk": "Neural Core (Cyberpunk)"
    },
    "theme_darkly": {
        "ru": "Тёмная (Darkly)", 
        "en": "Dark (Darkly)",
        "uk": "Темна (Darkly)"
    },
    "theme_litera": {
        "ru": "Светлая (Litera)", 
        "en": "Light (Litera)",
        "uk": "Світла (Litera)"
    },
    "theme_superhero": {
        "ru": "Контрастная (Superhero)", 
        "en": "Contrast (Superhero)",
        "uk": "Контрастна (Superhero)"
    },
    "help_menu": {
        "ru": "Помощь", 
        "en": "Help",
        "uk": "Допомога"
    },
    "about_menu": {
        "ru": "О программе", 
        "en": "About",
        "uk": "Про програму"
    },
    "llama_tab": {
        "ru": "Llama.cpp Сервер", 
        "en": "Llama.cpp Server",
        "uk": "Llama.cpp Сервер"
    },
    "webui_tab": {
        "ru": "Open WebUI", 
        "en": "Open WebUI",
        "uk": "Open WebUI"
    },
    "server_executable_path": {
        "ru": "Исполняемый файл Llama.cpp (server.exe)", 
        "en": "Llama.cpp Executable (server.exe)",
        "uk": "Виконуваний файл Llama.cpp (server.exe)"
    },
    "backend_cpu": {
        "ru": "Бэкенд CPU", 
        "en": "CPU Backend",
        "uk": "Бекенд CPU"
    },
    "backend_vulkan": {
        "ru": "Бэкенд Vulkan", 
        "en": "Vulkan Backend",
        "uk": "Бекенд Vulkan"
    },
    "backend_mixed": {
        "ru": "Бэкенд Mixed", 
        "en": "Mixed Backend",
        "uk": "Бекенд Mixed"
    },
    "browse_button": {
        "ru": "Обзор...", 
        "en": "Browse...",
        "uk": "Огляд..."
    },
    "model_path": {
        "ru": "Модель", 
        "en": "Model",
        "uk": "Модель"
    },
    "main_sampling_tab": {
        "ru": "Основные и Генерация", 
        "en": "Main & Generation",
        "uk": "Основні та Генерація"
    },
    "system_tab": {
        "ru": "Система и Сеть", 
        "en": "System & Network",
        "uk": "Система та Мережа"
    },
    "key_params": {
        "ru": "Ключевые параметры", 
        "en": "Key Parameters",
        "uk": "Ключові параметри"
    },
    "port": {
        "ru": "Порт", 
        "en": "Port",
        "uk": "Порт"
    },
    "context": {
        "ru": "Контекст", 
        "en": "Context",
        "uk": "Контекст"
    },
    "gpu_layers": {
        "ru": "Слои ГПУ (-1 = все)", 
        "en": "GPU Layers (-1 = all)",
        "uk": "Шари ГПУ (-1 = всі)"
    },
    "cpu_threads": {
        "ru": "Потоки ЦПУ", 
        "en": "CPU Threads",
        "uk": "Потоки ЦПУ"
    },
    "batch_size": {
        "ru": "Размер батча", 
        "en": "Batch Size",
        "uk": "Розмір батча"
    },
    "flags": {
        "ru": "Флаги", 
        "en": "Flags",
        "uk": "Прапорці"
    },
    "jinja_template": {
        "ru": "Jinja Template", 
        "en": "Jinja Template",
        "uk": "Jinja Шаблон"
    },
    "no_warmup": {
        "ru": "Без прогрева (no-warmup)", 
        "en": "No Warmup",
        "uk": "Без прогріву (no-warmup)"
    },
    "embedding_mode": {
        "ru": "Embedding Mode", 
        "en": "Embedding Mode",
        "uk": "Режим Embedding"
    },
    "sampling_params": {
        "ru": "Параметры генерации текста", 
        "en": "Text Generation Parameters",
        "uk": "Параметри генерації тексту"
    },
    "temperature": {
        "ru": "Температура", 
        "en": "Temperature",
        "uk": "Температура"
    },
    "top_k": {
        "ru": "Top-K", 
        "en": "Top-K",
        "uk": "Top-K"
    },
    "top_p": {
        "ru": "Top-P", 
        "en": "Top-P",
        "uk": "Top-P"
    },
    "repeat_penalty": {
        "ru": "Штраф за повторения", 
        "en": "Repeat Penalty",
        "uk": "Штраф за повторення"
    },
    "network_settings": {
        "ru": "Сетевые настройки", 
        "en": "Network Settings",
        "uk": "Мережеві налаштування"
    },
    "host": {
        "ru": "Хост (IP-адрес)", 
        "en": "Host (IP Address)",
        "uk": "Хост (IP-адреса)"
    },
    "api_key": {
        "ru": "Ключ API", 
        "en": "API Key",
        "uk": "Ключ API"
    },
    "performance": {
        "ru": "Производительность", 
        "en": "Performance",
        "uk": "Продуктивність"
    },
    "mlock": {
        "ru": "Блокировать в ОЗУ (mlock)", 
        "en": "Lock in Memory (mlock)",
        "uk": "Блокувати в ОЗП (mlock)"
    },
    "custom_params": {
        "ru": "Дополнительные параметры (вручную)", 
        "en": "Additional Parameters (Manual)",
        "uk": "Додаткові параметры (вручную)"
    },
    "raw_args": {
        "ru": "Сырые аргументы (Raw args)", 
        "en": "Raw arguments string",
        "uk": "Дод. аргументи рядком (Raw args)"
    },
    "info_raw_args": {
        "ru": "Впишите любые флаги через пробел (например: --kv-unified --cache-idle-slots)", 
        "en": "Enter any flags separated by space (e.g. --kv-unified --cache-idle-slots)",
        "uk": "Введіть будь-які прапорці через пробіл (наприклад: --kv-unified --cache-idle-slots)"
    },
    "run_llama_button": {
        "ru": "Запустить Llama.cpp", 
        "en": "Run Llama.cpp",
        "uk": "Запустити Llama.cpp"
    },
    "stop_llama_button": {
        "ru": "Остановить Llama.cpp", 
        "en": "Stop Llama.cpp",
        "uk": "Зупинити Llama.cpp"
    },
    "open_webui_button": {
        "ru": "Открыть Web UI", 
        "en": "Open Web UI",
        "uk": "Відкрити Web UI"
    },
    "reset_settings_button": {
        "ru": "Сбросить настройки", 
        "en": "Reset Settings",
        "uk": "Скинути налаштування"
    },
    "apply_preset_button": {
        "ru": "Применить пресет модели", 
        "en": "Apply Model Preset",
        "uk": "Застосувати пресет моделі"
    },
    "llama_logs": {
        "ru": "Логи Llama.cpp сервера", 
        "en": "Llama.cpp Server Logs",
        "uk": "Логи Llama.cpp сервера"
    },
    "webui_controls": {
        "ru": "Управление сервером Open WebUI", 
        "en": "Open WebUI Server Control",
        "uk": "Керування сервером Open WebUI"
    },
    "run_webui_button": {
        "ru": "Запустить Open WebUI", 
        "en": "Run Open WebUI",
        "uk": "Запустити Open WebUI"
    },
    "stop_webui_button": {
        "ru": "Остановить Open WebUI", 
        "en": "Stop Open WebUI",
        "uk": "Зупинити Open WebUI"
    },
    "webui_logs": {
        "ru": "Логи Open WebUI", 
        "en": "Open WebUI Logs",
        "uk": "Логи Open WebUI"
    },
    "status_llama": {
        "ru": "Llama.cpp", 
        "en": "Llama.cpp",
        "uk": "Llama.cpp"
    },
    "status_webui": {
        "ru": "WebUI", 
        "en": "WebUI",
        "uk": "WebUI"
    },
    "status_running": {
        "ru": "Запущен", 
        "en": "Running",
        "uk": "Запущено"
    },
    "status_stopped": {
        "ru": "Остановлен", 
        "en": "Stopped",
        "uk": "Зупинено"
    },
    "about_title": {
        "ru": "О программе AI Server Launcher", 
        "en": "About AI Server Launcher",
        "uk": "Про програму AI Server Launcher"
    },
    "about_text": {
        "ru": "AI Server Launcher Prestige v3.2 (Neural Core)\n\nПродвинутый интерфейс для управления серверами llama.cpp и Open WebUI.\n\nРазработано Архитектором.", 
        "en": "AI Server Launcher Prestige v3.2 (Neural Core)\n\nAn advanced GUI for managing llama.cpp and Open WebUI servers.\n\nDeveloped by the Architect.",
        "uk": "AI Server Launcher Prestige v3.2 (Neural Core)\n\nПросунутий інтерфейс для керування серверами llama.cpp та Open WebUI.\n\nРозробено Архітектором."
    },
    "preset_applied": {
        "ru": "Применен пресет '{preset}' для модели.", 
        "en": "Applied preset '{preset}' for the model.",
        "uk": "Застосовано пресет '{preset}' для моделі."
    },
    "preset_not_found": {
        "ru": "Автоматический пресет для модели не найден. Используются стандартные настройки.", 
        "en": "Automatic preset for the model not found. Using default settings.",
        "uk": "Автоматичний пресет для моделі не знайдено. Використовуються стандартні налаштування."
    },
    "settings_reset": {
        "ru": "Настройки сброшены к значениям по умолчанию.", 
        "en": "Settings have been reset to default.",
        "uk": "Налаштування скинуті до значень за замовчуванням."
    },
    "settings_loaded": {
        "ru": "Загружены настройки для '{model}'.", 
        "en": "Loaded settings for '{model}'.",
        "uk": "Завантажено налаштування для '{model}'."
    },
    "settings_saved": {
        "ru": "Настройки для '{model}' сохранены.", 
        "en": "Settings for '{model}' saved.",
        "uk": "Налаштування для '{model}' збережено."
    },
    "default_settings_used": {
        "ru": "Для '{model}' используются настройки по умолчанию.", 
        "en": "Using default settings for '{model}'.",
        "uk": "Використовуються налаштування за замовчуванням для '{model}'."
    },
    "backend_selection": {
        "ru": "Выберите бэкенд", 
        "en": "Select Backend",
        "uk": "Виберіть бекенд"
    },
    "toggle_backends": {
        "ru": "▸ Показать бэкенды", 
        "en": "▸ Show Backends",
        "uk": "▸ Показати бекенди"
    },
    "toggle_backends_hide": {
        "ru": "▾ Скрыть бэкенды", 
        "en": "▾ Hide Backends",
        "uk": "▾ Сховати бекенди"
    },
    "backend_label_cpu": {
        "ru": "CPU:", 
        "en": "CPU:",
        "uk": "CPU:"
    },
    "backend_label_vulkan": {
        "ru": "Vulkan:", 
        "en": "Vulkan:",
        "uk": "Vulkan:"
    },
    "backend_label_mixed": {
        "ru": "Mixed:", 
        "en": "Mixed:",
        "uk": "Mixed:"
    },
    "custom_params_1_6": {
        "ru": "Параметры 1-6",
        "en": "Parameters 1-6",
        "uk": "Параметри 1-6"
    },
    "custom_params_7_12": {
        "ru": "Параметры 7-12",
        "en": "Parameters 7-12",
        "uk": "Параметри 7-12"
    },
    "info_custom_params": {
        "ru": "Введите дополнительные параметры llama.cpp в формате: 'имя_параметра значение'", 
        "en": "Enter additional llama.cpp parameters in format: 'parameter_name value'",
        "uk": "Введіть додаткові параметри llama.cpp у форматі: 'ім'я_параметра значення'"
    },
    "info_webui": {
        "ru": "Open WebUI запускается командой 'open-webui serve'. Убедитесь, что Open WebUI установлен.", 
        "en": "Open WebUI is launched with 'open-webui serve'. Make sure Open WebUI is installed.",
        "uk": "Open WebUI запускається командою 'open-webui serve'. Переконайтеся, що Open WebUI встановлено."
    },
    "select_server_exe": {
        "ru": "Выберите server.exe", 
        "en": "Select server.exe",
        "uk": "Виберіть server.exe"
    },
    "select_gguf_model": {
        "ru": "Выберите модель GGUF", 
        "en": "Select GGUF model",
        "uk": "Виберіть модель GGUF"
    },
    "error_executable_not_found": {
        "ru": "Ошибка: Исполняемый файл Llama.cpp не найден для выбранного бэкенда!", 
        "en": "Error: Llama.cpp executable not found for selected backend!",
        "uk": "Помилка: Виконуваний файл Llama.cpp не знайдено для вибраного бекенду!"
    },
    "error_model_not_found": {
        "ru": "Ошибка: Файл модели не выбран или не найден!", 
        "en": "Error: Model file not selected or not found!",
        "uk": "Помилка: Файл моделі не вибрано або не знайдено!"
    },
    "starting_server": {
        "ru": "--- Запуск {p_type} сервера ---", 
        "en": "--- Starting {p_type} server ---",
        "uk": "--- Запуск {p_type} сервера ---"
    },
    "stopping_server": {
        "ru": "--- Остановка сервера {p_type} ---", 
        "en": "--- Stopping {p_type} server ---",
        "uk": "--- Зупинка сервера {p_type} ---"
    },
    "command": {
        "ru": "Команда: ", 
        "en": "Command: ",
        "uk": "Команда: "
    },
    "error_starting": {
        "ru": "Ошибка при запуске: ", 
        "en": "Error starting: ",
        "uk": "Помилка при запуску: "
    },
}

# --- ToolTip Class ---
class ToolTip:
    def __init__(self, widget, text_provider):
        self.widget = widget
        self.text_provider = text_provider
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)
    
    def show_tooltip(self, event):
        if not self.text_provider(): 
            return
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(f"+{x}+{y}")
        label = ttk.Label(self.tooltip_window, text=self.text_provider(), justify='left', 
                         bootstyle=INVERSE, padding=5, wraplength=250)
        label.pack(ipadx=1)
    
    def hide_tooltip(self, event):
        if self.tooltip_window: 
            self.tooltip_window.destroy()
        self.tooltip_window = None

# --- Collapsible Frame Class ---
class CollapsibleFrame(ttk.Frame):
    def __init__(self, parent, text="", *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        
        self.show = tk.BooleanVar(value=False)
        self.toggle_text = tk.StringVar(value=text)
        
        # Toggle button
        self.toggle_btn = ttk.Button(
            self, 
            textvariable=self.toggle_text,
            command=self.toggle,
            bootstyle="link",
            width=20
        )
        self.toggle_btn.pack(fill="x", anchor="w", pady=(0, 5))
        
        # Content frame
        self.content_frame = ttk.Frame(self, relief="flat")
        
    def toggle(self):
        if self.show.get():
            self.content_frame.pack_forget()
            self.toggle_text.set(self.toggle_text.get().replace("▾", "▸"))
        else:
            self.content_frame.pack(fill="x", expand=True)
            self.toggle_text.set(self.toggle_text.get().replace("▸", "▾"))
        self.show.set(not self.show.get())

# ==================================================================================================
# Main Application Class
# ==================================================================================================
class LlamaCppGUI(ttk.Window):
    def __init__(self):
        # 1. Читаем конфиг, чтобы понять, какой язык и тему хочет юзер
        initial_theme, initial_lang = self.load_app_config_statically()
        
        # 2. Инициализируем окно базовой темой (темной), чтобы получить доступ к Style
        super().__init__(themename="darkly")
        
        # 3. Инжектим нашу кастомную Neural Core тему
        self.create_custom_theme()
        
        # 4. Применяем нужную тему (если в конфиге neural_core, ставим ее)
        if initial_theme == "neural_core" or initial_theme not in self.style.theme_names():
            self.style.theme_use("neural_core")
            self.theme_var = tk.StringVar(value="neural_core")
        else:
            self.style.theme_use(initial_theme)
            self.theme_var = tk.StringVar(value=initial_theme)
            
        self.apply_custom_theme_overrides()
            
        self.language = tk.StringVar(value=initial_lang)
        
        self.settings_file = "launcher_settings.json"
        self.processes = {"llama": None, "webui": None}
        
        self.define_default_settings()

        self.title(self.translate("app_title"))
        try:
            self.iconbitmap(r"G:\Проект\llama1.ico")
        except Exception:
            pass  # Ігнорувати, если иконка не найдена
        self.geometry("1050x1000")
        
        self.create_menu()
        self.create_widgets()
        self.create_status_bar()

        self.load_initial_settings()
        self.update_ui_text()
        self.apply_theme_to_logs()  # Применяем шрифты и цвета терминала к логам

    def create_custom_theme(self):
        """Инжектим кастомную тему в стиле Neural Core"""
        from ttkbootstrap.style import ThemeDefinition, Colors

        colors = Colors(
            primary="#00f0ff",      # Cyan (Main accents)
            secondary="#131c2a",    # Dark slate (Panels, disabled)
            success="#00ff9d",      # Bright green (Success)
            info="#b061ff",         # Purple (Info/Secondary accents)
            warning="#ffb800",      # Orange/Yellow
            danger="#ff3366",       # Red/Pink (Stop, Errors)
            bg="#0a0f18",           # Very dark blue-grey (Main BG)
            fg="#a3c2c2",           # Light cyan-grey (Main Text)
            selectbg="#00f0ff",     # Selection
            selectfg="#0a0f18",     # Selected text
            border="#213145",       # Borders
            inputfg="#00f0ff",      # Text inside entries
            inputbg="#0d1421",      # Entry background
            light="#131c2a",        # Light variant
            dark="#050a10",         # Dark variant
            active="#00b8c4"        # Active state
        )

        td = ThemeDefinition(
            name="neural_core",
            colors=colors,
            themetype="dark"
        )

        self.style.register_theme(td)

    def apply_custom_theme_overrides(self):
        """Применяет исправления стилей для темы Neural Core (cyberpunk)"""
        theme_name = self.style.theme.name
        if theme_name == "neural_core":
            # Исправляем нечитаемый текст на вкладках (Notebook tabs)
            for style_name in ["TNotebook.Tab", "primary.TNotebook.Tab", "secondary.TNotebook.Tab", "Secondary.TNotebook.Tab", "Primary.TNotebook.Tab"]:
                self.style.map(
                    style_name,
                    foreground=[("selected", "#00f0ff"), ("!selected", "#a3c2c2")],
                    background=[("selected", "#0a0f18"), ("!selected", "#131c2a")]
                )
            
            # Исправляем нечитаемые readonly поля ввода (Entry)
            self.style.map(
                "TEntry",
                fieldbackground=[("readonly", "#131c2a")],
                foreground=[("readonly", "#a3c2c2")]
            )

    def translate(self, key):
        return TRANSLATIONS.get(key, {}).get(self.language.get(), key)

    @staticmethod
    def load_app_config_statically():
        """Loads language and theme before the main window is created."""
        try:
            with open("launcher_settings.json", 'r', encoding='utf-8') as f:
                config = json.load(f)
            # Ставим neural_core по умолчанию для всех новых запусков
            theme = config.get('app_theme', 'neural_core')
            lang = config.get('app_language', 'ru')
            return theme, lang
        except (IOError, json.JSONDecodeError):
            return 'neural_core', 'ru'

    def define_default_settings(self):
        self.defaults = {
            "params": {"port": "8080", "ctx_size": "4096", "n_gpu_layers": "-1", "threads": "8", "batch_size": "512"},
            "sampling_params": {"temp": "0.7", "top_k": "40", "top_p": "0.95", "repeat_penalty": "1.1"},
            "system_params": {"host": "127.0.0.1", "api_key": ""},
            "flags": {"jinja": False, "no_warmup": False, "embedding": False, "mlock": True},
        }
        self.params = {key: tk.StringVar(value=val) for key, val in self.defaults["params"].items()}
        self.sampling_params = {key: tk.StringVar(value=val) for key, val in self.defaults["sampling_params"].items()}
        self.system_params = {key: tk.StringVar(value=val) for key, val in self.defaults["system_params"].items()}
        self.flags = {key: tk.BooleanVar(value=val) for key, val in self.defaults["flags"].items()}
        # 12 custom parameters (slots)
        self.custom_params = [(tk.StringVar(value=""), tk.StringVar(value="")) for _ in range(12)]
        
        # New Raw Args parameter
        self.raw_args = tk.StringVar(value="")

        self.server_paths = {
            "cpu": tk.StringVar(),
            "vulkan": tk.StringVar(),
            "mixed": tk.StringVar()
        }
        self.selected_backend = tk.StringVar(value="cpu")  # Default to CPU
        
        # Словники для зберігання посилань на віджети бекендів
        self.backend_labels = {}
        self.backend_entries = {}
        self.backend_browse_buttons = {}

    def create_menu(self):
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label=self.translate("file_menu"), menu=self.file_menu)
        self.file_menu.add_command(label=self.translate("exit_menu"), command=self.on_closing)

        self.settings_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label=self.translate("settings_menu"), menu=self.settings_menu)
        
        self.language_menu = tk.Menu(self.settings_menu, tearoff=0)
        self.settings_menu.add_cascade(label=self.translate("language_menu"), menu=self.language_menu)
        self.language_menu.add_radiobutton(label="Українська", variable=self.language, value="uk", command=self.on_language_change)
        self.language_menu.add_radiobutton(label="Русский", variable=self.language, value="ru", command=self.on_language_change)
        self.language_menu.add_radiobutton(label="English", variable=self.language, value="en", command=self.on_language_change)
        
        self.theme_menu = tk.Menu(self.settings_menu, tearoff=0)
        self.settings_menu.add_cascade(label=self.translate("theme_menu"), menu=self.theme_menu)
        self.theme_menu.add_radiobutton(label=self.translate("theme_neural"), variable=self.theme_var, value="neural_core", command=self.on_theme_change)
        self.theme_menu.add_radiobutton(label=self.translate("theme_darkly"), variable=self.theme_var, value="darkly", command=self.on_theme_change)
        self.theme_menu.add_radiobutton(label=self.translate("theme_litera"), variable=self.theme_var, value="litera", command=self.on_theme_change)
        self.theme_menu.add_radiobutton(label=self.translate("theme_superhero"), variable=self.theme_var, value="superhero", command=self.on_theme_change)

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label=self.translate("help_menu"), menu=self.help_menu)
        self.help_menu.add_command(label=self.translate("about_menu"), command=self.show_about)

    def create_widgets(self):
        self.main_notebook = ttk.Notebook(self, bootstyle="primary")
        self.main_notebook.pack(expand=True, fill='both', padx=10, pady=10)

        self.llama_tab = ttk.Frame(self.main_notebook)
        self.main_notebook.add(self.llama_tab, text=self.translate("llama_tab"))
        self.create_llama_cpp_tab(self.llama_tab)

        self.webui_tab = ttk.Frame(self.main_notebook)
        self.main_notebook.add(self.webui_tab, text=self.translate("webui_tab"))
        self.create_open_webui_tab(self.webui_tab)

    def create_status_bar(self):
        self.status_bar = ttk.Frame(self, padding=(5, 2))
        self.status_bar.pack(side=BOTTOM, fill=X)
        
        # Іконки статусу (кольорові кружечки)
        self.llama_status_icon = ttk.Label(self.status_bar, text="⬤", font=("Arial", 12), foreground=self.style.colors.danger)
        self.llama_status_icon.pack(side=LEFT, padx=(10, 5))
        
        self.llama_status_var = tk.StringVar(value=f"{self.translate('status_llama')}: {self.translate('status_stopped')}")
        ttk.Label(self.status_bar, textvariable=self.llama_status_var).pack(side=LEFT, padx=5)
        
        ttk.Separator(self.status_bar, orient=VERTICAL).pack(side=LEFT, fill=Y, padx=10)
        
        self.webui_status_icon = ttk.Label(self.status_bar, text="⬤", font=("Arial", 12), foreground=self.style.colors.danger)
        self.webui_status_icon.pack(side=LEFT, padx=(10, 5))
        
        self.webui_status_var = tk.StringVar(value=f"{self.translate('status_webui')}: {self.translate('status_stopped')}")
        ttk.Label(self.status_bar, textvariable=self.webui_status_var).pack(side=LEFT, padx=5)

    def create_llama_cpp_tab(self, parent):
        # Налаштування ваги рядків
        parent.grid_rowconfigure(7, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        
        # Рядок 0: Згортаємий фрейм для бекендів
        server_frame_outer = ttk.Frame(parent)
        server_frame_outer.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        
        # Collapsible frame for backends
        self.backends_frame = CollapsibleFrame(server_frame_outer, text=self.translate("toggle_backends"))
        self.backends_frame.pack(fill=X, expand=True)
        
        # Server frame inside collapsible
        self.server_frame = ttk.LabelFrame(self.backends_frame.content_frame, text=self.translate("server_executable_path"))
        self.server_frame.pack(fill=X, expand=True, pady=5)

        # Backend selection
        backend_selection_frame = ttk.Frame(self.server_frame)
        backend_selection_frame.pack(fill=X, pady=5)
        ttk.Label(backend_selection_frame, text=self.translate("backend_selection")).pack(side=LEFT, padx=5)
        ttk.Radiobutton(backend_selection_frame, text=self.translate("backend_cpu"), 
                       variable=self.selected_backend, value="cpu").pack(side=LEFT, padx=5)
        ttk.Radiobutton(backend_selection_frame, text=self.translate("backend_vulkan"), 
                       variable=self.selected_backend, value="vulkan").pack(side=LEFT, padx=5)
        ttk.Radiobutton(backend_selection_frame, text=self.translate("backend_mixed"), 
                       variable=self.selected_backend, value="mixed").pack(side=LEFT, padx=5)

        # Paths for each backend - вирівняні поля
        backend_labels = {"cpu": "backend_label_cpu", "vulkan": "backend_label_vulkan", "mixed": "backend_label_mixed"}
        
        for backend in ["cpu", "vulkan", "mixed"]:
            frame = ttk.Frame(self.server_frame)
            frame.pack(fill=X, pady=2, padx=5)
            
            # Мітка фіксованої ширини
            label = ttk.Label(frame, text=self.translate(backend_labels[backend]), width=8, anchor="w")
            label.pack(side=LEFT, padx=(0, 5))
            self.backend_labels[backend] = label
            
            # Поле для шляху
            entry = ttk.Entry(frame, textvariable=self.server_paths[backend], state="readonly")
            entry.pack(side=LEFT, fill=X, expand=True, padx=5)
            self.backend_entries[backend] = entry
            
            # Кнопка огляду
            browse_btn = ttk.Button(frame, text=self.translate("browse_button"), 
                      command=lambda b=backend: self.browse_server_executable(b))
            browse_btn.pack(side=LEFT, padx=5)
            self.backend_browse_buttons[backend] = browse_btn
        
        # Роздільник 1
        ttk.Separator(parent, orient=HORIZONTAL).grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        
        # Рядок 2: Модель
        model_frame_outer = ttk.Frame(parent)
        model_frame_outer.grid(row=2, column=0, sticky="ew", padx=5, pady=(0, 10))
        self.model_frame = ttk.LabelFrame(model_frame_outer, text=self.translate("model_path"))
        self.model_frame.pack(fill=X, expand=True)
        self.model_path = tk.StringVar()
        ttk.Entry(self.model_frame, textvariable=self.model_path, state="readonly").pack(
            side=LEFT, fill=X, expand=True, padx=5, pady=5)
        self.browse_model_btn = ttk.Button(self.model_frame, text=self.translate("browse_button"), 
                                          command=self.browse_model)
        self.browse_model_btn.pack(side=LEFT, padx=5, pady=5)

        # Рядок 3: Notebook для налаштувань
        self.settings_notebook = ttk.Notebook(parent, bootstyle="secondary")
        self.settings_notebook.grid(row=3, column=0, sticky="ew", pady=(0, 10))

        self.tab_main_sampling = ttk.Frame(self.settings_notebook)
        self.tab_system = ttk.Frame(self.settings_notebook)
        
        self.settings_notebook.add(self.tab_main_sampling, text=self.translate("main_sampling_tab"))
        self.settings_notebook.add(self.tab_system, text=self.translate("system_tab"))
        
        # Заповнюємо вкладки
        self.populate_main_sampling_tab(self.tab_main_sampling)
        self.populate_system_tab(self.tab_system)

        # Роздільник 2
        ttk.Separator(parent, orient=HORIZONTAL).grid(row=4, column=0, sticky="ew", padx=5, pady=5)
        
        # Рядок 5: Кнопки керування
        control_frame = ttk.Frame(parent)
        control_frame.grid(row=5, column=0, sticky="ew", padx=5, pady=10)
        
        # Ліві кнопки
        left_buttons = ttk.Frame(control_frame)
        left_buttons.pack(side=LEFT)
        
        self.start_button = ttk.Button(left_buttons, text=self.translate("run_llama_button"), 
                                      command=self.start_llama_server, bootstyle=SUCCESS)
        self.start_button.pack(side=LEFT, padx=5)
        
        self.stop_button = ttk.Button(left_buttons, text=self.translate("stop_llama_button"), 
                                     state="disabled", command=self.stop_llama_server, bootstyle=DANGER)
        self.stop_button.pack(side=LEFT, padx=5)
        
        self.open_webui_button = ttk.Button(left_buttons, text=self.translate("open_webui_button"), 
                                           state="disabled", command=self.open_webui_in_browser, bootstyle=INFO)
        self.open_webui_button.pack(side=LEFT, padx=15)
        
        # Праві кнопки
        right_buttons = ttk.Frame(control_frame)
        right_buttons.pack(side=RIGHT)
        
        self.apply_preset_btn = ttk.Button(right_buttons, text=self.translate("apply_preset_button"), 
                                          command=self.apply_model_preset, bootstyle=PRIMARY)
        self.apply_preset_btn.pack(side=RIGHT, padx=5)
        
        self.reset_settings_btn = ttk.Button(right_buttons, text=self.translate("reset_settings_button"), 
                                            command=self.reset_settings, bootstyle=SECONDARY)
        self.reset_settings_btn.pack(side=RIGHT, padx=5)

        # Роздільник 3
        ttk.Separator(parent, orient=HORIZONTAL).grid(row=6, column=0, sticky="ew", padx=5, pady=(5, 0))
        
        # Рядок 7: Логи
        log_frame_outer = ttk.Frame(parent)
        log_frame_outer.grid(row=7, column=0, sticky="nsew", padx=5, pady=5)
        
        self.log_frame = ttk.LabelFrame(log_frame_outer, text=self.translate("llama_logs"))
        self.log_frame.pack(fill=BOTH, expand=True)
        
        self.llama_output_area = scrolledtext.ScrolledText(self.log_frame, wrap=tk.WORD, height=12)
        self.llama_output_area.pack(fill=BOTH, expand=True, padx=5, pady=5)
        self.llama_output_area.configure(state='disabled')

    def populate_main_sampling_tab(self, parent):
        # Основний контейнер з сіткою 1x3
        container = ttk.Frame(parent)
        container.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        # Налаштовуємо 3 рівні колонки
        container.grid_columnconfigure(0, weight=1, uniform="cols")
        container.grid_columnconfigure(1, weight=1, uniform="cols")
        container.grid_columnconfigure(2, weight=1, uniform="cols")
        
        # Ліва колонка: Ключовые параметры
        left_frame = ttk.LabelFrame(container, text=self.translate("key_params"))
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        
        # Середня колонка: Параметры генерации
        middle_frame = ttk.LabelFrame(container, text=self.translate("sampling_params"))
        middle_frame.grid(row=0, column=1, sticky="nsew", padx=5)
        
        # Права колонка: Прапорці
        right_frame = ttk.LabelFrame(container, text=self.translate("flags"))
        right_frame.grid(row=0, column=2, sticky="nsew", padx=(5, 0))
        
        # === Ліва колонка: Ключові параметри ===
        key_params = [
            ("port", "port"),
            ("ctx_size", "context"),
            ("n_gpu_layers", "gpu_layers"),
            ("threads", "cpu_threads"),
            ("batch_size", "batch_size")
        ]
        
        self.param_labels = {}
        for i, (key, text_key) in enumerate(key_params):
            frame = ttk.Frame(left_frame)
            frame.pack(fill=X, pady=3)
            
            label = ttk.Label(frame, text=self.translate(text_key), width=20, anchor="w")
            label.pack(side=LEFT)
            self.param_labels[key] = label
            
            entry = ttk.Entry(frame, textvariable=self.params[key], width=15)
            entry.pack(side=RIGHT)
        
        # Роздільник і продуктивність
        ttk.Separator(left_frame, orient=HORIZONTAL).pack(fill=X, pady=10)
        
        perf_frame = ttk.Frame(left_frame)
        perf_frame.pack(fill=X, pady=2)
        
        perf_label = ttk.Label(perf_frame, text=self.translate("performance"), font=("", 9, "bold"))
        perf_label.pack(anchor="w", pady=(0, 5))
        
        self.mlock_cb = ttk.Checkbutton(left_frame, text=self.translate("mlock"), 
                                       variable=self.flags["mlock"])
        self.mlock_cb.pack(anchor="w", padx=5, pady=2)
        
        # === Середня колонка: Параметри генерації ===
        sampling_params = [
            ("temp", "temperature"),
            ("top_k", "top_k"),
            ("top_p", "top_p"),
            ("repeat_penalty", "repeat_penalty")
        ]
        
        tooltips_uk = {
            "temp": "Контролює випадковість. (0.0-2.0)",
            "top_k": "Вибірка з K найймовірніших слів.",
            "top_p": "Вибірка з ядра слів із сукупною вірогідністю > P.",
            "repeat_penalty": "Штрафує модель за повторення токенів."
        }
        tooltips_ru = {
            "temp": "Контролирует случайность. (0.0-2.0)",
            "top_k": "Выборка из K наиболее вероятных слов.",
            "top_p": "Выборка из ядра слов с суммарной вер. > P.",
            "repeat_penalty": "Штрафует модель за повторение токенов."
        }
        tooltips_en = {
            "temp": "Controls randomness. (0.0-2.0)",
            "top_k": "Select from K most likely words.",
            "top_p": "Select from nucleus of words with cumulative prob > P.",
            "repeat_penalty": "Penalizes the model for repeating tokens."
        }
        
        self.sampling_labels = {}
        for i, (key, text_key) in enumerate(sampling_params):
            frame = ttk.Frame(middle_frame)
            frame.pack(fill=X, pady=3)
            
            label = ttk.Label(frame, text=self.translate(text_key), width=20, anchor="w")
            label.pack(side=LEFT)
            self.sampling_labels[key] = label
            
            if self.language.get() == 'uk':
                ToolTip(label, lambda k=key: tooltips_uk[k])
            elif self.language.get() == 'ru':
                ToolTip(label, lambda k=key: tooltips_ru[k])
            else:
                ToolTip(label, lambda k=key: tooltips_en[k])
            
            entry = ttk.Entry(frame, textvariable=self.sampling_params[key], width=15)
            entry.pack(side=RIGHT)
            
            if self.language.get() == 'uk':
                ToolTip(entry, lambda k=key: tooltips_uk[k])
            elif self.language.get() == 'ru':
                ToolTip(entry, lambda k=key: tooltips_ru[k])
            else:
                ToolTip(entry, lambda k=key: tooltips_en[k])
        
        # Роздільник і мережеві налаштування
        ttk.Separator(middle_frame, orient=HORIZONTAL).pack(fill=X, pady=10)
        
        net_frame = ttk.Frame(middle_frame)
        net_frame.pack(fill=X, pady=2)
        
        net_label = ttk.Label(net_frame, text=self.translate("network_settings"), font=("", 9, "bold"))
        net_label.pack(anchor="w", pady=(0, 5))
        
        net_tooltips_uk = {
            "host": "Адреса для запуску. '0.0.0.0' для доступу по мережі.",
            "api_key": "Bearer token для авторизації (необов'язково)."
        }
        net_tooltips_ru = {
            "host": "Адрес для запуска. '0.0.0.0' для доступа по сети.",
            "api_key": "Bearer token для авторизации (необязательно)."
        }
        net_tooltips_en = {
            "host": "Address to run on. '0.0.0.0' for network access.",
            "api_key": "Bearer token for authorization (optional)."
        }
        
        self.system_labels = {}
        for i, (key, text_key) in enumerate({"host": "host", "api_key": "api_key"}.items()):
            frame = ttk.Frame(middle_frame)
            frame.pack(fill=X, pady=3)
            
            label = ttk.Label(frame, text=self.translate(text_key), width=15, anchor="w")
            label.pack(side=LEFT)
            self.system_labels[key] = label
            
            if self.language.get() == 'uk':
                ToolTip(label, lambda k=key: net_tooltips_uk[k])
            elif self.language.get() == 'ru':
                ToolTip(label, lambda k=key: net_tooltips_ru[k])
            else:
                ToolTip(label, lambda k=key: net_tooltips_en[k])
            
            entry = ttk.Entry(frame, textvariable=self.system_params[key], width=20)
            entry.pack(side=RIGHT, padx=5)
            
            if self.language.get() == 'uk':
                ToolTip(entry, lambda k=key: net_tooltips_uk[k])
            elif self.language.get() == 'ru':
                ToolTip(entry, lambda k=key: net_tooltips_ru[k])
            else:
                ToolTip(entry, lambda k=key: net_tooltips_en[k])
        
        # === Права колонка: Прапорці ===
        flags_list = [
            ("jinja", "jinja_template"),
            ("no_warmup", "no_warmup"),
            ("embedding", "embedding_mode")
        ]
        
        flag_tooltips_uk = {
            "jinja": "Використовувати Jinja2 шаблони для форматування промптів",
            "no_warmup": "Вимкнути прогрів моделі при запуску",
            "embedding": "Режим створення ембеддингів"
        }
        flag_tooltips_ru = {
            "jinja": "Использовать Jinja2 шаблоны для форматирования промптов",
            "no_warmup": "Отключить прогрев модели при запуске",
            "embedding": "Режим создания эмбеддингов"
        }
        flag_tooltips_en = {
            "jinja": "Use Jinja2 templates for prompt formatting",
            "no_warmup": "Disable model warmup at startup",
            "embedding": "Embedding generation mode"
        }
        
        self.flag_cbs = {}
        for key, cb_text in flags_list:
            frame = ttk.Frame(right_frame)
            frame.pack(fill=X, pady=8, anchor="w")
            
            cb = ttk.Checkbutton(frame, text=self.translate(cb_text), variable=self.flags[key])
            cb.pack(side=LEFT, anchor="w")
            self.flag_cbs[key] = cb
            
            if self.language.get() == 'uk':
                ToolTip(cb, lambda k=key: flag_tooltips_uk[k])
            elif self.language.get() == 'ru':
                ToolTip(cb, lambda k=key: flag_tooltips_ru[k])
            else:
                ToolTip(cb, lambda k=key: flag_tooltips_en[k])
        
        # Вертикальні роздільники між колонками
        separator1 = ttk.Separator(container, orient=VERTICAL)
        separator1.place(in_=container, relx=0.33, rely=0.05, relheight=0.9, anchor='n')
        
        separator2 = ttk.Separator(container, orient=VERTICAL)
        separator2.place(in_=container, relx=0.66, rely=0.05, relheight=0.9, anchor='n')

    def populate_system_tab(self, parent):
        container = ttk.Frame(parent, padding=10)
        container.pack(fill=BOTH, expand=True)
        
        # Заголовок
        custom_label = ttk.Label(container, text=self.translate("custom_params"), 
                                font=("", 10, "bold"))
        custom_label.pack(anchor="w", pady=(0, 10))
        
        # Фрейм для двох колонок
        columns_frame = ttk.Frame(container)
        columns_frame.pack(fill=BOTH, expand=True)
        
        # Ліва колонка (параметри 1-6)
        left_column = ttk.LabelFrame(columns_frame, text=self.translate("custom_params_1_6"))
        left_column.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))
        
        # Права колонка (параметри 7-12)
        right_column = ttk.LabelFrame(columns_frame, text=self.translate("custom_params_7_12"))
        right_column.pack(side=RIGHT, fill=BOTH, expand=True)
        
        # Додаємо параметри (6 в кожній колонці)
        for i, (k_var, v_var) in enumerate(self.custom_params):
            if i < 6:
                column = left_column
                param_num = i + 1
            else:
                column = right_column
                param_num = i + 1
                
            frame = ttk.Frame(column)
            frame.pack(fill=X, pady=3)
            
            ttk.Label(frame, text=f"{param_num}:", width=3).pack(side=LEFT, padx=(0, 5))
            ttk.Entry(frame, textvariable=k_var, width=22).pack(side=LEFT, padx=5)
            ttk.Entry(frame, textvariable=v_var).pack(side=LEFT, fill=X, expand=True, padx=5)
        
        # Інформаційне повідомлення для слотів
        info_frame = ttk.Frame(container)
        info_frame.pack(fill=X, pady=(10, 5))
        self.info_custom_params_label = ttk.Label(info_frame, text=self.translate("info_custom_params"), font=("", 8), foreground="gray")
        self.info_custom_params_label.pack(anchor="w")

        # Новий блок: Сырые аргументы (Raw Args)
        raw_args_frame = ttk.LabelFrame(container, text=self.translate("raw_args"))
        raw_args_frame.pack(fill=X, pady=10)
        self.raw_args_label_frame = raw_args_frame # сохраним для перевода
        
        ttk.Entry(raw_args_frame, textvariable=self.raw_args).pack(fill=X, padx=5, pady=5)
        
        self.info_raw_args_label = ttk.Label(raw_args_frame, text=self.translate("info_raw_args"), font=("", 8), foreground="gray")
        self.info_raw_args_label.pack(anchor="w", padx=5, pady=(0, 5))

    def create_open_webui_tab(self, parent):
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.webui_control_frame = ttk.LabelFrame(parent, text=self.translate("webui_controls"))
        self.webui_control_frame.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        
        # Інформація про WebUI
        info_frame = ttk.Frame(self.webui_control_frame)
        info_frame.pack(fill=X, pady=(0, 10))
        
        info_text = ttk.Label(info_frame, text=self.translate("info_webui"), 
                             font=("", 8), foreground="gray")
        info_text.pack(anchor="w")
        
        # Кнопки керування WebUI
        buttons_frame = ttk.Frame(self.webui_control_frame)
        buttons_frame.pack(fill=X)
        
        self.webui_start_button = ttk.Button(buttons_frame, text=self.translate("run_webui_button"), 
                                            command=self.start_webui_server, bootstyle=SUCCESS)
        self.webui_start_button.pack(side=LEFT, padx=10, pady=10)
        
        self.webui_stop_button = ttk.Button(buttons_frame, text=self.translate("stop_webui_button"), 
                                           state="disabled", command=self.stop_webui_server, bootstyle=DANGER)
        self.webui_stop_button.pack(side=LEFT, padx=10, pady=10)
        
        # Логи WebUI
        self.webui_log_frame = ttk.LabelFrame(parent, text=self.translate("webui_logs"))
        self.webui_log_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=10)
        
        self.webui_output_area = scrolledtext.ScrolledText(self.webui_log_frame, wrap=tk.WORD)
        self.webui_output_area.pack(fill=BOTH, expand=True, padx=5, pady=5)
        self.webui_output_area.configure(state='disabled')

    def on_language_change(self):
        self.update_ui_text()
        self.save_app_config()

    def on_theme_change(self):
        theme = self.theme_var.get()
        self.style.theme_use(theme)
        self.apply_custom_theme_overrides()
        self.apply_theme_to_logs()
        self.save_app_config()

    def apply_theme_to_logs(self):
        """Applies appropriate log colors based on the current theme."""
        theme_name = self.style.theme.name
        
        if theme_name == "neural_core":
            log_colors = {'bg': '#05080c', 'fg': '#00f0ff'} # Cyberpunk terminal look
            font_style = ("Consolas", 10)
        elif self.style.theme.type == 'dark':
            log_colors = {'bg': '#2b2b2b', 'fg': '#d3d3d3'}
            font_style = ("Consolas", 10)
        else:
            log_colors = {'bg': '#ffffff', 'fg': '#333333'}
            font_style = ("Consolas", 10)
            
        self.llama_output_area.config(background=log_colors['bg'], foreground=log_colors['fg'], font=font_style)
        self.webui_output_area.config(background=log_colors['bg'], foreground=log_colors['fg'], font=font_style)
        
        # Обновляем цвет иконок статуса
        is_llama_running = self.processes["llama"] is not None
        is_webui_running = self.processes["webui"] is not None
        
        self.llama_status_icon.config(
            foreground=self.style.colors.success if is_llama_running else self.style.colors.danger
        )
        self.webui_status_icon.config(
            foreground=self.style.colors.success if is_webui_running else self.style.colors.danger
        )

    def update_ui_text(self):
        self.title(self.translate("app_title"))
        
        # Оновлення меню
        self.menu_bar.entryconfigure(0, label=self.translate("file_menu"))
        self.file_menu.entryconfigure(0, label=self.translate("exit_menu"))
        self.menu_bar.entryconfigure(1, label=self.translate("settings_menu"))
        
        # Оновлення підменю налаштувань
        self.settings_menu.entryconfigure(0, label=self.translate("language_menu"))
        self.settings_menu.entryconfigure(1, label=self.translate("theme_menu"))
        
        # Оновлення тем у підменю
        for i, theme_key in enumerate(["theme_neural", "theme_darkly", "theme_litera", "theme_superhero"]):
            self.theme_menu.entryconfigure(i, label=self.translate(theme_key))
        
        # Оновлення меню допомоги
        self.menu_bar.entryconfigure(2, label=self.translate("help_menu"))
        self.help_menu.entryconfigure(0, label=self.translate("about_menu"))
        
        # Оновлення вкладок
        self.main_notebook.tab(0, text=self.translate("llama_tab"))
        self.main_notebook.tab(1, text=self.translate("webui_tab"))
        
        # Оновлення фрейму бекендів
        self.server_frame.config(text=self.translate("server_executable_path"))
        
        # Оновлення тексту згортаємого фрейму
        if self.backends_frame.show.get():
            self.backends_frame.toggle_text.set(self.translate("toggle_backends_hide"))
        else:
            self.backends_frame.toggle_text.set(self.translate("toggle_backends"))
        
        # Оновлення міток бекендів
        backend_labels_map = {"cpu": "backend_label_cpu", "vulkan": "backend_label_vulkan", "mixed": "backend_label_mixed"}
        for backend, label_widget in self.backend_labels.items():
            if backend in backend_labels_map:
                label_widget.config(text=self.translate(backend_labels_map[backend]))
        
        # Оновлення кнопок огляду бекендів
        for btn in self.backend_browse_buttons.values():
            btn.config(text=self.translate("browse_button"))
        
        # Оновлення фрейму моделі
        self.model_frame.config(text=self.translate("model_path"))
        self.browse_model_btn.config(text=self.translate("browse_button"))
        
        # Оновлення вкладок налаштувань
        self.settings_notebook.tab(0, text=self.translate("main_sampling_tab"))
        self.settings_notebook.tab(1, text=self.translate("system_tab"))
        
        # Оновлення заголовків колонок на вкладці "Основні та Генерація"
        for child in self.tab_main_sampling.winfo_children():
            if isinstance(child, ttk.Frame):  # Це container
                for subchild in child.winfo_children():
                    if isinstance(subchild, ttk.LabelFrame):
                        text = subchild.cget("text")
                        if text in [self.translate("key_params"), "Key Parameters", "Ключевые параметры"]:
                            subchild.config(text=self.translate("key_params"))
                        elif text in [self.translate("sampling_params"), "Text Generation Parameters", "Параметры генерации текста"]:
                            subchild.config(text=self.translate("sampling_params"))
                        elif text in [self.translate("flags"), "Flags", "Флаги"]:
                            subchild.config(text=self.translate("flags"))
        
        # Оновлення міток параметрів
        key_params_map = {
            "port": "port", "ctx_size": "context", "n_gpu_layers": "gpu_layers",
            "threads": "cpu_threads", "batch_size": "batch_size"
        }
        for key, label in self.param_labels.items():
            if key in key_params_map:
                label.config(text=self.translate(key_params_map[key]))
        
        # Оновлення міток параметрів генерации
        sampling_map = {
            "temp": "temperature", "top_k": "top_k", 
            "top_p": "top_p", "repeat_penalty": "repeat_penalty"
        }
        for key, label in self.sampling_labels.items():
            if key in sampling_map:
                label.config(text=self.translate(sampling_map[key]))
        
        # Оновлення міток мережевих налаштувань
        system_map = {"host": "host", "api_key": "api_key"}
        for key, label in self.system_labels.items():
            if key in system_map:
                label.config(text=self.translate(system_map[key]))
        
        # Оновлення прапорців
        flags_map = {
            "jinja": "jinja_template", 
            "no_warmup": "no_warmup", 
            "embedding": "embedding_mode"
        }
        for key, cb in self.flag_cbs.items():
            if key in flags_map:
                cb.config(text=self.translate(flags_map[key]))
        
        # Оновлення mlock
        self.mlock_cb.config(text=self.translate("mlock"))
        
        # Оновлення кнопок
        self.start_button.config(text=self.translate("run_llama_button"))
        self.stop_button.config(text=self.translate("stop_llama_button"))
        self.open_webui_button.config(text=self.translate("open_webui_button"))
        self.reset_settings_btn.config(text=self.translate("reset_settings_button"))
        self.apply_preset_btn.config(text=self.translate("apply_preset_button"))
        self.log_frame.config(text=self.translate("llama_logs"))
        
        # Оновлення WebUI вкладки
        self.webui_control_frame.config(text=self.translate("webui_controls"))
        self.webui_start_button.config(text=self.translate("run_webui_button"))
        self.webui_stop_button.config(text=self.translate("stop_webui_button"))
        self.webui_log_frame.config(text=self.translate("webui_logs"))
        
        # Оновлення заголовків на вкладці "Система та Мережа"
        for child in self.tab_system.winfo_children():
            if isinstance(child, ttk.Frame):
                for subchild in child.winfo_children():
                    if isinstance(subchild, ttk.LabelFrame):
                        text = subchild.cget("text")
                        if text in [self.translate("custom_params_1_6"), "Parameters 1-6", "Параметры 1-6"]:
                            subchild.config(text=self.translate("custom_params_1_6"))
                        elif text in [self.translate("custom_params_7_12"), "Parameters 7-12", "Параметры 7-12"]:
                            subchild.config(text=self.translate("custom_params_7_12"))
                        
        if hasattr(self, 'info_custom_params_label'):
            self.info_custom_params_label.config(text=self.translate("info_custom_params"))
        if hasattr(self, 'raw_args_label_frame'):
            self.raw_args_label_frame.config(text=self.translate("raw_args"))
        if hasattr(self, 'info_raw_args_label'):
            self.info_raw_args_label.config(text=self.translate("info_raw_args"))
        
        # Оновлення статус-бара
        self.update_status("llama", self.processes["llama"] is not None)
        self.update_status("webui", self.processes["webui"] is not None)

    def show_about(self):
        messagebox.showinfo(self.translate("about_title"), self.translate("about_text"))

    def apply_model_preset(self):
        filename = os.path.basename(self.model_path.get()).lower()
        if not filename: 
            return
        
        presets = {
            "chat": {"temp": "0.7", "top_k": "50", "top_p": "0.9"},
            "instruct": {"temp": "0.2", "top_k": "40", "top_p": "0.95"},
            "code": {"temp": "0.1", "top_k": "10", "top_p": "0.95", "repeat_penalty": "1.0"},
            "story": {"temp": "0.9", "top_k": "0", "top_p": "0.9", "repeat_penalty": "1.15"},
            "creative": {"temp": "1.0", "top_k": "0", "top_p": "0.9", "repeat_penalty": "1.15"}
        }
        
        applied_preset = None
        for key, values in presets.items():
            if key in filename:
                for p_key, p_val in values.items():
                    self.sampling_params[p_key].set(p_val)
                applied_preset = key
                break
        
        if applied_preset:
            self.log_llama_message(self.translate("preset_applied").format(preset=applied_preset))
        else:
            self.log_llama_message(self.translate("preset_not_found"))
    
    def reset_settings(self):
        for key, value in self.defaults["params"].items(): 
            self.params[key].set(value)
        for key, value in self.defaults["sampling_params"].items(): 
            self.sampling_params[key].set(value)
        for key, value in self.defaults["system_params"].items(): 
            self.system_params[key].set(value)
        for key, value in self.defaults["flags"].items(): 
            self.flags[key].set(value)
        for i in range(len(self.custom_params)): 
            self.custom_params[i][0].set("")
            self.custom_params[i][1].set("")
        self.raw_args.set("")
        self.log_llama_message(self.translate("settings_reset"))
    
    def open_webui_in_browser(self):
        host = self.system_params['host'].get().strip()
        port = self.params['port'].get().strip()
        display_host = "127.0.0.1" if host == "0.0.0.0" else host
        webbrowser.open(f"http://{display_host}:{port}")
    
    def build_llama_command(self):
        backend = self.selected_backend.get()
        server_exec = self.server_paths[backend].get()
        model_path_val = self.model_path.get()
        
        if not (server_exec and os.path.exists(server_exec)):
            self.log_llama_message(self.translate("error_executable_not_found"))
            return None
        
        if not (model_path_val and os.path.exists(model_path_val)):
            self.log_llama_message(self.translate("error_model_not_found"))
            return None
        
        command = [server_exec, "-m", model_path_val]
        all_params = {**self.params, **self.sampling_params, **self.system_params}
        param_mapping = {
            "ctx_size": "ctx-size", 
            "n_gpu_layers": "n-gpu-layers", 
            "repeat_penalty": "repeat-penalty", 
            "api_key": "api-key"
        }
        
        for key, var in all_params.items():
            if value := var.get().strip():
                command.extend([f"--{param_mapping.get(key, key)}", value])
        
        for key, var in self.flags.items():
            if var.get():
                command.append(f"--{key.replace('_', '-')}")
        
        for key_var, val_var in self.custom_params:
            key = key_var.get().strip()
            val = val_var.get().strip()
            if key:
                command.append(f"--{key}")
                if val:
                    command.append(val)
                    
        raw_str = self.raw_args.get().strip()
        if raw_str:
            try:
                # shlex правильно разобьет строку, даже если там есть кавычки или пробелы внутри значений
                command.extend(shlex.split(raw_str))
            except ValueError:
                # Fallback, если shlex не смог распарсить строку
                command.extend(raw_str.split())
        
        return command
    
    def start_llama_server(self): 
        self.start_process("llama", self.build_llama_command)
    
    def stop_llama_server(self): 
        self.stop_process("llama")
    
    def start_webui_server(self): 
        self.start_process("webui", lambda: ["open-webui", "serve"])
    
    def stop_webui_server(self): 
        self.stop_process("webui")
    
    def start_process(self, p_type, command_builder):
        if not (command := command_builder()): 
            return
        
        if p_type == "llama": 
            self.save_settings()
        
        self.log_message(p_type, self.translate("starting_server").format(p_type=p_type.upper()))
        self.log_message(p_type, self.translate("command") + " ".join(f'"{c}"' if " " in c else c for c in command))
        
        try:
            env = os.environ.copy()
            if p_type == 'webui': 
                env["PYTHONIOENCODING"] = "utf-8"
            
            self.processes[p_type] = subprocess.Popen(
                command, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.STDOUT, 
                text=True,
                encoding='utf-8', 
                errors='replace',
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0,
                shell=(p_type == 'webui' and os.name == 'nt'), 
                env=env
            )
            
            threading.Thread(target=self.read_output, args=(p_type,), daemon=True).start()
            self.update_ui_state(p_type, is_running=True)
        
        except Exception as e:
            self.log_message(p_type, self.translate("error_starting") + str(e))
    
    def stop_process(self, p_type):
        if process := self.processes[p_type]:
            self.log_message(p_type, self.translate("stopping_server").format(p_type=p_type.upper()))
            
            process.terminate()
            try: 
                process.wait(timeout=3)
            except subprocess.TimeoutExpired: 
                process.kill()
            
            self.processes[p_type] = None
            self.update_ui_state(p_type, is_running=False)
    
    def read_output(self, p_type):
        if process := self.processes[p_type]:
            for line in iter(process.stdout.readline, ''): 
                self.after(0, self.log_message, p_type, line.strip())
            process.stdout.close()
    
    def log_message(self, p_type, message):
        area = self.llama_output_area if p_type == 'llama' else self.webui_output_area
        area.configure(state='normal')
        area.insert(tk.END, message + "\n")
        area.see(tk.END)
        area.configure(state='disabled')
    
    def log_llama_message(self, message): 
        self.log_message("llama", message)
    
    def update_ui_state(self, p_type, is_running):
        if p_type == "llama":
            self.start_button.config(state="disabled" if is_running else "normal")
            self.stop_button.config(state="normal" if is_running else "disabled")
            self.open_webui_button.config(state="normal" if is_running else "disabled")
        elif p_type == "webui":
            self.webui_start_button.config(state="disabled" if is_running else "normal")
            self.webui_stop_button.config(state="normal" if is_running else "disabled")
        
        self.update_status(p_type, is_running)
    
    def update_status(self, p_type, is_running):
        status_var = self.llama_status_var if p_type == 'llama' else self.webui_status_var
        status_key = 'status_running' if is_running else 'status_stopped'
        status_text = self.translate(status_key)
        prefix = self.translate(f'status_{p_type}')
        status_var.set(f"{prefix}: {status_text}")
        
        # Оновлення іконок статусу
        color = self.style.colors.success if is_running else self.style.colors.danger
        if p_type == "llama":
            self.llama_status_icon.config(foreground=color)
        else:
            self.webui_status_icon.config(foreground=color)
    
    def browse_server_executable(self, backend):
        title = self.translate("select_server_exe")
        filepath = filedialog.askopenfilename(
            title=title,
            filetypes=[("Executable files", "*.exe"), ("All files", "*.*")]
        )
        if filepath: 
            self.server_paths[backend].set(filepath)
    
    def browse_model(self):
        title = self.translate("select_gguf_model")
        filepath = filedialog.askopenfilename(
            title=title, 
            filetypes=[("GGUF files", "*.gguf"), ("All files", "*.*")]
        )
        if filepath: 
            self.model_path.set(filepath)
            self.load_settings_for_model(filepath)
    
    def save_app_config(self):
        try:
            with open(self.settings_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
        except (IOError, json.JSONDecodeError):
            config = {}
        
        config['app_language'] = self.language.get()
        config['app_theme'] = self.theme_var.get()
        
        with open(self.settings_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4)
    
    def save_settings(self):
        model_path = self.model_path.get()
        if not model_path: 
            return
        
        try:
            with open(self.settings_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
        except (IOError, json.JSONDecodeError):
            config = {}
        
        config[model_path] = {
            "params": {k: v.get() for k, v in self.params.items()},
            "sampling_params": {k: v.get() for k, v in self.sampling_params.items()},
            "system_params": {k: v.get() for k, v in self.system_params.items()},
            "flags": {k: v.get() for k, v in self.flags.items()},
            "custom_params": [(k.get(), v.get()) for k, v in self.custom_params],
            "raw_args": self.raw_args.get(),
            "selected_backend": self.selected_backend.get()
        }
        
        config["last_model_path"] = model_path
        config["server_paths"] = {k: v.get() for k, v in self.server_paths.items()}
        
        with open(self.settings_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        
        self.log_llama_message(self.translate("settings_saved").format(model=os.path.basename(model_path)))
    
    def load_settings_for_model(self, model_path):
        self.reset_settings()
        
        try:
            with open(self.settings_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            settings = config.get(model_path)
            if settings:
                # Завантажуємо основні параметри
                for group, group_vars in {
                    "params": self.params, 
                    "sampling_params": self.sampling_params, 
                    "system_params": self.system_params, 
                    "flags": self.flags
                }.items():
                    if group in settings:
                        for key, var in group_vars.items():
                            if key in settings[group]:
                                var.set(settings[group][key])
                
                # Завантажуємо додаткові параметри
                if "custom_params" in settings:
                    for i, (k, v) in enumerate(settings["custom_params"]):
                        if i < len(self.custom_params):
                            self.custom_params[i][0].set(k)
                            self.custom_params[i][1].set(v)
                            
                # Завантажуємо сырые аргументы
                if "raw_args" in settings:
                    self.raw_args.set(settings["raw_args"])
                
                # Завантажуємо вибраний бекенд
                if "selected_backend" in settings:
                    self.selected_backend.set(settings["selected_backend"])
                
                self.log_llama_message(self.translate("settings_loaded").format(model=os.path.basename(model_path)))
            else:
                self.log_llama_message(self.translate("default_settings_used").format(model=os.path.basename(model_path)))
        
        except (IOError, json.JSONDecodeError):
            self.log_llama_message(self.translate("default_settings_used").format(model=os.path.basename(model_path)))
    
    def load_initial_settings(self):
        try:
            with open(self.settings_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            # Завантажуємо шляхи до серверів
            server_paths = config.get("server_paths", {})
            for backend, path in server_paths.items():
                if backend in self.server_paths:
                    self.server_paths[backend].set(path)
            
            # Завантажуємо останню модель
            if last_model := config.get("last_model_path", ""):
                if os.path.exists(last_model):
                    self.model_path.set(last_model)
                    self.load_settings_for_model(last_model)
        
        except (IOError, json.JSONDecodeError):
            pass
    
    def on_closing(self):
        if self.processes["llama"]: 
            self.stop_process("llama")
        if self.processes["webui"]: 
            self.stop_process("webui")
        self.destroy()

if __name__ == "__main__":
    app = LlamaCppGUI()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
