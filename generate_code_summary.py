import os
import tempfile
import subprocess
import pathspec


def read_file_content(filepath):
    """Read the content of a file."""
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        return content if content.strip() else "(empty)"


def load_gitignore():
    """Load the .gitignore specifications."""
    with open(".gitignore", "r") as f:
        gitignore = f.readlines()
    return pathspec.PathSpec.from_lines("gitwildmatch", gitignore)


def main():
    # Create a temporary file
    temp_fd, temp_path = tempfile.mkstemp(suffix=".md")
    os.close(temp_fd)  # Close the file descriptor, we'll use the path directly

    # Check if .gitignore exists and load its rules
    gitignore_spec = None
    if os.path.exists(".gitignore"):
        gitignore_spec = load_gitignore()

    # Create a list to store the names of the read files
    read_files = []

    # Iterate over the files in the current directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            relative_filepath = os.path.relpath(
                filepath
            )  # get path relative to current directory

            # Check against gitignore rules
            if gitignore_spec and gitignore_spec.match_file(relative_filepath):
                continue  # Skip this file

            if filename.endswith(".py"):
                # Add the file to the list of read files
                read_files.append(relative_filepath)
                
                content = read_file_content(filepath)
                with open(temp_path, "a", encoding="utf-8") as temp_file:
                    temp_file.write(f"``` {filename}\n{content}\n```\n\n")

    print("Editing in VS Code. Close to continue.")

    # Open the temporary file in VS Code
    subprocess.run(["cmd", "/c", "code", "-w", temp_path])

    print("Editing completed. Continuing script execution...")

    # Print the list of read files
    print("\nFiles read:")
    for file in read_files:
        print(file)

    # Remove the temporary file
    os.remove(temp_path)


if __name__ == "__main__":
    main()
