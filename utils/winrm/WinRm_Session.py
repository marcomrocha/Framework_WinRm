import winrm

EXECUTION = 'executionpolicy'

GET_EXECUTION_POLICY = str.format('get-{}', EXECUTION)

SET_EXECUTION_POLICY = str.format('set-{}', EXECUTION)

ERROR = "Error"

SUCCESSFUL = "Successful"

IPCONFIG = 'ipconfig'


class WinRm_Session:

    def __init__(self, I_VM):
        """
        Construct
        :param I_VM: classes that implement the I_VM interface.
        """
        self.host_name = I_VM.get_host_name()   # set windows host name
        self.user_name = I_VM.get_user_name()   # set windows user name
        self.user_password = I_VM.get_user_password()   # set windows user password
        """ instance the win_rm library """
        self.session = winrm.Session(self.host_name, auth=(self.user_name, self.user_password))

    def get_ipconfig_all(self):
        """
        Get the IP configuration of Windows OS.
        :return: A String with the IpConfig information.
        """
        return self.session.run_cmd(IPCONFIG, ['/all']).std_out

    def get_environment_variable(self):
        """
        Get the environments variables of Windows OS.
        :return: A string with the environments variables of the system.
        """
        command_env = 'Get-ChildItem Env:'
        return self.session.run_ps(command_env).std_out

    def get_hostname_configuration(self):
        """
        Get the hostname configuration of Windows OS.
        :return: A string with the hostname configuration of the OS.
        """
        command_hostname = str.format('{}{}', 'nbtstat -a', self.host_name)
        return self.session.run_ps(command_hostname).std_out

    def get_execution_policy(self):
        """
        get the status execution policy of the OS.
        :return: a string with the status execution policy.
        """
        return self.session.run_ps(GET_EXECUTION_POLICY).std_out

    def set_execution_policy_to_unrestricted(self):
        """
        Set up the execution policy to unrestricted status.
        :return: a string message of confirmation
        "Successful" as status ok
        "Error" as bad request.
        """
        code_status = self.session.run_ps('%s Unrestricted' % SET_EXECUTION_POLICY).status_code
        return SUCCESSFUL if code_status == 0 else ERROR

    def set_execution_policy_to_restrict(self):
        """
        Set up the execution policy to restricted status.
        :return: a string message of confirmation
        "Successful" as status ok
        "Error" as bad request.
        """
        code_status = self.session.run_ps('%s restricted' % SET_EXECUTION_POLICY).status_code
        return SUCCESSFUL if code_status == 0 else ERROR

    def run_ps_scripts(self, path):
        """
        Execute a powerShell script file.
        :param path: file path.
        :return: script result.
        """
        return self.session.run_ps(path).std_out

