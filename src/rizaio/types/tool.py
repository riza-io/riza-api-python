# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

    language: Literal["python", "javascript", "typescript"]
    """The language of the tool's code."""

    name: str
    """The name of the tool."""

    revision_id: str
    """The ID of the tool's current revision.

    This is used to pin executions to specific versions of the Tool, even if the
    Tool is updated later.
    """
