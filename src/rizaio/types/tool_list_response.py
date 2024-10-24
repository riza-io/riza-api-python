# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .tool import Tool
from .._models import BaseModel

__all__ = ["ToolListResponse"]


class ToolListResponse(BaseModel):
    tools: Optional[List[Tool]] = None
