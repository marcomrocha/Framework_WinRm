from abc import ABCMeta,abstractmethod


class I_VM(object):
    __metaclass__ = ABCMeta

    global host_name
    global user_name
    global user_password

    @abstractmethod
    def get_host_name(self):
        """
        Get the hostname of the Windows OS.
        :return: a string with the hostname of the Windows OS.
        """
        pass

    @abstractmethod
    def get_user_name(self):
        """
        Get the user name of the Windows user.
        :return: a string with the user name.
        """
        pass

    @abstractmethod
    def get_user_password(self):
        """
        Get the user password.
        :return: a string with the user password.
        """
        pass




