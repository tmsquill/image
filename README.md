# Image

Convenient image pre-processing for DSLR & Mirrorless cameras. Digital cameras typically write images in JPEG & RAW formats. Interacting with high-megapixel images (especially in RAW format) on older hardware can be a frustrating experience.

The `image` tool provides dead-simple reviewing, selecting, and organizing capabilities that run smoothly on older hardware.

## How It Works

At a high level, `image` takes one argument; a path to a directory containing __JPEG & RAW__ images. The tool will load __JPEG__ images one-by-one and display them using OpenCV. 

![Imgur](https://i.imgur.com/uBNRBRI.png)

One of the following actions can be taken for each image:

- `Keep an Image` by pressing the `k` key. This _discards_ the __JPEG__ version of the image but _keeps_ the __RAW__ version.
- `Discard an Image` by pressing the `d` key. This _discards_ both the __JPEG & RAW__ versions of the images.

### Facial Detection

An optional `--facial-detection` flag can be passed to `image` to detect faces. Images containing faces that are kept are stored inside a sub-directory.

## Commands

```bash
❯ python image.py --help
Usage: image.py [OPTIONS] DIRECTORY

  Convenient image pre-processing for DSLR & Mirrorless cameras.

Options:
  --facial-detection / --no-facial-detection
  --help                          Show this message and exit.
```