import struct

from PIL import Image
from PIL.PngImagePlugin import PngImageFile
from io import BytesIO
from typing import Union

from .util import executor

@executor
def change_png_color(img: Union[PngImageFile, bytes], from_rgb: Union[tuple, str], to_rgb: Union[tuple, str], delta_rank: int = 10):
    """Change a color from a PNG image

    Parameters
    ==========
        img: Union[PngImageFile, bytes]
            The image to change the color from. This can be
            a premade PNG image from PIL.Image, or raw bytes.
        from_rgb: Union[tuple, str]
            The HEX color code or RGB tuple of the color
            that needs to be replaced with the new color.
        to_rgb: Union[tuple, str]
            The HEX color code or the RGB tuple of the new
            color that needs to replace the color from from_rgb.
        delta_rank: int
            How close colors of a color match with the
            from_rgb color also need to be replaced.

    Returns
    =======
        Image
            The Image with the changed colors.
    """
    if isinstance(from_rgb, str):
        from_rgb = from_rgb.replace('#', '').replace('0x', '')
        from_rgb = struct.unpack('BBB', bytes.fromhex(from_rgb))
    if isinstance(to_rgb, str):
        to_rgb = to_rgb.replace('#', '').replace('0x', '')
        to_rgb = struct.unpack('BBB', bytes.fromhex(to_rgb))

    if isinstance(img, bytes):
        img = Image.open(BytesIO(img))

    img = img.convert("RGBA")
    pixdata = img.load()

    for x in range(0, img.size[0]):
        for y in range(0, img.size[1]):
            rdelta = pixdata[x, y][0] - from_rgb[0]
            gdelta = pixdata[x, y][1] - from_rgb[1]
            bdelta = pixdata[x, y][2] - from_rgb[2]
            if abs(rdelta) <= delta_rank and abs(gdelta) <= delta_rank and abs(bdelta) <= delta_rank:
                pixdata[x, y] = (to_rgb[0] + rdelta, to_rgb[1] + gdelta, to_rgb[2] + bdelta, pixdata[x, y][3])

    return img

@executor
def make_transparent(img: Union[PngImageFile, bytes], color: Union[tuple, str], delta_rank: int = 10):
    """Make a color from a PNG image transparent

    Parameters
    ==========
        img: Union[PngImageFile, bytes]
            The image to change the color from. This can be
            a premade PNG image from PIL.Image, or raw bytes.
        color: Union[tuple, str]
            The HEX color code or RGB tuple of the color
            that needs to be made transparent.
        delta_rank: int
            How close colors of a color match with the
            from_rgb color also need to be changed.

    Returns
    =======
        Image
            The Image with the changed colors.
    """
    if isinstance(color, str):
        color = color.replace('#', '').replace('0x', '')
        color = struct.unpack('BBB', bytes.fromhex(color))

    if isinstance(img, bytes):
        img = Image.open(BytesIO(img))

    datas = img.getdata()

    new_data = []
    for item in datas:
        r = item[0] - color[0]
        g = item[1] - color[1]
        b = item[2] - color[2]
        if abs(r) <= delta_rank and abs(g) <= delta_rank and abs(b) <= delta_rank:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)

    return img