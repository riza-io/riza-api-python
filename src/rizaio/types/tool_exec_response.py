# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ToolExecResponse", "Execution"]


class Execution(BaseModel):
    exit_code: int

    stderr: str

    stdout: str


class ToolExecResponse(BaseModel):
    execution: Execution

    output: Optional[str] = None
