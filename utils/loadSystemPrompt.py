import os

def load_system_prompt(level=1):
    """Load system prompt from markdown file based on level"""
    prompt_file = f"prompts/level-{level}.md"
    
    if not os.path.exists(prompt_file):
        raise FileNotFoundError(f"Prompt file {prompt_file} not found")
    
    with open(prompt_file, 'r', encoding='utf-8') as f:
        content = f.read()
        # Remove markdown header and return clean prompt
        lines = content.split('\n')
        return '\n'.join(lines[2:]).strip()
