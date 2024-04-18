# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ..types import V1ExecuteResponse, v1_execute_params
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

__all__ = ["V1", "AsyncV1"]


class V1(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V1WithRawResponse:
        return V1WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V1WithStreamingResponse:
        return V1WithStreamingResponse(self)

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
    ) -> V1ExecuteResponse:
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
                v1_execute_params.V1ExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ExecuteResponse,
        )


class AsyncV1(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV1WithRawResponse:
        return AsyncV1WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV1WithStreamingResponse:
        return AsyncV1WithStreamingResponse(self)

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
    ) -> V1ExecuteResponse:
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
                v1_execute_params.V1ExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V1ExecuteResponse,
        )


class V1WithRawResponse:
    def __init__(self, v1: V1) -> None:
        self._v1 = v1

        self.execute = to_raw_response_wrapper(
            v1.execute,
        )


class AsyncV1WithRawResponse:
    def __init__(self, v1: AsyncV1) -> None:
        self._v1 = v1

        self.execute = async_to_raw_response_wrapper(
            v1.execute,
        )


class V1WithStreamingResponse:
    def __init__(self, v1: V1) -> None:
        self._v1 = v1

        self.execute = to_streamed_response_wrapper(
            v1.execute,
        )


class AsyncV1WithStreamingResponse:
    def __init__(self, v1: AsyncV1) -> None:
        self._v1 = v1

        self.execute = async_to_streamed_response_wrapper(
            v1.execute,
        )
