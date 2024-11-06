# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rizaio import Riza, AsyncRiza
from tests.utils import assert_matches_type
from rizaio.types import (
    Tool,
    ToolExecResponse,
    ToolListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Riza) -> None:
        tool = client.tools.create(
            code="code",
            name="name",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Riza) -> None:
        tool = client.tools.create(
            code="code",
            name="name",
            description="description",
            input_schema={},
            language="PYTHON",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Riza) -> None:
        response = client.tools.with_raw_response.create(
            code="code",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Riza) -> None:
        with client.tools.with_streaming_response.create(
            code="code",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Riza) -> None:
        tool = client.tools.update(
            id="id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Riza) -> None:
        tool = client.tools.update(
            id="id",
            code="code",
            description="description",
            input_schema={},
            language="PYTHON",
            name="name",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Riza) -> None:
        response = client.tools.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Riza) -> None:
        with client.tools.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Riza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tools.with_raw_response.update(
                id="",
            )

    @parametrize
    def test_method_list(self, client: Riza) -> None:
        tool = client.tools.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Riza) -> None:
        response = client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Riza) -> None:
        with client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_exec(self, client: Riza) -> None:
        tool = client.tools.exec(
            id="id",
        )
        assert_matches_type(ToolExecResponse, tool, path=["response"])

    @parametrize
    def test_method_exec_with_all_params(self, client: Riza) -> None:
        tool = client.tools.exec(
            id="id",
            env=[
                {
                    "name": "name",
                    "secret_id": "secret_id",
                    "value": "value",
                },
                {
                    "name": "name",
                    "secret_id": "secret_id",
                    "value": "value",
                },
                {
                    "name": "name",
                    "secret_id": "secret_id",
                    "value": "value",
                },
            ],
            http={
                "allow": [
                    {
                        "auth": {
                            "basic": {
                                "password": "password",
                                "secret_id": "secret_id",
                                "user_id": "user_id",
                            },
                            "bearer": {
                                "token": "token",
                                "secret_id": "secret_id",
                            },
                            "query": {
                                "key": "key",
                                "secret_id": "secret_id",
                                "value": "value",
                            },
                        },
                        "host": "host",
                    },
                    {
                        "auth": {
                            "basic": {
                                "password": "password",
                                "secret_id": "secret_id",
                                "user_id": "user_id",
                            },
                            "bearer": {
                                "token": "token",
                                "secret_id": "secret_id",
                            },
                            "query": {
                                "key": "key",
                                "secret_id": "secret_id",
                                "value": "value",
                            },
                        },
                        "host": "host",
                    },
                    {
                        "auth": {
                            "basic": {
                                "password": "password",
                                "secret_id": "secret_id",
                                "user_id": "user_id",
                            },
                            "bearer": {
                                "token": "token",
                                "secret_id": "secret_id",
                            },
                            "query": {
                                "key": "key",
                                "secret_id": "secret_id",
                                "value": "value",
                            },
                        },
                        "host": "host",
                    },
                ]
            },
            input={},
            revision_id="revision_id",
        )
        assert_matches_type(ToolExecResponse, tool, path=["response"])

    @parametrize
    def test_raw_response_exec(self, client: Riza) -> None:
        response = client.tools.with_raw_response.exec(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolExecResponse, tool, path=["response"])

    @parametrize
    def test_streaming_response_exec(self, client: Riza) -> None:
        with client.tools.with_streaming_response.exec(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolExecResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_exec(self, client: Riza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tools.with_raw_response.exec(
                id="",
            )

    @parametrize
    def test_method_get(self, client: Riza) -> None:
        tool = client.tools.get(
            "id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Riza) -> None:
        response = client.tools.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Riza) -> None:
        with client.tools.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Riza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.tools.with_raw_response.get(
                "",
            )


class TestAsyncTools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncRiza) -> None:
        tool = await async_client.tools.create(
            code="code",
            name="name",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRiza) -> None:
        tool = await async_client.tools.create(
            code="code",
            name="name",
            description="description",
            input_schema={},
            language="PYTHON",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRiza) -> None:
        response = await async_client.tools.with_raw_response.create(
            code="code",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRiza) -> None:
        async with async_client.tools.with_streaming_response.create(
            code="code",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncRiza) -> None:
        tool = await async_client.tools.update(
            id="id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRiza) -> None:
        tool = await async_client.tools.update(
            id="id",
            code="code",
            description="description",
            input_schema={},
            language="PYTHON",
            name="name",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRiza) -> None:
        response = await async_client.tools.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRiza) -> None:
        async with async_client.tools.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRiza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tools.with_raw_response.update(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRiza) -> None:
        tool = await async_client.tools.list()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRiza) -> None:
        response = await async_client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRiza) -> None:
        async with async_client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_exec(self, async_client: AsyncRiza) -> None:
        tool = await async_client.tools.exec(
            id="id",
        )
        assert_matches_type(ToolExecResponse, tool, path=["response"])

    @parametrize
    async def test_method_exec_with_all_params(self, async_client: AsyncRiza) -> None:
        tool = await async_client.tools.exec(
            id="id",
            env=[
                {
                    "name": "name",
                    "secret_id": "secret_id",
                    "value": "value",
                },
                {
                    "name": "name",
                    "secret_id": "secret_id",
                    "value": "value",
                },
                {
                    "name": "name",
                    "secret_id": "secret_id",
                    "value": "value",
                },
            ],
            http={
                "allow": [
                    {
                        "auth": {
                            "basic": {
                                "password": "password",
                                "secret_id": "secret_id",
                                "user_id": "user_id",
                            },
                            "bearer": {
                                "token": "token",
                                "secret_id": "secret_id",
                            },
                            "query": {
                                "key": "key",
                                "secret_id": "secret_id",
                                "value": "value",
                            },
                        },
                        "host": "host",
                    },
                    {
                        "auth": {
                            "basic": {
                                "password": "password",
                                "secret_id": "secret_id",
                                "user_id": "user_id",
                            },
                            "bearer": {
                                "token": "token",
                                "secret_id": "secret_id",
                            },
                            "query": {
                                "key": "key",
                                "secret_id": "secret_id",
                                "value": "value",
                            },
                        },
                        "host": "host",
                    },
                    {
                        "auth": {
                            "basic": {
                                "password": "password",
                                "secret_id": "secret_id",
                                "user_id": "user_id",
                            },
                            "bearer": {
                                "token": "token",
                                "secret_id": "secret_id",
                            },
                            "query": {
                                "key": "key",
                                "secret_id": "secret_id",
                                "value": "value",
                            },
                        },
                        "host": "host",
                    },
                ]
            },
            input={},
            revision_id="revision_id",
        )
        assert_matches_type(ToolExecResponse, tool, path=["response"])

    @parametrize
    async def test_raw_response_exec(self, async_client: AsyncRiza) -> None:
        response = await async_client.tools.with_raw_response.exec(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolExecResponse, tool, path=["response"])

    @parametrize
    async def test_streaming_response_exec(self, async_client: AsyncRiza) -> None:
        async with async_client.tools.with_streaming_response.exec(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolExecResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_exec(self, async_client: AsyncRiza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tools.with_raw_response.exec(
                id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncRiza) -> None:
        tool = await async_client.tools.get(
            "id",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncRiza) -> None:
        response = await async_client.tools.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncRiza) -> None:
        async with async_client.tools.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncRiza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.tools.with_raw_response.get(
                "",
            )
