### Step 1: Create a Virtual Environment

1. **Navigate to Your Project Directory**:
   - Open a command prompt (Windows) or terminal (Mac/Linux).
   - Navigate to the directory where you want to create your Django project.
     ```bash
     cd path/to/your/project-directory
     ```

2. **Create a Virtual Environment**:
   - Run the following command to create a virtual environment. Replace `myenv` with your preferred environment name.
     ```bash
     python -m venv myenv
     ```

3. **Activate the Virtual Environment**:
   - **Windows**:
     ```bash
     myenv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source myenv/bin/activate
     ```

4. **Verify Activation**:
   - Your command prompt or terminal should now show the name of your virtual environment. For example, `(myenv)`.

### Step 2: Install Django

1. **Install Django**:
   - With the virtual environment activated, install Django using pip.
     ```bash
     pip install django
     ```

2. **Verify Installation**:
   - Check the installed version of Django.
     ```bash
     django-admin --version
     ```

### Step 3: Create a Django Project

1. **Create a New Django Project**:
   - Run the following command to create a new Django project. Replace `myproject` with your preferred project name.
     ```bash
     django-admin startproject myproject
     ```

2. **Navigate to the Project Directory**:
   - Change to the project directory.
     ```bash
     cd myproject
     ```

3. **Verify Project Structure**:
   - Your project directory should look like this:
     ```
     myproject/
         manage.py
         myproject/
             __init__.py
             settings.py
             urls.py
             wsgi.py
     ```

### Step 4: Create a Django App

1. **Create a New App**:
   - Run the following command to create a new app within your project. Replace `myapp` with your preferred app name.
     ```bash
     python manage.py startapp myapp
     ```

2. **Verify App Structure**:
   - Your project directory should now look like this:
     ```
     myproject/
         manage.py
         myproject/
             __init__.py
             settings.py
             urls.py
             wsgi.py
         myapp/
             __init__.py
             admin.py
             apps.py
             models.py
             tests.py
             views.py
     ```

### Step 5: Configure the Django App

1. **Add the App to Installed Apps**:
   - Open `myproject/settings.py`.
   - Add your new app to the `INSTALLED_APPS` list.
     ```python
     INSTALLED_APPS = [
         ...
         'myapp',
     ]
     ```

2. **Run Migrations**:
   - Apply initial migrations to set up the database.
     ```bash
     python manage.py migrate
     ```

3. **Run the Development Server**:
   - Start the Django development server.
     ```bash
     python manage.py runserver
     ```

4. **Verify the Setup**:
   - Open your web browser and go to `http://127.0.0.1:8000/`. You should see the Django welcome page.
