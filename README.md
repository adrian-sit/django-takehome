# Product Catalog

**A Django web application for browsing and filtering a sample catalog of manufacturing and engineering products. The application supports category and tag filtering, configurable matching conditions, and description-based search.**

## Setup
Requires Python 3.11+. Create a virtual environment, install the project dependencies from pyproject.toml, initialize the SQLite database, and load the provided sample dataset. In Powershell, run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e .
python manage.py migrate
python manage.py loaddata products
```

Start the Django development server:

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ to access the product catalog. 
The sample dataset is stored in catalog/fixtures/products.json and contains 7 categories, 12 tags, and 25 products. No manual data entry is required during setup.

Press Ctrl+C to stop the server. To exit the virtual environment, run:

```powershell
deactivate
```

## Use Instructions
1. Open the product catalog in your browser. All products are displayed by default.
2. Optionally, select one or more categories to filter products by category.
3. Optionally, select one or more tags, then choose whether products must match any or all selected tags.
4. Choose whether products must match both the category and tag filters, or match either filter group.
5. Optionally, enter keywords in the description search field.
6. Click Apply Filters to display matching products.
7. Click Clear Filters to reset all selections and display all products.

## Assumptions and Addition Notes
- Categories have a one-to-many relationship with products, while tags have a many-to-many relationship.
- Since each product belongs to exactly one category, multiple selected categories use "match any"  logic.
- No selections on either categories or tags means no filters are applied on the respective group.
- Combining category and tag filters are only active when both groups have selections.
- All available options are displayed as category and tags filtering options.
- Description search is combined with filters with "match all" logic (results match both the filters and search query).
- Description search has no typo/fuzzy tolerance, and includes partial match.

## AI Use
AI assistance was used to generate initial scaffolding for views.py and product_list.html. AI-generated code is identified in comments within the respective files as required.
