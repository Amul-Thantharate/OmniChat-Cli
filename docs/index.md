# OmniChat Documentation

Welcome to OmniChat - A Unified Chat Platform

## Table of Contents
- [Getting Started](#getting-started)
- [API Keys](#api-keys)
- [Installation](#installation)
- [Configuration](#configuration)
- [Configuration Options](#configuration-options)
- [Usage](#usage)
- [FAQ](#faq)
- [Examples](#examples)
- [Future Releases](#future-releases)

## Getting Started

OmniChat is a unified chat platform that allows you to connect multiple messaging services into one seamless interface. This documentation will guide you through the setup and usage of OmniChat.

## API Keys

To use OmniChat, you'll need to obtain API keys from the following services:

### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/account/api-keys)
2. Create an account or sign in
3. Go to API section
4. Generate new API key
5. Copy and save the key securely

### Groq Api Key
1. Visit [Groq](https://console.groq.com/playground)
2. Create an account or sign in
3. Go to API section
4. Generate new API key
5. Copy and save the key securely

### Airforce Api Key
1. Visit [Airforce](https://api.airforce/)
2. Create an account or sign in
3. Go to API section
4. Generate new API key
5. Copy and save the key securely

## Installation

```bash
git clone https://github.com/yourusername/OmniChat.git
cd OmniChat
pip install -r requirements.txt
```

### Exporting API Keys

#### Windows
Using Command Prompt:
```cmd
set OPENAI_API_KEY=your_openai_key_here
set GROQ_API_KEY=your_groq_key_here
set APP_URL=your_image_generation_api_url
```

Using PowerShell:
```powershell
$env:OPENAI_API_KEY="your_openai_key_here"
$env:GROQ_API_KEY="your_groq_key_here"
$env:APP_URL="your_image_generation_api_url"
```

#### Linux/macOS
```bash
export OPENAI_API_KEY="your_openai_key_here"
export GROQ_API_KEY="your_groq_key_here"
export APP_URL="your_image_generation_api_url"
```

To make these permanent:
1. For Linux/macOS: Add to `~/.bashrc` or `~/.zshrc`
2. For Windows: Add through System Properties > Environment Variables

## Usage

```bash
omenicli --help
```

## ⚙️ Configuration Options

| Option | Short | Default | Description |
|--------|--------|---------|-------------|
| --model-type | -mt | openai | Model provider (openai/groq/image) |
| --temperature | -T | 0.5 | Response randomness (0-1) |
| --max-tokens | -M | 1024 | Maximum response length |
| --stream | -S | False | Enable streaming responses |
| --save | -s | False | Save chat history |
| --openai-model | -o | gpt-3.5-turbo | OpenAI model name |
| --groq-model | -g | llama3-8b-8192 | Groq model name |
| --image-dir | -i | generated_images | Directory to save generated images |
| --export-format | -e | json | Export format (json/pdf/markdown) |

## 📚 Examples

### Chat Examples

```bash
# Start a chat session with OpenAI (default)
$ omenicli
> How can I learn Python?

# Chat with specific temperature
$ omenicli -T 0.8
> Write a creative story

# Use Groq for faster responses
$ omenicli --model-type groq
> Explain quantum computing
```

### Image Generation

```bash
# Generate a basic image
$ omenicli --model-type image
> A serene mountain landscape at sunset

# Save image to custom directory
$ omenicli -mt image -i my_art_folder
> A futuristic cityscape with flying cars
```

### Advanced Usage

```bash
# Stream responses with custom settings
$ omenicli --stream -T 0.7 -M 2048
> Write a detailed analysis of AI trends

# Save chat history with custom export
$ omenicli --save --export-format markdown
> Explain the theory of relativity

# Use specific model with custom settings
$ omenicli -mt openai -o gpt-4 -T 0.9
> Generate a complex algorithm
```

### Practical Examples

```bash
# Code explanation
$ omenicli
> Explain this code: for i in range(10): print(i)

# Technical writing
$ omenicli --save
> Write documentation for a REST API

# Creative tasks
$ omenicli -T 0.8
> Create a unique marketing slogan for an eco-friendly product
```

## FAQ

### Q: Can I use OmniChat without API keys?
A: The basic functionality requires at least the OpenAI API key. Other platform-specific features require their respective API keys.

### Q: Is my data secure?
A: Yes, all messages are encrypted in transit and we don't store any message content on our servers.

### Q: Can I run multiple instances?
A: Yes, you can run multiple instances with different configurations.

### Q: How do I update OmniChat?
A: Pull the latest changes from the repository and restart the application.

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for more information.

## Support

If you encounter any issues or need help, please:
1. Check the FAQ section
2. Search existing [GitHub Issues](https://github.com/yourusername/OmniChat/issues)
3. Create a new issue if needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🚀 Future Releases

### Version v0.2.3 (Upcoming)
- Multi-modal Interactions
  - Send text and images in the same prompt
  - Image-to-text capabilities (image description)
  - Custom prompt templates
  - Adding Replicate AI or Together AI for image generation
- Conversation Management
  - View past conversations
  - Conversation summarization
  - Email drafting assistance

### Version v0.2.4 (Planned)
- Media Processing
  - YouTube video summarization
  - Audio content summarization
  - Video content analysis
- UI Enhancements
  - Dark theme support
  - Customizable interface
  - Improved accessibility

### Version v0.2.4 (Planned)
- Advanced Features
  - Real-time translation
  - Voice command support
  - Document analysis
- Integration Improvements
  - More AI model providers
  - Enhanced API support
  - Plugin system

### Version v0.2.5 (Planned)
- Ritrival Augmentation Generation
  - Enhanced content generation
  - Personalized responses
- Vector Database Integration
  - Chat with pdf and text documents
  - Dashboard for vector database