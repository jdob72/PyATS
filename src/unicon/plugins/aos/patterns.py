'''
Author: Alex Pfeil
Contact: www.linkedin.com/in/alex-p-352040a0
Contents largely inspired by sample Unicon repo and Knox Hutchinson:
https://github.com/CiscoDevNet/pyats-plugin-examples/tree/master/unicon_plugin_example/src/unicon_plugin_example
'''
class aosPatterns():
    def __init__(self):
        super().__init__()
        self.shell_prompt = r'.+$'
        self.login_prompt = r'.+$'
        self.disable_mode = r'((.|\n)*\>)$'
        self.config_mode = r'((.|\n)*config.#)$'
        self.password = r'.+$'
        self.linePassword = r'(^(.*?)\w+.*[Pp]assword:)$'
        self.enable_prompt = r'(^(.*?)((.|\n)*)w+.*#)$'
        self.config_prompt = r'(^(.*?)\w+.config.#)$'
        self.proxy = r'((.|\n)*rhome.*\$)$'
        self.generic = r'(^(.*?)\#)$'
        self.escape_char = r"Escape character is '(~)'"
        self.press_return = '((.|\n)*continue)$'