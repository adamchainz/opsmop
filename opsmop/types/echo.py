
from opsmop.core.field import Field
from opsmop.core.fields import Fields
from opsmop.core.errors import ValidationError
from opsmop.types.type import Type

import inspect

class Echo(Type):

    """
    Represents a debug statement
    """

    def __init__(self, msg, *args, **kwargs):
        kwargs['msg'] = msg
        super().__init__(self, *args, **kwargs)

    def fields(self):
        return Fields(
            msg = Field(kind=str, allow_none=False, help="string to print")
        )

    def validate(self):
        pass

    def default_provider(self, facts):
        from opsmop.providers.echo import Echo
        return Echo
