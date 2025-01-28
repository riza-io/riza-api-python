# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolCreateParams"]


class ToolCreateParams(TypedDict, total=False):
    code: Required[str]
    """The code of the tool.

    You must define a function named "execute" that takes in a single argument and
    returns a JSON-serializable value. The argument will be the "input" passed when
    executing the tool, and will match the input schema.
    """

    language: Required[Literal["python", "javascript", "typescript"]]
    """The language of the tool's code."""

    name: Required[str]
    """The name of the tool."""

    description: str
    """A description of the tool."""

    input_schema: object
    """The input schema of the tool. This must be a valid JSON Schema object."""

    runtime_revision_id: str
    """The ID of the runtime revision to use when executing the tool."""
