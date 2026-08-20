# Prompt Templates for Customer Statement Classification
def zero_shot_prompt(statement):
    return f"""
Classify the following customer statement into one of these categories:
- Not Interested
- Happy With Current Provider
- Wants Comparison
- Other
Customer statement:
{statement}
"""
def few_shot_prompt(statement):
    return f"""
Classify the customer statement using the examples below.
Example 1:
Customer: "I am happy with my current provider."
Category: Happy With Current Provider
Example 2:
Customer: "I don't want to change my provider."
Category: Not Interested
Example 3:
Customer: "I want to compare electricity prices."
Category: Wants Comparison
Now classify this statement:
Customer: "{statement}"
Category:
"""
def structured_reasoning_prompt(statement):
    return f"""
Classify the customer statement.
Follow these steps:
1. Identify the customer's main intent.
2. Determine whether the customer is interested in changing or comparing providers.
3. Select the most appropriate category.
4. Return only the category as the final answer.
Categories:
- Not Interested
- Happy With Current Provider
- Wants Comparison
- Other
Customer statement:
{statement}
"""
