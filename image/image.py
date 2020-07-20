import click
import cv2
import imutils
import sys

from imutils import face_utils
from pathlib import Path

@click.command()
@click.argument('directory')
@click.option(
    "--facial-detection/--no-facial-detection",
    default=False,
    help="Enables facial detection, images with faces are saved to the 'facial_detections' sub-directory."
)
@click.option(
    "--keep-jpeg/--no-keep-jpeg",
    default=False,
    help="Keep JPEG version of images selected by the user to keep."
)
@click.option(
    "--keep-raw/--no-keep-raw",
    default=True,
    help="Keep RAW version of images selected by the user to keep."
)
def image(directory, facial_detection, keep_jpeg, keep_raw):

    """Convenient image pre-processing for DSLR & Mirrorless cameras."""

    path = Path(directory)

    if facial_detection:

        try:

            import dlib
            detector = dlib.get_frontal_face_detector()

        except Exception as _:

            click.echo("Facial detection unavailable, please ensure dlib is installed correctly.")
            sys.exit(1)

        (path / 'facial_detections').mkdir()

    if path.exists() and path.is_dir():

        for jpeg in path.glob('*.JPG'):

            raw = Path(f'{jpeg.parent}/{jpeg.stem}.ARW')

            image = cv2.imread(str(jpeg), cv2.IMREAD_COLOR)
            image = imutils.resize(image, width=500)

            if facial_detection:

                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                rects = detector(gray, 1)

                for i, rect in enumerate(rects):

                    # Convert the dlib-style bounding box to an OpenCV-style bounding box.
                    x, y, w, h = face_utils.rect_to_bb(rect)
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    # Show the face number.
                    cv2.putText(image, f"Face #{i + 1}", (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            cv2.imshow(str(jpeg), image)

            val = cv2.waitKey(0)

            if val == ord('k'):

                click.echo(click.style(f'{jpeg.stem} -> Keep', fg='green'))

                if not keep_jpeg:

                    jpeg.unlink()

                if not keep_raw and raw.exists():

                    raw.unlink()

                elif facial_detection and raw.exists() and len(rects) > 0:

                    raw.replace(Path(f'{raw.parent}/facial_detections/{raw.name}'))

            elif val == ord('d'):

                click.echo(click.style(f'{jpeg.stem} -> Discard', fg='red'))

                jpeg.unlink()
                raw.unlink()

            else:

                break

            cv2.destroyAllWindows()

    else:

        click.echo("Please provide a path to a valid directory containing images to pre-process.")

if __name__ == '__main__':

    image()
