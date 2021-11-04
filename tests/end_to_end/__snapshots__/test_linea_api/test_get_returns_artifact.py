import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

source_1 = SourceCode(
    code="""import lineapy
x = 1
lineapy.save(x, "x")

res = lineapy.get("x")
y = res.value + 1
lineapy.save(y, "y")
""",
    location=PosixPath("[source file path]"),
)
import_1 = ImportNode(
    source_location=SourceLocation(
        lineno=1,
        col_offset=0,
        end_lineno=1,
        end_col_offset=14,
        source_code=source_1.id,
    ),
    library=Library(
        name="lineapy",
    ),
)
call_2 = CallNode(
    source_location=SourceLocation(
        lineno=3,
        col_offset=0,
        end_lineno=3,
        end_col_offset=20,
        source_code=source_1.id,
    ),
    function_id=CallNode(
        source_location=SourceLocation(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=12,
            source_code=source_1.id,
        ),
        function_id=LookupNode(
            name="getattr",
        ).id,
        positional_args=[
            import_1.id,
            LiteralNode(
                value="save",
            ).id,
        ],
    ).id,
    positional_args=[
        LiteralNode(
            source_location=SourceLocation(
                lineno=2,
                col_offset=4,
                end_lineno=2,
                end_col_offset=5,
                source_code=source_1.id,
            ),
            value=1,
        ).id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=3,
                col_offset=16,
                end_lineno=3,
                end_col_offset=19,
                source_code=source_1.id,
            ),
            value="x",
        ).id,
    ],
)
call_8 = CallNode(
    source_location=SourceLocation(
        lineno=7,
        col_offset=0,
        end_lineno=7,
        end_col_offset=20,
        source_code=source_1.id,
    ),
    function_id=CallNode(
        source_location=SourceLocation(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=12,
            source_code=source_1.id,
        ),
        function_id=LookupNode(
            name="getattr",
        ).id,
        positional_args=[
            import_1.id,
            LiteralNode(
                value="save",
            ).id,
        ],
    ).id,
    positional_args=[
        CallNode(
            source_location=SourceLocation(
                lineno=6,
                col_offset=4,
                end_lineno=6,
                end_col_offset=17,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="add",
            ).id,
            positional_args=[
                CallNode(
                    source_location=SourceLocation(
                        lineno=6,
                        col_offset=4,
                        end_lineno=6,
                        end_col_offset=13,
                        source_code=source_1.id,
                    ),
                    function_id=LookupNode(
                        name="getattr",
                    ).id,
                    positional_args=[
                        CallNode(
                            source_location=SourceLocation(
                                lineno=5,
                                col_offset=6,
                                end_lineno=5,
                                end_col_offset=22,
                                source_code=source_1.id,
                            ),
                            function_id=CallNode(
                                source_location=SourceLocation(
                                    lineno=5,
                                    col_offset=6,
                                    end_lineno=5,
                                    end_col_offset=17,
                                    source_code=source_1.id,
                                ),
                                function_id=LookupNode(
                                    name="getattr",
                                ).id,
                                positional_args=[
                                    import_1.id,
                                    LiteralNode(
                                        value="get",
                                    ).id,
                                ],
                            ).id,
                            positional_args=[
                                LiteralNode(
                                    source_location=SourceLocation(
                                        lineno=5,
                                        col_offset=18,
                                        end_lineno=5,
                                        end_col_offset=21,
                                        source_code=source_1.id,
                                    ),
                                    value="x",
                                ).id
                            ],
                        ).id,
                        LiteralNode(
                            value="value",
                        ).id,
                    ],
                ).id,
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=6,
                        col_offset=16,
                        end_lineno=6,
                        end_col_offset=17,
                        source_code=source_1.id,
                    ),
                    value=1,
                ).id,
            ],
        ).id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=7,
                col_offset=16,
                end_lineno=7,
                end_col_offset=19,
                source_code=source_1.id,
            ),
            value="y",
        ).id,
    ],
)
