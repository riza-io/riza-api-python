# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from riza import Riza, AsyncRiza
from riza.types import V1ExecuteResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV1:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_execute(self, client: Riza) -> None:
        v1 = client.v1.execute()
        assert_matches_type(V1ExecuteResponse, v1, path=["response"])

    @parametrize
    def test_method_execute_with_all_params(self, client: Riza) -> None:
        v1 = client.v1.execute(
            args=["string", "string", "string"],
            code="string",
            env={"foo": "string"},
            language="UNSPECIFIED",
            stdin="string",
        )
        assert_matches_type(V1ExecuteResponse, v1, path=["response"])

    @parametrize
    def test_raw_response_execute(self, client: Riza) -> None:
        response = client.v1.with_raw_response.execute()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = response.parse()
        assert_matches_type(V1ExecuteResponse, v1, path=["response"])

    @parametrize
    def test_streaming_response_execute(self, client: Riza) -> None:
        with client.v1.with_streaming_response.execute() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = response.parse()
            assert_matches_type(V1ExecuteResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncV1:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_execute(self, async_client: AsyncRiza) -> None:
        v1 = await async_client.v1.execute()
        assert_matches_type(V1ExecuteResponse, v1, path=["response"])

    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncRiza) -> None:
        v1 = await async_client.v1.execute(
            args=["string", "string", "string"],
            code="string",
            env={"foo": "string"},
            language="UNSPECIFIED",
            stdin="string",
        )
        assert_matches_type(V1ExecuteResponse, v1, path=["response"])

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncRiza) -> None:
        response = await async_client.v1.with_raw_response.execute()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v1 = await response.parse()
        assert_matches_type(V1ExecuteResponse, v1, path=["response"])

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncRiza) -> None:
        async with async_client.v1.with_streaming_response.execute() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v1 = await response.parse()
            assert_matches_type(V1ExecuteResponse, v1, path=["response"])

        assert cast(Any, response.is_closed) is True
