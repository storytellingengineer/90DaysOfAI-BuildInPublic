# Time Series Forecasting using LSTM

This project implements a time series forecasting model using Long Short-Term Memory (LSTM) neural networks on a public dataset — the monthly airline passenger data.

## Overview

LSTM models are a type of Recurrent Neural Network (RNN) that are especially good at learning long-term dependencies in sequential data — like stock prices, temperature, or time-series demand.

### Dataset Used
- [Airline Passengers Dataset](https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv)


## Key Steps

1. **Data Preprocessing**  
   - Normalized the data using MinMaxScaler  
   - Converted time series into supervised learning format

2. **Model Architecture**  
   - One LSTM layer with 64 units  
   - Output Dense layer for prediction  
   - Mean Squared Error loss and Adam optimizer

3. **Evaluation**  
   - Plotted predictions vs actual values  
   - Compared visually to understand forecast performance

## Sample Output

The plot below shows predicted vs actual values for the test data.

![forecast](https://github.com/user-attachments/assets/b9b8f38c-1d0e-413f-a0ef-3f125b0f14aa)
