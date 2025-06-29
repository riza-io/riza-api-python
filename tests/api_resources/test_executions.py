# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rizaio import Riza, AsyncRiza
from tests.utils import assert_matches_type
from rizaio.types import Execution
from rizaio.pagination import SyncDefaultPagination, AsyncDefaultPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Riza) -> None:
        execution = client.executions.list()
        assert_matches_type(SyncDefaultPagination[Execution], execution, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Riza) -> None:
        execution = client.executions.list(
            limit=0,
            only_non_zero_exit_codes=True,
            starting_after="starting_after",
        )
        assert_matches_type(SyncDefaultPagination[Execution], execution, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Riza) -> None:
        response = client.executions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(SyncDefaultPagination[Execution], execution, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Riza) -> None:
        with client.executions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(SyncDefaultPagination[Execution], execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Riza) -> None:
        execution = client.executions.get(
            "id",
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Riza) -> None:
        response = client.executions.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Riza) -> None:
        with client.executions.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(Execution, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Riza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.executions.with_raw_response.get(
                "",
            )


class TestAsyncExecutions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncRiza) -> None:
        execution = await async_client.executions.list()
        assert_matches_type(AsyncDefaultPagination[Execution], execution, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRiza) -> None:
        execution = await async_client.executions.list(
            limit=0,
            only_non_zero_exit_codes=True,
            starting_after="starting_after",
        )
        assert_matches_type(AsyncDefaultPagination[Execution], execution, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRiza) -> None:
        response = await async_client.executions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(AsyncDefaultPagination[Execution], execution, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRiza) -> None:
        async with async_client.executions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(AsyncDefaultPagination[Execution], execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncRiza) -> None:
        execution = await async_client.executions.get(
            "id",
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncRiza) -> None:
        response = await async_client.executions.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncRiza) -> None:
        async with async_client.executions.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(Execution, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncRiza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.executions.with_raw_response.get(
                "",
            )
