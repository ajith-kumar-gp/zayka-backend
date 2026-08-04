import copy
import json
import os
import tempfile
import threading
from datetime import datetime, timezone
from pathlib import Path

from .seed import SEED_CATEGORIES, SEED_FOODS


class JsonStore:
    def __init__(self, path=None):
        backend_root = Path(__file__).resolve().parents[2]
        default_path = backend_root / "src" / "data" / "zayka_data.json"
        self.path = Path(path or os.getenv("DATA_FILE", default_path)).resolve()
        self._lock = threading.Lock()

    def ensure(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.write(self._seed_data())

    def read(self):
        self.ensure()
        with self._lock:
            with self.path.open("r", encoding="utf-8") as data_file:
                return json.load(data_file)

    def write(self, data):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self._lock:
            fd, temp_path = tempfile.mkstemp(
                dir=self.path.parent,
                prefix=f"{self.path.stem}-",
                suffix=".tmp",
                text=True,
            )
            try:
                with os.fdopen(fd, "w", encoding="utf-8") as temp_file:
                    json.dump(data, temp_file, indent=2)
                    temp_file.write("\n")
                os.replace(temp_path, self.path)
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)

    def update(self, updater):
        self.ensure()
        with self._lock:
            with self.path.open("r", encoding="utf-8") as data_file:
                data = json.load(data_file)
            result = updater(data)
            fd, temp_path = tempfile.mkstemp(
                dir=self.path.parent,
                prefix=f"{self.path.stem}-",
                suffix=".tmp",
                text=True,
            )
            try:
                with os.fdopen(fd, "w", encoding="utf-8") as temp_file:
                    json.dump(data, temp_file, indent=2)
                    temp_file.write("\n")
                os.replace(temp_path, self.path)
            finally:
                if os.path.exists(temp_path):
                    os.remove(temp_path)
            return result

    def _seed_data(self):
        return {
            "meta": {
                "created_at": datetime.now(timezone.utc).isoformat(),
                "storage": "json",
            },
            "categories": copy.deepcopy(SEED_CATEGORIES),
            "foods": copy.deepcopy(SEED_FOODS),
            "users": [],
            "orders": [],
            "carts": {},
        }


store = JsonStore()
