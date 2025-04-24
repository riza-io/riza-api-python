# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ToolListParams"]


class ToolListParams(TypedDict, total=False):
    limit: int
    """The number of items to return. Defaults to 100. Maximum is 100."""

    starting_after: str
    """The ID of the item to start after.

    To get the next page of results, set this to the ID of the last item in the
    current page.
    """
