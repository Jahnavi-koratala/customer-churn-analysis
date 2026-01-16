import sys
import os
from logging_setup import setup_logging
from data_analysis import ExploratoryDataAnalyzer
from visualizations import VisualizationEngine

logger = setup_logging('run_analysis')

if __name__ == '__main__':
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, 'customer_data.csv')
        analyzer = ExploratoryDataAnalyzer(csv_path)
        df = analyzer.get_dataframe()
        VisualizationEngine.generate_plots(df)
    except Exception as e:
        error_type, error_msg, error_line = sys.exc_info()
        logger.info(f'Error in line no:{error_line.tb_lineno} due to:{error_msg}')