import subprocess

def get_diff(ignore_whitespace=True):
    arguments = [
        "git",
        "--no-pager",
        "diff",
        "--staged",
    ]
    if ignore_whitespace:
        arguments += [
            "--ignore-space-change",
            "--ignore-blank-lines",
        ]
    diff_process = subprocess.run(arguments, capture_output=True, text=True, encoding='utf-8')
    diff_process.check_returncode()
    return diff_process.stdout.strip() if diff_process.stdout else None

def commit(message):
    # will ignore message if diff is empty
    return subprocess.run(["git", "commit", "--message", message, "--edit"]).returncode
