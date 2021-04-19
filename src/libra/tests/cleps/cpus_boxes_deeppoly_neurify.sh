#!/usr/bin/env bash
##########################################
# experiment C: different number of CPUs #
##########################################



#========================#
# boxes+deeppoly+neurify #
#========================#

$LIBRA $LIBRA_REPO/census.txt $LIBRA_REPO/20.py --domain boxes_deeppoly_neurify --lower 0.015625 --upper 6 --cpu 64 | tee $1/census-20-boxes_deeppoly_neurify-64cpu.log
$LIBRA $LIBRA_REPO/census.txt $LIBRA_REPO/20.py --domain boxes_deeppoly_neurify --lower 0.015625 --upper 6 --cpu 32 | tee $1/census-20-boxes_deeppoly_neurify-32cpu.log
$LIBRA $LIBRA_REPO/census.txt $LIBRA_REPO/20.py --domain boxes_deeppoly_neurify --lower 0.015625 --upper 6 --cpu 16 | tee $1/census-20-boxes_deeppoly_neurify-16cpu.log
$LIBRA $LIBRA_REPO/census.txt $LIBRA_REPO/20.py --domain boxes_deeppoly_neurify --lower 0.015625 --upper 6 --cpu 8 | tee $1/census-20-boxes_deeppoly_neurify-8cpu.log
$LIBRA $LIBRA_REPO/census.txt $LIBRA_REPO/20.py --domain boxes_deeppoly_neurify --lower 0.015625 --upper 6 --cpu 4 | tee $1/census-20-boxes_deeppoly_neurify-4cpu.log
