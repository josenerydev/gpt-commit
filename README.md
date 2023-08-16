# gpt-commit 🚀

`gpt-commit` is a command-line tool that intelligently generates commit messages based on staged file changes in Git. It utilizes OpenAI's GPT model to craft concise and descriptive commit messages.

## Prerequisites 📋

- Python
- A valid OpenAI API key

## Installation 🛠️

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/gpt-commit.git
   ```

2. Navigate to the project directory:
   ```bash
   cd gpt-commit/
   ```

3. Install the package:
   ```bash
   pip install .
   ```

   For developers: If you're making changes and want to reflect them immediately, install in editable mode:
   ```bash
   pip install -e .
   ```

## Update ⬆️

To upgrade the tool to the latest version:
```bash
pip install --upgrade .
```

## Uninstallation ❌

To uninstall the tool:
```bash
pip uninstall gpt-commit
```

## Configuration ⚙️

Before using the tool, you need to set up your OpenAI API key.

### On Windows (PowerShell):

Run the `setupEnvironmentVariables.ps1` script:
```powershell
.\setupEnvironmentVariables.ps1 -openaiKey YOUR_OPENAI_API_KEY
```

### On Linux/Mac:

Run the `setupEnvironmentVariables.sh` script:
```bash
./setupEnvironmentVariables.sh YOUR_OPENAI_API_KEY
```

Remember to replace `YOUR_OPENAI_API_KEY` with your actual API key.

## Usage 🚀

After installation, you can use the `gpt-commit` tool anywhere in your system:

```bash
gpt-commit
```

Running the above command will analyze changes in staged files in Git and generate a commit message. This message will then be opened in Git's default editor for review or editing. After reviewing the message, save and close the editor to finalize the commit.

For help on available options:

```bash
gpt-commit --help
```