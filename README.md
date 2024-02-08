# Celsius to Fahrenheit Neural Network Example

This Jupyter Notebook illustrates the process of building, training, and evaluating a simple neural network to convert temperatures from Celsius to Fahrenheit using PyTorch, a machine learning library. Here's a didactic description of what is being done:

## 1. Library Imports
The project begins with the importation of necessary libraries. `torch` and `torch.nn` are used for constructing the neural network, `pandas` for data manipulation, and `matplotlib.pyplot` for data and results visualization.

## 2. Conversion Function
A `convert_celsius_to_farenheit` function is defined to calculate the actual values for converting Celsius to Fahrenheit. This function is utilized to generate true values against which the model's predictions will be compared.

## 3. Data Preparation
An interval of temperature values in Celsius is created using `torch.linspace` and converted into Fahrenheit using the defined function. Additionally, a `pandas` DataFrame with specific temperature values for training is prepared. The data is converted into PyTorch tensors, which are the required format for training with neural networks.

## 4. Model Definition
The `CelsiusFarenheintModel` class is defined by inheriting from `nn.Module`. It has a single linear layer (`nn.Linear`) with one input and one output neuron, representing the expected linear relationship between temperatures in Celsius and Fahrenheit.
