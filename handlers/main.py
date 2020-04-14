#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2



def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

class MainHandler(webapp2.RequestHandler):

    def post(self):
        cif = self.request.get("edCif", "0")
        nombre = self.request.get("edNombre", "0")
        direccion = self.request.get("edDireccion", "0")
        poblacion = self.request.get("edPoblacion", "0")
        provincia = self.request.get("edProvincia", "0")
        cp = self.request.get("edCP", "0")
        pais = self.request.get("edPais", "0")
        contacto = self.request.get("edContacto", "0")
        email = self.request.get("edEmail", "0")
        telefono = self.request.get("edTelefono", "0")

        cifCliente = self.request.get("edCifc", "0")
        nombreCliente = self.request.get("edNombrec", "0")
        direccionCliente = self.request.get("edDireccionc", "0")
        poblacionCliente = self.request.get("edPoblacionc", "0")
        provinciaCliente = self.request.get("edProvinciac", "0")
        cpCliente = self.request.get("edCPc", "0")
        paisCliente = self.request.get("edPaisc", "0")
        contactoCliente = self.request.get("edContactoc", "0")
        emailCliente = self.request.get("edEmailc", "0")
        telefonoCliente = self.request.get("edTelefonoc", "0")

        concepto = self.request.get("edConcepto", "0")
        prunidad = self.request.get("edPrunidad", "0")
        unidades = self.request.get("edUnidades", "0")
        bruto = self.request.get("edBruto", "0")
        iva = self.request.get("edIva", "0")





        if len(cif.strip()) == 0:
            cif = "Desconocido"
        if len(nombre.strip()) == 0:
            nombre = "Desconocido"
        if len(direccion.strip()) == 0:
            direccion = "Desconocido"
        if len(poblacion.strip()) == 0:
            poblacion = "Desconocido"
        if len(provincia.strip()) == 0:
           provincia = "Desconocido"
        if len(cp.strip()) == 0:
            cp = "Desconocido"
        if len(pais.strip()) == 0:
            pais = "Desconocido"
        if len(contacto.strip()) == 0:
            contacto = "Desconocido"
        if len(email.strip()) == 0:
            email = "Desconocido"
        if len(telefono.strip()) == 0:
            telefono = "Desconocido"

        if len(cifCliente.strip()) == 0:
            cifCliente = "Desconocido"
        if len(nombreCliente.strip()) == 0:
            nombreCliente = "Desconocido"
        if len(direccionCliente.strip()) == 0:
            direccionCliente = "Desconocido"
        if len(poblacionCliente.strip()) == 0:
            poblacionCliente = "Desconocido"
        if len(provinciaCliente.strip()) == 0:
           provinciaCliente = "Desconocido"
        if len(cpCliente.strip()) == 0:
            cpCliente = "Desconocido"
        if len(paisCliente.strip()) == 0:
            paisCliente = "Desconocido"
        if len(contactoCliente.strip()) == 0:
            contactoCliente = "Desconocido"
        if len(emailCliente.strip()) == 0:
            emailCliente = "Desconocido"
        if len(telefonoCliente.strip()) == 0:
            telefonoCliente = "Desconocido"

        if len(concepto.strip()) == 0 :
            concepto = "Desconocido"
        if len(prunidad.strip()) == 0 or isFloat(prunidad) == False:
            prunidad = 0
        if len(unidades.strip()) == 0 or isFloat(unidades) == False:
            unidades = 0
        if len(iva.strip()) == 0 or isFloat(iva) == False:
            iva = 0

        bruto=float(unidades)*float(prunidad)
        precio=float(bruto)*(1+(float(iva)/100))
        total=precio

        jinja = jinja2.get_jinja2(app=self.app)

        valores_plantilla = {
            "cif": cif,
            "nombre": nombre,
            "direccion": direccion,
            "poblacion": poblacion,
            "provincia": provincia,
            "cp": cp,
            "pais": pais,
            "contacto": contacto,
            "email": email,
            "telefono": telefono,
            "cifCliente": cifCliente,
            "nombreCliente": nombreCliente,
            "direccionCliente": direccionCliente,
            "poblacionCliente": poblacionCliente,
            "provinciaCliente": provinciaCliente,
            "cpCliente": cpCliente,
            "paisCliente": paisCliente,
            "contactoCliente": contactoCliente,
            "emailCliente": emailCliente,
            "telefonoCliente": telefonoCliente,
            "concepto": concepto,
            "precio": precio,
            "prunidad": prunidad,
            "iva": iva,
            "unidades": unidades,
            "bruto": bruto,
            "total": total
        }

        self.response.write(jinja.render_template("answer.html", **valores_plantilla))




app = webapp2.WSGIApplication([
    ('/factura', MainHandler)
], debug=True)
