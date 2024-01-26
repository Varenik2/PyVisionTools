import struct
import zlib
from urllib import request
from array import array
from io import BytesIO

def open_image_from_url(url):
    response = request.urlopen(url)
    image_data = array('B', response.read())
    return image_data

def decompress_png(data):
    if data[:8] == array('B', [137, 80, 78, 71, 13, 10, 26, 10]):
        chunks = []
        pos = 8

        while pos < len(data):
            length = struct.unpack('>I', data[pos:pos + 4].tobytes())[0]
            pos += 4
            chunk_type = data[pos:pos + 4].tobytes()
            pos += 4
            chunk_data = data[pos:pos + length].tobytes()
            pos += length
            crc = data[pos:pos + 4].tobytes()
            pos += 4

            check_crc = zlib.crc32(chunk_type + chunk_data) & 0xffffffff
            if check_crc != struct.unpack('>I', crc)[0]:
                raise ValueError("CRC check failed for PNG chunk")

            chunks.append((chunk_type, chunk_data))

            if chunk_type == b'IEND':
                break

        reconstructed_data = b''.join([b''.join([struct.pack('>I', len(chunk_data)), chunk_type, chunk_data, crc])
                                      for chunk_type, chunk_data in chunks])

        return array('B', reconstructed_data), chunks

    return data, []

def resize_image(input_data, output_path, new_size, chunks):
    old_width, old_height = new_size

    input_data, _ = decompress_png(input_data)

    new_data = bytearray()

    for i in range(old_height):
        for j in range(old_width):
            x = j * (old_width - 1) / old_width
            y = i * (old_height - 1) / old_height

            x0, y0 = int(x), int(y)
            x1, y1 = min(x0 + 1, old_width - 1), min(y0 + 1, old_height - 1)

            if 0 <= x0 < old_width and 0 <= y0 < old_height and 0 <= x1 < old_width and 0 <= y1 < old_height:
                for c in range(4):
                    try:
                        value = (
                        (x1 - x) * (y1 - y) * input_data[(y0 * old_width + x0) * 4 + c] +
                        (x1 - x) * (y - y0) * input_data[(y1 * old_width + x0) * 4 + c] +
                        (x - x0) * (y1 - y) * input_data[(y0 * old_width + x1) * 4 + c] +
                        (x - x0) * (y - y0) * input_data[(y1 * old_width + x1) * 4 + c]
                        )
                        new_data.append(round(value))
                    except IndexError:
                        pass

    with BytesIO() as buffer:
        buffer.write(b'\x89PNG\r\n\x1a\n')
        for chunk_type, chunk_data in chunks:
            buffer.write(struct.pack('>I', len(chunk_data)))
            buffer.write(chunk_type)
            buffer.write(chunk_data)
            crc = zlib.crc32(chunk_type + chunk_data) & 0xffffffff
            buffer.write(struct.pack('>I', crc))

        with open(output_path, 'wb') as file:
            file.write(buffer.getvalue())
