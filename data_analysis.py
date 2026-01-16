import sys
import pandas as pd
import warnings
from logging_setup import setup_logging

warnings.filterwarnings('ignore')
logger = setup_logging('data_analysis')

class ExploratoryDataAnalyzer:
    def __init__(self, path):
        try:
            self.path = path
            self.df = pd.read_csv(self.path)
            logger.info(f'Data Set :\n{self.df}')
            logger.info(f'Data Set shape :\n{self.df.shape}')
            logger.info(f'Data Set null values :\n{self.df.isnull().sum()}')
            logger.info(f"value counts in gender :\n{self.df['gender'].value_counts()}")
            logger.info(f"value counts in senior citizen :\n{self.df['SeniorCitizen'].value_counts()}")
            logger.info(f"value counts in Internetservice :\n{self.df['InternetService'].value_counts()}")
            logger.info(f"value counts in paymentmethod :\n{self.df['PaymentMethod'].value_counts()}")
            logger.info(f"value counts in sim :\n{self.df['Sim'].value_counts()}")
            logger.info(f"value counts in region :\n{self.df['Region'].value_counts()}")

        except Exception as e:
            error_type, error_msg, error_line = sys.exc_info()
            logger.info(f'Error in line no:{error_line.tb_lineno} due to:{error_msg}')

    def get_dataframe(self):
        return self.df
