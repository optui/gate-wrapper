# Gate wrapper

A python wrapper for the GATE (v10) software, part of the OpenGATE collaboration. It features a Dear PyGui interface to manage and visualize medical simulations. GATE is built on top of the GEANT4 toolkit and is used for medical imaging simulations such as PET, SPECT, CT, and radiotherapy.

## Table of Contents

- [Gate Wrapper](#gate-wrapper)
- [Sources](#sources)
- [Build Environment](#build-environment)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [Documentation](#documentation)
  - [Main Functionalities](#main-functionalities)
    - [Simulation Manager](#simulation-manager)
    - [Simulation Control](#simulation-control)
    - [Volume Manager](#volume-manager)
    - [Sources Manager](#sources-manager)
    - [Material Manager](#material-manager)
    - [Detector Manager](#detector-manager)
- [Milestones](#milestones)

## Sources

- [OpenGATE collaboration](http://www.opengatecollaboration.org/)
- [GATE v10 Documentation](https://opengate-python.readthedocs.io/en/latest/user_guide.html)
- [Geant4 Documentation](https://geant4.web.cern.ch/docs/)
- [Dear PyGui Documentation](https://dearpygui.readthedocs.io/en/latest/index.html)

## Build Environment

The following specifications were used during development and testing:

- **OS**: Pop!_OS 22.04 LTS (based on Ubuntu)
- **Processor**: AMD Ryzen 5 5600h
- **Graphics**: NVIDIA GeForce RTX 3050 mobile

## Installation

### Prerequisites

- [GATE](https://opengate-python.readthedocs.io/en/latest/index.html)
  - [User Installation Guide](https://opengate-python.readthedocs.io/en/latest/user_guide.html#installation-for-users-not-for-developers)
  - [Developer Installation Guide](https://opengate-python.readthedocs.io/en/latest/developer_guide.html#installation-for-developers)
- [Dear PyGui](https://dearpygui.readthedocs.io/en/latest/tutorials/first-steps.html)

### Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/optui/gate-wrapper.git
    cd gate-wrapper
    ```

2. Run the setup script:
    ```bash
    ./setup.sh
    ```

3. Run:
   ```bash
   ./run.sh
   ```

> Note: If you encounter the error `opengate_core is not detected`, you may need to export the necessary library paths as indicated in the error message.

## Documentation

### Main functionalities

#### Simulation manager

- Set simulation name
- Set simulation verbosity
- Set simulation visualisation
- Set simulation multithreading
- Physics settings
    - Set physics list
    - Set cutoff thresholds
    - Set interactions

#### Simulation control

- Run, pause/resume and stop simulation

#### Volume manager

- Create volume
    - Translate and scale volumes
- Read volumes
- Update volume
- Delete volume

#### Sources manager

- Create source
- Read sources
- Update source
- Delete source

#### Material manager

- Create material
- Read materials
- Update material
- Delete material

#### Detector manager

- Create detector
- Read detector
- Update detector
- Delete detector

## Milestones

### Milestone 1

- From: 2024.09.30.
- To: 2024.10.13.
- Info: scoping

### Milestone 2

- From: 2024.10.14.
- To: 2024.10.27.
- Info: ...

### Milestone 3

- From: 2024.10.28.
- To: 2024.11.10.
- Info: ...

### Milestone 4

- From: 2024.11.11.
- To: 2024.11.24.
- Info: ...

### Milestone 5

- From: 2024.11.25.
- To: 2024.12.08.
- Info: ...

### Milestone 6

- From: 2024.12.09.
- To: 2024.12.22.
- Info: ...

### Milestone 7

- From: 2024.12.23.
- To: 2025.01.06.
- Info: ...

### Milestone 8

- From: 2025.01.07.
- To: 2025.01.20.
- Info: finish