// src/api/api.ts

// Simulación de datos de inventario
let inventario = [
  { id: 1, nombre: "Laptop", categoria: "Electrónica", stock: 8, minimo: 5 },
  { id: 2, nombre: "Mouse", categoria: "Electrónica", stock: 3, minimo: 10 },
  { id: 3, nombre: "Silla", categoria: "Muebles", stock: 15, minimo: 5 },
  { id: 4, nombre: "Escritorio", categoria: "Muebles", stock: 4, minimo: 6 },
  { id: 5, nombre: "Café", categoria: "Alimentos", stock: 20, minimo: 10 },
];

// 🚀 Obtener todos los productos
export function getInventario() {
  return Promise.resolve(inventario);
}

// 🚀 Agregar un nuevo producto
export function agregarProducto(producto: {
  nombre: string;
  categoria: string;
  stock: number;
  minimo: number;
}) {
  const nuevo = { id: Date.now(), ...producto };
  inventario.push(nuevo);
  return Promise.resolve(nuevo);
}

// 🚀 Actualizar un producto
export function actualizarProducto(id: number, cambios: Partial<typeof inventario[0]>) {
  const index = inventario.findIndex((p) => p.id === id);
  if (index !== -1) {
    inventario[index] = { ...inventario[index], ...cambios };
    return Promise.resolve(inventario[index]);
  }
  return Promise.reject("Producto no encontrado");
}

// 🚀 Eliminar un producto
export function eliminarProducto(id: number) {
  inventario = inventario.filter((p) => p.id !== id);
  return Promise.resolve(true);
}
