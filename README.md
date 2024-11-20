# OmniChat CLI 🤖

A powerful command-line interface for interacting with AI models and generating images. Features multiple AI providers, streaming responses, and a colorful interface.

## ✨ Features

### AI Providers
- 🧠 **OpenAI** (`gpt-3.5-turbo`)
- 🚀 **Groq** (`llama3-8b-8192`)
- 🎨 **Image Generation**

### Core Features
- 📡 Real-time streaming responses
- 🌈 Colorful, emoji-enhanced interface
- 💾 Chat history saving
- 📁 Custom save locations
- ⚙️ Configurable parameters
  - Temperature control
  - Token limits
  - Model selection
  - Response streaming

### Interface
- 👤 User messages in yellow
- 🤖 Assistant responses in blue
- 🎨 Image generation with custom prompts
- 🚦 Color-coded status messages
- 📝 Easy-to-read format with emoji indicators

## 🛠️ Prerequisites

- Python 3.7+
- Required API Keys:
  - OpenAI API key
  - Groq API key
  - Image Generation API URL

##  🌟 Image Demo

![Image Demo](Image/Image.png)

## 📦 Installation

1. Create and activate conda environment:
```bash
# Create new environment
conda create -n omnichat python=3.10

# Activate environment
conda activate omnichat
```

2. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure API Keys:

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
python app/chat.py
```

2. Chat with Groq:
```bash
python app/chat.py --model-type groq
```

3. Generate Images:
```bash
python app/chat.py --model-type image
```

### Advanced Usage

1. Stream Responses:
```bash
python app/chat.py --stream
```

2. Custom Model Settings:
```bash
python app/chat.py --temperature 0.7 --max-tokens 2048
```

3. Save Chat History:
```bash
python app/chat.py --save
```

4. Custom Image Directory:
```bash
python app/chat.py --model-type image --image-dir my_images
```

5. Combined Features:
```bash
python app/chat.py --model-type image --save --image-dir my_images --stream
```

## 📚 Example
Refer to the [Example](DEMO.md) section.

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

## 💾 Data Management

### Chat History
- Default Location: `chat_history/`
- Format: JSON files with timestamps
- Custom Locations: Use any path when prompted
- Naming: `chat_[model-type]_[timestamp].json`

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
[MIT License](LICENSE)

## 🔍 Tips & Tricks

1. **Chat Mode**:
   - Use "exit" to end the session
   - Try different temperatures for varied responses
   - Enable streaming for real-time responses

2. **Image Generation**:
   - Be specific in your prompts
   - Use custom directories for organization
   - Combine with chat history saving

3. **History Management**:
   - Use descriptive directory names
   - Organize by date or project
   - Review saved JSON files for conversation tracking


## Thanks to:
- [Groq](https://groq.com/)
- [OpenAI](https://openai.com)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [Typer](https://typer.tiangolo.com/)
- [Colorama](https://pypi.org/project/colorama/)
