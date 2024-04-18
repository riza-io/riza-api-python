# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, TypedDict

__all__ = ["V1ExecuteParams"]


class V1ExecuteParams(TypedDict, total=False):
    args: List[str]

    code: str

    env: Dict[str, str]

    language: Literal["UNSPECIFIED", "PYTHON", "JAVASCRIPT", "TYPESCRIPT", "RUBY", "PHP"]

    stdin: str
