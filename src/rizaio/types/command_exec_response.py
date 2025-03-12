# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["CommandExecResponse"]


class CommandExecResponse(BaseModel):
    duration: int
    """The execution time of the script in milliseconds."""

    exit_code: int
    """The exit code returned by the script.

    Will often be '0' on success and non-zero on failure.
    """

    stderr: str
    """The contents of 'stderr' after executing the script."""

    stdout: str
    """The contents of 'stdout' after executing the script."""
