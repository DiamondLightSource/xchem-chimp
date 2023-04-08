import pytest

import tests.conftest as cfg
from xchem_chimp.detector.chimp_detector import ChimpDetector
from xchem_chimp.detector.coord_generator import ChimpXtalCoordGenerator  # type: ignore
from xchem_chimp.detector.coord_generator import PointsMode  # type: ignore


@pytest.fixture
def echo_xtal_coord_generator(echo_detector):
    return ChimpXtalCoordGenerator(echo_detector, extract_echo=True)


class TestBasicFunctions:
    def test_coord_generator_has_detector(self, echo_xtal_coord_generator):
        assert isinstance(echo_xtal_coord_generator.detector, ChimpDetector)

    def test_echo_coord_generator_has_detector(self, echo_xtal_coord_generator):
        assert isinstance(echo_xtal_coord_generator.detector, ChimpDetector)


class TestXtalCoordinateExtraction:
    def test_extract_coordinates_output_data_out(self, echo_xtal_coord_generator):
        assert len(echo_xtal_coord_generator.combined_coords_list) == 0
        echo_xtal_coord_generator.extract_coordinates()
        assert (
            len(echo_xtal_coord_generator.combined_coords_list) == cfg.NUM_REAL_IMS
        )  # one dict per image

    def test_extract_coordinates_output_data_out_grid(self, echo_xtal_coord_generator):
        echo_xtal_coord_generator.points_mode = PointsMode.REGULAR
        assert len(echo_xtal_coord_generator.combined_coords_list) == 0
        echo_xtal_coord_generator.extract_coordinates()
        assert (
            len(echo_xtal_coord_generator.combined_coords_list) == cfg.NUM_REAL_IMS
        )  # one dict per image

    def test_extract_coordinates_output_data_out_single(
        self, echo_xtal_coord_generator
    ):
        echo_xtal_coord_generator.points_mode = PointsMode.SINGLE
        assert len(echo_xtal_coord_generator.combined_coords_list) == 0
        echo_xtal_coord_generator.extract_coordinates()
        assert (
            len(echo_xtal_coord_generator.combined_coords_list) == cfg.NUM_REAL_IMS
        )  # one dict per image


class TestEchoCoordinateExtraction:
    def test_extract_coordinates_output_data_out(self, echo_xtal_coord_generator):
        assert len(echo_xtal_coord_generator.combined_coords_list) == 0
        echo_xtal_coord_generator.extract_coordinates()
        assert (
            len(echo_xtal_coord_generator.combined_coords_list) == cfg.NUM_REAL_IMS
        )  # one dict per image

    def test_extract_coordinates_output_data_out_grid(self, echo_xtal_coord_generator):
        echo_xtal_coord_generator.points_mode = PointsMode.REGULAR
        assert len(echo_xtal_coord_generator.combined_coords_list) == 0
        echo_xtal_coord_generator.extract_coordinates()
        assert (
            len(echo_xtal_coord_generator.combined_coords_list) == cfg.NUM_REAL_IMS
        )  # one dict per image

    def test_extract_coordinates_output_data_out_single(
        self, echo_xtal_coord_generator
    ):
        echo_xtal_coord_generator.points_mode = PointsMode.SINGLE
        assert len(echo_xtal_coord_generator.combined_coords_list) == 0
        echo_xtal_coord_generator.extract_coordinates()
        assert (
            len(echo_xtal_coord_generator.combined_coords_list) == cfg.NUM_REAL_IMS
        )  # one dict per image

    def test_extract_coordinates_output_data_echo_point(
        self, echo_xtal_coord_generator
    ):
        echo_xtal_coord_generator.points_mode = PointsMode.SINGLE
        assert len(echo_xtal_coord_generator.combined_coords_list) == 0
        echo_xtal_coord_generator.extract_coordinates()
        first_dict = echo_xtal_coord_generator.combined_coords_list[0]
        assert len(first_dict["echo_coordinate"]) == 1

    class TestCalculateWellCentres:
        def test_well_centres_output(self, echo_xtal_coord_generator):
            echo_xtal_coord_generator.extract_coordinates()
            echo_xtal_coord_generator.calculate_well_centres()
            first_dict = echo_xtal_coord_generator.combined_coords_list[0]
            assert len(first_dict["echo_coordinate"]) == 1
            assert first_dict["well_centroid"] is not None


class TestOutputsToDisk:
    def test_coordinates_csv(self, echo_xtal_coord_generator, empty_dir):
        echo_xtal_coord_generator.extract_coordinates()
        csv_path = empty_dir / "testpos_out.csv"
        echo_xtal_coord_generator.save_output_csv(csv_path)
        assert csv_path.is_file()
        with open(csv_path) as f:
            count = sum(1 for _ in f)
        assert count == cfg.NUM_REAL_IMS + 1

    def test_output_images(self, echo_xtal_coord_generator, empty_dir):
        echo_xtal_coord_generator.extract_coordinates()
        echo_xtal_coord_generator.save_preview_images(empty_dir)
        assert len(list(empty_dir.glob("*.png"))) == cfg.NUM_REAL_IMS
