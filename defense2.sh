#!/bin/sh

attack=$1
defense=$2
dataset=$3
device=$4
epoch=$5
batch_size=128
cur_dir=$PWD

if [ "$defense" = 'neural_cleanse' ]
then
  cd model/defenses/neural_cleanse
  python -u neural_cleanse.py --dataset $dataset --attack $attack --attack_mode all2one --data_root "${cur_dir}/datasets/" --checkpoints "${cur_dir}/checkpoints/${attack}/" --result "${cur_dir}/checkpoints/${attack}/${dataset}/defense/${defense}" --device $device --bs $batch_size --epoch $epoch
  cd $cur_dir
elif [ "$defense" = 'STRIP' ]
then
  cd model/defenses/STRIP
  python -u STRIP.py --dataset $dataset --attack $attack --attack_mode all2one --data_root "${cur_dir}/datasets/" --checkpoints "${cur_dir}/checkpoints/${attack}/" --result "${cur_dir}/checkpoints/${attack}/${dataset}/defense/${defense}" --device $device
  cd $cur_dir
elif [ "$defense" = 'fine_pruning' ]
then
  cd model/defenses/fine_pruning
  python -u fine-pruning.py --dataset $dataset --attack $attack --attack_mode all2one --data_root "${cur_dir}/datasets/" --checkpoints "${cur_dir}/checkpoints/${attack}/" --results "${cur_dir}/checkpoints/${attack}/${dataset}/defense/${defense}" --device $device
  cd $cur_dir
elif [ "$defense" = 'CLP' ]
then
  cd model/defenses/CLP
  python -u clp.py --dataset $dataset --attack $attack --attack_mode all2one --data_root "${cur_dir}/datasets/" --checkpoints "${cur_dir}/checkpoints/${attack}/" --results "${cur_dir}/checkpoints/${attack}/${dataset}/defense/${defense}" --device $device
  cd $cur_dir
fi