# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ..types import SandboxExecuteResponse, sandbox_execute_params
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

__all__ = ["Sandbox", "AsyncSandbox"]


class Sandbox(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SandboxWithRawResponse:
        return SandboxWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SandboxWithStreamingResponse:
        return SandboxWithStreamingResponse(self)

    def execute(
        self,
        *,
        code: str,
        language: Literal["PYTHON", "JAVASCRIPT", "TYPESCRIPT", "RUBY", "PHP"],
        args: List[str] | NotGiven = NOT_GIVEN,
        env: Dict[str, str] | NotGiven = NOT_GIVEN,
        stdin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SandboxExecuteResponse:
        """Run a script in a secure, isolated sandbox.

        Scripts can read from stdin and
        write to stdout or stderr. They can access environment variables and command
        line arguments.

        Args:
          code: The code to execute in the sandbox.

          language: The interpreter to use when executing code.

          args: List of command line arguments to pass to the script.

          env: Set of key-value pairs to add to the script's execution environment.

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
                    "stdin": stdin,
                },
                sandbox_execute_params.SandboxExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxExecuteResponse,
        )


class AsyncSandbox(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSandboxWithRawResponse:
        return AsyncSandboxWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSandboxWithStreamingResponse:
        return AsyncSandboxWithStreamingResponse(self)

    async def execute(
        self,
        *,
        code: str,
        language: Literal["PYTHON", "JAVASCRIPT", "TYPESCRIPT", "RUBY", "PHP"],
        args: List[str] | NotGiven = NOT_GIVEN,
        env: Dict[str, str] | NotGiven = NOT_GIVEN,
        stdin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SandboxExecuteResponse:
        """Run a script in a secure, isolated sandbox.

        Scripts can read from stdin and
        write to stdout or stderr. They can access environment variables and command
        line arguments.

        Args:
          code: The code to execute in the sandbox.

          language: The interpreter to use when executing code.

          args: List of command line arguments to pass to the script.

          env: Set of key-value pairs to add to the script's execution environment.

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
                    "stdin": stdin,
                },
                sandbox_execute_params.SandboxExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxExecuteResponse,
        )


class SandboxWithRawResponse:
    def __init__(self, sandbox: Sandbox) -> None:
        self._sandbox = sandbox

        self.execute = to_raw_response_wrapper(
            sandbox.execute,
        )


class AsyncSandboxWithRawResponse:
    def __init__(self, sandbox: AsyncSandbox) -> None:
        self._sandbox = sandbox

        self.execute = async_to_raw_response_wrapper(
            sandbox.execute,
        )


class SandboxWithStreamingResponse:
    def __init__(self, sandbox: Sandbox) -> None:
        self._sandbox = sandbox

        self.execute = to_streamed_response_wrapper(
            sandbox.execute,
        )


class AsyncSandboxWithStreamingResponse:
    def __init__(self, sandbox: AsyncSandbox) -> None:
        self._sandbox = sandbox

        self.execute = async_to_streamed_response_wrapper(
            sandbox.execute,
        )
