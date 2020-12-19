"""
Source: https://github.com/sqlalchemy/sqlalchemy/issues/3467
"""

import re

from sqlalchemy import TypeDecorator, cast
from sqlalchemy.dialects.postgresql import ARRAY


class ArrayOfEnum(TypeDecorator):
    impl = ARRAY

    def bind_expression(self, bindvalue):
        return cast(bindvalue, self)

    def result_processor(self, dialect, coltype):
        super_rp = super(ArrayOfEnum, self).result_processor(dialect, coltype)

        def handle_raw_string(value):
            inner = re.match(r"^{(.*)}$", value).group(1)

            return inner.split(",") if inner else []

        def process(value):
            if value is None:
                return None

            return super_rp(handle_raw_string(value))

        return process
