import os

target_dir = r"C:\Users\gcasamayor\Downloads\05_Proyectos\esgar-psc-mri"
os.makedirs(target_dir, exist_ok=True)
target_file = os.path.join(target_dir, "index.html")

html_content = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ESGAR 2025 PSC MR Reporting Module</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #f4f6f9;
            --surface-color: #ffffff;
            --text-color: #2c3e50;
            --text-secondary: #607274;
            --title-color: #1a252f;
            --border-color: #dcdfe6;
            --panel-bg: #ffffff;
            --section-header-bg: #edf2f7;
            --accent-color: #0284c7;
            --accent-hover: #0369a1;
            --accent-light: #e0f2fe;
            --accent-border: #38bdf8;
            --danger-bg: #fee2e2;
            --danger-text: #991b1b;
            --danger-border: #f87171;
            --warning-bg: #fef3c7;
            --warning-text: #92400e;
            --warning-border: #fcd34d;
            --success-bg: #dcfce7;
            --success-text: #166534;
            --success-border: #86efac;
            --badge-bg: #e2e8f0;
            --badge-text: #334155;
            --code-bg: #f8fafc;
            --input-bg: #ffffff;
            --shadow: 0 4px 6px -1px rgba(0,0,0,0.07), 0 2px 4px -2px rgba(0,0,0,0.05);
            --shadow-md: 0 10px 15px -3px rgba(0,0,0,0.08), 0 4px 6px -4px rgba(0,0,0,0.04);
        }

        [data-theme="dark"] {
            --bg-color: #0f172a;
            --surface-color: #1e293b;
            --text-color: #f1f5f9;
            --text-secondary: #94a3b8;
            --title-color: #38bdf8;
            --border-color: #334155;
            --panel-bg: #1e293b;
            --section-header-bg: #1e293b;
            --accent-color: #38bdf8;
            --accent-hover: #0ea5e9;
            --accent-light: #082f49;
            --accent-border: #0284c7;
            --danger-bg: #450a0a;
            --danger-text: #fca5a5;
            --danger-border: #b91c1c;
            --warning-bg: #451a03;
            --warning-text: #fde68a;
            --warning-border: #b45309;
            --success-bg: #052e16;
            --success-text: #86efac;
            --success-border: #15803d;
            --badge-bg: #334155;
            --badge-text: #cbd5e1;
            --code-bg: #0b1120;
            --input-bg: #0f172a;
            --shadow: 0 4px 6px -1px rgba(0,0,0,0.4);
            --shadow-md: 0 10px 15px -3px rgba(0,0,0,0.5);
        }

        * {
            box-sizing: border-box;
            font-family: 'Ubuntu', sans-serif;
            margin: 0;
            padding: 0;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            transition: background-color 0.25s ease, color 0.25s ease;
            min-height: 100vh;
        }

        header {
            background-color: var(--surface-color);
            padding: 14px 28px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border-color);
            box-shadow: var(--shadow);
            position: sticky;
            top: 0;
            z-index: 50;
        }

        .header-title-box {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .header-badge {
            background-color: var(--accent-color);
            color: #ffffff;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 4px 8px;
            border-radius: 4px;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }

        h1 {
            font-size: 1.25rem;
            color: var(--title-color);
            font-weight: 700;
        }

        .header-subtitle {
            font-size: 0.78rem;
            color: var(--text-secondary);
            margin-top: 2px;
        }

        .header-controls {
            display: flex;
            gap: 12px;
            align-items: center;
        }

        select, button {
            padding: 7px 12px;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            background-color: var(--input-bg);
            color: var(--text-color);
            font-size: 0.88rem;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        button:hover {
            border-color: var(--accent-color);
            color: var(--accent-color);
        }

        button.btn-primary {
            background-color: var(--accent-color);
            color: #ffffff;
            border-color: var(--accent-color);
            font-weight: 500;
        }

        button.btn-primary:hover {
            background-color: var(--accent-hover);
            color: #ffffff;
        }

        .layout-container {
            display: grid;
            grid-template-columns: 1.85fr 1.15fr;
            min-height: calc(100vh - 65px);
            max-width: 1920px;
            margin: 0 auto;
        }

        @media (max-width: 1200px) {
            .layout-container {
                grid-template-columns: 1fr;
            }
        }

        .form-column {
            padding: 24px 32px 60px;
            overflow-y: auto;
            max-height: calc(100vh - 65px);
            border-right: 1px solid var(--border-color);
        }

        .report-column {
            padding: 24px 28px;
            background-color: var(--surface-color);
            display: flex;
            flex-direction: column;
            gap: 16px;
            max-height: calc(100vh - 65px);
            position: sticky;
            top: 65px;
        }

        .card-section {
            background-color: var(--panel-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: var(--shadow);
            overflow: hidden;
            transition: border-color 0.2s ease;
        }

        .card-section:hover {
            border-color: var(--accent-border);
        }

        .section-header {
            background-color: var(--section-header-bg);
            padding: 10px 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border-color);
        }

        .section-header h2 {
            font-size: 0.98rem;
            font-weight: 700;
            color: var(--title-color);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .section-body {
            padding: 16px 20px;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .field-row {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .field-label {
            font-size: 0.86rem;
            font-weight: 600;
            color: var(--text-color);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .radio-group, .checkbox-group {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .radio-card {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 12px;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            background-color: var(--input-bg);
            font-size: 0.85rem;
            cursor: pointer;
            user-select: none;
            transition: all 0.15s ease;
        }

        .radio-card input {
            cursor: pointer;
            accent-color: var(--accent-color);
        }

        .radio-card:hover {
            border-color: var(--accent-color);
        }

        .radio-card.active {
            border-color: var(--accent-color);
            background-color: var(--accent-light);
            font-weight: 500;
        }

        .input-inline {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }

        input[type="text"], input[type="number"], select.form-select {
            padding: 6px 10px;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            background-color: var(--input-bg);
            color: var(--text-color);
            font-size: 0.86rem;
        }

        input[type="number"] {
            width: 90px;
        }

        .conditional-box {
            display: none;
            padding: 12px 14px;
            background-color: var(--bg-color);
            border-left: 3px solid var(--accent-color);
            border-radius: 0 6px 6px 0;
            margin-top: 4px;
            gap: 12px;
            flex-direction: column;
        }

        .conditional-box.visible {
            display: flex;
        }

        .notice-box {
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 0.8rem;
            line-height: 1.4;
            display: flex;
            align-items: flex-start;
            gap: 8px;
        }

        .notice-info {
            background-color: var(--accent-light);
            color: var(--accent-color);
            border: 1px solid var(--accent-border);
        }

        .notice-warning {
            background-color: var(--warning-bg);
            color: var(--warning-text);
            border: 1px solid var(--warning-border);
        }

        .notice-danger {
            background-color: var(--danger-bg);
            color: var(--danger-text);
            border: 1px solid var(--danger-border);
            font-weight: 500;
        }

        .anali-score-card {
            background-color: var(--panel-bg);
            border: 2px solid var(--accent-color);
            border-radius: 8px;
            padding: 14px 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 10px;
        }

        .anali-score-val {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--accent-color);
        }

        .anali-risk-tag {
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.82rem;
            font-weight: 700;
            text-transform: uppercase;
        }

        .risk-low {
            background-color: var(--success-bg);
            color: var(--success-text);
            border: 1px solid var(--success-border);
        }

        .risk-intermediate {
            background-color: var(--warning-bg);
            color: var(--warning-text);
            border: 1px solid var(--warning-border);
        }

        .risk-high {
            background-color: var(--danger-bg);
            color: var(--danger-text);
            border: 1px solid var(--danger-border);
        }

        /* Report View */
        .report-header-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .report-header-row h3 {
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--title-color);
        }

        .report-actions {
            display: flex;
            gap: 8px;
        }

        #report-output {
            flex: 1;
            width: 100%;
            height: calc(100vh - 220px);
            padding: 16px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 0.88rem;
            line-height: 1.5;
            background-color: var(--code-bg);
            color: var(--text-color);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            resize: none;
            white-space: pre-wrap;
            overflow-y: auto;
        }

        /* Toast */
        #toast {
            visibility: hidden;
            min-width: 250px;
            background-color: #0f172a;
            color: #fff;
            text-align: center;
            border-radius: 8px;
            padding: 12px 18px;
            position: fixed;
            z-index: 100;
            bottom: 30px;
            right: 30px;
            font-size: 0.88rem;
            box-shadow: var(--shadow-md);
            opacity: 0;
            transition: opacity 0.3s, visibility 0.3s;
            border: 1px solid var(--accent-color);
        }

        #toast.show {
            visibility: visible;
            opacity: 1;
        }
    </style>
</head>
<body data-theme="light">

    <header>
        <div class="header-title-box">
            <span class="header-badge">ESGAR 2025</span>
            <div>
                <h1 id="ui-main-title">RM en Colangitis Esclerosante Primaria</h1>
                <div class="header-subtitle" id="ui-subtitle">Módulo de Informe Estructurado &bull; Guías de Consenso Europeo (Ippolito et al., 2025)</div>
            </div>
        </div>
        <div class="header-controls">
            <select id="lang-selector" onchange="changeLanguage()">
                <option value="es" selected>Español</option>
                <option value="ca">Català</option>
                <option value="en">English</option>
            </select>
            <button onclick="toggleTheme()" id="theme-btn">&#9790; Modo Oscuro</button>
            <button onclick="resetForm()" id="reset-btn">&#8635; Reiniciar</button>
        </div>
    </header>

    <div class="layout-container">
        <!-- FORMULARIO CLINICO IZQUIERDA -->
        <div class="form-column">

            <!-- DATOS GENERALES Y TIPO DE ESTUDIO -->
            <div class="card-section">
                <div class="section-header">
                    <h2 id="sec-general">&#128100; Datos del Estudio e Indicación</h2>
                </div>
                <div class="section-body">
                    <div class="input-inline">
                        <label class="field-label" id="lbl-exam-type">Tipo de Exploración:</label>
                        <select id="exam-type" class="form-select" onchange="updateReport()">
                            <option value="baseline" id="opt-exam-baseline">Estudio inicial / Sospecha diagnóstica</option>
                            <option value="surveillance" id="opt-exam-surv">Seguimiento anual / Cribado de complicaciones</option>
                            <option value="stent" id="opt-exam-stent">Control post-intervencionismo / Stent</option>
                            <option value="acute" id="opt-exam-acute">Sospecha de colangitis bacteriana / Complicación aguda</option>
                        </select>
                    </div>
                    <div class="input-inline">
                        <label class="field-label" id="lbl-prior-interventions">Intervenciones Previas:</label>
                        <select id="prior-interventions" class="form-select" onchange="updateReport()">
                            <option value="none" id="opt-prior-none">Ninguna / No constan</option>
                            <option value="stent" id="opt-prior-stent">Stent biliar endoscópico previo</option>
                            <option value="ercp" id="opt-prior-ercp">CPRE / Dilatación con balón previa</option>
                            <option value="cholecystectomy" id="opt-prior-chole">Colecistectomía previa</option>
                            <option value="surgery" id="opt-prior-surg">Cirugía biliar / Derivación biliodigestiva</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- PROTOCOLO TECNICO ESGAR -->
            <div class="card-section">
                <div class="section-header">
                    <h2 id="sec-protocol">&#9881; Protocolo de Adquisición (Consenso ESGAR)</h2>
                </div>
                <div class="section-body">
                    <div class="input-inline">
                        <label class="field-label" id="lbl-field">Campo Magnético:</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="field-strength" value="1.5T" checked onchange="updateReport()"> 1.5 T</label>
                            <label class="radio-card"><input type="radio" name="field-strength" value="3.0T" onchange="updateReport()"> 3.0 T</label>
                        </div>
                    </div>
                    <div class="input-inline">
                        <label class="field-label" id="lbl-fasting">Ayuno previo &ge; 4 horas:</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="fasting" value="yes" checked onchange="updateReport()"> <span id="opt-yes-fasting">Sí</span></label>
                            <label class="radio-card"><input type="radio" name="fasting" value="no" onchange="updateReport()"> <span id="opt-no-fasting">No</span></label>
                        </div>
                    </div>
                    <div class="field-row">
                        <label class="field-label" id="lbl-sequences">Secuencias Adquiridas:</label>
                        <div class="checkbox-group">
                            <label class="radio-card"><input type="checkbox" id="seq-t2" checked onchange="updateReport()"> T2WI Coronal/Axial (non-FS)</label>
                            <label class="radio-card"><input type="checkbox" id="seq-t1" checked onchange="updateReport()"> T1WI En/Fuera fase / DIXON</label>
                            <label class="radio-card"><input type="checkbox" id="seq-mrcp" checked onchange="updateReport()"> Colangio-RM 2D/3D (MRCP)</label>
                            <label class="radio-card"><input type="checkbox" id="seq-dwi" checked onchange="updateReport()"> Difusión (DWI bajo y alto b)</label>
                            <label class="radio-card"><input type="checkbox" id="seq-dyn" checked onchange="updateReport()"> T1 Dinámico con Contraste IV</label>
                            <label class="radio-card"><input type="checkbox" id="seq-hba" onchange="onHbaSeqChange()"> Fase Hepatobiliar (HBA)</label>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 1. HALLAZGOS EN VIA BILIAR -->
            <div class="card-section">
                <div class="section-header">
                    <h2 id="sec-biliary">&#127793; 1. Vía Biliar (Biliary Findings)</h2>
                </div>
                <div class="section-body">
                    <!-- Estenosis -->
                    <div class="field-row">
                        <label class="field-label" id="lbl-strictures">Estenosis Biliares:</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="strictures" value="absent" checked onchange="onStricturesChange()"> <span id="opt-strict-absent">Ausentes</span></label>
                            <label class="radio-card"><input type="radio" name="strictures" value="present" onchange="onStricturesChange()"> <span id="opt-strict-present">Presentes</span></label>
                        </div>
                    </div>

                    <!-- Condicional si estenosis presentes -->
                    <div id="box-strictures" class="conditional-box">
                        <div class="input-inline">
                            <label class="field-label" id="lbl-strict-number">Número:</label>
                            <div class="radio-group">
                                <label class="radio-card"><input type="radio" name="strict-num" value="single" checked onchange="updateReport()"> <span id="opt-num-single">Única</span></label>
                                <label class="radio-card"><input type="radio" name="strict-num" value="multiple" onchange="updateReport()"> <span id="opt-num-multiple">Múltiples</span></label>
                            </div>
                        </div>
                        <div class="input-inline">
                            <label class="field-label" id="lbl-strict-loc">Localización:</label>
                            <div class="radio-group">
                                <label class="radio-card"><input type="radio" name="strict-loc" value="intra" checked onchange="updateReport()"> <span id="opt-loc-intra">Intrahepática</span></label>
                                <label class="radio-card"><input type="radio" name="strict-loc" value="extra" onchange="updateReport()"> <span id="opt-loc-extra">Extrahepática</span></label>
                                <label class="radio-card"><input type="radio" name="strict-loc" value="both" onchange="updateReport()"> <span id="opt-loc-both">Ambas</span></label>
                            </div>
                        </div>
                        <div class="input-inline">
                            <label class="field-label" id="lbl-strict-grade">Severidad / Grado:</label>
                            <div class="radio-group">
                                <label class="radio-card"><input type="radio" name="strict-grade" value="low" checked onchange="onStrictGradeChange()"> <span id="opt-grade-low">Bajo grado (&lt; 75%)</span></label>
                                <label class="radio-card"><input type="radio" name="strict-grade" value="high" onchange="onStrictGradeChange()"> <span id="opt-grade-high">Alto grado (&ge; 75%)</span></label>
                            </div>
                        </div>

                        <div id="notice-high-grade" class="notice-box notice-danger" style="display:none;">
                            &#9888; <span id="msg-high-grade">ESGAR: Las estenosis de alto grado (&ge; 75%) o dominantes conllevan mayor riesgo tumoral y requieren correlación estrecha, cepillado citológico endoscópico y control evolutivo.</span>
                        </div>

                        <div class="input-inline">
                            <label class="field-label" id="lbl-strict-longest">Longitud de la estenosis más larga:</label>
                            <input type="number" id="strict-longest" placeholder="mm" min="0" step="1" oninput="updateReport()"> mm
                        </div>
                        <div class="input-inline">
                            <label class="field-label" id="lbl-strict-severe">Longitud de la estenosis más severa:</label>
                            <input type="number" id="strict-severe" placeholder="mm" min="0" step="1" oninput="updateReport()"> mm
                        </div>
                    </div>

                    <!-- Dilataciones -->
                    <div class="field-row">
                        <label class="field-label" id="lbl-dilations">Dilatación de la Vía Biliar:</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="dilations" value="absent" checked onchange="onDilationsChange()"> <span id="opt-dil-absent">Ausente</span></label>
                            <label class="radio-card"><input type="radio" name="dilations" value="present" onchange="onDilationsChange()"> <span id="opt-dil-present">Presente</span></label>
                        </div>
                    </div>
                    <div id="box-dilations" class="conditional-box">
                        <div class="input-inline">
                            <label class="field-label" id="lbl-dil-max">Calibre máximo:</label>
                            <input type="number" id="dil-max-caliber" placeholder="mm" min="1" step="0.5" oninput="updateReport()"> mm
                        </div>
                        <div class="input-inline">
                            <label class="field-label" id="lbl-dil-site">Distribución de dilatación:</label>
                            <div class="radio-group">
                                <label class="radio-card"><input type="radio" name="dil-site" value="intra" checked onchange="updateReport()"> <span id="opt-dilsite-intra">Intrahepática focal / segmentaria</span></label>
                                <label class="radio-card"><input type="radio" name="dil-site" value="diffuse" onchange="updateReport()"> <span id="opt-dilsite-diffuse">Difusa</span></label>
                                <label class="radio-card"><input type="radio" name="dil-site" value="main" onchange="updateReport()"> <span id="opt-dilsite-main">Vía biliar principal</span></label>
                            </div>
                        </div>
                    </div>

                    <!-- Engrosamiento parietal -->
                    <div class="field-row">
                        <label class="field-label" id="lbl-thickening">Engrosamiento Parietal de Vía Biliar (&gt; 2 mm):</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="thickening" value="no" checked onchange="updateReport()"> <span id="opt-thick-no">No (&le; 2 mm)</span></label>
                            <label class="radio-card"><input type="radio" name="thickening" value="yes" onchange="updateReport()"> <span id="opt-thick-yes">Sí (&gt; 2 mm) [Patológico]</span></label>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 2. VESICULA BILIAR Y LITIASIS -->
            <div class="card-section">
                <div class="section-header">
                    <h2 id="sec-gb">&#128167; 2. Vesícula Biliar y Litiasis</h2>
                </div>
                <div class="section-body">
                    <div class="input-inline">
                        <label class="field-label" id="lbl-gb-presence">Vesícula Biliar:</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="gb-presence" value="yes" checked onchange="onGbPresenceChange()"> <span id="opt-gb-pres">Presente</span></label>
                            <label class="radio-card"><input type="radio" name="gb-presence" value="no" onchange="onGbPresenceChange()"> <span id="opt-gb-abs">Ausente (Colecistectomía)</span></label>
                        </div>
                    </div>

                    <div id="box-gb" class="conditional-box visible">
                        <div class="input-inline">
                            <label class="field-label" id="lbl-gb-wall">Alteraciones parietales vesiculares:</label>
                            <div class="radio-group">
                                <label class="radio-card"><input type="radio" name="gb-wall" value="no" checked onchange="updateReport()"> <span id="opt-gbwall-no">No</span></label>
                                <label class="radio-card"><input type="radio" name="gb-wall" value="yes" onchange="updateReport()"> <span id="opt-gbwall-yes">Sí</span></label>
                            </div>
                        </div>
                        <div class="input-inline">
                            <label class="field-label" id="lbl-gb-lith">Colelitiasis:</label>
                            <div class="radio-group">
                                <label class="radio-card"><input type="radio" name="gb-lith" value="no" checked onchange="updateReport()"> <span id="opt-gblith-no">No</span></label>
                                <label class="radio-card"><input type="radio" name="gb-lith" value="yes" onchange="updateReport()"> <span id="opt-gblith-yes">Sí</span></label>
                            </div>
                        </div>
                        <div class="input-inline">
                            <label class="field-label" id="lbl-cystic-irreg">Irregularidades en el conducto cístico:</label>
                            <div class="radio-group">
                                <label class="radio-card"><input type="radio" name="cystic-irreg" value="no" checked onchange="updateReport()"> <span id="opt-cystic-no">No</span></label>
                                <label class="radio-card"><input type="radio" name="cystic-irreg" value="yes" onchange="updateReport()"> <span id="opt-cystic-yes">Sí</span></label>
                            </div>
                        </div>
                    </div>

                    <!-- Litiasis en via biliar -->
                    <div class="field-row">
                        <label class="field-label" id="lbl-tree-lith">Litiasis en el árbol biliar (Coledocolitiasis / Hepatolitiasis):</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="tree-lith" value="no" checked onchange="onTreeLithChange()"> <span id="opt-treelith-no">No</span></label>
                            <label class="radio-card"><input type="radio" name="tree-lith" value="yes" onchange="onTreeLithChange()"> <span id="opt-treelith-yes">Sí</span></label>
                        </div>
                    </div>
                    <div id="box-tree-lith" class="conditional-box">
                        <div class="input-inline">
                            <label class="field-label" id="lbl-treelith-loc">Localización de la litiasis:</label>
                            <div class="radio-group">
                                <label class="radio-card"><input type="radio" name="treelith-loc" value="intra" checked onchange="updateReport()"> <span id="opt-treelith-intra">Intrahepática</span></label>
                                <label class="radio-card"><input type="radio" name="treelith-loc" value="extra" onchange="updateReport()"> <span id="opt-treelith-extra">Extrahepática</span></label>
                                <label class="radio-card"><input type="radio" name="treelith-loc" value="both" onchange="updateReport()"> <span id="opt-treelith-both">Ambas</span></label>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 3. PARENQUIMA HEPATICO -->
            <div class="card-section">
                <div class="section-header">
                    <h2 id="sec-liver">&#129658; 3. Parénquima Hepático (Liver Findings)</h2>
                </div>
                <div class="section-body">
                    <div class="input-inline">
                        <label class="field-label" id="lbl-morphology">Morfología Hepática:</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="morphology" value="normal" checked onchange="updateReport()"> <span id="opt-morph-normal">Normal</span></label>
                            <label class="radio-card"><input type="radio" name="morphology" value="abnormal" onchange="updateReport()"> <span id="opt-morph-abnormal">Alterada / Dismórfica (Atrofia/Hipertrofia caudado)</span></label>
                        </div>
                    </div>

                    <div class="input-inline">
                        <label class="field-label" id="lbl-margins">Contornos Hepáticos:</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="margins" value="smooth" checked onchange="updateReport()"> <span id="opt-marg-smooth">Lisos</span></label>
                            <label class="radio-card"><input type="radio" name="margins" value="irregular" onchange="updateReport()"> <span id="opt-marg-irregular">Irregulares / Lobulados</span></label>
                        </div>
                    </div>

                    <div class="input-inline">
                        <label class="field-label" id="lbl-steatosis">Esteatosis:</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="steatosis" value="no" checked onchange="updateReport()"> No</label>
                            <label class="radio-card"><input type="radio" name="steatosis" value="yes" onchange="updateReport()"> Sí</label>
                        </div>
                    </div>

                    <div class="input-inline">
                        <label class="field-label" id="lbl-fibrosis">Fibrosis Confluente:</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="fibrosis" value="no" checked onchange="updateReport()"> No</label>
                            <label class="radio-card"><input type="radio" name="fibrosis" value="yes" onchange="updateReport()"> Sí (T2 intermedio / hipointenso tardío)</label>
                        </div>
                    </div>

                    <div class="input-inline">
                        <label class="field-label" id="lbl-edema">Edema Agudo / Inflamación Periductal:</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="edema" value="no" checked onchange="updateReport()"> No</label>
                            <label class="radio-card"><input type="radio" name="edema" value="yes" onchange="updateReport()"> Sí</label>
                        </div>
                    </div>

                    <div class="input-inline">
                        <label class="field-label" id="lbl-reg-nodules">Nódulos Regenerativos (&gt; 3 mm):</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="reg-nodules" value="no" checked onchange="updateReport()"> No</label>
                            <label class="radio-card"><input type="radio" name="reg-nodules" value="yes" onchange="updateReport()"> Sí (Macronodulares)</label>
                        </div>
                    </div>

                    <!-- Fases de contraste dinámico -->
                    <div id="box-contrast-phases" class="conditional-box visible">
                        <div class="field-label" id="lbl-contrast-pat">Patrón de Realce tras Contraste IV:</div>
                        <div class="input-inline">
                            <span style="font-size:0.84rem; width:140px;">Fase Arterial:</span>
                            <div class="radio-group">
                                <label class="radio-card"><input type="radio" name="art-phase" value="homogeneous" checked onchange="updateReport()"> Homogéneo</label>
                                <label class="radio-card"><input type="radio" name="art-phase" value="inhomogeneous" onchange="updateReport()"> Heterogéneo</label>
                            </div>
                        </div>
                        <div class="input-inline">
                            <span style="font-size:0.84rem; width:140px;">Fase Portal-Venosa:</span>
                            <div class="radio-group">
                                <label class="radio-card"><input type="radio" name="pv-phase" value="homogeneous" checked onchange="updateReport()"> Homogéneo</label>
                                <label class="radio-card"><input type="radio" name="pv-phase" value="inhomogeneous" onchange="updateReport()"> Heterogéneo</label>
                            </div>
                        </div>
                        <div id="row-hba-excretion" class="input-inline" style="display:none;">
                            <span style="font-size:0.84rem; width:140px;">Excreción HBA:</span>
                            <div class="radio-group">
                                <label class="radio-card"><input type="radio" name="hba-phase" value="homogeneous" checked onchange="updateReport()"> Homogénea</label>
                                <label class="radio-card"><input type="radio" name="hba-phase" value="inhomogeneous" onchange="updateReport()"> Heterogénea</label>
                            </div>
                        </div>
                    </div>

                    <!-- Lesiones focales -->
                    <div class="field-row">
                        <label class="field-label" id="lbl-focal-lesion">Lesión Focal Hepática:</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="focal-lesion" value="no" checked onchange="onFocalLesionChange()"> No</label>
                            <label class="radio-card"><input type="radio" name="focal-lesion" value="yes" onchange="onFocalLesionChange()"> Sí</label>
                        </div>
                    </div>
                    <div id="box-focal-lesion" class="conditional-box">
                        <div class="input-inline">
                            <label class="field-label" id="lbl-focal-type">Naturaleza sospechada:</label>
                            <div class="radio-group">
                                <label class="radio-card"><input type="radio" name="focal-nature" value="benign" checked onchange="updateReport()"> Benigna (quiste, hemangioma)</label>
                                <label class="radio-card"><input type="radio" name="focal-nature" value="malignant" onchange="updateReport()"> Sospecha de Malignidad (Colangiocarcinoma / CHC)</label>
                            </div>
                        </div>
                        <div class="input-inline">
                            <label class="field-label" id="lbl-focal-desc">Descripción / Localización / Tamaño:</label>
                            <input type="text" id="focal-desc" placeholder="Ej: Lesión de 18 mm en segmento IVb sospechosa de CCA" style="flex:1;" oninput="updateReport()">
                        </div>
                    </div>

                    <!-- Signos de descompensacion / HTP -->
                    <div class="field-row">
                        <label class="field-label" id="lbl-decomp">Signos de Hipertensión Portal / Descompensación:</label>
                        <div class="checkbox-group">
                            <label class="radio-card"><input type="checkbox" id="htp-collaterals" onchange="updateReport()"> Colaterales venosas porto-sistémicas</label>
                            <label class="radio-card"><input type="checkbox" id="htp-splenomegaly" onchange="updateReport()"> Esplenomegalia</label>
                            <label class="radio-card"><input type="checkbox" id="htp-ascites" onchange="updateReport()"> Ascitis</label>
                        </div>
                    </div>

                    <!-- Adenopatías perihepáticas -->
                    <div class="input-inline">
                        <label class="field-label" id="lbl-nodes">Adenopatías perihepáticas aumentadas (&gt; 10 mm):</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="nodes" value="no" checked onchange="updateReport()"> No</label>
                            <label class="radio-card"><input type="radio" name="nodes" value="yes" onchange="updateReport()"> Sí</label>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 4. BAZO -->
            <div class="card-section">
                <div class="section-header">
                    <h2 id="sec-spleen">&#127814; 4. Bazo (Spleen)</h2>
                </div>
                <div class="section-body">
                    <div class="input-inline">
                        <label class="field-label" id="lbl-spleen-size">Diámetro bipolar esplénico:</label>
                        <input type="number" id="spleen-size" placeholder="cm" min="5" max="30" step="0.5" oninput="onSpleenSizeChange()"> cm
                        <span id="spleen-status-badge" style="font-size:0.8rem; color:var(--text-secondary);">(Normal &le; 12 cm)</span>
                    </div>
                    <div class="notice-box notice-info">
                        &#8505; <span id="msg-spleen-note">ESGAR: El incremento de la longitud o volumen esplénico durante el seguimiento es un biomarcador independiente de progresión clínica y eventos adversos.</span>
                    </div>
                </div>
            </div>

            <!-- 5. PANCREAS -->
            <div class="card-section">
                <div class="section-header">
                    <h2 id="sec-pancreas">&#128300; 5. Páncreas</h2>
                </div>
                <div class="section-body">
                    <div class="input-inline">
                        <label class="field-label" id="lbl-aip">Pancreatitis Autoinmune (AIP) / Sospecha IgG4:</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="aip" value="rule-out" checked onchange="updateReport()"> <span id="opt-aip-out">Descartada / No sugestiva (Rule-out)</span></label>
                            <label class="radio-card"><input type="radio" name="aip" value="rule-in" onchange="updateReport()"> <span id="opt-aip-in">Sospecha de afectación IgG4 (Rule-in)</span></label>
                        </div>
                    </div>
                    <div class="field-row">
                        <label class="field-label" id="lbl-mpd">Dilatación del conducto pancreático principal (Wirsung):</label>
                        <div class="radio-group">
                            <label class="radio-card"><input type="radio" name="mpd" value="no" checked onchange="onMpdChange()"> No</label>
                            <label class="radio-card"><input type="radio" name="mpd" value="yes" onchange="onMpdChange()"> Sí</label>
                        </div>
                    </div>
                    <div id="box-mpd" class="conditional-box">
                        <div class="input-inline">
                            <label class="field-label" id="lbl-mpd-caliber">Calibre del Wirsung:</label>
                            <input type="number" id="mpd-caliber" placeholder="mm" min="2" step="0.5" oninput="updateReport()"> mm
                        </div>
                    </div>
                </div>
            </div>

            <!-- 6. CALCULADORA PRONOSTICA ANALI -->
            <div class="card-section">
                <div class="section-header">
                    <h2 id="sec-anali">&#128202; 6. Score Pronóstico ANALI Integrado</h2>
                </div>
                <div class="section-body">
                    <div class="notice-box notice-warning">
                        &#9888; <span id="msg-anali-caution">El panel ESGAR recomienda usar los modelos de riesgo radiológicos como el score ANALI con prudencia debido a la variabilidad interobservador, combinándolos siempre con la elastografía y datos clínicos/bioquímicos.</span>
                    </div>

                    <div class="anali-score-card">
                        <div>
                            <div style="font-weight:700; font-size:1rem;" id="title-anali-nogd">Score ANALI (Sin Gadolinio)</div>
                            <div style="font-size:0.8rem; color:var(--text-secondary);" id="desc-anali-nogd">Dilatación intrahepática + Dismorfia + Signos HTP (Rango 0-3)</div>
                        </div>
                        <div style="display:flex; align-items:center; gap:12px;">
                            <span class="anali-score-val" id="anali-nogd-val">0 / 3</span>
                            <span class="anali-risk-tag risk-low" id="anali-nogd-tag">Riesgo Bajo</span>
                        </div>
                    </div>

                    <div class="anali-score-card" id="card-anali-gd">
                        <div>
                            <div style="font-weight:700; font-size:1rem;" id="title-anali-gd">Score ANALI (Con Gadolinio)</div>
                            <div style="font-size:0.8rem; color:var(--text-secondary);" id="desc-anali-gd">ANALI sin Gd + Heterogeneidad parenquimatosa portal/tardía (+2 pts) (Rango 0-5)</div>
                        </div>
                        <div style="display:flex; align-items:center; gap:12px;">
                            <span class="anali-score-val" id="anali-gd-val">0 / 5</span>
                            <span class="anali-risk-tag risk-low" id="anali-gd-tag">Riesgo Bajo</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- 7. OBSERVACIONES Y NOTAS LIBRES -->
            <div class="card-section">
                <div class="section-header">
                    <h2 id="sec-notes">&#9998; 7. Observaciones Adicionales</h2>
                </div>
                <div class="section-body">
                    <textarea id="free-notes" rows="3" placeholder="Añade aquí hallazgos adicionales, comparativa con estudios previos o recomendaciones específicas..." oninput="updateReport()" style="width:100%; padding:10px; border-radius:6px; border:1px solid var(--border-color); background:var(--input-bg); color:var(--text-color); font-size:0.88rem;"></textarea>
                </div>
            </div>

        </div>

        <!-- COLUMNA INFORME ESTRUCTURADO (DERECHA) -->
        <div class="report-column">
            <div class="report-header-row">
                <h3 id="ui-rep-preview-title">Previsualización de Informe Estructurado</h3>
                <div class="report-actions">
                    <button class="btn-primary" onclick="copyReport()" id="btn-copy">&#128203; Copiar Informe</button>
                    <button onclick="downloadReport()" id="btn-download">&#128190; Guardar</button>
                </div>
            </div>
            <textarea id="report-output" readonly spellcheck="false"></textarea>
        </div>
    </div>

    <div id="toast">Informe copiado al portapapeles</div>

    <script>
        const translations = {
            es: {
                mainTitle: "RM en Colangitis Esclerosante Primaria",
                subtitle: "Módulo de Informe Estructurado • Guías de Consenso Europeo (Ippolito et al., 2025)",
                themeDark: "🌙 Modo Oscuro",
                themeLight: "☀️ Modo Claro",
                resetBtn: "↺ Reiniciar",
                btnCopy: "📋 Copiar Informe",
                btnDownload: "💾 Guardar",
                toastCopied: "Informe copiado al portapapeles",
                repTitle: "INFORME DE RESONANCIA MAGNÉTICA: COLANGITIS ESCLEROSANTE PRIMARIA (ESGAR 2025)",
                secTechnique: "TÉCNICA Y PROTOCOLO:",
                secBiliary: "1. VÍA BILIAR:",
                secGb: "2. VESÍCULA BILIAR Y LITIASIS:",
                secLiver: "3. PARÉNQUIMA HEPÁTICO:",
                secSpleen: "4. BAZO:",
                secPancreas: "5. PÁNCREAS:",
                secScores: "6. ESTRATIFICACIÓN PRONÓSTICA (SCORE ANALI):",
                secConclusion: "CONCLUSIÓN / IMPRESIÓN:",
                secNotes: "OBSERVACIONES / COMENTARIOS:"
            },
            ca: {
                mainTitle: "RM en Colangitis Esclerosant Primària",
                subtitle: "Mòdul d'Informe Estructurat • Guies de Consens Europeu (Ippolito et al., 2025)",
                themeDark: "🌙 Mode Fosc",
                themeLight: "☀️ Mode Clar",
                resetBtn: "↺ Reiniciar",
                btnCopy: "📋 Copiar Informe",
                btnDownload: "💾 Guardar",
                toastCopied: "Informe copiat al porta-retalls",
                repTitle: "INFORME DE RESONÀNCIA MAGNÈTICA: COLANGITIS ESCLEROSANT PRIMÀRIA (ESGAR 2025)",
                secTechnique: "TÈCNICA I PROTOCOL:",
                secBiliary: "1. VIA BILIAR:",
                secGb: "2. VESÍCULA BILIAR I LITIASI:",
                secLiver: "3. PARÈNQUIMA HEPÀTIC:",
                secSpleen: "4. BAF:",
                secPancreas: "5. PÀNCREES:",
                secScores: "6. ESTRATIFICACIÓ PRONÒSTICA (SCORE ANALI):",
                secConclusion: "CONCLUSIÓ / IMPRESSIÓ:",
                secNotes: "OBSERVACIONS / COMENTARIS:"
            },
            en: {
                mainTitle: "MR Imaging in Primary Sclerosing Cholangitis",
                subtitle: "Structured Reporting Module • European Consensus Statement (Ippolito et al., 2025)",
                themeDark: "🌙 Dark Mode",
                themeLight: "☀️ Light Mode",
                resetBtn: "↺ Reset",
                btnCopy: "📋 Copy Report",
                btnDownload: "💾 Save",
                toastCopied: "Report copied to clipboard",
                repTitle: "MRI REPORT: PRIMARY SCLEROSING CHOLANGITIS (ESGAR 2025)",
                secTechnique: "TECHNIQUE & PROTOCOL:",
                secBiliary: "1. BILIARY FINDINGS:",
                secGb: "2. GALLBLADDER & LITHIASIS:",
                secLiver: "3. LIVER PARENCHYMA:",
                secSpleen: "4. SPLEEN:",
                secPancreas: "5. PANCREAS:",
                secScores: "6. PROGNOSTIC STRATIFICATION (ANALI SCORE):",
                secConclusion: "CONCLUSION / IMPRESSION:",
                secNotes: "ADDITIONAL NOTES:"
            }
        };

        function toggleTheme() {
            const body = document.body;
            const currentTheme = body.getAttribute("data-theme");
            const newTheme = currentTheme === "dark" ? "light" : "dark";
            body.setAttribute("data-theme", newTheme);
            const lang = document.getElementById("lang-selector").value;
            document.getElementById("theme-btn").innerHTML = newTheme === "dark" ? translations[lang].themeLight : translations[lang].themeDark;
        }

        function changeLanguage() {
            const lang = document.getElementById("lang-selector").value;
            const t = translations[lang];
            document.getElementById("ui-main-title").innerText = t.mainTitle;
            document.getElementById("ui-subtitle").innerText = t.subtitle;
            const currentTheme = document.body.getAttribute("data-theme");
            document.getElementById("theme-btn").innerHTML = currentTheme === "dark" ? t.themeLight : t.themeDark;
            document.getElementById("reset-btn").innerHTML = t.resetBtn;
            document.getElementById("btn-copy").innerHTML = t.btnCopy;
            document.getElementById("btn-download").innerHTML = t.btnDownload;
            updateReport();
        }

        function onStricturesChange() {
            const val = document.querySelector('input[name="strictures"]:checked')?.value;
            const box = document.getElementById("box-strictures");
            if (val === "present") {
                box.classList.add("visible");
            } else {
                box.classList.remove("visible");
            }
            onStrictGradeChange();
            updateReport();
        }

        function onStrictGradeChange() {
            const strictVal = document.querySelector('input[name="strictures"]:checked')?.value;
            const gradeVal = document.querySelector('input[name="strict-grade"]:checked')?.value;
            const notice = document.getElementById("notice-high-grade");
            if (strictVal === "present" && gradeVal === "high") {
                notice.style.display = "flex";
            } else {
                notice.style.display = "none";
            }
            updateReport();
        }

        function onDilationsChange() {
            const val = document.querySelector('input[name="dilations"]:checked')?.value;
            const box = document.getElementById("box-dilations");
            if (val === "present") {
                box.classList.add("visible");
            } else {
                box.classList.remove("visible");
            }
            updateReport();
        }

        function onGbPresenceChange() {
            const val = document.querySelector('input[name="gb-presence"]:checked')?.value;
            const box = document.getElementById("box-gb");
            if (val === "yes") {
                box.classList.add("visible");
            } else {
                box.classList.remove("visible");
            }
            updateReport();
        }

        function onTreeLithChange() {
            const val = document.querySelector('input[name="tree-lith"]:checked')?.value;
            const box = document.getElementById("box-tree-lith");
            if (val === "yes") {
                box.classList.add("visible");
            } else {
                box.classList.remove("visible");
            }
            updateReport();
        }

        function onHbaSeqChange() {
            const checked = document.getElementById("seq-hba").checked;
            document.getElementById("row-hba-excretion").style.display = checked ? "flex" : "none";
            updateReport();
        }

        function onFocalLesionChange() {
            const val = document.querySelector('input[name="focal-lesion"]:checked')?.value;
            const box = document.getElementById("box-focal-lesion");
            if (val === "yes") {
                box.classList.add("visible");
            } else {
                box.classList.remove("visible");
            }
            updateReport();
        }

        function onSpleenSizeChange() {
            const val = parseFloat(document.getElementById("spleen-size").value);
            const badge = document.getElementById("spleen-status-badge");
            if (!isNaN(val)) {
                if (val > 12) {
                    badge.innerText = `(Esplenomegalia: > 12 cm)`;
                    badge.style.color = "var(--danger-text)";
                    document.getElementById("htp-splenomegaly").checked = true;
                } else {
                    badge.innerText = `(Normal: ≤ 12 cm)`;
                    badge.style.color = "var(--success-text)";
                }
            } else {
                badge.innerText = `(Normal ≤ 12 cm)`;
                badge.style.color = "var(--text-secondary)";
            }
            updateReport();
        }

        function onMpdChange() {
            const val = document.querySelector('input[name="mpd"]:checked')?.value;
            const box = document.getElementById("box-mpd");
            if (val === "yes") {
                box.classList.add("visible");
            } else {
                box.classList.remove("visible");
            }
            updateReport();
        }

        function calculateAnali() {
            // ANALI sin Gd:
            // 1. Dilatación intrahepática: 1 pt
            // 2. Dismorfia hepática: 1 pt
            // 3. Hipertensión portal (esplenomegalia, ascitis o colaterales): 1 pt
            let scoreNoGd = 0;
            const dilPresent = document.querySelector('input[name="dilations"]:checked')?.value === "present";
            const dilSite = document.querySelector('input[name="dil-site"]:checked')?.value;
            if (dilPresent && (dilSite === "intra" || dilSite === "diffuse")) {
                scoreNoGd += 1;
            }

            const morphAbnormal = document.querySelector('input[name="morphology"]:checked')?.value === "abnormal";
            if (morphAbnormal) {
                scoreNoGd += 1;
            }

            const htpCollaterals = document.getElementById("htp-collaterals").checked;
            const htpSpleno = document.getElementById("htp-splenomegaly").checked;
            const htpAscites = document.getElementById("htp-ascites").checked;
            if (htpCollaterals || htpSpleno || htpAscites) {
                scoreNoGd += 1;
            }

            // ANALI con Gd: scoreNoGd + heterogeneidad en fase portal-venosa (2 pts)
            const pvInhomogeneous = document.querySelector('input[name="pv-phase"]:checked')?.value === "inhomogeneous";
            let scoreGd = scoreNoGd + (pvInhomogeneous ? 2 : 0);

            // Actualizar UI
            document.getElementById("anali-nogd-val").innerText = `${scoreNoGd} / 3`;
            const tagNoGd = document.getElementById("anali-nogd-tag");
            if (scoreNoGd <= 1) {
                tagNoGd.className = "anali-risk-tag risk-low";
                tagNoGd.innerText = "Riesgo Bajo";
            } else {
                tagNoGd.className = "anali-risk-tag risk-high";
                tagNoGd.innerText = "Riesgo Alto";
            }

            document.getElementById("anali-gd-val").innerText = `${scoreGd} / 5`;
            const tagGd = document.getElementById("anali-gd-tag");
            if (scoreGd <= 1) {
                tagGd.className = "anali-risk-tag risk-low";
                tagGd.innerText = "Riesgo Bajo";
            } else if (scoreGd <= 3) {
                tagGd.className = "anali-risk-tag risk-intermediate";
                tagGd.innerText = "Riesgo Intermedio";
            } else {
                tagGd.className = "anali-risk-tag risk-high";
                tagGd.innerText = "Riesgo Alto";
            }

            return { scoreNoGd, scoreGd };
        }

        function updateReport() {
            const lang = document.getElementById("lang-selector").value;
            const t = translations[lang];
            const anali = calculateAnali();

            let r = "";
            r += "========================================================================\n";
            r += `${t.repTitle}\n`;
            r += "========================================================================\n\n";

            // DATOS ESTUDIO
            const examSelect = document.getElementById("exam-type");
            const examText = examSelect.options[examSelect.selectedIndex].text;
            const priorSelect = document.getElementById("prior-interventions");
            const priorText = priorSelect.options[priorSelect.selectedIndex].text;
            r += `INDICACIÓN / TIPO: ${examText}\n`;
            r += `INTERVENCIONES PREVIAS: ${priorText}\n\n`;

            // TECNICA
            r += `${t.secTechnique}\n`;
            const field = document.querySelector('input[name="field-strength"]:checked')?.value || "1.5T";
            const fasting = document.querySelector('input[name="fasting"]:checked')?.value === "yes" ? "Sí (≥ 4h)" : "No";
            r += ` - Campo Magnético: ${field} | Ayuno previo: ${fasting}\n`;
            let seqs = [];
            if (document.getElementById("seq-t2").checked) seqs.push("T2WI no-FS (axial/coronal)");
            if (document.getElementById("seq-t1").checked) seqs.push("T1WI fase/opuesta");
            if (document.getElementById("seq-mrcp").checked) seqs.push("Colangio-RM 2D/3D (MRCP)");
            if (document.getElementById("seq-dwi").checked) seqs.push("DWI (b-bajo y b-alto)");
            if (document.getElementById("seq-dyn").checked) seqs.push("T1 dinámico con cte");
            if (document.getElementById("seq-hba").checked) seqs.push("Fase Hepatobiliar HBA (ácido gadoxético)");
            r += ` - Secuencias: ${seqs.join(", ")}\n\n`;

            // 1. VIA BILIAR
            r += `${t.secBiliary}\n`;
            const strict = document.querySelector('input[name="strictures"]:checked')?.value;
            if (strict === "absent") {
                r += " - Estenosis biliares: AUSENTES.\n";
            } else {
                const sNum = document.querySelector('input[name="strict-num"]:checked')?.value === "single" ? "Única" : "Múltiples";
                const sLocVal = document.querySelector('input[name="strict-loc"]:checked')?.value;
                const sLoc = sLocVal === "intra" ? "Intrahepática" : sLocVal === "extra" ? "Extrahepática" : "Intra y extrahepática";
                const sGradeVal = document.querySelector('input[name="strict-grade"]:checked')?.value;
                const sGrade = sGradeVal === "high" ? "ALTO GRADO (≥ 75%) [Estenosis relevante / dominante]" : "Bajo grado (< 75%)";
                r += ` - Estenosis biliares: PRESENTES (${sNum}, localización ${sLoc}, ${sGrade}).\n`;
                const sLong = document.getElementById("strict-longest").value;
                if (sLong) r += `   * Longitud de estenosis más larga: ${sLong} mm.\n`;
                const sSev = document.getElementById("strict-severe").value;
                if (sSev) r += `   * Longitud de estenosis más severa: ${sSev} mm.\n`;
            }

            const dil = document.querySelector('input[name="dilations"]:checked')?.value;
            if (dil === "absent") {
                r += " - Dilatación biliar: AUSENTE.\n";
            } else {
                const dilCal = document.getElementById("dil-max-caliber").value;
                const dSiteVal = document.querySelector('input[name="dil-site"]:checked')?.value;
                const dSite = dSiteVal === "intra" ? "intrahepática segmentaria" : dSiteVal === "diffuse" ? "difusa intrahepática" : "vía biliar principal";
                r += ` - Dilatación biliar: PRESENTE (${dSite}${dilCal ? `, calibre máx: ${dilCal} mm` : ""}).\n`;
            }

            const thick = document.querySelector('input[name="thickening"]:checked')?.value === "yes";
            r += ` - Engrosamiento parietal ductal (> 2 mm): ${thick ? "SÍ (Patológico, sugerente de inflamación/colangitis)" : "NO (≤ 2 mm, normal)"}.\n\n`;

            // 2. VESICULA Y LITIASIS
            r += `${t.secGb}\n`;
            const gbPres = document.querySelector('input[name="gb-presence"]:checked')?.value === "yes";
            if (!gbPres) {
                r += " - Vesícula biliar: AUSENTE quirúrgicamente (Colecistectomía previa).\n";
            } else {
                r += " - Vesícula biliar: Presente.\n";
                const gbWall = document.querySelector('input[name="gb-wall"]:checked')?.value === "yes";
                r += `   * Alteraciones parietales: ${gbWall ? "SÍ (engrosamiento/edema)" : "No"}.\n`;
                const gbLith = document.querySelector('input[name="gb-lith"]:checked')?.value === "yes";
                r += `   * Colelitiasis: ${gbLith ? "SÍ" : "No"}.\n`;
                const cystIrreg = document.querySelector('input[name="cystic-irreg"]:checked')?.value === "yes";
                r += `   * Irregularidades en conducto cístico: ${cystIrreg ? "SÍ" : "No"}.\n`;
            }

            const treeLith = document.querySelector('input[name="tree-lith"]:checked')?.value === "yes";
            if (!treeLith) {
                r += " - Litiasis en árbol biliar: NO identificada.\n\n";
            } else {
                const tlLocVal = document.querySelector('input[name="treelith-loc"]:checked')?.value;
                const tlLoc = tlLocVal === "intra" ? "intrahepática" : tlLocVal === "extra" ? "extrahepática (coledocolitiasis)" : "intra y extrahepática";
                r += ` - Litiasis en árbol biliar: SÍ (localización ${tlLoc}).\n\n`;
            }

            // 3. PARÉNQUIMA HEPÁTICO
            r += `${t.secLiver}\n`;
            const morph = document.querySelector('input[name="morphology"]:checked')?.value === "abnormal";
            r += ` - Morfología: ${morph ? "ALTERADA (Dismorfia con atrofia de segmentos periféricos y/o hipertrofia de lóbulo caudado)" : "Conservada / Normal"}.\n`;
            const margins = document.querySelector('input[name="margins"]:checked')?.value === "irregular";
            r += ` - Contornos: ${margins ? "Irregulares / nodulares" : "Lisos y regulares"}.\n`;
            const steat = document.querySelector('input[name="steatosis"]:checked')?.value === "yes";
            r += ` - Esteatosis: ${steat ? "Presente" : "No identificada"}.\n`;
            const fib = document.querySelector('input[name="fibrosis"]:checked')?.value === "yes";
            r += ` - Fibrosis confluente: ${fib ? "SÍ (áreas de señal intermedia en T2 con hipointensidad portal/tardía)" : "No identificada"}.\n`;
            const edema = document.querySelector('input[name="edema"]:checked')?.value === "yes";
            r += ` - Edema periductal / inflamación activa: ${edema ? "SÍ (hiperintensidad T2 peribiliar)" : "No"}.\n`;
            const nodules = document.querySelector('input[name="reg-nodules"]:checked')?.value === "yes";
            r += ` - Nódulos regenerativos macronodulares (> 3 mm): ${nodules ? "PRESENTES" : "No identificados"}.\n`;

            const artPh = document.querySelector('input[name="art-phase"]:checked')?.value === "inhomogeneous" ? "Heterogéneo" : "Homogéneo";
            const pvPh = document.querySelector('input[name="pv-phase"]:checked')?.value === "inhomogeneous" ? "Heterogéneo" : "Homogéneo";
            r += ` - Realce dinámico: Fase arterial ${artPh} | Fase portal ${pvPh}.\n`;
            if (document.getElementById("seq-hba").checked) {
                const hbaPh = document.querySelector('input[name="hba-phase"]:checked')?.value === "inhomogeneous" ? "Heterogénea (captación/excreción parcheada)" : "Homogénea";
                r += ` - Fase Hepatobiliar HBA: Excreción ${hbaPh}.\n`;
            }

            const focal = document.querySelector('input[name="focal-lesion"]:checked')?.value === "yes";
            if (!focal) {
                r += " - Lesiones focales hepáticas: NO se aprecian lesiones focales sospechosas.\n";
            } else {
                const natVal = document.querySelector('input[name="focal-nature"]:checked')?.value;
                const nat = natVal === "benign" ? "Benigna" : "SOSPECHOSA DE MALIGNIDAD (Colangiocarcinoma / CHC)";
                const desc = document.getElementById("focal-desc").value;
                r += ` - Lesión focal hepática: PRESENTE (${nat}${desc ? `: ${desc}` : ""}).\n`;
            }

            let htpItems = [];
            if (document.getElementById("htp-collaterals").checked) htpItems.push("circulación colateral porto-sistémica");
            if (document.getElementById("htp-splenomegaly").checked) htpItems.push("esplenomegalia");
            if (document.getElementById("htp-ascites").checked) htpItems.push("ascitis");
            r += ` - Signos de hipertensión portal: ${htpItems.length > 0 ? "PRESENTES (" + htpItems.join(", ") + ")" : "Ausentes"}.\n`;
            const nodes = document.querySelector('input[name="nodes"]:checked')?.value === "yes";
            r += ` - Adenopatías perihepáticas aumentadas: ${nodes ? "SÍ (> 10 mm)" : "No significativas"}.\n\n`;

            // 4. BAZO
            r += `${t.secSpleen}\n`;
            const splSize = document.getElementById("spleen-size").value;
            r += ` - Longitud bipolar esplénica: ${splSize ? splSize + " cm" : "No medida"}${splSize && parseFloat(splSize) > 12 ? " (Esplenomegalia)" : ""}.\n\n`;

            // 5. PANCREAS
            r += `${t.secPancreas}\n`;
            const aip = document.querySelector('input[name="aip"]:checked')?.value;
            r += ` - Afectación sugerente de Pancreatitis Autoinmune / IgG4: ${aip === "rule-in" ? "SOSPECHA (Rule-in: considerar determinación IgG4 y correlación clínica)" : "Descartada (Rule-out)"}.\n`;
            const mpd = document.querySelector('input[name="mpd"]:checked')?.value === "yes";
            if (!mpd) {
                r += " - Conducto de Wirsung: Calibre normal, sin dilatación.\n\n";
            } else {
                const mpdCal = document.getElementById("mpd-caliber").value;
                r += ` - Conducto de Wirsung: DILATADO${mpdCal ? ` (${mpdCal} mm)` : ""}.\n\n`;
            }

            // 6. SCORES
            r += `${t.secScores}\n`;
            r += ` - ANALI Score (sin Gd): ${anali.scoreNoGd} / 3 puntos [${anali.scoreNoGd <= 1 ? "Riesgo Bajo / Buen pronóstico a 4 años" : "Riesgo Alto / Mayor probabilidad de progresión"}]\n`;
            r += ` - ANALI Score (con Gd): ${anali.scoreGd} / 5 puntos [${anali.scoreGd <= 1 ? "Riesgo Bajo" : anali.scoreGd <= 3 ? "Riesgo Intermedio" : "Riesgo Alto"}]\n`;
            r += `   (Nota de consenso ESGAR: Los scores radiológicos deben valorarse con precaución debido a variabilidad interobservador, integrándolos con elastografía y parámetros de colestasis).\n\n`;

            // 7. CONCLUSION
            r += `${t.secConclusion}\n`;
            let concList = [];
            if (strict === "present") {
                const sGradeVal = document.querySelector('input[name="strict-grade"]:checked')?.value;
                if (sGradeVal === "high") {
                    concList.push("1. Hallazgos compatibles con Colangitis Esclerosante Primaria (CEP) con ESTENOSIS BILIAR DE ALTO GRADO / DOMINANTE. Se recomienda correlación con CA 19-9, cepillado citológico endoscópico y seguimiento estrecho.");
                } else {
                    concList.push("1. Hallazgos de colangiopatía estenosante compatibles con Colangitis Esclerosante Primaria (CEP) de bajo grado.");
                }
            } else {
                concList.push("1. No se identifican estenosis biliares definidas en el estudio actual.");
            }

            if (focal && document.querySelector('input[name="focal-nature"]:checked')?.value === "malignant") {
                concList.push("2. ALERTA: Lesión focal hepática con criterios de sospecha neoplásica (posible colangiocarcinoma / hepatocarcinoma). Se recomienda estudio específico y comité multidisciplinar.");
            }

            if (htpItems.length > 0 || morph) {
                concList.push("3. Signos de remodelado hepático / cirrosis y signos radiológicos de hipertensión portal.");
            }

            concList.push("4. Recomendación de seguimiento ESGAR: Vigilancia anual con Colangio-RM + RM con contraste IV, asociada a determinación de CA 19-9.");

            r += concList.join("\n") + "\n\n";

            // OBSERVACIONES
            const notes = document.getElementById("free-notes").value;
            if (notes.trim()) {
                r += `${t.secNotes}\n${notes.trim()}\n\n`;
            }

            r += "========================================================================\n";
            r += "Informe estructurado generado con el módulo ESGAR 2025 PSC v1.0\n";
            r += "Oriol Busquets & Guillem Casamayor - Consenso Europeo ESGAR\n";
            r += "========================================================================";

            document.getElementById("report-output").value = r;
        }

        function copyReport() {
            const text = document.getElementById("report-output").value;
            navigator.clipboard.writeText(text).then(() => {
                showToast();
            }).catch(err => {
                const textarea = document.getElementById("report-output");
                textarea.select();
                document.execCommand("copy");
                showToast();
            });
        }

        function showToast() {
            const toast = document.getElementById("toast");
            const lang = document.getElementById("lang-selector").value;
            toast.innerText = translations[lang].toastCopied;
            toast.className = "show";
            setTimeout(() => { toast.className = toast.className.replace("show", ""); }, 2500);
        }

        function downloadReport() {
            const text = document.getElementById("report-output").value;
            const blob = new Blob([text], { type: "text/plain;charset=utf-8" });
            const url = URL.createObjectURL(blob);
            const a = document.createElement("a");
            a.href = url;
            a.download = `Informe_RM_CEP_ESGAR_${new Date().toISOString().slice(0,10)}.txt`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);
        }

        function resetForm() {
            if (confirm("¿Deseas reiniciar todos los campos del formulario?")) {
                location.reload();
            }
        }

        // Inicializar al cargar
        window.onload = function() {
            updateReport();
        };
    </script>
</body>
</html>
'''

with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated {target_file} successfully ({len(html_content)} bytes)")
