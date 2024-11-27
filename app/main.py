from groq import Groq
import openai
import os
import typer
from typing import Optional
from colorama import Fore, Style, init
from dotenv import load_dotenv
import time
import json
from datetime import datetime
import requests
from PIL import Image
from io import BytesIO
from fpdf import FPDF
from fpdf.enums import XPos, YPos
import markdown2
from rich.markdown import Markdown
from rich.console import Console
load_dotenv()

# Initialize colorama
init()

## Load environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')
client = Groq(api_key=os.getenv('GROQ_API_KEY'))
image_api_url = os.getenv('APP_URL')

## Loading models for different AI providers
OPENAI_MODEL = "gpt-3.5-turbo"  
GROQ_MODEL = "llama3-8b-8192"

## Define the Temperature, max_tokens, stream 
TEMPERATURE = 0.5
MAX_TOKENS = 1024
STREAM = False

## USER Icon and ASSISTANT Icon
USER_ICON = "👤"
ASSISTANT = "🤖"
app = typer.Typer()

def save_chat_history(messages, model_type, save_path=None, custom_filename=None, export_format='json'):
    # Handle save directory path
    if save_path:
        # Handle both file and directory paths
        if os.path.splitext(save_path)[1]:  # If path has extension, treat as file
            save_dir = os.path.dirname(save_path)
            filename = save_path
        else:  # Treat as directory
            save_dir = save_path
            if custom_filename:
                # Add appropriate extension based on export format
                if not custom_filename.endswith(f'.{export_format}'):
                    custom_filename += f'.{export_format}'
                filename = os.path.join(save_dir, custom_filename)
            else:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = os.path.join(save_dir, f"chat_{model_type}_{timestamp}.{export_format}")
    else:
        # Default behavior: save in chat_history directory
        save_dir = "chat_history"
        if custom_filename:
            # Add appropriate extension based on export format
            if not custom_filename.endswith(f'.{export_format}'):
                custom_filename += f'.{export_format}'
            filename = os.path.join(save_dir, custom_filename)
        else:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(save_dir, f"chat_{model_type}_{timestamp}.{export_format}")
    
    # Create directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)
    
    # Handle different export formats
    if export_format.lower() == 'pdf':
        return export_to_pdf(messages, filename)
    elif export_format.lower() == 'markdown':
        return export_to_markdown(messages, filename)
    else:  # default to JSON
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(messages, f, indent=2, ensure_ascii=False)
        return filename

def export_to_pdf(messages, output_file):
    """Export chat history to a PDF file."""
    try:
        pdf = FPDF()
        pdf.add_page()
        
        # Title
        pdf.set_font('Helvetica', size=16)
        pdf.cell(0, 10, 'Chat History', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.set_font('Helvetica', size=10)
        pdf.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(10)
        
        # Content
        pdf.set_font('Helvetica', size=12)
        for msg in messages:
            role = msg.get('role', 'user').lower()
            # Replace emoji with text equivalents and display in uppercase
            display_role = role.upper()
            icon = "[USER]" if role == "user" else "[ASSISTANT]"
            content = msg.get('content', '')
            
            # Role header
            pdf.set_text_color(0, 0, 255 if role == "user" else 128)
            pdf.cell(0, 10, f"{icon} {display_role}:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
            # Message content
            pdf.set_text_color(0, 0, 0)
            pdf.multi_cell(0, 10, content)
            pdf.ln(5)
        
        pdf.output(output_file)
        return output_file
    except Exception as e:
        raise Exception(f"Failed to export to PDF: {str(e)}")

def export_to_markdown(messages, output_file):
    """Export chat history to a Markdown file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Chat History\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            for msg in messages:
                role = msg.get('role', 'user').lower()
                # Display role in uppercase but store as lowercase
                display_role = role.upper()
                icon = USER_ICON if role == "user" else ASSISTANT
                content = msg.get('content', '')
                
                f.write(f"### {icon} {display_role}\n\n")
                f.write(f"{content}\n\n")
                f.write("---\n\n")
        
        return output_file
    except Exception as e:
        raise Exception(f"Failed to export to Markdown: {str(e)}")

def generate_image(prompt: str, output_dir: str = "generated_images") -> str:
    """Generate an image from a text prompt"""
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate timestamp for unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_dir, f"image_{timestamp}.png")
        
        # Start timing
        start = time.time()
        
        # Make API request
        response = requests.get(image_api_url, params={'prompt': prompt})
        
        if response.status_code == 200:
            # Save the image
            image = Image.open(BytesIO(response.content))
            image.save(output_file)
            
            # Calculate generation time
            elapsed_time = time.time() - start
            return output_file, elapsed_time
        else:
            raise Exception(f"API request failed with status code: {response.status_code}")
            
    except Exception as e:
        raise Exception(f"Failed to generate image: {str(e)}")

@app.command()
def interactive_chat(
    text: Optional[str] = typer.Argument(None, help="Initial text for the conversation"),
    temperature: Optional[float] = typer.Option(TEMPERATURE, "--temperature", "-T", help="Temperature for the model"),
    max_tokens: Optional[int] = typer.Option(MAX_TOKENS, "--max-tokens", "-M", help="Maximum number of tokens to generate"),
    stream: Optional[bool] = typer.Option(STREAM, "--stream", "-S", help="Stream the response"),
    model_type: Optional[str] = typer.Option("openai", "--model-type", "-mt", help="Type of model to use (openai, groq, or image)"),
    openai_model: Optional[str] = typer.Option(OPENAI_MODEL, "--openai-model", "-o", help="Model to use for generating responses"),
    groq_model: Optional[str] = typer.Option(GROQ_MODEL, "--groq-model", "-g", help="Model to use for generating responses from Groq"),
    save_history: Optional[bool] = typer.Option(False, "--save", "-s", help="Save chat history to a file"),
    image_dir: Optional[str] = typer.Option(None, "--image-dir", "-i", help="Directory to save generated images"),
    export_format: Optional[str] = typer.Option("json", "--format", "-f", help="Export format for chat history (json, pdf, markdown)")
):
    if model_type.lower() == "image" and not image_api_url:
        typer.echo(f"{Fore.RED}Error: APP_URL environment variable is not set for image generation.{Style.RESET_ALL}")
        return
    elif model_type.lower() == "openai" and not openai.api_key:
        typer.echo(f"{Fore.RED}Error: OPENAI_API_KEY environment variable is not set.{Style.RESET_ALL}")
        return
    elif model_type.lower() == "groq" and not client.api_key:
        typer.echo(f"{Fore.RED}Error: GROQ_API_KEY environment variable is not set.{Style.RESET_ALL}")
        return

    typer.echo(f"{Fore.GREEN}Starting interactive {'image generation' if model_type.lower() == 'image' else 'chat'} with model type: {model_type}{Style.RESET_ALL}")
    if text:
        typer.echo(f"{Fore.CYAN}Initial text: {text}{Style.RESET_ALL}")

    messages = []
    while True:
        if not text:
            text = typer.prompt(f"{Fore.YELLOW}{'Enter image prompt' if model_type.lower() == 'image' else 'You'}{Style.RESET_ALL}")

        if text.lower() == "exit":
            if save_history and messages:
                custom_path = typer.prompt(
                    f"{Fore.YELLOW}Enter path to save chat history (press Enter for default){Style.RESET_ALL}",
                    default=""
                )
                custom_filename = typer.prompt(
                    f"{Fore.YELLOW}Enter filename for chat history (press Enter for default timestamp){Style.RESET_ALL}",
                    default=""
                )
                filename = save_chat_history(messages, model_type, custom_path, custom_filename, export_format)
                typer.echo(f"{Fore.GREEN}Chat history saved to: {Fore.CYAN}{filename}{Style.RESET_ALL}")
            typer.echo(f"{Fore.GREEN}Thanks for {'generating images' if model_type.lower() == 'image' else 'chatting'}!{Style.RESET_ALL}")
            break

        if model_type.lower() == "image":
            try:
                # Ask for custom save location if not provided via command line
                if not image_dir:
                    image_dir = typer.prompt(
                        f"{Fore.YELLOW}Enter path to save image (press Enter for default){Style.RESET_ALL}",
                        default="generated_images"
                    )
                
                output_file, elapsed_time = generate_image(text, output_dir=image_dir)
                typer.echo(f"{Fore.GREEN}Image generated successfully in {elapsed_time:.2f} seconds!{Style.RESET_ALL}")
                typer.echo(f"{Fore.CYAN}Saved as: {output_file}{Style.RESET_ALL}")
                messages.append({"role": "user", "content": f"Generated image with prompt: {text}"})
                messages.append({"role": "assistant", "content": f"Image saved as: {output_file}"})
                # Reset text for next input
                text = None
            except Exception as e:
                typer.echo(f"{Fore.RED}Error generating image: {str(e)}{Style.RESET_ALL}")
                # Reset text on error
                text = None
        elif model_type.lower() == "openai":
            try:
                messages.append({"role": "user", "content": text})
                if stream:
                    response = openai.ChatCompletion.create(
                        model=openai_model,
                        messages=messages,
                        temperature=temperature,
                        max_tokens=max_tokens,
                        stream=True,
                    )
                    typer.echo(f"\n{Fore.BLUE}Assistant: {Style.RESET_ALL}", nl=False)
                    collected_content = []
                    for chunk in response:
                        if chunk.choices[0].delta.get("content"):
                            content = chunk.choices[0].delta.content
                            collected_content.append(content)
                            typer.echo(content, nl=False)
                    typer.echo("\n")
                    messages.append({"role": "assistant", "content": "".join(collected_content)})
                else:
                    response = openai.ChatCompletion.create(
                        model=openai_model,
                        messages=messages,
                        temperature=temperature,
                        max_tokens=max_tokens,
                        stream=False,
                    )
                    content = response.choices[0].message.content
                    typer.echo(f"\n{Fore.BLUE}Assistant: {Style.RESET_ALL}" + content)
                    messages.append({"role": "assistant", "content": content})
                # Reset text for next input
                text = None
            except Exception as e:
                typer.echo(f"{Fore.RED}Error with OpenAI API: {str(e)}{Style.RESET_ALL}")
                if "invalid_api_key" in str(e).lower():
                    typer.echo(f"{Fore.RED}Please check your OpenAI API key.{Style.RESET_ALL}")
                elif "rate_limit" in str(e).lower():
                    typer.echo(f"{Fore.RED}Rate limit exceeded. Please wait a moment before trying again.{Style.RESET_ALL}")
                # Reset text on error
                text = None

        elif model_type.lower() == "groq":
            try:
                messages.append({"role": "user", "content": text})
                if stream:
                    completion = client.chat.completions.create(
                        model=groq_model,
                        messages=messages,
                        temperature=temperature,
                        max_tokens=max_tokens,
                        stream=True,
                    )
                    typer.echo(f"\n{Fore.BLUE}Assistant: {Style.RESET_ALL}", nl=False)
                    collected_content = []
                    for chunk in completion:
                        try:
                            content = chunk.choices[0].delta.content
                            if content:
                                collected_content.append(content)
                                typer.echo(content, nl=False)
                        except Exception:
                            continue
                    typer.echo("\n")
                    messages.append({"role": "assistant", "content": "".join(collected_content)})
                else:
                    completion = client.chat.completions.create(
                        model=groq_model,
                        messages=messages,
                        temperature=temperature,
                        max_tokens=max_tokens,
                        stream=False,
                    )
                    content = completion.choices[0].message.content
                    typer.echo(f"\n{Fore.BLUE}Assistant: {Style.RESET_ALL}" + content)
                    messages.append({"role": "assistant", "content": content})
                # Reset text for next input
                text = None
            except Exception as e:
                typer.echo(f"{Fore.RED}Error with Groq API: {str(e)}{Style.RESET_ALL}")
                if "invalid_api_key" in str(e).lower():
                    typer.echo(f"{Fore.RED}Please check your Groq API key.{Style.RESET_ALL}")
                elif "rate_limit" in str(e).lower():
                    typer.echo(f"{Fore.RED}Rate limit exceeded. Please wait a moment before trying again.{Style.RESET_ALL}")
                # Reset text on error
                text = None
        else:
            typer.echo(f"{Fore.RED}Invalid model type. Please use 'openai', 'groq', or 'image'.{Style.RESET_ALL}")
            continue
        text = None
        time.sleep(1)

if __name__ == "__main__":
    app()