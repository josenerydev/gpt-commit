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

def extract_diff_summary(diff):
    """
    Extract a summary from a given git diff.
    """
    # Split diff by files
    diffs = diff.split("diff --git")
    file_diff_summaries = []

    for file_diff in diffs:
        if not file_diff.strip():
            continue
        lines = file_diff.split('\n')
        file_name = lines[0].split(' ')[-1] if lines else None
        if not file_name:
            continue

        # Extract changes for this file
        changes = "\n".join(lines[1:])

        file_diff_summaries.append({
            'file_name': file_name,
            'changes': changes
        })

    return file_diff_summaries

def commit(message):
    # will ignore message if diff is empty
    return subprocess.run(["git", "commit", "--message", message, "--edit"]).returncode
