# Importing necessary libraries
import pandas as pd  # Importing pandas library for data manipulation
from sklearn import linear_model  # Importing linear_model module from sklearn for linear regression
import tkinter as tk  # Importing tkinter library for GUI development
import matplotlib.pyplot as plt  # Importing matplotlib.pyplot for plotting
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Importing FigureCanvasTkAgg for embedding matplotlib plots in tkinter GUI

# Reading the CSV file into a DataFrame
df = pd.read_csv('HDFC.csv')  # Reading HDFC.csv file into a pandas DataFrame

# Defining independent variables (features) and dependent variable (target)
X = df[['Open','Close']]  # Independent variables
Y = df['Turnover']  # Dependent variable

# Creating a linear regression model
regr = linear_model.LinearRegression()  # Creating a linear regression model object
regr.fit(X, Y)  # Fitting the model to the data

# Creating a Tkinter GUI window
root = tk.Tk()  # Creating a Tkinter GUI window object
root.title("Stock Turnover Prediction")  # Setting the title of the GUI window

# Creating a canvas for placing widgets
canvas1 = tk.Canvas(root, width=700, height=400, bg='lightsteelblue2')  # Creating a canvas with specified width, height, and background color
canvas1.pack()  # Packing the canvas into the root window

# Creating a label for the title
label_title = tk.Label(root, text="Stock Turnover Prediction", bg='lightsteelblue2', fg='black', font=('Helvetica', 20, 'bold'))  # Creating a label widget with specified text, background color, foreground color, and font
canvas1.create_window(350, 30, window=label_title)  # Placing the label widget on the canvas at specified coordinates

# Creating a label for the instruction
label_instruction = tk.Label(root, text="Enter Open and Close Rates:", bg='lightsteelblue2', fg='black', font=('Helvetica', 12))  # Creating a label widget with specified text, background color, foreground color, and font
canvas1.create_window(350, 80, window=label_instruction)  # Placing the label widget on the canvas at specified coordinates

# Creating an entry box for Open rate
entry_open = tk.Entry(root, font=('Helvetica', 12))  # Creating an entry widget with specified font
canvas1.create_window(300, 120, window=entry_open)  # Placing the entry widget on the canvas at specified coordinates

# Creating an entry box for Close rate
entry_close = tk.Entry(root, font=('Helvetica', 12))  # Creating an entry widget with specified font
canvas1.create_window(500, 120, window=entry_close)  # Placing the entry widget on the canvas at specified coordinates

# Function to predict turnover based on user input
def predict_turnover():
    open_rate = float(entry_open.get())  # Getting the value from the entry box and converting it to float
    close_rate = float(entry_close.get())  # Getting the value from the entry box and converting it to float
    predicted_turnover = regr.predict([[open_rate, close_rate]])[0]  # Predicting turnover based on user input and accessing the first element of the array
    predicted_turnover_millions = predicted_turnover / 1000000  # Converting predicted turnover to millions
    label_prediction = tk.Label(root, text=f"Predicted Turnover: {predicted_turnover_millions:.2f} Million INR", bg='orange', font=('Helvetica', 14))  # Creating a label widget with predicted turnover value in millions
    canvas1.create_window(350, 200, window=label_prediction)  # Placing the label widget on the canvas at specified coordinates

# Button to trigger the prediction function
button_predict = tk.Button(root, text="Predict Turnover", command=predict_turnover, bg='orange', fg='black', font=('Helvetica', 12))  # Creating a button widget with specified text, command, background color, foreground color, and font
canvas1.create_window(350, 160, window=button_predict)  # Placing the button widget on the canvas at specified coordinates

# Scatter plot 1: Open rate vs. Turnover
figure1 = plt.Figure(figsize=(5, 4), dpi=100)  # Creating a figure object with specified size and dpi
ax1 = figure1.add_subplot(111)  # Adding a subplot to the figure
ax1.scatter(df['Open'].astype(float), df['Turnover'].astype(float), color='r')  # Creating a scatter plot
scatter1 = FigureCanvasTkAgg(figure1, root)  # Creating a canvas for embedding matplotlib plot in tkinter GUI
scatter1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)  # Packing the canvas into the root window
ax1.legend(['Turnover'])  # Adding a legend to the plot
ax1.set_xlabel('Open Rate')  # Setting the x-axis label
ax1.set_title('Open Rate Vs. Turnover')  # Setting the title of the plot

# Scatter plot 2: Close rate vs. Turnover
figure2 = plt.Figure(figsize=(5, 4), dpi=100)  # Creating a figure object with specified size and dpi
ax2 = figure2.add_subplot(111)  # Adding a subplot to the figure
ax2.scatter(df['Close'].astype(float), df['Turnover'].astype(float), color='g')  # Creating a scatter plot
scatter2 = FigureCanvasTkAgg(figure2, root)  # Creating a canvas for embedding matplotlib plot in tkinter GUI
scatter2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)  # Packing the canvas into the root window
ax2.legend(['Turnover'])  # Adding a legend to the plot
ax2.set_xlabel('Close Rate')  # Setting the x-axis label
ax2.set_title('Close Rate Vs. Turnover')  # Setting the title of the plot

# Running the main event loop
root.mainloop()  # Running the main event loop of the GUI
