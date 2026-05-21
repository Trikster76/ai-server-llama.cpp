# 🧠 Neural Core: AI Server Launcher

**Prestige v3.2** — *An advanced, sovereign GUI for managing local LLM deployments.*

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![ttkbootstrap](https://img.shields.io/badge/ttkbootstrap-1.6%2B-purple)](https://github.com/israel-dryer/ttkbootstrap)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

[English](#english) | [Русский](#русский)

---

## English

### Overview

**Neural Core: AI Server Launcher** is a powerful, sovereign desktop orchestrator designed to streamline local AI inference. It provides a clean graphical control center for running and configuring **llama.cpp** and **Open WebUI** without the need to manually compose long command-line arguments.

Built for users who prioritize **data autonomy**, **local execution**, and **hardware flexibility**, Neural Core gives direct control over the inference stack through a polished cyberpunk-inspired interface.

### ✨ Core Features

#### 🖥️ Interface & Aesthetics
- **4 UI themes**: Neural Core (Cyberpunk — default), Dark (Darkly), Light (Litera), High Contrast (Superhero)
- **2 interface languages**: English and Russian
- Integrated monospace log terminal with theme-matched colors

#### ⚙️ Smart Backend Routing
- Switch between **CPU**, **Vulkan**, and **Mixed** backends
- Store a separate `server.exe` path for each backend
- Use a collapsible backend panel to save screen space

#### 📋 Granular llama.cpp Configuration
**Key parameters:**

| Parameter | Description | Default |
|-----------|-------------|---------|
| Port | API listening port | 8080 |
| Context | Context window size in tokens | 4096 |
| GPU Layers | Layers offloaded to VRAM (`-1` = maximum) | -1 |
| CPU Threads | Parallel CPU thread allocation | 8 |
| Batch Size | Prompt processing batch size | 512 |

**Sampling parameters:**

| Parameter | Description | Default |
|-----------|-------------|---------|
| Temperature | Response randomness / creativity | 0.7 |
| Top-K | Top-K token selection limit | 40 |
| Top-P | Nucleus sampling threshold | 0.95 |
| Repeat Penalty | Token repetition penalty | 1.1 |

**Behavior flags:**
- `Jinja Template`
- `No Warmup`
- `Embedding Mode`

**Network and memory settings:**
- Host binding (`127.0.0.1` or `0.0.0.0`)
- Optional API key
- Memory locking via `--mlock`

#### 🔧 Advanced Customization
- **12 manual parameter slots**
- **Raw Args** field for direct custom `llama.cpp` flags
- Safe parsing of raw arguments through `shlex`

#### 🧠 Intelligent Model Presets

| Keyword in filename | Temperature | Top-K | Top-P | Repeat Penalty |
|---------------------|-------------|-------|-------|----------------|
| `chat` | 0.7 | 50 | 0.9 | — |
| `instruct` | 0.2 | 40 | 0.95 | — |
| `code` | 0.1 | 10 | 0.95 | 1.0 |
| `story` | 0.9 | 0 | 0.9 | 1.15 |
| `creative` | 1.0 | 0 | 0.9 | 1.15 |

#### 💾 Persistent Per-Model Settings
- Automatically saves settings for each model
- Automatically restores configuration when the model is selected again
- Includes a reset option for safe defaults

#### 🔄 Integrated Process Management
- Separate real-time logs for **llama.cpp** and **Open WebUI**
- Status indicators in the bottom bar
- One-click access to Web UI in the browser

### 📋 Screenshots

#### System & Network Tab
![System tab](https://github.com/user-attachments/assets/25c27368-fed0-4310-a91e-9e52466320ac)

#### Main & Generation Tab
![Main tab](https://github.com/user-attachments/assets/8c95295d-c0be-4165-a3b0-a564e6ad4cf0)

### 🔧 Requirements

- **Python**: 3.10 or higher
- **OS**: Windows (primary), macOS, Linux
- **RAM**: 8 GB minimum
- **VRAM**: 2 GB minimum for GPU acceleration
- **llama.cpp**: use a build that matches your backend

### 📦 Dependencies

```txt
ttkbootstrap >= 1.6.0
```

### 🚀 Quick Start

```bash
git clone https://github.com/Trikster76/ai-server-llama.cpp.git
cd ai-server-llama.cpp
pip install -r requirements.txt
python AI-Server-Launcher.py
```

### First Run Checklist

1. Click **"▸ Show Backends"** to expand the backend panel.
2. Select **CPU**, **Vulkan**, or **Mixed**.
3. Choose the matching `server.exe`.
4. Select a `.gguf` model file.
5. Adjust core parameters or apply a preset.
6. Click **Run Llama.cpp**.
7. Open **Open WebUI** or access the API directly.

### 🌐 API Usage

#### Chat Completions

```bash
curl -X POST http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"default","messages":[{"role":"user","content":"Initialize system diagnostics."}]}'
```

#### Embeddings

```bash
curl -X POST http://127.0.0.1:8080/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{"input":"Data to embed","model":"default"}'
```

### 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Executable not found | Verify that `server.exe` is assigned to the active backend |
| Server crashes immediately | Reduce context size or GPU layers, check available memory |
| Slow generation | Use the correct backend build and update GPU drivers |
| Open WebUI connection issues | Verify the port and ensure `open-webui` is installed |
| Settings are not saved | Check write permissions in the app folder |

### 📖 Documentation

- [CHANGELOG.md](CHANGELOG.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [LICENSE](LICENSE)

---

## Русский

### Описание

**Neural Core: AI Server Launcher** — это продвинутый десктопный оркестратор для локального AI-инференса. Он предоставляет удобный графический центр управления для запуска и настройки **llama.cpp** и **Open WebUI**, полностью избавляя от необходимости вручную составлять длинные аргументы командной строки.

Программа создана для пользователей, которым важны **локальное выполнение**, **автономия данных** и **гибкость работы с железом**. Neural Core даёт прямой контроль над inference-стеком через выверенный интерфейс в эстетике киберпанка.

### ✨ Главные возможности

#### 🖥️ Интерфейс и эстетика
- **4 темы оформления**: Neural Core (Cyberpunk — по умолчанию), Darkly, Litera, Superhero
- **2 языка интерфейса**: Русский и English
- Встроенный терминал логов с моноширинным шрифтом

#### ⚙️ Умная маршрутизация бэкендов
- Переключение между **CPU**, **Vulkan** и **Mixed**
- Отдельный путь к `server.exe` для каждого бэкенда
- Сворачиваемая панель выбора бэкенда

#### 📋 Гранулярная настройка llama.cpp
**Ключевые параметры:**

| Параметр | Описание | По умолчанию |
|----------|----------|--------------|
| Порт | Порт API | 8080 |
| Контекст | Размер окна контекста в токенах | 4096 |
| Слои ГПУ | Выгрузка слоёв в VRAM (`-1` = максимум) | -1 |
| Потоки ЦПУ | Количество потоков CPU | 8 |
| Размер батча | Размер батча обработки промпта | 512 |

**Параметры генерации:**

| Параметр | Описание | По умолчанию |
|----------|----------|--------------|
| Температура | Случайность / креативность ответа | 0.7 |
| Top-K | Ограничение выборки | 40 |
| Top-P | Порог ядерной выборки | 0.95 |
| Штраф за повторения | Пенальти за повтор токенов | 1.1 |

**Флаги поведения:**
- `Jinja Template`
- `Без прогрева (No Warmup)`
- `Embedding Mode`

**Сеть и память:**
- Хост (`127.0.0.1` или `0.0.0.0`)
- Необязательный API-ключ
- Блокировка памяти через `--mlock`

#### 🔧 Расширенная кастомизация
- **12 ручных слотов параметров**
- Поле **Raw Args** для передачи любых флагов `llama.cpp`
- Безопасный разбор аргументов через `shlex`

#### 🧠 Интеллектуальные пресеты моделей

| Маркер в имени | Температура | Top-K | Top-P | Штраф |
|----------------|-------------|-------|-------|-------|
| `chat` | 0.7 | 50 | 0.9 | — |
| `instruct` | 0.2 | 40 | 0.95 | — |
| `code` | 0.1 | 10 | 0.95 | 1.0 |
| `story` | 0.9 | 0 | 0.9 | 1.15 |
| `creative` | 1.0 | 0 | 0.9 | 1.15 |

#### 💾 Сохранение настроек для каждой модели
- Настройки автоматически сохраняются
- Конфигурация автоматически восстанавливается при повторном выборе модели
- Есть кнопка сброса к безопасным значениям

#### 🔄 Управление процессами
- Отдельные логи для **llama.cpp** и **Open WebUI**
- Индикаторы состояния в статус-баре
- Быстрое открытие Web UI в браузере

### 📋 Скриншоты

<img width="1052" height="1032" alt="Image" src="https://github.com/user-attachments/assets/44aadc78-92de-43a0-adae-3fc7d1a0437f" />
<img width="1052" height="1032" alt="Image" src="https://github.com/user-attachments/assets/571d769a-932d-4a1e-ba58-9d72229a986a" />
<img width="1052" height="1032" alt="Image" src="https://github.com/user-attachments/assets/332064ed-d981-4088-b8f1-5df1392304ae" />

### 🔧 Требования

- **Python**: 3.10 или выше
- **ОС**: Windows (основная), macOS, Linux
- **ОЗУ**: минимум 8 ГБ
- **VRAM**: от 2 ГБ для GPU-ускорения
- **llama.cpp**: используйте сборку под нужный бэкенд

### 📦 Зависимости

```txt
ttkbootstrap >= 1.6.0
```

### 🚀 Быстрый старт

```bash
git clone https://github.com/Trikster76/ai-server-llama.cpp.git
cd ai-server-llama.cpp
pip install -r requirements.txt
python AI-Server-Launcher.py
```

### Первый запуск

1. Нажмите **«▸ Показать бэкенды»**.
2. Выберите **CPU**, **Vulkan** или **Mixed**.
3. Укажите путь к нужному `server.exe`.
4. Выберите `.gguf` модель.
5. Настройте параметры или примените пресет.
6. Нажмите **«Запустить Llama.cpp»**.
7. Откройте **Open WebUI** или используйте API напрямую.

### 🌐 Использование API

#### Chat Completions

```bash
curl -X POST http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"default","messages":[{"role":"user","content":"Инициализация системы завершена."}]}'
```

#### Embeddings

```bash
curl -X POST http://127.0.0.1:8080/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{"input":"Данные для эмбеддинга","model":"default"}'
```

### 🐛 Решение проблем

| Проблема | Решение |
|----------|---------|
| Исполняемый файл не найден | Проверьте, что `server.exe` назначен активному бэкенду |
| Сервер падает при запуске | Уменьшите контекст или слои GPU, проверьте память |
| Низкая скорость | Используйте правильную сборку backend и обновите драйверы |
| Open WebUI не подключается | Проверьте порт и наличие `open-webui` |
| Настройки не сохраняются | Проверьте права записи в папке приложения |

### 📖 Документация

- [CHANGELOG.md](CHANGELOG.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [LICENSE](LICENSE)

---

**Made with ❤️ by [Trikster76](https://github.com/Trikster76)**
