import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder  
from sklearn.impute import SimpleImputer  
import warnings
warnings.filterwarnings("ignore")

class GameImpactAnalysis:
    def _init_(self, data_path):

        self.data = pd.read_csv(data_path)
        self.report = {}    

    def clean_data(self):
        imputer = SimpleImputer(strategy='median')
        numeric_cols = self.data.select_dtypes(include=np.number).columns
        self.data[numeric_cols] = imputer.fit_transform(self.data[numeric_cols])

        le = LabelEncoder()
        cat_cols = self.data.select_dtypes(include='object').columns
        for col in cat_cols:
            self.data[col] = le.fit_transform(self.data[col])

        q1 = self.data['horas_jogo_diarias'].quantile(0.25)
        q3 = self.data['horas_jogo_diarias'].quantile(0.75)
        iqr = q3 - q1
        self.data = self.data[
            (self.data['horas_jogo_diarias'] >= (q1 - 1.5 * iqr)) &
            (self.data['horas_jogo_diarias'] <= (q3 + 1.5 * iqr))
        ]

        self.report['missing_values'] = self.data.isnull().sum().to_dict()
        return self.data

    def analyze_impact(self):
        correlation = self.data[['horas_jogo_diarias', 'Social_Impact', 'Emotional_Impact', 'Cognitive_Impact']].corr()
        