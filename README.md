# ESGAR 2025 PSC MR Reporting Module (Colangitis Esclerosante Primaria)

[![Online Demo](https://img.shields.io/badge/Demo-Online%20App-0284c7?style=flat-square&logo=github)](https://guillemcasamayor.github.io/esgar-psc-mri/)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-blue.svg?style=flat-square)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

> 🌐 **Acceso directo online:** **[https://guillemcasamayor.github.io/esgar-psc-mri/](https://guillemcasamayor.github.io/esgar-psc-mri/)**

Módulo interactivo de informe radiológico estructurado para **Resonancia Magnética y Colangio-RM en pacientes con Colangitis Esclerosante Primaria (CEP / PSC)**, desarrollado en base al consenso oficial de la **European Society of Gastrointestinal and Abdominal Radiology (ESGAR)**:

> **Referencia oficial:**  
> Ippolito, D., et al. *ESGAR consensus statement on MR imaging in primary sclerosing cholangitis*. **European Radiology** (2025) 35:6495–6506.  
> DOI: [10.1007/s00330-025-11583-4](https://doi.org/10.1007/s00330-025-11583-4)

---

## 👥 Autoría y Equipo del Proyecto
* **Dr. Guillem Casamayor** (Radiología & Desarrollo IA / Informes Estructurados)
* **Dr. Oriol Busquets** (Radiología Abdominal / Digestiva)

---

## ⚖️ Licencia y Distribución
Este software y módulo de informe estructurado se distribuye bajo la licencia:  
**[Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)**

* **Atribución (BY):** Debe darse el crédito adecuado a los autores (**Dr. Guillem Casamayor & Dr. Oriol Busquets**) y citar la publicación original del Consenso ESGAR 2025.
* **No Comercial (NC):** No se permite el uso del material con fines comerciales. Uso libre para asistencia médica, docencia e investigación clínica sin ánimo de lucro.
* **Compartir Igual (SA):** Si se remezcla, transforma o crea a partir del material, debe distribuirse bajo la misma licencia.

---

## 🎯 Características Principales

1. **Alineación Estricta con el Consenso ESGAR 2025:**
   * Basado en la **Figura 1** (*Structured MR Reporting Template*) y las 23 declaraciones con acuerdo unánime del panel internacional de expertos.
2. **Arquitectura Zero-Dependency (Single-File):**
   * Archivo único `index.html` con HTML5 semántico, CSS3 moderno y Vanilla JavaScript.
   * Totalmente funcional en modo offline y ejecutable directamente en cualquier navegador web o estación de trabajo PACS.
3. **Soporte Trilingüe Completo:**
   * **Español (`es`)**, **Català (`ca`)** e **Inglés (`en`)**.
   * Traducción en tiempo real tanto de la interfaz gráfica como del informe generado.
4. **Diseño Visual de Alta Fidelidad y Ergonomía:**
   * Tipografía moderna **Ubuntu** (Google Fonts).
   * Modo Claro y Modo Oscuro conmutables al instante.
   * **Cabecera compacta de perfil bajo (44px):** Todo en una sola línea (Título, Referencia de consenso, Autoría y Licencia CC).
   * **Panel Split-View Redimensionable:** Divisor interactivo arrastrable para regular el ancho de la lista de verificación y del informe preview al gusto del usuario, con persistencia en `localStorage`.
5. **Protocolo Técnico Optimizado (Consenso ESGAR):**
   * Registro de campo (1.5T / 3.0T) y ayuno (≥ 4h).
   * **Agente antiperistáltico / espasmolítico:** Butilescopolamina (Buscapina), Glucagón, No administrado o Contraindicado.
   * Secuencias estándar ESGAR (T2WI, T1WI Dixon, Colangio-RM, DWI, T1 dinámico, Fase HBA) más opción de **Otras secuencias** con campo de texto libre editable.
6. **Calculadora Pronóstica Integrada (Score ANALI):**
   * Cálculo reactivo automático del **ANALI Score sin Gadolinio** (0–3 puntos) y **ANALI Score con Gadolinio** (0–5 puntos) en base a los hallazgos seleccionados (dilatación intrahepática, dismorfia, signos de HTP y heterogeneidad de captación).
   * Incorporación de las recomendaciones de prudencia clínica acordadas por la ESGAR.
6. **Alertas de Estenosis Dominante y Cribado Neoplásico:**
   * Identificación automática de estenosis biliares de alto grado ($\ge 75\%$) con advertencia de necesidad de correlación con CA 19-9, cepillado citológico y valoración endoscópica.
   * Recomendaciones estandarizadas de intervalo de seguimiento (control anual con Colangio-RM + RM con contraste).
7. **Herramientas de Exportación:**
   * Botón de **Copiar al Portapapeles** con notificación toast.
   * Botón de **Guardar / Descargar** informe en formato texto (`.txt`).
   * Botón de **Reiniciar formulario**.

---

## 📂 Estructura de Archivos del Proyecto

```text
05_Proyectos/esgar-psc-mri/
├── index.html                   # Módulo web interactivo de informe estructurado
├── README.md                    # Documentación técnica y clínica del proyecto
├── PSC - ESGAR consensus.pdf    # Guía oficial del consenso ESGAR 2025 (PDF)
└── esgar_psc_template_fig1.png  # Extracción en alta resolución de la plantilla oficial
```

---

## ☁️ Sincronización en Google Drive

El proyecto cuenta con carpeta oficial sincronizada en la unidad de Google Drive:
* **Ubicación en Drive:** `05_Proyectos / esgar_psc_mri`
* **ID de carpeta:** `12MfxMAUUju7a7KH2HP1jS7rTnh_Ogj-I`
* **Enlace web:** [Abrir carpeta en Google Drive](https://drive.google.com/drive/folders/12MfxMAUUju7a7KH2HP1jS7rTnh_Ogj-I)
