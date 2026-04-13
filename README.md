# remarcableProj

A Django project that models products, categories, and tags with search and filter functionality.

## Models

- **Product** has a title, description, and price. It has a ForeignKey to Category (many-to-one — a product belongs to one category) and a ManyToManyField with Tag (a product can have multiple tags).
- **Category** and **Tag** each have a title field.

## Setup

1. Clone the repo
    ```bash
    git clone <your-repo-url>
    cd remarcableProj
    ```

2. Create and activate a virtual environment
    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    source venv/bin/activate  # Mac/Linux
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Run the server
    ```bash
    python manage.py runserver
    ```

5. Go to `http://127.0.0.1:8000/`

## Notes

- The database is included with pre-populated sample data (20 products, 5 categories, 10 tags) so no migrations or data entry is needed.
- To access the admin panel at `http://127.0.0.1:8000/admin`, create a superuser with `python manage.py createsuperuser`.

## AI Usage

AI assistance was used in the following areas:
- Generating sample data entries for the database
- Initial HTML template structure, which was then modified to implement checkbox-based multi-tag filtering and selected-state persistence for the category dropdown
