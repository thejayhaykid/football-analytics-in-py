# Football Analytics in Python

Following along the book using a VSCode Dev Container

[Companion Repo in R](https://github.com/thejayhaykid/football-analytics-in-r)

---

## This project uses virtualenv in each chapter folder

`virtualenv` is another popular tool for creating isolated Python environments. While it doesn't handle dependency management like Pipenv, it’s simple, lightweight, and works well when you only need environment isolation. Here’s how to get started with `virtualenv`:

### 1. **Install Virtualenv**
   First, install `virtualenv` using `pip`:
   ```bash
   pip install virtualenv
   ```

### 2. **Create a Virtual Environment**
   Navigate to your project directory and create a virtual environment. By convention, it’s usually called `venv`, but you can name it whatever you like:
   ```bash
   virtualenv venv
   ```
   This creates a `venv` folder with a standalone Python environment, including a separate `bin` or `Scripts` directory with its own Python interpreter and pip installer.

### 3. **Activate the Virtual Environment**
   After creating the environment, activate it:
   - **On macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
   - **On Windows**:
     ```bash
     .\venv\Scripts\activate
     ```

   Once activated, you’ll see `(venv)` or your environment name in the terminal prompt, indicating you’re working in the virtual environment.

### 4. **Installing Packages**
   After activation, any package installed with `pip` is installed only within this environment:
   ```bash
   pip install requests
   ```

   You can freeze the current list of dependencies into a `requirements.txt` file:
   ```bash
   pip freeze > requirements.txt
   ```

### 5. **Deactivating the Virtual Environment**
   To exit the virtual environment and return to your system Python, simply run:
   ```bash
   deactivate
   ```

### 6. **Reproducing the Environment**
   To replicate the same environment on another machine:
   - Create and activate a new `virtualenv`.
   - Install the dependencies listed in `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

### Summary of Virtualenv Commands
   - **Create Virtual Environment**: `virtualenv venv`
   - **Activate Environment**: `source venv/bin/activate` (macOS/Linux) or `.\venv\Scripts\activate` (Windows)
   - **Deactivate Environment**: `deactivate`
   - **Install Packages**: `pip install package_name`
   - **Save Dependencies**: `pip freeze > requirements.txt`
   - **Install from Requirements**: `pip install -r requirements.txt`

### Pipenv vs Virtualenv
- **Pipenv** handles both environment and dependency management, making it ideal for complex projects.
- **Virtualenv** is lightweight and fast, but requires additional tools like `pip` and `requirements.txt` to manage dependencies.

If you want environment management with simpler tooling, go with `virtualenv`. If you need both environment and dependency management, `Pipenv` may be more convenient.