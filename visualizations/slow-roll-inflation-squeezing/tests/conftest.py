import importlib
import sys
from pathlib import Path
from types import ModuleType

import pytest


@pytest.fixture(scope="session")
def slowroll():
    name = "slow_roll_inflation_squeezing_tests"
    package = ModuleType(name)
    package.__path__ = [str(Path(__file__).resolve().parents[1])]
    sys.modules[name] = package
    return importlib.import_module(f"{name}.physics")


@pytest.fixture(scope="session")
def builder(slowroll):
    return importlib.import_module("slow_roll_inflation_squeezing_tests.visualization")


@pytest.fixture(scope="session")
def backgrounds(slowroll):
    return {key: slowroll.solve_background(model) for key, model in slowroll.MODELS.items()}
