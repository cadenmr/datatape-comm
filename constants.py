# Constants file

_byte_encoding = 'utf-8'

# Master keyword prefix
_kwd_prefix = bytes('D`A`T`A`T`A`P`E`', _byte_encoding)

# Transmission control keywords
bot_kwd = _kwd_prefix + bytes('TBOTxxxx', _byte_encoding)
eot_kwd = _kwd_prefix + bytes('TEOTxxxxx', _byte_encoding)

# File control keywords
bof_kwd = _kwd_prefix + bytes('FBOFxxxx', _byte_encoding)
eof_kwd = _kwd_prefix + bytes('FEOFxxxx', _byte_encoding)

# FPGA state control keywords
tape_read_start_kwd = _kwd_prefix + bytes('CTRSxxxx', _byte_encoding)
tape_read_end_kwd = _kwd_prefix + bytes('CTRExxxx', _byte_encoding)

tape_write_start_kwd = _kwd_prefix + bytes('CTWSxxxx', _byte_encoding)
tape_write_end_kwd = _kwd_prefix + bytes('CTWExxxx', _byte_encoding)

fpga_cmd_ack = _kwd_prefix + bytes('CACKxxxx', _byte_encoding)
