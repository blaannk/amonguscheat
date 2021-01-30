import pymem, pymem.process, time

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

def impostor():
    A_ptr = module + 0x01C57F7C
    A = pm.read_int(A_ptr)
    B_ptr = A + 0x5C
    B = pm.read_int(B_ptr)
    C_ptr = B + 0x0
    C = pm.read_int(C_ptr)
    D_ptr = C + 0x34
    D = pm.read_int(D_ptr)
    forceimpostor_ptr = D + 0x28
    isImpostor = pm.read_int(forceimpostor_ptr)
    if isImpostor == 0:
        pm.write_int(forceimpostor_ptr, 1)
    #elif isImpostor == 1:
        #pm.write_int(forceimpostor_ptr, 0)

def killcooldown(valueasked):
    A_ptr = module + 0x01C57F7C
    A = pm.read_int(A_ptr)
    B_ptr = A + 0x5C
    B = pm.read_int(B_ptr)
    C_ptr = B + 0x4
    C = pm.read_int(C_ptr)
    resetkill_ptr = C + 0x20
    cooldown = pm.read_float(resetkill_ptr)
    pm.write_float(resetkill_ptr, float(valueasked))

def resetkill():
    A_ptr = module + 0x01C57F7C
    A = pm.read_int(A_ptr)
    B_ptr = A + 0x5C
    B = pm.read_int(B_ptr)
    C_ptr = B + 0x0
    C = pm.read_int(C_ptr)
    resetkill_ptr = C + 0x44
    while True:
        try:
            cooldown = pm.read_float(resetkill_ptr)
            if cooldown > 0:
                pm.write_float(resetkill_ptr, float(0))
            time.sleep(0.5)
        except:
            pass
