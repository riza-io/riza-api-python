# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "CommandExecFuncParams",
    "File",
    "HTTP",
    "HTTPAllow",
    "HTTPAllowAuth",
    "HTTPAllowAuthBasic",
    "HTTPAllowAuthBearer",
    "HTTPAllowAuthHeader",
    "HTTPAllowAuthQuery",
    "Limits",
]


class CommandExecFuncParams(TypedDict, total=False):
    code: Required[str]
    """The function to execute.

    Your code must define a function named 'execute' and return a JSON-serializable
    value.
    """

    language: Required[Literal["python", "javascript", "typescript", "ruby", "php"]]
    """The interpreter to use when executing code."""

    env: Dict[str, str]
    """Set of key-value pairs to add to the script's execution environment."""

    files: Iterable[File]
    """List of input files."""

    http: Optional[HTTP]
    """Configuration for HTTP requests and authentication."""

    input: object

    limits: Optional[Limits]
    """Configuration for execution environment limits."""

    runtime_revision_id: str
    """The ID of the runtime revision to use when executing code."""


class File(TypedDict, total=False):
    contents: str
    """The contents of the file."""

    path: str
    """The relative path of the file."""


class HTTPAllowAuthBasic(TypedDict, total=False):
    password: str

    user_id: str


class HTTPAllowAuthBearer(TypedDict, total=False):
    token: str
    """The token to set, e.g. 'Authorization: Bearer <token>'."""


class HTTPAllowAuthHeader(TypedDict, total=False):
    name: str

    value: str


class HTTPAllowAuthQuery(TypedDict, total=False):
    key: str

    value: str


class HTTPAllowAuth(TypedDict, total=False):
    basic: Optional[HTTPAllowAuthBasic]

    bearer: Optional[HTTPAllowAuthBearer]
    """Configuration to add an 'Authorization' header using the 'Bearer' scheme."""

    header: Optional[HTTPAllowAuthHeader]

    query: Optional[HTTPAllowAuthQuery]


class HTTPAllow(TypedDict, total=False):
    auth: HTTPAllowAuth
    """Authentication configuration for outbound requests to this host."""

    host: str
    """The hostname to allow."""


class HTTP(TypedDict, total=False):
    allow: Iterable[HTTPAllow]
    """List of allowed HTTP hosts and associated authentication."""


class Limits(TypedDict, total=False):
    execution_timeout: int
    """The maximum time allowed for execution (in seconds). Default is 30."""

    memory_size: int
    """The maximum memory allowed for execution (in MiB). Default is 128."""
