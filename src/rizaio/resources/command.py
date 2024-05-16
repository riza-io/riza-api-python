# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ..types import command_exec_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.command_exec_response import CommandExecResponse

__all__ = ["CommandResource", "AsyncCommandResource"]


class CommandResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommandResourceWithRawResponse:
        return CommandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommandResourceWithStreamingResponse:
        return CommandResourceWithStreamingResponse(self)

    def exec(
        self,
        *,
        code: str,
        language: Literal["PYTHON", "JAVASCRIPT", "TYPESCRIPT", "RUBY", "PHP"],
        args: List[str] | NotGiven = NOT_GIVEN,
        env: Dict[str, str] | NotGiven = NOT_GIVEN,
        net: List[str] | NotGiven = NOT_GIVEN,
        stdin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommandExecResponse:
        """Run a script in a secure, isolated sandbox.

        Scripts can read from stdin and
        write to stdout or stderr. They can access environment variables and command
        line arguments.

        Args:
          code: The code to execute in the sandbox.

          language: The interpreter to use when executing code.

          args: List of command line arguments to pass to the script.

          env: Set of key-value pairs to add to the script's execution environment.

          net: List of allowed hosts for HTTP requests

          stdin: Input to pass to the script via `stdin`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/execute",
            body=maybe_transform(
                {
                    "code": code,
                    "language": language,
                    "args": args,
                    "env": env,
                    "net": net,
                    "stdin": stdin,
                },
                command_exec_params.CommandExecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommandExecResponse,
        )


class AsyncCommandResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommandResourceWithRawResponse:
        return AsyncCommandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommandResourceWithStreamingResponse:
        return AsyncCommandResourceWithStreamingResponse(self)

    async def exec(
        self,
        *,
        code: str,
        language: Literal["PYTHON", "JAVASCRIPT", "TYPESCRIPT", "RUBY", "PHP"],
        args: List[str] | NotGiven = NOT_GIVEN,
        env: Dict[str, str] | NotGiven = NOT_GIVEN,
        net: List[str] | NotGiven = NOT_GIVEN,
        stdin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommandExecResponse:
        """Run a script in a secure, isolated sandbox.

        Scripts can read from stdin and
        write to stdout or stderr. They can access environment variables and command
        line arguments.

        Args:
          code: The code to execute in the sandbox.

          language: The interpreter to use when executing code.

          args: List of command line arguments to pass to the script.

          env: Set of key-value pairs to add to the script's execution environment.

          net: List of allowed hosts for HTTP requests

          stdin: Input to pass to the script via `stdin`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/execute",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "language": language,
                    "args": args,
                    "env": env,
                    "net": net,
                    "stdin": stdin,
                },
                command_exec_params.CommandExecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommandExecResponse,
        )


class CommandResourceWithRawResponse:
    def __init__(self, command: CommandResource) -> None:
        self._command = command

        self.exec = to_raw_response_wrapper(
            command.exec,
        )


class AsyncCommandResourceWithRawResponse:
    def __init__(self, command: AsyncCommandResource) -> None:
        self._command = command

        self.exec = async_to_raw_response_wrapper(
            command.exec,
        )


class CommandResourceWithStreamingResponse:
    def __init__(self, command: CommandResource) -> None:
        self._command = command

        self.exec = to_streamed_response_wrapper(
            command.exec,
        )


class AsyncCommandResourceWithStreamingResponse:
    def __init__(self, command: AsyncCommandResource) -> None:
        self._command = command

        self.exec = async_to_streamed_response_wrapper(
            command.exec,
        )
