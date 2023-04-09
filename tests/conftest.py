import warnings
from pathlib import Path

import pytest
import requests  # type: ignore

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    # Chimp adapter object.
    from xchem_chimp.detector.chimp_detector import ChimpDetector

TEST_IM_FILENAME = "small_crystals_2.jpg"
TEST_IM_FILENAME_2 = "big_crystals_3.jpg"
NUM_REAL_IMS = 2
ECHO_MODEL_FILE_NAME = (
    "2022-12-07_CHiMP_Mask_R_CNN_XChem_50eph_VMXi_finetune_DICT_NZ.pytorch"
)
ECHO_NUM_CLASSES = 3


def del_dir(target):
    """
    Delete a given directory and its subdirectories.

    :param target: The directory to delete
    """
    target = Path(target).expanduser()
    assert target.is_dir()
    for p in sorted(target.glob("**/*"), reverse=True):
        if not p.exists():
            continue
        p.chmod(0o666)
        if p.is_dir():
            p.rmdir()
        else:
            p.unlink()
    target.rmdir()


@pytest.fixture()
def cwd():
    return Path(__file__).parent


@pytest.fixture()
def image_folder_real_ims(cwd):
    return cwd / "test_imgs"


@pytest.fixture()
def image_folder_echo_ims(cwd):
    return cwd / "echo_test_imgs"


@pytest.fixture()
def empty_dir(tmp_path):
    tmp_dir = tmp_path / "empty_dir"
    tmp_dir.mkdir(exist_ok=True)
    yield tmp_dir
    del_dir(tmp_dir)


@pytest.fixture()
def echo_detector_model_path(cwd):
    model_file_path = cwd.parent / ECHO_MODEL_FILE_NAME
    if not model_file_path.exists():

        # The file which has been uploaded to Zenodo.
        file_id = f"7810708/files/{ECHO_MODEL_FILE_NAME}"

        # Set the Zenodo API base URL
        base_url = "https://zenodo.org/record"
        full_url = f"{base_url}/{file_id}?download=1"

        # Download the file from the download URL
        response = requests.get(full_url)

        # Save the file to disk
        with open(model_file_path, "wb") as f:
            f.write(response.content)

    return model_file_path


@pytest.fixture()
def echo_detector(echo_detector_model_path, image_folder_echo_ims):
    return ChimpDetector(
        echo_detector_model_path,
        list(Path(image_folder_echo_ims).glob("*")),
        ECHO_NUM_CLASSES,
    )
