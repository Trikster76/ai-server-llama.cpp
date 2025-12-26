# Contributing to AI Server Launcher

Thank you for your interest in contributing! We welcome contributions from everyone.

## Code of Conduct

Be respectful and constructive. We maintain a friendly and inclusive community.

## How to Contribute

### Reporting Bugs

1. **Check existing issues** - Your bug may already be reported
2. **Create a new issue** with:
   - Clear title describing the bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Your environment (OS, Python version, etc.)
   - Error messages or logs

### Suggesting Features

1. **Check discussions** - Your idea may already be discussed
2. **Create a new discussion** or issue with:
   - Clear feature description
   - Use case and motivation
   - Possible implementation approaches
   - Examples or mockups if relevant

### Submitting Pull Requests

#### Setup Development Environment

```bash
# Fork the repository
git clone https://github.com/YOUR-USERNAME/ai-server-llama.cpp.git
cd ai-server-llama.cpp

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Making Changes

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Keep commits atomic and well-described
   - Follow existing code style
   - Add comments for complex logic

3. **Test your changes**
   ```bash
   python AI-Server-Launcher.py
   ```

4. **Document changes**
   - Update README if needed
   - Update CHANGELOG.md
   - Add docstrings to functions

#### Submitting PR

1. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request**
   - Use descriptive title
   - Describe changes and motivation
   - Link related issues
   - Include screenshots for UI changes

3. **Address review comments**
   - Be open to feedback
   - Make requested changes
   - Re-request review after updates

## Code Style Guidelines

### Python

- Follow PEP 8 conventions
- Use meaningful variable names
- Add docstrings to functions
- Keep lines under 100 characters

```python
# Good
def process_model_settings(model_path: str) -> dict:
    """Load and process model settings from file.
    
    Args:
        model_path: Path to the GGUF model file
        
    Returns:
        Dictionary of model settings
    """
    settings = load_settings(model_path)
    return validate_settings(settings)

# Avoid
def process(m):
    s = load_settings(m)
    return validate_settings(s)
```

### UI Elements

- Use existing design patterns from code
- Maintain consistent spacing (5px padding)
- Use design system color variables
- Test on all 3 themes

```python
# Good - consistent with existing code
frame = ttk.LabelFrame(parent, text=label, padding=10)
button = ttk.Button(frame, text=text, bootstyle=SUCCESS)
button.pack(side=LEFT, padx=5, pady=5)

# Avoid
button = ttk.Button(frame, text=text)
button.pack()
```

## Areas for Contribution

### High Priority
- Bug fixes
- Performance improvements
- Documentation improvements
- UI/UX enhancements

### Medium Priority
- Feature additions
- Test coverage
- Error handling

### Nice to Have
- Code refactoring
- Comments and docstrings
- Example scripts

## Development Tips

### Debugging

```python
# Enable debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Print variables
print(f"Debug: {variable_name}={variable_name}")
```

### Testing UI Changes

1. Test on all 3 themes:
   - Settings → Theme → Darkly/Litera/Superhero

2. Test both languages:
   - Settings → Language → Русский/English

3. Test with different models

### Performance Testing

```bash
# Profile code execution
python -m cProfile AI-Server-Launcher.py

# Monitor memory
python -m tracemalloc AI-Server-Launcher.py
```

## Documentation Style

### README
- Use clear headings
- Include code examples
- Keep bilingual (Russian/English)
- Add screenshots for features

### Code Comments
```python
# Short explanation for non-obvious code
if gpu_layers == -1:  # -1 means use all available layers
    gpu_layers = calculate_max_layers()
```

### Docstrings
```python
def function_name(param1: str, param2: int) -> bool:
    """Short description.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When input is invalid
    """
```

## Commit Messages

```
# Good
Fix GPU memory calculation for RTX cards
Refactor settings loading to use new config format
Add Russian translation for error messages

# Avoid
fix bug
update code
changes
```

## Release Process

Maintainers will:
1. Review and merge PRs
2. Update CHANGELOG.md
3. Create GitHub release
4. Tag version

## Getting Help

- **Questions**: Open a Discussion
- **Issues**: Check existing issues first
- **Code Review**: Ask in PR comments
- **Design Decisions**: Start a Discussion

## Community

- GitHub Issues: Bug reports and feature requests
- GitHub Discussions: Questions and ideas
- Pull Requests: Code contributions

## License

By contributing, you agree that your code will be licensed under the MIT License.

## Recognition

Contributors will be:
- Added to README contributors list
- Mentioned in release notes
- Thanked in discussions

---

**Thank you for contributing to AI Server Launcher! 🚀**
