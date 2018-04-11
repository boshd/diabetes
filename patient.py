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

    def displayPatient(self):
        print("ID : ", self.id_n,  ", Conf: ", self.conf, "Data: ", self.data)
        #df_ = df.loc[df['CODE'] == 33]

    def getPatientId(self):
        return self.id_n

    def getPatientConfidence(self):
        return self.conf

    def getPatientData(self):
        return self.data
