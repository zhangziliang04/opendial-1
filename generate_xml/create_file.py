from rules import Rules


class GenerateXML():
    def __init__(self):
        """
        init method
        :return: None
        """
        self.r = Rules('domain')
        self.create_file()

    def create_file(self):
        """
        Creates the xml file
        :return: None
        """
        save = open('/Users/arashsaidi/Blindern/INF5820/oblig3/opendial/domains/my-test-domains/therapist.xml', 'w')
        save2 = open('therapist.xml', 'w')

        self.rules()

        save.write(self.r.create_xml())
        save2.write(self.r.create_xml())

    def rules(self):
        self.r = Rules('domain')

        self.r.if_('trigger', 'u_u', 'ta til venstre', 'ok')