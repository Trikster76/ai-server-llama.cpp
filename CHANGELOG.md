# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-26

### Added
- Initial public release
- Dual server management (llama.cpp + Open WebUI)
- Advanced parameter configuration through GUI
- Bilingual support (Russian + English)
- Smart settings persistence per model
- Intelligent model presets (Chat, Instruct, Code, Story, Creative)
- Multiple UI themes (Darkly, Litera, Superhero)
- Real-time server logging and monitoring
- GPU acceleration support (CUDA, ROCm, Metal)
- API key authentication
- Network configuration options
- Custom parameter support
- OpenAI API compatible endpoints
- Comprehensive documentation
- MIT License

### Features
- **Server Management**
  - Single-click start/stop for llama.cpp and Open WebUI
  - Real-time status monitoring
  - Process health checking
  - Automatic cleanup on exit

- **Configuration**
  - 20+ configurable parameters
  - Automatic per-model settings persistence
  - Preset profiles for common use cases
  - Custom parameter slots

- **Performance**
  - GPU layer offloading
  - Context window configuration
  - Batch size optimization
  - CPU thread management
  - Memory locking (mlock) support

- **Text Generation**
  - Temperature control
  - Top-K and Top-P sampling
  - Repeat penalty adjustment
  - Token limit configuration

- **User Interface**
  - Clean, intuitive tabbed interface
  - Multi-language support with hotswitch
  - 3 modern themes
  - Live log monitoring
  - Helpful tooltips

- **Network**
  - Local and network access modes
  - Custom port configuration
  - Bearer token authentication
  - Full OpenAI API compatibility

### Documentation
- Comprehensive README with bilingual content
- Detailed installation guide
- Advanced features documentation
- Troubleshooting guide with FAQ
- API reference
- Example curl commands

---

## Version History

This release represents the culmination of development efforts to create a
comprehensive GUI for local LLM server management. All features are production-ready.

### Future Enhancements (Planned)
- Model management UI
- Performance benchmarking tools
- Advanced scheduling
- Docker support
- Web UI embedding
- Extended API endpoints
- Plugin system
- Distributed inference

---

## Compatibility

### Supported Platforms
- Windows 10+
- macOS 10.14+
- Linux (any distro)

### Python Versions
- Python 3.10+
- Tested on 3.13.5

### Dependencies
- ttkbootstrap >= 1.6.0
- tkinter (included with Python)

### Compatible Servers
- llama.cpp (latest)
- Open WebUI (latest)

### GPU Support
- NVIDIA CUDA 11.8+
- AMD ROCm 5.0+
- Apple Metal (M1/M2/M3)

---

## Development

For development history and contributions, see:
- [GitHub Issues](https://github.com/Trikster76/ai-server-llama.cpp/issues)
- [GitHub Discussions](https://github.com/Trikster76/ai-server-llama.cpp/discussions)

## License

MIT License - See LICENSE file for details
