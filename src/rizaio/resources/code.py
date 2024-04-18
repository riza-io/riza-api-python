# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ..types import CodeExecuteResponse, code_execute_params
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

__all__ = ["Code", "AsyncCode"]


class Code(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CodeWithRawResponse:
        return CodeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CodeWithStreamingResponse:
        return CodeWithStreamingResponse(self)

    def execute(
        self,
        *,
        args: List[str] | NotGiven = NOT_GIVEN,
        code: str | NotGiven = NOT_GIVEN,
        env: Dict[str, str] | NotGiven = NOT_GIVEN,
        language: Literal["UNSPECIFIED", "PYTHON", "JAVASCRIPT", "TYPESCRIPT", "RUBY", "PHP"] | NotGiven = NOT_GIVEN,
        stdin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeExecuteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/execute",
            body=maybe_transform(
                {
                    "args": args,
                    "code": code,
                    "env": env,
                    "language": language,
                    "stdin": stdin,
                },
                code_execute_params.CodeExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CodeExecuteResponse,
        )


class AsyncCode(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCodeWithRawResponse:
        return AsyncCodeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCodeWithStreamingResponse:
        return AsyncCodeWithStreamingResponse(self)

    async def execute(
        self,
        *,
        args: List[str] | NotGiven = NOT_GIVEN,
        code: str | NotGiven = NOT_GIVEN,
        env: Dict[str, str] | NotGiven = NOT_GIVEN,
        language: Literal["UNSPECIFIED", "PYTHON", "JAVASCRIPT", "TYPESCRIPT", "RUBY", "PHP"] | NotGiven = NOT_GIVEN,
        stdin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeExecuteResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/execute",
            body=await async_maybe_transform(
                {
                    "args": args,
                    "code": code,
                    "env": env,
                    "language": language,
                    "stdin": stdin,
                },
                code_execute_params.CodeExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CodeExecuteResponse,
        )


class CodeWithRawResponse:
    def __init__(self, code: Code) -> None:
        self._code = code

        self.execute = to_raw_response_wrapper(
            code.execute,
        )


class AsyncCodeWithRawResponse:
    def __init__(self, code: AsyncCode) -> None:
        self._code = code

        self.execute = async_to_raw_response_wrapper(
            code.execute,
        )


class CodeWithStreamingResponse:
    def __init__(self, code: Code) -> None:
        self._code = code

        self.execute = to_streamed_response_wrapper(
            code.execute,
        )


class AsyncCodeWithStreamingResponse:
    def __init__(self, code: AsyncCode) -> None:
        self._code = code

        self.execute = async_to_streamed_response_wrapper(
            code.execute,
        )
