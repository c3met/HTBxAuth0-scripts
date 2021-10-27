from pwn import * 
import re

context.log_level = 'info'

# connect to server
io = remote('<server-ip>', '<server-port>')


def solve(io):
    io.recvuntil(':\n\n')
    calc = io.recvline().decode().strip() # get question

    calc_2 = re.sub('\\?','', calc )
    calc_3 = re.sub('\\=','', calc_2 ) # remove ? and = from message

    answer = eval(calc_3) # calculate solution
    info('Answer: %s', answer)

    io.sendlineafter(':', str(answer)) # send answer

for i in range(777):
    solve(io)

# switch to interactive shell
io.interactive()
