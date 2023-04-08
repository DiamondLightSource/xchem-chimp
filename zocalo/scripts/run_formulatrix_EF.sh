#!/usr/bin/env bash
export ZOCALO_CONFIG="/dls_sw/apps/zocalo/live/configuration.yaml"
SCRIPT_DIR=/dls_sw/i02-2/software/uploader/zocalo_version/dlsformulatrix.uploader/
SCRIPT_COMMAND="python ${SCRIPT_DIR}formulatrix_uploader.py -c ${SCRIPT_DIR}config_ef.json -d /dls_sw/dasc/mariadb/credentials/ispyb_fmlx_uploader.cfg -f $1"
echo $SCRIPT_COMMAND
$SCRIPT_COMMAND
