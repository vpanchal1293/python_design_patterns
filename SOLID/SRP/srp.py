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

class I2CCommunicator():
    def __init__(self):
        pass
    
    def connect(self):
        print('I2C connected')
    
    def diconnect(self):
        print('I2C disconnected')
        
    def rx(self):
        rx_data = 'ABCD' 
        print(f'I2C RX data : {rx_data}')
        return rx_data
    
    def tx(self, tx_data):
        print(f'I2C TX data : {tx_data}')

class ProtocolFileHandler:
    def __init__(self):
        pass
    
    def file_rx(self, protocol_handler, filename):
        rx_data = protocol_handler.rx()
        with open(filename,'w') as readfile:
            readfile.write(rx_data)

    def file_tx(self, protocol_handler, filename):
        with open(filename,'r') as readfile:
            tx_data = readfile.read()
            protocol_handler.tx(tx_data)
        
uart_com = UARTCommunicator()
uart_protcol_file_handler = ProtocolFileHandler()
uart_protcol_file_handler.file_rx(uart_com, './temp/uart_rx.txt')
uart_protcol_file_handler.file_tx(uart_com, './temp/uart_rx.txt')

i2c_com = I2CCommunicator()
i2c_protcol_file_handler = ProtocolFileHandler()
i2c_protcol_file_handler.file_rx(i2c_com, './temp/i2c_rx.txt')
i2c_protcol_file_handler.file_tx(i2c_com, './temp/i2c_rx.txt')
