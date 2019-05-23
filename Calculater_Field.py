# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Calculater_Field.py
# Created on: 2019-05-23 15:16:50.00000
#   (generated by ArcGIS/ModelBuilder)
# Usage: Calculater_Field <mapeamento_mi_XXXX_X> 
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Script arguments
mapeamento_mi_XXXX_X = arcpy.GetParameterAsText(0)
if mapeamento_mi_XXXX_X == '#' or not mapeamento_mi_XXXX_X:
    mapeamento_mi_XXXX_X = "mapeamento_mi_XXXX_X" # provide a default value if unspecified

# Local variables:
mapeamento_mi_XXXX_X__2_ = mapeamento_mi_XXXX_X
mapeamento_mi_XXXX_X__5_ = mapeamento_mi_XXXX_X
mapeamento_mi_XXXX_X__3_ = mapeamento_mi_XXXX_X

# Process: Calculate Field
arcpy.CalculateField_management(mapeamento_mi_XXXX_X, "NIVEL_I", "Reclass( !codigo! )", "PYTHON", "def Reclass(codigo):\\n    if (codigo == 1):\\n       return \"Áreas de Vegetação Natural\"\\n    elif (codigo >= 2 and codigo <= 4):\\n        return \"Áreas Antrópicas Agrícolas\"\\n    elif (codigo == 5):\\n        return \"Áreas Antrópicas Agrícolas/Áreas de Vegetação Natural\"\\n    elif (codigo == 6):\\n        return \"Água\"\\n    elif (codigo >= 7 and codigo <= 9):\\n        return \"Áreas de Vegetação Natural\"\\n    elif (codigo == 10):\\n        return \"Outras áreas\"\\n    elif (codigo >= 11 and codigo <= 13):\\n        return \"Áreas Antrópicas Não Agrícolas\"")

# Process: Calculate Field (2)
arcpy.CalculateField_management(mapeamento_mi_XXXX_X, "NIVEL_II", "Reclass( !codigo! )", "PYTHON", "def Reclass(codigo):\\n    if (codigo == 1):\\n       return \"Floresta Nativa\"\\n    elif (codigo == 2):\\n        return \"Plantios Florestais\"\\n    elif (codigo == 3):\\n        return \"Agricultura Perene\"\\n    elif (codigo == 4):\\n        return \"Agricultura Anual\"\\n    elif (codigo == 5):\\n        return \"Pastagem/Campo\"\\n    elif (codigo == 6):\\n        return \"Corpos d’Água\"\\n    elif (codigo == 7):\\n        return \"Várzea\"\\n    elif (codigo == 8):\\n        return \"Mangue\"\\n    elif (codigo == 9):\\n        return \"Restinga\"\\n    elif (codigo == 10):\\n        return \"Linha de Praia\"\\n    elif (codigo == 11):\\n        return \"Solo Exposto/Mineração\"\\n    elif (codigo == 12):\\n        return \"Área Urbanizada\"\\n    elif (codigo == 13):\\n        return \"Área Construída\"")

# Process: Calculate Field (3)
arcpy.CalculateField_management(mapeamento_mi_XXXX_X, "NIVEL_III", "Reclass( !codigo! )", "PYTHON", "def Reclass(codigo):\\n    if (codigo == 1):\\n       return \"Floresta Estacional Semi-Decidual; Floresta Ombrófila Mista; Floresta Ombrófila Densa, Aluviais, Submontana, Montana e Altomontana \"\\n    elif (codigo == 2):\\n        return \"Espécie Nativa (Araucaria angustifolia) e Espécies Exótica/Silvicultura (Pinus spp e Eucalyptus spp) e Sistemas Agroflorestais.\"\\n    elif (codigo == 3):\\n        return \"Frutíferas perenes (Café, Seringueira, Banana).\"\\n    elif (codigo == 4):\\n        return \"Culturas de ciclo curto (milho, trigo, soja, tubérculos e hortaliças). \"\\n    elif (codigo == 5):\\n        return \"Pecuária/ Estepe Gramíneo-Lenhosa, Savana Arborizada, Parque, Refúgios Ecológicos\"\\n    elif (codigo == 6):\\n        return \"Rios de margem dupla, lagos, lagoas, barragens, represas, canais naturais ou artificiais, tanques d’água\"\\n    elif (codigo == 7):\\n        return \"Formação pioneira com influência fluvial e/ou lacustre, com - comunidades arbóreas, arbustivas e herbáceas\"\\n    elif (codigo == 8):\\n        return \"Formação pioneira com influência fluviomarinha com - comunidades arbóreas, arbustivas e herbáceas\"\\n    elif (codigo == 9):\\n        return \"Formação pioneira com influência marinha - com - comunidades arbóreas, arbustivas e herbáceas\"\\n    elif (codigo == 10):\\n        return \"Faixa de areia sem vegetação próximo ao oceano.\"\\n    elif (codigo == 11):\\n        return \"Áreas sem vegetação, podendo ser ocupada por mineração, exploração de jazidas, lavras, extração de areia\"\\n    elif (codigo == 12):\\n        return \"Edificações e sistema viário, metrópoles, cidades, vilas, áreas de rodovias, serviços e transporte, energia, comunicações e terrenos associados\"\\n    elif (codigo == 13):\\n        return \"Usinas, diques, barragens, marinas, silos, grande galpões, indústrias, pátios de manobras de sistema de transporte, portos, aeroportos e demais estruturas de tamanhos consideráveis e isolados de mancha urbana\"		")

