import inspect

from kubiya_sdk.tools.models import Tool, Arg, FileSpec

from .main import main

hello_tool = Tool(
    name="say_hello",
    type="docker",
    image="python:3.12-slim-bullseye",
    description="Greets person in a random movie star way",
    args=[Arg(name="name", description="name to say hello to", required=True)],
    content="""
pip install litellm==1.59.5

python /tmp/main.py --name "{{ .name }}"
""",
    with_files=[
        FileSpec(
            destination="/tmp/main.py",
            content=inspect.getsource(main),
        ),
    ],
)
