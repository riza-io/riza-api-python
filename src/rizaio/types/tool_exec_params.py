# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ToolExecParams", "Env", "HTTP", "HTTPAllow", "HTTPAllowAuth", "HTTPAllowAuthBasic", "HTTPAllowAuthBearer"]


class ToolExecParams(TypedDict, total=False):
    env: Iterable[Env]

    http: Optional[HTTP]

    input: object

    revision_id: str


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


class HTTPAllowAuth(TypedDict, total=False):
    basic: Optional[HTTPAllowAuthBasic]

    bearer: Optional[HTTPAllowAuthBearer]
    """Configuration to add an 'Authorization' header using the 'Bearer' scheme."""


class HTTPAllow(TypedDict, total=False):
    auth: HTTPAllowAuth
    """Authentication configuration for outbound requests to this host."""

    host_desc: Annotated[str, PropertyInfo(alias="host desc:")]


class HTTP(TypedDict, total=False):
    allow: Iterable[HTTPAllow]
    """List of allowed HTTP hosts and associated authentication."""
