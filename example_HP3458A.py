import pyvisa
rm = pyvisa.ResourceManager('@py')

inst = rm.open_resource("GPIB0::23::INSTR")

inst.write("END ALWAYS")

print(inst.query("ID?"))

#get reading
print(inst.read())
