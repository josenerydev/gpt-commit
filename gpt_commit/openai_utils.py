import os
import openai
from .diff_utils import parse_diff, assemble_diffs
from .conventional_commits import CONVENTIONAL_COMMITS
import asyncio

DIFF_PROMPT = "Generate a succinct summary of the following code changes:"
COMMIT_MSG_PROMPT = (
    "Using no more than 50 characters, "
    "generate a descriptive commit message from these summaries:"
)
PROMPT_CUTOFF = 10000

openai.organization = os.getenv("OPENAI_ORG_ID")
openai.api_key = os.environ["OPENAI_API_KEY"]

async def complete(prompt):
    model_name = "gpt-3.5-turbo"

    print(f"Using AI model: {model_name}")
    print("----- Start of Prompt -----")
    print(prompt)
    print("----- End of Prompt -----")

    completion_resp = await openai.ChatCompletion.acreate(
        model=model_name,
        messages=[{"role": "user", "content": prompt[: PROMPT_CUTOFF + 100]}],
        max_tokens=128,
    )
    completion = completion_resp.choices[0].message.content.strip()

    print("----- Start of OpenAI Response -----")
    print(completion)
    print("----- End of OpenAI Response -----")

    return completion


async def summarize_diff(diff):
    assert diff
    return await complete(DIFF_PROMPT + "\n\n" + diff + "\n\n")

async def summarize_summaries(summaries):
    assert summaries
    return await complete(COMMIT_MSG_PROMPT + "\n\n" + summaries + "\n\n")

async def summarize_file_changes(file_diff_summaries):
    """
    Summarize changes in each file using OpenAI.
    """
    summaries = []
    for file_diff in file_diff_summaries:
        file_name = file_diff['file_name']
        changes = file_diff['changes']

        prompt = (f"You are a proficient code analyst and you can interpret complex changes efficiently. "
                  f"I have a Git diff from the file {file_name} that details some code modifications: {changes}. "
                  f"Can you provide an insightful summary of these alterations, focusing on the core components affected, "
                  f"the objectives behind them, and possible impacts? Your concise yet comprehensive summation should "
                  f"assist non-technical users in understanding these updates clearly.")

        summary = await complete(prompt)
        summaries.append({
            'file_name': file_name,
            'summary': summary
        })

    return summaries

async def generate_single_commit_message(summaries):
    """
    Convert summaries into a format that can be used in the new prompt
    """
    summarized_diff = "\n".join([f"{summary['file_name']}: {summary['summary']}" for summary in summaries])

    prompt = (f"Consider yourself as an experienced software engineer. You are well versed in using the guide "
              f"[{CONVENTIONAL_COMMITS}] to communicate commit messages effectively and professionally. "
              f"Your current goal is to analyze a summarized diff file provided by me, identified as "
              f"[{summarized_diff}], and create an insightful commit message based on this analysis. "
              f"While crafting the commit message, it's essential that you maintain good practice; ensure your commit "
              f"title stays around 50 characters while the body and footer(s) should be wrapped at approximately 72 characters. Limit your commit message to 50 characters per line."
              f"Do not provide any extra explanations or additional details; just draft one sample commit message as per the given requirements.")

    return await complete(prompt)

async def generate_commit_message(diff):
    if not diff:
        return "Fix whitespace"
    assembled_diffs = assemble_diffs(parse_diff(diff), PROMPT_CUTOFF)
    summaries = await asyncio.gather(
        *[summarize_diff(diff) for diff in assembled_diffs]
    )
    return await summarize_summaries("\n".join(summaries))
