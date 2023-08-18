#!/usr/bin/env python3

import asyncio
import sys
from .git_utils import get_diff, commit
from .openai_utils import generate_single_commit_message
from .cli_parser import parse_args

async def async_main():
    args = parse_args()

    try:
        diff_content = get_diff(ignore_whitespace=False)
        if not diff_content:
            print(
                "No changes staged. Use `git add` to stage files before invoking gpt-commit."
            )
            exit()
        commit_message = await generate_single_commit_message(diff_content)
    except UnicodeDecodeError:
        print("gpt-commit does not support binary files", file=sys.stderr)
        commit_message = (
            "# gpt-commit does not support binary files. "
            "Please enter a commit message manually or unstage any binary files."
        )

    if args.print_message:
        print(commit_message)
    else:
        exit(commit(commit_message))

def main():
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
