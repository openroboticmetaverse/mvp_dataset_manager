import asyncio
import websockets
import h5py
import numpy as np
from functools import wraps
from time import time
import json

episode_id = 0
# Define the HDF5 file and dataset structure
file_name = f"episode_{episode_id}.hdf5"
num_samples = 600  # Total number of timesteps in the stream


# Function to create the HDF5 file with preallocated datasets
def create_hdf5_file():
    with h5py.File(file_name, "w") as hdf_file:
        # Create a group for images
        images_group = hdf_file.create_group("images")
        
        # Preallocate datasets with full size
        images_group.create_dataset(
            "cam_high", 
            shape=(num_samples, 480, 640, 3), 
            dtype="uint8"
        )
        images_group.create_dataset(
            "cam_low", 
            shape=(num_samples, 480, 640, 3), 
            dtype="uint8"
        )
        
        # Preallocate qpos and qvel datasets
        hdf_file.create_dataset(
            "qpos", 
            shape=(num_samples, 7), 
            dtype="float64"
        )
        hdf_file.create_dataset(
            "qvel", 
            shape=(num_samples, 14), 
            dtype="float64"
        )
    print("HDF5 file created with preallocated datasets.")

# Function to update one row of data in the HDF5 file
def update_data(timestep, cam_high, cam_low, qpos, qvel):
    with h5py.File(file_name, "a") as hdf_file:
        # Update the specific row in each dataset
        #hdf_file["images/cam_high"][timestep] = cam_high
        #hdf_file["images/cam_low"][timestep] = cam_low
        hdf_file["qpos"][timestep] = qpos
        #hdf_file["qvel"][timestep] = qvel



async def listen():
    url = "ws://127.0.0.1:8081"
        # Connect to the server
    async with websockets.connect(url) as ws:
        # Send a greeting message
        await ws.send("Hello Server!")
        i = 1
        while True:
            #print(f"iteration: {i}")
            msg = await ws.recv()
            msg = json.loads(msg)
            qpos = [float(i) for i in msg[list(msg.keys())[0]].values()]
            update_data(timestep=i-1, cam_high=None, cam_low=None, qpos=qpos, qvel=None)
            
            if i < num_samples:
                i += 1
            else:
                #print("Stop Test Client")
                break

if __name__ == "__main__":
    # asyncio.get_event_loop().run_until_complete(listen())
    # Create the HDF5 files
    create_hdf5_file()
    asyncio.run(listen())
    print("Data streaming completed!")

        
        
