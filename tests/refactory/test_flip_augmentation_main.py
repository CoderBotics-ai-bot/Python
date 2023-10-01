import shutil

import cv2
import tempfile
import os
import numpy as np
import glob
import pytest
from typing import List, Tuple
from computer_vision.flip_augmentation import *


@pytest.fixture
def generate_sample_files():
    with tempfile.TemporaryDirectory() as tempdir:
        # create sample images and annotation files
        for i in range(10):
            img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
            cv2.imwrite(f"{tempdir}/img_{i}.jpg", img)

            with open(f"{tempdir}/anno_{i}.txt", "w") as f:
                f.write(f"1 0.5 0.5 1 1\n")

        # yield directory path
        yield tempdir

        # cleanup
        files = glob.glob(f"{tempdir}/*")
        for f in files:
            os.remove(f)


# insert the existing functions here


def test_main_no_errors(generate_sample_files: str):
    # patch the constants with the temp directory
    IMAGE_DIR = LABEL_DIR = OUTPUT_DIR = generate_sample_files
    FLIP_TYPE = 1
    try:
        main()
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {e}")


def test_main_files_created(generate_sample_files: str):
    # patch the constants with the temp directory
    IMAGE_DIR = LABEL_DIR = OUTPUT_DIR = generate_sample_files
    FLIP_TYPE = 1
    main()
    files = os.listdir(OUTPUT_DIR)
    assert len(files) == 20, "Image and annotation files are not created as expected"


# more tests here
