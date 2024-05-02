from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.memory_usage = 0
        self.capacity_usage = 0

    def install(self, software: Software):
        available_memory = self.memory - self.memory_usage
        available_capacity = self.capacity - self.capacity_usage

        if available_memory < software.memory_consumption or available_capacity < software.capacity_consumption:
            raise Exception('Software cannot be installed')

        self.capacity_usage += software.capacity_consumption
        self.memory_usage += software.memory_consumption

        self.software_components.append(software)

    def uninstall(self, software: Software):
        self.capacity_usage -= software.capacity_consumption
        self.memory_usage -= software.memory_consumption

        self.software_components.remove(software)
