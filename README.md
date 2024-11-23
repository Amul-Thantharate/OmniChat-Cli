# OmniChat CLI 🤖

A powerful CLI tool that combines multiple AI models (OpenAI, Groq) for chat, image generation, and content creation. Features streaming responses, conversation history, and multi-format exports.

📚 [View Full Documentation](https://amul-thantharate.github.io/omenicli/)

## ✨ Features

### AI Providers
- 🧠 **OpenAI** (`gpt-3.5-turbo`)
- 🚀 **Groq** (`llama3-8b-8192`)
- 🎨 **Image Generation**

### Core Features
- 📡 Real-time streaming responses
- 🌈 Colorful, emoji-enhanced interface
- 💾 Chat history saving with custom filenames
- 📁 Custom save locations
- 📊 Multiple export formats
  - JSON (structured data)
  - PDF (formatted document)
  - Markdown (human-readable)
- ⚙️ Configurable parameters
  - Temperature control
  - Token limits
  - Model selection
  - Response streaming
  - Export format selection

### Interface
- 👤 User messages in yellow
- 🤖 Assistant responses in blue
- 🎨 Image generation with custom prompts
- 🚦 Color-coded status messages
- 📝 Easy-to-read format with emoji indicators

## 🛠️ Prerequisites

- Python 3.10+
- Required API Keys:
  - OpenAI API key
  - Groq API key
  - Image Generation API URL

## 📦 Installation

### From PyPI
```bash
pip install omenicli
```

### From Source
```bash
git clone https://github.com/Amul-Thantharate/omenicli.git
cd omenicli
pip install -e .
```

3. Configure API Keys:

### Method A: Environment Variables
```bash
# Windows (Command Prompt)
set OPENAI_API_KEY=your_openai_api_key
set GROQ_API_KEY=your_groq_api_key
set APP_URL=your_image_generation_api_url

# Windows (PowerShell)
$env:OPENAI_API_KEY="your_openai_api_key"
$env:GROQ_API_KEY="your_groq_api_key"
$env:APP_URL="your_image_generation_api_url"

# Linux/Mac
export OPENAI_API_KEY="your_openai_api_key"
export GROQ_API_KEY="your_groq_api_key"
export APP_URL="your_image_generation_api_url"
```

### Method B: .env File
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
APP_URL=your_image_generation_api_url
```

## 🚀 Usage

### Quick Start

1. Chat with OpenAI (Default):
```bash
omenicli
```

2. Chat with Groq:
```bash
omenicli --model-type groq
```

3. Generate Images:
```bash
omenicli --model-type image
```

### Advanced Usage

1. Stream Responses:
```bash
omenicli --stream
```

2. Custom Model Settings:
```bash
omenicli --temperature 0.7 --max-tokens 2048
```

3. Save Chat History:
```bash
omenicli --save
```

4. Custom Image Directory:
```bash
omenicli --model-type image --image-dir my_images
```

5. Combined Features:
```bash
omenicli --model-type image --save --image-dir my_images --stream
```

## 📚 Example
Refer to the [Example](https://github.com/Amul-Thantharate/omenicli/blob/master/DEMO.md) section.

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

## 💾 Data Management

### Chat History
- Default Location: `chat_history/`
- Format: JSON files
- Custom Options:
  - Directory: Enter custom path when prompted
  - Filename: Enter custom name when prompted
  - Default naming: `chat_[model-type]_[timestamp].json`

### Generated Images
- Default Location: `generated_images/`
- Format: PNG files with timestamps
- Custom Locations:
  - Via CLI: `--image-dir path/to/directory`
  - Via Prompt: Enter path when asked
- Naming: `image_[timestamp].png`

## 🔧 Error Handling

The application handles various scenarios:
- Missing/Invalid API keys
- Network connectivity issues
- Rate limiting
- Invalid configurations
- File system errors

## 🤝 Contributing

Feel free to:
- Open issues
- Submit pull requests
- Suggest improvements
- Report bugs

## 📝 License
[MIT License](https://github.com/Amul-Thantharate/omenicli/blob/master/LICENSE)

## 🔍 Tips & Tricks

1. **Chat Mode**:
   - Use "exit" to end the session
   - Try different temperatures for varied responses
   - Enable streaming for real-time responses
   - Use custom filenames for better organization

2. **Image Generation**:
   - Be specific in your prompts
   - Use custom directories for organization
   - Combine with chat history saving

3. **Chat History**:
   - Use descriptive filenames
   - Organize by project/topic
   - Use custom paths for better file management
