# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExecutionListParams"]


class ExecutionListParams(TypedDict, total=False):
    limit: int
    """The number of items to return. Defaults to 100. Maximum is 100."""

    only_non_zero_exit_codes: bool
    """
    If true, only show executions where the exit code is not 0, indicating an
    execution error. Defaults to false.
    """

    starting_after: str
    """The ID of the item to start after.

    To get the next page of results, set this to the ID of the last item in the
    current page.
    """
