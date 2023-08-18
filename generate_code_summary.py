import os
import tempfile
import subprocess


def read_file_content(filepath):
    """Read the content of a file."""
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        return content if content.strip() else "(empty)"


def main():
    # Directory containing the .py files
    source_directory = os.path.join("gpt_commit")

    # Create a temporary file
    temp_fd, temp_path = tempfile.mkstemp(suffix=".md")
    os.close(temp_fd)  # Close the file descriptor, we'll use the path directly

    # Iterate over the files in the directory and write to the temporary file
    for filename in os.listdir(source_directory):
        if filename.endswith(".py"):
            filepath = os.path.join(source_directory, filename)
            content = read_file_content(filepath)
            with open(temp_path, "a", encoding="utf-8") as temp_file:
                temp_file.write(f"``` {filename}\n{content}\n```\n\n")

    print("Editing in VS Code. Close to continue.")

    # Open the temporary file in VS Code
    subprocess.run(["cmd", "/c", "code", "-w", temp_path])
    # The '-w' flag will wait until the file is closed in VS Code
    print("Editing completed. Continuing script execution...")

    # Remove the temporary file
    os.remove(temp_path)


if __name__ == "__main__":
    main()
