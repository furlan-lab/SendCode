import os
import subprocess


def _resolve_cmux(cmux):
    if os.path.isabs(cmux):
        return cmux
    # Sublime Text may not have /opt/homebrew/bin in PATH
    for p in ["/opt/homebrew/bin/cmux", "/usr/local/bin/cmux"]:
        if os.path.isfile(p):
            return p
    return cmux


def _send_to_cmux(cmd, cmux, surface=None):
    n = 200
    chunks = [cmd[i:i+n] for i in range(0, len(cmd), n)]
    for chunk in chunks:
        args = [cmux, 'send']
        if surface:
            args.extend(['--surface', surface])
        args.append(chunk)
        subprocess.check_call(args)


def _send_key_to_cmux(key, cmux, surface=None):
    args = [cmux, 'send-key']
    if surface:
        args.extend(['--surface', surface])
    args.append(key)
    subprocess.check_call(args)


def send_to_cmux(cmd, cmux="cmux", surface=None, bracketed=False, commit=True):
    cmux = _resolve_cmux(cmux)
    if bracketed:
        _send_to_cmux("\x1b[200~", cmux, surface)
        _send_to_cmux(cmd, cmux, surface)
        _send_to_cmux("\x1b[201~", cmux, surface)
        if commit:
            _send_key_to_cmux("enter", cmux, surface)
    else:
        _send_to_cmux(cmd, cmux, surface)
        if commit and cmd != "\x04":
            _send_key_to_cmux("enter", cmux, surface)
