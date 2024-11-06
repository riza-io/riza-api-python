# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Tool"]


class Tool(BaseModel):
    id: str

    code: str

    description: str

    input_schema: object

    language: Literal["PYTHON", "JAVASCRIPT", "TYPESCRIPT", "RUBY", "PHP"]

    name: str

    revision_id: str
