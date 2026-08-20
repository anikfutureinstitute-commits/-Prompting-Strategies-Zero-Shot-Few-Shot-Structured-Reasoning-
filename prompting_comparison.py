# Prompting Strategies Comparison
# Zero-Shot, Few-Shot and Structured Reasoning
customer_statement = "I am happy with my current electricity provider and don't want to change."
print("Customer Statement:")
print(customer_statement)
print("\n--- Zero-Shot Prompting ---")
print("Classify the customer statement into the most appropriate category.")
print("\n--- Few-Shot Prompting ---")
print("Classify the statement using examples of previously classified customer statements.")
print("\n--- Structured Reasoning ---")
print("Analyze the customer's intent, identify relevant keywords, and then assign the most appropriate category.")
print("\nCategories:")
print("1. Not Interested")
print("2. Happy With Current Provider")
print("3. Wants Comparison")
print("4. Other")
