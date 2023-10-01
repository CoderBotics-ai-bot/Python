from PIL import Image
from cellular_automata.conways_game_of_life import *
import pytest


import pytest


def test_generate_images_execution(cells, frames):
    result = generate_images(cells, frames)
    assert result is not None


def test_generate_images_return_type(cells, frames):
    result = generate_images(cells, frames)
    assert isinstance(result, list)


def test_generate_images_list_elements(cells, frames):
    result = generate_images(cells, frames)

    for image in result:
        assert isinstance(image, Image.Image)


def test_generate_images_list_length(cells, frames):
    result = generate_images(cells, frames)
    assert len(result) == frames


@pytest.fixture
def cells():
    return [[0, 1, 0], [1, 0, 1], [0, 1, 0]]


@pytest.fixture
def frames():
    return 10
