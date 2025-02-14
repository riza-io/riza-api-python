# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal

import httpx

from ..types import command_exec_params, command_exec_func_params
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
from .._base_client import make_request_options
from ..types.command_exec_response import CommandExecResponse
from ..types.command_exec_func_response import CommandExecFuncResponse

__all__ = ["CommandResource", "AsyncCommandResource"]


class CommandResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/riza-io/riza-api-python#accessing-raw-response-data-eg-headers
        """
        return CommandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/riza-io/riza-api-python#with_streaming_response
        """
        return CommandResourceWithStreamingResponse(self)

    def exec(
        self,
        *,
        code: str,
        language: Literal["python", "javascript", "typescript", "ruby", "php"],
        args: List[str] | NotGiven = NOT_GIVEN,
        env: Dict[str, str] | NotGiven = NOT_GIVEN,
        files: Iterable[command_exec_params.File] | NotGiven = NOT_GIVEN,
        http: command_exec_params.HTTP | NotGiven = NOT_GIVEN,
        limits: command_exec_params.Limits | NotGiven = NOT_GIVEN,
        runtime_revision_id: str | NotGiven = NOT_GIVEN,
        stdin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommandExecResponse:
        """Run a script in a secure, isolated environment.

        Scripts can read from `stdin`
        and write to `stdout` or `stderr`. They can access input files, environment
        variables and command line arguments.

        Args:
          code: The code to execute.

          language: The interpreter to use when executing code.

          args: List of command line arguments to pass to the script.

          env: Set of key-value pairs to add to the script's execution environment.

          files: List of input files.

          http: Configuration for HTTP requests and authentication.

          limits: Configuration for execution environment limits.

          runtime_revision_id: The ID of the runtime revision to use when executing code.

          stdin: Input made available to the script via 'stdin'.

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
                    "files": files,
                    "http": http,
                    "limits": limits,
                    "runtime_revision_id": runtime_revision_id,
                    "stdin": stdin,
                },
                command_exec_params.CommandExecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommandExecResponse,
        )

    def exec_func(
        self,
        *,
        code: str,
        language: Literal["python", "javascript", "typescript"],
        env: Dict[str, str] | NotGiven = NOT_GIVEN,
        files: Iterable[command_exec_func_params.File] | NotGiven = NOT_GIVEN,
        http: command_exec_func_params.HTTP | NotGiven = NOT_GIVEN,
        input: object | NotGiven = NOT_GIVEN,
        limits: command_exec_func_params.Limits | NotGiven = NOT_GIVEN,
        runtime_revision_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommandExecFuncResponse:
        """Run a function in a secure, isolated environment.

        Define a function named
        `execute`. The function will be passed `input` as an object.

        Args:
          code: The function to execute. Your code must define a function named "execute" that
              takes in a single argument and returns a JSON-serializable value.

          language: The interpreter to use when executing code.

          env: Set of key-value pairs to add to the function's execution environment.

          files: List of input files.

          http: Configuration for HTTP requests and authentication.

          input: The input to the function. This must be a valid JSON-serializable object. If you
              do not pass an input, your function will be called with None (Python) or null
              (JavaScript/TypeScript) as the argument.

          limits: Configuration for execution environment limits.

          runtime_revision_id: The ID of the runtime revision to use when executing code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/execute-function",
            body=maybe_transform(
                {
                    "code": code,
                    "language": language,
                    "env": env,
                    "files": files,
                    "http": http,
                    "input": input,
                    "limits": limits,
                    "runtime_revision_id": runtime_revision_id,
                },
                command_exec_func_params.CommandExecFuncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommandExecFuncResponse,
        )


class AsyncCommandResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/riza-io/riza-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/riza-io/riza-api-python#with_streaming_response
        """
        return AsyncCommandResourceWithStreamingResponse(self)

    async def exec(
        self,
        *,
        code: str,
        language: Literal["python", "javascript", "typescript", "ruby", "php"],
        args: List[str] | NotGiven = NOT_GIVEN,
        env: Dict[str, str] | NotGiven = NOT_GIVEN,
        files: Iterable[command_exec_params.File] | NotGiven = NOT_GIVEN,
        http: command_exec_params.HTTP | NotGiven = NOT_GIVEN,
        limits: command_exec_params.Limits | NotGiven = NOT_GIVEN,
        runtime_revision_id: str | NotGiven = NOT_GIVEN,
        stdin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommandExecResponse:
        """Run a script in a secure, isolated environment.

        Scripts can read from `stdin`
        and write to `stdout` or `stderr`. They can access input files, environment
        variables and command line arguments.

        Args:
          code: The code to execute.

          language: The interpreter to use when executing code.

          args: List of command line arguments to pass to the script.

          env: Set of key-value pairs to add to the script's execution environment.

          files: List of input files.

          http: Configuration for HTTP requests and authentication.

          limits: Configuration for execution environment limits.

          runtime_revision_id: The ID of the runtime revision to use when executing code.

          stdin: Input made available to the script via 'stdin'.

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
                    "files": files,
                    "http": http,
                    "limits": limits,
                    "runtime_revision_id": runtime_revision_id,
                    "stdin": stdin,
                },
                command_exec_params.CommandExecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommandExecResponse,
        )

    async def exec_func(
        self,
        *,
        code: str,
        language: Literal["python", "javascript", "typescript"],
        env: Dict[str, str] | NotGiven = NOT_GIVEN,
        files: Iterable[command_exec_func_params.File] | NotGiven = NOT_GIVEN,
        http: command_exec_func_params.HTTP | NotGiven = NOT_GIVEN,
        input: object | NotGiven = NOT_GIVEN,
        limits: command_exec_func_params.Limits | NotGiven = NOT_GIVEN,
        runtime_revision_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommandExecFuncResponse:
        """Run a function in a secure, isolated environment.

        Define a function named
        `execute`. The function will be passed `input` as an object.

        Args:
          code: The function to execute. Your code must define a function named "execute" that
              takes in a single argument and returns a JSON-serializable value.

          language: The interpreter to use when executing code.

          env: Set of key-value pairs to add to the function's execution environment.

          files: List of input files.

          http: Configuration for HTTP requests and authentication.

          input: The input to the function. This must be a valid JSON-serializable object. If you
              do not pass an input, your function will be called with None (Python) or null
              (JavaScript/TypeScript) as the argument.

          limits: Configuration for execution environment limits.

          runtime_revision_id: The ID of the runtime revision to use when executing code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/execute-function",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "language": language,
                    "env": env,
                    "files": files,
                    "http": http,
                    "input": input,
                    "limits": limits,
                    "runtime_revision_id": runtime_revision_id,
                },
                command_exec_func_params.CommandExecFuncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommandExecFuncResponse,
        )


class CommandResourceWithRawResponse:
    def __init__(self, command: CommandResource) -> None:
        self._command = command

        self.exec = to_raw_response_wrapper(
            command.exec,
        )
        self.exec_func = to_raw_response_wrapper(
            command.exec_func,
        )


class AsyncCommandResourceWithRawResponse:
    def __init__(self, command: AsyncCommandResource) -> None:
        self._command = command

        self.exec = async_to_raw_response_wrapper(
            command.exec,
        )
        self.exec_func = async_to_raw_response_wrapper(
            command.exec_func,
        )


class CommandResourceWithStreamingResponse:
    def __init__(self, command: CommandResource) -> None:
        self._command = command

        self.exec = to_streamed_response_wrapper(
            command.exec,
        )
        self.exec_func = to_streamed_response_wrapper(
            command.exec_func,
        )


class AsyncCommandResourceWithStreamingResponse:
    def __init__(self, command: AsyncCommandResource) -> None:
        self._command = command

        self.exec = async_to_streamed_response_wrapper(
            command.exec,
        )
        self.exec_func = async_to_streamed_response_wrapper(
            command.exec_func,
        )
