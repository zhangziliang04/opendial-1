from xml.etree.ElementTree import Element, SubElement, Comment
from ElementTree_pretty import prettify


class Rules():
    def __init__(self, top):
        """
        Sets the initial parameters in the domain file
        :param top: top element in xml file
        :return: None
        """
        self.top = Element(top)
        self.top.append(Comment('Assignment 3 - Development of a Spoken Dialogue System'))

        self.initial_state = Element('initialstate')
        self.initial_state.append(Comment('(optional) initial state variables '))
        self.top.append(self.initial_state)

        self.parameters = Element('parameters')
        self.parameters.append(Comment('(optional) prior distributions for rule parameters'))
        self.top.append(self.parameters)

        self.settings = Element('settings')
        _modules = SubElement(self.settings, 'modules')
        _modules.text = 'opendial.plugins.NuanceSpeech'
        _id = SubElement(self.settings, 'id')
        _id.text = 'NMDPTRIAL_garash8420141029160511'
        _key = SubElement(self.settings, 'key')
        _key.text = 'd89a8e437c74b8cc9b73e0eef132adce26889142e1ffd000c4729adcaaa95c8244eac5c05e7e8cf9f16de7e29f95b1c5' \
                    '1d4207fe41d7fe054998e1f4423d7686'
        _lang = SubElement(self.settings, 'lang')
        _lang.text = 'nor-NOR'
        self.top.append(self.settings)

    def if_(self, model_name, variable, _if, _then, user='u_u', system='u_m'):
        """
        simple if statements
        :param model_name: name of model, example: <model trigger="u_u"> , here trigger is model_name
        :param variable: variable of model, example <model trigger="u_u">, here "u_u" is variable
        :param _if: the if statement
        :param _then: when if statement is true
        :param user: name of user utterance
        :param system: name of system utterance
        :return: None
        """
        kw = {model_name: variable}  # keyword variables needs to be sent as dictionary

        model = Element('model', **kw)
        rule = SubElement(model, 'rule')
        case = SubElement(rule, 'case')

        self.top.append(model)

    def create_xml(self):
        return prettify(self.top)
