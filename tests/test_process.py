# coding: utf-8

import os
import signal
from time import sleep

from unipath import Path

from jplib import clipboard as cb
from jplib import config as cfg
from jplib import process


def test_get_simple_cmd_output():
    res = process.get_simple_cmd_output("echo -n Ubuntu")
    assert str(res) == 'Ubuntu'


def test_get_complex_cmd_output():
    res = process.get_complex_cmd_output("cat /etc/passwd | head -1")
    assert len(res) == 1


def test_get_cmd_output_input_from_stdin():
    res = process.get_cmd_output_input_from_stdin("grep es", "test")
    assert res == 'test\n'
    res = process.get_cmd_output_input_from_stdin("wc -w", "a b c d e")
    assert res == '5\n'


def test_get_return_code_of_simple_cmd():
    assert process.get_return_code_of_simple_cmd("date") == 0
    assert process.get_return_code_of_simple_cmd("date -wrong-option") == 1


def test_get_exitcode_stdout_stderr():
    prg = Path(cfg.TEST_ASSETS_DIR, "process", "exitcode_out_err.py")
    cmd = "python3 {prg}".format(prg=prg)
    exitcode, out, err = process.get_exitcode_stdout_stderr(cmd)
    assert exitcode == 3
    assert out == "árvíztűrő tükörfúrógép"
    assert err == "stderr"


def test_execute_cmd():
    bak_primary = cb.read_primary()
    #
    text = 'arbitrary text'
    cb.to_primary(text)
    assert cb.read_primary() == text
    process.execute_cmd('xsel -pc')    # clear primary
    assert cb.read_primary() == ''
    #
    cb.to_primary(bak_primary)


def test_execute_cmd_in_background():
    """Launch a process in the background then kill it by its pid.
    If the kill was successful, then the process was launched in
    the background correctly."""
    pid = process.execute_cmd_in_background('sleep 101')
    sleep(0.1)
    ret = process.get_return_code_of_simple_cmd("kill {pid}".format(pid=pid))
    assert ret == 0


def test_get_process_list():
    """Launch a process in the background, get its pid, and list
    the running processes. If the given pid is in the list, then
    we had a good list. At the end kill the process."""
    pid = process.execute_cmd_in_background('sleep 102')
    sleep(0.1)
    found = False
    for p in process.get_process_list():
        if p.pid == pid:
            found = True
            break

    assert found
    os.kill(pid, signal.SIGTERM)


def test_keep_alive():
    # TODO
    import psutil
