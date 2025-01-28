# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = [
    "ToolExecParams",
    "Env",
    "HTTP",
    "HTTPAllow",
    "HTTPAllowAuth",
    "HTTPAllowAuthBasic",
    "HTTPAllowAuthBearer",
    "HTTPAllowAuthQuery",
]


class ToolExecParams(TypedDict, total=False):
    env: Iterable[Env]
    """Set of key-value pairs to add to the tool's execution environment."""

    http: HTTP
    """Configuration for HTTP requests and authentication."""

    input: object
    """The input to the tool.

    This must be a valid JSON-serializable object. It will be validated against the
    tool's input schema.
    """

    revision_id: str
    """The Tool revision ID to execute.

    This optional parmeter is used to pin executions to specific versions of the
    Tool. If not provided, the latest (current) version of the Tool will be
    executed.
    """


class Env(TypedDict, total=False):
    name: Required[str]

    secret_id: str

    value: str


class HTTPAllowAuthBasic(TypedDict, total=False):
    password: str

    secret_id: str

    user_id: str


class HTTPAllowAuthBearer(TypedDict, total=False):
    token: str
    """The token to set, e.g. 'Authorization: Bearer <token>'."""

    secret_id: str


class HTTPAllowAuthQuery(TypedDict, total=False):
    key: str

    secret_id: str

    value: str


class HTTPAllowAuth(TypedDict, total=False):
    basic: HTTPAllowAuthBasic

    bearer: HTTPAllowAuthBearer
    """Configuration to add an 'Authorization' header using the 'Bearer' scheme."""

    query: HTTPAllowAuthQuery


class HTTPAllow(TypedDict, total=False):
    auth: HTTPAllowAuth
    """Authentication configuration for outbound requests to this host."""

    host: str
    """The hostname to allow."""


class HTTP(TypedDict, total=False):
    allow: Iterable[HTTPAllow]
    """List of allowed HTTP hosts and associated authentication."""
