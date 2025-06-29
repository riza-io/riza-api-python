# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["RuntimeDeleteResponse"]


class RuntimeDeleteResponse(BaseModel):
    id: Optional[str] = None

    deleted: Optional[bool] = None
