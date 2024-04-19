# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SandboxExecuteParams"]


class SandboxExecuteParams(TypedDict, total=False):
    code: Required[str]
    """The code to execute in the sandbox."""

    language: Required[Literal["PYTHON", "JAVASCRIPT", "TYPESCRIPT", "RUBY", "PHP"]]
    """The interpreter to use when executing code."""

    args: List[str]
    """List of command line arguments to pass to the script."""

    env: Dict[str, str]
    """Set of key-value pairs to add to the script's execution environment."""

    stdin: str
    """Input to pass to the script via `stdin`."""
