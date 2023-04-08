#!/usr/bin/env bash
module --silent load python/3
conda activate /dls_sw/apps/chimp/conda_env
SCRIPT_DIR=/dls_sw/apps/chimp/master/chimp/
SCRIPT_COMMAND="python ${SCRIPT_DIR}detect_list_file_to_ispyb.py --MODEL_PATH=${SCRIPT_DIR}detector/model/210630_xtal_detector_VMXi237_augs_ADAMW_OneCyclLR_20eph_Mask_R_CNN_DICT_NZ.pth --LIST_FILE_PATH=$1 --ISPYB_CONFIG=${SCRIPT_DIR}ispyb_fmlx_uploader.cfg"
echo "Running the following command:"
echo $SCRIPT_COMMAND
$SCRIPT_COMMAND
