# flaskIP3

### Clone this repository
```bash
 git clone https://github.com/conceptacherono/flaskIP3.git
```
* Move into the cloned directory:
```bash
cd BLUE_CHIP_PITCH_APP
```
* Create and activate your virtual environment:
```bash
mkvirtualenv virtual
```
* Install project dependancies within your active environment: (Read: requirements.txt and use command below)
```bash
(virtual)$ pip3 Install -r requirements.txt
```
* Environment variables:
    *  Create a file called ```.env``` in the root folder
    ```bash
    (virtual)$ touch .env
    ```
    * Add the following lines to the file as seen in ```.env-template```
    ```bash 
    SECRET_KEY=
    DATABASE_URL=
    ```
* Start the flask server
```bash
(Virtual)$ flask run
```
## Features and BDD

- Users are able to create user profile and login to their profiles.


## Technology Used

**Framework:** Flask
**Language** Python

### Developed with
**Structure:** Bootstrap, HTML

## Author

* Design and developed by: [Concepta Cherono](https://github.com/conceptacherono)
