import os

def read_file_content(filepath):
    """Read the content of a file."""
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        return content if content.strip() else "(empty)"

def write_to_md(output_path, filename, content):
    """Write the content into a .md file in the desired format."""
    with open(output_path, 'a', encoding='utf-8') as md_file:
        md_file.write(f"``` {filename}\n{content}\n```\n\n")

def main():
    # Directory containing the .py files
    source_directory = os.path.join("gpt_commit")
    
    # Name of the output .md file
    output_md = "gpt_commit_code_summary.md"
    
    # If the output file already exists, remove it to start fresh
    if os.path.exists(output_md):
        os.remove(output_md)
    
    # Iterate over the files in the directory
    for filename in os.listdir(source_directory):
        if filename.endswith(".py"):
            filepath = os.path.join(source_directory, filename)
            content = read_file_content(filepath)
            write_to_md(output_md, filename, content)
    
    print(f"Content written to {output_md}")

if __name__ == '__main__':
    main()
