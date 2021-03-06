import logging
from simuvex.s_format import FormatParser
from . import _IO_FILE

l = logging.getLogger("simuvex.procedures.libc_so_6.fprintf")

######################################
# fprintf
######################################

class fprintf(FormatParser):

    def run(self, file_ptr):
        # The format str is at index 1
        fmt_str = self._parse(1)
        out_str = fmt_str.replace(2, self.arg)

        fd_offset = _IO_FILE[self.state.arch.name]['fd']
        fileno = self.state.mem[file_ptr + fd_offset:].int.resolved
        self.state.posix.write(fileno, out_str, out_str.size() / 8)

        return out_str.size() / 8
