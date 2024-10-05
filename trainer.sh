#! /bin/bash

#python3 -c 'from predictcrypto.component.cmg import training_manager; training_manager("prophet")'

echo "Starting model training."

python trainer.py

echo "Model training in completed"