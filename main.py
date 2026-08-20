from prompts import (
    zero_shot_prompt,
    few_shot_prompt,
    structured_reasoning_prompt
)
customer_statement = "I want to compare my current electricity bill with other providers."
print("CUSTOMER STATEMENT")
print(customer_statement)
print("\n" + "=" * 50)
print("ZERO-SHOT PROMPT")
print("=" * 50)
print(zero_shot_prompt(customer_statement))
print("\n" + "=" * 50)
print("FEW-SHOT PROMPT")
print("=" * 50)
print(few_shot_prompt(customer_statement))
print("\n" + "=" * 50)
print("STRUCTURED REASONING PROMPT")
print("=" * 50)
print(structured_reasoning_prompt(customer_statement))
