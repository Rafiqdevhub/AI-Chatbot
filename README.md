# AI Chatbot with Ollama and Deepseek

A simple command-line chatbot using Ollama with the Deepseek language model.

## Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed and running on your system
- Deepseek model (will be automatically downloaded on first run)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Rafiqdevhub/AI-Chatbot.git
cd AI-Chatbot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Ensure Ollama is running on your system before starting the chatbot.

## Usage

1. Start the chatbot:

```bash
python main.py
```

2. The program will:

   - Check if Ollama is running
   - Download the Deepseek model if not present
   - Initialize the chatbot

3. Interact with the chatbot:
   - Type your message and press Enter
   - Type 'quit' to exit the program

## Features

- Streaming responses in real-time
- Automatic model downloading
- Error handling for common issues
- Command-line interface

## Technical Details

- Uses LangChain for LLM integration
- Deepseek model (deepseek-r1:1.5b)
- Temperature setting: 0.7 (balanced between creativity and coherence)

## Troubleshooting

If you encounter issues:

1. Ensure Ollama is running:

```bash
ollama start
```

2. Manually pull the Deepseek model:

```bash
ollama pull deepseek-r1:1.5b
```

3. Check if Python dependencies are installed correctly:

```bash
pip install -r requirements.txt
```
