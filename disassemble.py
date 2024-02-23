import os
import subprocess

Import("env")

def run_objdump(source, target, env):
    path_rel = os.path.dirname(str(target[0]))
    path = os.path.join(os.getcwd(), path_rel)
    out_file = os.path.join(path, "disassembly.asm")
    with open (out_file, "w") as f:
        subprocess.run(["avr-objdump", "-dS", str(target[0])], stdout=f, check=True)

env.AddPostAction("$BUILD_DIR/${PROGNAME}.elf", run_objdump)