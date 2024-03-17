import os
import json
import re

def sanitize_filename(filename):
    # Remove characters not allowed in filenames and leading/trailing whitespace
    sanitized_filename = re.sub(r'[\\/*?:"<>|\n]', '', filename.strip())
    return sanitized_filename

def truncate_filename(filename, max_length=100):
    # Truncate filename if it exceeds max_length
    if len(filename) > max_length:
        filename = filename[:max_length].rsplit(' ', 1)[0]  # truncate at last space before max_length
    return filename

def convert_json_to_markdown(json_folder):
    # Create a folder to store markdown files
    markdown_folder = "markdown_results"
    os.makedirs(markdown_folder, exist_ok=True)

    # Iterate through each JSON file
    for filename in os.listdir(json_folder):
        if filename.endswith(".json"):
            json_file_path = os.path.join(json_folder, filename)
            with open(json_file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Create a folder for this JSON file
            file_folder = os.path.join(markdown_folder, os.path.splitext(filename)[0])
            os.makedirs(file_folder, exist_ok=True)

            # Process each entry in the JSON file
            for entry in data:
                title = entry.get("title")
                content = entry.get("content")
                url = entry.get("url")

                # Sanitize and truncate title for filename
                sanitized_title = sanitize_filename(title)
                truncated_title = truncate_filename(sanitized_title)

                # Create a markdown file for each entry
                markdown_filename = os.path.join(file_folder, f"{truncated_title}.md")

                # Format the content for readability
                formatted_content = content.strip()  # Remove leading and trailing whitespace
                formatted_content = re.sub(r'\n{2,}', '\n\n', formatted_content)  # Remove extra blank lines
                formatted_content = re.sub(r'(?<!\n)\n(?!\n)', '  \n', formatted_content)  # Add double space for line breaks

                # Write to the markdown file
                with open(markdown_filename, 'w', encoding='utf-8') as markdown_file:
                    markdown_file.write(f"# [{title}]({url})\n\n{formatted_content}")

def main():
    json_folder = "results"
    convert_json_to_markdown(json_folder)
    print("Conversion completed successfully.")

if __name__ == "__main__":
    main()
