# Data for GW170817-Chaos-Analysis Project

## Overview

This folder is intended to hold data files used for the analysis of the GW170817 gravitational wave event.

**Note:** Due to file size constraints and data hosting policies, raw data files (e.g., `.hdf5` strain data) are **not included** directly in this repository.

## Data Source

The primary data files are publicly available from the [LIGO Open Science Center (LOSC)](https://losc.ligo.org/events/GW170817/).

For example, one of the main data files used in this project is:

- `H-H1_LOSC_CLN_16_V1-1187007040-2048.hdf5`  
  [Direct download link](https://dcc.ligo-wa.caltech.edu/public/0146/P1700349/001/H-H1_LOSC_CLN_16_V1-1187007040-2048.hdf5)

## How to Obtain the Data

To download the necessary data files, you can use the download script provided in the `src/` folder.

1. Ensure you have an active internet connection.
2. In the project directory, run the following command in your terminal:

   ```bash
   python3 src/download.py
