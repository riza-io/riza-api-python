# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Tool"]


class Tool(BaseModel):
    id: str
    """The ID of the tool."""

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

    revision_id: str
    """The ID of the tool's current revision.

    This is used to pin executions to a specific version of the tool, even if the
    tool is updated later.
    """

    runtime_revision_id: Optional[str] = None
    """The ID of the custom runtime revision that the tool uses for executions.

    This pins executions to specific version of a custom runtime runtime, even if
    the runtime is updated later.
    """
