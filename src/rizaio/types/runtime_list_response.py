# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .runtime import Runtime
from .._models import BaseModel

__all__ = ["RuntimeListResponse"]


class RuntimeListResponse(BaseModel):
    runtimes: List[Runtime]
