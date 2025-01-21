# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import runtime_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .revisions import (
    RevisionsResource,
    AsyncRevisionsResource,
    RevisionsResourceWithRawResponse,
    AsyncRevisionsResourceWithRawResponse,
    RevisionsResourceWithStreamingResponse,
    AsyncRevisionsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.runtime import Runtime
from ...types.runtime_list_response import RuntimeListResponse

__all__ = ["RuntimesResource", "AsyncRuntimesResource"]


class RuntimesResource(SyncAPIResource):
    @cached_property
    def revisions(self) -> RevisionsResource:
        return RevisionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RuntimesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/riza-io/riza-api-python#accessing-raw-response-data-eg-headers
        """
        return RuntimesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RuntimesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/riza-io/riza-api-python#with_streaming_response
        """
        return RuntimesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        language: Literal["python", "javascript"],
        manifest_file: runtime_create_params.ManifestFile,
        name: str,
        additional_python_imports: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Runtime:
        """
        Creates a runtime.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/runtimes",
            body=maybe_transform(
                {
                    "language": language,
                    "manifest_file": manifest_file,
                    "name": name,
                    "additional_python_imports": additional_python_imports,
                },
                runtime_create_params.RuntimeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Runtime,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuntimeListResponse:
        """Returns a list of runtimes in your project."""
        return self._get(
            "/v1/runtimes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuntimeListResponse,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Runtime:
        """
        Retrieves a runtime.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/runtimes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Runtime,
        )


class AsyncRuntimesResource(AsyncAPIResource):
    @cached_property
    def revisions(self) -> AsyncRevisionsResource:
        return AsyncRevisionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRuntimesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/riza-io/riza-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRuntimesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRuntimesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/riza-io/riza-api-python#with_streaming_response
        """
        return AsyncRuntimesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        language: Literal["python", "javascript"],
        manifest_file: runtime_create_params.ManifestFile,
        name: str,
        additional_python_imports: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Runtime:
        """
        Creates a runtime.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/runtimes",
            body=await async_maybe_transform(
                {
                    "language": language,
                    "manifest_file": manifest_file,
                    "name": name,
                    "additional_python_imports": additional_python_imports,
                },
                runtime_create_params.RuntimeCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Runtime,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RuntimeListResponse:
        """Returns a list of runtimes in your project."""
        return await self._get(
            "/v1/runtimes",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RuntimeListResponse,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Runtime:
        """
        Retrieves a runtime.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/runtimes/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Runtime,
        )


class RuntimesResourceWithRawResponse:
    def __init__(self, runtimes: RuntimesResource) -> None:
        self._runtimes = runtimes

        self.create = to_raw_response_wrapper(
            runtimes.create,
        )
        self.list = to_raw_response_wrapper(
            runtimes.list,
        )
        self.get = to_raw_response_wrapper(
            runtimes.get,
        )

    @cached_property
    def revisions(self) -> RevisionsResourceWithRawResponse:
        return RevisionsResourceWithRawResponse(self._runtimes.revisions)


class AsyncRuntimesResourceWithRawResponse:
    def __init__(self, runtimes: AsyncRuntimesResource) -> None:
        self._runtimes = runtimes

        self.create = async_to_raw_response_wrapper(
            runtimes.create,
        )
        self.list = async_to_raw_response_wrapper(
            runtimes.list,
        )
        self.get = async_to_raw_response_wrapper(
            runtimes.get,
        )

    @cached_property
    def revisions(self) -> AsyncRevisionsResourceWithRawResponse:
        return AsyncRevisionsResourceWithRawResponse(self._runtimes.revisions)


class RuntimesResourceWithStreamingResponse:
    def __init__(self, runtimes: RuntimesResource) -> None:
        self._runtimes = runtimes

        self.create = to_streamed_response_wrapper(
            runtimes.create,
        )
        self.list = to_streamed_response_wrapper(
            runtimes.list,
        )
        self.get = to_streamed_response_wrapper(
            runtimes.get,
        )

    @cached_property
    def revisions(self) -> RevisionsResourceWithStreamingResponse:
        return RevisionsResourceWithStreamingResponse(self._runtimes.revisions)


class AsyncRuntimesResourceWithStreamingResponse:
    def __init__(self, runtimes: AsyncRuntimesResource) -> None:
        self._runtimes = runtimes

        self.create = async_to_streamed_response_wrapper(
            runtimes.create,
        )
        self.list = async_to_streamed_response_wrapper(
            runtimes.list,
        )
        self.get = async_to_streamed_response_wrapper(
            runtimes.get,
        )

    @cached_property
    def revisions(self) -> AsyncRevisionsResourceWithStreamingResponse:
        return AsyncRevisionsResourceWithStreamingResponse(self._runtimes.revisions)
