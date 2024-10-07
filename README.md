# Gate wrapper

A python wrapper for the GATE (v10) software, part of the OpenGATE collaboration. It features a Dear PyGui interface to manage and visualize medical simulations. GATE is built on top of the GEANT4 toolkit and is used for medical imaging simulations such as PET, SPECT, CT, and radiotherapy.

## Table of Contents

- [Gate Wrapper](#gate-wrapper)
- [Sources](#sources)
- [Build Environment](#build-environment)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installation Steps](#installation-steps)
- [Functionalities](#functionalities)
  - [Simulation manager](#simulation-manager)
  - [Volume manager](#volume-manager)
  - [Physics manager](#physics-manager)
  - [Sources manager](#sources-manager)
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

## Functionalities

### Simulation manager

- Set simulation name
- Set simulation parameters via `user_info`

### Volume manager

- Create, read, update, delete volumes
- Transformations (translation, scaling)

### Physics manager

### Actor manager

### Sources manager

## Milestones

### Milestone 1

- From: 2024.09.30.
- To: 2024.10.13.
- Info:
  - implement core manager: simulation
  - implement sub-managers: volume, physics, actor and sources

### Milestone 2

- From: 2024.10.14.
- To: 2024.10.27.
- Info:
  - implement a live editor
  - implement volume scaling and transformation via live editor

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
