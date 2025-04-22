# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Generic, TypeVar, Optional, cast
from typing_extensions import Protocol, override, runtime_checkable

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncRuntimesPagination",
    "AsyncRuntimesPagination",
    "SyncToolsPagination",
    "AsyncToolsPagination",
    "SyncSecretsPagination",
    "AsyncSecretsPagination",
]

_T = TypeVar("_T")


@runtime_checkable
class RuntimesPaginationItem(Protocol):
    id: str


@runtime_checkable
class ToolsPaginationItem(Protocol):
    id: str


@runtime_checkable
class SecretsPaginationItem(Protocol):
    id: str


class SyncRuntimesPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    runtimes: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        runtimes = self.runtimes
        if not runtimes:
            return []
        return runtimes

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        runtimes = self.runtimes
        if not runtimes:
            return None

        item = cast(Any, runtimes[-1])
        if not isinstance(item, RuntimesPaginationItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
            # TODO emit warning log
            return None

        return PageInfo(params={"starting_after": item.id})


class AsyncRuntimesPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    runtimes: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        runtimes = self.runtimes
        if not runtimes:
            return []
        return runtimes

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        runtimes = self.runtimes
        if not runtimes:
            return None

        item = cast(Any, runtimes[-1])
        if not isinstance(item, RuntimesPaginationItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
            # TODO emit warning log
            return None

        return PageInfo(params={"starting_after": item.id})


class SyncToolsPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    tools: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        tools = self.tools
        if not tools:
            return []
        return tools

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        tools = self.tools
        if not tools:
            return None

        item = cast(Any, tools[-1])
        if not isinstance(item, ToolsPaginationItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
            # TODO emit warning log
            return None

        return PageInfo(params={"starting_after": item.id})


class AsyncToolsPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    tools: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        tools = self.tools
        if not tools:
            return []
        return tools

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        tools = self.tools
        if not tools:
            return None

        item = cast(Any, tools[-1])
        if not isinstance(item, ToolsPaginationItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
            # TODO emit warning log
            return None

        return PageInfo(params={"starting_after": item.id})


class SyncSecretsPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    secrets: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        secrets = self.secrets
        if not secrets:
            return []
        return secrets

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        secrets = self.secrets
        if not secrets:
            return None

        item = cast(Any, secrets[-1])
        if not isinstance(item, SecretsPaginationItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
            # TODO emit warning log
            return None

        return PageInfo(params={"starting_after": item.id})


class AsyncSecretsPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    secrets: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        secrets = self.secrets
        if not secrets:
            return []
        return secrets

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        secrets = self.secrets
        if not secrets:
            return None

        item = cast(Any, secrets[-1])
        if not isinstance(item, SecretsPaginationItem) or item.id is None:  # pyright: ignore[reportUnnecessaryComparison]
            # TODO emit warning log
            return None

        return PageInfo(params={"starting_after": item.id})
