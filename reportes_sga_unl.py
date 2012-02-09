
################################################################################################
Consulta para buscar los estudiantes por provincia

EJEMPLO:

tendremos que anteriormente establecer:
- el estado de matricula, 
- bueno el estado de papeleta que en este caso es pagada
- la oferta academica a la que queremos hacer referencia
- y porsupuesto la provincia que esta dentro de like y en este caso es "El Oro"

orences=Matricula.query.join(['estudiante','datos_personales'],'paralelo').join('papeleta').filter(and_(DatosPersonales.provincia_procedencia.like(u'%%El Oro%%'),Papeleta.estado == u'pagada', Matricula.estado == estado, Paralelo.oferta_academica == oa)).distinct().all()
 
################################################################################################

Consulta de Estudiantes extranjeros

EJEMPLO

tendremos que anteriormente establecer:
- el estado de matricula, 
- bueno el estado de papeleta que en este caso es pagada
- la oferta academica a la que queremos hacer referencia
- dentro de like ponemos "extranjeros" para que busque 


extranjeros=Matricula.query.join(['estudiante'],'paralelo').join('papeleta').filter(and_(Estudiante.procedencia.like(u'%%extranjero%%'),Papeleta.estado == u'pagada', Matricula.estado == estado, Paralelo.oferta_academica == oa)).distinct().all()

################################################################################################

Consulta de todos los estudiantes de la UNL

tot=Matricula.query.join(['estudiante','datos_personales'],'paralelo').join('papeleta').filter(and_(or_(Papeleta.estado == u'pagada',Papeleta.estado == u'ajustada'), Matricula.estado == estado, Paralelo.oferta_academica == oa)).distinct().all()

ecuatorianos=[]

colombianos=[]

peruanos=[]

varios=[]

for m in tot:
    if m.estudiante.datos_personales.pais_procedencia==u'Ecuador':
        ecuatorianos.append(m)
    if m.estudiante.datos_personales.pais_procedencia==u'Peru':
        peruanos.append(m)
    if m.estudiante.datos_personales.pais_procedencia==u'Colombia':
        colombianos.append(m)
    if m.estudiante.datos_personales.pais_procedencia!=u'Ecuador' and m.estudiante.datos_personales.pais_procedencia!=u'Colombia' and m.estudiante.datos_personales.pais_procedencia!=u'Peru':
        varios.append(m)


OJO varios....!!!!!!!!!!!!!!!!!

SALIA BEATRIZ OTHMAN SIVISAKA cedula: 1104342603 carrera: Ingeniería en Contabilidad y Auditoría Pais: Russia
ERICK JAVIER TRUJILLO RODRÍGUEZ cedula: 1720132925 carrera: Derecho Pais: Russia
SADIA PAOLA JIMENEZ MALDONADO cedula: 1104648900 carrera: Psicología Clínica Pais: Dominican Republic

for i in extranjeros:
    if i.estudiante.datos_personales.pais_procedencia==u'Ecuador':
        extranjerosecuador.append(i)
        
OJO en nacionalidad tienen otra pero tienen pais procedencia Ecuador

JOELI ISAI MOGOLLON VILCHEZ cedula: 44590110 carrera: Medicina Humana Pais: Ecuador
ROGGER ORLANDO GENOVES MORAN cedula: 45317526 carrera: Medicina Humana Pais: Ecuador
RODOLFO NICOLAS DAZA SALCEDO cedula: 84104221 carrera: Enfermería Pais: Ecuador
CAROLINA GRACIELA PINO FARÍAS cedula: 172895247 carrera: Medicina Humana Pais: Ecuador
JUAN CARLOS VILLALOBOS FLORES cedula: 44099848 carrera: Medicina Humana Pais: Ecuador


################################################################################

    @expose(template="sga.templates.reportes.principalreportes")
    def generarporanio(self):
        """
            borrar esta operacion despues
        """
        oa = OfertaAcademica.get(25)
        lista_c_oferta = oa.get_carreras_programas()
        estado=EstadoMatricula.get_by(estado=u'EstadoMatriculaMatriculada')
        print estado
        totalestudiantes=0
        totalhombres=0
        totalmujeres=0
        for a in Area.query.all():
            lista_carreras=[]
            for n in a.niveles:
                    for c in n.carreras_programas:
                            lista_carreras.append(c)
            lista_final = list(set(lista_carreras)&set(lista_c_oferta))
            for carrera in lista_final:
                    hombrescarrera=0
                    mujerescarrera=0
                    totalcarrera=0
                    print "###########################################"
                    print carrera.nombre
                    primero=Matricula.query.join(['modulo','carrera_programa', 'nivel'],'paralelo').join('papeleta').filter(CarreraPrograma.nombre==carrera.nombre).filter(and_(or_(Papeleta.estado == u'pagada',Papeleta.estado == u'ajustada'), Matricula.estado == estado, or_(Modulo.numero==u'1',Modulo.numero==u'2'),Paralelo.oferta_academica == oa)).distinct().all()                                       
                    segundo=Matricula.query.join(['modulo','carrera_programa', 'nivel'],'paralelo').join('papeleta').filter(CarreraPrograma.nombre==carrera.nombre).filter(and_(or_(Papeleta.estado == u'pagada',Papeleta.estado == u'ajustada'), Matricula.estado == estado, or_(Modulo.numero==u'3',Modulo.numero==u'4'),Paralelo.oferta_academica == oa)).distinct().all()
                    tercero=Matricula.query.join(['modulo','carrera_programa', 'nivel'],'paralelo').join('papeleta').filter(CarreraPrograma.nombre==carrera.nombre).filter(and_(or_(Papeleta.estado == u'pagada',Papeleta.estado == u'ajustada'), Matricula.estado == estado, or_(Modulo.numero==u'5',Modulo.numero==u'6'),Paralelo.oferta_academica == oa)).distinct().all()
                    cuarto=Matricula.query.join(['modulo','carrera_programa', 'nivel'],'paralelo').join('papeleta').filter(CarreraPrograma.nombre==carrera.nombre).filter(and_(or_(Papeleta.estado == u'pagada',Papeleta.estado == u'ajustada'), Matricula.estado == estado, or_(Modulo.numero==u'7',Modulo.numero==u'8'),Paralelo.oferta_academica == oa)).distinct().all()
                    quinto=Matricula.query.join(['modulo','carrera_programa', 'nivel'],'paralelo').join('papeleta').filter(CarreraPrograma.nombre==carrera.nombre).filter(and_(or_(Papeleta.estado == u'pagada',Papeleta.estado == u'ajustada'), Matricula.estado == estado, or_(Modulo.numero==u'9',Modulo.numero==u'10'),Paralelo.oferta_academica == oa)).distinct().all()
                    sexto=Matricula.query.join(['modulo','carrera_programa', 'nivel'],'paralelo').join('papeleta').filter(CarreraPrograma.nombre==carrera.nombre).filter(and_(or_(Papeleta.estado == u'pagada',Papeleta.estado == u'ajustada'), Matricula.estado == estado, or_(Modulo.numero==u'11',Modulo.numero==u'12'),Paralelo.oferta_academica == oa)).distinct().all()
                    h1 = 0
                    m1 = 0
                    t1 = 0
                    h2 = 0
                    m2 = 0
                    t2 = 0
                    h3 = 0
                    m3 = 0
                    t3 = 0
                    h4 = 0
                    m4 = 0
                    t4 = 0
                    h5 = 0
                    m5 = 0
                    t5 = 0
                    h6 = 0
                    m6 = 0
                    t6 = 0
                    for m in primero:
                        if m.estudiante.datos_personales.genero==u'MASCULINO' or m.estudiante.datos_personales.genero.lower()==u'masculino':
                            h1+=1
                        else:
                            m1+=1
                    for m in segundo:
                        if m.estudiante.datos_personales.genero==u'MASCULINO' or m.estudiante.datos_personales.genero.lower()==u'masculino':
                            h2+=1
                        else:
                            m2+=1
                    for m in tercero:
                        if m.estudiante.datos_personales.genero==u'MASCULINO' or m.estudiante.datos_personales.genero.lower()==u'masculino':
                            h3+=1
                        else:
                            m3+=1
                    for m in cuarto:
                        if m.estudiante.datos_personales.genero==u'MASCULINO' or m.estudiante.datos_personales.genero.lower()==u'masculino':
                            h4+=1
                        else:
                            m4+=1
                    for m in quinto:
                        if m.estudiante.datos_personales.genero==u'MASCULINO' or m.estudiante.datos_personales.genero.lower()==u'masculino':
                            h5+=1
                        else:
                            m5+=1
                    for m in sexto:
                        if m.estudiante.datos_personales.genero==u'MASCULINO' or m.estudiante.datos_personales.genero.lower()==u'masculino':
                            h6+=1
                        else:
                            h6+=1
                            
                    t1=h1+m1
                    t2=h2+m2
                    t3=h3+m3
                    t4=h4+m4
                    t5=h5+m5
                    t6=h6+m6
                    datos=[str(h1+h2+h3+h4+h5+h6),str(m1+m2+m3+m4+m5+m6),str(t1+t2+t3+t4+t5+t6),str(h1),str(m1),str(t1),str(h2),str(m2),str(t2),str(h3),str(m3),str(t3),str(h4),str(m4),str(t4),str(h5),str(m5),str(t5),str(h6),str(m6),str(t6)]
                    if a.siglas=='AEAC':
                        file = open("/home/marcoxavi/Escritorio/Conesup4/AEAC/poranio%s"%carrera.nombre,"w")
                    if a.siglas=='AJSA':
                        file = open("/home/marcoxavi/Escritorio/Conesup4/AJSA/poranio%s"%carrera.nombre,"w")
                    if a.siglas=='ASH':
                        file = open("/home/marcoxavi/Escritorio/Conesup4/ASH/poranio%s"%carrera.nombre,"w")
                    if a.siglas=='AEIRNNR':
                        file = open("/home/marcoxavi/Escritorio/Conesup4/AEIRNNR/poranio%s"%carrera.nombre,"w")
                    if a.siglas=='AARNR':
                        file = open("/home/marcoxavi/Escritorio/Conesup4/AARNR/poranio%s"%carrera.nombre,"w")
                    if a.siglas=='PREUNIVERSITARIO':
                        file = open("/home/marcoxavi/Escritorio/Conesup4/PREUNIVERSITARIO/poranio%s"%carrera.nombre,"w")
                    for v in datos:
                        if v is not None:
                                if len(v)==0:
                                        file.write("vacio")
                                else:
                                        file.write(v.encode('utf-8'))
                        else:
                                file.write("vacio")
                        file.write(",")
                    file.close()
                    hombrescarrera=hombrescarrera+h1+h2+h3+h4+h5+h6
                    mujerescarrera=mujerescarrera+m1+m2+m3+m4+m5+m6
                    totalcarrera=t1+t2+t3+t4+t5+t6
                    totalhombres+=hombrescarrera
                    totalmujeres+=mujerescarrera
                    totalestudiantes+= totalcarrera
                    print "Hombres: %s Mujeres: %s Total: %s" %(hombrescarrera,mujerescarrera,totalcarrera)
        print "Total Hombres: %s,Total Mujeres: %s,Total de Estudiantes: %s" %(totalhombres,totalmujeres,totalestudiantes)
        flash(u'Se termino el proceso Hombres: %s, Mujeres: %s Total: %s' %(totalhombres, totalmujeres, totalestudiantes))
        raise redirect("/reportes")
    
    @expose(template="sga.templates.reportes.principalreportes")
    def generarporpais(self):
        """
            borrar esta operacion despues
        """
        oa = OfertaAcademica.get(25)
        lista_c_oferta = oa.get_carreras_programas()
        estado=EstadoMatricula.get_by(estado=u'EstadoMatriculaMatriculada')
        print estado
        listatotal=[]
        totalestudiantes=0
        totalhombres=0
        totalmujeres=0
        for a in Area.query.all():
            lista_carreras=[]
            for n in a.niveles:
                    for c in n.carreras_programas:
                            lista_carreras.append(c)
            lista_final = list(set(lista_carreras)&set(lista_c_oferta))
            for carrera in lista_final:
                    hombresperu=0
                    mujeresperu=0
                    totalesperu=0
                    hombrescolombia=0
                    mujerescolombia=0
                    totalescolombia=0
                    hombresecuador=0
                    mujeresecuador=0
                    totalesecuador=0
                    print "###########################################"
                    print carrera.nombre
                    
                    
                    peru=Matricula.query.join(['modulo','carrera_programa', 'nivel'],'paralelo').join(['estudiante','datos_personales']).join('papeleta').filter(CarreraPrograma.nombre==carrera.nombre).filter(DatosPersonales.pais_procedencia==u'Peru').filter(and_(or_(Papeleta.estado == u'pagada',Papeleta.estado == u'ajustada'), Matricula.estado == estado, Paralelo.oferta_academica == oa)).distinct().all()                                       
                    colombia=Matricula.query.join(['modulo','carrera_programa', 'nivel'],'paralelo').join(['estudiante','datos_personales']).join('papeleta').filter(CarreraPrograma.nombre==carrera.nombre).filter(DatosPersonales.pais_procedencia==u'Colombia').filter(and_(or_(Papeleta.estado == u'pagada',Papeleta.estado == u'ajustada'), Matricula.estado == estado, Paralelo.oferta_academica == oa)).distinct().all()                                       
                    ecuador=Matricula.query.join(['modulo','carrera_programa', 'nivel'],'paralelo').join(['estudiante','datos_personales']).join('papeleta').filter(CarreraPrograma.nombre==carrera.nombre).filter(DatosPersonales.pais_procedencia==u'Ecuador').filter(and_(or_(Papeleta.estado == u'pagada',Papeleta.estado == u'ajustada'), Matricula.estado == estado, Paralelo.oferta_academica == oa)).distinct().all()                                       
                    hombrespe = 0
                    mujerespe = 0
                    totalespe = 0
                    hombresco = 0
                    mujeresco = 0
                    totalesco = 0
                    hombresec = 0
                    mujeresec = 0
                    totalesec = 0
                    
                    for m in peru:
                        if m.estudiante.datos_personales.genero==u'MASCULINO' or m.estudiante.datos_personales.genero.lower()==u'masculino':
                            hombrespe+=1
                        else:
                            mujerespe+=1
                    for m in colombia:
                        if m.estudiante.datos_personales.genero==u'MASCULINO' or m.estudiante.datos_personales.genero.lower()==u'masculino':
                            hombresco+=1
                        else:
                            mujeresco+=1
                    for m in ecuador:
                        if m.estudiante.datos_personales.genero==u'MASCULINO' or m.estudiante.datos_personales.genero.lower()==u'masculino':
                            hombresec+=1
                        else:
                            mujeresec+=1
                    
                            
                    totalespe+=hombrespe+mujerespe
                    totalesco+=hombresco+mujeresco
                    totalesec+=hombresec+mujeresec
                    datos=[a.siglas,carrera.nombre,str(hombresco+hombresec+hombrespe),str(mujeresco+mujerespe+mujeresec),str(totalesco+totalespe+totalesec),str(hombresec),str(mujeresec),str(totalesec),str(hombresco),str(mujeresco),str(totalesco),str(hombrespe),str(mujerespe),str(totalespe)]
                    listatotal.append(datos)
                    #if a.siglas=='AEAC':
                    #    file = open("/home/marcoxavi/Escritorio/Conesup3/AEAC/%s"%carrera.nombre,"w")
                    #if a.siglas=='AJSA':
                    #    file = open("/home/marcoxavi/Escritorio/Conesup3/AJSA/%s"%carrera.nombre,"w")
                    #if a.siglas=='ASH':
                    #    file = open("/home/marcoxavi/Escritorio/Conesup3/ASH/%s"%carrera.nombre,"w")
                    #if a.siglas=='AEIRNNR':
                    #    file = open("/home/marcoxavi/Escritorio/Conesup3/AEIRNNR/%s"%carrera.nombre,"w")
                    #if a.siglas=='AARNR':
                    #    file = open("/home/marcoxavi/Escritorio/Conesup3/AARNR/%s"%carrera.nombre,"w")
                    #if a.siglas=='PREUNIVERSITARIO':
                    #    file = open("/home/marcoxavi/Escritorio/Conesup3/PREUNIVERSITARIO/%s"%carrera.nombre,"w")

                    totalhombres+=hombresco+hombrespe+hombresec
                    totalmujeres+=mujeresco+mujerespe+mujeresec
                    totalestudiantes+= totalhombres+totalmujeres
                    print "Hombres Ecuador: %s Hombres Peru: %s Hombres Colombia: %s" %(hombresec,hombrespe,hombresco)
                    print "Mujeres Ecuador: %s Mujeres Peru: %s Mujeres Colombia: %s" %(mujeresec,mujerespe,mujeresco)
        listatotal.sort()
        file = open("/home/marcoxavi/Escritorio/Conesup3/datosporpais","w")
        for data in listatotal:
            for v in data:
                if v is not None:
                        if len(v)==0:
                                file.write("vacio")
                        else:
                                file.write(v.encode('utf-8'))
                else:
                        file.write("vacio")
                file.write(",")
            file.write("\n")    
        file.close()
        
        print "Total Hombres: %s,Total Mujeres: %s,Total de Estudiantes: %s" %(totalhombres,totalmujeres,totalestudiantes)
        flash(u'Se termino el proceso Hombres: %s, Mujeres: %s Total: %s' %(totalhombres, totalmujeres, totalestudiantes))
        raise redirect("/reportes")    

######################################## Generar Datos de Estudiantes por Area #####################3
        oa = OfertaAcademica.get(25)
        lista_c_oferta = oa.get_carreras_programas()
        estado=EstadoMatricula.get_by(estado=u'EstadoMatriculaMatriculada')
            
        lista_carreras=[]
        for n in a.niveles:
                for c in n.carreras_programas:
                        lista_carreras.append(c)
        lista_final = list(set(lista_carreras)&set(lista_c_oferta))
        
        #NOTA: "a" es el area, entonces todo esto que sigue deberia estar en un for para recorrer cada
        #      Area
        for carrera in lista_final:
            print carrera.nombre                      
            listatotal= [(unicode('UNIVERSIDAD NACIONAL DE LOJA'), unicode(m.estudiante.apellidos), unicode(m.estudiante.nombres), unicode(m.estudiante.cedula), unicode(m.estudiante.datos_personales.fecha_nacimiento), unicode(m.estudiante.datos_personales.nacionalidad), unicode(m.estudiante.datos_personales.pais_procedencia), unicode(m.id), unicode(m.modulo.carrera_programa.nivel.area.nombre), unicode(m.modulo.carrera_programa.nombre), unicode(m.estudiante.datos_personales.provincia_actual), unicode(m.modulo.carrera_programa.modalidad), unicode(m.modulo.numero), unicode(m.paralelo.nombre)) for m in Matricula.query.join(['modulo','carrera_programa', 'nivel'],'paralelo').join(['estudiante','datos_personales']).join('papeleta').filter(CarreraPrograma.nombre==carrera.nombre).filter(and_(or_(Papeleta.estado == u'pagada',Papeleta.estado == u'ajustada'), Matricula.estado == estado, Paralelo.oferta_academica == oa)).distinct().all()]
            if a.siglas=='ASH':
                file = open("/home/marcoxavi/Escritorio/Reportes/ASH/%s" %carrera.nombre,"w")
            listatotal.sort()
            for data in listatotal:
                for v in data:
                    if v is not None:
                            if len(v)==0:
                                    file.write("vacio")
                            else:
                                    file.write(v.encode('utf-8'))
                    else:
                            file.write("vacio")
                    file.write(",")
                file.write("\n")    
            file.close()
            
#############################################################################

Todos los Estudiantes
#lista_estudiantes= [(unicode(m.estudiante.apellidos.upper()), unicode(m.estudiante.nombres.upper()), "'%s" %unicode(m.estudiante.cedula), unicode(m.modulo.carrera_programa.nombre), unicode(m.modulo.numero), unicode(m.paralelo.nombre), unicode(m.paralelo.seccion), unicode(m.estudiante.datos_personales.direccion_actual), unicode(m.estudiante.datos_personales.telefono)) for m in Matricula.query.join(['modulo','carrera_programa', 'nivel'],'paralelo').join(['estudiante','datos_personales']).join('papeleta').filter(and_(or_(Papeleta.estado == u'pagada',Papeleta.estado == u'ajustada'), Nivel.area == area, Matricula.estado == estado, Paralelo.oferta_academica == oa)).distinct().all()]
| Nombres | Apellidos | Cédula | Matrícula | Direccion Actual|

oa = OfertaAcademica.get(25)
estado=EstadoMatricula.get_by(estado=u'EstadoMatriculaMatriculada')
areas = Area.query.all()
for area in areas:
    print "Iniciamos con el %s" %area.nombre    
    lista_estudiantes= [(unicode(m.estudiante.apellidos.upper()), unicode(m.estudiante.nombres.upper()), "'%s" %unicode(m.estudiante.cedula), unicode(m.id), unicode(m.modulo.carrera_programa.nivel.area.nombre), unicode(m.modulo.carrera_programa.nombre), unicode(m.estudiante.datos_personales.direccion_actual)) for m in Matricula.query.join(['modulo','carrera_programa', 'nivel'],'paralelo').join(['estudiante','datos_personales']).join(['modulo','carrera_programa']).join('papeleta').filter(and_(or_(Papeleta.estado == u'pagada',Papeleta.estado == u'ajustada'), Nivel.area == area, Matricula.estado == estado, Paralelo.oferta_academica == oa)).distinct().all()]
    lista_estudiantes.sort()    
    file = open("/home/marcoxavi/Escritorio/Reportes/CedulaCompleta/estudiantesdireccion%s" %area.nombre,"w")    
    for data in lista_estudiantes:
        for v in data:
            if v is not None:
                    file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")
    file.close()
    print "Se termino el %s" %area.nombre

#########################################################
import time
fin =60
def procesando(fin=None):
    for i in range(1,fin+1):
        clear    
        if i%3 == 1:
            comenzamos="Procesando ."
        if i%3 == 2:
            comenzamos="Procesando .."
        if i%3 == 0:
            comenzamos="Procesando ..."        
        print comenzamos
        print i
        time.sleep(0.333)
        if i==fin:
            clear
            print "Proceso Terminado... Gracias...!!!"
            
            
### lista de estudiantes de la MED
#carreras = Lista de Carreras que desemos buscar
estado = EstadoMatricula.get_by(estado=u"EstadoMatriculaMigrada")
for carrera in carreras:
    print "Comenzo la Carrera de %s" %carrera.nombre
    encabezado=[(u'APELLIDOS',u'NOMBRES',u'CEDULA',u'MATRICULA',u'AREA',u'CARRERA',u'MODULO')]
    lista_estudiantes = [(unicode(m.estudiante.apellidos.upper()), unicode(m.estudiante.nombres.upper()), "'%s" %unicode(m.estudiante.cedula), unicode(m.id), unicode(m.modulo.carrera_programa.nivel.area.nombre.upper()), unicode(m.modulo.carrera_programa.nombre.upper()), unicode(m.modulo.numero)) for m in Matricula.query.join(["modulo","carrera_programa"],"paralelo").filter(Matricula.estado == estado).filter(CarreraPrograma.modalidad==u"distancia").filter(CarreraPrograma.id==carrera.id).distinct().all()]
    lista_estudiantes.sort()
    lista_estudiantes = encabezado + lista_estudiantes
    file = open("/home/marcoxavi/Escritorio/Reportes/MED/estudiantesMED%s" %carrera.nombre,"w")    
    for data in lista_estudiantes:
        for v in data:
            if v is not None:
                    file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")
    file.close()
    print "Se termino la Carrera de %s" %carrera.nombre
    
### Populate da actualizador de datos para el CNE
file  = open("/home/marcoxavi/CNE/UNL/UNL02.txt")
while 1:
    s = file.readline()
    if not s:
        break    
    linea = s.split(",")
    if CertificadoVotacion.get_by(cedula = linea[0]) is None:
        ced = CertificadoVotacion()
        ced.cedula=linea[0]
        ced.codigo1=linea[3]
        ced.codigo2=linea[4][:-2]
        session.flush()


file.close()

###############################################################################################################
CONSULTAS DEL PERIODO MARZO JULIO 2009
Oferta Acedemica # 26
oa = OfertaAcademica.get(26)
numero_total = Matricula.query.options(eagerload('papeleta')).join(['modulo','carrera_programa','nivel']).join('paralelo').join('expediente').join('papeleta').filter(and_(or_(Papeleta.estado==u'pagada',Papeleta.estado==u'ajustada'), Matricula.estado==estado, Paralelo.oferta_academica == oa)).distinct().count()
sin_costo= Matricula.query.options(eagerload('papeleta')).join(['modulo','carrera_programa','nivel']).join('paralelo').join('expediente').join('papeleta').filter(and_(or_(Papeleta.estado==u'pagada',Papeleta.estado==u'ajustada'), Papeleta.costo_total==0,Matricula.estado==estado, Paralelo.oferta_academica == oa)).distinct().all()
con_costo= Matricula.query.options(eagerload('papeleta')).join(['modulo','carrera_programa','nivel']).join('paralelo').join('expediente').join('papeleta').filter(and_(or_(Papeleta.estado==u'pagada',Papeleta.estado==u'ajustada'), Papeleta.costo_total>0,Matricula.estado==estado, Paralelo.oferta_academica == oa)).distinct().all()
pf=0
extranjeros=0
otros=0
for m in con_costo:
    if m.estudiante.procedencia==u'profesionales':
        pf+=1
    else:
        if m.estudiante.procedencia==u'extranjeros':
            extranjeros+=1
        else:
            otros+=1


##################################################################3
"""
    ESTUDIANTES APROBADOS EN MEDICINA EN UNA UNIDAD QUE ESTABA SIN APROBACION OBLIGATORIA
"""
oa=OfertaAcademica.get(25)
unidad=Unidad.get(543)
estado = EstadoMatricula.get_by(estado = u"EstadoMatriculaAprobada")
numero_total =[ m for m in Matricula.query.options(eagerload('papeleta')).join(['paralelo','plan_estudio']).join(['modulo','carrera_programa','nivel','area']).join('paralelo').join('expediente').join('papeleta').filter(and_(or_(Papeleta.estado==u'pagada',Papeleta.estado==u'ajustada'),Modulo.numero==u'1' , Area.siglas==u'ASH',Matricula.estado==estado, PlanEstudio.id==idpl,Paralelo.oferta_academica == oa)).distinct().all() if m.paralelo.plan_estudio.calcular(m)[unidad]['nota'] < 7]


####################################################################

"""
    ESTUDIANTES DEL PERIODO ACADEMICO PREGRADO SEPTIEMBRE 2008 FEBRERO 2009
"""

aprobada = EstadoMatricula.get_by(estado = u"EstadoMatriculaAprobada")
reprobada = EstadoMatricula.get_by(estado = u"EstadoMatriculaReprobada")
matriculada = EstadoMatricula.get_by(estado = u"EstadoMatriculaMatriculada")
#formato 1
num_estudiantes=[(u"%s %s" %(m.estudiante.apellidos.upper(),m.estudiante.nombres.upper()),u"'%s" %m.estudiante.cedula,u"%s" %m.estudiante.datos_personales.canton_actual,u"%s" %m.estudiante.datos_personales.canton_procedencia,u"'%s" %m.estudiante.datos_personales.celular,u"%s" %m.estudiante.datos_personales.ciudad_actual,u"%s" %m.estudiante.datos_personales.ciudad_procedencia,u"%s" %m.estudiante.datos_personales.direccion_actual,u"%s" %m.estudiante.datos_personales.direccion_padre,u"%s" %m.estudiante.datos_personales.direccion_madre,u"%s" %m.estudiante.datos_personales.direccion_procedencia,u"%s" %m.estudiante.datos_personales.email,u"%s" %m.estudiante.datos_personales.estado_civil,str(m.estudiante.datos_personales.fecha_nacimiento),u"%s" %m.estudiante.datos_personales.genero,u"'%s" %m.estudiante.datos_personales.libreta_militar,u"%s" %m.estudiante.datos_personales.lugar_trabajo_conyuge,u"%s" %m.estudiante.datos_personales.lugar_trabajo_padre,u"%s" %m.estudiante.datos_personales.lugar_trabajo_madre,u"%s" %m.estudiante.datos_personales.nacionalidad,u"%s" %m.estudiante.datos_personales.nombre_conyuge,u"%s" %m.estudiante.datos_personales.nombres_madre,u"%s" %m.estudiante.datos_personales.nombres_padre,u"'%s" %m.estudiante.datos_personales.numero_hijos,u"%s" %m.estudiante.datos_personales.ocupacion,u"%s" %m.estudiante.datos_personales.ocupacion_conyuge,u"%s" %m.estudiante.datos_personales.pais_actual,u"%s" %m.estudiante.datos_personales.pais_procedencia,u"%s" %m.estudiante.datos_personales.provincia_actual,u"%s" %m.estudiante.datos_personales.provincia_procedencia,u"'%s" %m.estudiante.datos_personales.telefono,u"'%s" %m.estudiante.datos_personales.telefono_padre,u"'%s" %m.estudiante.datos_personales.telefono_madre,u"%s" %m.estudiante.datos_personales.tipo_sangre,u"%s" %m.modulo.carrera_programa.nivel.area.nombre,u"%s" %m.modulo.carrera_programa.nombre,u"%s" %m.modulo.numero,u"%s" %anio(m.modulo.numero)) for m in Matricula.query.join(['modulo','carrera_programa', 'nivel'],'paralelo').join(['estudiante','datos_personales']).join(['modulo','carrera_programa']).join(['papeleta','periodo']).filter(and_(or_(Papeleta.estado == u'pagada',Papeleta.estado == u'ajustada'), or_(Matricula.estado == matriculada, Matricula.estado == aprobada, Matricula.estado == reprobada), PeriodoMatricula.oferta_academica == oa)).distinct().all()]
#formato 2
num_estudiantes=[(u"%s %s" %(m.estudiante.apellidos.upper(),m.estudiante.nombres.upper()),u"-",u"SIERRA",u"LOJA",u"LOJA",u"-",u"LOJA",u"%s" %m.modulo.carrera_programa.nombre,u"-",u"MATRIZ",u"%s" %m.modulo.carrera_programa.nivel.area.nombre,u"%s" %m.modulo.carrera_programa.nombre,u"TERCER NIVEL",u"PRESENCIAL",u"SEMESTRAL",u"%s" %anio(m.modulo.numero),u"%s" %beca(m),u"'15/09/2009",u"%s" %m.estudiante.datos_personales.provincia_procedencia,u"%s" %m.estudiante.datos_personales.canton_procedencia,u"-",str(m.estudiante.datos_personales.fecha_nacimiento),u"'%s" %m.estudiante.cedula,u"'%s" %m.id,u"%s" %m.estudiante.datos_personales.nacionalidad,u"%s" %m.estudiante.datos_personales.genero,u"Septiembre 2008 - Febrero 2009") for m in Matricula.query.join(['modulo','carrera_programa', 'nivel'],'paralelo').join(['estudiante','datos_personales']).join(['modulo','carrera_programa']).join(['papeleta','periodo']).filter(and_(or_(Papeleta.estado == u'pagada',Papeleta.estado == u'ajustada'), or_(Matricula.estado == matriculada, Matricula.estado == aprobada, Matricula.estado == reprobada), PeriodoMatricula.oferta_academica == oa)).distinct().all()]


def anio(n):
    
    if n =='1' or n=='2':
        anio=u'1'
    if n =='3' or n=='4':
        anio=u'2'
    if n =='5' or n=='6':
        anio=u'3'
    if n =='7' or n=='8':
        anio=u'4'
    if n =='9' or n=='10':
        anio=u'5'
    if n =='11' or n=='12':
        anio=u'6'
    if n =='13' or n=='14':
        anio=u'7'
    return anio

def beca(m):
    b = u"NO"
    if m.estudiante.ficha_socio_economica.beca is not None:
        b = u"BECA TIPO %s" %m.estudiante.ficha_socio_economica.beca.tipo
    return b

def equivalencia(n):
    """
        permite devolver el equivalente de la nota ej: buena, muy buena, etc
    """
    msj = u""
    if n >= 7 and n < 8:
        msj = u", equivalente a Bueno"
    if n >= 8 and n < 9:
        msj = u", equivalente a Muy Bueno"
    if n >= 9 and n <= 10:
        msj = u", equivalente a Sobresaliente"
    return msj


### Muestra el listado de todas las carreras del usuario, los titulos que son afines con la carrera
### y el numero de titulos que son afines
user = User.get_by(user_name=u'marcoxavi')
nt=len(TituloBachiller.query.all())
for c in user.carreras:    
    if len(c.titulos_bachiller) == nt:
        print "............."
        print "%s ======> %s T" %(c.nombre.upper(), len(c.titulos_bachiller))
        print "id %s " %c.id
        print u"Cualquier Titulo"
    else:
        if len(c.titulos_bachiller) != 0:
            print "............."
            print "%s ======> %s T" %(c.nombre.upper(), len(c.titulos_bachiller))
            print "id %s " %c.id
            for t in c.titulos_bachiller:
                print t.nombres


### les establece afinidad con todos los titulos a la lista de carreras dada
cualquier=[32, 33, 34, 35, 37, 38, 39, 40, 77, 78, 79, 80, 95]
for id in cualquier:
    carrera=CarreraPrograma.get(id)
    print carrera.nombre
    carrera.titulos_bachiller=[]
    carrera.titulos_bachiller=TituloBachiller.query.all()    
    print "##########################"
    session.flush()

### Muestra las carreras por las que puede optar un titulo de bachiller
for t in TituloBachiller.query.all():
    print ".................."
    print t.nombres.upper()
    listacarr=[c.nombre for c in t.carreras_programas]
    for nom in listacarr:
        print nom + u', '
    print ".................."


tot = 0
for caracteristica in carrera.caracteristicas_bp:
    if caracteristica.num_preguntas is not None:
        tot += caracteristica.num_preguntas

 
#Imprime la carrera juntamente con los numeros de preguntas por cada bancos de preguntas
lista=[35,34,37,45,36,38,42,44,43,33,40,32,95,39,2,8,1,7,5,6,3,98,19,21,20,22,23,77,79,78,80,72,71,96,73,74]
for id in lista:
    c=CarreraPrograma.get(id)
    print c.nombre
    print [(car.banco_preguntas.nombre, str(car.num_preguntas)[:-3]) for car in c.caracteristicas_bp]
    print ".................."

####notas mal####
notas_mal=NotaBachillerato.query.filter(and_(
    NotaBachillerato.nota_maxima != 20,
    NotaBachillerato.nota_maxima != 10,
    NotaBachillerato.nota_maxima != 30,
    NotaBachillerato.nota != 0)).all()
i=1
con_examen = 0
con_examen_cero = 0
sin_examen = 0
for nm in notas_mal:
    if nm.expediente:
        if nm.expediente.examen_admision:
            if nm.expediente.examen_admision.calificacion > 0:
                con_examen += 1
            else:
                con_examen_cero += 1
        else:
            sin_examen +=1
        p=0
        for m in nm.expediente.estudiante.matriculas:
            if m.modulo.id == 597 and m.paralelo is not None:
                p+=1
        if p>0:
            mat=u''
            for m in nm.expediente.estudiante.matriculas:
                if m.modulo.numero == u'1' or m.modulo.numero == u'0':
                    mat+=u'-'
                    mat+=m.modulo.carrera_programa.nombre
            print u"%s| '%s| %s %s| %s/%s| %s | '%s | '%s" %(i, nm.expediente.estudiante.cedula, nm.expediente.estudiante.nombres.upper(), nm.expediente.estudiante.apellidos.upper(), nm.nota, nm.nota_maxima, mat,nm.expediente.estudiante.datos_personales.telefono, nm.expediente.estudiante.datos_personales.celular)
            i+=1
    else:
        print "errorrrrrrrr"
        x=nm
        print nm





admisiones=Matricula.query.join(['expediente','examen_admision','carrera_programa'],'modulo','paralelo').filter(CarreraPrograma.id==carrera.id).filter(Modulo.id == mod.id).filter(Paralelo.oferta_academica == oa).distinct().all()


    def matriculaadmision(ex = None):
        """
            devuelve la matricula de admisiones de un estudiante en base a su examen
            @autor: marcoxavi
        """
        modadmision = Modulo.get(597)
        mat = None
        if ex is not None:
            for m in ex.expediente.estudiante.matriculas:
                if m.modulo == modadmision and m.paralelo is not None:
                    mat = m               
        return mat
    

************************** OJO *******************************
*<Estudiante "Jose Pablo Muñoz Loja" (1104114952)>           *
*<Estudiante "nohely gabriela gonzalez lojan" (1104999386)>  *
************************** OJO *******************************


for exm in totalexamenes:
    try:
        tupla=[exm[0],exm[1],exm[2],exm[3],exm[4],exm[5],exm[6],exm[6].paralelo.plan_estudio.calcular(exm[6])]
    except:
        tupla=[exm[0],exm[1],exm[2],exm[3],exm[4],exm[5],exm[6],u'Error']
    examenes.append(tupla)
    
    
    
# Scriptpara subir la matricula a la que va el estudiante de admisiones en el expediente del estudiante
modulo = Modulo.get(597) #Obtener Modulo de Admisiones
est_pre = EstadoMatricula.get_by(estado=u"EstadoMatriculaPreMatricula")
est_aprob = EstadoMatricula.get_by(estado=u"EstadoMatriculaAprobada")
est_borrada= EstadoMatricula.get_by(estado=u"EstadoMatriculaBorrada")
ms = Matricula.query.join(['expediente','examen_admision']).filter(ExamenAdmision.calificacion > 0).filter(Matricula.modulo==modulo).join(['expediente','examen_admision']).distinct().all()
for m in ms:
    e=m.estudiante
    mat =  Matricula.query.join("modulo").join("estudiante").filter(Modulo.numero==u'1').filter(Modulo.carrera_programa == e.expediente.examen_admision.carrera_programa).filter(and_(Matricula.estado==est_pre,Matricula.estudiante==e)).all()
    if len(mat) == 1:
        if m.estado == est_aprob:
            if mat[0] not in e.expediente.matriculas:
                e.expediente.matriculas.append(mat[0])
                session.flush()
        else:
            if mat[0] in e.expediente.matriculas:
                e.expediente.matriculas.remove(mat[0])
                session.flush()
            mat[0].estado = est_borrada
            session.flush()
    else:
        print "Mat ID: %s; tiene %s matriculas..." %(m.id, len(mat))


# OJO... REVISAR ESTO EN SGA 4
Mat ID: 53942; tiene 0 matriculas...
Mat ID: 54279; tiene 0 matriculas...
Mat ID: 57258; tiene 0 matriculas...
Mat ID: 62464; tiene 0 matriculas...
Mat ID: 63912; tiene 0 matriculas...
Mat ID: 64386; tiene 2 matriculas...
Mat ID: 64695; tiene 0 matriculas...
Mat ID: 67378; tiene 0 matriculas...
Mat ID: 67479; tiene 0 matriculas...


def SemanaSanta(anyo):
    # Constantes mágicas
    M = 24
    N = 5

    #Cálculo de residuos
    a = anyo % 19
    b = anyo % 4
    c = anyo % 7
    d = (19*a + M) % 30
    e = (2*b+4*c+6*d + N) % 7

    # Decidir entre los 2 casos:
    if d+e < 10 :
        dia = d+e+22
        mes = "marzo"
    else:
        dia = d+e-9
    mes = "abril"
    # Excepciones especiales (según artículo)
    if dia == 26 and mes == "abril":
        dia = 19
    if dia == 25 and mes == "abril" and d==28 and e == 6 and a >10:
    dia = 18
    return [dia, mes, anyo]


# Agregar respuestas aleatoriamente 
e=Estudiante.get_by(cedula=u'1104974439')
l=[]
import random
while len(l) <= 64:
    r = random.choice(Respuesta.query.filter(Respuesta.correcta == True).all())
    if r not in l:
        l.append(r)
        print r


#################################################
#   MATRICULADOS EN UNA OFERTA ACADEMICA POR CARRERA
oa = OfertaAcademica.get(28)
est_mat = EstadoMatricula.get_by(estado = u"EstadoMatriculaMatriculada")
est_apr = EstadoMatricula.get_by(estado = u"EstadoMatriculaAprobada")
est_rep = EstadoMatricula.get_by(estado = u"EstadoMatriculaReprobada")
carreras = oa.get_carreras_programas()
for carrera in carreras:
    print carrera.nombre.upper() + u'-'+ carrera.modalidad.upper() + u"|" + str(Matricula.query.join('modulo').filter(Modulo.carrera_programa == carrera).filter(Matricula.oferta_academica == oa).filter(Matricula.estado==est_mat).distinct().count())
    
##################################################
# Número de Matriculas por Oferta Académica
for oa in OfertaAcademica.query.all():
    m=Matricula.query.filter(Matricula.oferta_academica == oa).distinct().count()
    print u'%s ====== %s' %(m,oa.descripcion)
    print "##############"
    

estados=[]
estados.append(EstadoMatricula.get_by(estado=u'EstadoMatriculaReprobada'))
estados.append(EstadoMatricula.get_by(estado=u'EstadoMatriculaAprobada'))
estados.append(EstadoMatricula.get_by(estado=u'EstadoMatriculaMatriculada'))
matriculas=Matricula.query.options(eagerload('papeleta')).join(['modulo','carrera_programa','nivel']).join('expediente').options(eagerload('estudiante')).join('papeleta').filter(and_(Nivel.area==area,or_(Papeleta.estado==u'pagada',Papeleta.estado==u'ajustada'), Matricula.estado in estados, Matricula.oferta_academica == oa)).distinct().all()

#####################
print u"CARRERA PROGRAMA|MATRICULADOS"
for carrera in carreras:
    l=len([m for m in Matricula.query.options(eagerload('papeleta')).join(['modulo','carrera_programa','nivel']).join('expediente').options(eagerload('estudiante')).join('papeleta').filter(and_(Modulo.carrera_programa==carrera, or_(Papeleta.estado==u'pagada',Papeleta.estado==u'ajustada'), Matricula.estado == est_mat, Matricula.oferta_academica == oa)).distinct().all() if m.paralelo is not None])
    print u'%s|%s|%s' %(carrera.nombre,carrera.modalidad,l)
    

#############################
#toda la info por carrera de sept 2009 feb 2010
for carrera in carreras:
    print carrera.nombre                      
    listatotal= [(unicode('UNIVERSIDAD NACIONAL DE LOJA'), unicode(m.estudiante.apellidos), unicode(m.estudiante.nombres), u"'%s" %unicode(m.estudiante.cedula), unicode(m.estudiante.datos_personales.fecha_nacimiento), unicode(m.estudiante.datos_personales.nacionalidad), unicode(m.estudiante.datos_personales.pais_procedencia), unicode(m.id), unicode(m.modulo.carrera_programa.nivel.area.nombre), unicode(m.modulo.carrera_programa.nombre), unicode(m.estudiante.datos_personales.provincia_actual), unicode(m.modulo.carrera_programa.modalidad.upper()), unicode(m.modulo.numero),unicode(m.paralelo.nombre.upper()), unicode(m.estudiante.datos_personales.genero.upper())) for m in Matricula.query.options(eagerload('papeleta')).join(['modulo','carrera_programa','nivel']).join('expediente').options(eagerload('estudiante')).join('papeleta').filter(and_(Modulo.carrera_programa==carrera,or_(Papeleta.estado==u'pagada',Papeleta.estado==u'ajustada'), Matricula.estado == est_mat, Matricula.oferta_academica == oa)).distinct().all() if m.paralelo is not None]
    file = open("/home/marcoxavi/Escritorio/Reportes/matriculadosporoferta/Septiembre-2009-Febrero-2010/todos/%s-%s.xls" %(carrera.nivel.area.siglas, carrera.nombre),"w")
    file.write(u"INSTITUCION|APELLIDOS|NOMBRES|CEDULA|FECHA DE NACIMIENTO|NACIONALIDAD|PAIS DE PROCEDENCIA|MATRICULA|AREA|CARRERA PROGRAMA|PROVINCIA PROCEDENCIA|MODALIDAD|MODULO|PARALELO|SEXO")
    file.write("\n")
    listatotal.sort()
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")    

    file.close()

##################
#toda la info por carrera de sept 2009 feb 2010 MED PROFESIONALES
listatotal= [(unicode('UNIVERSIDAD NACIONAL DE LOJA'), unicode(m.estudiante.apellidos), unicode(m.estudiante.nombres), u"'%s" %unicode(m.estudiante.cedula), unicode(m.estudiante.datos_personales.fecha_nacimiento), unicode(m.estudiante.datos_personales.nacionalidad), unicode(m.estudiante.datos_personales.pais_procedencia), unicode(m.id), unicode(m.modulo.carrera_programa.nivel.area.nombre), unicode(m.modulo.carrera_programa.nombre), unicode(m.estudiante.datos_personales.provincia_actual), unicode(m.modulo.carrera_programa.modalidad), unicode(m.modulo.numero)) for m in Matricula.query.options(eagerload('papeleta')).join(['modulo','carrera_programa','nivel','area']).join('estudiante').join('expediente').options(eagerload('estudiante')).join('papeleta').filter(and_(Area.siglas==u'MED',Estudiante.procedencia==u"profesionales",or_(Papeleta.estado==u'pagada',Papeleta.estado==u'ajustada'), Matricula.estado == est_mat, Matricula.oferta_academica == oa)).distinct().all() if m.paralelo is not None]
file = open("/home/marcoxavi/Escritorio/Reportes/matriculadosporoferta/MED-sept2009--feb2010" ,"w")
file.write(u"INSTITUCION|APELLIDOS|NOMBRES|CEDULA|FECHA DE NACIMIENTO|NACIONALIDAD|PAIS DE PROCEDENCIA|MATRICULA|AREA|CARRERA PROGRAMA|PROVINCIA PROCEDENCIA|MODALIDAD|MODULO")
file.write("\n")
listatotal.sort()
for data in listatotal:
    for v in data:
        if v is not None:
                if len(v)==0:
                        file.write("vacio")
                else:
                        file.write(v.encode('utf-8'))
        else:
                file.write("vacio")
        file.write("|")
    file.write("\n")    

file.close()

#toda la info por carrera de sept 2009 feb 2010 MODALIDAD PRESENCIAL PROFESIONALES
listatotal= [(unicode('UNIVERSIDAD NACIONAL DE LOJA'), unicode(m.estudiante.apellidos), unicode(m.estudiante.nombres), u"'%s" %unicode(m.estudiante.cedula), unicode(m.estudiante.datos_personales.fecha_nacimiento), unicode(m.estudiante.datos_personales.nacionalidad), unicode(m.estudiante.datos_personales.pais_procedencia), unicode(m.id), unicode(m.modulo.carrera_programa.nivel.area.nombre), unicode(m.modulo.carrera_programa.nombre), unicode(m.estudiante.datos_personales.provincia_actual), unicode(m.modulo.carrera_programa.modalidad), unicode(m.modulo.numero), u'si') for m in Matricula.query.options(eagerload('papeleta')).join(['modulo','carrera_programa','nivel','area']).join('estudiante').join('expediente').options(eagerload('estudiante')).join('papeleta').filter(and_(Area.siglas!=u'ACE',Area.siglas!=u'MED',Estudiante.procedencia==u"profesionales",or_(Papeleta.estado==u'pagada',Papeleta.estado==u'ajustada'), Matricula.estado == est_mat, Matricula.oferta_academica == oa)).distinct().all() if m.paralelo is not None]
file = open("/home/marcoxavi/Escritorio/Reportes/matriculadosporoferta/PRESENCIAL-sept2009--feb2010" ,"w")
file.write(u"INSTITUCION|APELLIDOS|NOMBRES|CEDULA|FECHA DE NACIMIENTO|NACIONALIDAD|PAIS DE PROCEDENCIA|MATRICULA|AREA|CARRERA PROGRAMA|PROVINCIA PROCEDENCIA|MODALIDAD|MODULO|PROFESIONAL")
file.write("\n")
listatotal.sort()
for data in listatotal:
    for v in data:
        if v is not None:
                if len(v)==0:
                        file.write("vacio")
                else:
                        file.write(v.encode('utf-8'))
        else:
                file.write("vacio")
        file.write("|")
    file.write("\n")    

file.close()

def es_repetidor(m):f
    r = 0
    est_rep = EstadoMatricula.get_by(estado = u"EstadoMatriculaReprobada")
    for mat in m.estudiante.matriculas:
        if mat.modulo.numero==m.modulo.numero and mat != m and mat.estado==est_rep:
            r=r+1
            print m
    return r

def cursos_especiales(m):
    r = 0
    est_mat = EstadoMatricula.get_by(estado = u"EstadoMatriculaMatriculada")
    oferta=OfertaAcademica.get(28)
    for mat in m.estudiante.matriculas:
        if mat != m and mat.estado==est_mat and mat.modulo.carrera_programa.nivel.area.siglas==u'ACE' and mat.oferta_academica == oferta:
            r=r+1            
    return r

ref ={0:['Admisiones','ADMISIONES'],1:['I','PRIMER'],2:['II','PRIMER'],3:['III','SEGUNDO'],4:['IV','SEGUNDO'],5:['V','TERCER'],6:['VI','TERCER'],7:['VII','CUARTO'],8:['VIII','CUARTO'],9:['IX','QUINTO'],10:['X','QUINTO'],11:['XI','SEXTO'],12:['XII','SEXTO']}
#para refernciar el genero y poder hacer una escritura sin parentesis
ref_genero={u'masculino':['o','el','señor'],u'femenino':['a','la','señorita']}
ref_nacionalidad={u'argentina':'argentina',u'bolivia':'boliviana',u'brasil':'brasileño',u'chile':'chileno',u'colombia':'colombiana',u'ecuador':'ecuatoriana',u'paraguay':'paraguaya',u'peru':'peruana',u'uruguay':'uruguaya',u'venezuela':'venezolana',u'mexico':' mexicana',u'salvador':'salvadoreña',u'cuba':'cubana',u'panama':'panameña',u'portugal':'portugues', u'puerto rico':'puertoricense',u'costa rica':'costaricense',u'alemania':'aleman',u'australia':'australiana',u'canada':'canadiense',u'china':'china',u'corea':'coreana',u'españa':'española',u'estados unidos':'americana',u'francia':'francesa',u'grecia':'griega ',u'india':'indu',u'inglaterra':'inglesa',u'israel':'israelí',u'italia':'italiana',u'suiza':'suiza ',u'holanda':'holandesa',u'polonia':'polaca',u'filipinas':'filipina',u'noruega':'noruega',u'suecia':'sueca'}
ref_area = {u'MED':'DE LA'}

texto = u"Que %s %s bachiller: <b>%s</b> de nacionalidad %s, con cédula Nro. <b>%s</b>, se encuentra matriculad%s en el <b>%s Módulo</b> denominado: '<b>%s</b>', <b>Modalidad %s</b>, que corresponde al <b>%s AÑO</b> de la carrera de: <b>%s</b>, con el <b>Nro. %s</b>, Folio <b>Nro. %s</b> del libro de matriculas, periodo académico <b>%s</b> %s" % (ref_genero[m.estudiante.datos_personales.genero][1],ref_genero[m.estudiante.datos_personales.genero][2],nombre_est.upper(),nacionalidad,str(m.estudiante.cedula),ref_genero[m.estudiante.datos_personales.genero][0],ref[int(m.modulo.numero)][0],nombre_modulo,str(m.modulo.carrera_programa.modalidad.title()),ref[int(m.modulo.numero)][1],m.modulo.carrera_programa.nombre.upper().encode('utf-8'),str(m.id),str(m.folio),m.oferta_academica.descripcion.encode('utf-8'), txtasis.encode('utf-8'))


print ref_genero[m.estudiante.datos_personales.genero][1]
print ref_genero[m.estudiante.datos_personales.genero][2]
print nombre_est.upper()
print nacionalidad
print str(m.estudiante.cedula)
print ref_genero[m.estudiante.datos_personales.genero][0]
print ref[int(m.modulo.numero)][0]
print nombre_modulo
print str(m.modulo.carrera_programa.modalidad.title())
print ref[int(m.modulo.numero)][1]
print m.modulo.carrera_programa.nombre.upper().encode('utf-8')
print str(m.id)
print str(m.folio)
print m.oferta_academica.descripcion.encode('utf-8')
print txtasis.encode('utf-8'))


# EMAIL de Estudiantes
listatotal = [u"%s|%s|%s" %(e.apellidos,e.nombres,e.datos_personales.email) for e in Estudiante.query.all() if e.datos_personales is not None and e.datos_personales.email is not None]
for data in listatotal:
    file = open("/home/marcoxavi/Escritorio/estudiantesemail1","w")
    file.write("APELLIDOS|NOMBRES|E-MAIL")
    file.write("\n")
    listatotal.sort()
    for v in data:
        if v is not None:
                if len(v)==0:
                        file.write("vacio")
                else:
                        file.write(v.encode('utf-8'))
        else:
                file.write("vacio")
        file.write("|")
    file.write("\n")    

    file.close()

########################################################
#Lista de Estudiantes Matriculados por SEXO
est_mat = EstadoMatricula.get_by(estado = u"EstadoMatriculaMatriculada")
oa=OfertaAcademica.get(28)
carreras_MED=[c for c in oa.get_carreras_programas() if c.modalidad == u'distancia']

print u'Carrera: %s' % c.nombre
for c in carreras_MED:
    listatotal = []
    for mod in c.modulos:
        lm = Matricula.query().filter(and_(Matricula.oferta_academica==oa,Matricula.estado==est_mat,Matricula.modulo==mod)).join('modulo').filter(Modulo.carrera_programa==c).join(['estudiante','datos_personales']).filter(or_(DatosPersonales.genero==u'masculino',DatosPersonales.genero==u'MASCULINO')).count()
        lf = Matricula.query().filter(and_(Matricula.oferta_academica==oa,Matricula.estado==est_mat,Matricula.modulo==mod)).join('modulo').filter(Modulo.carrera_programa==c).join(['estudiante','datos_personales']).filter(or_(DatosPersonales.genero==u'femenino',DatosPersonales.genero==u'FEMENINO')).count()
        lt = lm + lf
        ap = (unicode(c.nombre),unicode(mod.numero),unicode(lt),unicode(lm),unicode(lf))
        listatotal.append(ap)
    
    file = open("/home/marcoxavi/Escritorio/Reportes/matriculadosporoferta/MED/Sept2009Feb2010/XSEXO%s" %c.nombre,"w")
    file.write("CARRERA|MODULO|ESTUDIANTES|HOMBRES|MUJERES")
    file.write("\n")    
    
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")    
    
    file.close()

###########
#por paises carreras y sexo
listadopaises=['Argentina', 'Brazil', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Cuba', 'Czech Republic',
    'Djibouti', 'Dominica', 'Ecuador', 'Egypt', 'Finland', 'France', 'Gambia', 'Germany', 'Ghana',
    'India', 'Mexico', 'Nigeria', 'Peru', 'Russia', 'Spain', 'United States', 'Uruguay']

for p in listadopaises:
    if DatosPersonales.query.filter(DatosPersonales.pais_procedencia==p).count() != 0:
        print "%s :%s" %(p,unicode(DatosPersonales.query.filter(DatosPersonales.pais_procedencia==p).count()))
        l.append(p)

est_mat = EstadoMatricula.get_by(estado = u"EstadoMatriculaMatriculada")
est_rep = EstadoMatricula.get_by(estado = u"EstadoMatriculaReprobada")
est_apr = EstadoMatricula.get_by(estado = u"EstadoMatriculaAprobada")
estados=[est_mat, est_rep, est_apr]
oa=OfertaAcademica.get(28)
carreras = oa.get_carreras_programas()
listatotal = []
for c in carreras:
    ap = [u'%s - %s'%(unicode(c.nombre),unicode(c.modalidad.upper()))]
    for p in listadopaises:
        lm = Matricula.query().filter(and_(Matricula.oferta_academica==oa,Matricula.estado in estados)).join('modulo').filter(Modulo.carrera_programa==c).join(['estudiante','datos_personales']).filter(and_(DatosPersonales.pais_procedencia == p,or_(DatosPersonales.genero==u'masculino',DatosPersonales.genero==u'MASCULINO'))).count()
        ap.append(unicode(lm))
        lf = Matricula.query().filter(and_(Matricula.oferta_academica==oa,Matricula.estado in estados)).join('modulo').filter(Modulo.carrera_programa==c).join(['estudiante','datos_personales']).filter(and_(DatosPersonales.pais_procedencia == p,or_(DatosPersonales.genero==u'femenino',DatosPersonales.genero==u'FEMENINO'))).count()
        ap.append(unicode(lf))
        lt = lm + lf
        ap.append(unicode(lt))    
    listatotal.append(ap)    
    file = open("/home/marcoxavi/Escritorio/Reportes/matriculadosporoferta/Septiembre-2009-Febrero-2010/Vice/xPais" ,"w")
    file.write(".|Argentina| | |Brazil| | |Chad| | |Chile| | |China| | |Colombia| | |Comoros| | |Cuba| | |Czech Republic| | |Djibouti| | |Dominica| | |Ecuador| | |Egypt| | |Finland| | |France| | |Gambia| | |Germany| | |Ghana| | |India| | |Mexico| | |Nigeria| | |Peru| | |Russia| | |Spain| | |United States| | |Uruguay")
    file.write("\n")    
    file.write("CARRERA|H|M|T")
    file.write("\n")    
    
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")    
    
    file.close()


#####################################################################
# por carreras con todos sus datos personales
def presencial(c):
    if c.modalidad == u'presencial':
        return unicode(u"X")
    else:
        return unicode(u"---")


def semipresencial(c):
    if c.modalidad == u'semipresencial':
        return unicode(u"X")
    else:
        return unicode(u"---")


def distancia(c):
    if c.modalidad == u'distancia':
        return unicode(u"X")
    else:
        return unicode(u"---")


def fiscal(e): 
    if e.procedencia == u'col_fiscal':
        return unicode(u"X")
    else:
        return unicode(u"---")


def particular(e):
    if e.procedencia == u'col_particular':
        return unicode(u"X")
    else:
        return unicode(u"---")


    

    
est_mat = EstadoMatricula.get_by(estado = u"EstadoMatriculaMatriculada")
est_rep = EstadoMatricula.get_by(estado = u"EstadoMatriculaReprobada")
est_apr = EstadoMatricula.get_by(estado = u"EstadoMatriculaAprobada")
estados=[est_mat, est_rep, est_apr]
oa=OfertaAcademica.get(28)
carreras = oa.get_carreras_programas()

for c in carreras:
    lm = Matricula.query().filter(and_(Matricula.oferta_academica==oa,Matricula.estado in estados)).join('modulo').filter(Modulo.carrera_programa==c).all()
    listatotal = [(u"%s %s" %(m.estudiante.apellidos.upper(),m.estudiante.nombres.upper()), u"'%s" %m.estudiante.cedula, unicode(m.modulo.carrera_programa.nombre.upper()), presencial(m.modulo.carrera_programa),semipresencial(m.modulo.carrera_programa),distancia(m.modulo.carrera_programa),m.estudiante.datos_personales.provincia_procedencia, m.estudiante.datos_personales.canton_procedencia, fiscal(m.estudiante),u"---", particular(m.estudiante), u"---",unicode(m.modulo.numero),unicode(m.paralelo.nombre)) for m in lm if m.paralelo is not None and m.estudiante.datos_personales is not None] #almacena la lista de matriculas
    listatotal.sort()
    file = open("/home/marcoxavi/Escritorio/Reportes/matriculadosporoferta/Septiembre-2009-Febrero-2010/Vice/xProcedencia%s-%s" %(c.nombre,c.modalidad.upper()) ,"w")
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")    
    
    file.close()



#############################################################
#Formato Conesup
def get_anio(n):
    if n ==1 or n==2:
        anio=u'1 AÑO'
    if n ==3 or n==4:
        anio=u'2 AÑOS'
    if n ==5 or n==6:
        anio=u'3 AÑOS'
    if n ==7 or n==8:
        anio=u'4 AÑOS'
    if n ==9 or n==10:
        anio=u'5 AÑOS'
    if n ==11 or n==12:
        anio=u'6 AÑOS'
    if n ==13 or n==14:
        anio=u'7 AÑOS'
    return anio

def nacionalidad(d):
    ref_nacionalidad={u'argentina':'argentina',u'bolivia':'boliviana',u'brasil':'brasileño',u'chile':'chileno',u'colombia':'colombiana',u'ecuador':'ecuatoriana',u'paraguay':'paraguaya',u'perú':'peruana',u'peru':'peruana',u'uruguay':'uruguaya',u'venezuela':'venezolana',u'mexico':' mexicana',u'salvador':'salvadoreña',u'cuba':'cubana',u'panama':'panameña',u'portugal':'portugues', u'puerto rico':'puertoricense',u'costa rica':'costaricense',u'alemania':'aleman',u'australia':'australiana',u'canada':'canadiense',u'china':'china',u'corea':'coreana',u'españa':'española',u'estados unidos':'americana',u'francia':'francesa',u'grecia':'griega ',u'india':'indu',u'inglaterra':'inglesa',u'israel':'israelí',u'italia':'italiana',u'suiza':'suiza ',u'holanda':'holandesa',u'polonia':'polaca',u'filipinas':'filipina',u'noruega':'noruega',u'suecia':'sueca',u'per\xfa':u'peruana'}
    if d.pais_procedencia is None:
        return u'no establecido'
    else:
        return u'%s' %ref_nacionalidad[d.pais_procedencia.lower()]



est_mat = EstadoMatricula.get_by(estado = u"EstadoMatriculaMatriculada")
est_rep = EstadoMatricula.get_by(estado = u"EstadoMatriculaReprobada")
est_apr = EstadoMatricula.get_by(estado = u"EstadoMatriculaAprobada")
oa=OfertaAcademica.get(34)
carreras = oa.get_carreras_programas()

for c in carreras:
    lm = Matricula.query.filter(and_(Matricula.oferta_academica==oa,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(Modulo.carrera_programa==c).all()
    listatotal = [(u"%s %s" %(m.estudiante.apellidos.upper(),m.estudiante.nombres.upper()),unicode(m.modulo.carrera_programa.nombre.upper()),u"%s" %m.modulo.carrera_programa.modalidad.upper(), u"'%s" %m.estudiante.cedula,m.estudiante.datos_personales.genero.upper(),nacionalidad(m.estudiante.datos_personales),unicode(m.id),unicode(m.estudiante.datos_personales.fecha_nacimiento),unicode(m.estudiante.datos_personales.provincia_procedencia),unicode(m.modulo.carrera_programa.nivel.area.nombre.upper()), unicode(oa.periodo_lectivo.descripcion),unicode(m.modulo.numero),unicode(m.paralelo.nombre)) for m in lm if m.paralelo is not None and m.estudiante.datos_personales is not None] #almacena la lista de matriculas
    listatotal.sort()
    file = open("/home/respaldos/Escritorio/Reportes/matriculadosporoferta/Marzo-Julio-2010/matriculados-%s-%s" %(c.nombre,c.modalidad.upper()) ,"w")
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")    
    
    file.close()

#################################################################################################################################
# PARA SACAR LA INFORMACION DE LOS ESTUDIANTES EXTRANJEROS POR AREA...
lm = Matricula.query.join('estudiante').filter(Estudiante.procedencia=='extranjeros').join(['modulo','carrera_programa']).filter(and_(CarreraPrograma.modalidad==u'distancia',Matricula.oferta_academica==oa)).all()
listatotal = [(u"%s %s" %(m.estudiante.apellidos.upper(),m.estudiante.nombres.upper()),unicode(m.modulo.carrera_programa.nombre.upper()),u"%s" %m.modulo.carrera_programa.modalidad.upper(), u"'%s" %m.estudiante.cedula,m.estudiante.datos_personales.genero.upper(),m.estudiante.datos_personales.pais_procedencia,unicode(m.id),unicode(m.estudiante.datos_personales.fecha_nacimiento),unicode(m.estudiante.datos_personales.provincia_actual),unicode(m.estudiante.datos_personales.canton_actual),unicode(m.estudiante.datos_personales.direccion_actual),unicode(m.modulo.carrera_programa.nivel.area.nombre.upper()), unicode(oa.periodo_lectivo.descripcion),unicode(m.modulo.numero)) for m in lm if m.estudiante.datos_personales is not None] #almacena la lista de matriculas
listatotal.sort()
file = open("/home/respaldos/Escritorio/Reportes/matriculadosporoferta/EXTRANJEROSmed" ,"w")
for data in listatotal:
    for v in data:
        if v is not None:
                if len(v)==0:
                        file.write("vacio")
                else:
                        file.write(v.encode('utf-8'))
        else:
                file.write("vacio")
        file.write("|")
    file.write("\n")    

file.close()


##################### ADMITIDOS POR SEXO Y POR CARRERA##########################

oa = OfertaAcademica.get(30) #CAMBIAR OFERTA SEGUN CORRESPONDA
carreras = oa.get_carreras_programas()
est_rep=EstadoMatricula.get_by(estado=u'EstadoMatriculaReprobada')
est_apr=EstadoMatricula.get_by(estado=u'EstadoMatriculaAprobada')
est_mat=EstadoMatricula.get_by(estado=u'EstadoMatriculaMatriculada')
listatotal = []
listatotal.append((u'CARRERA O PROGRAMA', u'MODALIDAD', u'HOMBRES APROBADOS', u'MUJERES APROBADAS',u'TOTAL APROBADOS',u'HOMBRES REPROBADOS', u'MUJERES REPROBADAS',u'TOTAL REPROBADOS',u'TOTAL',u'MS'))
for carrera in carreras:
     ms = TipoPlanEstudioAdmisiones.get_tabla_acreditacion_carrera(carrera, oa.id)
     eah = len([m for m in ms if m.matricula.estado==est_apr and m.matricula.estudiante.datos_personales.genero=='masculino'])
     eam = len([m for m in ms if m.matricula.estado==est_apr and m.matricula.estudiante.datos_personales.genero=='femenino'])
     erh = len([m for m in ms if m.matricula.estado==est_rep and m.matricula.estudiante.datos_personales.genero=='masculino'])
     erm = len([m for m in ms if m.matricula.estado==est_rep and m.matricula.estudiante.datos_personales.genero=='femenino'])
     if len(ms) > 0:
         listatotal.append((unicode(carrera.nombre.upper()), unicode(carrera.modalidad),  str(eah), str(eam), str(eah+eam), str(erh), str(erm), str(erh + erm),str(eah+eam+erh+erm),str(len(ms))))

file = open("/home/respaldos/Escritorio/Admitidos-%s.csv" %oa.descripcion,"w")

for data in listatotal:
    for v in data:
        if v is not None:
                if len(v)==0:
                        file.write("vacio")
                else:
                        file.write(v.encode('utf-8'))
        else:
                file.write("vacio")
        file.write("|")
    file.write("\n")    

file.close()


###################### reporte por sexo carrera y seccion ######################
oa = OfertaAcademica.get(34) #CAMBIAR OFERTA SEGUN CORRESPONDA
est_rep=EstadoMatricula.get_by(estado=u'EstadoMatriculaReprobada')
est_apr=EstadoMatricula.get_by(estado=u'EstadoMatriculaAprobada')
est_mat=EstadoMatricula.get_by(estado=u'EstadoMatriculaMatriculada')
listatotal = []
listatotal.append((u'CARRERA O PROGRAMA', u'MODALIDAD', u'HOMBRES', u'MUJERES',u'TOTAL',u'MATUTINO',u'VESPERTINO',u'NOCTURNO',u'TOTAL POR SECCION'))
for carrera in oa.get_carreras_programas():
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(Modulo.carrera_programa==carrera).all()
    ho = len([m for m in ms if m.estudiante.datos_personales.genero=='masculino' and m.paralelo is not None and m.estudiante.datos_personales is not None])
    mu = len([m for m in ms if m.estudiante.datos_personales.genero=='femenino' and m.paralelo is not None and m.estudiante.datos_personales is not None])
    man = len([m for m in ms if m.paralelo.seccion=='matutino' and m.paralelo is not None and m.estudiante.datos_personales is not None])
    tar = len([m for m in ms if m.paralelo.seccion=='vespertino' and m.paralelo is not None and m.estudiante.datos_personales is not None])
    noc = len([m for m in ms if m.paralelo.seccion=='nocturno' and m.paralelo is not None and m.estudiante.datos_personales is not None])
    if len(ms) > 0 and carrera != c:
        listatotal.append(((unicode(carrera.nombre.upper()),unicode(carrera.modalidad),str(ho),str(mu),str(ho+mu),str(man),str(tar),str(noc),str(man+tar+noc))))
    else:
        print u'carrera mal %s' %carrera.nombre


file = open("/home/respaldos/Escritorio/Reportes/matriculadosporoferta/MArzo-Julio-2010/matriculadosXsexoYseccion" ,"w")

for data in listatotal:
    for v in data:
        if v is not None:
                if len(v)==0:
                        file.write("vacio")
                else:
                        file.write(v.encode('utf-8'))
        else:
                file.write("vacio")
        file.write("|")
    file.write("\n")

file.close()

###################### reporte datos basicos de estudiantes por carrera ######################
oa = OfertaAcademica.get(34) #CAMBIAR OFERTA SEGUN CORRESPONDA
est_rep=EstadoMatricula.get_by(estado=u'EstadoMatriculaReprobada')
est_apr=EstadoMatricula.get_by(estado=u'EstadoMatriculaAprobada')
est_mat=EstadoMatricula.get_by(estado=u'EstadoMatriculaMatriculada')

for carrera in oa.get_carreras_programas():
    #modulo = Modulo.get()
    listatotal = []
    listatotal.append((u'APELLIDOS Y NOMBRES',u'MODULO',u'PARALELO',u'DIRECCION',u'E-MAIL',u'TELEFONO CONVENCIONAL',u'CELULAR',u'CEDULA',u'CARRERA O PROGRAMA', u'MODALIDAD', u'OFERTA ACADEMICA',u'ESTADO'))
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(Modulo.carrera_programa==carrera).all()
    #ms = Matricula.query.filter(and_(Matricula.modulo == modulo, Matricula.oferta_academica==oa,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).all()
    if len(ms) > 0:
        lista = [(u'%s %s' %(m.estudiante.apellidos.upper(),m.estudiante.nombres.upper()),unicode(m.modulo.numero),unicode(m.paralelo.nombre),unicode(m.estudiante.datos_personales.direccion_actual),unicode(m.estudiante.datos_personales.email),u"'%s" %m.estudiante.datos_personales.telefono,u"'%s" %m.estudiante.datos_personales.celular,u"'%s" %m.estudiante.cedula,unicode(m.modulo.carrera_programa.nombre),unicode(m.modulo.carrera_programa.modalidad),unicode(oa.descripcion),unicode(m.estado.estado[15:])) for m in ms if m.paralelo is not None and m.estudiante.datos_personales is not None]
        lista.sort()
        listatotal.extend(lista)
    #file = open(u"/home/respaldos/Escritorio/%s - %s - %s" %(modulo.carrera_programa.nombre,modulo.carrera_programa.modalidad, oa.descripcion) ,"w")
    #file = open(u"/home/respaldos/Escritorio/estudiantes %s" %oa.descripcion ,"w")
    file = open(u"/home/respaldos/Escritorio/%s - %s - %s" %(carrera.nombre,carrera.modalidad,oa.descripcion) ,"w")
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")
    
    file.close()
#############################################################################
###################### reporte Matriculados por oferta ######################
oa = OfertaAcademica.get(34) #CAMBIAR OFERTA SEGUN CORRESPONDA
est_rep=EstadoMatricula.get_by(estado=u'EstadoMatriculaReprobada')
est_apr=EstadoMatricula.get_by(estado=u'EstadoMatriculaAprobada')
est_mat=EstadoMatricula.get_by(estado=u'EstadoMatriculaMatriculada')
listatotal = []
listatotal.append((u'CARRERA O PROGRAMA', u'MATRICULADOS', u'OFERTA'))
for carrera in oa.get_carreras_programas():
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(Modulo.carrera_programa==carrera).count()    
    if ms > 0 :
        listatotal.append( (u'%s-%s' %(carrera.nombre.upper(),carrera.modalidad), u'%s' %ms, u'%s' %oa.descripcion) )
    else:
        print u'carrera mal %s' %carrera.nombre


file = open("/home/respaldos/Escritorio/info/matriculas-%s.csv" %oa.descripcion ,"w")

for data in listatotal:
    for v in data:
        if v is not None:
                if len(v)==0:
                        file.write("vacio")
                else:
                        file.write(v.encode('utf-8'))
        else:
                file.write("vacio")
        file.write("|")
    file.write("\n")

file.close()

#############################################################################
###################### reporte Matriculados Desercion por oferta ######################
def porcentaje(t,v):
    return(float(100*v)/float(t))

oa = OfertaAcademica.get(34) #CAMBIAR OFERTA SEGUN CORRESPONDA
est_rep=EstadoMatricula.get_by(estado=u'EstadoMatriculaReprobada')
est_apr=EstadoMatricula.get_by(estado=u'EstadoMatriculaAprobada')
est_mat=EstadoMatricula.get_by(estado=u'EstadoMatriculaMatriculada')
listatotal = []
listatotal.append((u'CARRERA O PROGRAMA', u'ALUMNOS MATRICULADOS',u'ALUMNOS APROBADOS', u'% DESERCIóN', u'OFERTA'))
for carrera in oa.get_carreras_programas():
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(Modulo.carrera_programa==carrera).count()    
    ap = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.estado == est_apr)).join('modulo').filter(Modulo.carrera_programa==carrera).count()        
    if ms > 0 :
        listatotal.append( (u'%s-%s' %(carrera.nombre.upper(),carrera.modalidad), u'%s' %ms, u'%s' %ap, u'%s' %porcentaje(ms,ms-ap), u'%s' %oa.descripcion) )
    else:
        print u'carrera mal %s' %carrera.nombre


file = open("/home/respaldos/Escritorio/info/Desercion-oaid-%s-%s.csv" %(oa.id,oa.descripcion) ,"w")

for data in listatotal:
    for v in data:
        if v is not None:
                if len(v)==0:
                        file.write("vacio")
                else:
                        file.write(v.encode('utf-8'))
        else:
                file.write("vacio")
        file.write("|")
    file.write("\n")

file.close()
###############################################################################################
###################### reporte datos basicos de estudiantes por carrera ######################
oa = OfertaAcademica.get(34) #CAMBIAR OFERTA SEGUN CORRESPONDA
est_rep=EstadoMatricula.get_by(estado=u'EstadoMatriculaReprobada')
est_apr=EstadoMatricula.get_by(estado=u'EstadoMatriculaAprobada')
est_mat=EstadoMatricula.get_by(estado=u'EstadoMatriculaMatriculada')
def get_anio(n):
    if n ==1 or n==2:
        anio=u'1'
    if n ==3 or n==4:
        anio=u'2'
    if n ==5 or n==6:
        anio=u'3'
    if n ==7 or n==8:
        anio=u'4'
    if n ==9 or n==10:
        anio=u'5'
    if n ==11 or n==12:
        anio=u'6'
    if n ==13 or n==14:
        anio=u'7'
    return anio

def nacionalidad(d):
    ref_nacionalidad={u'argentina':'argentina',u'bolivia':'boliviana',u'brasil':'brasileño',u'chile':'chileno',u'colombia':'colombiana',u'ecuador':'ecuatoriana',u'paraguay':'paraguaya',u'perú':'peruana',u'peru':'peruana',u'uruguay':'uruguaya',u'venezuela':'venezolana',u'mexico':' mexicana',u'salvador':'salvadoreña',u'cuba':'cubana',u'panama':'panameña',u'portugal':'portugues', u'puerto rico':'puertoricense',u'costa rica':'costaricense',u'alemania':'aleman',u'australia':'australiana',u'canada':'canadiense',u'china':'china',u'corea':'coreana',u'españa':'española',u'estados unidos':'americana',u'francia':'francesa',u'grecia':'griega ',u'india':'indu',u'inglaterra':'inglesa',u'israel':'israelí',u'italia':'italiana',u'suiza':'suiza ',u'holanda':'holandesa',u'polonia':'polaca',u'filipinas':'filipina',u'noruega':'noruega',u'suecia':'sueca',u'per\xfa':u'peruana'}
    if d.pais_procedencia is None:
        return u'no establecido'
    else:
        return u'%s' %ref_nacionalidad[d.pais_procedencia.lower()]



for carrera in carreras:
    listatotal = []
    listatotal.append((u'APELLIDOS Y NOMBRES',u'CARRERA',u'MODALIDAD',u'CEDULA',u'E-MAIL',u'GÉNERO',u'NACIONALIDAD',u'NUM MATRICULA',u'AREA_ESTUDIO',u'PERIODO_LECTIVO',u'MODULO',u'PARALELO'))    
    #modulo = Modulo.get()
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(Modulo.carrera_programa==carrera).all()
    #ms = Matricula.query.filter(and_(Matricula.modulo == modulo, Matricula.oferta_academica==oa,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).all()    
    area = carrera.nivel.area.nombre
    modalidad=carrera.modalidad
    cnombre=carrera.nombre
    if len(ms) > 0:
        lista = [(u'%s %s' %(m.estudiante.apellidos.upper(),m.estudiante.nombres.upper()),unicode(cnombre),unicode(modalidad),u"'%s" %m.estudiante.cedula,u'%s' %m.estudiante.datos_personales.email,u'%s' %m.estudiante.datos_personales.genero,nacionalidad(m.estudiante.datos_personales),unicode(m.id),unicode(area),unicode(oa.descripcion),unicode(m.modulo.numero),unicode(m.paralelo.nombre)) for m in ms if m.paralelo is not None and m.estudiante.datos_personales is not None]
        lista.sort()
        listatotal.extend(lista)
    file = open(u"/home/marcoxavi/Escritorio/OfertaSept2010Febrero2011/Carrera - %s - %s" %(cnombre,oa.descripcion) ,"w")
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")
    
    file.close()

################################################## REPORTE PARA DR SOLO 1ER MODULO ##############################################################################

listatotal = []
#CARRERA MODALIDAD OFERTA MODULO H M TOTAL_MS TOTAL_H+S

listatotal.append((u'CARRERA',u'MODALIDAD',u'OFERTA',u'MODULO',u'HOMBRES',u'MUJERES',u'TOTAL',u'H+S'))
for carrera in oa.get_carreras_programas():
    #modulo = Modulo.get()
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(and_(Modulo.carrera_programa==carrera,Modulo.numero==u'1')).all() 
    msm = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(and_(Modulo.carrera_programa==carrera,Modulo.numero==u'1')).join(['estudiante','datos_personales']).filter(DatosPersonales.genero==u'masculino').all()
    msf = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(and_(Modulo.carrera_programa==carrera,Modulo.numero==u'1')).join(['estudiante','datos_personales']).filter(DatosPersonales.genero==u'femenino').all()
    modalidad = carrera.modalidad
    if len(ms) > 0:
        listatotal.append( (u'%s' %carrera.nombre,u'%s' %modalidad,u'%s' %oa.descripcion,u'1',u'%s' %str(len(msm)),u'%s' %str(len(msf)),u'%s' %str(len(ms)),str(len(msm+msf))) )

file = open(u"/home/respaldos/Escritorio/Informacion de estudiantes 1 modulo %s.csv" %oa.descripcion ,"w")
for data in listatotal:
    for v in data:
        if v is not None:
                if len(v)==0:
                        file.write("vacio")
                else:
                        file.write(v.encode('utf-8'))
        else:
                file.write("vacio")
        file.write("|")
    file.write("\n")

file.close()


################################################## REPORTE POR CARRERA Y SEXO ##############################################################################

listatotal = []
#CARRERA MODALIDAD OFERTA H M TOTAL_MS TOTAL_H+S
carreras = [c for c in CarreraPrograma.query.join('nivel').filter(Nivel.area != ace).all() if c in oa.get_carreras_programas()]
listatotal.append((u'CARRERA',u'MODALIDAD',u'OFERTA',u'HOMBRES',u'MUJERES',u'TOTAL',u'H+S'))
for carrera in carreras:
    #modulo = Modulo.get()
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(and_(Modulo.carrera_programa==carrera)).all() 
    msm = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(and_(Modulo.carrera_programa==carrera)).join(['estudiante','datos_personales']).filter(DatosPersonales.genero==u'masculino').all()
    msf = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(and_(Modulo.carrera_programa==carrera)).join(['estudiante','datos_personales']).filter(DatosPersonales.genero==u'femenino').all()
    modalidad = carrera.modalidad
    if len(ms) > 0:
        listatotal.append( (u'%s' %carrera.nombre,u'%s' %modalidad,u'%s' %oa.descripcion,u'%s' %str(len(msm)),u'%s' %str(len(msf)),u'%s' %str(len(ms)),str(len(msm+msf))) )

file = open(u"/home/respaldos/Escritorio/Informacion de estudiantes %s.csv" %oa.descripcion ,"w")
for data in listatotal:
    for v in data:
        if v is not None:
                if len(v)==0:
                        file.write("vacio")
                else:
                        file.write(v.encode('utf-8'))
        else:
                file.write("vacio")
        file.write("|")
    file.write("\n")

file.close()


#################################################### REPORTE DE LOS MEJORES ESTUDIANTES PARA BECAS ##############################################

oa = OfertaAcademica.get(34) #CAMBIAR OFERTA SEGUN CORRESPONDA
est_rep=EstadoMatricula.get_by(estado=u'EstadoMatriculaReprobada')
est_apr=EstadoMatricula.get_by(estado=u'EstadoMatriculaAprobada')
est_mat=EstadoMatricula.get_by(estado=u'EstadoMatriculaMatriculada')
carreras = oa.get_carreras_programas()
for carrera in carreras:
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(Modulo.carrera_programa==carrera).all()
    lista = []
    lista.append((u'CALIFICACION',u'CEDULA',u'APELLIDOS Y NOMBRES',u'CARRERA',u'TELEFONO',u'CELULAR',u'ESTADO DE MATRICULA'))
    for m in ms:
        try:
            prom = m.paralelo.plan_estudio.calcular(m)['total']
        except:
            prom = None
        if prom.__class__.__name__ == 'Decimal':
            m.promedio_acreditacion = prom
        session.flush()
        if m.estado == est_apr:
            lista.append((m.promedio_acreditacion,u"%s" %m.estudiante.cedula, u"%s %s" %(m.estudiante.apellidos.upper(),m.estudiante.nombres.upper()),u"%s-%s" %(m.modulo.carrera_programa.nombre,m.modulo.carrera_programa.modalidad), u"%s" %m.estudiante.datos_personales.telefono,u"%s" %m.estudiante.datos_personales.celular, u"%s" %m.estado.estado[15:]))
    lista.sort()
    listatotal=[(u"%s" %e[0],e[1],e[2],e[3],e[4],e[5],e[6]) for e in lista]
    file = open(u"/home/respaldos/Escritorio/Becas/Becas %s-%s %s.csv" %(carrera.nombre,carrera.modalidad,oa.descripcion) ,"w")
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")

    file.close()

###################################### ADMISIONES 2010 ##################################################
#patovala:10:33:23] Daniel dice:
#nro de estudaintes por áreas de los admitidos por sexo
#[10:33:29] Daniel dice:
#y por edad
#[10:33:57] Daniel dice:
#colegio de prosedencia
#[10:34:25] Daniel dice:
#y por cantones
#patovala:y el tipo de colegio
#[10:35:24] Daniel dice:
#publico o privado
areas=[]
areas.append(Area.query.all()[0])
areas.append(Area.query.all()[2])
areas.append(Area.query.all()[3])
areas.append(Area.query.all()[6])
areas.append(Area.query.all()[8])




#
l='5, 19, 72, 42, 22, 23, 32, 34, 25, 79, 78, 80, 91, 74, 77, 73, 71, 6, 3, 8, 7, 21, 35, 36, 38, 33, 37, 40, 43, 44, 2, 45, 39, 95, 1, 96, 98, 2'

import datetime
def getEdad(fecha_nacimiento):
    delta = datetime.date.today() - fecha_nacimiento
    return datetime.date.fromordinal(delta.days).year

#saca matriculas de admisiones 
#por carrera
ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,Matricula.tipo==None,Matricula.estado == est_mat, Matricula.paralelo != None)).join('papeleta').filter(Papeleta.costo_total == 0).join('modulo').filter(and_(Modulo.numero==u'1',Modulo.carrera_programa==carrera)).all()

for area in areas:
    #por area
    msa = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,Matricula.tipo==None,Matricula.estado == est_mat, Matricula.paralelo != None)).join('papeleta').filter(Papeleta.costo_total == 0).join('modulo').filter(Modulo.numero==u'1').join(['modulo','carrera_programa','nivel']).filter(Nivel.area==area).distinct().count()
    #por area y sexo
    #Hombres
    msh = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,Matricula.tipo==None,Matricula.estado == est_mat, Matricula.paralelo != None)).join('papeleta').filter(Papeleta.costo_total == 0).join('modulo').filter(Modulo.numero==u'1').join(['modulo','carrera_programa','nivel']).filter(Nivel.area==area).distinct().join(['estudiante','datos_personales']).filter(DatosPersonales.genero==u'masculino').count()
    #Mujeres
    msm = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,Matricula.tipo==None,Matricula.estado == est_mat, Matricula.paralelo != None)).join('papeleta').filter(Papeleta.costo_total == 0).join('modulo').filter(Modulo.numero==u'1').join(['modulo','carrera_programa','nivel']).filter(Nivel.area==area).distinct().join(['estudiante','datos_personales']).filter(DatosPersonales.genero==u'femenino').count()
    print u'%s|%s|%s|%s|%s|' %(area.nombre,area.siglas,msa,msh,msm)

for area in areas:
    #saca matriculas de admisiones 
    #por area y tipo de colegio
    msa = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,Matricula.tipo==None,Matricula.estado == est_mat, Matricula.paralelo != None)).join('papeleta').filter(Papeleta.costo_total == 0).join('modulo').filter(Modulo.numero==u'1').join(['modulo','carrera_programa','nivel']).filter(Nivel.area==area).distinct().count()
    #col_fiscal
    mscf = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,Matricula.tipo==None,Matricula.estado == est_mat, Matricula.paralelo != None)).join('papeleta').filter(Papeleta.costo_total == 0).join('modulo').filter(Modulo.numero==u'1').join(['modulo','carrera_programa','nivel']).filter(Nivel.area==area).join('estudiante').filter(Estudiante.procedencia==u'col_fiscal').distinct().count()
    #col_fiscomisional
    mscfm = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,Matricula.tipo==None,Matricula.estado == est_mat, Matricula.paralelo != None)).join('papeleta').filter(Papeleta.costo_total == 0).join('modulo').filter(Modulo.numero==u'1').join(['modulo','carrera_programa','nivel']).filter(Nivel.area==area).join('estudiante').filter(Estudiante.procedencia==u'col_fiscomisional').distinct().count()
    #col_particular
    mscp = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,Matricula.tipo==None,Matricula.estado == est_mat, Matricula.paralelo != None)).join('papeleta').filter(Papeleta.costo_total == 0).join('modulo').filter(Modulo.numero==u'1').join(['modulo','carrera_programa','nivel']).filter(Nivel.area==area).join('estudiante').filter(Estudiante.procedencia==u'col_particular').distinct().count()
    print u'%s|%s|%s|%s|%s|%s|' %(area.nombre,area.siglas,msa,mscf,mscfm,mscp)

colegios=Colegio.query.all()
for area in areas:
    #saca matriculas de admisiones 
    #por area y por Colegio
    print area.nombre
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,Matricula.tipo==None,Matricula.estado == est_mat, Matricula.paralelo != None)).join('papeleta').filter(Papeleta.costo_total == 0).join('modulo').filter(Modulo.numero==u'1').join(['modulo','carrera_programa','nivel']).filter(Nivel.area==area).distinct().all()
    lista_estudiantes=[(m.estudiante.cedula,m.estudiante.apellidos,m.estudiante.nombres,m.estudiante.datos_personales.colegio,getEdad(m.estudiante.datos_personales.fecha_nacimiento)-1,m.estudiante.datos_personales.colegio.canton_plantel,m.estudiante.datos_personales.colegio.provincia_plantel) for m in ms]
    colegios_area=list(set([l[3] for l in lista_estudiantes]))
    listatotal=[]   
    listatotal.append((u'Colegio',u'Canton',u'Provincia',u'Nro Estudiantes'))
    for col in colegios_area:
        len([l for l in lista_estudiantes if l[3]==col])
        listatotal.append((col.plantel,col.canton_plantel,col.provincia_plantel,str(len([l for l in lista_estudiantes if l[3]==col]))))
    file = open(u"/home/respaldos/Documentos/Admitidos por Colegio %s - %s.csv" %(area.siglas,oa.descripcion) ,"w")
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")

    file.close()



for area in areas:
    #saca matriculas de admisiones 
    #por area y por Canton
    print area.nombre
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,Matricula.tipo==None,Matricula.estado == est_mat, Matricula.paralelo != None)).join('papeleta').filter(Papeleta.costo_total == 0).join('modulo').filter(Modulo.numero==u'1').join(['modulo','carrera_programa','nivel']).filter(Nivel.area==area).distinct().all()
    lista_estudiantes=[(m.estudiante.cedula,m.estudiante.apellidos,m.estudiante.nombres,m.estudiante.datos_personales.colegio,getEdad(m.estudiante.datos_personales.fecha_nacimiento)-1,u'%s-%s' %(m.estudiante.datos_personales.colegio.canton_plantel,m.estudiante.datos_personales.colegio.provincia_plantel)) for m in ms]
    cantones_area=list(set([l[5] for l in lista_estudiantes]))
    listatotal=[]   
    listatotal.append((u'Canton',u'Nro Estudiantes'))
    for can in cantones_area:
        len([l for l in lista_estudiantes if l[5]==can])
        listatotal.append((can,str(len([l for l in lista_estudiantes if l[5]==can]))))
    file = open(u"/home/respaldos/Documentos/Admitidos/%s - %s - %s.csv" %(carrera.nombre,carrera.modalidad,oa.descripcion) ,"w")
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")

    file.close()


for area in areas:
    #saca matriculas de admisiones 
    #por area y por Edad
    print area.nombre
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,Matricula.tipo==None,Matricula.estado == est_mat, Matricula.paralelo != None)).join('papeleta').filter(Papeleta.costo_total == 0).join('modulo').filter(Modulo.numero==u'1').join(['modulo','carrera_programa','nivel']).filter(Nivel.area==area).distinct().all()
    lista_estudiantes=[(m.estudiante.cedula,m.estudiante.apellidos,m.estudiante.nombres,m.estudiante.datos_personales.colegio,getEdad(m.estudiante.datos_personales.fecha_nacimiento)-1,u'%s-%s' %(m.estudiante.datos_personales.colegio.canton_plantel,m.estudiante.datos_personales.colegio.provincia_plantel)) for m in ms]
    edades_area=list(set([l[4] for l in lista_estudiantes]))
    listatotal=[]   
    listatotal.append((u'Area',u'Edad',u'Nro Estudiantes'))
    for edad in edades_area:
        len([l for l in lista_estudiantes if l[4]==can])
        listatotal.append((area.nombre,str(edad),str(len([l for l in lista_estudiantes if l[4]==edad]))))
    file = open(u"/home/respaldos/Documentos/Admitidos por Edades %s - %s.csv" %(area.siglas,oa.descripcion) ,"w")
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")

    file.close()
#################### NOMINA DE ESTUDIANTES ADMITIDOS 2010 ###################################

listatotal=[]
listatotal.append((u'CARRERA',u'MODALIDAD',u'CEDULA',u'APELLIDOS Y NOMBRES',u'GENERO',u'NOMBRE COLEGIO', u'PROVINCIA',u'CANTON',u'FECHA NACIMIENTO',u'PROVINCIA',u'CANTON',u'TIPO COLEGIO',u'CALIFICACION OBTENIDA',u'PERIODO'))
for carrera in carreras:
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,Matricula.tipo==None,Matricula.estado == est_mat, Matricula.paralelo != None)).join('papeleta').filter(Papeleta.costo_total == 0).join('modulo').filter(and_(Modulo.numero==u'1',Modulo.carrera_programa==carrera)).distinct().all()
    listacarrera=[(u'%s %s' %(m.estudiante.apellidos,m.estudiante.nombres),m.estudiante.cedula,u'%s - %s' %(carrera.nombre,carrera.modalidad)) for m in ms]
    listacarrera.sort()
    if len(listatotal) >0:
        listatotal.extend(listacarrera)

file = open(u"/home/respaldos/Documentos/Admitidos/%s.csv" %oa.descripcion ,"w")
for data in listatotal:
    for v in data:
        if v is not None:
                if len(v)==0:
                        file.write("vacio")
                else:
                        file.write(v.encode('utf-8'))
        else:
                file.write("vacio")
        file.write("|")
    file.write("\n")

file.close()



#################################################### REPORTE DE LOS MEJORES ESTUDIANTES PARA BECAS ##############################################
l='5, 19, 72, 42, 22, 23, 32, 34, 25, 79, 78, 80, 91, 74, 77, 73, 71, 6, 3, 8, 7, 21, 35, 36, 38, 33, 37, 40, 43, 44, 2, 45, 39, 95, 1, 96, 98, 2'
l=l.split(',')
l=list(set(l))
cm={}
for id in l:
    c=CarreraPrograma.get(id)
    modulos=[int(mod.numero) for mod in c.modulos]
    modulos.sort()
    um = str(modulos[-1])
    cm[c]=um
    print c,um

areas=[Area.query.all()[0],Area.query.all()[2],Area.query.all()[3],Area.query.all()[6],Area.query.all()[8]]
oa = OfertaAcademica.get(34) #CAMBIAR OFERTA SEGUN CORRESPONDA
est_rep=EstadoMatricula.get_by(estado=u'EstadoMatriculaReprobada')
est_apr=EstadoMatricula.get_by(estado=u'EstadoMatriculaAprobada')
est_mat=EstadoMatricula.get_by(estado=u'EstadoMatriculaMatriculada')
carreras = [carrera for carrera in oa.get_carreras_programas() if carrera.nivel.area in areas]
for carrera in carreras:
    ult_mod = max([mod.numero for mod in oa.modulos if mod.carrera_programa == carrera]) #para que no se tome en cuenta los ultimos modulos
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(and_(Modulo.numero!= ult_mod,Modulo.carrera_programa==carrera)).all()
    lista = []
    lista.append((u'CALIFICACION',u'CEDULA',u'APELLIDOS Y NOMBRES',u'CARRERA','MODULO',u'TELEFONO',u'CELULAR',u'ESTADO DE MATRICULA'))
    for m in ms:
        try:
            prom = m.paralelo.plan_estudio.calcular(m)['total']
        except:
            prom = None
        if prom.__class__.__name__ == 'Decimal':
            m.promedio_acreditacion = prom
        session.flush()
        if m.estado == est_apr: #cm es un diccionario {carrera:ultimomodulo}
            lista.append((m.promedio_acreditacion,u"%s" %m.estudiante.cedula, u"%s %s" %(m.estudiante.apellidos.upper(),m.estudiante.nombres.upper()),u"%s-%s" %(m.modulo.carrera_programa.nombre,m.modulo.carrera_programa.modalidad),m.modulo.numero, u"%s" %m.estudiante.datos_personales.telefono,u"%s" %m.estudiante.datos_personales.celular, u"%s" %m.estado.estado[15:]))
    lista.sort()
    listatotal=[(u"%s" %e[0],e[1],e[2],e[3],e[4],e[5],e[6],e[7]) for e in lista]
    file = open(u"/home/marcoxavi/Escritorio/Beca2-2011/Becas %s-%s %s.csv" %(carrera.nombre,carrera.modalidad,oa.descripcion) ,"w")
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")
    
    file.close()


----------------------
def carrera_optada(m):
    if m.estado == est_reg:
        car = m.estudiante.expediente.examen_admision.carrera_programa
    else:        
        car = Matricula.query.filter(and_(Matricula.estudiante==m.estudiante,Matricula.oferta_academica==oac)).join('modulo').filter(Modulo.numero==u'1').join(['modulo','carrera_programa','nivel']).filter(Nivel.area!=ace).first()
        car = car.modulo.carrera_programa
    return car

def porcentaje(m):
    nb = m.estudiante.expediente.nota_bachillerato.nota
    nbm = m.estudiante.expediente.nota_bachillerato.nota_maxima
    valor_nota_bachiller = Decimal(30)
    if nbm<nb or not nbm or nbm<=0:
        nota_bachillerato = u'S/N'
    else:
        nota_bachillerato = ((nb*valor_nota_bachiller)/nbm)
    return nota_bachillerato

def examen_admision(m):
    try:
        ne = m.estudiante.expediente.examen_admision.calificacion
    except:
        ne = u'S/N'
    return ne


def nota_total(m):
    ex = examen_admision(m)
    porc = porcentaje(m)
    if ex != u'S/N' and porc != u'S/N':
        tot = ex + porc
    else:
        tot = u'S/N'
    return tot



    
    
    
    
    
oa=OfertaAcademica.get(35)
oac=OfertaAcademica.get(36)
mod=Modulo.get(597)
listamal=[]
ms=Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.modulo==mod,or_(Matricula.estado==est_reg,Matricula.estado==est_apr))).distinct().all()
listatotal=[]
listatotal.append((u'NOMBRES Y APELLIDOS',u'CEDULA',u'FECHA NACIMIENTO',u'SEXO',u'COLEGIO',u'TIPO DE INSTITUCIÓN',u'ESPECIALIDAD DEL BACHILLERATO',u'CANTÓN COLEGIO',u'PROVINCIA COLEGIO',u'ADMITIDO',u'AREA',u'CARRERA',u'NOTA TÍTULO DE BACHILLER',u'NOTA QUE OBTUVO EN LA PRUEBA DE ADMISIÓN',u'PORCENTAJE',u'NOTA TOTAL',u'ESTADO CIVIL'))
for m in ms:
    if m.estado == est_reg:
        car = m.estudiante.expediente.examen_admision.carrera_programa
        try:
            listatotal.append((u'%s %s' %(m.estudiante.apellidos,m.estudiante.nombres),m.estudiante.cedula,str(m.estudiante.datos_personales.fecha_nacimiento),m.estudiante.datos_personales.genero,m.estudiante.datos_personales.colegio.plantel,m.estudiante.datos_personales.colegio.sotenimiento_plantel,m.estudiante.expediente.titulo_bachiller.nombres,m.estudiante.datos_personales.colegio.canton_plantel,m.estudiante.datos_personales.colegio.provincia_plantel,u'no admitido',car.nivel.area.siglas,car.nombre,u'%s/%s' %(str(m.estudiante.expediente.nota_bachillerato.nota),str(m.estudiante.expediente.nota_bachillerato.nota_maxima)),str(examen_admision(m)),str(porcentaje(m)),str(nota_total(m)),m.estudiante.datos_personales.estado_civil))
        except:
            print m,m.estado
    else:        
        car = Matricula.query.filter(and_(Matricula.estudiante==m.estudiante,Matricula.oferta_academica==oac)).join('modulo').filter(Modulo.numero==u'1').join(['modulo','carrera_programa','nivel']).filter(Nivel.area!=ace).first()
        if car is None:
            car = Matricula.query.filter(and_(Matricula.estudiante==m.estudiante,Matricula.oferta_academica==oa)).join('modulo').filter(Modulo.numero==u'1').join(['modulo','carrera_programa','nivel']).filter(Nivel.area!=ace).first()            
        car = car.modulo.carrera_programa
        try:
            listatotal.append((u'%s %s' %(m.estudiante.apellidos,m.estudiante.nombres),m.cedula,str(m.estudiante.datos_personales.fecha_nacimiento),m.estudiante.datos_personales.genero,m.estudiante.datos_personales.colegio.plantel,m.estudiante.datos_personales.colegio.sotenimiento_plantel,m.estudiante.expediente.titulo_bachiller.nombres,m.estudiante.datos_personales.colegio.canton_plantel,m.estudiante.datos_personales.colegio.provincia_plantel,u'admitido',car.nivel.area.siglas,car.nombre,u'%s/%s' %(str(m.estudiante.expediente.nota_bachillerato.nota),str(m.estudiante.expediente.nota_bachillerato.nota_maxima)),str(examen_admision(m)),str(porcentaje(m)),str(nota_total(m)),m.estudiante.datos_personales.estado_civil))
        except:
            print m,m.estado

################################## REPORTE PARA PLANIFICACION #############################

oa=OfertaAcademica.get(35)
oac=OfertaAcademica.get(36)
mod=Modulo.get(597)
listamal=[]
############### REGISTRADOS o APROBADOS ES DECIR TODOS ####################################
ms=Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.modulo==mod,or_(Matricula.estado==est_reg,Matricula.estado==est_apr))).distinct().all()
############### que se presentaron a la prueba de admision ####################################
ms=Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.modulo==mod,or_(Matricula.estado==est_reg,Matricula.estado==est_apr))).join(['estudiante','expediente',u'examen_admision']).filter(ExamenAdmision.calificacion > 0).distinct().all()
############### APROBADOS ####################################
ms=Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.modulo==mod,Matricula.estado==est_apr)).distinct().all()
listatotal=[]
listatotal.append((u'CARRERA',u'MODALIDAD',u'CEDULA',u'APELLIDOS Y NOMBRES',u'SEXO',u'COLEGIO',u'PROVINCIA COLEGIO',u'CANTON COLEGIO',u'FECHA NACIMIENTO',u'PROVINCIA PROCEDENCIA',u'CANTON PROCEDENCIA',u'TIPO DE INSTITUCION',u'NOTA TOTAL'))
for m in ms:
    if m.estado == est_reg:
        car = m.estudiante.expediente.examen_admision.carrera_programa
        try:
            listatotal.append((car.nombre,car.modalidad,m.estudiante.cedula,u'%s %s' %(m.estudiante.apellidos,m.estudiante.nombres),m.estudiante.datos_personales.genero,m.estudiante.datos_personales.colegio.plantel,m.estudiante.datos_personales.colegio.provincia_plantel,m.estudiante.datos_personales.colegio.canton_plantel,str(m.estudiante.datos_personales.fecha_nacimiento),m.estudiante.datos_personales.colegio.provincia_plantel,m.estudiante.datos_personales.colegio.canton_plantel,m.estudiante.datos_personales.colegio.sotenimiento_plantel,str(nota_total(m))))
            #listatotal.append((u'%s %s' %(m.estudiante.apellidos,m.estudiante.nombres),m.estudiante.cedula,str(m.estudiante.datos_personales.fecha_nacimiento),m.estudiante.datos_personales.genero,m.estudiante.datos_personales.colegio.plantel,m.estudiante.datos_personales.colegio.sotenimiento_plantel,m.estudiante.expediente.titulo_bachiller.nombres,m.estudiante.datos_personales.colegio.canton_plantel,m.estudiante.datos_personales.colegio.provincia_plantel,u'no admitido',car.nivel.area.siglas,car.nombre,u'%s/%s' %(str(m.estudiante.expediente.nota_bachillerato.nota),str(m.estudiante.expediente.nota_bachillerato.nota_maxima)),str(examen_admision(m)),str(porcentaje(m)),str(nota_total(m)),m.estudiante.datos_personales.estado_civil))
        except:
            print m,m.estado
    else:        
        car = Matricula.query.filter(and_(Matricula.estudiante==m.estudiante,Matricula.oferta_academica==oac)).join('modulo').filter(Modulo.numero==u'1').join(['modulo','carrera_programa','nivel']).filter(Nivel.area!=ace).first()
        if car is None:
            car = Matricula.query.filter(and_(Matricula.estudiante==m.estudiante,Matricula.oferta_academica==oa)).join('modulo').filter(Modulo.numero==u'1').join(['modulo','carrera_programa','nivel']).filter(Nivel.area!=ace).first()            
        car = car.modulo.carrera_programa
        try:
            listatotal.append((car.nombre,car.modalidad,m.estudiante.cedula,u'%s %s' %(m.estudiante.apellidos,m.estudiante.nombres),m.estudiante.datos_personales.genero,m.estudiante.datos_personales.colegio.plantel,m.estudiante.datos_personales.colegio.provincia_plantel,m.estudiante.datos_personales.colegio.canton_plantel,str(m.estudiante.datos_personales.fecha_nacimiento),m.estudiante.datos_personales.colegio.provincia_plantel,m.estudiante.datos_personales.colegio.canton_plantel,m.estudiante.datos_personales.colegio.sotenimiento_plantel,str(nota_total(m))))
            #listatotal.append((u'%s %s' %(m.estudiante.apellidos,m.estudiante.nombres),m.cedula,str(m.estudiante.datos_personales.fecha_nacimiento),m.estudiante.datos_personales.genero,m.estudiante.datos_personales.colegio.plantel,m.estudiante.datos_personales.colegio.sotenimiento_plantel,m.estudiante.expediente.titulo_bachiller.nombres,m.estudiante.datos_personales.colegio.canton_plantel,m.estudiante.datos_personales.colegio.provincia_plantel,u'admitido',car.nivel.area.siglas,car.nombre,u'%s/%s' %(str(m.estudiante.expediente.nota_bachillerato.nota),str(m.estudiante.expediente.nota_bachillerato.nota_maxima)),str(examen_admision(m)),str(porcentaje(m)),str(nota_total(m)),m.estudiante.datos_personales.estado_civil))
        except:
            print m,m.estado

file = open(u"/home/marcoxavi/reportes/admitidosxoferta/Rindieron examen %s.csv" %oa.descripcion ,"w")
for data in listatotal:
    for v in data:
        if v is not None:
                if len(v)==0:
                        file.write("vacio")
                else:
                        file.write(v.encode('utf-8'))
        else:
                file.write("vacio")
        file.write("|")
    file.write("\n")

file.close()

#############################################################################################################
def colegio(e):
    try:
        col=e.datos_personales.colegio.plantel
    except:
        col=u'no establecido'
    return col

def canton_colegio(e):
    try:
        col=e.datos_personales.colegio.canton_plantel
    except:
        col=u'no establecido'
    return col

def provincia_colegio(e):
    try:
        col=e.datos_personales.colegio.provincia_plantel
    except:
        col=u'no establecido'
    return col

def sotenimiento_colegio(e):
    try:
        col=e.datos_personales.colegio.sotenimiento_plantel
    except:
        col=u'no establecido'
    return col


for carrera in carreras:
    listatotal = []
    listatotal.append((u'CARRERA',u'NIVEL',u'LUGAR',u'SISTEMA DE ESTUDIOS',u'MODALIDAD',u'CEDULA',u'APELLIDOS Y NOMBRES',u'GENERO',u'NACIONALIDAD',u'Nro MATRICULA',u'NOMBRE COLEGIO',u'PROVINCIA COLEGIO',u'CANTON COLEGIO',u'FECHA DE NACIMIENTO',u'PROVINCIA PROCEDENCIA',u'CANTON PROCEDENCIA',u'TIPO DE COLEGIO',u'PERIODO',u'MODULO',u'PARALELO'))
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(Modulo.carrera_programa==carrera).all()
    print u'Inicio: %s - %s : %s' %(carrera.nombre,carrera.modalidad, len(ms))
    if len(ms) > 0:
        for m in ms:
            if m.paralelo:
                listatotal.append( (m.modulo.carrera_programa.nombre,m.modulo.carrera_programa.nivel.nivel, u'---', u'SEMESTRAL', carrera.modalidad, m.estudiante.cedula, u'%s %s' %(m.estudiante.apellidos,m.estudiante.nombres), m.estudiante.datos_personales.genero, nacionalidad(m.estudiante.datos_personales), str(m.id), colegio(m.estudiante), provincia_colegio(m.estudiante), canton_colegio(m.estudiante),str(m.estudiante.datos_personales.fecha_nacimiento), m.estudiante.datos_personales.provincia_procedencia, m.estudiante.datos_personales.canton_procedencia, sotenimiento_colegio(m.estudiante), oa.descripcion, m.modulo.numero, m.paralelo.nombre) )
    file = open(u"/home/marcoxavi/reportes/admitidosxoferta/sept2010-feb2011/Matriculados %s-%s %s.csv" %(carrera.nombre, carrera.modalidad, oa.descripcion) ,"w")
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")
    
    file.close()
################################################################################
[10:13:25] patovala se une a la conversación

[10:13:25] roto zalapeva dice:

sabes que me pide el director financiero que necesita unos datos sobre la med

[10:11:10] Jamil dice: 

un reporte sobre los matriculados en los periodos marzo-julio 2010

[10:11:20] Jamil dice: 

y sept 2010 - feb 2011

[10:11:34] Jamil dice: 

cuantos matriculados y los costos ingresados por amtriculas
ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,Matricula.tipo==None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep), Matricula.paralelo != None)).join(['modulo','carrera_programa','nivel']).filter(Nivel.area==area).distinct().all()
oa=OfertaAcademica.get(34)
suma = 0
for m in ms:
    suma += m.papeleta.costo_total
    

######################## Ultimos Modulos de carreras ###################
carreras=[carrera for carrera in oa.get_carreras_programas() if carrera.nivel.area in areas and len(carrera.modulos) != 0]


carreramodalto={}
for carrera in carreras:
    modulos=[int(mod.numero) for mod in carrera.modulos]
    modulos.sort()
    modalto=modulos[-1]
    print carrera.nombre
    print modalto
    print u''
    carreramodalto[carrera.id]=[carrera.nombre,unicode(modalto)]

for carrera in carreras:
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,Matricula.estado == est_apr)).join('modulo').filter(and_(Modulo.numero==carreramodalto[carrera.id][1],Modulo.carrera_programa==carrera)).distinct().count()
    if ms > 0:
        print u'%s - %s' %(carrera.nombre,carrera.modalidad)
        print u'Egresados: %s' %ms
        print u'---'

for carrera in carreras:
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,Matricula.estado == est_apr)).join('modulo').filter(and_(Modulo.numero==carreramodalto[carrera.id][1],Modulo.carrera_programa==carrera)).distinct().count()
    print u'%s - %s ' %(carrera.nombre,carrera.modalidad)
    print u'Egresados: %s' %ms
    print u'---'




################################################### N O T A ############################################
#NOTA:  Ésta es la consulta más optima para encontrar los matriculados en una oferta academica...
#       se puede afinar para hacer busqueda por areas carreras y demas...
ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.paralelo!=None,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join(['modulo','carrera_programa','nivel']).join('papeleta').filter(or_(Papeleta.estado==u'pagada',Papeleta.estado==u'ajustada')).filter(and_(Nivel.area!=ace,Nivel.area!=med)).count()
################################################### N O T A ############################################
for carrera in carreras:    
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.paralelo!=None,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(and_(Modulo.numero==u'1',Modulo.carrera_programa==carrera)).join(['modulo','carrera_programa','nivel']).join('papeleta').filter(or_(Papeleta.estado==u'pagada',Papeleta.estado==u'ajustada')).filter(and_(Nivel.area!=ace,Nivel.area!=med)).count()
    print u'%s - %s - %s' %(carrera.nombre,carrera.modalidad,ms)
###############################################
for carrera in carreras:
    listatotal = []
    listatotal.append((u'CARRERA',u'NIVEL',u'LUGAR',u'SISTEMA DE ESTUDIOS',u'MODALIDAD',u'CEDULA',u'APELLIDOS Y NOMBRES',u'GENERO',u'Nro MATRICULA',u'PERIODO',u'MODULO',u'PARALELO'))
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.paralelo!=None,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(and_(Modulo.numero==u'1',Modulo.carrera_programa==carrera)).join(['modulo','carrera_programa','nivel']).join('papeleta').filter(or_(Papeleta.estado==u'pagada',Papeleta.estado==u'ajustada')).filter(and_(Nivel.area!=ace,Nivel.area!=med)).count()
    print u'Inicio: %s - %s : %s' %(carrera.nombre,carrera.modalidad, len(ms))
    if len(ms) > 0:
        for m in ms:
            if m.paralelo:
                listatotal.append( (m.modulo.carrera_programa.nombre,m.modulo.carrera_programa.nivel.nivel, u'---', u'SEMESTRAL', carrera.modalidad, m.estudiante.cedula, u'%s %s' %(m.estudiante.apellidos,m.estudiante.nombres), m.estudiante.datos_personales.genero, str(m.id), oa.descripcion, m.modulo.numero, m.paralelo.nombre) )
    file = open(u"/home/marcoxavi/Escritorio/admitidosxoferta/sept2010-feb2011/Matriculados %s-%s %s.csv" %(carrera.nombre, carrera.modalidad, oa.descripcion) ,"w")
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")
    
    file.close()



########3
def cuantosarea(carrera,ms):
    if carrera.nivel.area.siglas==u'AEAC':
        aeac+=len(ms)
    if carrera.nivel.area.siglas==u'AEIRNNR':
        aeirnnr+=len(ms)
    if carrera.nivel.area.siglas==u'ASH':
        ash+=len(ms)
    if carrera.nivel.area.siglas==u'AARNR':
        aarnr+=len(ms)
    if carrera.nivel.area.siglas==u'AJSA':
        ajsa+=len(ms)

aeac=0
ash=0
ajsa=0
aeirnnr=0
aarnr=0
otros=0
for carrera in carreras:    
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.paralelo!=None,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(and_(Modulo.numero==u'1',Modulo.carrera_programa==carrera)).join(['modulo','carrera_programa','nivel']).join('papeleta').filter(or_(Papeleta.estado==u'pagada',Papeleta.estado==u'ajustada')).filter(and_(Nivel.area!=ace,Nivel.area!=med)).count()
    print u'%s - %s - %s' %(carrera.nombre,carrera.modalidad,ms)
    if carrera.nivel.area.siglas==u'AEAC':
        aeac+=ms
    if carrera.nivel.area.siglas==u'AEIRNNR':
        aeirnnr+=ms
    if carrera.nivel.area.siglas==u'ASH':
        ash+=ms
    if carrera.nivel.area.siglas==u'AARNR':
        aarnr+=ms
    if carrera.nivel.area.siglas==u'AJSA':
        ajsa+=ms
    if carrera.nivel.area.siglas!=u'AEAC' and carrera.nivel.area.siglas!=u'AEIRNNR'and carrera.nivel.area.siglas!=u'ASH' and carrera.nivel.area.siglas!=u'AARNR' and carrera.nivel.area.siglas!=u'AJSA':
        otros +=ms

################################################# DATOS PATO VILLAMARIN ############################################

for a in areas:
    print area.nombre
    ms = Matricula.query.join("oferta_academica").join(["modulo","carrera_programa","nivel","area"]).filter(OfertaAcademica.id==oa.id).filter(or_(Matricula.estado==est_mat,Matricula.estado==est_apr,Matricula.estado==est_rep)).filter(Matricula.paralelo!=None).filter(Matricula.papeleta != None).filter(Area.siglas==a.siglas).all()
    listatotal=[(unicode(m.estudiante.cedula),unicode(m.id),m.estudiante.apellidos,m.estudiante.nombres,m.modulo.carrera_programa.nombre,m.modulo.numero,m.paralelo.nombre,m.paralelo.seccion,a.siglas) for m in ms]
	file = open(u"/home/marcoxavi/Escritorio/Matriculados %s-%s.csv" %(carrera.nombre, oa.descripcion) ,"w")
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")
    file.close()

##################################### PARA SACAR LOS PROFES ###########################################
profe_horarios_semana = [(h.docente.cedula,h.docente.apellidos,h.docente.nombres, h.docente.titulo,h.jornada.paralelo.nombre,h.jornada.paralelo.seccion,h.jornada.paralelo.modulo.numero,h.jornada.paralelo.modulo.carrera_programa.nombre,h.jornada.paralelo.modulo.carrera_programa.nivel.area.siglas,h.unidad.nombre) for h in HorarioSemana.query.join(["jornada","paralelo","oferta_academica"]).filter(OfertaAcademica.id == oa.id).all() if h.docente is not None]

for a in areas:
    print area.nombre
    profe_horarios_semana = [(h.docente.cedula,h.docente.apellidos,h.docente.nombres, h.docente.titulo,h.jornada.paralelo.nombre,h.jornada.paralelo.seccion,h.jornada.paralelo.modulo.numero,h.jornada.paralelo.modulo.carrera_programa.nombre,h.jornada.paralelo.modulo.carrera_programa.nivel.area.siglas,h.unidad.nombre) for h in HorarioSemana.query.join(["jornada","paralelo","oferta_academica"]).filter(OfertaAcademica.id == oa.id).join("unidad","plan_estudio","modulo","carrera_programa","nivel").filter(Nivel.area == a).all() if h.docente is not None]
	file = open(u"/home/marcoxavi/Escritorio/Docentes %s-%s.csv" %(carrera.nombre, oa.descripcion) ,"w")
	for data in profe_horarios_semana:
		for v in data:
		    if v is not None:
		            if len(v)==0:
		                    file.write("vacio")
		            else:
		                    file.write(v.encode('utf-8'))
		    else:
		            file.write("vacio")
		    file.write("|")
		file.write("\n")
	file.close()
####################################### CAMBIAR CLAVE A USUARIO ############################################
                     u.password = identity.current_provider.encrypt_password(cedula)
############################################################################################################
respaldos/.wine/drive_c/windows/profiles/respaldos/Configuración local/Datos de programa/Ares/My Shared Folder

file=open("evaluados_28.csv")
lineas=file.readlines()

for l in lineas:
    l=l.strip().split(';')
    if not EvaluacionDocente.get_by(cedula=l[0].replace('"','')):
        e=EvaluacionDocente()
        e.cedula=l[0].replace('"','')
        e.matid=l[1].replace('"','')
        session.flush()






##############33
oa.get_carreras_programas()
est_mat = EstadoMatricula.get_by(estado = u"EstadoMatriculaMatriculada")
est_apr = EstadoMatricula.get_by(estado = u"EstadoMatriculaAprobada")
est_rep = EstadoMatricula.get_by(estado = u"EstadoMatriculaReprobada")

for carrera in carreras:
    listatotal = []
    listatotal.append((u'CARRERA',u'NIVEL',u'LUGAR',u'SISTEMA DE ESTUDIOS',u'MODALIDAD',u'CEDULA',u'APELLIDOS Y NOMBRES',u'GENERO',u'Nro MATRICULA',u'PERIODO',u'MODULO',u'PARALELO',u'EMAIL'))
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.paralelo!=None,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('papeleta').filter(or_(Papeleta.estado==u'pagada',Papeleta.estado==u'ajustada')).join(['modulo','carrera_programa','nivel']).filter(and_(Nivel.area!=ace,Nivel.area!=med)).join('modulo').filter(Modulo.carrera_programa==carrera).all()
    print u'Inicio: %s - %s : %s' %(carrera.nombre,carrera.modalidad, len(ms))
    if len(ms) > 0:
        for m in ms:
            if m.paralelo:
                listatotal.append( (m.modulo.carrera_programa.nombre,m.modulo.carrera_programa.nivel.nivel, u'---', u'SEMESTRAL', carrera.modalidad, m.estudiante.cedula, u'%s %s' %(m.estudiante.apellidos,m.estudiante.nombres), m.estudiante.datos_personales.genero, str(m.id), oa.descripcion, m.modulo.numero, m.paralelo.nombre,u'%s' %m.estudiante.datos_personales.email) )
    file = open(u"/home/marcoxavi/Escritorio/admitidosxoferta/sept2009-feb2010/Matriculados %s-%s %s.csv" %(carrera.nombre, carrera.modalidad, oa.descripcion) ,"w")
    for data in listatotal:
        for v in data:
            if v is not None:
                    if len(v)==0:
                            file.write("vacio")
                    else:
                            file.write(v.encode('utf-8'))
            else:
                    file.write("vacio")
            file.write("|")
        file.write("\n")
    
    file.close()

######################## Poblacion Estudiantil por Carrera ############################
areas=[Area.query.all()[0],Area.query.all()[2],Area.query.all()[3],Area.query.all()[6],Area.query.all()[8]]
carreras = [carrera for carrera in oa.get_carreras_programas() if carrera.nivel.area in areas]

est_mat = EstadoMatricula.get_by(estado = u"EstadoMatriculaMatriculada")
est_apr = EstadoMatricula.get_by(estado = u"EstadoMatriculaAprobada")
est_rep = EstadoMatricula.get_by(estado = u"EstadoMatriculaReprobada")
for carrera in carreras:
    ms = Matricula.query.filter(and_(Matricula.oferta_academica==oa,Matricula.papeleta != None,or_(Matricula.estado == est_mat,Matricula.estado == est_apr,Matricula.estado == est_rep))).join('modulo').filter(Modulo.carrera_programa==carrera).count()
    print carrera.nombre,carrera.modalidad,ms


#http://elbarrio.forumfree.it/?t=54830262



################ SCRIPT PARA COPIAR BANCO DE PREGUNTAS ##########################
bancos = [b for b in BancoPreguntas.query.all() if b.estado==u'activo']
b = bancos[0]
bancon = BancoPreguntas("Nombre nuevo banco")

file_resp = open(u"/home/patovala/id_resp.csv" ,"w")
file_preg = open(u"/home/patovala/id_preg.csv" ,"w")
#TODO: controlar cuando sean RespuestaNoContestada para que no se cree
for p in b.preguntas:
    pn = Pregunta()
    pn.enunciado = p.enunciado
    pn.valoracion = p.valoracion
    pn.path = p.path
    bancon.preguntas.append(pn)               
    session.flush()    
    if p.path is not None and p.path == u'si':
        file_preg.write(u"%s|%s\n" %(p.id,pn.id))
    for resp in p.respuestas:
        rn = Respuesta()
        rn.texto_respuesta = resp.texto_respuesta
        rn.correcta = resp.correcta
        rn.path = resp.path
        pn.respuestas.append(rn)
        session.flush()  
        if resp.path is not None and resp.path == u'si':
            file_resp.write(u"%s|%s\n" %(resp.id,rn.id))


file_preg.close()
file_resp.close()

-------------------------------- encerar Bancos ------------------
idcarreras=[2,8,1,98,5,7,3,6,72,73,74,71,96,19,20,21,22,23,78,79,77,80,35,37,34,32,38,33,40,39,45,36,44,43,42]
for carrera in carreras:
    print carrera
    for c in carrera.caracteristicas_bp:
        print c.banco_preguntas        
    print '------'

for carrera in carreras:
    print carrera
    for c in carrera.caracteristicas_bp:
        print c.banco_preguntas
        c.delete()
        session.flush()
    print '------'
---------------------------------------------
--------------------------- Aranceles ----------------------
aranceles son los pagados de una oferta

colegios = list(set([a.estudiante.datos_personales.colegio for a in aranceles]))
suma = 0
for col in colegios:    
    arancelescolegio = [ a for a in aranceles if a.estudiante.datos_personales.colegio == col]
    if col is not None:
        print "%s|%s|%s|%s" %(col.plantel,col.canton_plantel,col.provincia_plantel,len(arancelescolegio))
    else:
        print "Sin Colegio|%s" %len(arancelescolegio)
    suma+=len(arancelescolegio)
------------ por componentes -----------
componentes = Componente.query.all()
--------------- forma 1 --------------------
for c in componentes:
    print u"%s|%s" %(c.nombre,len([a for a in aranceles if c in a.componentes]))
--------------- forma 2 --------------------    
[(c.nombre,len([a for a in aranceles if c in a.componentes])) for c in componentes]




##################### INSCRITOS, VALIDADOS Y EXÁMENES DADOS DE ADMISIONES 2011 #########################
oa=OfertaAcademica.get(43)
examenes = ExamenAdmision.query.join('paralelo').filter(Paralelo.oferta_academica == oa).all()
carreras = oa.get_carreras_programas()
suma = 0
sumadadoa = 0
for car in carreras:
    numex = ExamenAdmision.query.filter(ExamenAdmision.carrera_programa == car).join('paralelo').filter(Paralelo.oferta_academica == oa).count()
    numexdados = ExamenAdmision.query.filter(and_(ExamenAdmision.carrera_programa == car,ExamenAdmision.calificacion >0)).join('paralelo').filter(Paralelo.oferta_academica == oa).count()
    print u'%s|%s|%s|%s' %(car.nombre,car.modalidad,numex,numexdados)
    suma += numex
    sumadadoa += numexdados


################################# VALIDADOS ADMISIONES 2011 #############################################
oa=OfertaAcademica.get(43)
examenes = ExamenAdmision.query.join('paralelo').filter(Paralelo.oferta_academica == oa).all()
listatotal = []
for ex in examenes:
    if len(ex.expediente.estudiante.sel_carrera_opcionales) == 0:
        listatotal.append((u'%s %s' %(ex.expediente.estudiante.apellidos,ex.expediente.estudiante.nombres),'%s' %ex.expediente.estudiante.cedula,ex.expediente.estudiante.datos_personales.genero,ex.carrera_programa.nombre,u'sin carrera opcional',u'%s' %ex.expediente.estudiante.datos_personales.fecha_nacimiento))
    else:
        listatotal.append((u'%s %s' %(ex.expediente.estudiante.apellidos,ex.expediente.estudiante.nombres),'%s' %ex.expediente.estudiante.cedula,ex.expediente.estudiante.datos_personales.genero,ex.carrera_programa.nombre,ex.expediente.estudiante.sel_carrera_opcionales[-1].carrera.nombre,u'%s' %ex.expediente.estudiante.datos_personales.fecha_nacimiento))
file = open(u"/home/marcoxavi/Escritorio/DatosEstudiantesInscritos%s.csv" %oa.descripcion ,"w")
for data in listatotal:
    for v in data:
        if v is not None:
                if len(v)==0:
                        file.write("vacio")
                else:
                        file.write(v.encode('utf-8'))
        else:
                file.write("vacio")
        file.write("|")
    file.write("\n")

file.close()

-------------------------

def tiene(e=None):
    oa = OfertaAcademica.get(36)
    mat = Matricula.query.filter(Matricula.oferta_academica==oa,Matricula.estudiante==e).distinct().all()
    if len == 0:
        return False
    else:
        return True


-------------------------



carrera=CarreraPrograma.get(14)
mod1 =  Modulo.get(256)
p = Paralelo.get(8241)
mod

for c in cedulas:
    e=Estudiante.get_by(cedula=c)
    if e:
        e.expediente.examen_admision.carrera_programa = carrera
        mat_carrera = Matricula.query.filter(and_(Matricula.modulo!=mod_admisiones,Matricula.estado==est_pre,Matricula.estudiante==e,Matricula.oferta_academica==oa)).first()
        mat_carrera.modulo = mod1
        e.expediente.examen_admision.paralelo = p
        session.flush()
        for m in e.matriculas:
            if m.modulo.id==620 and m.oferta_academica == oa:
                m.paralelo = p
        session.flush()
    else:
        print "mal %s" %c

### para ver cuantos examenes igual a cero

print len([c for c in cedulas if Estudiante.get_by(cedula=c) and Estudiante.get_by(cedula=c).expediente.examen_admision.calificacion == 0])

    
    
    
    
idcarreras=["54","122","56","9","13","14","15","53"]
    

###################3

for c in cedulas:
    e=Estudiante.get_by(cedula=c)    
    if e:
        print "###"        
        print u'Carrera del expediante: %s-%s' %(e.expediente.examen_admision.carrera_programa.nombre,e.expediente.examen_admision.carrera_programa.modalidad)
        mat_carrera = Matricula.query.filter(and_(Matricula.modulo!=mod_admisiones,Matricula.estado==est_pre,Matricula.estudiante==e,Matricula.oferta_academica==oa)).first()
        print "mat_carrera - carrera a la que va: %s-%s" %(mat_carrera.modulo.carrera_programa.nombre,mat_carrera.modulo.carrera_programa.modalidad)
        print "mat_carrera oferta: %s" %mat_carrera.oferta_academica
        print "paralelos: %s" %[m for m in e.expediente.examen_admision.paralelo.matriculas if m.estudiante == e]
        print "Examen Calificacion: %s " %e.expediente.examen_admision.calificacion
        print "estudiante: %s" %e.cedula
    else:
        print "mal %s" %c

for c in cedulas:
    e=Estudiante.get_by(cedula=c)
    if not e:
        e
        
        

    
##################

while 1:
    s = file.readline()
    if not s:
        break
    linea = s.split("|")
    c = CertificadoVotacion.get_by(cedula=linea[0]+linea[1])
    if c:
        c.codigo1=linea[3]
        c.codigo2=linea[4][:-2]
        session.flush()
    else:
        ced = CertificadoVotacion()
        ced.cedula=linea[0]+linea[1]
        ced.codigo1=linea[3]
        ced.codigo2=linea[4][:-2]
        session.flush()

file.close()

