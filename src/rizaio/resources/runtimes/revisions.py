# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.runtimes import revision_create_params
from ...types.runtimes.revision import Revision
from ...types.runtimes.revision_list_response import RevisionListResponse

__all__ = ["RevisionsResource", "AsyncRevisionsResource"]


class RevisionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/riza-io/riza-api-python#accessing-raw-response-data-eg-headers
        """
        return RevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/riza-io/riza-api-python#with_streaming_response
        """
        return RevisionsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        manifest_file: revision_create_params.ManifestFile,
        additional_python_imports: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Revision:
        """
        Creates a new runtime revision.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v1/runtimes/{id}/revisions",
            body=maybe_transform(
                {
                    "manifest_file": manifest_file,
                    "additional_python_imports": additional_python_imports,
                },
                revision_create_params.RevisionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Revision,
        )

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RevisionListResponse:
        """
        Lists all revisions for a runtime.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/runtimes/{id}/revisions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RevisionListResponse,
        )

    def get(
        self,
        revision_id: str,
        *,
        runtime_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Revision:
        """
        Retrieves a runtime revision.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not runtime_id:
            raise ValueError(f"Expected a non-empty value for `runtime_id` but received {runtime_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return self._get(
            f"/v1/runtimes/{runtime_id}/revisions/{revision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Revision,
        )


class AsyncRevisionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevisionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/riza-io/riza-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRevisionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevisionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/riza-io/riza-api-python#with_streaming_response
        """
        return AsyncRevisionsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        manifest_file: revision_create_params.ManifestFile,
        additional_python_imports: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Revision:
        """
        Creates a new runtime revision.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v1/runtimes/{id}/revisions",
            body=await async_maybe_transform(
                {
                    "manifest_file": manifest_file,
                    "additional_python_imports": additional_python_imports,
                },
                revision_create_params.RevisionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Revision,
        )

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RevisionListResponse:
        """
        Lists all revisions for a runtime.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/runtimes/{id}/revisions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RevisionListResponse,
        )

    async def get(
        self,
        revision_id: str,
        *,
        runtime_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Revision:
        """
        Retrieves a runtime revision.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not runtime_id:
            raise ValueError(f"Expected a non-empty value for `runtime_id` but received {runtime_id!r}")
        if not revision_id:
            raise ValueError(f"Expected a non-empty value for `revision_id` but received {revision_id!r}")
        return await self._get(
            f"/v1/runtimes/{runtime_id}/revisions/{revision_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Revision,
        )


class RevisionsResourceWithRawResponse:
    def __init__(self, revisions: RevisionsResource) -> None:
        self._revisions = revisions

        self.create = to_raw_response_wrapper(
            revisions.create,
        )
        self.list = to_raw_response_wrapper(
            revisions.list,
        )
        self.get = to_raw_response_wrapper(
            revisions.get,
        )


class AsyncRevisionsResourceWithRawResponse:
    def __init__(self, revisions: AsyncRevisionsResource) -> None:
        self._revisions = revisions

        self.create = async_to_raw_response_wrapper(
            revisions.create,
        )
        self.list = async_to_raw_response_wrapper(
            revisions.list,
        )
        self.get = async_to_raw_response_wrapper(
            revisions.get,
        )


class RevisionsResourceWithStreamingResponse:
    def __init__(self, revisions: RevisionsResource) -> None:
        self._revisions = revisions

        self.create = to_streamed_response_wrapper(
            revisions.create,
        )
        self.list = to_streamed_response_wrapper(
            revisions.list,
        )
        self.get = to_streamed_response_wrapper(
            revisions.get,
        )


class AsyncRevisionsResourceWithStreamingResponse:
    def __init__(self, revisions: AsyncRevisionsResource) -> None:
        self._revisions = revisions

        self.create = async_to_streamed_response_wrapper(
            revisions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            revisions.list,
        )
        self.get = async_to_streamed_response_wrapper(
            revisions.get,
        )
