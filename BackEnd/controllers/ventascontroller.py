import os
from collections import defaultdict
from datetime import datetime
from xml.etree import ElementTree as ET
from flask import Blueprint, jsonify, request
from clases import Venta

BlueprintVenta = Blueprint('venta', __name__)

departamentos_permitidos = [
    'Guatemala', 'Quetzaltenango', 'Sacatepequez', 'Huehuetenango', 'San Marcos', 'Quiche', 'Suchitepequez',
    'Escuintla', 'Chimaltenango', 'Santa Rosa', 'Solola', 'Totonicapan', 'Zacapa', 'Chiquimula', 'Jalapa',
    'Izabal', 'El Progreso', 'Peten', 'Jutiapa', 'Baja Verapaz', 'Alta Verapaz', 'Retalhuleu'
]

@BlueprintVenta.route('/venta/cargar', methods=['POST'])
def cargarVentas():
    ventas = precargarXML()
    try:
        # Lee el xml que obtiene de entrada
        xml_entrada = request.data.decode('utf-8')
        if xml_entrada == '':
            return jsonify({
                'mensaje': 'No se ha enviado un xml',
                'status': 400
            }),400
        # Parsea el xml al Element Tree
        root = ET.fromstring(xml_entrada)
        #recorremos el root de ventas
        for venta in root:
            #recorremos las etiquetas de la venta
            for elemento in venta:
                departamento = venta.get('departamento')
                nueva_venta = Venta(departamento)
                ventas.append(nueva_venta)
        # Guardamos la lista de ventas en el archivo xml
        crearXML(ventas)
        return jsonify({
            'mensaje': 'Ventas cargadas',
            'status': 200
        }),200
    except KeyError as e:
        return jsonify({
            'mensaje': str(e),
            'status': 500
        }),500


@BlueprintVenta.route('/venta/procesar', methods=['POST'])
def procesarVenta():
    ventas = precargarXML()
    try:
        xml_entrada = request.data.decode('utf-8')
        if xml_entrada == '':
            return jsonify({
                'mensaje': 'No se ha enviado un xml',
                'status': 400
            }),400
        root = ET.fromstring(xml_entrada)
        for elemento in root:
            pass
        nueva_venta = Venta(contador_ventas, fecha, hora, cliente)
        nueva_venta.setProductos(productos)
        ventas.append(nueva_venta)
        total_nueva_venta = 0
        for producto in nueva_venta.getProductos():
            total_nueva_venta += producto.subtotal
        crearXML(ventas)
        xml_salida = '''<compra>
    <nombre>'''+nueva_venta.cliente.nombre+'''</nombre>
    <nit>'''+nueva_venta.cliente.nit+'''</nit>
    <fecha>'''+str(nueva_venta.fecha)+'''</fecha>
    <hora>'''+str(nueva_venta.hora)+'''</hora>
    <total>'''+str(total_nueva_venta)+'''</total>
</compra>
'''
        return jsonify({
            'mensaje': 'Venta procesada',
            'xml': xml_salida,
            'status': 200
        }),200
    except:
        return jsonify({
            'mensaje': 'Error al leer el xml',
            'status': 500
        }),500

def crearXML(ventas):
    if os.path.exists('database/ventas.xml'):
        os.remove('database/ventas.xml')
    tree = ET.Element('ventas')
    for venta in ventas:
        venta_xml = ET.SubElement(tree, 'venta')
        venta_xml.set('departamento', venta.getDepartamento())
    tree = ET.ElementTree(tree)
    ET.indent(tree, space="\t", level=0)
    tree.write('database/ventas.xml', encoding='utf-8', xml_declaration=True)


def precargarXML():
    ventas = []
    if os.path.exists('database/ventas.xml'):
        tree = ET.parse('database/ventas.xml')
        root = tree.getroot()
        for venta in root.find('ListadoVentas'):
            departamento = venta.get('departamento')
            nueva_venta = Venta(departamento)
            ventas.append(nueva_venta)
    return ventas