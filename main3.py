from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ConnectionException
import os

# PLC_ADDR = os.getenv("PLC_ADDR", "localhost")
PLC_ADDR = "192.168.1.5"
PLC_MODBUS_PORT = 502


if __name__ == "__main__":
    _plc_addr = PLC_ADDR
    _plc_port = PLC_MODBUS_PORT
    mc_conn = ModbusTcpClient(host=_plc_addr, port=_plc_port)
    try:
        is_connect = mc_conn.connect()
        if mc_conn.is_socket_open():
            result = mc_conn.read_holding_registers(
                address=6, count=3, slave=1
            )
            print(result)
    except ConnectionException as e:
        print(f"AFTER Fail to connected to Modbus TCP server == {mc_conn}.")