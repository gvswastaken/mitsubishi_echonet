from .eojx import *

class HomeSolarPowerFunctions:
    
    def _027980(edt):
        ops_value = int.from_bytes(edt, 'big')
        return {'status': ('On' if ops_value == 0x30 else 'Off')}

    def _0279e0(edt):
        return {'instantaneous_power': int.from_bytes(edt, 'big')}

    def _0279e1(edt):
        return {'cumul_power': int.from_bytes(edt, 'big')}
