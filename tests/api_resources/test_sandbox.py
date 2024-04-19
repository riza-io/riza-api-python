# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rizaio import Riza, AsyncRiza
from tests.utils import assert_matches_type
from rizaio.types import SandboxExecuteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSandbox:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_execute(self, client: Riza) -> None:
        sandbox = client.sandbox.execute(
            code='print("Hello world!")',
            language="PYTHON",
        )
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @parametrize
    def test_method_execute_with_all_params(self, client: Riza) -> None:
        sandbox = client.sandbox.execute(
            code='print("Hello world!")',
            language="PYTHON",
            args=["string", "string", "string"],
            env={"foo": "string"},
            stdin="string",
        )
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @parametrize
    def test_raw_response_execute(self, client: Riza) -> None:
        response = client.sandbox.with_raw_response.execute(
            code='print("Hello world!")',
            language="PYTHON",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @parametrize
    def test_streaming_response_execute(self, client: Riza) -> None:
        with client.sandbox.with_streaming_response.execute(
            code='print("Hello world!")',
            language="PYTHON",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSandbox:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_execute(self, async_client: AsyncRiza) -> None:
        sandbox = await async_client.sandbox.execute(
            code='print("Hello world!")',
            language="PYTHON",
        )
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncRiza) -> None:
        sandbox = await async_client.sandbox.execute(
            code='print("Hello world!")',
            language="PYTHON",
            args=["string", "string", "string"],
            env={"foo": "string"},
            stdin="string",
        )
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncRiza) -> None:
        response = await async_client.sandbox.with_raw_response.execute(
            code='print("Hello world!")',
            language="PYTHON",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncRiza) -> None:
        async with async_client.sandbox.with_streaming_response.execute(
            code='print("Hello world!")',
            language="PYTHON",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True
