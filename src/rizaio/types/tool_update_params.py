# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ToolUpdateParams"]


class ToolUpdateParams(TypedDict, total=False):
    code: Optional[str]

    description: Optional[str]

    input_schema: object

    language: Literal["python", "javascript", "typescript"]

    name: Optional[str]
