from mycroft import MycroftSkill, intent_file_handler


class CakeCommand(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('command.cake.intent')
    def handle_command_cake(self, message):
        self.speak_dialog('command.cake')


def create_skill():
    return CakeCommand()

