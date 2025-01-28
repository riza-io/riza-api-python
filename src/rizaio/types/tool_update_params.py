# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ToolUpdateParams"]


class ToolUpdateParams(TypedDict, total=False):
    code: str
    """The code of the tool.

    You must define a function named "execute" that takes in a single argument and
    returns a JSON-serializable value. The argument will be the "input" passed when
    executing the tool, and will match the input schema.
    """

    description: str
    """A description of the tool."""

    input_schema: object
    """The input schema of the tool. This must be a valid JSON Schema object."""

    language: Literal["python", "javascript", "typescript"]
    """The language of the tool's code."""

    name: str
    """The name of the tool."""

    runtime_revision_id: str
    """The ID of the custom runtime revision that the tool uses for executions.

    This is used to pin executions to a specific version of a custom runtime, even
    if the runtime is updated later.
    """
