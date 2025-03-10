# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolExecResponse", "Execution"]


class Execution(BaseModel):
    duration: int
    """The execution time of the function in milliseconds."""

    exit_code: int
    """The exit code returned by the function.

    Will often be '0' on success and non-zero on failure.
    """

    stderr: str
    """The contents of 'stderr' after executing the function."""

    stdout: str
    """The contents of 'stdout' after executing the function."""


class ToolExecResponse(BaseModel):
    execution: Execution
    """The execution details of the function."""

    output: object
    """The returned value of the Tool's execute function."""

    output_status: Literal["error", "json_serialization_error", "valid"]
    """The status of the output.

    "valid" means your Tool executed successfully and returned a valid
    JSON-serializable object, or void. "json_serialization_error" means your Tool
    executed successfully, but returned a nonserializable object. "error" means your
    Tool failed to execute.
    """
