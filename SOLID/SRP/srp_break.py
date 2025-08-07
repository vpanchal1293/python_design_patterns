# Below example is breaking SRP
class UARTCommunicator:
    def __init__(self):
        pass
    
    def connect(self):
        print('UART connected')
    
    def diconnect(self):
        print('UART disconnected')
        
    def rx(self):
        rx_data = 'ABCD' 
        print(f'UART RX data : {rx_data}')
        return rx_data
    
    def tx(self, tx_data):
        print(f'UART TX data : {tx_data}')
        
    def file_rx(self, filename):
        rx_data = 'ABCD'
        with open(filename,'w') as readfile:
            readfile.write(rx_data)

    def file_tx(self, filename):
        with open(filename,'r') as readfile:
            tx_data = readfile.read()
            print(f'UART TX data : {tx_data}')
        
uart_com = UARTCommunicator()
uart_com.rx()
uart_com.tx('XYZ')
