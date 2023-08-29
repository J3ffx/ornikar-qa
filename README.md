# Ornikar QA Engineer Technical Test - Fanfan

This repository contains an automated UI and API testing framework developed using Behave and Allure for generating test reports. The framework is designed to test ornikar insurance website and a dummy API.

## Getting Started

These instructions will help you set up and run the automated tests on your local machine.

### Prerequisites

- Python 3.x
- OpenJDK (for Allure reports)
- Chrome WebDriver (for Selenium tests)

### Installation

1. **Clone the Repository:**

   Clone this repository to your local machine:

   ```bash
   git clone [repository_url]
   cd ornikar-qa
   ```

2. **Set Up Virtual Environment:**

   Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   Install the required Python packages:

   ```bash
   pip install selenium behave allure-behave requests
   ```

4. **Install OpenJDK (for Allure reports):**

   Download and install OpenJDK for your operating system. Set `JAVA_HOME` and update the `PATH` environment variable as needed.

5. **Download Chrome WebDriver:**

   Download the appropriate Chrome WebDriver executable and place it in a directory included in your system's `PATH`.

### Running Tests

1. **Run Behave Tests:**

   To run the Behave tests, execute the following command:

   ```bash
   behave --format=allure_behave.formatter:AllureFormatter -o results
   ```

2. **Generate Allure Report:**

   After the tests are complete, generate the Allure report:

   ```bash
   allure serve results
   ```

   This will launch a local web server displaying the interactive test report.

## Project Structure

- `features/`: Contains feature files written in Gherkin syntax.
- `features/steps/`: Contains step definitions for the feature files.
- `features/support/`: Contains supporting code, including Page Objects and environment.
- `results/`: Contains test results.
