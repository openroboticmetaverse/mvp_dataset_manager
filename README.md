
<p align="center">
  <a href="https://www.openroboticmetaverse.org">
    <img alt="orom" src="https://raw.githubusercontent.com/openroboverse/knowledge-base/main/docs/assets/icon.png" width="100" />
  </a>
</p>
<h1 align="center">
  🤖 open robotic metaverse mvp - Dataset Manager 🌐
</h1>

## Overview 🔍

This project serves as the MVP (Minimum Viable Product) 🚀 for generating and maintaining datasets used for training robotic models in openroboticmetaverse.

## Technology Stack 🛠️

- **Simulation**: Developed using the Mujoco physics engine


## Setup ⚙️

1. Clone the repo:
```bash
git clone https://github.com/openroboticmetaverse/mvp_mujoco_simulation.git
```

2. Run container:
```bash
cd mvp_mujoco_simulation
```
```bash
docker compose up -d
```

3. Start the Simulation and Save the Dataset:

```bash
cd ../
```
```bash
git clone https://github.com/openroboticmetaverse/mvp_dataset_manager.git
```
```bash
cd mvp_dataset_manager
```

4. Install the following python libraries in a new python virtual environment:
    - h5py
    - numpy

5. Run the following script to run the simulation and save the results in HDF5 format:
```bash
python3 src/data_saver.py
```

After a short time the script stops, now you should see the message "Data streaming completed!" in the console. The HDF5 dataset for the current training episode will be saved to the current working directory.

## HDF5 file structure

```
.
├── Images             
|   ├── cam_high       # Image (stationary camera)
|   └── cam_low        # Image (moving camera)
├── qpos               # Joint positions
└── qvel               # Joint velocities

```

#### Note: The script only captures the joint position data. Image and velocity data will be added in a future update