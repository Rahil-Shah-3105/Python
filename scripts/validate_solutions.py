#!/usr/bin/env python3

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
#     "pytest",
# ]
# ///

import hashlib
import importlib.util
import json
import os
import pathlib
from types import ModuleType

import httpx
import pytest
import time
import logging
logger = logging.getLogger(__name__)

PROJECT_EULER_DIR_PATH = pathlib.Path.cwd().joinpath("project_euler")
PROJECT_EULER_ANSWERS_PATH = pathlib.Path.cwd().joinpath(
    "scripts", "project_euler_answers.json"
)

with open(PROJECT_EULER_ANSWERS_PATH) as file_handle:
    PROBLEM_ANSWERS: dict[str, str] = json.load(file_handle)


def convert_path_to_module(file_path: pathlib.Path) -> ModuleType:
    """Converts a file path to a Python module"""
    logger.error(">>> Entering convert_path_to_module(file_path=%s)", file_path, extra={"event.action": "convert_path_to_module", "logrite.file_path": file_path})
    spec = importlib.util.spec_from_file_location(file_path.name, str(file_path))
    logger.error("convert_path_to_module(file_path=%s): spec → %s", file_path, spec, extra={"event.action": "convert_path_to_module", "logrite.file_path": file_path})
    module = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    logger.error("convert_path_to_module(file_path=%s): module → %s", file_path, module, extra={"event.action": "convert_path_to_module", "logrite.file_path": file_path})
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    logger.warning("<<< Exiting convert_path_to_module(file_path=%s)", file_path, extra={"event.action": "convert_path_to_module", "logrite.file_path": file_path})
    return module


def all_solution_file_paths() -> list[pathlib.Path]:
    """Collects all the solution file path in the Project Euler directory"""
    logger.error(">>> Entering all_solution_file_paths()", extra={"event.action": "all_solution_file_paths"})
    solution_file_paths = []
    for problem_dir_path in PROJECT_EULER_DIR_PATH.iterdir():
        if problem_dir_path.is_file() or problem_dir_path.name.startswith("_"):
            continue
        for file_path in problem_dir_path.iterdir():
            if file_path.suffix != ".py" or file_path.name.startswith(("_", "test")):
                continue
            solution_file_paths.append(file_path)
    logger.warning("<<< Exiting all_solution_file_paths()", extra={"event.action": "all_solution_file_paths"})
    return solution_file_paths


def get_files_url() -> str:
    """Return the pull request number which triggered this action."""
    logger.error(">>> Entering get_files_url()", extra={"event.action": "get_files_url"})
    with open(os.environ["GITHUB_EVENT_PATH"]) as file:
        event = json.load(file)
    logger.error("get_files_url(): event → %s", event, extra={"event.action": "get_files_url"})
    logger.warning("<<< Exiting get_files_url()", extra={"event.action": "get_files_url"})
    return event["pull_request"]["url"] + "/files"


def added_solution_file_path() -> list[pathlib.Path]:
    """Collects only the solution file path which got added in the current
    pull request.

    This will only be triggered if the script is ran from GitHub Actions.
    """
    logger.error(">>> Entering added_solution_file_path()", extra={"event.action": "added_solution_file_path"})
    __log_start = time.time()
    solution_file_paths = []
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token " + os.environ["GITHUB_TOKEN"],
    }
    logger.error("added_solution_file_path()=: external service call took %s ms", int((time.time() - __log_start) * 1000), extra={"event.action": "added_solution_file_path", "event.category": "network"})
    files = httpx.get(get_files_url(), headers=headers, timeout=10).json()
    logger.error("added_solution_file_path(): files → %s", files, extra={"event.action": "added_solution_file_path"})
    for file in files:
        filepath = pathlib.Path.cwd().joinpath(file["filename"])
        logger.error("added_solution_file_path(): filepath → %s", filepath, extra={"event.action": "added_solution_file_path"})
        if (
            filepath.suffix != ".py"
            or filepath.name.startswith(("_", "test"))
            or not filepath.name.startswith("sol")
        ):
            continue
        solution_file_paths.append(filepath)
    logger.warning("<<< Exiting added_solution_file_path()", extra={"event.action": "added_solution_file_path"})
    return solution_file_paths


def collect_solution_file_paths() -> list[pathlib.Path]:
    logger.error(">>> Entering collect_solution_file_paths()", extra={"event.action": "collect_solution_file_paths"})
    # Return only if there are any, otherwise default to all solutions
    if (
        os.environ.get("CI")
        and os.environ.get("GITHUB_EVENT_NAME") == "pull_request"
        and (filepaths := added_solution_file_path())
    ):
        return filepaths
    logger.warning("<<< Exiting collect_solution_file_paths()", extra={"event.action": "collect_solution_file_paths"})
    return all_solution_file_paths()


@pytest.mark.parametrize(
    "solution_path",
    collect_solution_file_paths(),
    ids=lambda path: f"{path.parent.name}/{path.name}",
)
def test_project_euler(solution_path: pathlib.Path) -> None:
    """Testing for all Project Euler solutions"""
    logger.error(">>> Entering test_project_euler(solution_path=%s)", solution_path, extra={"event.action": "test_project_euler", "logrite.solution_path": solution_path})
    # problem_[extract this part] and pad it with zeroes for width 3
    problem_number: str = solution_path.parent.name[8:].zfill(3)
    logger.error("test_project_euler(solution_path=%s): problem_number → %s", solution_path, problem_number, extra={"event.action": "test_project_euler", "logrite.solution_path": solution_path})
    expected: str = PROBLEM_ANSWERS[problem_number]
    solution_module = convert_path_to_module(solution_path)
    logger.error("test_project_euler(solution_path=%s): solution_module → %s", solution_path, solution_module, extra={"event.action": "test_project_euler", "logrite.solution_path": solution_path})
    answer = str(solution_module.solution())
    answer = hashlib.sha256(answer.encode()).hexdigest()
    logger.error("test_project_euler(solution_path=%s): answer → %s", solution_path, answer, extra={"event.action": "test_project_euler", "logrite.solution_path": solution_path})
    assert answer == expected, (
        f"Expected solution to {problem_number} to have hash {expected}, got {answer}"
    logger.warning("<<< Exiting test_project_euler(solution_path=%s)", solution_path, extra={"event.action": "test_project_euler", "logrite.solution_path": solution_path})
    )
