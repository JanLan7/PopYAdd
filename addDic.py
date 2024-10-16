libros_por_genero = {
    "Fantasía": ["El Señor de los Anillos", "Harry Potter"],
    "Ciencia Ficción": ["Dune", "Neuromante"],
    "Misterio": ["El nombre de la rosa", "El código Da Vinci"],
    "Romance": ["Orgullo y Prejuicio", "Crepúsculo"]
}

libros_fantasia = libros_por_genero.pop("Fantasía")
libros_ciencia_ficcion = libros_por_genero.pop("Ciencia Ficción", {})
libros_de_misterio = libros_por_genero.pop("Misterio")
libros_de_romance =  libros_por_genero.pop("Romance", {})

print(libros_fantasia)
print(libros_de_romance)
