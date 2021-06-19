#!/bin/bash
#
# This script is sourced by bash when the docker container starts.
#

echo "sourcing ${BASH_SOURCE[0]}"

export LABELFUSION_SOURCE_DIR=$(cd $(dirname ${BASH_SOURCE[0]})/../.. && pwd)
echo $LABELFUSION_SOURCE_DIR

export DIRECTOR_INSTALL_DIR=/root/install
echo $DIRECTOR_INSTALL_DIR

source ${LABELFUSION_SOURCE_DIR}/setup_environment.sh