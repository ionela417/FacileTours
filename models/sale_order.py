from odoo import models, fields

class ExtendedSaleOrder(models.Model):
    _inherit = 'sale.order'

    nome = fields.Char(string="Nome", required=True, default="")
    cognome = fields.Char(string="Cognome", required=True, default="")
    codice_fiscale = fields.Char(string="Codice Fiscale", required=True, default="")
    email = fields.Char(string="Email", required=True, default="")
    numero_telefono = fields.Char(string="Numero di telefono", required=True, default="")
    luogo_pickup = fields.Char(string="Luogo di pickup", required=True, default="")
    numero_partecipanti = fields.Integer(string="Numero partecipanti", required=True, default=1)
    lingua = fields.Char(string="Lingua", required=True, default="")
    data = fields.Date(string="Data")
    assistenza_disabile = fields.Boolean(string="Assistenza disabile", default=False)
    richieste_extra = fields.Text(string="Richieste extra")