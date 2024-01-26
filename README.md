# PyVisionTools

PyVisionTools is a Python library for image processing, offering convenient tools to enhance your vision-related projects.

## Installation

You can install PyVisionTools using pip:

```bash
pip install PyVisionTools
```

## Features

### image_processor
- **Resize image**: Easily resize images with 'resize_image' method

```python
import PyVisionTools

image_url = "http://example.com/your_cool_image.png"
output_image_path = "resized_image.png"
new_size = (69, 69)

image_data = PyVisionTools.ImageProcessor.open_image_from_url(image_url)
image_data, chunks = PyVisionTools.ImageProcessor.decompress_png(image_data)
PyVisionTools.ImageProcessor.resize_image(image_data, output_image_path, new_size, chunks)

```

## License

This project is licensed under the MIT License
