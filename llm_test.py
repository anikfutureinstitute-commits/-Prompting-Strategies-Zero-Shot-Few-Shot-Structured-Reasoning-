import os
from openai import OpenAI
from dotenv import load_dotenv

from prompts import (
    zero_shot_prompt,
    few_shot_prompt,
    structured_reasoning_prompt
)

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

customer_statement = (
    "I want to compare my current electricity bill with other providers."
)

prompts = {
    "Zero-Shot": zero_shot_prompt(customer_statement),
    "Few-Shot": few_shot_prompt(customer_statement),
    "Structured Reasoning": structured_reasoning_prompt(customer_statement)
}

for name, prompt in prompts.items():
    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    response = client.responses.create(
        model="gpt-5-mini",
        input=prompt
    )

    print(response.output_text)
