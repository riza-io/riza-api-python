# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["V1ExecuteResponse"]


class V1ExecuteResponse(BaseModel):
    exit_code: Optional[str] = FieldInfo(alias="exitCode", default=None)

    stderr: Optional[str] = None

    stdout: Optional[str] = None
