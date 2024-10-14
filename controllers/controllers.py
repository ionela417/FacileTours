from odoo import http
from odoo.http import request, route, Controller

class CustomFormController(Controller):
     
    @http.route(['/shop/custom_form'], type='http', auth='public', website=True, csrf=False)
    def custom_form(self, **post):
        # Render your custom form template
        return request.render('your_custom_module.custom_form_template', {})

    @route(['/submit/custom/form'], type='http', auth="public", website=True, methods=['POST'])
    def submit_custom_form(self, **post):
        # Get form data
        nome = post.get('zxiz6mpqr47')
        cognome = post.get('yu0h7t6liuj')
        codice_fiscale = post.get('ebxoyrz9cg')
        email = post.get('3ftq9ooocp1')
        numero_telefono = post.get ('mhhfbu34tzb')
        luogo_pickup = post.get('lb7wksag1z')
        numero_partecipanti = post.get('ttwqp4nzzml')
        lingua = post.get('otlvho0im6c')
        data = post.get('m1qzntbc58')
        assistenza_disabile = post.get('layi4xnp3w')
        richieste_extra = post.get('ktf4dsr8yia')

        # Get the current sale order
        sale_order = request.website.sale_get_order()

        if sale_order:
            # Update the sale order with processed data
            sale_order.write({
                'nome': nome,
                'cognome': cognome,
                'codice_fiscale': codice_fiscale,
                'email': email,
                'numero_telefono': numero_telefono,
                'luogo_pickup': luogo_pickup,
                'numero_partecipanti': numero_partecipanti,
                'lingua': lingua,
                'data': data,
                'assistenza_disabile': assistenza_disabile,
                'richieste_extra': richieste_extra

            })

        # Redirect or return response as needed
        return request.redirect("/shop/payment")