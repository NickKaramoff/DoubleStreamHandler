import logging

from io import StringIO
from unittest import TestCase, main
from unittest.mock import patch


class DoubleStreamHandlerTestCase(TestCase):
    @patch("sys.stderr", new_callable=StringIO)
    @patch("sys.stdout", new_callable=StringIO)
    def test(self, mock_stdout, mock_stderr):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(message)s")

        custom_out = StringIO()
        custom_err = StringIO()

        from double_stream_handler import DoubleStreamHandler

        handler_default = DoubleStreamHandler()
        handler_default.setFormatter(formatter)
        handler_custom = DoubleStreamHandler(
            err_level=logging.CRITICAL, streams=(custom_out, custom_err)
        )
        handler_custom.setFormatter(formatter)
        logger.addHandler(handler_default)
        logger.addHandler(handler_custom)

        logger.debug("Debug")
        logger.info("Info")
        logger.warning("Warning")
        logger.error("Error")
        logger.critical("Critical")

        self.assertEqual(mock_stdout.getvalue(), "Debug\nInfo\n")
        self.assertEqual(mock_stderr.getvalue(), "Warning\nError\nCritical\n")

        self.assertEqual(custom_out.getvalue(), "Debug\nInfo\nWarning\nError\n")
        self.assertEqual(custom_err.getvalue(), "Critical\n")


if __name__ == "__main__":
    main()
