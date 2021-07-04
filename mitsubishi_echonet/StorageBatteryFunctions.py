from .eojx import *

class StorageBatteryFunctions:
    
    def _027d80(edt):
        ops_value = int.from_bytes(edt, 'big')
        return {'status': ('On' if ops_value == 0x30 else 'Off')}

    def _027de4(edt):
        return {'remaining_electricity_3': int.from_bytes(edt, 'big')}

    def _027dcf(edt):
        STATES = {
            0x41: "Rapid charging",
            0x42: "Charging",
            0x43: "Discharging",
            0x44: "Standby",
            0x45: "Test",
            0x46: "Automatic",
            0x48: "Restart",
            0x49: "Effective capacity recalculation processing"
        }

        return {"working_operation_status": STATES[int.from_bytes(edt, 'big')]}
