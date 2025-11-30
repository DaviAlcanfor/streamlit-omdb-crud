"""Package initializer for the `components` package.

Expose commonly used symbols so imports like
`from components.page_config import pg_config` continue to work,
and make the folder a regular package for reliable imports.
"""
from .page_config import pg_config

__all__ = ["pg_config"]
