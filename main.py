import os
import gradio as gr
from groq import Groq
from dotenv import load_dotenv
from utils.loadSystemPrompt import load_system_prompt

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = load_system_prompt(level=3)

def generate_command(user_input):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            temperature=0.1,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

with gr.Blocks(title="CLI Command Generator") as iface:
    gr.Markdown("# 🤖 **CLI Command Generator**")
    gr.Markdown("### ✨ **Write what you want to do, get the CLI command instantly**")
    
    with gr.Row():
        with gr.Column():
            user_input = gr.Textbox(
                lines=3,
                placeholder="💬 Describe what you want to do (e.g., delete all text files)",
                label="📝 **Your Request**"
            )
            submit_btn = gr.Button("⚡ Generate Command", variant="primary", size="lg")
        
        with gr.Column():
            output = gr.Code(
                label="💻 **Generated Command**",
                language="shell"
            )
    
    gr.Examples(
        examples=[
            ["Find all PDF files in current directory"],
            ["Copy file report.txt to backup folder"],
            ["Show network connections"],
            ["Rename file old.txt to new.txt"]
        ],
        inputs=user_input
    )
    
    submit_btn.click(fn=generate_command, inputs=user_input, outputs=output)
    user_input.submit(fn=generate_command, inputs=user_input, outputs=output)

if __name__ == "__main__":
    iface.launch(
        theme=gr.themes.Soft(
            primary_hue="blue",
            secondary_hue="cyan"
        )
    )