from typing import Optional

from pydantic import BaseModel, validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator("titulo")
    def validar_titulo(cls, value):
        # Validação 1
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError("O título deve ter pelo menos 3 palavras.")
        # Validação 2
        if value.islower():
            raise ValueError("O título deve ser capitalizado")
        return value


cursos = [
    Curso(id=1, titulo="Programação para Leigos", aulas=42, horas=85),
    Curso(id=1, titulo="Algoritmos e lógica de programação", aulas=72, horas=41),
]