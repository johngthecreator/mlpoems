import re

def clean_and_format_poems(input_file_path, output_file_path):
    # Open and read the file content
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Using regular expressions to remove the numbers, parentheses with their contents
    cleaned_content = re.sub(r'\d+\.\s*(.*?)\s*\([^)]*\)', r'\1', content)

    # Split poems by two or more newlines, which are assumed to separate poems in the original file
    poems = re.split(r'\n\n+', cleaned_content.strip())

    # Join poems with a line of dashes
    formatted_poems = '--------------\n'.join(poems)

    # Save the cleaned and formatted poems to a new text file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(formatted_poems)

    print(f"Processing finished. The formatted poems have been saved to: {output_file_path}")

# Define the input and output file paths
input_file_path = './shelpoems.txt'  # Replace this with the path to your input file
output_file_path = './shelremoved.txt'  # Replace this with the path to your output file

# Call the function to process the poems
clean_and_format_poems(input_file_path, output_file_path)
