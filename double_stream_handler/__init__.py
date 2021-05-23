import logging
import sys
from typing import TextIO, Tuple

__version__ = "0.1.0"


class DoubleStreamHandler(logging.StreamHandler):
    terminator = "\n"

    def __init__(
        self,
        err_from: int = logging.WARNING,
        streams: Tuple[TextIO, TextIO] = (sys.stdout, sys.stderr),
    ) -> None:
        logging.StreamHandler.__init__(self)

        out_stream, err_stream = streams
        self.out_handler = logging.StreamHandler(stream=out_stream)
        self.err_handler = logging.StreamHandler(stream=err_stream)
        self.err_from = err_from

    def flush(self) -> None:
        self.err_handler.flush()
        self.out_handler.flush()

    def emit(self, record: logging.LogRecord):
        if record.levelno >= self.err_from:
            self.err_handler.emit(record=record)
        else:
            self.out_handler.emit(record=record)

    def setStream(self, stream):
        return None

    def __repr__(self):
        level = logging.getLevelName(self.level)
        out_name = getattr(self.out_handler.stream, "name", "")
        err_name = getattr(self.err_handler.stream, "name", "")
        #  bpo-36015: name can be an int
        out_name = str(out_name)
        err_name = str(err_name)
        if out_name:
            out_name += " "
        if err_name:
            err_name += " "

        return "<%s (%s, %s)(%s)>" % (
            self.__class__.__name__,
            out_name,
            err_name,
            level,
        )
