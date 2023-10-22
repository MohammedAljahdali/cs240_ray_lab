# cs240_ray_lab
To install the dependencies, run the following command in the terminal:
```bash
conda create -n <env_name> python=3.9 jupyterlab 
```
Then activate the env and start the notebook:
```bash
conda activate <env_name>
jupyter lab
```

Note that you might need to change the python version match the one
on your deployed cluster.

There is a toy script you can use to test the cluster.
Make sure the env is activated before running the script.
```bash
python toy_ray_job.py
```

To setup a cluster of your own, you can use the following command:
```bash
ray up -y config.yaml
```
To shutdown the cluster, run the following command:
```bash
ray down -y config.yaml
```

Make sure you have your AWS credentials setup in your environment.