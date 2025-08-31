# GW170817-Chaos-Analysis Project

## Overview

The **GW170817-Chaos-Analysis** project focuses on setting up methods to analyse signals, in this case specifically gravitational wave signals, in order to identify whether or not the signals are chaotic. While the project can be repeated with other signal detections, here it has focused on the data from the **GW170817** gravitational wave event observed by LIGO, the first detection of a collision between two neutron stars. Two body problems of this sort can often be expected to be well-understood, and indeed the signal does not appear to be chaotic. In future these methods can be repeated, to investigate possible cases of chaos in gravitational wave detections or, with some adjustments, other kinds of signals. 

This repository contains the necessary code, data download scripts, and instructions to allow for the analysis and visualization of the raw data. It is designed to facilitate the study of the intersection between gravitational wave astronomy, and more broadly astronomy, and chaos theory.

---

## Project Structure

- **`src/`** : This folder contains Python scripts for processing, analysing, and visualizing the data. Key analysis tools, including preprocessing, feature extraction, and plotting utilities, are found here.
  
- **`data/`** : The data folder holds the relevant data files for analysis. Due to their large size, the raw `.hdf5` files from LIGO are not included in this repository. However, instructions and scripts are provided for downloading the required data.

- **`notebooks/`** : Jupyter notebooks for performing exploratory data analysis, visualizing results, and running specific analysis workflows interactively. These notebooks are a great starting point for anyone new to the project.

- **`README.md`** : This file, providing an overview of the project, instructions for usage, and necessary context for anyone wishing to collaborate.

---

## How to Use the Repository

### Step 1: Clone the Repository

To get started, you can clone this repository to your local machine:

git clone https://github.com/yourusername/GW170817-Chaos-Analysis.git


Replace `yourusername` with your actual GitHub username.

### Step 2: Download the Data

Since the raw data files are large, they are not included in the repository. You can download them using the provided script or manually from the LIGO website.

- **Automatically Download the Data**:
    - Navigate to the `src/` folder and run the following script:

    ```
    python3 src/download.py
    ```

    - This will automatically download the necessary `.hdf5` strain data files from the LIGO Open Science Center (LOSC) and save them in the `data/` folder.

- **Manual Download**:
    - Alternatively, you can manually download the data from the [LIGO LOSC](https://losc.ligo.org/events/GW170817/). Instructions are also available in the `data/README.md` file.

### Step 3: Set Up Your Python Environment

Ensure you have Python 3.x installed. You will also need to install some dependencies. You can install them by running:

pip install -r requirements.txt


If the `requirements.txt` file isn't present, you can manually install the necessary libraries like `numpy`, `scipy`, `matplotlib`, and others as required.

### Step 4: Run the Code

After downloading the data and setting up your environment, you can run the Python scripts found in the `src/` folder to analyse the data. For interactive analysis, use the notebooks in the `notebooks/` folder.

### Step 5: Explore the Notebooks

The notebooks in `notebooks/` folder allow for interactive data exploration. These are useful for visualizing the data and conducting specific analyses like signal detection or feature extraction. Run the notebooks in a Jupyter environment to get started.

---

## Requirements

- **Python 3.x**: The code is compatible with Python 3.
- **Required Libraries**: The project requires several Python libraries for data processing and analysis. Install them using:

    ```
    pip install -r requirements.txt
    ```

    If `requirements.txt` is not available, here’s a list of libraries you might need:
    - `numpy`
    - `scipy`
    - `matplotlib`
    - `pandas`
    - `h5py` (for handling `.hdf5` files)
    - `seaborn`
    - `sklearn`

---

## License

This project is licenced under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- The data used in this project comes from the **LIGO Open Science Center (LOSC)**.
- The **GW170817** event was a landmark discovery in gravitational wave astronomy. You can read more about it in the official [LIGO publication](https://www.ligo.org/detecting-gravitational-waves/).
