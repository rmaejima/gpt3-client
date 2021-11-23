import os
from dotenv import load_dotenv
import openai
from openai.api_resources import engine


def create_text_by_gpt3(text_list):
    # Set API key
    load_dotenv(".env")
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    openai.api_key = OPENAI_API_KEY

    # Create prompt
    prompt = f"文章{len(text_list)+1}を生成します\n"
    for i, text in enumerate(text_list):
        prompt += f"文章{i+1}: {text}\n"
    prompt += f"文章{len(text_list)+1}:"

    # Inference
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=500,  # Length of generations
        n=3,  # The number of generations
    )

    return response
