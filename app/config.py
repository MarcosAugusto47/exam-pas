RESULTS_INFO = ['numero_inscricao',
                'nome_x',
                'escore_bruto_p1_etapa1',
                'escore_bruto_p2_etapa1',
                'nota_redacao_etapa1',
                'escore_bruto_p1_etapa2',
                'escore_bruto_p2_etapa2',
                'nota_redacao_etapa2',
                'escore_bruto_p1_etapa3',
                'escore_bruto_p2_etapa3',
                'nota_redacao_etapa3',
                'argumento_final',
                'classificacao_final_universal',
                'classificacao_final_cotas_negros',
                'classificacao_final_publicas1',
                'classificacao_final_publicas2',
                'classificacao_final_publicas3',
                'classificacao_final_publicas4',
                'classificacao_final_publicas5',
                'classificacao_final_publicas6',
                'classificacao_final_publicas7',
                'classificacao_final_publicas8',
                'course',
                'cotista',
                'cotas_negros_flag',
                #'publicas1_flag',
                #'publicas2_flag',
                #'publicas3_flag',
                #'publicas4_flag',
                #'publicas5_flag',
                #'publicas6_flag',
                #'publicas7_flag',
                #'publicas8_flag',
                #'publicas_flag',
                #'nome_y',
                #'sistema_subsistema',
                #'curso',
                #'_merge',
                #'label',
                #'pseudo_argumento_final',
                'mean',
                'median',
                'min',
                'max',
                'std',
                'min_flag',
                'max_flag',
                'median_flag',
                'mean_flag']

FEATURES = ['escore_bruto_p1_etapa1',
            'escore_bruto_p2_etapa1',
            'nota_redacao_etapa1',
            'escore_bruto_p1_etapa2',
            'escore_bruto_p2_etapa2',
            'nota_redacao_etapa2',
            'escore_bruto_p1_etapa3',
            'escore_bruto_p2_etapa3',
            'nota_redacao_etapa3',
            'cotista',
            'cotas_negros_flag',
            'publicas_flag',
            'publicas1_flag',
            'publicas2_flag',
            'publicas3_flag',
            'publicas4_flag',
            'publicas5_flag',
            'publicas6_flag',
            'publicas7_flag',
            'publicas8_flag',
            'AGRONOMIA (BACHARELADO)',
            'ARQUITETURA E URBANISMO (BACHARELADO)',
            'ARQUIVOLOGIA (BACHARELADO)',
            'ARTES CÊNICAS - INTERPRETAÇÃO TEATRAL (BACHARELADO)',
            'ARTES VISUAIS (BACHARELADO)',
            'ARTES VISUAIS (LICENCIATURA)',
            'BIBLIOTECONOMIA (BACHARELADO)',
            'BIOTECNOLOGIA (BACHARELADO)',
            'CAMPUS UNB CEILÂNDIA (FCE) ENFERMAGEM (BACHARELADO)',
            'CAMPUS UNB PLANALTINA (FUP) – DIURNO CIÊNCIAS NATURAIS (LICENCIATURA)',
            'CAMPUS UNB PLANALTINA (FUP) – NOTURNO CIÊNCIAS NATURAIS (LICENCIATURA)',
            'CIÊNCIA DA COMPUTAÇÃO (BACHARELADO)',
            'CIÊNCIA POLÍTICA (BACHARELADO)',
            'CIÊNCIAS AMBIENTAIS (BACHARELADO)',
            'CIÊNCIAS BIOLÓGICAS (BACHARELADO)',
            'CIÊNCIAS CONTÁBEIS (BACHARELADO)',
            'CIÊNCIAS ECONÔMICAS (BACHARELADO)',
            'CIÊNCIAS SOCIAIS – ANTROPOLOGIA / SOCIOLOGIA (BACHARELADO/LICENCIATURA)',
            'COMPUTAÇÃO (LICENCIATURA)',
            'COMUNICAÇÃO ORGANIZACIONAL (BACHARELADO)',
            'COMUNICAÇÃO SOCIAL - PUBLICIDADE E PROPAGANDA (BACHARELADO)',
            'COMUNICAÇÃO SOCIAL – AUDIOVISUAL (BACHARELADO)',
            'DESIGN – PROGRAMAÇÃO VISUAL/PROJETO DO PRODUTO (BACHARELADO)',
            'DIREITO (BACHARELADO)',
            'DIURNO ADMINISTRAÇÃO (BACHARELADO)',
            'EDUCAÇÃO FÍSICA (BACHARELADO)',
            'EDUCAÇÃO FÍSICA (LICENCIATURA)',
            'ENFERMAGEM (BACHARELADO)',
            'ENGENHARIA AMBIENTAL (BACHARELADO)',
            'ENGENHARIA CIVIL (BACHARELADO)',
            'ENGENHARIA DE COMPUTAÇÃO (BACHARELADO)',
            'ENGENHARIA DE PRODUÇÃO (BACHARELADO)',
            'ENGENHARIA DE REDES DE COMUNICAÇÃO (BACHARELADO)',
            'ENGENHARIA ELÉTRICA (BACHARELADO)',
            'ENGENHARIA FLORESTAL (BACHARELADO)',
            'ENGENHARIA MECATRÔNICA – CONTROLE E AUTOMAÇÃO (BACHARELADO)',
            'ENGENHARIA MECÂNICA (BACHARELADO)',
            'ENGENHARIA QUÍMICA (BACHARELADO)',
            'ENGENHARIAS – AEROESPACIAL / AUTOMOTIVA / ELETRÔNICA / ENERGIA / SOFTWARE (BACHARELADOS)',
            'ESTATÍSTICA (BACHARELADO)',
            'FARMÁCIA (BACHARELADO)',
            'FILOSOFIA (BACHARELADO/LICENCIATURA)',
            'FILOSOFIA (LICENCIATURA)',
            'FISIOTERAPIA (BACHARELADO)',
            'FONOAUDIOLOGIA (BACHARELADO)',
            'FÍSICA (BACHARELADO)',
            'GEOFÍSICA (BACHARELADO)',
            'GEOGRAFIA (BACHARELADO/LICENCIATURA)',
            'GEOLOGIA (BACHARELADO)',
            'GESTÃO AMBIENTAL (BACHARELADO)',
            'GESTÃO DE AGRONEGÓCIO (BACHARELADO)',
            'GESTÃO DE POLÍTICAS PÚBLICAS (BACHARELADO)',
            'GESTÃO DO AGRONEGÓCIO (BACHARELADO)',
            'HISTÓRIA (BACHARELADO/LICENCIATURA )',
            'HISTÓRIA (LICENCIATURA)',
            'JORNALISMO (BACHARELADO)',
            'LETRAS – PORTUGUÊS DO BRASIL COMO SEGUNDA LÍNGUA (LICENCIATURA)',
            'LETRAS – TRADUÇÃO ESPANHOL (BACHARELADO)',
            'LETRAS – TRADUÇÃO – FRANCÊS (BACHARELADO)',
            'LETRAS – TRADUÇÃO – INGLÊS (BACHARELADO)',
            'LICENCIATURA EM ARTES CÊNICAS',
            'LICENCIATURA EM CIÊNCIAS BIOLÓGICAS',
            'LICENCIATURA EM FÍSICA',
            'LICENCIATURA EM MATEMÁTICA',
            'LICENCIATURA EM QUÍMICA',
            'LÍNGUA E LITERATURA JAPONESA (LICENCIATURA)',
            'LÍNGUA ESPANHOLA E LITERATURA ESPANHOLA E HISPANO - AMERICANA (LICENCIATURA)',
            'LÍNGUA ESTRANGEIRA APLICADA – MULTILINGUISMO E SOCIEDADE DA INFORMAÇÃO (BACHARELADO)',
            'LÍNGUA FRANCESA E RESPECTIVA LITERATURA (BACHARELADO/LICENCIATURA)',
            'LÍNGUA INGLESA E RESPECTIVA LITERATURA (BACHARELADO/LICENCIATURA)',
            'LÍNGUA PORTUGUESA E RESPECTIVA LITERATURA (BACHARELADO/LICENCIATURA)',
            'LÍNGUA PORTUGUESA E RESPECTIVA LITERATURA (LICENCIATURA)',
            'MATEMÁTICA (BACHARELADO/LICENCIATURA)',
            'MEDICINA (BACHARELADO)',
            'MEDICINA VETERINÁRIA (BACHARELADO)',
            'MUSEOLOGIA (BACHARELADO)',
            'MÚSICA (BACHARELADO)',
            'MÚSICA (LICENCIATURA)',
            'NOTURNO ADMINISTRAÇÃO (BACHARELADO)',
            'NUTRIÇÃO (BACHARELADO)',
            'ODONTOLOGIA (BACHARELADO)',
            'PEDAGOGIA (LICENCIATURA)',
            'PSICOLOGIA (BACHARELADO / LICENCIATURA / PSICÓLOGO)',
            'QUÍMICA (BACHARELADO)',
            'QUÍMICA TECNOLÓGICA (BACHARELADO)',
            'RELAÇÕES INTERNACIONAIS (BACHARELADO)',
            'SAÚDE COLETIVA (BACHARELADO)',
            'SERVIÇO SOCIAL (BACHARELADO)',
            'TEORIA, CRÍTICA E HISTÓRIA DA ARTE (BACHARELADO)',
            'TERAPIA OCUPACIONAL (BACHARELADO)',
            'TURISMO (BACHARELADO)']

COURSE_NAMES = ['DIURNO ADMINISTRAÇÃO (BACHARELADO)',
                'NOTURNO ADMINISTRAÇÃO (BACHARELADO)',
                'CAMPUS UNB CEILÂNDIA (FCE) ENFERMAGEM (BACHARELADO)',
                'ENFERMAGEM (BACHARELADO)',
                'ENGENHARIAS – AEROESPACIAL / AUTOMOTIVA / ELETRÔNICA / ENERGIA / SOFTWARE (BACHARELADOS)',
                'CAMPUS UNB PLANALTINA (FUP) – DIURNO CIÊNCIAS NATURAIS (LICENCIATURA)',
                'CAMPUS UNB PLANALTINA (FUP) – NOTURNO CIÊNCIAS NATURAIS (LICENCIATURA)',
                'AGRONOMIA (BACHARELADO)',
                'ARQUITETURA E URBANISMO (BACHARELADO)',
                'ARQUIVOLOGIA (BACHARELADO)',
                'ARTES CÊNICAS - INTERPRETAÇÃO TEATRAL (BACHARELADO)',
                'ARTES VISUAIS (BACHARELADO)',
                'ARTES VISUAIS (LICENCIATURA)',
                'BIBLIOTECONOMIA (BACHARELADO)',
                'BIOTECNOLOGIA (BACHARELADO)',
                'CIÊNCIA DA COMPUTAÇÃO (BACHARELADO)',
                'CIÊNCIA POLÍTICA (BACHARELADO)',
                'CIÊNCIAS AMBIENTAIS (BACHARELADO)',
                'CIÊNCIAS BIOLÓGICAS (BACHARELADO)',
                'CIÊNCIAS CONTÁBEIS (BACHARELADO)',
                'CIÊNCIAS ECONÔMICAS (BACHARELADO)',
                'CIÊNCIAS SOCIAIS – ANTROPOLOGIA / SOCIOLOGIA (BACHARELADO/LICENCIATURA)',
                'COMPUTAÇÃO (LICENCIATURA)',
                'COMUNICAÇÃO ORGANIZACIONAL (BACHARELADO)',
                'COMUNICAÇÃO SOCIAL - PUBLICIDADE E PROPAGANDA (BACHARELADO)',
                'COMUNICAÇÃO SOCIAL – AUDIOVISUAL (BACHARELADO)',
                'DESIGN – PROGRAMAÇÃO VISUAL/PROJETO DO PRODUTO (BACHARELADO)',
                'DIREITO (BACHARELADO)',
                'EDUCAÇÃO FÍSICA (BACHARELADO)',
                'EDUCAÇÃO FÍSICA (LICENCIATURA)',
                'ENGENHARIA AMBIENTAL (BACHARELADO)',
                'ENGENHARIA CIVIL (BACHARELADO)',
                'ENGENHARIA DE COMPUTAÇÃO (BACHARELADO)',
                'ENGENHARIA DE PRODUÇÃO (BACHARELADO)',
                'ENGENHARIA DE REDES DE COMUNICAÇÃO (BACHARELADO)',
                'ENGENHARIA ELÉTRICA (BACHARELADO)',
                'ENGENHARIA FLORESTAL (BACHARELADO)',
                'ENGENHARIA MECATRÔNICA – CONTROLE E AUTOMAÇÃO (BACHARELADO)',
                'ENGENHARIA MECÂNICA (BACHARELADO)',
                'ENGENHARIA QUÍMICA (BACHARELADO)',
                'ESTATÍSTICA (BACHARELADO)',
                'FARMÁCIA (BACHARELADO)',
                'FILOSOFIA (BACHARELADO/LICENCIATURA)',
                'FILOSOFIA (LICENCIATURA)',
                'FISIOTERAPIA (BACHARELADO)',
                'FONOAUDIOLOGIA (BACHARELADO)',
                'FÍSICA (BACHARELADO)',
                'GEOFÍSICA (BACHARELADO)',
                'GEOGRAFIA (BACHARELADO/LICENCIATURA)',
                'GEOLOGIA (BACHARELADO)',
                'GESTÃO AMBIENTAL (BACHARELADO)',
                'GESTÃO DE AGRONEGÓCIO (BACHARELADO)',
                'GESTÃO DE POLÍTICAS PÚBLICAS (BACHARELADO)',
                'GESTÃO DO AGRONEGÓCIO (BACHARELADO)',
                'HISTÓRIA (BACHARELADO/LICENCIATURA )',
                'HISTÓRIA (LICENCIATURA)',
                'JORNALISMO (BACHARELADO)',
                'LETRAS – PORTUGUÊS DO BRASIL COMO SEGUNDA LÍNGUA (LICENCIATURA)',
                'LETRAS – TRADUÇÃO ESPANHOL (BACHARELADO)',
                'LETRAS – TRADUÇÃO – FRANCÊS (BACHARELADO)',
                'LETRAS – TRADUÇÃO – INGLÊS (BACHARELADO)',
                'LICENCIATURA EM ARTES CÊNICAS',
                'LICENCIATURA EM CIÊNCIAS BIOLÓGICAS',
                'LICENCIATURA EM FÍSICA',
                'LICENCIATURA EM MATEMÁTICA',
                'LICENCIATURA EM QUÍMICA',
                'LÍNGUA E LITERATURA JAPONESA (LICENCIATURA)',
                'LÍNGUA ESPANHOLA E LITERATURA ESPANHOLA E HISPANO - AMERICANA (LICENCIATURA)',
                'LÍNGUA ESTRANGEIRA APLICADA – MULTILINGUISMO E SOCIEDADE DA INFORMAÇÃO (BACHARELADO)',
                'LÍNGUA FRANCESA E RESPECTIVA LITERATURA (BACHARELADO/LICENCIATURA)',
                'LÍNGUA INGLESA E RESPECTIVA LITERATURA (BACHARELADO/LICENCIATURA)',
                'LÍNGUA PORTUGUESA E RESPECTIVA LITERATURA (BACHARELADO/LICENCIATURA)',
                'LÍNGUA PORTUGUESA E RESPECTIVA LITERATURA (LICENCIATURA)',
                'MATEMÁTICA (BACHARELADO/LICENCIATURA)',
                'MEDICINA (BACHARELADO)',
                'MEDICINA VETERINÁRIA (BACHARELADO)',
                'MUSEOLOGIA (BACHARELADO)',
                'MÚSICA (BACHARELADO)',
                'MÚSICA (LICENCIATURA)',
                'NUTRIÇÃO (BACHARELADO)',
                'ODONTOLOGIA (BACHARELADO)',
                'PEDAGOGIA (LICENCIATURA)',
                'PSICOLOGIA (BACHARELADO / LICENCIATURA / PSICÓLOGO)',
                'QUÍMICA (BACHARELADO)',
                'QUÍMICA TECNOLÓGICA (BACHARELADO)',
                'RELAÇÕES INTERNACIONAIS (BACHARELADO)',
                'SAÚDE COLETIVA (BACHARELADO)',
                'SERVIÇO SOCIAL (BACHARELADO)',
                'TEORIA, CRÍTICA E HISTÓRIA DA ARTE (BACHARELADO)',
                'TERAPIA OCUPACIONAL (BACHARELADO)',
                'TURISMO (BACHARELADO)']
