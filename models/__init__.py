#!/usr/bin/python3
"""
creates a single instance of FileStorage for use
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
