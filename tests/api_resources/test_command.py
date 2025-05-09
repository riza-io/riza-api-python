# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rizaio import Riza, AsyncRiza
from tests.utils import assert_matches_type
from rizaio.types import CommandExecResponse, CommandExecFuncResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommand:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_exec(self, client: Riza) -> None:
        command = client.command.exec(
            code='print("Hello world!")',
            language="python",
        )
        assert_matches_type(CommandExecResponse, command, path=["response"])

    @parametrize
    def test_method_exec_with_all_params(self, client: Riza) -> None:
        command = client.command.exec(
            code='print("Hello world!")',
            language="python",
            args=["string"],
            env={"foo": "string"},
            files=[
                {
                    "contents": "contents",
                    "path": "path",
                }
            ],
            http={
                "allow": [
                    {
                        "auth": {
                            "basic": {
                                "password": "password",
                                "user_id": "user_id",
                            },
                            "bearer": {"token": "token"},
                            "header": {
                                "name": "name",
                                "value": "value",
                            },
                            "query": {
                                "key": "key",
                                "value": "value",
                            },
                        },
                        "host": "host",
                    }
                ]
            },
            limits={
                "execution_timeout": 0,
                "memory_size": 0,
            },
            runtime_revision_id="runtime_revision_id",
            stdin="stdin",
        )
        assert_matches_type(CommandExecResponse, command, path=["response"])

    @parametrize
    def test_raw_response_exec(self, client: Riza) -> None:
        response = client.command.with_raw_response.exec(
            code='print("Hello world!")',
            language="python",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(CommandExecResponse, command, path=["response"])

    @parametrize
    def test_streaming_response_exec(self, client: Riza) -> None:
        with client.command.with_streaming_response.exec(
            code='print("Hello world!")',
            language="python",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(CommandExecResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_exec_func(self, client: Riza) -> None:
        command = client.command.exec_func(
            code='def execute(input): return { "name": input["name"], "executed": True }',
            language="python",
        )
        assert_matches_type(CommandExecFuncResponse, command, path=["response"])

    @parametrize
    def test_method_exec_func_with_all_params(self, client: Riza) -> None:
        command = client.command.exec_func(
            code='def execute(input): return { "name": input["name"], "executed": True }',
            language="python",
            env={"foo": "string"},
            files=[
                {
                    "contents": "contents",
                    "path": "path",
                }
            ],
            http={
                "allow": [
                    {
                        "auth": {
                            "basic": {
                                "password": "password",
                                "user_id": "user_id",
                            },
                            "bearer": {"token": "token"},
                            "header": {
                                "name": "name",
                                "value": "value",
                            },
                            "query": {
                                "key": "key",
                                "value": "value",
                            },
                        },
                        "host": "host",
                    }
                ]
            },
            input={"name": "John"},
            limits={
                "execution_timeout": 0,
                "memory_size": 0,
            },
            runtime_revision_id="runtime_revision_id",
        )
        assert_matches_type(CommandExecFuncResponse, command, path=["response"])

    @parametrize
    def test_raw_response_exec_func(self, client: Riza) -> None:
        response = client.command.with_raw_response.exec_func(
            code='def execute(input): return { "name": input["name"], "executed": True }',
            language="python",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = response.parse()
        assert_matches_type(CommandExecFuncResponse, command, path=["response"])

    @parametrize
    def test_streaming_response_exec_func(self, client: Riza) -> None:
        with client.command.with_streaming_response.exec_func(
            code='def execute(input): return { "name": input["name"], "executed": True }',
            language="python",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = response.parse()
            assert_matches_type(CommandExecFuncResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCommand:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_exec(self, async_client: AsyncRiza) -> None:
        command = await async_client.command.exec(
            code='print("Hello world!")',
            language="python",
        )
        assert_matches_type(CommandExecResponse, command, path=["response"])

    @parametrize
    async def test_method_exec_with_all_params(self, async_client: AsyncRiza) -> None:
        command = await async_client.command.exec(
            code='print("Hello world!")',
            language="python",
            args=["string"],
            env={"foo": "string"},
            files=[
                {
                    "contents": "contents",
                    "path": "path",
                }
            ],
            http={
                "allow": [
                    {
                        "auth": {
                            "basic": {
                                "password": "password",
                                "user_id": "user_id",
                            },
                            "bearer": {"token": "token"},
                            "header": {
                                "name": "name",
                                "value": "value",
                            },
                            "query": {
                                "key": "key",
                                "value": "value",
                            },
                        },
                        "host": "host",
                    }
                ]
            },
            limits={
                "execution_timeout": 0,
                "memory_size": 0,
            },
            runtime_revision_id="runtime_revision_id",
            stdin="stdin",
        )
        assert_matches_type(CommandExecResponse, command, path=["response"])

    @parametrize
    async def test_raw_response_exec(self, async_client: AsyncRiza) -> None:
        response = await async_client.command.with_raw_response.exec(
            code='print("Hello world!")',
            language="python",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(CommandExecResponse, command, path=["response"])

    @parametrize
    async def test_streaming_response_exec(self, async_client: AsyncRiza) -> None:
        async with async_client.command.with_streaming_response.exec(
            code='print("Hello world!")',
            language="python",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(CommandExecResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_exec_func(self, async_client: AsyncRiza) -> None:
        command = await async_client.command.exec_func(
            code='def execute(input): return { "name": input["name"], "executed": True }',
            language="python",
        )
        assert_matches_type(CommandExecFuncResponse, command, path=["response"])

    @parametrize
    async def test_method_exec_func_with_all_params(self, async_client: AsyncRiza) -> None:
        command = await async_client.command.exec_func(
            code='def execute(input): return { "name": input["name"], "executed": True }',
            language="python",
            env={"foo": "string"},
            files=[
                {
                    "contents": "contents",
                    "path": "path",
                }
            ],
            http={
                "allow": [
                    {
                        "auth": {
                            "basic": {
                                "password": "password",
                                "user_id": "user_id",
                            },
                            "bearer": {"token": "token"},
                            "header": {
                                "name": "name",
                                "value": "value",
                            },
                            "query": {
                                "key": "key",
                                "value": "value",
                            },
                        },
                        "host": "host",
                    }
                ]
            },
            input={"name": "John"},
            limits={
                "execution_timeout": 0,
                "memory_size": 0,
            },
            runtime_revision_id="runtime_revision_id",
        )
        assert_matches_type(CommandExecFuncResponse, command, path=["response"])

    @parametrize
    async def test_raw_response_exec_func(self, async_client: AsyncRiza) -> None:
        response = await async_client.command.with_raw_response.exec_func(
            code='def execute(input): return { "name": input["name"], "executed": True }',
            language="python",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        command = await response.parse()
        assert_matches_type(CommandExecFuncResponse, command, path=["response"])

    @parametrize
    async def test_streaming_response_exec_func(self, async_client: AsyncRiza) -> None:
        async with async_client.command.with_streaming_response.exec_func(
            code='def execute(input): return { "name": input["name"], "executed": True }',
            language="python",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            command = await response.parse()
            assert_matches_type(CommandExecFuncResponse, command, path=["response"])

        assert cast(Any, response.is_closed) is True
