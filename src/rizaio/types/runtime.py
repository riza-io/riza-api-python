# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Runtime", "ManifestFile"]


class ManifestFile(BaseModel):
    contents: str

    name: Literal["requirements.txt", "package.json"]


class Runtime(BaseModel):
    id: str

    language: Literal["python", "javascript"]

    name: str

    revision_id: str

    status: Literal["pending", "building", "succeeded", "failed", "cancelled"]

    additional_python_imports: Optional[str] = None

    manifest_file: Optional[ManifestFile] = None
