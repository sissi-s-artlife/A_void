def count_letter_e(text):
    count = 0
    for char in text:
        if char.lower() == 'e':
            count += 1
    return count

def visualize_without_e(text):
    return text.replace('e', ' ')

# Get input text
input_text = input("Enter a text: ")

# Count occurrences of 'e'
e_count = count_letter_e(input_text)
total_characters = len(input_text)
e_percentage = (e_count / total_characters) * 100

# Visualize text without 'e'
visualized_text = visualize_without_e(input_text)

# Print results
print(f"\nOccurrences of 'e': {e_count}")
print(f"Total characters: {total_characters}")
print(f"Percentage of 'e': {e_percentage:.2f}%")
print("\nText without 'e':")
print(visualized_text)

