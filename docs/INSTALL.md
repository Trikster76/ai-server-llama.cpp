# 🚀 Installation Guide

## System Requirements

### Minimum Specifications
- **CPU**: Any modern processor (Intel, AMD, ARM)
- **RAM**: 8GB (16GB+ recommended)
- **Storage**: 10GB free space (for models)
- **Python**: 3.10+ (tested on 3.13.5)
- **OS**: Windows 10+, macOS 10.14+, Linux (any distro)

### For GPU Acceleration (Optional)
- **NVIDIA GPU**: CUDA 11.8+, 2GB+ VRAM minimum
- **AMD GPU**: ROCm 5.0+, 2GB+ VRAM minimum
- **macOS**: M1/M2/M3 with Metal support

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Trikster76/ai-server-llama.cpp.git
cd ai-server-llama.cpp
```

### 2. Create Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed ttkbootstrap-1.6.0
```

### 4. Download llama.cpp

**Option A: Pre-built Binary (Recommended)**

1. Visit [llama.cpp Releases](https://github.com/ggerganov/llama.cpp/releases)
2. Download the latest release for your OS:
   - `llama-X.X.X-bin-win-cuda-cu12.2.0.zip` (Windows with NVIDIA GPU)
   - `llama-X.X.X-bin-macos-arm64.zip` (macOS M1/M2/M3)
   - `llama-X.X.X-bin-linux-x64.tar.gz` (Linux)

3. Extract to a convenient location:
   - Windows: `C:\\AI\\llama.cpp\\`
   - macOS/Linux: `~/AI/llama.cpp/`

4. The executable will be at:
   - Windows: `C:\\AI\\llama.cpp\\llama-server.exe`
   - macOS/Linux: `~/AI/llama.cpp/llama-server`

**Option B: Build from Source**

For advanced users or custom CUDA versions:

```bash
# Clone repository
git clone https://github.com/ggerganov/llama.cpp.git
cd llama.cpp

# Build (Unix)
make

# Or with GPU support
make LLAMA_CUDA=1  # For NVIDIA
make LLAMA_HIPBLAS=1  # For AMD
```

### 5. Download AI Models

**From Hugging Face (Recommended)**

1. Visit [Hugging Face Models](https://huggingface.co/models?search=gguf)
2. Popular models to start:
   - **Mistral 7B** (Fast, good quality)
   - **Neural Chat 7B** (Optimized for conversation)
   - **Llama 2 7B** (Balanced)
   - **DeepSeek 7B** (For Russian)

3. Download in GGUF format (`.gguf` files only)
4. Store models in a dedicated folder:
   - Windows: `C:\\AI\\Models\\`
   - macOS/Linux: `~/AI/Models/`

**Example using Hugging Face CLI:**
```bash
# Install huggingface-hub
pip install huggingface-hub

# Download a model
huggingface-cli download \
  TheBloke/Mistral-7B-Instruct-v0.2-GGUF \
  mistral-7b-instruct-v0.2.Q4_K_M.gguf \
  --local-dir ~/AI/Models/
```

### 6. Run the Application

**Activate virtual environment (if not already):**
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

**Launch the application:**
```bash
python AI-Server-Launcher.py
```

The GUI window should appear.

## First Configuration

### Step 1: Select llama.cpp Executable
1. Click "Browse..." next to "Llama.cpp (server.exe)"
2. Navigate to your llama.cpp installation
3. Select `llama-server.exe` (Windows) or `llama-server` (Unix)

### Step 2: Select Model
1. Click "Browse..." next to "Model"
2. Select your GGUF model file
3. Settings will auto-load if they were saved before

### Step 3: Configure Parameters (Optional)
The default settings work for most models. Adjust if needed:
- **Context**: 2048-4096 for most models
- **GPU Layers**: -1 (use all available)
- **CPU Threads**: Match your CPU core count
- **Batch Size**: 512 (higher if you have VRAM)

### Step 4: Start Server
1. Click "Run Llama.cpp"
2. Wait for "slot_load_model: 100%"
3. Server is ready when you see the HTTP listening message

### Step 5: Access the Server

**Option A: Web UI**
- Click "Open WebUI" button
- Or manually start "Open WebUI" from the WebUI tab

**Option B: API**
- Use curl or your client: `http://127.0.0.1:8080/v1/chat/completions`
- See API documentation

## Troubleshooting Installation

### Issue: Python not found
```bash
# Check Python installation
python --version

# If not found, install from python.org or:
brew install python  # macOS
sudo apt install python3-venv  # Linux
```

### Issue: ttkbootstrap installation fails
```bash
# Try with specific version
pip install ttkbootstrap==1.6.0

# Or upgrade pip first
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### Issue: llama-server not starting
1. Ensure you selected the correct executable path
2. Try running llama-server directly from command line
3. Check if required CUDA/ROCm drivers are installed

### Issue: "Model file not found"
1. Verify model path is correct
2. Ensure model is in GGUF format (.gguf extension)
3. Check file is not corrupted

### Issue: Out of memory (OOM)
1. Reduce context size (try 2048 instead of 4096)
2. Reduce GPU layers
3. Use smaller model (Q4 instead of Q5/Q6)

## Optional: GPU Setup

### NVIDIA CUDA
```bash
# Check CUDA version
nvidia-smi

# Install CUDA toolkit (if needed)
# Visit: https://developer.nvidia.com/cuda-downloads
```

### AMD ROCm
```bash
# Install ROCm
wget -q -O - https://repo.radeon.com/rocm/rocm.gpg.key | sudo apt-key add -

# Then build llama.cpp with ROCm support
cd llama.cpp
make LLAMA_HIPBLAS=1 clean
make LLAMA_HIPBLAS=1
```

### macOS Metal
```bash
# Just build normally, Metal is automatic on macOS
cd llama.cpp
make
```

## Verification

### Check Installation
```bash
# Verify Python packages
pip list | grep ttkbootstrap

# Verify llama.cpp
./llama-server --version  # Windows: llama-server.exe

# Verify model
ls -lh ~/AI/Models/*.gguf
```

### Test Run
1. Start the application
2. Select llama.cpp executable
3. Select a model
4. Click "Run Llama.cpp"
5. Wait for startup messages
6. Check logs for errors

## Uninstallation

```bash
# Remove virtual environment
rm -rf venv  # macOS/Linux
rmdir /s venv  # Windows

# Remove models (optional)
rm -rf ~/AI/Models/  # macOS/Linux
rmdir /s C:\\AI\\Models  # Windows
```

## Getting Help

- **Issues**: [GitHub Issues](https://github.com/Trikster76/ai-server-llama.cpp/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Trikster76/ai-server-llama.cpp/discussions)
- **llama.cpp Issues**: [llama.cpp GitHub](https://github.com/ggerganov/llama.cpp/issues)
