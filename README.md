# Smartcut
## Meet the Team
| Member | Student ID | Learning Path | Role | Contacts |
| :--------------------: | :--------: | :----------------: | :-----------------------------: | :---------------------------------------------: |
| Rizki Aji Mahardika  | M125DKX4707 | Machine Learning | Machine Learning Engineer | [LinkedIn - Rizki] |
| Feri Firmansah | M282DSX1495 | Machine Learning | Machine Learning Engineer | [LinkedIn - Feri] |
| Nicholas Sky Salvatio | M181DSX0251 | Machine Learning | Machine Learning Engineer | [LinkedIn - Nicholas] |
| Rafli Dwi Putra | C225DSX0611 | Cloud Computing | Cloud Engineer | [LinkedIn - Rafli] |
| Felix Savero | C225DSX0936 | Cloud Computing | Cloud Engineer| [LinkedIn - Felix] |
| Farrell Liko Tanlimhuijaya | A225DSX1678 | Mobile Development | Mobile Engineer | [LinkedIn - Farrell] |

## About Smartcut

This is our capstone project in Bangkit 2023. The application can give suitable hairstyle recommendations based on the user's face shape. We leverage Machine Learning algorithms using the VGG-16 model to analyze the user's facial shape and give personalized recommendations.

## Main Features

- Analyze the user's facial shape
- Give recommendations based on the analyzed face shape

---

How to replicate

Assuming you already have Google Cloud Platform Project with a linked billing account.
- Create a Cloud SQL instance in the VPC and import our .sql database file
- Create a serverless VPC connector
- Create a Cloud Storage Bucket and a service account with the role "Storage Admin", then download the key json file
- Clone this repository
- Add .env and the service account key JSON file
- The .env file MUST contain : 
    - ```JWT_SECRET_KEY : *your_jwt_secret_key*```
    - ```STORAGE_BUCKET : *cloud_storage_bucket_name*```
    - ```STORAGE_KEY : *service_account_key.json*```
    - ```USER_PROFILE_PICTURE_PATH : *cloud_storage_directory*```
    - ```HAIRSTYLE_PICTURE_PATH : *cloud_storage_directory*```
    - ```ID_CARD_PICTURE_PATH : *cloud_storage_directory*```
    - ```BARBERSHOP_PICTURE_PATH : *cloud_storage_directory*```
- Create a virtual environment ```python -m venv venv``` and activate it ```source venv/bin/activate```
- Install the required dependencies```pip install -r requirements.txt```
- Containerize it using Docker and tag it ```gcr.io/**YOUR_PROJECT_ID**/smartcut:v1```
- Push the container image to Google Container Registry (GCR)
- Create a Cloud Run service
    - For the container image url, choose ```gcr.io/**YOUR_PROJECT_ID**/smartcut:v1```
    - For the region, we choose asia-southeast2-a(Jakarta) to get the lowest latency
    - The minimum number of instances is 0
    - The maximum number of instances is 1
    - The memory is 512MiB
    - The number of CPUs is 1
    - Add environment variables : ```DB_HOST, DB_NAME, DB_USER, DB_PASSWORD```
        - For the DB_HOST, the value must be the internal IP of the Cloud SQL instance
    - To connect this Cloud Run instance to Cloud SQL, choose the same VPC as Cloud SQL. Here we use the serverless VPC connector created earlier.
    - **Deploy the application**

The API specification (documentation) can be found here https://drive.google.com/file/d/1Aq_TTDIuAyRKoXk8uddbzlW5c--Df46d/view?usp=sharing

[linkedin - Rizki]: https://www.linkedin.com/in/rizkiajimahardika/
[linkedin - Feri]: https://www.linkedin.com/in/ferifirmansah/
[linkedin - Nicholas]: https://www.linkedin.com/in/nicholas-sky-salvatio-1957091b6/
[linkedin - Rafli]: https://www.linkedin.com/in/rafli-d-70b183137/
[linkedin - Felix]: https://www.linkedin.com/in/felixsavero/
[linkedin - Farrell]: https://www.linkedin.com/in/farrelllikotanlimhuijaya/
