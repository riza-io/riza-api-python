# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolCreateParams"]


class ToolCreateParams(TypedDict, total=False):
    code: Required[str]

    language: Required[Literal["python", "javascript", "typescript"]]

    name: Required[str]

    description: str

    input_schema: object
