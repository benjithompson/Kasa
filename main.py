import os
import asyncio
from kasa import SmartBulb

KASA_DEVICE_IP = os.environ['KASA_DEVICE_IP']
KASA_HUE_SPEED = os.environ['KASA_HUE_SPEED']
async def main():
    bulb = SmartBulb(KASA_DEVICE_IP)
    await bulb.update()
    print(bulb.alias)
    hue = 0
    while(True):
        await bulb.set_hsv(hue, 100, 100)
        hue = (hue + KASA_HUE_SPEED) % 360


if __name__ == "__main__":
    asyncio.run(main())