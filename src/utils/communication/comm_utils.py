from typing import Any, Dict, List, TYPE_CHECKING
from enum import Enum
from utils.communication.grpc.main import GRPCCommunication
from utils.communication.mpi import MPICommUtils
import numpy as np
import subprocess
import sys
import platform
import shutil

if TYPE_CHECKING:
    from algos.base_class import BaseNode

def installMPI():
    system_name = platform.system()
    if system_name == "Linux":
        try:
            subprocess.check_call(["sudo", "apt", "update"])
            subprocess.check_call(["sudo", "apt", "install", "-y", "libopenmpi-dev", "openmpi-bin"])
            
            # Install additional libraries
            subprocess.check_call(["sudo", "apt-get", "install", "-y", "libgl1", "libglib2.0-0"])
        except subprocess.CalledProcessError as e:
            print(f"Error during installation on Linux: {e}")
    elif system_name == "Darwin":
        try:
            # Check if brew is installed
            if shutil.which("brew") is None:
                raise EnvironmentError("Homebrew is not installed. Please install Homebrew and try again.")   
            subprocess.check_call(["brew", "install", "openmpi"])
        except EnvironmentError as e:
            print(e)
        except subprocess.CalledProcessError as e:
            print(f"Error during installation on macOS: {e}")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", mpi4py]) #type: ignore
    except Exception as e:
        print(f"Exception when installing mpi4py: {e}")

class CommunicationType(Enum):
    MPI = 1
    GRPC = 2
    HTTP = 3

class CommunicationFactory:
    @staticmethod
    def create_communication(
        config: Dict[str, Any], comm_type: CommunicationType
    ):
        comm_type = comm_type
        if comm_type == CommunicationType.MPI:
            return MPICommUtils(config)
        elif comm_type == CommunicationType.GRPC:
            return GRPCCommunication(config)
        elif comm_type == CommunicationType.HTTP:
            raise NotImplementedError("HTTP communication not yet implemented")
        else:
            raise ValueError("Invalid communication type", comm_type)


class CommunicationManager:
    def __init__(self, config: Dict[str, Any]):
        self.comm_type = CommunicationType[config["comm"]["type"]]
        self.comm = CommunicationFactory.create_communication(config, self.comm_type)
        self.comm.initialize()

    def register_node(self, obj: "BaseNode"):
        self.comm.register_self(obj)

    def get_rank(self) -> int:
        if self.comm_type == CommunicationType.MPI:
            if self.comm.rank is None:
                raise ValueError("Rank not set for MPI")
            return self.comm.rank
        elif self.comm_type == CommunicationType.GRPC:
            if self.comm.rank is None:
                raise ValueError("Rank not set for gRPC")
            return self.comm.rank
        else:
            raise NotImplementedError(
                "Rank not implemented for communication type", self.comm_type
            )

    def send(self, dest: str | int | List[str | int], data: Any, tag: int = 0):
        if isinstance(dest, list):
            for d in dest:
                self.comm.send(dest=int(d), data=data)
        else:
            print(f"Sending data to {dest}")
            self.comm.send(dest=int(dest), data=data)
    
    def receive(self, node_ids: List[int]) -> Any:
        """
        Receive data from the specified node
        Returns a list if multiple node_ids are provided, else just returns the data
        """
        return self.comm.receive(node_ids)

    def broadcast(self, data: Any, tag: int = 0):
        self.comm.broadcast(data)

    def send_quorum(self):
        self.comm.send_quorum()

    def all_gather(self, tag: int = 0):
        return self.comm.all_gather()

    def finalize(self):
        self.comm.finalize()

    def set_is_working(self, is_working: bool):
        self.comm.set_is_working(is_working)

    def get_comm_cost(self):
        return self.comm.get_comm_cost()

    def receive_pushed(self):
        return self.comm.receive_pushed()

    def all_gather_pushed(self):
        return self.comm.all_gather_pushed()