# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CommandExecResponse"]


class CommandExecResponse(BaseModel):
    exit_code: Optional[int] = None
    """The exit code returned by the script.

    Will often be '0' on success and non-zero on failure.
    """

    stderr: Optional[str] = None
    """The contents of 'stderr' after executing the script."""

    stdout: Optional[str] = None
    """The contents of 'stdout' after executing the script."""
