xchem-chimp
=======================================================================


CHiMP (Crystal Hits in My Plate) is a deep learning system to help researchers work with micrographs of protein crystallisation experiments. XChem CHiMP consists of one component:

1. **CHiMP Detector**. This uses an object detection network to find the position of any crystals and drops in the image and uses this information to
calculate a coordinate for dispensing compound using the Echo.


Installation
-----------------------------------------------------------------------
::

    pip install chimpflow

    chimpflow --version


Model file for xchem-chimp
-----------------------------------------------------------------------

The model file is saved in::

    https://gitlab.diamond.ac.uk/xchem/xchem-chimp-models


This file is too large for github.

For GitHub pytest to find the file in its CI/CD Actions, this file has been uploaded to zenodo::

    https://zenodo.org/record/7810708/2022-12-07_CHiMP_Mask_R_CNN_XChem_50eph_VMXi_finetune_DICT_NZ.pytorch

The tests/conftest.py fetches this file automatically.

Running
-----------------------------------------------------------------------
::

    rm -rf detector_output
    python -m detect_folder_chimp \
        --echo --preview \
        --num_classes=3 \
        --MODEL_PATH=src/xchem_chimp/detector/model/2022-12-07_CHiMP_Mask_R_CNN_XChem_50eph_VMXi_finetune_DICT_NZ.pytorch \
        --IMAGE_PATH=tests/SubwellImages/97wo_2021-09-14_RI1000-0276-3drop

you can expect something like::

   20-Mar-23 08:09:21 - INFO - Loading libraries...
   20-Mar-23 08:09:21 - DEBUG - Loading model from src/xchem_chimp/detector/model/2022-12-07_CHiMP_Mask_R_CNN_XChem_50eph_VMXi_finetune_DICT_NZ.pytorch
   20-Mar-23 08:09:21 - INFO - Making directory for detector output: /27/xchem-chimp/detector_output
   20-Mar-23 08:09:21 - DEBUG - extracting coordinates...
   20-Mar-23 08:09:25 - DEBUG - create_detector_output_dict: 97wo_01A_1.jpg - Number of objects found: 33
   20-Mar-23 08:09:25 - DEBUG - 1 drops, 32 crystals over prob threshold
   20-Mar-23 08:09:26 - DEBUG - Extracting Echo coordinate from distance transform.
   20-Mar-23 08:09:27 - DEBUG - Calculating well centroids...
   20-Mar-23 08:09:27 - DEBUG - Loading background images
   20-Mar-23 08:09:27 - DEBUG - Well centroid found at (504, 600)


Development questions
-----------------------------------------------------------------------
- Is the folder src/xchem_chimp/detector/background_images needed in the distribution?
- Where best to put model_file for unit testing?
- Is torchvision a necessary dependency for runtime?
- How are the model files built?
- Why are there so many mypy problems in coord_generator.py and detector_utils.py?
- How significant is this: DeprecationWarning: Please use gaussian_filter from the scipy.ndimage namespace, the scipy.ndimage.filters namespace is deprecated.
- Do we need to keep anything in the zocalo directory?
- Is there some example image where target_position is properly calculated?

Documentation
-----------------------------------------------------------------------

See https://www.cs.diamond.ac.uk/chimpflow for more detailed documentation.

Building and viewing the documents locally::

    git clone git+https://gitlab.diamond.ac.uk/scisoft/bxflow/chimpflow.git 
    cd chimpflow
    virtualenv /scratch/$USER/venv/chimpflow
    source /scratch/$USER/venv/chimpflow/bin/activate 
    pip install -e .[dev]
    make -f .chimpflow/Makefile validate_docs
    browse to file:///scratch/$USER/venvs/chimpflow/build/html/index.html

Topics for further documentation:

- TODO list of improvements
- change log


..
    Anything below this line is used when viewing README.rst and will be replaced
    when included in index.rst

