# Datarecod Docker
Base image : argnctu/locobot:NUC-sis
- lcm

## Usage

[1] Build docker image
```bash
$ cd LabelFusion/docker/Datarecord
$ source build.sh
```
 
[2] Enter Label Fusion
```bash
$ cd LabelFusion/docker/Datarecord
$ source docker_run.sh
```
If you want to join container by another terminal.

```bash
$ cd LabelFusion/docker/Datarecord
$ source docker_join.sh
```

[3] Source Source vitial envirment in docker
```bash
$ source pyenv_pyrobot_python3/bin/activate
```