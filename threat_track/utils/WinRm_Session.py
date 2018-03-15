import winrm

EXECUTION = 'executionpolicy'

GET_EXECUTION_POLICY = str.format('get-{}', EXECUTION)

SET_EXECUTION_POLICY = str.format('set-{}', EXECUTION)

ERROR = "Error"

SUCCESSFUL = "Successful"

IPCONFIG = 'ipconfig'


""" This Class use WinRM Lib. for execute PowerShell commands and Command Prompt"""
class WinRm_Session:
    global result_request

    def builtWinRM(self, I_VM):
        """
        Construct
        :param I_VM: classes that implement the I_VM interface.
        """
        self.host_name = I_VM.get_host_name()   # set windows host name
        self.user_name = I_VM.get_user_name()   # set windows user name
        self.user_password = I_VM.get_user_password()   # set windows user password
        self.session = winrm.Session(self.host_name, auth=(self.user_name, self.user_password))

    def get_ping_to_windows_rm(self):
        """
        Do ping to windows configured
        :return: string
        """
        self.result_request = self.session.run_cmd('ping ' + self.host_name).std_out
        return self.result_request

    def get_ipconfig_all(self):
        """
        Get the IP configuration of Windows OS.
        :return: A String with the IpConfig information.
        """
        self.result_request = self.session.run_cmd(IPCONFIG, ['/all']).std_out
        return self.result_request

    def get_environment_variable(self):
        """
        Get the environments variables of Windows OS.
        :return: A string with the environments variables of the system.
        """
        command_env = 'Get-ChildItem Env:'
        self.result_request = self.session.run_ps(command_env).std_out
        return self.result_request

    def get_hostname_configuration(self):
        """
        Get the hostname configuration of Windows OS.
        :return: A string with the hostname configuration of the OS.
        """
        command_hostname = str.format('{}{}', 'nbtstat -a ', self.host_name)
        self.result_request = self.session.run_ps(command_hostname).std_out
        return self.result_request

    def get_execution_policy(self):
        """
        get the status execution policy of the OS.
        :return: a string with the status execution policy.
        """
        self.result_request = self.session.run_ps(GET_EXECUTION_POLICY).std_out
        return self.result_request

    def set_execution_policy_to_unrestricted(self):
        """
        Set up the execution policy to unrestricted status.
        :return: a string message of confirmation
        "Successful" as status ok
        "Error" as bad request.
        """
        code_status = self.session.run_ps('%s Unrestricted' % SET_EXECUTION_POLICY).status_code
        self.result_request = SUCCESSFUL if code_status == 0 else ERROR
        return self.result_request

    def set_execution_policy_to_restrict(self):
        """
        Set up the execution policy to restricted status.
        :return: a string message of confirmation
        "Successful" as status ok
        "Error" as bad request.
        """
        code_status = self.session.run_ps('%s restricted' % SET_EXECUTION_POLICY).status_code
        self.result_request = SUCCESSFUL if code_status == 0 else ERROR
        return self.result_request

    def run_ps_scripts(self, path):
        """
        Execute a powerShell script file.
        :param path: file path.
        :return: script result.
        """
        expect_result = str(self.session.run_ps(path).std_out)
        return expect_result

    def verify_results(self, expect_result):
        expect_result = str(self.result_request).__contains__(str(expect_result))
        return str(expect_result)
