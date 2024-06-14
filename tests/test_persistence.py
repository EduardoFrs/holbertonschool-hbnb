import unittest
import sys
import os
from ..Persistence.repository import DataManager
from unittest.mock import MagicMock, patch
import json
from unittest import mock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestDataManager(unittest.TestCase):

  @patch('os.path.join')
  @patch('json.dump')
  def test_save_data(self, mock_json_dump, mock_os_path_join):
    # Mock data
    data_path = "data/"
    entity_type = "user"
    entity_data = {"id": 1, "name": "Emmanuel Macron"}
    mock_os_path_join.return_value = f"{data_path}{entity_type}.json"

    data_manager = DataManager()
    data_manager._data = {entity_type: entity_data}

    # Call save_data
    data_manager.save_data()

    # Assertions - checks file path and data passed to json.dump
    mock_os_path_join.assert_called_once_with(data_path, f"{entity_type}.json")
    mock_json_dump.assert_called_once_with(entity_data, mock.ANY, indent=4)

  @patch('builtins.open')
  @patch('json.load')
  def test_load_data(self, mock_json_load, mock_open):
    # Mock data
    data_path = "data/"
    entity_type = "user"
    entity_data = {"id": 1, "name": "Emmanuel Macron"}
    mock_file = MagicMock()
    mock_file.read.return_value = json.dumps(entity_data)
    mock_open.return_value = mock_file

    # Create DataManager instance
    data_manager = DataManager()
    data_manager._data_path = data_path

    # Call _load_data
    data_manager._load_data()

    # Assertions - verify file open and json.load calls
    mock_open.assert_called_once_with(f"{data_path}{entity_type}.json", "r", encoding="utf-8")
    mock_json_load.assert_called_once_with(mock_file.read())
    self.assertEqual(data_manager._data[entity_type], entity_data)

  def test_save_entity(self):
    # Mock entity object
    entity_type = "user"
    entity_id = 1
    entity_data = {"name": "Jacques Chirac"}
    entity = MagicMock()
    entity.__name__ = entity_type
    entity.id = entity_id
    setattr(entity, "id", entity_id)  # Simulate attribute access

    # Create DataManager instance
    data_manager = DataManager()

    # Call save
    data_manager.save(entity)

    # Assertions - verify data update and _save_data call
    self.assertEqual(data_manager._data[entity_type][entity_id], entity_data)
    data_manager._save_data.assert_called_once()

  @patch('DataManager._save_data')
  def test_update_entity(self, mock_save_data):
    # Mock entity object
    entity_type = "user"
    entity_id = 1
    entity_data = {"name": "Jane Doe"}
    entity = MagicMock()
    entity.__name__ = entity_type
    entity.id = entity_id
    setattr(entity, "id", entity_id)  # Simulate attribute access

    # Create DataManager instance with loaded data
    data_manager = DataManager()
    data_manager._data = {entity_type: {entity_id: {"name": "Old Name"}}}

    # Call update
    data_manager.update(entity)

    # Assertions - verify data update and _save_data call
    self.assertEqual(data_manager._data[entity_type][entity_id], entity_data)
    mock_save_data.assert_called_once()

  def test_update_entity_not_found(self):
    # Mock entity object
    entity_type = "user"
    entity_id = 1
    entity_data = {"name": "Jane Doe"}
    entity = MagicMock()
    entity.__name__ = entity_type
