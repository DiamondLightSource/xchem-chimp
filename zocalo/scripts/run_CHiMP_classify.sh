#!/usr/bin/env bash
module --silent load python/3
conda activate /dls_sw/apps/chimp/conda_env
SCRIPT_DIR=/dls_sw/apps/chimp/master/chimp/
SCRIPT_COMMAND="python ${SCRIPT_DIR}classify_list_file_to_ispyb.py --MODEL_PATH=${SCRIPT_DIR}classifier/model/200504_CHiMP_512_5Xfzn_6Xufzn_OS_Callback.pkl --LIST_FILE_PATH=$1 --ISPYB_CONFIG=/dls_sw/dasc/mariadb/credentials/ispyb_fmlx_uploader.cfg"
echo "Running the following command:"
echo $SCRIPT_COMMAND
$SCRIPT_COMMAND
