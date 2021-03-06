###########
# imports #
###########
from Parser import Parser
from Parser import C_COMMAND_TYPE, A_COMMAND_TYPE, EMPTY_COMMAND_TYPE, LABEL_COMMAND_TYPE

#############
# constants #
#############
D_INST_FIRST_DELIMITERS = "="
D_INST_SECOND_DELIMITERS = ";"


class SecondParse (Parser):
    """
    A Parser object to parse the command to its parts in the second parse phase.
    """
    def __init__(self):
        """
        Creates a new SecondParse object.
        """
        Parser.__init__(self)
        self.__address = None
        self.__dest = None
        self.__comp = None
        self.__jump = None

    def parse(self):
        """
        Parse the command into its parts and set the address / dest / comp / jump
        """
        if self.get_type() == A_COMMAND_TYPE:
            self.__address = self.command[1:]  # cuts the A-instruction note
            # sets the rest of the parts to None
            self.__dest = None
            self.__comp = None
            self.__jump = None
        elif self.get_type() == C_COMMAND_TYPE:
            command_parts = self.command.split(D_INST_FIRST_DELIMITERS)  # split the dest and the comp
            if len(command_parts) < 2:  # if dest doesn't exist
                command_parts.insert(0, "")
            self.__dest = command_parts[0]

            second_part = command_parts[1].split(D_INST_SECOND_DELIMITERS)  # split the jump part
            if len(second_part) < 2:  # if jump doesn't exist
                second_part.append("")
            self.__comp, self.__jump = second_part
            self.__address = None  # sets the rest of the parts to None

    def get_address(self):
        """
        :return: the address in the memory in the command in case of the command is a A-address. Otherwise, returns None
        """
        return self.__address

    def get_dest(self):
        """
        :return: the dest part of the command in case of the command is a C-address. Otherwise, returns None
        """
        return self.__dest

    def get_comp(self):
        """
        :return: the comp part of the command in case of the command is a C-address. Otherwise, returns None
        """
        return self.__comp

    def get_jump(self):
        """
        :return: the jump part of the command in case of the command is a C-address. The jump can be an empty
        string. If the command is not a C-instruction, returns None
        """
        return self.__jump
