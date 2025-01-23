import inspect

from kubiya_sdk.tools.models import Tool, Arg, FileSpec
from kubiya_sdk.tools.registry import tool_registry

from . import main

hello_tool = Tool(
    name="say_hello",
    type="docker",
    image="python:3.12-slim-bullseye",
    description="Says hello",
    args=[Arg(name="name", description="surname", required=True),
    Arg(name="last_name", description="last name", required=True)],
    #env=["LLM_BASE_URL"],
    #secrets=["LLM_API_KEY"],
    content="""
python /tmp/main.py --name "{{ .name }} --last_name {{ .last_name}}"
""",
    with_files=[
        FileSpec(
            destination="/tmp/main.py",
            content=inspect.getsource(main),
        ),
    ],
)

tool_registry.register(hello_tool)
