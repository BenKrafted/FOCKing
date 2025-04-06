title = "<tspan class='h1'>KINGpill</tspan> <tspan class='h2'>Pinout</tspan>"
description = "Pinout diagram for the KINGpill board."

legend = [
    ("Power", "pwr"),
    ("PWM", "pwm"),
    ("GPIO", "gpio"),
    ("Analog", "analog"),
    ("CAN/I2C/SPI/SWD", "comms"),
    ("Unused", "unused"),
]

left_header = [
    [("PC12", "unused")],
    [("H1", "pwm")],
    [("H2", "pwm")],
    [("H3", "pwm")],
    [("L1", "pwm")],
    [("L2", "pwm")],
    [("L3", "pwm")],
    [("TX_SCL_MOSI", "comms", {"body": {"width": 150}})],
    [("MISO_ADC_EXT2", "comms", {"body": {"width": 150}})],
    [("SCK_ADC_EXT", "comms", {"body": {"width": 150}})],
    [("RX_SDA_NSS", "comms", {"body": {"width": 150}})],
    [("ADC_9", "analog")],
    [("ADC_8", "analog")],
    [("LED_RED", "gpio")],
    [("TEMP_MOTOR", "analog", {"body": {"width": 150}})],
    [("CAN_RX", "comms")],
    [("CAN_TX", "comms")],
    [("5V", "pwr")],
    [("GND", "gnd")],
    [("3V3", "pwr")],
]

right_header = [
    [("5V", "pwr")],
    [("GND", "gnd")],
    [("3V3", "pwr")],
    [("PB10", "unused")],
    [("SERVO", "gpio")],
    [("ADC_TEMP", "gpio", {"body": {"width": 120}})],
    [("AN_IN", "gpio")],
    [("VOLT_MON1", "gpio", {"body": {"width": 120}})],
    [("VOLT_MON2", "gpio", {"body": {"width": 120}})],
    [("VOLT_MON3", "gpio", {"body": {"width": 120}})],
    [("CURR_PH2", "analog", {"body": {"width": 100}})],
    [("CURR_PH1", "analog", {"body": {"width": 100}})],
    [("CURR_PH3", "analog", {"body": {"width": 100}})],
    [("PC14", "unused")],
    [("PC13", "unused")],
    [("NRST", "gpio")],
    [("Hall_3", "gpio")],
    [("Hall_2", "gpio")],
    [("Hall_1", "gpio")],
    [("V_BAT", "gpio")],
]

swd_header = [
    [
        ("NRST", "gpio"),
    ],
    [
        ("PA14", "gpio"),
        ("SWCLK", "comms"),
    ],
    [
        ("GND", "gnd"),
    ],
    [
        ("PA14", "gpio"),
        ("SWDIO", "comms"),
    ],
    [
        ("VCC", "pwr"),
    ],
]

