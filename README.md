# Image

Convenient image pre-processing for DSLR & Mirrorless cameras. Digital cameras typically write images in JPEG & RAW formats. Interacting with high-megapixel images (especially in RAW format) on older hardware can be a frustrating experience.

The `image` tool provides dead-simple reviewing, selecting, and organizing capabilities that run smoothly on older hardware.

## Installation

```bash
pip install -r requirements.txt
```

Optionally install `dlib` to enable facial detection capabilities, see [here](https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/).

## How It Works

At a high level, `image` takes one argument; a path to a directory containing __JPEG & RAW__ images. The tool will load __JPEG__ images one-by-one and display them using OpenCV.

![Imgur](https://i.imgur.com/uBNRBRI.png)

One of the following actions can be taken for each image:

- `Keep an Image` by pressing the `k` key. This _discards_ the __JPEG__ version of the image but _keeps_ the __RAW__ version.
- `Discard an Image` by pressing the `d` key. This _discards_ both the __JPEG & RAW__ versions of the images.

### View Size

An optional `--view-size` flag can be passed to `image` to specify the size to use when resizing images for displaying. This is especially useful for images produced by full-frame and medium format sensors since resulting images are often too large for most monitors.

### Facial Detection

An optional `--facial-detection` flag can be passed to `image` to detect faces. Images containing faces that are kept are stored inside a sub-directory.

### Keeping Options

By default, `image` will discard __JPEG__ files and keep __RAW__ files. This functionality can be tuned with the `--keep-jpeg/--no-keep-jpeg` and `--keep-raw/--no-keep-raw` flags respectively.

## Commands

```
❯ python image.py --help
Usage: image.py [OPTIONS] DIRECTORY

  Convenient image pre-processing for DSLR & Mirrorless cameras.

Options:
  --preview-size INTEGER          Resizes images for displaying (based on
                                  width or height, whichever is larger)
                                  equivalent to the preview size.

  --facial-detection / --no-facial-detection
                                  Enables facial detection, images with faces
                                  are saved to the 'facial_detections' sub-
                                  directory.

  --keep-jpeg / --no-keep-jpeg    Keep JPEG version of images selected by the
                                  user to keep.

  --keep-raw / --no-keep-raw      Keep RAW version of images selected by the
                                  user to keep.

  --help                          Show this message and exit.
```
