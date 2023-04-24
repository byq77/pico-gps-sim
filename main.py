from machine import UART, Pin
import time
import ujson

def main():
    gps1_uart = UART(0, 9600, bits=8, parity=None, stop=1, tx=Pin(0), rx=Pin(1))
    gps2_uart = UART(1, 9600, bits=8, parity=None, stop=1, tx=Pin(4), rx=Pin(5))
    led = Pin("LED", Pin.OUT)

    with open("nema_gga_test_data.json", "r") as f:
        json_data = ujson.load(f)
    
    gps1_test_data = json_data['GPS1']
    gps2_test_data = json_data['GPS2']

    max_samples = min(len(gps1_test_data), len(gps2_test_data))

    while True:
        for i in range(max_samples):
            led.on()

            gps1_msg = bytes(gps1_test_data[i] + "\r\n", "utf-8")
            # print(gps1_msg.decode('utf-8'))
            gps1_uart.write(gps1_msg)

            gps2_msg = bytes(gps2_test_data[i] + "\r\n", "utf-8")
            # print(gps2_msg.decode('utf-8'))
            gps2_uart.write(gps2_msg)

            led.off()
            time.sleep(1)

if __name__ == "__main__":
    main()