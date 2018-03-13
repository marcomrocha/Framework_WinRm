from vm_interfaces.I_VM import I_VM


class VM_Windows_8(I_VM):

    def __init__(self, host_name, user_name, user_password):
        """
        Construct
        :param host_name: hostname of the windows OS.
        :param user_name: User name of the windows OS.
        :param user_password: user password of the windows OS.
        """
        self.host_name = host_name
        self.user_name = user_name
        self.user_password = user_password
        super(VM_Windows_8, self).__init__()

    def get_host_name(self):
        """
        Get the hostname of the Windows OS.
        :return: a string with the hostname of the Windows OS.
        """
        return self.host_name

    def get_user_name(self):
        """
        Get the user name of the Windows user.
        :return: a string with the user name.
        """
        return self.user_name

    def get_user_password(self):
        """
        Get the user password.
        :return: a string with the user password.
        """
        return self.user_password
