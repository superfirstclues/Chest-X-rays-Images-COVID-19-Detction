
# Chest X-rays COVID-19 Detection

## Project Description
The Chest X-rays COVID-19 Detection project aims to develop a deep learning model to detect COVID-19 cases in chest X-ray images. The model utilizes the MobileNet architecture and is trained on a dataset of chest X-ray images containing COVID-19 positive and negative cases.
## Dataset
The model is trained on a dataset of chest X-ray images that includes both COVID-19, Normal and Viral Pneumonia. The dataset used for training is not included in this repository due to its large size. However, you can obtain the dataset in my Google Drive after this link: https://drive.google.com/drive/folders/1ejOBXjnWi7RNlSUv6m-s4L8k-1hchErx?usp=drive_link
also, similar datasets from various sources such as medical research institutions, public repositories, or kaggle

## Installation
To set up the project on your local machine, follow the steps below:
1. Clone the repository to your local machine where you can either Vs Code, Jupyter notebook 
git clone https://github.com/your-username/chest-xrays-covid19.git
2. Install the necessary dependencies. You can use `pip` to install them:
-it is necessary to use Anaconda distribution in the local Machine it contains most ML inbuild Libraries which will otherwise be installed by pip one after the other.
pip install -r requirements.txt
3.For the sake of the computation complexity of CNN algorithm the local CPU is slower Compared to the GPU of the Google Colab which as well doesn’t not need the installation dependencies. for the Colab you can access the stored chest Chest X-rays dataset by two ways:
a) by using the Script from google.drive import drive 
b) by manually clicking the file file icon and mount 
4. Download the dataset from the provided Google Drive link: and place it in the appropriate directory in the project.

## Usage
To use the Chest X-rays COVID-19 Detection model, follow these steps:
1. Prepare your chest X-ray images for inference. Ensure that your images are in a compatible format (e.g., jpeg, png etc) and place them in a designated directory.
## Web App
The project also includes a web application for convenient usage. Follow the steps below to run the web app on your local machine:
1. Install the necessary dependencies (if not already done): 
pip install -r requirements.txt
2. Launch the web application in your local machine remember the file directory streamlit run app.py on the local Machine after cloning
The web app will be accessible at `http://localhost:5000` in your web browser. Upload your chest X-ray images through the provided interface and view the predicted COVID-19
## Contributing
Contributions to this project are welcome. To contribute, You can submit bug reports, feature requests, or pull requests to improve the project.
## License
This project is licensed under the MIT License. Feel free to modify, distribute, and use the code for both commercial and non-commercial purposes. However, please note that the trained model itself may have specific licensing restrictions depending on the dataset used for training.
## Acknowledgements
We would like to acknowledge the efforts of the researchers and organizations that provide publicly available chest X-ray datasets for COVID-19 research. Their contribution enables the development of models like this one and facilitates the fight against the COVID-19 pandemic.
## Contact
For questions, support, or collaboration opportunities, please contact super.firstclues@gmail.com. Feel free to reach out with any inquiries related to the project.
