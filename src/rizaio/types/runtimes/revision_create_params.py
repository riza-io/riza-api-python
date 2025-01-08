# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RevisionCreateParams", "ManifestFile"]


class RevisionCreateParams(TypedDict, total=False):
    manifest_file: Required[ManifestFile]

    additional_python_imports: str


class ManifestFile(TypedDict, total=False):
    contents: Required[str]

    name: Required[Literal["requirements.txt", "package.json"]]
