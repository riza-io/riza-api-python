# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rizaio import Riza, AsyncRiza
from tests.utils import assert_matches_type
from rizaio.types import CodeExecuteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCode:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_execute(self, client: Riza) -> None:
        code = client.code.execute()
        assert_matches_type(CodeExecuteResponse, code, path=["response"])

    @parametrize
    def test_method_execute_with_all_params(self, client: Riza) -> None:
        code = client.code.execute(
            args=["string", "string", "string"],
            code="string",
            env={"foo": "string"},
            language="UNSPECIFIED",
            stdin="string",
        )
        assert_matches_type(CodeExecuteResponse, code, path=["response"])

    @parametrize
    def test_raw_response_execute(self, client: Riza) -> None:
        response = client.code.with_raw_response.execute()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        code = response.parse()
        assert_matches_type(CodeExecuteResponse, code, path=["response"])

    @parametrize
    def test_streaming_response_execute(self, client: Riza) -> None:
        with client.code.with_streaming_response.execute() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            code = response.parse()
            assert_matches_type(CodeExecuteResponse, code, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCode:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_execute(self, async_client: AsyncRiza) -> None:
        code = await async_client.code.execute()
        assert_matches_type(CodeExecuteResponse, code, path=["response"])

    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncRiza) -> None:
        code = await async_client.code.execute(
            args=["string", "string", "string"],
            code="string",
            env={"foo": "string"},
            language="UNSPECIFIED",
            stdin="string",
        )
        assert_matches_type(CodeExecuteResponse, code, path=["response"])

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncRiza) -> None:
        response = await async_client.code.with_raw_response.execute()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        code = await response.parse()
        assert_matches_type(CodeExecuteResponse, code, path=["response"])

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncRiza) -> None:
        async with async_client.code.with_streaming_response.execute() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            code = await response.parse()
            assert_matches_type(CodeExecuteResponse, code, path=["response"])

        assert cast(Any, response.is_closed) is True
