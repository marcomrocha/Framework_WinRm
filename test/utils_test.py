from utils.winrm.WinRm_Session import WinRm_Session
from vm_classes.vm_window_7 import VM_Window_7
from vm_classes.vm_windows_8 import VM_Windows_8

# this is an example for instance VM_windows
win7 = VM_Window_7('192.168.130.129', '\Marco Mendez', 'Control123')
win8 = VM_Windows_8('192.168.130.129', '\Marco Mendez', 'Control123')

# is an example for instance WinRm_Session.
win_rm = WinRm_Session(win8)

print(win_rm.host_name)  # Print the configured hostname
print(win_rm.user_name)  # Print the configured username
print(win_rm.user_password)  # Print the configured user password
print(win_rm.set_execution_policy_to_restrict())  # print the execution set_execution_policy
print(win_rm.get_ipconfig_all())    # print the ipconfig result.
