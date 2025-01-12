"""A package to deploy SPARQL endpoint to serve local RDF files, machine learning models, or any other logic implemented in Python, using RDFLib and FastAPI."""

__version__ = "0.4.0"

from .sparql_router import SparqlRouter
from .sparql_endpoint import SparqlEndpoint
