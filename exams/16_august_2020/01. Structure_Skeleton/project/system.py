from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


def find_obj_by_name(obj_name, objects_list):
    for obj in objects_list:
        if obj.name == obj_name:
            return obj


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = find_obj_by_name(hardware_name, System._hardware)

        if not hardware:
            return 'Hardware does not exist'

        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(express_software)
        System._software.append(express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = find_obj_by_name(hardware_name, System._hardware)

        if not hardware:
            return 'Hardware does not exist'

        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(light_software)
        System._software.append(light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = find_obj_by_name(hardware_name, System._hardware)
        software = find_obj_by_name(software_name, System._software)

        if not hardware or not software:
            return 'Some of the components do not exist'

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        return f"System Analysis" +'\n'\
               f"Hardware Components: {len(System._hardware)}" +'\n'\
               f"Software Components: {len(System._software)}" +'\n'\
               f"Total Operational Memory: {sum([x.memory_consumption for x in System._software])} / {sum([x.memory for x in System._hardware])}"+'\n' \
               f"Total Capacity Taken: {sum([x.capacity_consumption for x in System._software])} / {sum([x.capacity for x in System._hardware])}"

    @staticmethod
    def system_split():
        result = []
        for hardware in System._hardware:
            result.append(f"Hardware Component - {hardware.name}")

            express_software = [x for x in hardware.software_components if x.software_type == 'Express']
            light_software = [x for x in hardware.software_components if x.software_type == 'Light']

            software_components = 'None'
            if hardware.software_components:
                software_components = ', '.join(x.name for x in hardware.software_components)

            result.append(f"Express Software Components: {len(express_software)}")
            result.append(f"Light Software Components: {len(light_software)}")
            result.append(f"Memory Usage: {hardware.memory_usage} / {hardware.memory}")
            result.append(f"Capacity Usage: {hardware.capacity_usage} / {hardware.capacity}")
            result.append(f"Type: {hardware.hardware_type}")
            result.append(f"Software Components: {software_components}")

        return '\n'.join(result)

