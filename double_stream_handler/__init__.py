import logging
import sys

from typing import TextIO, Tuple


__version__ = "1.0.0"


class DoubleStreamHandler(logging.Handler):
    terminator = "\n"

    def __init__(
        self,
        err_level: int = logging.WARNING,
        streams: Tuple[TextIO, TextIO] = (sys.stdout, sys.stderr),
    ) -> None:
        logging.Handler.__init__(self)

        self.out, self.err = streams
        self.err_level = err_level

    def flush(self) -> None:
        self.acquire()
        try:
            for stream in [self.err, self.out]:
                if stream and hasattr(stream, "flush"):
                    stream.flush()
        finally:
            self.release()

    def emit(self, record: logging.LogRecord):
        if record.levelno >= self.err_level:
            stream = self.err
        else:
            stream = self.out

        try:
            msg = self.format(record)
            stream.write(msg + self.terminator)
            self.flush()
        except RecursionError:
            raise
        except Exception:
            self.handleError(record)

    def __repr__(self):
        err_level_name = logging.getLevelName(self.err_level)
        out_name = str(getattr(self.out, "name", ""))
        err_name = str(getattr(self.err, "name", ""))

        return "<%s err_level='%s', streams=(%s, %s)>" % (
            self.__class__.__name__,
            err_level_name,
            out_name,
            err_name,
        )
