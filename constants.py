# TODO:
#   CREATE AN EDGE CASE KWD WHERE FILE IS ONE PACKET

# Constants file

_byte_encoding = 'utf-8'

# Master keyword prefix
_kwd_prefix = bytes('D`A`T`A`T`A`P`E`', _byte_encoding)

# Transmission control keywords
# beginning of transmission
bot_kwd = _kwd_prefix + bytes('TBOTxxxx', _byte_encoding)
# end of transmission
eot_kwd = _kwd_prefix + bytes('TEOTxxxx', _byte_encoding)

# File control keywords
# beginning of file
bof_kwd = _kwd_prefix + bytes('FBOFxxxx', _byte_encoding)
# first packet of file
fpof_kwd = _kwd_prefix + bytes('FFPFxxxx', _byte_encoding)
# in file
inf_kwd = _kwd_prefix + bytes('FINFxxxx', _byte_encoding)
# last packet of file
lpof_kwd = _kwd_prefix + bytes('FLPFxxxx', _byte_encoding)
# end of file
eof_kwd = _kwd_prefix + bytes('FEOFxxxx', _byte_encoding)

# FPGA state control keywords
# tape read start
tape_read_start_kwd = _kwd_prefix + bytes('CTRSxxxx', _byte_encoding)
# tape read end
tape_read_end_kwd = _kwd_prefix + bytes('CTRExxxx', _byte_encoding)

# tape write start
tape_write_start_kwd = _kwd_prefix + bytes('CTWSxxxx', _byte_encoding)
# tape write end
tape_write_end_kwd = _kwd_prefix + bytes('CTWExxxx', _byte_encoding)
# transmission continue
tape_write_cont_kwd = _kwd_prefix + bytes('CTWCxxxx', _byte_encoding)
# transmission pause
tape_write_pause_kwd = _kwd_prefix + bytes('CTWPxxxx', _byte_encoding)

# command acknowledge
cmd_ack = _kwd_prefix + bytes('CACKxxxx', _byte_encoding)

# keyword set for comparison
valid_kwds = (bot_kwd, eot_kwd, bof_kwd, fpof_kwd, inf_kwd, lpof_kwd, eof_kwd,
              tape_read_start_kwd, tape_read_end_kwd, tape_write_start_kwd,
              tape_write_end_kwd, tape_write_cont_kwd, tape_write_pause_kwd, cmd_ack)


# Packet info
header_size = 24
payload_size = 376


# ensure keywords size is correct
for i in valid_kwds:
    if len(i) != header_size:
        raise ValueError(f'a keyword was not the correct size: {i}')