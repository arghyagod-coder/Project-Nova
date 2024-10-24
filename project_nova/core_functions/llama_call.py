import ollama

def process_command_with_ollama(command):
    try:
        response = ollama.chat(model='llama2-uncensored:latest', messages=[
            {
                'role': 'user',
                'content': command,
            },
        ])

        return response['message']['content']
    
    except Exception as e:
        print(f"Error processing command with Ollama: {e}")
        return None