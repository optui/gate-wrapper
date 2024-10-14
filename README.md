# Gate wrapper

A python wrapper for the GATE (v10) software, part of the OpenGATE collaboration. It features a Dear PyGui interface to manage and visualize medical simulations. GATE is built on top of the GEANT4 toolkit and is used for medical imaging simulations such as PET, SPECT, CT, and radiotherapy.

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

- [GATE v10](https://opengate-python.readthedocs.io/en/latest/user_guide.html#installation-for-users-not-for-developers)
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

## Further reading

- [Issues](https://github.com/optui/gate-wrapper/issues)
- [Milestones](https://github.com/optui/gate-wrapper/milestones)
- [Design documentation](./docs/design.md)