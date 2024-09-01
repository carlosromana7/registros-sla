from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SLAEvent(BaseModel):
    fecha_reporte: datetime
    evento_programado: bool
    descripcion_evento: str
    tipo_problema: str
    proveedor: str
    empresa: str
    descripcion_problema: str
    acciones_tomadas: str
    inicio_evento: datetime
    fin_evento: datetime
    tiempo_inactividad_no_planificada: float = 0.0  # Permitir 0 como valor por defecto
    tiempo_inactividad_planificada: float = 0.0  # Permitir 0 como valor por defecto

    @property
    def sli(self) -> float:
        # Asumiendo que el SLO es 98.4
        total_tiempo = 370
        tiempo_inactividad_total = self.tiempo_inactividad_no_planificada + self.tiempo_inactividad_planificada
        sli = ((total_tiempo - tiempo_inactividad_total) / total_tiempo) * 100
        return sli

    @property
    def sla_cumplido(self) -> bool:
        return self.sli >= 98.4  # Comparar con el SLO que es 98.4

    def calculate_metrics(self):
        # Este método puede ser utilizado para cualquier lógica adicional si es necesario
        pass

