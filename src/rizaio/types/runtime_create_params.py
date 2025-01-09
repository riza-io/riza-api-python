# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuntimeCreateParams", "ManifestFile"]


class RuntimeCreateParams(TypedDict, total=False):
    language: Required[Literal["python", "javascript"]]

    manifest_file: Required[ManifestFile]

    name: Required[str]

    additional_python_imports: str


class ManifestFile(TypedDict, total=False):
    contents: Required[str]

    name: Required[Literal["requirements.txt", "package.json"]]
