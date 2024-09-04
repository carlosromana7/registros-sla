from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta
from database import get_database
from fastapi import Response
from bson import ObjectId
import os

# Definición de la aplicación FastAPI
app = FastAPI()

# Configuración de archivos estáticos y plantillas
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))

# Modelo de datos para los eventos SLA
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
    tiempo_inactividad_no_planificada: float
    tiempo_inactividad_planificada: float

    @property
    def sli(self) -> float:
        """Calcular el SLI basado en la fórmula proporcionada."""
        tiempo_total = 370  # horas de operación
        tiempo_inactividad = self.tiempo_inactividad_no_planificada + self.tiempo_inactividad_planificada
        sli = ((tiempo_total - tiempo_inactividad) / tiempo_total) * 100
        return sli

    @property
    def sla_cumplido(self) -> bool:
        """Determinar si el SLA ha sido cumplido según el SLO de 98.4%."""
        slo = 98.4  # SLO en porcentaje
        return self.sli >= slo

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit")
async def submit_form(
    request: Request,
    fecha_reporte: str = Form(...),
    evento_programado: bool = Form(False),
    descripcion_evento: str = Form(...),
    tipo_problema: str = Form(...),
    proveedor: str = Form(...),
    empresa: str = Form(...),
    descripcion_problema: str = Form(...),
    acciones_tomadas: str = Form(...),
    inicio_evento: str = Form(...),
    fin_evento: str = Form(...),
    tiempo_inactividad_no_planificada: float = Form(0.0),
    tiempo_inactividad_planificada: float = Form(0.0)
):
    # Crear el evento SLA
    event = SLAEvent(
        fecha_reporte=datetime.strptime(fecha_reporte, "%Y-%m-%dT%H:%M"),
        evento_programado=evento_programado,
        descripcion_evento=descripcion_evento,
        tipo_problema=tipo_problema,
        proveedor=proveedor,
        empresa=empresa,
        descripcion_problema=descripcion_problema,
        acciones_tomadas=acciones_tomadas,
        inicio_evento=datetime.strptime(inicio_evento, "%Y-%m-%dT%H:%M"),
        fin_evento=datetime.strptime(fin_evento, "%Y-%m-%dT%H:%M"),
        tiempo_inactividad_no_planificada=tiempo_inactividad_no_planificada,
        tiempo_inactividad_planificada=tiempo_inactividad_planificada
    )

    # Insertar en la base de datos
    db = await get_database()
    result = await db.sla_events.insert_one(event.dict())

    if result.inserted_id:
        return templates.TemplateResponse("success.html", {"request": request})
    raise HTTPException(status_code=400, detail="Failed to create SLA event")

@app.get("/stats")
async def get_stats(request: Request):
    db = await get_database()
    total_eventos = await db.sla_events.count_documents({})
    eventos = await db.sla_events.find().to_list(length=total_eventos)

    if total_eventos == 0:
        return templates.TemplateResponse("stats.html", {
            "request": request,
            "total_eventos": 0,
            "sla_cumplido_count": 0,
            "sla_no_cumplido_count": 0,
            "sli_promedio": 0,
            "dias": []
        })

    # Calcula el número de días en el mes actual
    current_month = datetime.now().month
    current_year = datetime.now().year
    next_month = current_month % 12 + 1
    next_month_year = current_year if next_month > 1 else current_year + 1
    days_in_month = (datetime(next_month_year, next_month, 1) - timedelta(days=1)).day

    # Inicializa los contadores para cada día
    day_counts = {day: {'sla_cumplido_count': 0, 'sla_no_cumplido_count': 0} for day in range(1, days_in_month + 1)}

    # Recorre los eventos y cuenta los SLA cumplidos y no cumplidos por día
    sli_total = 0
    for evento in eventos:
        event = SLAEvent(**evento)  # Convierte el diccionario en una instancia de SLAEvent
        sli_total += event.sli
        day = event.fecha_reporte.day
        if event.sla_cumplido:
            day_counts[day]['sla_cumplido_count'] += 1
        else:
            day_counts[day]['sla_no_cumplido_count'] += 1

    # Formatea los datos para el gráfico
    dias = [
        {
            "dia": day,
            "mes": current_month,
            "sla_cumplido_count": day_counts[day]['sla_cumplido_count'],
            "sla_no_cumplido_count": day_counts[day]['sla_no_cumplido_count']
        }
        for day in range(1, days_in_month + 1)
    ]

    # Calcula el SLA promedio
    sli_promedio = sli_total / total_eventos if total_eventos > 0 else 0

    return templates.TemplateResponse("stats.html", {
        "request": request,
        "total_eventos": total_eventos,
        "sla_cumplido_count": sum(day['sla_cumplido_count'] for day in day_counts.values()),
        "sla_no_cumplido_count": sum(day['sla_no_cumplido_count'] for day in day_counts.values()),
        "sli_promedio": sli_promedio,
        "dias": dias
    })
@app.get("/registros")
async def ver_registros(request: Request):
    db = await get_database()
    eventos = await db.sla_events.find().to_list(length=None)
    return templates.TemplateResponse("registros.html", {"request": request, "eventos": eventos})

@app.delete("/eliminar/{id}")
async def eliminar_evento(id: str):
    db = await get_database()
    try:
        result = await db.sla_events.delete_one({"_id": ObjectId(id)})
        if result.deleted_count:
            return {"success": True}
        else:
            return {"success": False, "message": "No se encontró el evento"}
    except Exception as e:
        print(f"Error al eliminar evento: {str(e)}")
        return {"success": False, "message": str(e)}
@app.get("/trend-analysis")
async def trend_analysis(request: Request):
    db = await get_database()
    total_eventos = await db.sla_events.count_documents({})
    eventos = await db.sla_events.find().to_list(length=total_eventos)

    if total_eventos == 0:
        return templates.TemplateResponse("trend.analysis.html", {
            "request": request,
            "labels": [],
            "data": []
        })

    # Inicializa listas para almacenar los datos
    labels = []
    sli_promedios = []

    # Calcula los promedios de SLI por día
    sli_totales_por_dia = {}
    conteos_por_dia = {}

    for evento in eventos:
        event = SLAEvent(**evento)
        dia = event.fecha_reporte.day
        if dia not in sli_totales_por_dia:
            sli_totales_por_dia[dia] = 0
            conteos_por_dia[dia] = 0
        sli_totales_por_dia[dia] += event.sli
        conteos_por_dia[dia] += 1

    # Generar los datos para el gráfico
    for dia in range(1, 32):  # Asumiendo un mes con 31 días
        labels.append(f"Día {dia}")
        if dia in sli_totales_por_dia:
            sli_promedio = sli_totales_por_dia[dia] / conteos_por_dia[dia]
            sli_promedios.append(sli_promedio)
        else:
            sli_promedios.append(0)

    return templates.TemplateResponse("trend.analysis.html", {
        "request": request,
        "labels": labels,
        "data": sli_promedios
    })

