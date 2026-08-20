# Results
## Test Statement
> I want to compare my current electricity bill with other providers.
## Expected Category
**Wants Comparison**
## Prompting Approaches
### 1. Zero-Shot Prompting
The model receives the task and category definitions without any examples.
**Expected result:**  
Wants Comparison
### 2. Few-Shot Prompting
The model receives several examples showing how customer statements were classified.
**Expected result:**  
Wants Comparison
### 3. Structured Reasoning
The model is instructed to identify the customer's intent, analyze the statement, and then select a category.
**Expected result:**  
Wants Comparison
## Observation
All three approaches should be evaluated using the same customer statements.
The purpose of the project is to compare how different prompting strategies affect classification accuracy and consistency.
## Conclusion
The results will be updated after testing the prompts with an LLM.
