from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import subprocess
import sys

def check_ollama_model():
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True)
        if 'deepseek-r1:1.5b' not in result.stdout:
            print("Deepseek model not found. Attempting to pull it now...")
            subprocess.run(['ollama', 'pull', 'deepseek-r1:1.5b hi'], check=True)
            print("Model successfully pulled!")
    except subprocess.CalledProcessError as e:
        print("Error: Failed to pull the model. Please ensure Ollama is running.")
        print("You can start Ollama and run: ollama pull deepseek")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: Ollama is not installed or not in PATH")
        sys.exit(1)

def create_chatbot():
    llm = Ollama(
        model="deepseek-r1:1.5b",
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
        temperature=0.7
    )
    return llm

def main():
    print("Checking Ollama and model availability...")
    check_ollama_model()
    
    print("Initializing AI Chatbot with Deepseek model...")
    try:
        chatbot = create_chatbot()
    except Exception as e:
        print(f"Error initializing chatbot: {str(e)}")
        sys.exit(1)
    
    print("\nAI Chatbot is ready! Type 'quit' to exit.")
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
            
        if user_input:
            try:
                response = chatbot(user_input)
                print("\nBot:", response)
            except Exception as e:
                print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
