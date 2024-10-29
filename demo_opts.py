# -*- coding: utf-8 -*-
# Copyright (c) 2014-2022 Richard Hull and contributors
# See LICENSE.rst for details.

import sys
import logging

from luma.core import cmdline, error
from luma.oled.device import ssd1309
from luma.core.interface.serial import spi

def get_device(actual_args=None):
    serial = spi(bus_speed_hz=1000000)
    device = ssd1309(serial,rotate=0)    
    return device

