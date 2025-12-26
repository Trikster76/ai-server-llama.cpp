<img width="999" height="952" alt="llama" src="https://github.com/user-attachments/assets/eaae1c9c-7a32-45bc-be05-661038281edb" />
<img width="996" height="942" alt="llama1" src="https://github.com/user-attachments/assets/5e189366-8a74-415e-9f6c-737680b5dece" />
<img width="997" height="944" alt="llama2" src="https://github.com/user-attachments/assets/c122a806-b3b4-4e71-bad4-d863b8f8d595" />
<img width="993" height="994" alt="llama3" src="https://github.com/user-attachments/assets/e463536d-f6c0-4467-ab3c-7a05fa7dd6c2" />
# 🚀 AI Server Launcher

**Advanced GUI application for managing llama.cpp and Open WebUI servers with flexible parameter configuration and multilingual support**

[English](#english) | [Русский](#русский)

---

## English

### Overview

**AI Server Launcher** is a powerful desktop application that simplifies the management of local AI language model servers. It provides an intuitive graphical interface for controlling:

- **llama.cpp Server** - High-performance inference engine for local LLM models
- **Open WebUI** - Feature-rich web interface for interacting with LLMs

### ✨ Key Features

- 🎯 **Easy Server Management** - Start/stop servers with a single click
- ⚙️ **Flexible Configuration** - Control all llama.cpp parameters from GUI
- 🌍 **Multilingual Support** - Russian and English interface languages
- 💾 **Smart Settings** - Automatic settings save/load per model
- 🎨 **Multiple Themes** - Dark (Darkly), Light (Litera), and High Contrast (Superhero) modes
- 🧠 **Intelligent Presets** - Auto-configuration for Chat, Instruct, Code, Story, Creative modes
- 📊 **Real-time Logs** - Live monitoring of server output
- 🚀 **GPU Acceleration** - Full support for GPU-accelerated inference
- 🔒 **API Security** - Support for Bearer token authentication
- 🖥️ **Network Access** - Configure server accessibility (localhost or network-wide)

### 📋 Screenshots

#### Main Interface
<img width="999" height="952" alt="llama" src="https://github.com/user-attachments/assets/eaae1c9c-7a32-45bc-be05-661038281edb" />

#### Generation Parameters
<img width="996" height="942" alt="llama1" src="https://github.com/user-attachments/assets/5e189366-8a74-415e-9f6c-737680b5dece" />

#### System Configuration
<img width="997" height="944" alt="llama2" src="https://github.com/user-attachments/assets/c122a806-b3b4-4e71-bad4-d863b8f8d595" />

#### Text Generation Parameters
<img width="993" height="994" alt="llama3" src="https://github.com/user-attachments/assets/e463536d-f6c0-4467-ab3c-7a05fa7dd6c2" />

### 🔧 System Requirements

- **Python**: 3.10 or higher (tested on 3.13.5)
- **Operating System**: Windows, macOS, Linux
- **RAM**: 8GB minimum (16GB+ recommended)
- **VRAM**: 2GB minimum (for GPU acceleration)

### 📦 Dependencies

```
tkinter (included with Python)
ttkbootstrap >= 1.6.0
```

### 🚀 Quick Start

#### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Trikster76/ai-server-llama.cpp.git
   cd ai-server-llama.cpp
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download llama.cpp**
   - Download from [llama.cpp releases](https://github.com/ggerganov/llama.cpp/releases)
   - Extract to a convenient location

5. **Download a model**
   - Get GGUF format models from [Hugging Face](https://huggingface.co/models?search=gguf)
   - Popular choices: Llama 2, Mistral, Neural Chat

6. **Run the application**
   ```bash
   python AI-Server-Launcher.py
   ```

#### First Run

1. Open the application
2. Select **"Browse..."** to choose your `llama-server.exe` executable
3. Select **"Browse..."** to choose your GGUF model file
4. Configure parameters in the **"Main"** tab (port, context, GPU layers, threads)
5. Click **"Run Llama.cpp"** to start the server
6. Open WebUI or access via API at `http://127.0.0.1:8080/v1/chat/completions`

### ⚙️ Advanced Configuration

#### Main Tab Parameters

| Parameter | Description | Default | Notes |
|-----------|-------------|---------|-------|
| **Port** | Server listening port | 8080 | Use different ports for multiple instances |
| **Context** | Token context window | 4096 | Larger = more memory usage |
| **GPU Layers** | Layers to offload to GPU | -1 | -1 = all layers, increase for better performance |
| **CPU Threads** | CPU threads for inference | 8 | Match your CPU core count |
| **Batch Size** | Prompt batch size | 512 | Higher = faster but more VRAM usage |

#### Generation Parameters (Sampling Tab)

| Parameter | Description | Default | Range | Notes |
|-----------|-------------|---------|-------|-------|
| **Temperature** | Response creativity | 0.7 | 0.0-2.0 | Lower = more deterministic |
| **Top-K** | Vocabulary filtering | 40 | 0-100 | Limits token selection to K most likely |
| **Top-P** | Nucleus sampling | 0.95 | 0.0-1.0 | Cumulative probability threshold |
| **Repeat Penalty** | Token repetition control | 1.1 | 1.0+ | Higher = less repetition |

#### Network Settings (System & Network Tab)

| Setting | Description | Default |
|---------|-------------|---------|
| **Host** | Binding address | 127.0.0.1 |
| **API Key** | Bearer token (optional) | - |
| **mlock** | Lock model in RAM | Enabled |

### 🧠 Smart Presets

The application includes intelligent presets that auto-configure parameters based on model type:

- **Chat** - Balanced settings for conversational AI
  - Temperature: 0.7, Top-K: 50, Top-P: 0.9
- **Instruct** - Precise following of instructions
  - Temperature: 0.2, Top-K: 40, Top-P: 0.95
- **Code** - Optimized for code generation
  - Temperature: 0.1, Top-K: 10, Top-P: 0.95, Repeat Penalty: 1.0
- **Story** - Creative narrative generation
  - Temperature: 0.9, Top-K: 0, Top-P: 0.9, Repeat Penalty: 1.15
- **Creative** - Maximum creativity
  - Temperature: 1.0, Top-K: 0, Top-P: 0.9, Repeat Penalty: 1.15

Simply select a model with matching keywords (e.g., `mistral-chat.gguf`) and click "Apply Model Preset".

### 🌐 API Usage

Once the server is running, you can interact with it via HTTP API:

#### Chat Completions
```bash
curl -X POST http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "default",
    "messages": [{"role": "user", "content": "Hello!"}],
    "temperature": 0.7,
    "max_tokens": 512
  }'
```

#### Embeddings
```bash
curl -X POST http://127.0.0.1:8080/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Your text here",
    "model": "default"
  }'
```

### 📖 Documentation Files

- **[FEATURES.md](docs/FEATURES.md)** - Detailed feature descriptions
- **[INSTALL.md](docs/INSTALL.md)** - Advanced installation guide
- **[API.md](docs/API.md)** - Complete API reference
- **[TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)** - Common issues and solutions

### 🐛 Troubleshooting

**Q: "Llama.cpp executable not found"**
- A: Make sure you selected the correct `llama-server.exe` file

**Q: Server starts but crashes immediately**
- A: Check context size is less than model's max tokens, reduce GPU layers if out of VRAM

**Q: Poor performance on GPU**
- A: Increase GPU layers (use -1 for all), ensure GPU drivers are updated

**Q: Open WebUI won't connect**
- A: Verify port number is correct and firewall isn't blocking connections

See [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) for more solutions.

### 🤝 Contributing

Contributions are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 🙏 Acknowledgments

- [llama.cpp](https://github.com/ggerganov/llama.cpp) - High-performance LLM inference
- [Open WebUI](https://github.com/open-webui/open-webui) - Modern web interface
- [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap) - Modern Tkinter themes

### 💬 Support

- 📧 Issues: [GitHub Issues](https://github.com/Trikster76/ai-server-llama.cpp/issues)
- 💡 Discussions: [GitHub Discussions](https://github.com/Trikster76/ai-server-llama.cpp/discussions)

---

## Русский

### Описание

**AI Server Launcher** — это мощное приложение для рабочего стола, которое упрощает управление локальными серверами языковых моделей ИИ. Оно предоставляет интуитивный графический интерфейс для управления:

- **Сервер llama.cpp** — высокопроизводительный движок для вывода локальных LLM моделей
- **Open WebUI** — многофункциональный веб-интерфейс для взаимодействия с LLM

### ✨ Основные возможности

- 🎯 **Простое управление серверами** - Запуск/остановка серверов одним кликом
- ⚙️ **Гибкая конфигурация** - Полный контроль параметров llama.cpp через GUI
- 🌍 **Поддержка многих языков** - Интерфейс на русском и английском
- 💾 **Умные настройки** - Автоматическое сохранение/загрузка настроек для каждой модели
- 🎨 **Несколько тем** - Тёмная (Darkly), светлая (Litera) и контрастная (Superhero)
- 🧠 **Интеллектуальные пресеты** - Автоконфигурация для режимов Chat, Instruct, Code, Story, Creative
- 📊 **Живые логи** - Мониторинг вывода сервера в реальном времени
- 🚀 **Ускорение на GPU** - Полная поддержка GPU-ускорения
- 🔒 **Безопасность API** - Поддержка аутентификации через Bearer token
- 🖥️ **Доступ в сети** - Конфигурация доступности сервера (локально или по сети)

### 🔧 Требования

- **Python**: 3.10 или выше (протестировано на 3.13.5)
- **ОС**: Windows, macOS, Linux
- **ОЗУ**: минимум 8GB (рекомендуется 16GB+)
- **VRAM**: минимум 2GB (для ускорения на GPU)

### 📦 Зависимости

```
tkinter (входит в Python)
ttkbootstrap >= 1.6.0
```

### 🚀 Быстрый старт

#### Установка

1. **Клонировать репозиторий**
   ```bash
   git clone https://github.com/Trikster76/ai-server-llama.cpp.git
   cd ai-server-llama.cpp
   ```

2. **Создать виртуальное окружение** (рекомендуется)
   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows: venv\Scripts\activate
   ```

3. **Установить зависимости**
   ```bash
   pip install -r requirements.txt
   ```

4. **Загрузить llama.cpp**
   - Скачайте с [llama.cpp releases](https://github.com/ggerganov/llama.cpp/releases)
   - Распакуйте в удобное место

5. **Загрузить модель**
   - Получите модели в формате GGUF с [Hugging Face](https://huggingface.co/models?search=gguf)
   - Популярные: Llama 2, Mistral, Neural Chat

6. **Запустить приложение**
   ```bash
   python AI-Server-Launcher.py
   ```

#### Первый запуск

1. Откройте приложение
2. Нажмите **"Обзор..."** и выберите файл `llama-server.exe`
3. Нажмите **"Обзор..."** и выберите файл модели в формате GGUF
4. Настройте параметры в табе **"Основные"** (порт, контекст, слои GPU, потоки)
5. Нажмите **"Запустить Llama.cpp"** для запуска сервера
6. Откройте WebUI или используйте API по адресу `http://127.0.0.1:8080/v1/chat/completions`

### ⚙️ Продвинутая конфигурация

#### Параметры вкладки "Основные"

| Параметр | Описание | По умолчанию | Примечания |
|----------|---------|--------------|-----------|
| **Порт** | Порт прослушивания сервера | 8080 | Используйте разные порты для разных инстансов |
| **Контекст** | Размер контекста в токенах | 4096 | Больше = больше памяти |
| **Слои ГПУ** | Слои для выгрузки на GPU | -1 | -1 = все слои, увеличивайте для лучшей производительности |
| **Потоки ЦПУ** | Потоки ЦПУ для вывода | 8 | Установите равным количеству ядер ЦПУ |
| **Размер батча** | Размер батча для промпта | 512 | Больше = быстрее, но больше использование VRAM |

#### Параметры генерации (вкладка "Генерация")

| Параметр | Описание | По умолчанию | Диапазон | Примечания |
|----------|---------|--------------|----------|-----------|
| **Температура** | Творческость ответа | 0.7 | 0.0-2.0 | Ниже = более предсказуемо |
| **Top-K** | Фильтрация словаря | 40 | 0-100 | Ограничивает выбор K самых вероятных токенов |
| **Top-P** | Выборка ядра | 0.95 | 0.0-1.0 | Порог кумулятивной вероятности |
| **Штраф повтора** | Контроль повтора токенов | 1.1 | 1.0+ | Выше = меньше повторений |

#### Сетевые настройки (вкладка "Система и Сеть")

| Настройка | Описание | По умолчанию |
|-----------|---------|--------------|
| **Хост** | Адрес привязки | 127.0.0.1 |
| **Ключ API** | Bearer token (опционально) | - |
| **mlock** | Блокировка модели в ОЗУ | Включено |

### 🧠 Умные пресеты

Приложение включает интеллектуальные пресеты, которые автоматически конфигурируют параметры на основе типа модели:

- **Chat** - Сбалансированные параметры для диалога
  - Температура: 0.7, Top-K: 50, Top-P: 0.9
- **Instruct** - Точное следование инструкциям
  - Температура: 0.2, Top-K: 40, Top-P: 0.95
- **Code** - Оптимизировано для генерации кода
  - Температура: 0.1, Top-K: 10, Top-P: 0.95, Штраф: 1.0
- **Story** - Творческая генерация текста
  - Температура: 0.9, Top-K: 0, Top-P: 0.9, Штраф: 1.15
- **Creative** - Максимальная творческость
  - Температура: 1.0, Top-K: 0, Top-P: 0.9, Штраф: 1.15

Просто выберите модель с соответствующим названием (например, `mistral-chat.gguf`) и нажмите "Применить пресет модели".

### 🌐 API использование

Когда сервер запущен, вы можете взаимодействовать с ним через HTTP API:

#### Chat Completions
```bash
curl -X POST http://127.0.0.1:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "default",
    "messages": [{"role": "user", "content": "Привет!"}],
    "temperature": 0.7,
    "max_tokens": 512
  }'
```

#### Embeddings
```bash
curl -X POST http://127.0.0.1:8080/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Ваш текст здесь",
    "model": "default"
  }'
```

### 📖 Документация

- **[FEATURES.md](docs/FEATURES.md)** - Подробное описание возможностей
- **[INSTALL.md](docs/INSTALL.md)** - Расширенное руководство установки
- **[API.md](docs/API.md)** - Полный справочник API
- **[TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)** - Решение типичных проблем

### 🐛 Решение проблем

**В: "Исполняемый файл Llama.cpp не найден"**
- О: Убедитесь, что выбран правильный файл `llama-server.exe`

**В: Сервер запускается но сразу крашится**
- О: Проверьте, что размер контекста меньше максимума модели, уменьшите слои GPU если недостаточно VRAM

**В: Плохая производительность на GPU**
- О: Увеличьте количество слоев GPU (используйте -1 для всех), обновите драйверы GPU

**В: Open WebUI не подключается**
- О: Проверьте корректность номера порта и что брандмауэр не блокирует соединения

Смотрите [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) для большего количества решений.

### 🤝 Внесение вклада

Приветствуются контрибьюции! Вы можете:

1. Сделать fork репозитория
2. Создать ветку для вашей функции (`git checkout -b feature/amazing-feature`)
3. Сделать commit изменений (`git commit -m 'Add amazing feature'`)
4. Отправить ветку (`git push origin feature/amazing-feature`)
5. Открыть Pull Request

### 📝 Лицензия

Этот проект распространяется под лицензией MIT - смотрите файл [LICENSE](LICENSE) для деталей.

### 🙏 Спасибо

- [llama.cpp](https://github.com/ggerganov/llama.cpp) - Высокопроизводительный вывод LLM
- [Open WebUI](https://github.com/open-webui/open-webui) - Современный веб-интерфейс
- [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap) - Современные темы Tkinter

### 💬 Поддержка

- 📧 Issues: [GitHub Issues](https://github.com/Trikster76/ai-server-llama.cpp/issues)
- 💡 Discussions: [GitHub Discussions](https://github.com/Trikster76/ai-server-llama.cpp/discussions)

---

**Made with ❤️ by [Trikster76](https://github.com/Trikster76)**
