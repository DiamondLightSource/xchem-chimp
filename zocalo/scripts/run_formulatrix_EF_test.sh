#!/usr/bin/env bash
module --silent load python/3
conda activate /dls_sw/apps/chimp/conda_env
SCRIPT_DIR=/dls_sw/i02-2/software/uploader/zocalo_version/dlsformulatrix.uploader/
SCRIPT_COMMAND="python ${SCRIPT_DIR}formulatrix_uploader.py -c ${SCRIPT_DIR}config_ef_test.json -d ${SCRIPT_DIR}ispyb_fmlx_uploader_test.cfg -f $1"
echo $SCRIPT_COMMAND
$SCRIPT_COMMAND
