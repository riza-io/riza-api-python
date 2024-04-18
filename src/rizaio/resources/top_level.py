# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ..types import TopLevelExecuteResponse, top_level_execute_params
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

__all__ = ["TopLevel", "AsyncTopLevel"]


class TopLevel(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopLevelWithRawResponse:
        return TopLevelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopLevelWithStreamingResponse:
        return TopLevelWithStreamingResponse(self)

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
    ) -> TopLevelExecuteResponse:
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
                top_level_execute_params.TopLevelExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TopLevelExecuteResponse,
        )


class AsyncTopLevel(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopLevelWithRawResponse:
        return AsyncTopLevelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopLevelWithStreamingResponse:
        return AsyncTopLevelWithStreamingResponse(self)

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
    ) -> TopLevelExecuteResponse:
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
                top_level_execute_params.TopLevelExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TopLevelExecuteResponse,
        )


class TopLevelWithRawResponse:
    def __init__(self, top_level: TopLevel) -> None:
        self._top_level = top_level

        self.execute = to_raw_response_wrapper(
            top_level.execute,
        )


class AsyncTopLevelWithRawResponse:
    def __init__(self, top_level: AsyncTopLevel) -> None:
        self._top_level = top_level

        self.execute = async_to_raw_response_wrapper(
            top_level.execute,
        )


class TopLevelWithStreamingResponse:
    def __init__(self, top_level: TopLevel) -> None:
        self._top_level = top_level

        self.execute = to_streamed_response_wrapper(
            top_level.execute,
        )


class AsyncTopLevelWithStreamingResponse:
    def __init__(self, top_level: AsyncTopLevel) -> None:
        self._top_level = top_level

        self.execute = async_to_streamed_response_wrapper(
            top_level.execute,
        )
