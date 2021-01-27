import pymem, pymem.process

pm = pymem.Pymem("Among Us.exe")
module = pymem.process.module_from_name(pm.process_handle, "GameAssembly.dll").lpBaseOfDll

def speedhack(speedvalue):
    try:
        A_ptr = module + 0x01C57F7C
        A = pm.read_int(A_ptr)
        B_ptr = A + 0x5C
        B = pm.read_int(B_ptr)
        C_ptr = B + 0x4
        C = pm.read_int(C_ptr)
        speed_ptr = C + 0x14
        # READ
        speed = pm.read_float(speed_ptr)
        # WRITE
        pm.write_float(speed_ptr, float(speedvalue))
    except Exception as e:
        print("SpeedHack Error :", str(e))
