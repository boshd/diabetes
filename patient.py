import pandas as pd

class Patient(object):
    id_n = 0
    data = pd.DataFrame()
    conf = 0

    # Constructor / Initaliser
    def __init__(self, id_n, data, conf):
        self.id_n = id_n
        self.data = data
        self.conf = conf

    def getPatientId(self):
        return self.id_n

    def getPatientConfidence(self):
        return self.conf

    def getPatientData(self):
        return self.data

    def update_patient_data(new_data):
        self.data = new_data