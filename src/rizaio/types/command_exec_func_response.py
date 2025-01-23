# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CommandExecFuncResponse", "Execution"]


class Execution(BaseModel):
    exit_code: Optional[int] = None
    """The exit code returned by the script.

    Will often be '0' on success and non-zero on failure.
    """

    stderr: Optional[str] = None
    """The contents of 'stderr' after executing the script."""

    stdout: Optional[str] = None
    """The contents of 'stdout' after executing the script."""


class CommandExecFuncResponse(BaseModel):
    execution: Optional[Execution] = None

    output: Optional[object] = None

    output_status: Optional[Literal["error", "json_serialization_error", "valid"]] = None
    """The status of the output.

    "valid" means your function executed successfully and returned a valid
    JSON-serializable object, or void. "json_serialization_error" means your
    function executed successfully, but returned a nonserializable object. "error"
    means your function failed to execute.
    """
