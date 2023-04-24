# pico gps simulator
Simulate two GPS sensors on using UARTs

```shell
pip3 install adafruit-ampy
```

```shell
ampy --port <<port_name>> put main.py
ampy --port <<port_name>> put nema_gga_test_data.json
```

```shell
ampy --port <<port_name>> reset --hard
```