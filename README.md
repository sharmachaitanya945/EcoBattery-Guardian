![EcoBattery-Guardian](https://socialify.git.ci/sharmachaitanya945/EcoBattery-Guardian/image?description=1&descriptionEditable=EcoBattery%20Guardian%3A%20Predictive%20maintenance%2C%20data%20simulation%2C%20education%2C%20recycling%20management.&font=Source%20Code%20Pro&language=1&name=1&owner=1&pattern=Circuit%20Board&stargazers=1&theme=Dark)

# 🔋 EV Battery Management System

Welcome to the EV Battery Management System! 🚗🔋 A comprehensive solution for managing and predicting the condition of electric vehicle (EV) batteries. This application features a data simulator, a machine learning model, and a web interface to help you monitor and predict battery health.

## 🌟 Features

- 📊 **Data Simulation**: Generates and stores random battery data (temperature, voltage, and current).
- 🔍 **Prediction**: Predicts battery condition based on input data using a machine learning model.
- 🌐 **Web Interface**: User-friendly interface to input battery data and view predictions.
- 📈 **Database Storage**: Stores generated data in an SQLite database.

## 📸 Screenshots

![EV Battery Management System Screenshot](images/Screenshot.png)

## 📷 Demo

[![YouTube](https://i.ytimg.com/vi/AmsKeEKQCnc/hqdefault.jpg?sqp=-oaymwE2CNACELwBSFXyq4qpAygIARUAAIhCGAFwAcABBvABAfgB_giAAtAFigIMCAAQARhdIGUoVzAP&rs=AOn4CLBxkfg3Js7Pip84k5Jg4o9j-wcEEg)](https://youtu.be/AmsKeEKQCnc)

## 🛠️ Technologies Used

- ⚛️ **HTML**
- 🎨 **CSS**
- 📜 **JavaScript**
- 🌐 **Flask**
- 🐍 **Python**
- 🗄️ **SQLite**
- 🧠 **scikit-learn**

## 📦 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sharmachaitanya945/EV-Battery-Management-System.git
    ```
2. Navigate to the project directory:
    ```bash
    cd EV-Battery-Management-System
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```
4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

1. **Run Data Simulation**:
    ```bash
    python data_simulator/generate_data.py
    ```
2. **Run the Flask Application**:
    ```bash
    cd recycling_management_platform/frontend/public
    python app.py
    ```
3. **Access the Application**:
    Open your web browser and go to `http://127.0.0.1:5000`.
4. **Interact with the Web Interface**:
    - Enter battery data (temperature, voltage, current) into the form.
    - Click the "Check Condition" button to see the prediction.
    - View the predicted condition of the battery.

## 📜 License

This project is licensed under the MIT License.

## 🙌 Acknowledgements

- 🌐 [Flask](https://flask.palletsprojects.com/) for the web framework.
- 🧠 [scikit-learn](https://scikit-learn.org/) for the machine learning model.
- 📊 [SQLite](https://www.sqlite.org/) for the database.

## 🤝 Contributing

Contributions are welcome! Open an issue or submit a pull request for any improvements or suggestions. Let's make this app even better together! 🌟
