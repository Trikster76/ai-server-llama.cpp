# 🧠 Neural Core: AI Server Launcher

**Prestige v3.2 — Advanced GUI for managing llama.cpp and Open WebUI servers**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![ttkbootstrap](https://img.shields.io/badge/ttkbootstrap-1.6%2B-purple)](https://github.com/israel-dryer/ttkbootstrap)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

[English](#english) | [Русский](#русский) | [Українська](#українська)

---

## English

### Overview

**Neural Core: AI Server Launcher** is a powerful desktop GUI application for managing local AI inference infrastructure. It provides a clean, feature-rich interface for running and configuring:

- **llama.cpp Server** — high-performance local LLM inference engine (CPU/Vulkan/Mixed backends)
- **Open WebUI** — modern web chat interface that connects to the llama.cpp API

All settings are saved per-model, so switching between models restores their individual configurations automatically.

---

### ✨ Features

#### 🖥️ Interface & Themes
- **4 UI themes**: Neural Core (Cyberpunk — default), Dark (Darkly), Light (Litera), High Contrast (Superhero)
- **3 interface languages**: Russian, Ukrainian, English — switchable at runtime from the Settings menu
- Monospace log terminal with theme-matched colors (cyan-on-black in Neural Core)

#### ⚙️ Backend Selection
- Switch between **CPU**, **Vulkan**, and **Mixed** llama.cpp backends via radio buttons
- Each backend stores its own path to `server.exe` — all three can be configured simultaneously
- Backend panel is **collapsible** to save screen space

#### 📋 llama.cpp Configuration (Main & Generation tab)
**Key Parameters:**
| Parameter | Description | Default |
|-----------|-------------|---------|
| Port | Listening port | 8080 |
| Context | Context window size (tokens) | 4096 |
| GPU Layers | Layers to offload to GPU (-1 = all) | -1 |
| CPU Threads | Parallel CPU threads | 8 |
| Batch Size | Prompt processing batch | 512 |

**Sampling / Generation Parameters** (with tooltips):
| Parameter | Description | Default |
|-----------|-------------|---------|
| Temperature | Response randomness (0.0–2.0) | 0.7 |
| Top-K | Top K token selection | 40 |
| Top-P | Nucleus sampling threshold | 0.95 |
| Repeat Penalty | Penalty for token repetition | 1.1 |

**Flags:**
- ✅ Jinja Template — use Jinja2 prompt formatting
- ✅ No Warmup — skip model warmup at startup
- ☐ Embedding Mode — enable embedding generation endpoint

**Network & Performance:**
- Host (default: `127.0.0.1`, use `0.0.0.0` for LAN access)
- API Key (optional Bearer token authentication)
- Lock model in RAM (`--mlock`)

#### 🔧 System & Network tab — Advanced Parameters
- **12 custom parameter slots** (split into 2 columns of 6): enter any llama.cpp flag name + value
- **Raw Args field**: paste any additional flags as a raw string (e.g. `--kv-unified --cache-idle-slots`), parsed via `shlex` for correct handling of spaces and quotes

#### 🧠 Model Presets
Click **"Apply Model Preset"** to auto-configure sampling parameters based on the model filename:

| Keyword in filename | Temperature | Top-K | Top-P | Repeat Penalty |
|---------------------|-------------|-------|-------|----------------|
| `chat` | 0.7 | 50 | 0.9 | — |
| `instruct` | 0.2 | 40 | 0.95 | — |
| `code` | 0.1 | 10 | 0.95 | 1.0 |
| `story` | 0.9 | 0 | 0.9 | 1.15 |
| `creative` | 1.0 | 0 | 0.9 | 1.15 |

#### 💾 Per-Model Settings
- Settings are **automatically saved** when starting the server
- On model file selection, stored settings are **automatically restored**
- "Reset Settings" resets all parameters to factory defaults

#### 📊 Real-time Logs
- Separate scrollable log terminal for llama.cpp and Open WebUI output
- Color-coded status indicators in the status bar (🟢 running / 🔴 stopped)
- "Open Web UI" button opens the server URL in the browser (active only when server is running)

#### 🌐 Open WebUI Tab
- Launch and stop `open-webui serve` process directly from the GUI
- Separate log panel for Open WebUI output

---

### 📋 Screenshots

#### System & Network Tab
![System tab](https://github.com/user-attachments/assets/25c27368-fed0-4310-a91e-9e52466320ac)

#### Main & Generation Tab
![Main tab](https://github.com/user-attachments/assets/8c95295d-c0be-4165-a3b0-a564e6ad4cf0)

---

### 🔧 Requirements

- **Python**: 3.10 or higher (tested on 3.13)
- **OS**: Windows (primary), macOS, Linux
- **RAM**: 8 GB minimum (16 GB+ recommended for large models)
- **VRAM**: 2 GB minimum for GPU acceleration
- **llama.cpp**: [latest release](https://github.com/ggerganov/llama.cpp/releases) — choose build matching your backend (CPU / Vulkan)

### 📦 Dependencies

```
ttkbootstrap >= 1.6.0
```

`tkinter`, `subprocess`, `threading`, `shlex`, `json`, `os`, `webbrowser` — all from Python standard library.

---

### 🚀 Quick Start

```bash
# 1. Clone
git clone https://github.com/Trikster76/ai-server-llama.cpp.git
cd ai-server-llama.cpp

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python AI-Server-Launcher.py
```

#### First Run Checklist
1. Click **"▸ Show Backends"** to expand the backend panel
2. Select your backend (CPU / Vulkan / Mixed) and click **"Browse..."** to set `server.exe` path
3. Click **"Browse..."** next to **Model** to select your `.gguf` file
4. In **Main & Generation** tab: set port, context size, GPU layers
5. Optionally click **"Apply Model Preset"** to auto-fill sampling parameters
6. Click **"Run Llama.cpp"** — the server starts and logs appear below
7. Click **"Open Web UI"** to open the API in your browser

---

### 🌐 API Usage

Once the server is running:

```bash
# Chat completions
curl -X POST http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"default","messages":[{"role":"user","content":"Hello!"}]}'

# Embeddings (requires Embedding Mode flag)
curl -X POST http://127.0.0.1:8080/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{"input":"Your text here","model":"default"}'
```

---

### 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Executable not found" | Make sure the correct `server.exe` is selected for the active backend |
| Server crashes on start | Reduce Context size or GPU Layers; check VRAM availability |
| Poor GPU performance | Set GPU Layers to `-1`; update GPU drivers |
| Open WebUI won't connect | Verify port; check that `open-webui` is installed (`pip install open-webui`) |
| Settings not saving | Check write permissions in the app directory |

---

### 📖 Documentation

- [FEATURES.md](docs/FEATURES.md) — detailed feature list
- [INSTALL.md](docs/INSTALL.md) — advanced installation
- [API.md](docs/API.md) — API reference
- [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) — extended troubleshooting
- [CHANGELOG.md](CHANGELOG.md) — version history

---

### 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork → feature branch → PR
2. Keep translations in sync across all 3 languages
3. Test on both dark and light themes

### 📝 License

MIT License — see [LICENSE](LICENSE)

### 🙏 Credits

- [llama.cpp](https://github.com/ggerganov/llama.cpp)
- [Open WebUI](https://github.com/open-webui/open-webui)
- [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap)

---

## Русский

### Описание

**Neural Core: AI Server Launcher** (Prestige v3.2) — настольное приложение с графическим интерфейсом для управления локальными AI-серверами:

- **llama.cpp** — движок вывода LLM (бэкенды CPU / Vulkan / Mixed)
- **Open WebUI** — веб-чат интерфейс поверх API llama.cpp

Настройки сохраняются **отдельно для каждой модели** и восстанавливаются автоматически при её выборе.

---

### ✨ Возможности

#### 🖥️ Интерфейс и темы
- **4 темы оформления**: Neural Core (Cyberpunk, по умолчанию), Тёмная (Darkly), Светлая (Litera), Контрастная (Superhero)
- **3 языка интерфейса**: Русский, Украинский, English — переключаются в меню «Настройки» без перезапуска
- Терминал логов с шрифтом Consolas и цветовой схемой под активную тему

#### ⚙️ Выбор бэкенда
- Переключение между **CPU**, **Vulkan** и **Mixed** бэкендами llama.cpp через радиокнопки
- Каждый бэкенд хранит свой путь к `server.exe` — все три можно настроить одновременно
- Панель бэкендов **сворачивается** кнопкой «▸ Показать бэкенды»

#### 📋 Вкладка «Основные и Генерация»
**Ключевые параметры:**
| Параметр | Описание | По умолчанию |
|----------|----------|--------------|
| Порт | Порт прослушивания сервера | 8080 |
| Контекст | Размер контекстного окна (токены) | 4096 |
| Слои ГПУ | Слои на GPU (-1 = все) | -1 |
| Потоки ЦПУ | Параллельные потоки CPU | 8 |
| Размер батча | Батч обработки промпта | 512 |

**Параметры генерации** (с всплывающими подсказками):
| Параметр | Описание | По умолчанию |
|----------|----------|--------------|
| Температура | Случайность (0.0–2.0) | 0.7 |
| Top-K | Выборка из K лучших токенов | 40 |
| Top-P | Ядерная выборка | 0.95 |
| Штраф за повторения | Пенальти за повтор токенов | 1.1 |

**Флаги** (чекбоксы):
- Jinja Template — использовать Jinja2 шаблоны промптов
- Без прогрева (no-warmup) — отключить прогрев модели
- Embedding Mode — режим генерации эмбеддингов

**Сетевые настройки и производительность:**
- Хост (по умолчанию `127.0.0.1`, `0.0.0.0` для доступа по сети)
- Ключ API (Bearer-токен, необязательно)
- Блокировать в ОЗУ (`--mlock`)

#### 🔧 Вкладка «Система и Сеть»
- **12 слотов для кастомных параметров** (два столбца по 6): имя флага + значение в произвольном формате
- **Поле Raw Args**: ввод любых дополнительных флагов строкой (например: `--kv-unified --cache-idle-slots`), парсится через `shlex`

#### 🧠 Пресеты моделей
Кнопка **«Применить пресет модели»** автоматически настраивает параметры генерации по ключевому слову в имени файла модели:

| Ключевое слово | Температура | Top-K | Top-P | Штраф |
|----------------|-------------|-------|-------|-------|
| `chat` | 0.7 | 50 | 0.9 | — |
| `instruct` | 0.2 | 40 | 0.95 | — |
| `code` | 0.1 | 10 | 0.95 | 1.0 |
| `story` | 0.9 | 0 | 0.9 | 1.15 |
| `creative` | 1.0 | 0 | 0.9 | 1.15 |

#### 💾 Настройки per-model
- Настройки **автоматически сохраняются** при запуске сервера
- При выборе файла модели настройки **автоматически восстанавливаются**
- Кнопка «Сбросить настройки» возвращает все значения к заводским

#### 📊 Логи и статус
- Отдельные прокручиваемые логи для llama.cpp и Open WebUI
- Цветные индикаторы статуса в статус-баре (🟢 запущен / 🔴 остановлен)
- Кнопка «Открыть Web UI» открывает адрес сервера в браузере (активна только когда сервер работает)

---

### 🔧 Требования

- **Python**: 3.10+ (протестировано на 3.13)
- **ОС**: Windows (основная), macOS, Linux
- **ОЗУ**: минимум 8 ГБ (рекомендуется 16 ГБ+)
- **VRAM**: от 2 ГБ для GPU-ускорения
- **llama.cpp**: [последний релиз](https://github.com/ggerganov/llama.cpp/releases)

### 📦 Зависимости

```
ttkbootstrap >= 1.6.0
```

---

### 🚀 Быстрый старт

```bash
git clone https://github.com/Trikster76/ai-server-llama.cpp.git
cd ai-server-llama.cpp
pip install -r requirements.txt
python AI-Server-Launcher.py
```

#### Первый запуск
1. Нажмите **«▸ Показать бэкенды»**, выберите бэкенд и укажите путь к `server.exe`
2. Нажмите **«Обзор...»** рядом с «Модель» и выберите `.gguf` файл
3. Настройте параметры во вкладке **«Основные и Генерация»**
4. Нажмите **«Применить пресет модели»** при необходимости
5. Нажмите **«Запустить Llama.cpp»** — сервер запустится, логи появятся ниже
6. Нажмите **«Открыть Web UI»** для доступа к API в браузере

---

### 🌐 Использование API

```bash
curl -X POST http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"default","messages":[{"role":"user","content":"Привет!"}]}'
```

---

### 🐛 Решение проблем

| Проблема | Решение |
|----------|---------|
| «Исполняемый файл не найден» | Убедитесь, что выбран правильный `server.exe` для активного бэкенда |
| Сервер падает при запуске | Уменьшите Контекст или Слои ГПУ; проверьте объём VRAM |
| Плохая производительность GPU | Установите Слои ГПУ = `-1`; обновите драйверы |
| Open WebUI не подключается | Проверьте порт; убедитесь что `open-webui` установлен |
| Настройки не сохраняются | Проверьте права на запись в папку с программой |

---

### 📖 Документация

- [FEATURES.md](docs/FEATURES.md), [INSTALL.md](docs/INSTALL.md), [API.md](docs/API.md), [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)
- [CHANGELOG.md](CHANGELOG.md)

---

## Українська

### Опис

**Neural Core: AI Server Launcher** (Prestige v3.2) — настільний застосунок з графічним інтерфейсом для керування локальними AI-серверами:

- **llama.cpp** — двигун виводу LLM (бекенди CPU / Vulkan / Mixed)
- **Open WebUI** — веб-чат інтерфейс поверх API llama.cpp

Налаштування зберігаються **окремо для кожної моделі** і відновлюються автоматично при її виборі.

---

### ✨ Можливості

- **4 теми оформлення**: Neural Core (Cyberpunk), Темна, Світла, Контрастна
- **3 мови інтерфейсу**: Українська, Русский, English — перемикаються без перезапуску
- Вибір бекенду: **CPU / Vulkan / Mixed** — кожен зберігає свій шлях до `server.exe`
- **12 слотів** для кастомних параметрів + поле **Raw Args** для довільних прапорців
- Пресети моделей: chat, instruct, code, story, creative
- Збереження налаштувань per-model + кнопка скидання
- Логи llama.cpp і Open WebUI в реальному часі
- Керування Open WebUI (запуск/зупинка) з окремої вкладки

---

### 🚀 Швидкий старт

```bash
git clone https://github.com/Trikster76/ai-server-llama.cpp.git
cd ai-server-llama.cpp
pip install -r requirements.txt
python AI-Server-Launcher.py
```

---

**Made with ❤️ by [Trikster76](https://github.com/Trikster76)**
