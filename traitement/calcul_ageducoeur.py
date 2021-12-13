import math
import time

from Form import Form


class AgeDuCoeurCalculator:
    def __init__(self, form: Form):
        self.form = form

    def calculerAgeDuCoeur(self):
        p = self.calculerRisque()
        if self.form.getInput("genre").getValue() == "femme":
            C = 0.009*(p**3) - 0.43*(p**2) + 8.6034*p + 20.739
        else:
            C = 0.0029*(p**3) - 0.1827*(p**2) + 4.8117*p + 22.869

        return C

    def calculerRisque(self):

        X = []
        X += [math.log(self.getNumericValueOfInput("age"))]
        X += [self.getNumericValueOfInput("fumeur")]
        X += [self.getNumericValueOfInput("diabetique")]
        hypertension = self.getNumericValueOfInput("hypertension")
        X += [hypertension]
        hypertension_traitee = self.getNumericValueOfInput("traitement_hypertension")
        X += [hypertension_traitee]
        #X += [math.log(self.getNumericValueOfInput("tension"))]
        X += [math.log(self.getNumericValueOfInput("taux_colesterol"))]
        X += [math.log(self.getNumericValueOfInput("HDL_colesterol"))]

        beta_homme = [3.06117, 0.65451, 0.57367, 0, 1.12370, -0.93263]
        if hypertension == 1:
            if hypertension_traitee == 1:
                beta_homme[3] = 1.99881
            else:
                beta_homme[3] = 1.93303

        beta_femme = [2.32888, 0.52873, 0.69154, 0, 1.20904, -0.70833]
        if hypertension == 1:
            if hypertension_traitee == 1:
                beta_homme[3] = 2.82263
            else:
                beta_homme[3] = 2.76157

        if self.form.getInput("genre").getValue() == "femme":
            So = 0.88936
            beta = beta_femme
        else:
            So = 0.95012
            beta = beta_homme


        sum_betai_xi = 0
        for i in range(len(X)):
            sum_betai_xi += beta[i]*X[i]

        moy_xi = 0
        for i in range(len(X)):
            moy_xi += X[i]
        moy_xi /= len(X)

        sum_betai = 0
        for i in range(len(X)):
            sum_betai += beta[i]

        p = 1 - So ** math.exp(sum_betai_xi - moy_xi*sum_betai)

        return p

    def getNumericValueOfInput(self, inputId):
        strValue = self.form.getInput(inputId).getValue()
        if strValue == "oui" or strValue == "yes":
            return 1
        if strValue == "non" or strValue == "no":
            return 0
        return float(strValue)




