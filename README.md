# Company Master
<p>In this project we convert raw open data into plots, that tell a story on the state of company registration in Maharashtra.
</p>

---

# Data used in this project
<p>I have used the company master data of Maharashtra in my projects and the links of the data can be found in the reference section.</p>

---

# How to run project?
### Clone the respository using ssh in your project folder
```
git clone git@gitlab.com:mountblue/cohort-17-python/gaurav-tiwari/company-master.git
```

### Install the virtualenv in your current folder if you don't have.
```
pip3 install virtualenv
```

### Create a virtual environment variable.
```
virtualenv v1
```

### Activate the virtual environment by running below command.
```
source v1/bin/activate
```

### Requirements

<p>We can install the requirements of the projects from the requirements.txt file by running the following the command.</p>

```
pip3 install -r requirements.txt
```
### Download all the necessary data required for this project from link given below as well as in reference section.

 * https://data.gov.in/catalog/company-master-data

 * https://www.goldenchennai.com/pin-code/maharashtra-postal-code/

### Keep the CSV file in the current directory
<br>

### Create a .gitignore file and put all the csv files and virtual environment variable in it. In my case, I did something like this in .gitignore file and save the file.
```
*.csv
v1
``` 

---
## Steps to run this prjoect:

1. Download all the data from the given link.
2. Open the histogram.py file, In this file we are plotting the histogram plot for the column for "Authorized_cap" with different intervals and taking input intervals from the users.
* To check the pep8 standards.
```
flake8 histogram.py
```
* To run the file.
```
 python3 histogram.py
```
* If you are getting an error ("UserWarning Matplotlib is currently using agg which is a non-GUI backend so cannot show the figure") then you need to install tkinter library for your computer for showing the plots.
```
pip3 install tk
```
3. Open the bar.py file, In this file we are extracting the year from the DATE_OF_REGISTRATION column from the Maharashtra.csv file and only considering the year >= 2000. Using this data, we are plotting a bar plot of the number of company registrations, vs. year.
* To check pep8 standards.
```
flake8 bar.py
```
* To run the file.
```
python3 bar.py
``` 
4. Open the createCsv.py file, we are creating the csv file of zip_code vs. district in this file and the resource of the data can be found in the reference section.
* To check pep8 standards
```
flake8 createCsv.py
```
* To create the csv file run below command.
```
python3 createCsv.py
```
5. Open the companyReg2015.py file, In this we are only considering data of the year 2015, we finding the zip code by district and we can find zip code in the address column of Maharashtra.csv file. Counting the registration by the district and plotting a bar plot of number of registration vs. district.
* To check pep8 standards
```
flake8 companyReg2015.py
```
* To run the file.
```
python3 companyReg2015.py
```
6. Open the groupBar.py file, we are plotting the grouped bar plot by aggregating registration count over
* Year of registration
* Principal Buisness activity

<br>

* To check pep8 standards
```
flake8 groupBar.py
```

* To run the file.
```
python3 groupBar.py
```
7. Open the test folder for the unit testing. There are total four unit testing file.
* test_bar.py
* test_companyReg2015.py
* test_groupBar.py
* test_histogram.py

---

* Open each and every file and test for pep8 standards and unit testing, replace filename with the actual name of your file.

* To check pep8 standards
```
flake8 file_name.py
```
* To run the file
```
python3 file_name.py
```

* If you are getting any modulenotfound error and import error while testing then copy the path of your project working directory by running the "pwd" command.

    * for linux user, open your .bash_profile and paste the path that you copied, save the file, close the terminal and run the terminal again for unit testing.
    ```
    export PYTHONPATH="path/to/your/project"
    ``` 
    * for mac user, open your .zprofile and paste the path that you copied, save the file close the terminal and run the terminal again for unit testing.
    ```
    export PYTHONPATH="path/to/your/project"
    ```

---
# REFERENCES
* https://data.gov.in/catalog/company-master-data
* https://www.goldenchennai.com/pin-code/maharashtra-postal-code/




