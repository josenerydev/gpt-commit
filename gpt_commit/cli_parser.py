import argparse

def parse_args():
    """
    Extract the CLI arguments from argparse
    """
    parser = argparse.ArgumentParser(
        description=(
            "Generate a commit message for staged files and commit them. "
            "Git will prompt you to edit the generated commit message."
        )
    )
    parser.add_argument(
        "-p",
        "--print-message",
        action="store_true",
        default=False,
        help="print message in place of performing commit",
    )
    return parser.parse_args()
