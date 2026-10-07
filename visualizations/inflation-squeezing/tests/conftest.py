import importlib
import sys
from pathlib import Path
from types import ModuleType

import pytest


@pytest.fixture(scope="session")
def inflation():
    name = "inflation_squeezing_tests"
    package = ModuleType(name)
    package.__path__ = [str(Path(__file__).resolve().parents[1])]
    sys.modules[name] = package
    return importlib.import_module(f"{name}.physics")


@pytest.fixture(scope="session")
def builder(inflation):
    return importlib.import_module("inflation_squeezing_tests.visualization")
