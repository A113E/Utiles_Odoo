Mapeo de Procesos de una PYME Real: "Ferretería El Constructor"

1. Contexto del Ejercicio
   IMPORTANTE: No vamos a escribir código. No vamos a instalar nada.
   Vamos a PENSAR como consultores Odoo. Este es el paso MÁS IMPORTANTE que muchos desarrolladores saltan.

Regla de oro: "Si no entiendes el negocio, no puedes automatizarlo bien"

2. Presentación del Caso
   "Ferretería El Constructor" - Fundada 1998, 15 empleados

Situación actual:

Todo en papeles y Excel

Dueño: Don Roberto (62 años, sabe del negocio, no de tecnología)

Problemas diarios: "No sé qué tengo", "No sé qué debo", "No sé cuánto gano"

Tu rol: Eres consultor Odoo, primera visita, presupuesto $5,000 USD

3. Paso 1: Entrevista de Descubrimiento
   Preguntas que HARÁS (y por qué):
1. "Don Roberto, cuénteme un día normal en la ferretería"

Objetivo: Entender flujo natural, no el teórico

2. "¿Qué es lo que más tiempo le quita cada día?"

Objetivo: Identificar puntos de dolor PRIORITARIOS

3. "Si tuviera una varita mágica, ¿qué 3 problemas solucionaría primero?"

Objetivo: Expectativas del cliente vs realidad

4. "¿Cómo sabe actualmente si tuvo ganancias este mes?"

Objetivo: Entender proceso de reporting actual

4. Paso 2: Observación en Campo (Tu Visita)
   Lo que observas:

Área de Ventas:
text
8:00 AM - Cliente llega pide "10 bolsas de cemento"
Vendedor: Revisa cuaderno amarillo → "Sí hay"
Cliente: "¿Precio?"
Vendedor: Llama a almacén → Espera 2 minutos → "$150 cada una"
Cliente: "Llévemelo"
Vendedor: Hace ticket manual en máquina de 3 copias
Copia 1: Cliente
Copia 2: Almacén  
Copia 3: Caja
Problemas identificados:

Información desactualizada (cuaderno vs realidad)

Comunicación lenta (llamadas internas)

Papel, papel, papel

Área de Almacén:
text
10:00 AM - Almacenista recibe ticket de ventas
Busca cemento → Solo hay 7 bolsas
Va a ventas: "Solo hay 7"
Vendedor: "Pero dije que había"
Cliente enojado se va sin comprar

Problemas críticos:

Inventario inexacto = Ventas perdidas

No hay registro de por qué faltan 3 bolsas

Responsabilidades difusas

Área de Compras/Proveedores:
text
2:00 PM - Don Roberto: "Hay que comprar más cemento"
Revisa cuaderno de proveedores → Llama a 3
Pide precios → Anota en hoja suelta
Ordena a proveedor más barato → No registra pedido
Problemas:

No hay historial de compras

No se comparan proveedores sistemáticamente

Pedidos no rastreados

5. Paso 3: Mapeo de Procesos AS-IS (Cómo es AHORA)
   Usaremos diagramas simples (papel es suficiente):

Proceso de Venta ACTUAL:

[Cliente llega] → [Vendedor busca en cuaderno] → [Llama almacén]
↓
[Da precio] → [Hace ticket manual] → [Cliente paga en caja]
↓
[Almacén recibe ticket] → [Busca producto] → ¿Hay? → Sí → [Entrega]
↓ ↓
No → [Cliente enojado]

Proceso de Compra ACTUAL:
[Producto bajo mínimo] → [Don Roberto decide comprar] → [Llama proveedores]
↓
[Compara precios en hoja] → [Ordena verbalmente] → [Recibe producto]
↓
[Paga cuando llega factura] → [No archiva sistemáticamente]

6. Paso 4: Identificación de Problemas Clave
   Vamos a categorizar (esto es lo que venderás al cliente):

Categoría A: Pérdida Directa de Dinero
Ventas perdidas por inventario inexacto (cliente se va)

Ejemplo real: 3-5 ventas perdidas/día × $100 promedio = $500/día

Impacto anual: $500 × 300 días = $150,000 potencial

Compras no optimizadas (paga más de lo necesario)

Sin historial: No sabe qué proveedor es mejor

Impacto: 10-15% sobrecosto estimado

Categoría B: Pérdida de Tiempo
Comunicación interna ineficiente

Tiempo perdido: 2-3 minutos/consulta × 50 consultas/día = 2.5 horas/día

Impacto: 2.5h × $15/hora × 300 días = $11,250 anual

Búsqueda de información

Ejemplo: "¿Cuánto vendimos de X?" → 30 minutos buscar papeles

Categoría C: Riesgos
Errores humanos (precios mal anotados, cantidades incorrectas)

Falta de trazabilidad (¿quién? ¿cuándo? ¿por qué?)

Dependencia de personas (si Don Roberto falta, nadie sabe)

7. Paso 5: Propuesta de Solución Odoo
   AHORA pensamos en módulos Odoo (pero sin detalles técnicos):

Fase 1: Cimientos (Mes 1-2)
text

1. Inventario (stock)

   - Saber QUÉ hay en tiempo real
   - Niveles mínimos de reposición automáticos

2. Ventas (sale)
   - Precios centralizados
   - Ver disponibilidad inmediata
   - Tickets/facturas automáticos
     Fase 2: Optimización (Mes 3-4)
     text
3. Compras (purchase)

   - Historial de proveedores
   - Órdenes de compra rastreables
   - Comparación de precios

4. Contabilidad (account)
   - Saber ganancias/pérdidas
   - Conciliación bancaria
     Fase 3: Crecimiento (Mes 5-6)
     text
5. Punto de Venta (pos)

   - Para venta directa en tienda
   - Más rápido que tickets manuales

6. Sitio Web (website)
   - Ventas online (opcional)

---

8. Paso 6: Beneficios Cuantificados
   Presentación para Don Roberto (en su idioma):

Lo que DEJA de perder:
Ventas perdidas: De $150,000 a ~$30,000 (80% reducción)

Tiempo perdido: Recupera 3 horas/día = 750 horas/año

Errores de precio: De 5-7 errores/semana a 0-1

Lo que GANA:
Información para decidir:

"¿Qué productos venden más?"

"¿Qué proveedor es mejor?"

"¿Qué empleado vende más?"

Crecimiento controlado:

De 15 a 30 empleados sin colapsar

--

9. Paso 7: Plan de Implementación Realista
   NO prometas magia:

Semana 1-2: Análisis detallado
Mapeo completo de productos (¿1,000? ¿5,000?)

Entrenamiento básico a 2-3 personas clave

Mes 1: Inventario + Ventas básico
Migración de productos a Odoo

Uso PARALELO (papel + sistema)

Mes 2: Compras integradas
Proveedores en sistema

Primeras órdenes de compra digitales

Mes 3: Contabilidad y abandono del papel
Todo digital

Papel solo como backup

10. Paso 8: Consideraciones Especiales
    Problemas únicos de ferretería:

Productos similares, diferentes marcas (cemento Cruz Azul vs Cemex)

Unidades de medida (kilos, litros, piezas, metros)

Caducidad (algunos productos químicos)

Pesos y volúmenes (importante para logística)

Propuesta Odoo:

Campos personalizados: marca, unidad_medida, peso, caducidad

Categorías inteligentes: construcción, electricidad, plomería

Atributos: tamaño, color, material
