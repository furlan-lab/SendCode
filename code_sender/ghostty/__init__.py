import os
from ..applescript import osascript

GHOSTTY = os.path.join(os.path.dirname(__file__), "ghostty.applescript")
GHOSTTY_BRACKETED = os.path.join(os.path.dirname(__file__), "ghostty_bracketed.applescript")


def send_to_ghostty(cmd, bracketed=False, commit=True):
    if bracketed:
        osascript(GHOSTTY_BRACKETED, cmd, str(commit))
    else:
        osascript(GHOSTTY, cmd, str(commit))
