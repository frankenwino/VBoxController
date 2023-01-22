from vboxcontroller import VBoxControl

v = VBoxControl()
v.start_vm(vm_name="PostgreSQL")