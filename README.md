# 🧠 Neural Core: AI Server Launcher

**Prestige v3.2 — Advanced GUI for managing llama.cpp and Open WebUI servers**

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://python.org)
[![ttkbootstrap](https://img.shields.io/badge/ttkbootstrap-1.6%2B-purple)](https://github.com/israel-dryer/ttkbootstrap)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

[English](#english) | [Русский](#русский)

---

## English

### Overview

**Neural Core: AI Server Launcher** is a powerful, sovereign desktop orchestrator designed to streamline the execution of local AI infrastructure. Built for those who prioritize data autonomy and hardware flexibility, it provides a clean, feature-rich interface for running and configuring:

- **llama.cpp Server** — high-performance local LLM inference engine supporting multiple hardware architectures (CPU, Vulkan, Mixed backends).
- **Open WebUI** — a modern, extensible web chat interface that seamlessly connects to the llama.cpp API.

Neural Core completely eliminates the hassle of writing complex command-line arguments. All settings are persistently saved per-model, meaning your perfect configuration is automatically restored the moment you switch models.

---

### ✨ Features

#### 🖥️ Interface & Aesthetics
- **4 UI themes**: Neural Core (Cyberpunk — default), Dark (Darkly), Light (Litera), High Contrast (Superhero).
- **2 interface languages**: English and Russian — switchable at runtime on the fly.
- Integrated monospace log terminal with theme-matched colors (e.g., cyan-on-black for the ultimate Cyberpunk terminal feel).

#### ⚙️ Smart Backend Routing
- Instantly switch between **CPU**, **Vulkan**, and **Mixed** llama.cpp backends via radio buttons.
- Each backend permanently stores its own path to `server.exe` — configure all three simultaneously and route your workload dynamically.
- Collapsible backend panel to maximize screen real estate for logs.

#### 📋 Granular llama.cpp Configuration (Main & Generation tab)
**Key Hardware & Context Parameters:**
| Parameter | Description | Default |
|-----------|-------------|---------|
| Port | Listening port for the API | 8080 |
| Context | Context window size (tokens) | 4096 |
| GPU Layers | Layers to offload to VRAM (-1 = maximum) | -1 |
| CPU Threads | Parallel CPU threads allocation | 8 |
| Batch Size | Prompt processing batch size | 512 |

**Precision Sampling Parameters:**
| Parameter | Description | Default |
|-----------|-------------|---------|
| Temperature | Response randomness/creativity (0.0–2.0) | 0.7 |
| Top-K | Top K token selection limit | 40 |
| Top-P | Nucleus sampling probability threshold | 0.95 |
| Repeat Penalty | Algorithmic penalty for token repetition | 1.1 |

**Behavioral Flags:**
- ✅ Jinja Template — enforces Jinja2 prompt formatting logic.
- ✅ No Warmup — skips model warmup at startup for faster initial generation.
- ☐ Embedding Mode — enables the embedding generation endpoint.

**Network & Memory Performance:**
- Host assignment (default: `127.0.0.1` for local, use `0.0.0.0` for LAN access).
- API Key integration (optional Bearer token authentication).
- Lock model in RAM (`--mlock`) to prevent paging out to slower storage.

#### 🔧 Limitless Customization (System & Network tab)
- **12 custom parameter slots**: Two columns allowing you to inject any specific llama.cpp flag name and its corresponding value.
- **Raw Args module**: Paste any complex string of additional flags (e.g., `--kv-unified --cache-idle-slots`). Parsed safely via `shlex` for correct handling of spaces and nested quotes.

#### 🧠 Intelligent Model Presets
Click **"Apply Model Preset"** to let the launcher auto-configure sampling parameters based on keyword detection in your `.gguf` filename:

| Keyword in filename | Temperature | Top-K | Top-P | Repeat Penalty |
|---------------------|-------------|-------|-------|----------------|
| `chat` | 0.7 | 50 | 0.9 | — |
| `instruct` | 0.2 | 40 | 0.95 | — |
| `code` | 0.1 | 10 | 0.95 | 1.0 |
| `story` | 0.9 | 0 | 0.9 | 1.15 |
| `creative` | 1.0 | 0 | 0.9 | 1.15 |

#### 💾 Persistent Context (Per-Model Settings)
- Settings are **automatically saved** the moment you start the server.
- Upon selecting a `.gguf` model file, its specific historical settings are **automatically restored**.
- "Reset Settings" acts as a panic button, returning all parameters to safe factory defaults.

#### 🔄 Integrated Process Management & Logs
- Separate, scrollable real-time log terminals for both `llama.cpp` and `Open WebUI`.
- Color-coded status indicators directly in the status bar (🟢 Running / 🔴 Stopped).
- One-click "Open Web UI" button launches your default browser straight to the active API interface.

---

### 📋 Screenshots

#### System & Network Tab
![System tab](https://github.com/user-attachments/assets/25c27368-fed0-4310-a91e-9e52466320ac)

#### Main & Generation Tab
![Main tab](https://github.com/user-attachments/assets/8c95295d-c0be-4165-a3b0-a564e6ad4cf0)

---

### 🔧 Requirements

- **Python**: 3.10 or higher (tested natively on 3.13)
- **OS**: Windows (primary target), macOS, Linux
- **RAM**: 8 GB absolute minimum (16 GB+ highly recommended for serious inference)
- **VRAM**: 2 GB minimum for any meaningful GPU acceleration
- **llama.cpp**: [latest release](https://github.com/ggerganov/llama.cpp/releases) — ensure you download the build matching your chosen backend (CPU / Vulkan)

### 📦 Dependencies
ttkbootstrap >= 1.6.0
*(Standard libraries used: `tkinter`, `subprocess`, `threading`, `shlex`, `json`, `os`, `webbrowser`)*

---

### 🚀 Quick Start

```bash
# 1. Clone the repository
git clone [https://github.com/Trikster76/ai-server-llama.cpp.git](https://github.com/Trikster76/ai-server-llama.cpp.git)
cd ai-server-llama.cpp

# 2. Install GUI dependencies
pip install -r requirements.txt

# 3. Initialize the Neural Core
python AI-Server-Launcher.py

First Run Checklist
Click "▸ Show Backends" to expand the backend routing panel.

Select your hardware target (CPU / Vulkan / Mixed) and click "Browse..." to locate your downloaded server.exe.

Click "Browse..." next to Model to select your downloaded .gguf weights.

In the Main & Generation tab: verify your port, set context size, and allocate GPU layers.

(Optional) Click "Apply Model Preset" to dial in optimal sampling math.

Hit "Run Llama.cpp" — watch the terminal output to confirm successful memory allocation.

Click "Open Web UI" to jump into the chat interface.

🌐 API Usage
Once Neural Core indicates the server is running, you can hit it directly:
# Standard Chat Completions
curl -X POST [http://127.0.0.1:8080/v1/chat/completions](http://127.0.0.1:8080/v1/chat/completions) \
  -H "Content-Type: application/json" \
  -d '{"model":"default","messages":[{"role":"user","content":"Initialize system diagnostics."}]}'

# Embeddings (Requires enabling the Embedding Mode flag)
curl -X POST [http://127.0.0.1:8080/v1/embeddings](http://127.0.0.1:8080/v1/embeddings) \
  -H "Content-Type: application/json" \
  -d '{"input":"Data to embed","model":"default"}'

🐛 TroubleshootingProblemSolution"Executable not found"Double-check that you've mapped server.exe to the currently active backend radio button.Server crashes immediatelyOut of memory (OOM). Reduce Context size or lower GPU Layers. Verify VRAM availability.Sluggish token generationIf using Vulkan, ensure GPU Layers is -1. Update your graphics drivers.Open WebUI refuses connectionVerify Llama is running on the correct port. Ensure Open WebUI is installed (pip install open-webui).Amnesia (Settings not saving)Ensure the app directory isn't read-only and you have write permissions.📖 DocumentationFEATURES.md — Deep dive into functionalities.INSTALL.md — Advanced deployment guide.API.md — Comprehensive API reference.TROUBLESHOOTING.md — Extended diagnostics.CHANGELOG.md — Version history and updates.🤝 ContributingReview CONTRIBUTING.md before submitting PRs.Fork → Create feature branch → Submit PR.Keep translations synchronized across both English and Russian.Verify UI alignment on both dark and light ttkbootstrap themes.📝 LicenseMIT License — see LICENSE🙏 CreditsEngine: llama.cppFrontend: Open WebUIUI Framework: ttkbootstrapРусскийОписаниеNeural Core: AI Server Launcher (Prestige v3.2) — это продвинутый десктопный оркестратор для развертывания и управления полностью суверенной локальной ИИ-инфраструктурой. Приложение избавляет от необходимости возиться с командной строкой, предоставляя элегантный интерфейс для:llama.cpp — высокопроизводительного движка инференса LLM (с поддержкой бэкендов CPU, Vulkan и Mixed).Open WebUI — современного веб-интерфейса, бесшовно подключающегося к API llama.cpp.Система обладает "памятью": настройки сохраняются индивидуально для каждой модели. При переключении между моделями ваша идеальная среда для конкретной нейросети восстанавливается мгновенно и автоматически.✨ Главные возможности🖥️ Эстетика и Интерфейс4 темы оформления: Neural Core (Cyberpunk, по умолчанию), Тёмная (Darkly), Светлая (Litera), Контрастная (Superhero).2 языка интерфейса: Русский и English — переключаются "на лету" без перезапуска приложения.Интегрированный терминал логов с моноширинным шрифтом (Consolas) и цветовой схемой, адаптирующейся под активную тему (например, циановый текст на глубоком черном фоне для Neural Core).⚙️ Умная маршрутизация бэкендовМгновенное переключение между исполняемыми файлами CPU, Vulkan и Mixed через радиокнопки.Приложение запоминает пути к server.exe для каждого бэкенда отдельно — настройте все три архитектуры один раз и переключайтесь в зависимости от задачи.Сворачиваемая панель маршрутизации для экономии места на экране.📋 Тотальный контроль (Вкладка «Основные и Генерация»)Аппаратные параметры и Контекст:ПараметрОписаниеПо умолчаниюПортСетевой порт API8080КонтекстРазмер окна контекста в токенах4096Слои ГПУВыгрузка слоев в VRAM (-1 = максимум)-1Потоки ЦПУРаспределение потоков процессора8Размер батчаОбъем батча для обработки промпта512Прецизионная настройка генерации:ПараметрОписаниеПо умолчаниюТемператураУровень "креативности" / хаоса (0.0–2.0)0.7Top-KОграничение выборки K лучших токенов40Top-PПорог вероятности ядерной выборки0.95ШтрафПенальти за зацикливание ответов1.1Флаги поведения:✅ Jinja Template — форсирует логику шаблонизации Jinja2.✅ Без прогрева (no-warmup) — отключает предварительный прогрев тензоров для ускорения первого ответа.☐ Embedding Mode — активирует эндпоинт для генерации векторных представлений (эмбеддингов).Сеть и Память:Хост-маршрутизация (127.0.0.1 для строгой изоляции, 0.0.0.0 для доступа внутри LAN).Интеграция API-ключа (Bearer-токен для авторизации).Блокировка в ОЗУ (--mlock) — запрещает системе сбрасывать веса модели в медленный файл подкачки.🔧 Безграничная кастомизация (Вкладка «Система и Сеть»)12 слотов для ручных флагов: два столбца для точечного внедрения любых параметров llama.cpp (Имя флага + Значение).Парсер Raw Args: поле для вброса целых строк сложных аргументов (например: --kv-unified --cache-idle-slots). Данные безопасно обрабатываются модулем shlex, корректно читая пробелы и кавычки.🧠 Автоматические пресетыКнопка «Применить пресет модели» сканирует имя файла вашей .gguf модели и сама выставляет оптимальную математику сэмплирования:Маркер в имениТемператураTop-KTop-PШтрафchat0.7500.9—instruct0.2400.95—code0.1100.951.0story0.900.91.15creative1.000.91.15🔄 Мониторинг процессов в реальном времениДва независимых терминала для потокового чтения логов llama.cpp и Open WebUI.Наглядные цветовые индикаторы состояния в статус-баре (🟢 Работает / 🔴 Остановлен).Интегрированная кнопка «Открыть Web UI» — активируется только при поднятом сервере и сразу ведет в чат.🔧 Системные требованияPython: 3.10+ (основные тесты на 3.13)ОС: Windows (приоритет), macOS, LinuxОЗУ: минимум 8 ГБ (строго рекомендуется 16 ГБ+ для серьезных задач)VRAM: от 2 ГБ для использования слоев GPUДвижок: Последний билд llama.cpp (выбирайте сборку строго под ваше железо — CPU или Vulkan).📦 Зависимостиttkbootstrap >= 1.6.0
🚀 Быстрый стартBashgit clone [https://github.com/Trikster76/ai-server-llama.cpp.git](https://github.com/Trikster76/ai-server-llama.cpp.git)
cd ai-server-llama.cpp
pip install -r requirements.txt
python AI-Server-Launcher.py
Инициализация (Первый запуск)Разверните панель маршрутизации кнопкой «▸ Показать бэкенды».Выберите нужную архитектуру (CPU / Vulkan / Mixed) и укажите путь к server.exe через кнопку «Обзор...».Укажите путь к скачанному файлу весов .gguf в поле "Модель".Во вкладке «Основные и Генерация» задайте порт, лимит контекста и слои ГПУ.При необходимости примените оптимальный пресет кнопкой «Применить пресет модели».Жмите «Запустить Llama.cpp» и следите за выделением памяти в терминале.Поднимите фронтенд кнопкой «Запустить Open WebUI», а затем перейдите в чат по кнопке «Открыть Web UI».🌐 Взаимодействие через APIПока сервер поднят, к нему можно обращаться напрямую:Bashcurl -X POST [http://127.0.0.1:8080/v1/chat/completions](http://127.0.0.1:8080/v1/chat/completions) \
  -H "Content-Type: application/json" \
  -d '{"model":"default","messages":[{"role":"user","content":"Инициализация системы завершена."}]}'
🐛 Решение частых проблемСимптомДиагноз и решение«Исполняемый файл не найден»Убедитесь, что вы привязали server.exe именно к тому бэкенду, который сейчас выбран радиокнопкой.Сервер "падает" при стартеНехватка памяти (OOM). Срежьте параметр Контекст или уменьшите Слои ГПУ.Низкая скорость генерацииПри работе через Vulkan убедитесь, что Слои ГПУ = -1. Обновите драйверы видеокарты.Open WebUI не подключаетсяПроверьте совпадение портов. Убедитесь, что модуль установлен глобально (pip install open-webui).Амнезия настроекУбедитесь, что лаунчер запущен из папки, где у пользователя есть права на запись файлов.Made with ❤️ by Trikster76
