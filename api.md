# Secrets

Types:

```python
from rizaio.types import Secret, SecretListResponse
```

Methods:

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
from rizaio.types import CommandExecResponse
```

Methods:

- <code title="post /v1/execute">client.command.<a href="./src/rizaio/resources/command.py">exec</a>(\*\*<a href="src/rizaio/types/command_exec_params.py">params</a>) -> <a href="./src/rizaio/types/command_exec_response.py">CommandExecResponse</a></code>
