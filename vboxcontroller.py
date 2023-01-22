from pprint import pprint
import subprocess
from datetime import datetime

class VBoxControl():
    
    def now(self) -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def print_message(self, message: str):
        print(f"{self.now()} - {message}")
    
    def run_command(self, command_list: list):
        output = subprocess.check_output(command_list).decode().strip()
        
        return output.split("\n")

    def parse_vms_list(self, vms_strings_list: list) -> list:
        vm_list = []
        for vm_string in vms_strings_list:
            vm = vm_string.split("{")[0].strip().replace('"', "")
            if len(vm) > 0:
                vm_list.append(vm)
        
        return vm_list

    def vms(self) -> list:
        command_list = ["VBoxManage", "list", "vms"]
        vms_strings_list = self.run_command(command_list)
        vm_list = self.parse_vms_list(vms_strings_list)
        
        return vm_list

    def running_vms(self) -> list:
        command_list = ["VBoxManage", "list", "runningvms"]
        vms_strings_list = self.run_command(command_list)
        vm_list = self.parse_vms_list(vms_strings_list)
        
        return vm_list
    
    def start_vm(self, vm_name):
        if vm_name in self.vms():
            if vm_name not in self.running_vms():
                self.print_message(f"Starting {vm_name}")
                command_list = ["VBoxManage", "startvm", vm_name, "--type", "headless"]
                # self.print_message(command_list)
                self.run_command(command_list)
            else:
                self.print_message(f"{vm_name} is already running")
        else:
            self.print_message(f"No VM named {vm_name} exists")
            
    def start_all_vms(self):
        for vm_name in self.vms():
            if vm_name not in self.running_vms():
                self.print_message(f"Starting {vm_name}")
                command_list = ["VBoxManage", "startvm", vm_name, "--type", "headless"]
                # self.print_message(command_list)
                self.run_command(command_list)
            else:
                self.print_message(f"{vm_name} is already running")
                
    def shutdown_all_running_vms(self):
        running_vms_list = self.running_vms()
        if len(running_vms_list) > 0:
            for running_vm in running_vms_list:
                self.print_message(f"Shutting down {running_vm}")
                command_list = ["VBoxManage", "controlvm", running_vm, "acpipowerbutton"]
                # self.print_message((command_list)
                self.run_command(command_list)
        else:
            self.print_message("No VMS running")
        
if __name__ == "__main__":
    pass
    # v = VBoxControl()
    # pprint(v.vms())
    # pprint(v.running_vms())
    # v.shutdown_running_vms()
    # v.start_vm(vm_name="PostgreSQL")
    # v.start_all_vms()
    # v.shutdown_all_running_vms()