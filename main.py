import pandas as pd
import medical_data_visualizer
from unittest import TestCase, main

class CatPlotTestCase(TestCase):
    def setUp(self):
        # Load the data here or create a mock DataFrame
        self.df = pd.read_csv("medical_examination.csv")  # Make sure this path is correct
        self.fig = medical_data_visualizer.draw_cat_plot(self.df)  # Pass the DataFrame

class HeatMapTestCase(TestCase):
    def setUp(self):
        # Load the data here or create a mock DataFrame
        self.df = pd.read_csv("medical_examination.csv")  # Make sure this path is correct
        self.fig = medical_data_visualizer.draw_heat_map(self.df)  # Pass the DataFrame

if __name__ == '__main__':
    main()


