# -*- coding: utf-8 -*-
from odoo import fields, models, api

class CuestionarioLlave(models.Model):
    _name = "cuestionario.llave"
    _description = "Cuestionario Llave"

    contacto = fields.Many2one('crm.lead', string='Contacto')
    llamada = fields.Many2one('llamadas', string='Llamada')
    nombre = fields.Char('Nombre')
    rango_edad = fields.Boolean('1. ¿Es usted mayor de 18 años y menor de 65 años?')
    lactancia = fields.Boolean('2. ¿Está usted embarazada o en periodo de lactancia?')
    conoce_peso_talla = fields.Boolean('3. ¿Conoce su peso y talla?')
    peso = fields.Float('Peso (Kg)')
    talla = fields.Float('Talla (m)')
    imc = fields.Float('IMC',compute="_imc")
    @api.depends()
    def _imc(self):
        for record in self:
            if record.peso > 0 and record.talla > 0:
                record.imc = record.peso / (record.talla**2)
            else:
                record.imc = 0
    clasificacion = fields.Selection([
        ('1','Normopeso'),
        ('2','Sobrepeso'),
        ('3','Obesidad grado I'),
        ('4','Obesidad grado II'),
        ('5','Obesidad grado III'),
        ('6','Obesidad grado IV')],
        string="Clasificación IMC",
        compute="_calcula_imc"
    )
    @api.depends()
    def _calcula_imc(self):
        for record in self:
            if record.imc > 0:
                if record.imc > 18.49 and record.imc < 24.99:
                    record.clasificacion = "1"
                elif record.imc < 29.99:
                    record.clasificacion = "2"
                elif record.imc < 34.99:
                    record.clasificacion = "3"
                elif record.imc < 39.99:
                    record.clasificacion = "4"
                elif record.imc < 49.99:
                    record.clasificacion = "5"
                elif record.imc > 50:
                    record.clasificacion = "6"
            else:
                record.clasificacion = None
    diabetes = fields.Boolean('4. ¿Le han diagnosticado con diabetes?')
    hipertension = fields.Boolean('5. ¿Le han diagnosticado con hipertensión?')
    contraindicaciones_anfepramona_y_mazindol = fields.Boolean('6. ¿Le han diagnosticado con hipertiroidismo, glaucoma, ateroesclerosis avanzada, enfermedad cardiovascular, insuficiencia cardíaca severa o arritmia?')
    enfermedad_renal_severa = fields.Boolean('7. ¿Le han diagnosticado con enfermedad renal severa?')
    insuficiencia_hepatica_severa = fields.Boolean('8. ¿Le han diagnosticado con insuficiencia hepática severa?')
    inhibidores_o_bloqueadores = fields.Boolean('9. ¿Actualmente está en tratamiento con inhibidores de la monoaminoxidasa (IMAO), bloqueadores ganglionares o neurales?')
    medicamento_baja_peso = fields.Boolean('10. ¿Ha estado en tratamiento con medicamentos para bajar de peso o supresores del apetito?')
    medicamento_y_adversidad = fields.Text('11. En caso de responder sí a la pregunta anterior: ¿recuerda qué medicamento fue y si tuvo algún evento adverso?')
    agitacion_tpm_insomnio = fields.Boolean('12. ¿Le han diagnosticado con algún trastorno psiquiátrico relacionado con estados de agitación, trastorno de personalidad múltiple o insomnio crónico?')
    abuso_substancias = fields.Boolean('13. ¿Tiene antecedente de abuso de sustancias (alcohol, drogas o cualquier otro medicamento)?')
    contraindicacion_neobes_hombre = fields.Boolean('14a. En caso de ser hombre: ¿Le han diagnosticado hipertrofia prostática benigna o cualquier padecimiento obstructivo de las vías urinarias o tracto gastrointestinal?')
    contraindicacion_neobes_mujer = fields.Boolean('14b. En caso de ser mujer: ¿Le han algún padecimiento obstructivo de las vías urinarias o tracto gastrointestinal?')
    estudios_recientes = fields.Boolean('15. ¿Se ha realizado estudios de laboratorio y/o gabinete en los últimos 30 días? En caso afirmativo ¿cuáles y por qué se los indicaron?')