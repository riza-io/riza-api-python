# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import tool_exec_params, tool_list_params, tool_create_params, tool_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncToolsPagination, AsyncToolsPagination
from ..types.tool import Tool
from .._base_client import AsyncPaginator, make_request_options
from ..types.tool_exec_response import ToolExecResponse

__all__ = ["ToolsResource", "AsyncToolsResource"]


class ToolsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/riza-io/riza-api-python#accessing-raw-response-data-eg-headers
        """
        return ToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/riza-io/riza-api-python#with_streaming_response
        """
        return ToolsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        code: str,
        language: Literal["python", "javascript", "typescript"],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        input_schema: object | NotGiven = NOT_GIVEN,
        runtime_revision_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Tool:
        """Create a tool in your project.

        Args:
          code: The code of the tool.

        You must define a function named "execute" that takes in a
              single argument and returns a JSON-serializable value. The argument will be the
              "input" passed when executing the tool, and will match the input schema.

          language: The language of the tool's code.

          name: The name of the tool.

          description: A description of the tool.

          input_schema: The input schema of the tool. This must be a valid JSON Schema object.

          runtime_revision_id: The ID of the runtime revision to use when executing the tool.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tools",
            body=maybe_transform(
                {
                    "code": code,
                    "language": language,
                    "name": name,
                    "description": description,
                    "input_schema": input_schema,
                    "runtime_revision_id": runtime_revision_id,
                },
                tool_create_params.ToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )

    def update(
        self,
        id: str,
        *,
        code: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        input_schema: object | NotGiven = NOT_GIVEN,
        language: Literal["python", "javascript", "typescript"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        runtime_revision_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Tool:
        """
        Update the source code and input schema of a tool.

        Args:
          code: The code of the tool. You must define a function named "execute" that takes in a
              single argument and returns a JSON-serializable value. The argument will be the
              "input" passed when executing the tool, and will match the input schema.

          description: A description of the tool.

          input_schema: The input schema of the tool. This must be a valid JSON Schema object.

          language: The language of the tool's code.

          name: The name of the tool.

          runtime_revision_id: The ID of the custom runtime revision that the tool uses for executions. This is
              used to pin executions to a specific version of a custom runtime, even if the
              runtime is updated later.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v1/tools/{id}",
            body=maybe_transform(
                {
                    "code": code,
                    "description": description,
                    "input_schema": input_schema,
                    "language": language,
                    "name": name,
                    "runtime_revision_id": runtime_revision_id,
                },
                tool_update_params.ToolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncToolsPagination[Tool]:
        """
        Returns a list of tools in your project.

        Args:
          limit: The number of items to return. Defaults to 100. Maximum is 100.

          starting_after: The ID of the item to start after. To get the next page of results, set this to
              the ID of the last item in the current page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/tools",
            page=SyncToolsPagination[Tool],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            model=Tool,
        )

    def exec(
        self,
        id: str,
        *,
        env: Iterable[tool_exec_params.Env] | NotGiven = NOT_GIVEN,
        http: tool_exec_params.HTTP | NotGiven = NOT_GIVEN,
        input: object | NotGiven = NOT_GIVEN,
        revision_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolExecResponse:
        """Execute a tool with a given input.

        The input is validated against the tool's
        input schema.

        Args:
          env: Set of key-value pairs to add to the tool's execution environment.

          http: Configuration for HTTP requests and authentication.

          input: The input to the tool. This must be a valid JSON-serializable object. It will be
              validated against the tool's input schema.

          revision_id: The Tool revision ID to execute. This optional parmeter is used to pin
              executions to specific versions of the Tool. If not provided, the latest
              (current) version of the Tool will be executed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v1/tools/{id}/execute",
            body=maybe_transform(
                {
                    "env": env,
                    "http": http,
                    "input": input,
                    "revision_id": revision_id,
                },
                tool_exec_params.ToolExecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolExecResponse,
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
    ) -> Tool:
        """
        Retrieves a tool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/tools/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )


class AsyncToolsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/riza-io/riza-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/riza-io/riza-api-python#with_streaming_response
        """
        return AsyncToolsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        code: str,
        language: Literal["python", "javascript", "typescript"],
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        input_schema: object | NotGiven = NOT_GIVEN,
        runtime_revision_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Tool:
        """Create a tool in your project.

        Args:
          code: The code of the tool.

        You must define a function named "execute" that takes in a
              single argument and returns a JSON-serializable value. The argument will be the
              "input" passed when executing the tool, and will match the input schema.

          language: The language of the tool's code.

          name: The name of the tool.

          description: A description of the tool.

          input_schema: The input schema of the tool. This must be a valid JSON Schema object.

          runtime_revision_id: The ID of the runtime revision to use when executing the tool.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tools",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "language": language,
                    "name": name,
                    "description": description,
                    "input_schema": input_schema,
                    "runtime_revision_id": runtime_revision_id,
                },
                tool_create_params.ToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )

    async def update(
        self,
        id: str,
        *,
        code: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        input_schema: object | NotGiven = NOT_GIVEN,
        language: Literal["python", "javascript", "typescript"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        runtime_revision_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Tool:
        """
        Update the source code and input schema of a tool.

        Args:
          code: The code of the tool. You must define a function named "execute" that takes in a
              single argument and returns a JSON-serializable value. The argument will be the
              "input" passed when executing the tool, and will match the input schema.

          description: A description of the tool.

          input_schema: The input schema of the tool. This must be a valid JSON Schema object.

          language: The language of the tool's code.

          name: The name of the tool.

          runtime_revision_id: The ID of the custom runtime revision that the tool uses for executions. This is
              used to pin executions to a specific version of a custom runtime, even if the
              runtime is updated later.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v1/tools/{id}",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "description": description,
                    "input_schema": input_schema,
                    "language": language,
                    "name": name,
                    "runtime_revision_id": runtime_revision_id,
                },
                tool_update_params.ToolUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Tool, AsyncToolsPagination[Tool]]:
        """
        Returns a list of tools in your project.

        Args:
          limit: The number of items to return. Defaults to 100. Maximum is 100.

          starting_after: The ID of the item to start after. To get the next page of results, set this to
              the ID of the last item in the current page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/tools",
            page=AsyncToolsPagination[Tool],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "starting_after": starting_after,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            model=Tool,
        )

    async def exec(
        self,
        id: str,
        *,
        env: Iterable[tool_exec_params.Env] | NotGiven = NOT_GIVEN,
        http: tool_exec_params.HTTP | NotGiven = NOT_GIVEN,
        input: object | NotGiven = NOT_GIVEN,
        revision_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolExecResponse:
        """Execute a tool with a given input.

        The input is validated against the tool's
        input schema.

        Args:
          env: Set of key-value pairs to add to the tool's execution environment.

          http: Configuration for HTTP requests and authentication.

          input: The input to the tool. This must be a valid JSON-serializable object. It will be
              validated against the tool's input schema.

          revision_id: The Tool revision ID to execute. This optional parmeter is used to pin
              executions to specific versions of the Tool. If not provided, the latest
              (current) version of the Tool will be executed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v1/tools/{id}/execute",
            body=await async_maybe_transform(
                {
                    "env": env,
                    "http": http,
                    "input": input,
                    "revision_id": revision_id,
                },
                tool_exec_params.ToolExecParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolExecResponse,
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
    ) -> Tool:
        """
        Retrieves a tool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/tools/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tool,
        )


class ToolsResourceWithRawResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.create = to_raw_response_wrapper(
            tools.create,
        )
        self.update = to_raw_response_wrapper(
            tools.update,
        )
        self.list = to_raw_response_wrapper(
            tools.list,
        )
        self.exec = to_raw_response_wrapper(
            tools.exec,
        )
        self.get = to_raw_response_wrapper(
            tools.get,
        )


class AsyncToolsResourceWithRawResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.create = async_to_raw_response_wrapper(
            tools.create,
        )
        self.update = async_to_raw_response_wrapper(
            tools.update,
        )
        self.list = async_to_raw_response_wrapper(
            tools.list,
        )
        self.exec = async_to_raw_response_wrapper(
            tools.exec,
        )
        self.get = async_to_raw_response_wrapper(
            tools.get,
        )


class ToolsResourceWithStreamingResponse:
    def __init__(self, tools: ToolsResource) -> None:
        self._tools = tools

        self.create = to_streamed_response_wrapper(
            tools.create,
        )
        self.update = to_streamed_response_wrapper(
            tools.update,
        )
        self.list = to_streamed_response_wrapper(
            tools.list,
        )
        self.exec = to_streamed_response_wrapper(
            tools.exec,
        )
        self.get = to_streamed_response_wrapper(
            tools.get,
        )


class AsyncToolsResourceWithStreamingResponse:
    def __init__(self, tools: AsyncToolsResource) -> None:
        self._tools = tools

        self.create = async_to_streamed_response_wrapper(
            tools.create,
        )
        self.update = async_to_streamed_response_wrapper(
            tools.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tools.list,
        )
        self.exec = async_to_streamed_response_wrapper(
            tools.exec,
        )
        self.get = async_to_streamed_response_wrapper(
            tools.get,
        )
