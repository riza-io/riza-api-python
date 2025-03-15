# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Revision", "ManifestFile"]


class ManifestFile(BaseModel):
    contents: str

    name: Literal["requirements.txt", "package.json"]


class Revision(BaseModel):
    id: str

    manifest_file: ManifestFile

    runtime_id: str

    status: Literal["pending", "building", "succeeded", "failed", "cancelled"]

    additional_python_imports: Optional[str] = None
