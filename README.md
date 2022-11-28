# tcpcunt

TCP 3way handshake fuzzer in Python.312 with Scapy

## command line arguments
* target: target IPv4/IPv6 address
* port: destination port
* strategy: bypass|dos

# strategies
* dos: aim to halt, confuse or shut down the target. this may be illegal
* bypass: inject into open TCP/IP window as in seq number prediction. this too.
