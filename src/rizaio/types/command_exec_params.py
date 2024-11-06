# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "CommandExecParams",
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


class CommandExecParams(TypedDict, total=False):
    code: Required[str]
    """The code to execute."""

    allow_http_hosts: List[str]
    """List of allowed hosts for HTTP requests."""

    args: List[str]
    """List of command line arguments to pass to the script."""

    env: Dict[str, str]
    """Set of key-value pairs to add to the script's execution environment."""

    files: Iterable[File]
    """List of input files."""

    http: Optional[HTTP]
    """Configuration for HTTP requests and authentication."""

    language: Literal["PYTHON", "JAVASCRIPT", "TYPESCRIPT", "RUBY", "PHP"]
    """The interpreter to use when executing code."""

    limits: Optional[Limits]
    """Configuration for execution environment limits."""

    revision: str

    runtime: str
    """The runtime to use when executing code."""

    stdin: str
    """Input made available to the script via 'stdin'."""


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
