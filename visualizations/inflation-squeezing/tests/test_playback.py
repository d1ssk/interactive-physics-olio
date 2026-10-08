"""Exercise playback races against the shipped scripts with a controlled clock."""

import shutil
import subprocess
from pathlib import Path

import pytest


def test_playback_callbacks_do_not_survive_restarts():
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is needed for the JavaScript playback regression tests")
    result = subprocess.run(
        [node, "--test", str(Path(__file__).with_name("playback.test.cjs"))],
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
