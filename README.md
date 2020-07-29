# datatape-comm
Computer interface scripts for the datatape project

### Software is UNFINISHED and NON-WORKING

## Data Transmission Standard
4 bytes per UDP packet: 
`xx xx xx xx`

#### Computer to FPGA
First byte is the run mode:
`00: Stop`, `01: Read`, `02: Write`

Second byte is reserved for future use.
Third byte is reserved for future use.

Fourth byte is data.

#### FPGA to computer
First byte is the system status:
`00: Stop`, `01: Data Wait`, `02: Data Run`

Second byte is reserved for future use.
Third byte is reserved for future use.

Fourth byte is data.
