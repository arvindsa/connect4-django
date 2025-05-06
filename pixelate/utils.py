import requests
from PIL import Image
from io import BytesIO


def pixelate_image_inline(url, n=7):
    # 1. Download the image
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("RGB")

    # 2. Crop to square
    width, height = img.size
    side = min(width, height)
    left = (width - side) // 2
    top = (height - side) // 2
    img = img.crop((left, top, left + side, top + side))

    # 3. Resize to n x n for pixelation
    small = img.resize((n, n), Image.Resampling.BILINEAR)

    # 4. Extract RGB data
    pixels = list(small.getdata())
    pixel_array = [list(pixels[i * n : (i + 1) * n]) for i in range(n)]

    # 5. Prepare JSON data
    json_data = {"format": "image", "data": pixel_array}

    # 6. Generate HTML string
    div_size = 30  # size of each pixel block
    html_snippet = f"<div style='width: {div_size * n}px;'>"
    for row in pixel_array:
        for r, g, b in row:
            color = f"rgb({r},{g},{b})"
            html_snippet += f"<div style='width:{div_size}px; height:{div_size}px; float:left; background:{color};'></div>"
        html_snippet += "<div style='clear:both;'></div>"
    html_snippet += "</div>"

    return html_snippet, json_data
