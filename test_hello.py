import subprocess
import pytest

def test_no_arguments():
    result = subprocess.run(['python3', 'hello.py'], stdout=subprocess.PIPE)
    assert result.stdout == b'Hello, GitHub Codespaces!\n'
