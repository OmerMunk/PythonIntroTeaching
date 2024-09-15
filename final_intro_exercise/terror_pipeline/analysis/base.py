

class AnalysisUnit(ABC):
    @abstractmethod
    def analyze(self):
        pass

    @staticmethod
    def current_utc_time():
        pass

class Loggable:
    @staticmethod
    def log(message):
        # log all actions of the classes to one logfile.
        pass

class IntelligenceAnalysisUnit(AnalysisUnit, Loggable):
    def __init__(self, name):
        pass

    @property
    def name(self):
        pass

    @name.setter
    def name(self, new_name):
        pass

    def log(self, message):
        pass

    @classmethod
    def create_analysis_unit(cls, name):
        pass

    def __eq__(self, other):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass
