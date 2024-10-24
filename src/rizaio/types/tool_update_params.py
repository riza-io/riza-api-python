# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ToolUpdateParams"]


class ToolUpdateParams(TypedDict, total=False):
    code: Optional[str]

    description: Optional[str]

    input_schema: Optional[object]

    language: Literal["PYTHON", "JAVASCRIPT", "TYPESCRIPT", "RUBY", "PHP"]

    name: Optional[str]
