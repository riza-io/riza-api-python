# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from rizaio import Riza, AsyncRiza
from tests.utils import assert_matches_type
from rizaio.types.runtimes import Revision, RevisionListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRevisions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Riza) -> None:
        revision = client.runtimes.revisions.create(
            id="id",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
        )
        assert_matches_type(Revision, revision, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Riza) -> None:
        revision = client.runtimes.revisions.create(
            id="id",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
            additional_python_imports="additional_python_imports",
        )
        assert_matches_type(Revision, revision, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Riza) -> None:
        response = client.runtimes.revisions.with_raw_response.create(
            id="id",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert_matches_type(Revision, revision, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Riza) -> None:
        with client.runtimes.revisions.with_streaming_response.create(
            id="id",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert_matches_type(Revision, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Riza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.runtimes.revisions.with_raw_response.create(
                id="",
                manifest_file={
                    "contents": "contents",
                    "name": "requirements.txt",
                },
            )

    @parametrize
    def test_method_list(self, client: Riza) -> None:
        revision = client.runtimes.revisions.list(
            "id",
        )
        assert_matches_type(RevisionListResponse, revision, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Riza) -> None:
        response = client.runtimes.revisions.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert_matches_type(RevisionListResponse, revision, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Riza) -> None:
        with client.runtimes.revisions.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert_matches_type(RevisionListResponse, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Riza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.runtimes.revisions.with_raw_response.list(
                "",
            )

    @parametrize
    def test_method_get(self, client: Riza) -> None:
        revision = client.runtimes.revisions.get(
            revision_id="revision_id",
            runtime_id="runtime_id",
        )
        assert_matches_type(Revision, revision, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Riza) -> None:
        response = client.runtimes.revisions.with_raw_response.get(
            revision_id="revision_id",
            runtime_id="runtime_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert_matches_type(Revision, revision, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Riza) -> None:
        with client.runtimes.revisions.with_streaming_response.get(
            revision_id="revision_id",
            runtime_id="runtime_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert_matches_type(Revision, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Riza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `runtime_id` but received ''"):
            client.runtimes.revisions.with_raw_response.get(
                revision_id="revision_id",
                runtime_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            client.runtimes.revisions.with_raw_response.get(
                revision_id="",
                runtime_id="runtime_id",
            )


class TestAsyncRevisions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncRiza) -> None:
        revision = await async_client.runtimes.revisions.create(
            id="id",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
        )
        assert_matches_type(Revision, revision, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRiza) -> None:
        revision = await async_client.runtimes.revisions.create(
            id="id",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
            additional_python_imports="additional_python_imports",
        )
        assert_matches_type(Revision, revision, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRiza) -> None:
        response = await async_client.runtimes.revisions.with_raw_response.create(
            id="id",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert_matches_type(Revision, revision, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRiza) -> None:
        async with async_client.runtimes.revisions.with_streaming_response.create(
            id="id",
            manifest_file={
                "contents": "contents",
                "name": "requirements.txt",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert_matches_type(Revision, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncRiza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.runtimes.revisions.with_raw_response.create(
                id="",
                manifest_file={
                    "contents": "contents",
                    "name": "requirements.txt",
                },
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRiza) -> None:
        revision = await async_client.runtimes.revisions.list(
            "id",
        )
        assert_matches_type(RevisionListResponse, revision, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRiza) -> None:
        response = await async_client.runtimes.revisions.with_raw_response.list(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert_matches_type(RevisionListResponse, revision, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRiza) -> None:
        async with async_client.runtimes.revisions.with_streaming_response.list(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert_matches_type(RevisionListResponse, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncRiza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.runtimes.revisions.with_raw_response.list(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncRiza) -> None:
        revision = await async_client.runtimes.revisions.get(
            revision_id="revision_id",
            runtime_id="runtime_id",
        )
        assert_matches_type(Revision, revision, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncRiza) -> None:
        response = await async_client.runtimes.revisions.with_raw_response.get(
            revision_id="revision_id",
            runtime_id="runtime_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert_matches_type(Revision, revision, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncRiza) -> None:
        async with async_client.runtimes.revisions.with_streaming_response.get(
            revision_id="revision_id",
            runtime_id="runtime_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert_matches_type(Revision, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncRiza) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `runtime_id` but received ''"):
            await async_client.runtimes.revisions.with_raw_response.get(
                revision_id="revision_id",
                runtime_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `revision_id` but received ''"):
            await async_client.runtimes.revisions.with_raw_response.get(
                revision_id="",
                runtime_id="runtime_id",
            )
