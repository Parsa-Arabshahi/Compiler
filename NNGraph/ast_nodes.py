from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple


# -----------------------------
# Model Section
# -----------------------------

@dataclass
class Model:
    name: str
    input_name: str
    input_shape: Tuple[int, ...]
    output_name: str


# -----------------------------
# Graph Section
# -----------------------------

@dataclass
class Node:
    id: str
    layer_type: str
    params: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Edge:
    source: str
    target: str
    label: Optional[str] = None


# -----------------------------
# Config Section
# -----------------------------

@dataclass
class Config:
    values: Dict[str, Any] = field(default_factory=dict)


# -----------------------------
# Whole Program
# -----------------------------

@dataclass
class Program:
    model: Model
    nodes: List[Node]
    edges: List[Edge]
    config: Optional[Config] = None