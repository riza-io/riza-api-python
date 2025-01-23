# Secrets

Types:

```python
from rizaio.types import Secret, SecretListResponse
```

Methods:

- <code title="post /v1/secrets">client.secrets.<a href="./src/rizaio/resources/secrets.py">create</a>(\*\*<a href="src/rizaio/types/secret_create_params.py">params</a>) -> <a href="./src/rizaio/types/secret.py">Secret</a></code>
- <code title="get /v1/secrets">client.secrets.<a href="./src/rizaio/resources/secrets.py">list</a>() -> <a href="./src/rizaio/types/secret_list_response.py">SecretListResponse</a></code>

# Tools

Types:

```python
from rizaio.types import Tool, ToolListResponse, ToolExecResponse
```

Methods:

- <code title="post /v1/tools">client.tools.<a href="./src/rizaio/resources/tools.py">create</a>(\*\*<a href="src/rizaio/types/tool_create_params.py">params</a>) -> <a href="./src/rizaio/types/tool.py">Tool</a></code>
- <code title="post /v1/tools/{id}">client.tools.<a href="./src/rizaio/resources/tools.py">update</a>(id, \*\*<a href="src/rizaio/types/tool_update_params.py">params</a>) -> <a href="./src/rizaio/types/tool.py">Tool</a></code>
- <code title="get /v1/tools">client.tools.<a href="./src/rizaio/resources/tools.py">list</a>() -> <a href="./src/rizaio/types/tool_list_response.py">ToolListResponse</a></code>
- <code title="post /v1/tools/{id}/execute">client.tools.<a href="./src/rizaio/resources/tools.py">exec</a>(id, \*\*<a href="src/rizaio/types/tool_exec_params.py">params</a>) -> <a href="./src/rizaio/types/tool_exec_response.py">ToolExecResponse</a></code>
- <code title="get /v1/tools/{id}">client.tools.<a href="./src/rizaio/resources/tools.py">get</a>(id) -> <a href="./src/rizaio/types/tool.py">Tool</a></code>

# Command

Types:

```python
from rizaio.types import CommandExecResponse, CommandExecFuncResponse
```

Methods:

- <code title="post /v1/execute">client.command.<a href="./src/rizaio/resources/command.py">exec</a>(\*\*<a href="src/rizaio/types/command_exec_params.py">params</a>) -> <a href="./src/rizaio/types/command_exec_response.py">CommandExecResponse</a></code>
- <code title="post /v1/execute-function">client.command.<a href="./src/rizaio/resources/command.py">exec_func</a>(\*\*<a href="src/rizaio/types/command_exec_func_params.py">params</a>) -> <a href="./src/rizaio/types/command_exec_func_response.py">CommandExecFuncResponse</a></code>

# Runtimes

Types:

```python
from rizaio.types import Runtime, RuntimeListResponse
```

Methods:

- <code title="post /v1/runtimes">client.runtimes.<a href="./src/rizaio/resources/runtimes/runtimes.py">create</a>(\*\*<a href="src/rizaio/types/runtime_create_params.py">params</a>) -> <a href="./src/rizaio/types/runtime.py">Runtime</a></code>
- <code title="get /v1/runtimes">client.runtimes.<a href="./src/rizaio/resources/runtimes/runtimes.py">list</a>() -> <a href="./src/rizaio/types/runtime_list_response.py">RuntimeListResponse</a></code>
- <code title="get /v1/runtimes/{id}">client.runtimes.<a href="./src/rizaio/resources/runtimes/runtimes.py">get</a>(id) -> <a href="./src/rizaio/types/runtime.py">Runtime</a></code>

## Revisions

Types:

```python
from rizaio.types.runtimes import Revision, RevisionListResponse
```

Methods:

- <code title="post /v1/runtimes/{id}/revisions">client.runtimes.revisions.<a href="./src/rizaio/resources/runtimes/revisions.py">create</a>(id, \*\*<a href="src/rizaio/types/runtimes/revision_create_params.py">params</a>) -> <a href="./src/rizaio/types/runtimes/revision.py">Revision</a></code>
- <code title="get /v1/runtimes/{id}/revisions">client.runtimes.revisions.<a href="./src/rizaio/resources/runtimes/revisions.py">list</a>(id) -> <a href="./src/rizaio/types/runtimes/revision_list_response.py">RevisionListResponse</a></code>
- <code title="get /v1/runtimes/{runtime_id}/revisions/{revision_id}">client.runtimes.revisions.<a href="./src/rizaio/resources/runtimes/revisions.py">get</a>(revision_id, \*, runtime_id) -> <a href="./src/rizaio/types/runtimes/revision.py">Revision</a></code>
