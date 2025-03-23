![Project Logo](Project_Addax/static/images/combined_logo.png)

# Project Addax

Project Addax is a Flask-based web application that provides dashboards and analytical tools for various countries in the Sahel region. The application includes individual dashboards for each country as well as a Sahel-wide comparison dashboard.

## Directory Structure
```
Project_Addax/
├── country_dashboards/
│   ├── mauritania/
│   │   ├── init.py        # Initializes the Mauritania dashboard package
│   │   ├── routes.py          # Contains the routes/endpoints for Mauritania’s dashboard
│   │   └── templates/
│   │       └── mauritania/
│   │           └── detail.html  # The detailed dashboard view for Mauritania
│   ├── mali/
│   │   ├── init.py        # Initializes the Mali dashboard package
│   │   ├── routes.py          # Contains the routes/endpoints for Mali’s dashboard
│   │   └── templates/
│   │       └── mali/
│   │           └── detail.html  # The detailed dashboard view for Mali
│   ├── niger/
│   │   ├── init.py        # Initializes the Niger dashboard package
│   │   ├── routes.py          # Contains the routes/endpoints for Niger’s dashboard
│   │   └── templates/
│   │       └── niger/
│   │           └── detail.html  # The detailed dashboard view for Niger
│   ├── chad/
│   │   ├── init.py        # Initializes the Chad dashboard package
│   │   ├── routes.py          # Contains the routes/endpoints for Chad’s dashboard
│   │   └── templates/
│   │       └── chad/
│   │           └── detail.html  # The detailed dashboard view for Chad
│   ├── burkinafaso/
│   │   ├── init.py        # Initializes the Burkina Faso dashboard package
│   │   ├── routes.py          # Contains the routes/endpoints for Burkina Faso’s dashboard
│   │   └── templates/
│   │       └── burkinafaso/
│   │           └── detail.html  # The detailed dashboard view for Burkina Faso
│   ├── senegal/
│   │   ├── init.py        # Initializes the Senegal dashboard package
│   │   ├── routes.py          # Contains the routes/endpoints for Senegal’s dashboard
│   │   └── templates/
│   │       └── senegal/
│   │           └── detail.html  # The detailed dashboard view for Senegal
│   └── sudan/
│       ├── init.py        # Initializes the Sudan dashboard package
│       ├── routes.py          # Contains the routes/endpoints for Sudan’s dashboard
│       └── templates/
│           └── sudan/
│               └── detail.html  # The detailed dashboard view for Sudan
├── templates/
│   ├── homepage.html         # The landing page template
│   ├── dashboard.html        # The main dashboard template (country map, Sahel-wide analysis button)
│   ├── analysis.html         # Template for additional analytical views
│   └── sahel_comparison.html # Template for Sahel-wide comparison dashboard
├── app.py                    # Main application file that initializes Flask and registers blueprints/routes
└── README.md                 # This file
```
## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/Project_Addax.git
    cd Project_Addax
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python3 -m venv addax_env
    source addax_env/bin/activate  # On Windows: addax_env\Scripts\activate
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Initialize Earth Engine:**

    Ensure you have access to [Google Earth Engine](https://earthengine.google.com/) and run the following in Python:
    
    ```python
    import ee
    ee.Initialize()
    ```

## Running the Application

1. **Start the Flask application:**

    ```sh
    python app.py
    ```

2. **Open your web browser** and navigate to `http://127.0.0.1:5000/` to access the homepage.

3. **Navigation:**

   - **Dashboard:**  
     The dashboard page displays an interactive map with clickable countries. When a user clicks on a country, they are redirected to that country's detailed dashboard.

   - **Sahel Wide Analysis:**  
     On the dashboard, there is a "Sahel Wide Analysis" button (centered beneath the map) that redirects to the Sahel-wide comparison page (`/sahel_comparison`). This page provides a comparison of key indicators across all Sahel countries.

## Application Structure

- **app.py**  
  The main application file that initializes the Flask app and registers blueprints/routes for:
  - The homepage
  - The main dashboard
  - Each individual country dashboard
  - The Sahel-wide comparison page

- **country_dashboards/**  
  Contains subdirectories for each country dashboard. Each country's directory includes:
  - `__init__.py`: Initializes the country's dashboard package.
  - `routes.py`: Contains the routes/endpoints for that country's dashboard.
  - `templates/[country_name]/detail.html`: The detailed dashboard view for that country.

- **templates/**  
  Contains global templates:
  - `homepage.html`: The landing page for the application.
  - `dashboard.html`: The main dashboard template with the interactive map and Sahel-wide analysis button.
  - `analysis.html`: Templates for additional analysis views.
  - `sahel_comparison.html`: The Sahel-wide comparison dashboard template, which includes a "Back to Dashboard" button.

- **static/**  
  Contains static assets such as:
  - `static/geojson/`: GeoJSON files for each country used for mapping administrative boundaries.
  - `static/css/style.css`: Global CSS styles.
  - `static/js/main.js`: Global JavaScript functions.

## Adding a New Country

To add a new country dashboard:

1. Create a new directory for the country under `country_dashboards/`.
2. Add an `__init__.py` file to initialize the package.
3. Create a `routes.py` file to define routes for the country's dashboard.
4. Create a `templates/[new_country]/detail.html` file for the detailed dashboard view.
5. Register the new blueprint in `app.py`.

## Sahel-Wide Comparison

The Sahel-wide comparison page is accessible via the "Sahel Wide Analysis" button on the dashboard. This page is defined in `templates/sahel_comparison.html` and provides a comparison of key indicators across all Sahel countries. It includes a "Back to Dashboard" button to allow users to navigate back to the main dashboard.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.