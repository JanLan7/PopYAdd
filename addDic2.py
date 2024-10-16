productos_en_almacen = {
    "Electrónica": ["Televisor", "Celular"],
    "Ropa": ["Camisa", "Pantalón"],
    "Juguetes": ["Pelota", "Muñeca"],
    "Muebles": ["Mesa", "Silla"]
}

productos_electronica = productos_en_almacen.pop("Electrónica")
productos_ropa = productos_en_almacen.pop("Ropa",{})
del productos_en_almacen["Juguetes"]
print(productos_en_almacen)