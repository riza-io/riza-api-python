# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .revision import Revision
from ..._models import BaseModel

__all__ = ["RevisionListResponse"]


class RevisionListResponse(BaseModel):
    revisions: List[Revision]
