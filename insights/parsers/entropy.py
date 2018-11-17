from insights import Parser, parser
from insights.specs import Specs


@parser(Specs.random_avail)
class RandomEntropyAvail(Parser):
    """
    Checks the value of /proc/sys/kernel/random/entropy_avail
    """
    def parse_content(self, content):
        self.value = int(content[0])


@parser(Specs.random_poolsize)
class RandomPoolsize(Parser):
    """
    Checks the value of /proc/sys/kernel/random/poolsize
    """
    def parse_content(self, content):
        self.value = int(content[0])
