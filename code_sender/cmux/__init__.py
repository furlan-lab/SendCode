import subprocess


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
    if surface:
        subprocess.check_call([cmux, 'send-key-surface', surface, key])
    else:
        subprocess.check_call([cmux, 'send-key', key])


def send_to_cmux(cmd, cmux="cmux", surface=None, bracketed=False, commit=True):
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
