from typing import Optional

from pydantic import BaseModel


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int


cursos = [
    Curso(id=1, titulo="Programação para Leigos", aulas=42, horas=85),
    Curso(id=1, titulo="Algoritmos e lógica de programação", aulas=72, horas=41),
]