# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rizaio import Riza, AsyncRiza
from tests.utils import assert_matches_type
from rizaio.types import Runtime, RuntimeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuntimes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Riza) -> None:
        runtime = client.runtimes.create(
            language="python",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
            name="name",
        )
        assert_matches_type(Runtime, runtime, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Riza) -> None:
        runtime = client.runtimes.create(
            language="python",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
            name="name",
            additional_python_imports="additional_python_imports",
        )
        assert_matches_type(Runtime, runtime, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Riza) -> None:
        response = client.runtimes.with_raw_response.create(
            language="python",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runtime = response.parse()
        assert_matches_type(Runtime, runtime, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Riza) -> None:
        with client.runtimes.with_streaming_response.create(
            language="python",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runtime = response.parse()
            assert_matches_type(Runtime, runtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Riza) -> None:
        runtime = client.runtimes.list()
        assert_matches_type(RuntimeListResponse, runtime, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Riza) -> None:
        response = client.runtimes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runtime = response.parse()
        assert_matches_type(RuntimeListResponse, runtime, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Riza) -> None:
        with client.runtimes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runtime = response.parse()
            assert_matches_type(RuntimeListResponse, runtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Riza) -> None:
        runtime = client.runtimes.get(
            "id",
        )
        assert_matches_type(Runtime, runtime, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Riza) -> None:
        response = client.runtimes.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runtime = response.parse()
        assert_matches_type(Runtime, runtime, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Riza) -> None:
        with client.runtimes.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runtime = response.parse()
            assert_matches_type(Runtime, runtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Riza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.runtimes.with_raw_response.get(
                "",
            )


class TestAsyncRuntimes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncRiza) -> None:
        runtime = await async_client.runtimes.create(
            language="python",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
            name="name",
        )
        assert_matches_type(Runtime, runtime, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRiza) -> None:
        runtime = await async_client.runtimes.create(
            language="python",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
            name="name",
            additional_python_imports="additional_python_imports",
        )
        assert_matches_type(Runtime, runtime, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRiza) -> None:
        response = await async_client.runtimes.with_raw_response.create(
            language="python",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runtime = await response.parse()
        assert_matches_type(Runtime, runtime, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRiza) -> None:
        async with async_client.runtimes.with_streaming_response.create(
            language="python",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runtime = await response.parse()
            assert_matches_type(Runtime, runtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncRiza) -> None:
        runtime = await async_client.runtimes.list()
        assert_matches_type(RuntimeListResponse, runtime, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRiza) -> None:
        response = await async_client.runtimes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runtime = await response.parse()
        assert_matches_type(RuntimeListResponse, runtime, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRiza) -> None:
        async with async_client.runtimes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runtime = await response.parse()
            assert_matches_type(RuntimeListResponse, runtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncRiza) -> None:
        runtime = await async_client.runtimes.get(
            "id",
        )
        assert_matches_type(Runtime, runtime, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncRiza) -> None:
        response = await async_client.runtimes.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runtime = await response.parse()
        assert_matches_type(Runtime, runtime, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncRiza) -> None:
        async with async_client.runtimes.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runtime = await response.parse()
            assert_matches_type(Runtime, runtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncRiza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.runtimes.with_raw_response.get(
                "",
            )
