# OmniChat CLI Demo 🤖

This demo showcases the various features and capabilities of OmniChat CLI.

## 1. Basic Chat Examples 💬

### OpenAI Chat (Default)
```bash
$ omenicli
👤 Tell me a joke about programming
🤖 Why do programmers prefer dark mode?
   Because light attracts bugs! 😄
```

### Groq Chat
```bash
$ omenicli --model-type groq
👤 What's the difference between AI and ML?
🤖 AI is like having a smart assistant who can think and make decisions,
   while ML is teaching that assistant through examples and experience.
```

## 2. Streaming Responses ⚡

### OpenAI with Streaming
```bash
$ omenicli --stream
👤 Write a short poem about coding
🤖 In lines of code, we find our way
   Through logic gates day by day
   Debug and test, we persevere
   Until solutions crystal clear
```

### Groq with Streaming
```bash
$ omenicli --model-type groq --stream
👤 Explain quantum computing
🤖 [Response streams word by word in real-time...]
```

## 3. Image Generation 🎨

### Basic Image Generation
```bash
$ omenicli --model-type image
👤 Create a cyberpunk city at night
🤖 Generating image... Done! ✨
📁 Saved as: generated_images/image_20240315_123456.png
```

### Custom Save Location
```bash
$ omenicli --model-type image --image-dir my_artwork
👤 A futuristic space station
🤖 Generating image... Done! ✨
📁 Saved as: my_artwork/image_20240315_123789.png
```

## 4. Advanced Configuration Examples ⚙️

### Custom Temperature
```bash
$ omenicli --temperature 0.8
👤 Generate a creative story
🤖 [More creative and varied response due to higher temperature]
```

### Custom Max Tokens
```bash
$ omenicli --max-tokens 2048
👤 Write a detailed analysis
🤖 [Longer, more detailed response]
```

### Custom Model Selection
```bash
$ omenicli --openai-model gpt-3.5-turbo
👤 Explain blockchain
🤖 [Response from specified model]
```

## 5. Chat History Management 📝

### Basic History Saving
```bash
$ omenicli --save
👤 What is quantum entanglement?
🤖 [Detailed explanation about quantum entanglement]
Enter path to save chat history (press Enter for default): 
Enter filename for chat history (press Enter for default timestamp): quantum_basics
💾 Chat history saved to: chat_history/quantum_basics.json
```

### Custom Directory and Filename
```bash
$ omenicli --save
👤 Explain string theory
🤖 [Detailed explanation about string theory]
Enter path to save chat history (press Enter for default): physics/quantum
Enter filename for chat history (press Enter for default timestamp): string_theory_explained
💾 Chat history saved to: physics/quantum/string_theory_explained.json
```

### Project-Based Organization
```bash
$ omenicli --save
👤 How do neural networks work?
🤖 [Detailed explanation about neural networks]
Enter path to save chat history (press Enter for default): ai_learning
Enter filename for chat history (press Enter for default timestamp): neural_networks_101
💾 Chat history saved to: ai_learning/neural_networks_101.json
```

## 6. Combined Features 🌟

### Image Generation with History
```bash
$ omenicli --model-type image --save --image-dir art_portfolio
👤 Create a Renaissance-style portrait
🤖 Generating image... Done! ✨
📁 Image: art_portfolio/image_20240315_124567.png
Enter path to save chat history (press Enter for default): art_portfolio/conversations
Enter filename for chat history (press Enter for default timestamp): renaissance_portrait
💾 Chat history saved to: art_portfolio/conversations/renaissance_portrait.json
```

### Streaming Chat with Custom Settings
```bash
$ omenicli --stream --temperature 0.7 --max-tokens 1500 --save
👤 Write a sci-fi story opening
🤖 [Streams creative response with custom parameters]
Enter path to save chat history (press Enter for default): stories
Enter filename for chat history (press Enter for default timestamp): scifi_story_draft1
💾 Chat history saved to: stories/scifi_story_draft1.json
```

## 7. Error Handling Examples ⚠️

### Missing API Key
```bash
$ omenicli
❌ Error: OpenAI API key not found. Please set OPENAI_API_KEY environment variable.
```

### Invalid Model Type
```bash
$ omenicli --model-type invalid
❌ Error: Invalid model type. Choose from: openai, groq, image
```

### Network Error
```bash
$ omenicli
❌ Error: Network connection failed. Please check your internet connection.
```

## 8. Interactive Features 🎮

### Exit and Save
```bash
$ omenicli --save
👤 What is the theory of relativity?
🤖 [Detailed explanation about relativity]
👤 exit
Enter path to save chat history (press Enter for default): physics
Enter filename for chat history (press Enter for default timestamp): relativity_explained
💾 Chat history saved to: physics/relativity_explained.json
🤖 Goodbye! Thanks for using OmniChat CLI! 👋
```

### Help Command
```bash
$ omenicli --help
[Displays all available commands and options]
```

## 9. Export Formats 📊

### JSON Export (Default)
```bash
$ omenicli --save
👤 Tell me about Python
🤖 Python is a versatile programming language...
👤 exit
💾 Chat saved to: chat_history/chat_openai_20240323_145623.json
```

### PDF Export
```bash
$ omenicli --save --format pdf
👤 What are the benefits of AI?
🤖 AI offers numerous advantages...
👤 exit
💾 Chat saved to: chat_history/chat_openai_20240323_145712.pdf
```

### Markdown Export
```bash
$ omenicli --save --format markdown
👤 Explain machine learning
🤖 Machine learning is a subset of AI...
👤 exit
💾 Chat saved to: chat_history/chat_openai_20240323_145830.md
```

## 10. Multi-Turn Conversations 🔄

```bash
$ omenicli --save
👤 What is Python?
🤖 Python is a high-level programming language...

👤 What are its main features?
🤖 Python's main features include:
   1. Easy to read syntax
   2. Dynamic typing
   3. Extensive libraries
   [...]

👤 exit
Enter path to save chat history (press Enter for default): programming/python
Enter filename for chat history (press Enter for default timestamp): python_introduction
💾 Chat history saved to: programming/python/python_introduction.json
```

## 11. Tips & Best Practices 💡

1. **Organizing Chat History**:
   - Use descriptive filenames (e.g., `quantum_basics`, `neural_networks_101`)
   - Create topic-based directories (e.g., `physics/`, `ai_learning/`)
   - Include project names in paths (e.g., `project_x/research/`)

2. **Image Generation**:
   - Be detailed in image descriptions
   - Use project-specific directories
   - Combine with chat history for context

3. **Efficient Workflow**:
   - Use streaming for long responses
   - Save important conversations with meaningful names
   - Organize files by topic and project

---

*Note: All timestamps and file names are examples. Actual values will vary based on when commands are run.*
