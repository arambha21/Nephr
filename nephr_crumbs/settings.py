from nephr.settings import TEMPLATES

TEMPLATES[0]["OPTIONS"]["context_processors"].append(
    "nephr_crumbs.context_processors.breadcrumbs",
)
