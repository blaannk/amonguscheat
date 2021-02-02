import pymem, time, threading, keyboard, mouse
import pymem.process

pm = pymem.Pymem("Phasmophobia.exe")
module = pymem.process.module_from_name(pm.process_handle, "GameAssembly.dll").lpBaseOfDll

def localplayeraddr():
    A_ptr = module + 0x0282C098
    A = pm.read_longlong(A_ptr)
    B_ptr = A + 0x40
    B = pm.read_longlong(B_ptr)
    C_ptr = B + 0x420
    C = pm.read_longlong(C_ptr)
    D_ptr = C + 0x2A0
    D = pm.read_longlong(D_ptr)
    LocalPlayer_ptr = D + 0x90
    return LocalPlayer_ptr

money_offset = 0x18
money_ptr = localplayeraddr() + money_offset
money_value = pm.read_int(money_ptr)
print(money_value)
