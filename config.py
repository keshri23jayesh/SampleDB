from typing import Dict, Any

from pydantic import BaseModel


class DataObject(BaseModel):
    data: Dict[str, Any]
