import re
import argparse
from collections import defaultdict

# Function to parse the snippet data
def parse_snippets(data):
    snippets = []
    current_category = "Uncategorized"
    category_pattern = re.compile(r'//\s*(.+)')
    snippet_pattern = re.compile(
        r'\{trigger:\s*(?P<trigger>".+?"|/.+?/),\s*replacement:\s*(?P<replacement>".+?"|/.+?/),\s*options:\s*"(?P<options>[^"]+)"(?:,\s*description:\s*"(?P<description>[^"]+)")?\}'
    )

    for line in data.splitlines():
        line = line.strip()
        if line.startswith('//'):
            match = category_pattern.match(line)
            if match:
                current_category = match.group(1).strip()
            continue
        if line.startswith('{') and not line.startswith('//'):
            match = snippet_pattern.match(line)
            if match:
                trigger = match.group('trigger').strip('"').strip('/')
                replacement = match.group('replacement').strip('"').strip('/')
                options = match.group('options').strip()
                description = match.group('description') if match.group('description') else ""
                snippets.append({
                    'category': current_category,
                    'trigger': trigger,
                    'replacement': replacement,
                    'options': options,
                    'description': description
                })
    return snippets

# Function to escape '|' characters in Markdown table cells
def escape_markdown(text):
    return text.replace('|', '\\|')

# Function to generate Markdown tables
def generate_markdown(snippets):
    categories = defaultdict(list)
    for snippet in snippets:
        categories[snippet['category']].append(snippet)

    markdown = ""

    for category, items in categories.items():
        markdown += f"## {category}\n\n"
        markdown += "| **Trigger** | **Replacement** | **Options** | **Description** |\n"
        markdown += "|-------------|-----------------|-------------|-----------------|\n"
        for item in items:
            # Escape '|' in trigger and replacement
            escaped_trigger = escape_markdown(item['trigger'])
            escaped_replacement = escape_markdown(item['replacement'])

            # Format with backticks
            trigger = f"`{escaped_trigger}`"
            replacement = f"`{escaped_replacement}`"
            options = f"`{item['options']}`"
            description = item['description'].replace('|', '\\|')  # Also escape '|' in description if any

            markdown += f"| {trigger} | {replacement} | {options} | {description} |\n"
        markdown += "\n---\n\n"
    
    return markdown

# Main execution
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert LaTeX Workshop snippets to a Markdown cheatsheet.")
    parser.add_argument("snippet_file", help="Path to the snippet file.")
    args = parser.parse_args()

    try:
        with open(args.snippet_file, "r") as snippet_file:
            snippet_data = snippet_file.read()
    except FileNotFoundError:
        print(f"Error: The file '{args.snippet_file}' was not found.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        exit(1)
        
    snippets = parse_snippets(snippet_data)
    markdown_output = generate_markdown(snippets)
    
    # Output to a Markdown file
    output_file = "LaTeX_Snippets_Cheatsheet.md"
    try:
        with open(output_file, "w") as md_file:
            md_file.write("# LaTeX Snippets Cheatsheet\n\n")
            md_file.write(markdown_output)
        
        print(f"Cheatsheet generated successfully as '{output_file}'.")
    except Exception as e:
        print(f"An error occurred while writing the Markdown file: {e}")
        exit(1)
