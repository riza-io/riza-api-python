# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "Execution",
    "Details",
    "DetailsToolExecutionDetails",
    "DetailsToolExecutionDetailsRequest",
    "DetailsToolExecutionDetailsRequestEnv",
    "DetailsToolExecutionDetailsRequestHTTP",
    "DetailsToolExecutionDetailsRequestHTTPAllow",
    "DetailsToolExecutionDetailsRequestHTTPAllowAuth",
    "DetailsToolExecutionDetailsRequestHTTPAllowAuthBasic",
    "DetailsToolExecutionDetailsRequestHTTPAllowAuthBearer",
    "DetailsToolExecutionDetailsRequestHTTPAllowAuthQuery",
    "DetailsToolExecutionDetailsResponse",
    "DetailsToolExecutionDetailsResponseExecution",
    "DetailsFunctionExecutionDetails",
    "DetailsFunctionExecutionDetailsRequest",
    "DetailsFunctionExecutionDetailsRequestFile",
    "DetailsFunctionExecutionDetailsRequestHTTP",
    "DetailsFunctionExecutionDetailsRequestHTTPAllow",
    "DetailsFunctionExecutionDetailsRequestHTTPAllowAuth",
    "DetailsFunctionExecutionDetailsRequestHTTPAllowAuthBasic",
    "DetailsFunctionExecutionDetailsRequestHTTPAllowAuthBearer",
    "DetailsFunctionExecutionDetailsRequestHTTPAllowAuthHeader",
    "DetailsFunctionExecutionDetailsRequestHTTPAllowAuthQuery",
    "DetailsFunctionExecutionDetailsRequestLimits",
    "DetailsFunctionExecutionDetailsResponse",
    "DetailsFunctionExecutionDetailsResponseExecution",
    "DetailsScriptExecutionDetails",
    "DetailsScriptExecutionDetailsRequest",
    "DetailsScriptExecutionDetailsRequestFile",
    "DetailsScriptExecutionDetailsRequestHTTP",
    "DetailsScriptExecutionDetailsRequestHTTPAllow",
    "DetailsScriptExecutionDetailsRequestHTTPAllowAuth",
    "DetailsScriptExecutionDetailsRequestHTTPAllowAuthBasic",
    "DetailsScriptExecutionDetailsRequestHTTPAllowAuthBearer",
    "DetailsScriptExecutionDetailsRequestHTTPAllowAuthHeader",
    "DetailsScriptExecutionDetailsRequestHTTPAllowAuthQuery",
    "DetailsScriptExecutionDetailsRequestLimits",
    "DetailsScriptExecutionDetailsResponse",
]


class DetailsToolExecutionDetailsRequestEnv(BaseModel):
    name: str

    secret_id: Optional[str] = None

    value: Optional[str] = None


class DetailsToolExecutionDetailsRequestHTTPAllowAuthBasic(BaseModel):
    password: Optional[str] = None

    secret_id: Optional[str] = None

    user_id: Optional[str] = None


class DetailsToolExecutionDetailsRequestHTTPAllowAuthBearer(BaseModel):
    token: Optional[str] = None
    """The token to set, e.g. 'Authorization: Bearer <token>'."""

    secret_id: Optional[str] = None


class DetailsToolExecutionDetailsRequestHTTPAllowAuthQuery(BaseModel):
    key: Optional[str] = None

    secret_id: Optional[str] = None

    value: Optional[str] = None


class DetailsToolExecutionDetailsRequestHTTPAllowAuth(BaseModel):
    basic: Optional[DetailsToolExecutionDetailsRequestHTTPAllowAuthBasic] = None

    bearer: Optional[DetailsToolExecutionDetailsRequestHTTPAllowAuthBearer] = None
    """Configuration to add an 'Authorization' header using the 'Bearer' scheme."""

    query: Optional[DetailsToolExecutionDetailsRequestHTTPAllowAuthQuery] = None


class DetailsToolExecutionDetailsRequestHTTPAllow(BaseModel):
    auth: Optional[DetailsToolExecutionDetailsRequestHTTPAllowAuth] = None
    """Authentication configuration for outbound requests to this host."""

    host: Optional[str] = None
    """The hostname to allow."""


class DetailsToolExecutionDetailsRequestHTTP(BaseModel):
    allow: Optional[List[DetailsToolExecutionDetailsRequestHTTPAllow]] = None
    """List of allowed HTTP hosts and associated authentication."""


class DetailsToolExecutionDetailsRequest(BaseModel):
    env: Optional[List[DetailsToolExecutionDetailsRequestEnv]] = None
    """Set of key-value pairs to add to the tool's execution environment."""

    http: Optional[DetailsToolExecutionDetailsRequestHTTP] = None
    """Configuration for HTTP requests and authentication."""

    input: Optional[object] = None
    """The input to the tool.

    This must be a valid JSON-serializable object. It will be validated against the
    tool's input schema.
    """

    revision_id: Optional[str] = None
    """The Tool revision ID to execute.

    This optional parmeter is used to pin executions to specific versions of the
    Tool. If not provided, the latest (current) version of the Tool will be
    executed.
    """


class DetailsToolExecutionDetailsResponseExecution(BaseModel):
    id: str
    """The ID of the execution."""

    duration: int
    """The execution time of the function in milliseconds."""

    exit_code: int
    """The exit code returned by the function.

    Will often be '0' on success and non-zero on failure.
    """

    stderr: str
    """The contents of 'stderr' after executing the function."""

    stdout: str
    """The contents of 'stdout' after executing the function."""


class DetailsToolExecutionDetailsResponse(BaseModel):
    execution: DetailsToolExecutionDetailsResponseExecution
    """The execution details of the function."""

    output: object
    """The returned value of the Tool's execute function."""

    output_status: Literal["error", "json_serialization_error", "valid"]
    """The status of the output.

    "valid" means your Tool executed successfully and returned a valid
    JSON-serializable object, or void. "json_serialization_error" means your Tool
    executed successfully, but returned a nonserializable object. "error" means your
    Tool failed to execute.
    """


class DetailsToolExecutionDetails(BaseModel):
    request: DetailsToolExecutionDetailsRequest

    response: DetailsToolExecutionDetailsResponse

    tool_id: str

    type: Literal["tool"]


class DetailsFunctionExecutionDetailsRequestFile(BaseModel):
    contents: Optional[str] = None
    """The contents of the file."""

    path: Optional[str] = None
    """The relative path of the file."""


class DetailsFunctionExecutionDetailsRequestHTTPAllowAuthBasic(BaseModel):
    password: Optional[str] = None

    user_id: Optional[str] = None


class DetailsFunctionExecutionDetailsRequestHTTPAllowAuthBearer(BaseModel):
    token: Optional[str] = None
    """The token to set, e.g. 'Authorization: Bearer <token>'."""


class DetailsFunctionExecutionDetailsRequestHTTPAllowAuthHeader(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None


class DetailsFunctionExecutionDetailsRequestHTTPAllowAuthQuery(BaseModel):
    key: Optional[str] = None

    value: Optional[str] = None


class DetailsFunctionExecutionDetailsRequestHTTPAllowAuth(BaseModel):
    basic: Optional[DetailsFunctionExecutionDetailsRequestHTTPAllowAuthBasic] = None

    bearer: Optional[DetailsFunctionExecutionDetailsRequestHTTPAllowAuthBearer] = None
    """Configuration to add an 'Authorization' header using the 'Bearer' scheme."""

    header: Optional[DetailsFunctionExecutionDetailsRequestHTTPAllowAuthHeader] = None

    query: Optional[DetailsFunctionExecutionDetailsRequestHTTPAllowAuthQuery] = None


class DetailsFunctionExecutionDetailsRequestHTTPAllow(BaseModel):
    auth: Optional[DetailsFunctionExecutionDetailsRequestHTTPAllowAuth] = None
    """Authentication configuration for outbound requests to this host."""

    host: Optional[str] = None
    """The hostname to allow."""


class DetailsFunctionExecutionDetailsRequestHTTP(BaseModel):
    allow: Optional[List[DetailsFunctionExecutionDetailsRequestHTTPAllow]] = None
    """List of allowed HTTP hosts and associated authentication."""


class DetailsFunctionExecutionDetailsRequestLimits(BaseModel):
    execution_timeout: Optional[int] = None
    """The maximum time allowed for execution (in seconds). Default is 30."""

    memory_size: Optional[int] = None
    """The maximum memory allowed for execution (in MiB). Default is 128."""


class DetailsFunctionExecutionDetailsRequest(BaseModel):
    code: str
    """The function to execute.

    Your code must define a function named "execute" that takes in a single argument
    and returns a JSON-serializable value.
    """

    language: Literal["python", "javascript", "typescript"]
    """The interpreter to use when executing code."""

    env: Optional[Dict[str, str]] = None
    """Set of key-value pairs to add to the function's execution environment."""

    files: Optional[List[DetailsFunctionExecutionDetailsRequestFile]] = None
    """List of input files."""

    http: Optional[DetailsFunctionExecutionDetailsRequestHTTP] = None
    """Configuration for HTTP requests and authentication."""

    input: Optional[object] = None
    """The input to the function.

    This must be a valid JSON-serializable object. If you do not pass an input, your
    function will be called with None (Python) or null (JavaScript/TypeScript) as
    the argument.
    """

    limits: Optional[DetailsFunctionExecutionDetailsRequestLimits] = None
    """Configuration for execution environment limits."""

    runtime_revision_id: Optional[str] = None
    """The ID of the runtime revision to use when executing code."""


class DetailsFunctionExecutionDetailsResponseExecution(BaseModel):
    id: str
    """The ID of the execution."""

    duration: int
    """The execution time of the function in milliseconds."""

    exit_code: int
    """The exit code returned by the function.

    Will often be '0' on success and non-zero on failure.
    """

    stderr: str
    """The contents of 'stderr' after executing the function."""

    stdout: str
    """The contents of 'stdout' after executing the function."""


class DetailsFunctionExecutionDetailsResponse(BaseModel):
    execution: DetailsFunctionExecutionDetailsResponseExecution
    """The execution details of the function."""

    output: object
    """The output of the function."""

    output_status: Literal["error", "json_serialization_error", "valid"]
    """The status of the output.

    "valid" means your function executed successfully and returned a valid
    JSON-serializable object, or void. "json_serialization_error" means your
    function executed successfully, but returned a nonserializable object. "error"
    means your function failed to execute.
    """


class DetailsFunctionExecutionDetails(BaseModel):
    request: DetailsFunctionExecutionDetailsRequest

    response: DetailsFunctionExecutionDetailsResponse

    type: Literal["function"]


class DetailsScriptExecutionDetailsRequestFile(BaseModel):
    contents: Optional[str] = None
    """The contents of the file."""

    path: Optional[str] = None
    """The relative path of the file."""


class DetailsScriptExecutionDetailsRequestHTTPAllowAuthBasic(BaseModel):
    password: Optional[str] = None

    user_id: Optional[str] = None


class DetailsScriptExecutionDetailsRequestHTTPAllowAuthBearer(BaseModel):
    token: Optional[str] = None
    """The token to set, e.g. 'Authorization: Bearer <token>'."""


class DetailsScriptExecutionDetailsRequestHTTPAllowAuthHeader(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None


class DetailsScriptExecutionDetailsRequestHTTPAllowAuthQuery(BaseModel):
    key: Optional[str] = None

    value: Optional[str] = None


class DetailsScriptExecutionDetailsRequestHTTPAllowAuth(BaseModel):
    basic: Optional[DetailsScriptExecutionDetailsRequestHTTPAllowAuthBasic] = None

    bearer: Optional[DetailsScriptExecutionDetailsRequestHTTPAllowAuthBearer] = None
    """Configuration to add an 'Authorization' header using the 'Bearer' scheme."""

    header: Optional[DetailsScriptExecutionDetailsRequestHTTPAllowAuthHeader] = None

    query: Optional[DetailsScriptExecutionDetailsRequestHTTPAllowAuthQuery] = None


class DetailsScriptExecutionDetailsRequestHTTPAllow(BaseModel):
    auth: Optional[DetailsScriptExecutionDetailsRequestHTTPAllowAuth] = None
    """Authentication configuration for outbound requests to this host."""

    host: Optional[str] = None
    """The hostname to allow."""


class DetailsScriptExecutionDetailsRequestHTTP(BaseModel):
    allow: Optional[List[DetailsScriptExecutionDetailsRequestHTTPAllow]] = None
    """List of allowed HTTP hosts and associated authentication."""


class DetailsScriptExecutionDetailsRequestLimits(BaseModel):
    execution_timeout: Optional[int] = None
    """The maximum time allowed for execution (in seconds). Default is 30."""

    memory_size: Optional[int] = None
    """The maximum memory allowed for execution (in MiB). Default is 128."""


class DetailsScriptExecutionDetailsRequest(BaseModel):
    code: str
    """The code to execute."""

    language: Literal["python", "javascript", "typescript", "ruby", "php"]
    """The interpreter to use when executing code."""

    args: Optional[List[str]] = None
    """List of command line arguments to pass to the script."""

    env: Optional[Dict[str, str]] = None
    """Set of key-value pairs to add to the script's execution environment."""

    files: Optional[List[DetailsScriptExecutionDetailsRequestFile]] = None
    """List of input files."""

    http: Optional[DetailsScriptExecutionDetailsRequestHTTP] = None
    """Configuration for HTTP requests and authentication."""

    limits: Optional[DetailsScriptExecutionDetailsRequestLimits] = None
    """Configuration for execution environment limits."""

    runtime_revision_id: Optional[str] = None
    """The ID of the runtime revision to use when executing code."""

    stdin: Optional[str] = None
    """Input made available to the script via 'stdin'."""


class DetailsScriptExecutionDetailsResponse(BaseModel):
    id: str
    """The ID of the execution."""

    duration: int
    """The execution time of the script in milliseconds."""

    exit_code: int
    """The exit code returned by the script.

    Will often be '0' on success and non-zero on failure.
    """

    stderr: str
    """The contents of 'stderr' after executing the script."""

    stdout: str
    """The contents of 'stdout' after executing the script."""


class DetailsScriptExecutionDetails(BaseModel):
    request: DetailsScriptExecutionDetailsRequest

    response: DetailsScriptExecutionDetailsResponse

    type: Literal["script"]


Details: TypeAlias = Annotated[
    Union[DetailsToolExecutionDetails, DetailsFunctionExecutionDetails, DetailsScriptExecutionDetails],
    PropertyInfo(discriminator="type"),
]


class Execution(BaseModel):
    id: str

    duration: int

    exit_code: int

    language: Literal["python", "javascript", "typescript", "ruby", "php"]

    started_at: datetime

    details: Optional[Details] = None
