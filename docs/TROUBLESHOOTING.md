# 🐛 Troubleshooting Guide

## Common Issues and Solutions

### Application Issues

#### Issue: Application won't start
**Symptoms:** Double-clicking AI-Server-Launcher.py does nothing

**Solutions:**
```bash
# Run from terminal to see errors
python AI-Server-Launcher.py

# Check Python version
python --version  # Should be 3.10+

# Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

#### Issue: "ModuleNotFoundError: No module named 'ttkbootstrap'"
**Solutions:**
```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Or manually
pip install ttkbootstrap>=1.6.0
```

#### Issue: GUI looks broken or unresponsive
**Solutions:**
1. Update tkinter:
   ```bash
   # Windows
   python -m pip install --upgrade python
   
   # macOS
   brew install python-tk
   
   # Linux
   sudo apt install python3-tk
   ```

2. Try different theme:
   - Settings → Theme → Litera (Light)

3. Restart application

---

### Server Issues

#### Issue: "Llama.cpp executable not found"
**Symptoms:** Error appears when clicking "Run Llama.cpp"

**Solutions:**
1. Verify path exists:
   ```bash
   # Windows
   dir "C:\\Path\\to\\llama-server.exe"
   
   # macOS/Linux
   ls -la ~/path/to/llama-server
   ```

2. Select correct executable:
   - Look for `llama-server.exe` (Windows)
   - Look for `llama-server` (macOS/Linux)
   - NOT `llama.cpp` or folder name

3. Download latest llama.cpp:
   - Visit [llama.cpp releases](https://github.com/ggerganov/llama.cpp/releases)
   - Download pre-built binary

#### Issue: Server starts but crashes immediately
**Symptoms:** Logs show error, server stops within seconds

**Causes and Solutions:**

1. **Model file not found:**
   ```
   Error: cannot open model
   ```
   - Verify model path is correct
   - Ensure file has `.gguf` extension
   - Check file isn't corrupted

2. **Insufficient VRAM:**
   ```
   Error: out of memory
   ```
   - Reduce GPU layers: Change from -1 to 20-30
   - Reduce context size: Change from 4096 to 2048
   - Use smaller model (Q4 instead of Q5/Q6/Q8)

3. **Insufficient RAM:**
   - Close other applications
   - Reduce context size
   - Reduce CPU threads

4. **Corrupted model:**
   - Re-download model from HuggingFace
   - Verify file hash if provided

#### Issue: Server running but very slow
**Symptoms:** "Processing prompt..." takes minutes

**Solutions:**

1. **Check GPU is being used:**
   - Windows: Open Task Manager → GPU tab
   - macOS: Activity Monitor → GPU
   - Linux: `nvidia-smi` or `rocm-smi`

2. **Increase GPU layers:**
   ```
   Current: -1 (should use all)
   If showing 0%: GPU layers = 20-30
   If showing 50%: GPU layers = 30-40
   ```

3. **Check CPU threads:**
   ```
   Current: 8
   Optimal: Match your CPU core count
   (Windows Task Manager → Performance → CPU)
   ```

4. **Increase batch size:**
   ```
   Current: 512
   Try: 1024 (if you have VRAM)
   ```

5. **Reduce context size:**
   ```
   Current: 4096
   Try: 2048
   ```

---

### Model Issues

#### Issue: "Model file not found" error
**Solutions:**
1. Ensure file path is correct
2. Check file exists:
   ```bash
   ls -lh ~/path/to/model.gguf
   ```
3. Verify it's GGUF format (ends with `.gguf`)
4. Don't use spaces in path

#### Issue: Model selected but settings don't load
**Symptoms:** Settings stay default after selecting model

**Solutions:**
1. Clear cached settings:
   ```bash
   rm launcher_settings.json  # macOS/Linux
   del launcher_settings.json  # Windows
   ```

2. Click "Apply Model Preset"

3. Manually set parameters

#### Issue: Model produces gibberish output
**Causes and Solutions:**

1. **Temperature too high:**
   ```
   Current: 1.5+
   Try: 0.7
   ```

2. **Repeat penalty too low:**
   ```
   Current: 1.0
   Try: 1.2
   ```

3. **Wrong prompt format:**
   - Check model documentation
   - Some models expect specific prompt format

4. **Model quality:**
   - Try Q5 or Q6 quantization
   - Try larger model (13B instead of 7B)

---

### Network Issues

#### Issue: WebUI won't connect
**Symptoms:** Connection refused or timeout

**Solutions:**
1. Verify llama.cpp server is running
   - Check status in logs
   - Look for "Server started"

2. Check port number:
   - Default: 8080
   - Verify in "Main" tab
   - Must match WebUI configuration

3. Verify server is listening:
   ```bash
   # Windows
   netstat -an | findstr 8080
   
   # macOS/Linux
   lsof -i :8080
   ```

4. Firewall issue:
   - Windows: Check Windows Defender Firewall
   - macOS: System Preferences → Security → Firewall
   - Linux: Check `ufw` or `iptables`

5. Wrong host:
   - If using 0.0.0.0, connect to 127.0.0.1 or machine IP
   - If using 127.0.0.1, can only access from same machine

#### Issue: API requests get connection refused
**Solutions:**
```bash
# Test connectivity
curl -X GET http://127.0.0.1:8080/health

# Check server is running
curl -X GET http://127.0.0.1:8080/v1/models

# If 404: Server not responding
# If 200: Server is working
```

#### Issue: "Port already in use"
**Symptoms:** "Address already in use" error

**Solutions:**
1. Change port:
   - Open "Main" tab
   - Change "Port" from 8080 to 8081 (or higher)

2. Kill existing process:
   ```bash
   # Windows
   netstat -ano | findstr :8080
   taskkill /PID <PID> /F
   
   # macOS/Linux
   lsof -i :8080
   kill -9 <PID>
   ```

---

### Performance Issues

#### Issue: High CPU usage, low GPU usage
**Solutions:**
1. Enable GPU acceleration:
   - Verify GPU drivers are installed
   - Ensure GPU model is supported
   - Increase GPU layers

2. Check driver versions:
   ```bash
   # NVIDIA
   nvidia-smi
   
   # AMD ROCm
   rocm-smi
   ```

#### Issue: Inconsistent performance
**Causes:**
- Background processes using GPU
- Thermal throttling
- CPU frequency scaling
- Swap usage

**Solutions:**
1. Close background apps
2. Monitor temperature:
   ```bash
   # NVIDIA
   nvidia-smi -l 1
   
   # AMD
   watch -n 1 rocm-smi
   ```
3. Check for swap:
   ```bash
   # macOS/Linux
   swapon -s
   free -h
   ```

---

### Configuration Issues

#### Issue: Settings not saving
**Symptoms:** Settings reset after restart

**Solutions:**
1. Ensure model is selected before changing settings
2. Check file permissions:
   ```bash
   # macOS/Linux
   ls -la launcher_settings.json
   chmod 644 launcher_settings.json
   ```

3. Save with "Apply Model Preset" or close application

#### Issue: Language not changing
**Solutions:**
1. Select language: Settings → Language → Choose
2. Restart application
3. Check launcher_settings.json contains correct language

#### Issue: Theme not applying
**Solutions:**
1. Select theme: Settings → Theme → Choose
2. Application must restart to change theme
3. Clear ttkbootstrap cache:
   ```bash
   # Find and remove cache
   rm -rf ~/.cache/ttkbootstrap/  # Linux
   rm -rf ~/Library/Caches/ttkbootstrap/  # macOS
   ```

---

## FAQ

### Can I run multiple models simultaneously?
**A:** Not with single instance. But you can:
1. Start multiple applications on different ports
2. Run multiple llama.cpp servers separately
3. Load balance with Open WebUI

### What GGUF quantization should I use?
- **Q4_K_M**: Best balance of speed/quality (recommended)
- **Q5_K_M**: Better quality, slightly slower
- **Q6_K**: High quality, much slower
- **Q2**: Very fast, low quality
- **Q8**: Highest quality, slowest

### How much VRAM do I need?
- 7B model Q4: 4-6GB
- 13B model Q4: 8-10GB
- 70B model Q4: 40-50GB
- Reduce with Q2/Q3 quantization

### Can I use different models?
Yes! Select any GGUF format model. Settings are saved per model.

### How do I update llama.cpp?
1. Download latest release
2. Replace executable
3. Restart application
4. Select new executable path

### Is GPU required?
No! CPU mode works fine, just slower. GPU makes it 5-20x faster.

### Can I use API with other tools?
Yes! OpenAI API compatible endpoints:
- `/v1/chat/completions`
- `/v1/embeddings`
- `/v1/models`

### How do I contribute?
1. Fork repository
2. Create feature branch
3. Make changes
4. Submit Pull Request

---

## Getting Help

1. **GitHub Issues**: [Report bugs](https://github.com/Trikster76/ai-server-llama.cpp/issues)
2. **Discussions**: [Ask questions](https://github.com/Trikster76/ai-server-llama.cpp/discussions)
3. **llama.cpp Issues**: [llama.cpp support](https://github.com/ggerganov/llama.cpp/issues)
4. **Check logs**: First see what the error says in the log panel

---

**Last updated**: December 2025
