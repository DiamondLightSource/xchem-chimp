"""Script to detect positions of crystals in a folder of drop images using
Mask-R-CNN based object detector.
"""
import argparse
import logging
import sys
import warnings
from pathlib import Path

import xchem_chimp.base.chimp_utils as utils
from xchem_chimp.base.chimp_errors import InputError
from xchem_chimp.detector.chimp_detector import ChimpDetector
from xchem_chimp.detector.coord_generator import ChimpXtalCoordGenerator, PointsMode
from xchem_chimp.detector.mask_saver import ChimpXtalMaskSaver

warnings.filterwarnings("ignore", category=RuntimeWarning)
warnings.filterwarnings("ignore", category=UserWarning)

LOGGING_FMT = "%(asctime)s - %(levelname)s - %(message)s"
LOGGING_DATE_FMT = "%d-%b-%y %H:%M:%S"

logging.basicConfig(level=logging.INFO, format=LOGGING_FMT, datefmt=LOGGING_DATE_FMT)


def init_argparse() -> argparse.ArgumentParser:
    """Custom argument parser for this program.

    Returns:
        argparse.ArgumentParser: An argument parser with the appropriate
        command line args contained within.
    """
    parser = argparse.ArgumentParser(
        description="CHiMP (Crystal Hits in My Plate) detector"
    )
    parser.add_argument(
        "--MODEL_PATH", required=True, type=str, help="path to model file."
    )
    parser.add_argument(
        "--LIST_FILE_PATH",
        required=True,
        type=str,
        help="path to text file with list of images.",
    )
    parser.add_argument("--num_classes", default=2, type=int)
    parser.add_argument("--mode", default="SINGLE", type=str)
    parser.add_argument("--preview", default=False, action="store_true")
    parser.add_argument("--masks", default=False, action="store_true")
    return parser


parser = init_argparse()
args = vars(parser.parse_args())
LIST_FILE_PATH = Path(args["LIST_FILE_PATH"])
MODEL_PATH = Path(args["MODEL_PATH"])
NUM_CLASSES = args["num_classes"]
MODE = PointsMode[args["mode"]]
PREVIEW_FLAG = args["preview"]
MASKS_FLAG = args["masks"]

try:
    utils.check_image_list_file(LIST_FILE_PATH)
except InputError as e:
    logging.error(e)
    sys.exit(1)

logging.info(f"Reading list of images from {LIST_FILE_PATH}")
with open(LIST_FILE_PATH, "r") as fh:
    image_list = fh.read().splitlines()

print("##### CHiMP (Crystal Hits in My Plate) detector #####")
logging.info("Loading libraries...")

# Run the script
try:
    detector = ChimpDetector(MODEL_PATH, image_list, NUM_CLASSES)
except InputError as e:
    logging.error(e)
    sys.exit(1)
cwd = Path.cwd()
results_dir = cwd / "detector_output"
logging.info(f"Making directory for detector output: {results_dir}")
results_dir.mkdir(exist_ok=True)
if MASKS_FLAG:
    mask_saver = ChimpXtalMaskSaver(detector, results_dir)
    mask_saver.extract_masks()
else:
    coord_generator = ChimpXtalCoordGenerator(detector, points_mode=MODE)
    coord_generator.extract_coordinates()
    coord_generator.save_output_csv(results_dir / "detector_positions.csv")
    if PREVIEW_FLAG:
        logging.info("Output of preview images requested:")
        im_out_dir = results_dir / "preview_images"
        logging.info(f"Making directory for preview image output: {im_out_dir}")
        im_out_dir.mkdir(exist_ok=True)
        coord_generator.save_preview_images(im_out_dir)
