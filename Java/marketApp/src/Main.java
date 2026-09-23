import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.TreeMap;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        List<Producto> productos = new ArrayList<>();
        List<Venta> ventas = new ArrayList<>();

        int opcion = 0;

        while (opcion != 5) {

            System.out.println();
            System.out.println("========================");
            System.out.println("        MARKET APP");
            System.out.println("========================");
            System.out.println("1. Ingresar producto");
            System.out.println("2. Eliminar producto");
            System.out.println("3. Vender producto");
            System.out.println("4. Resumen de caja");
            System.out.println("5. Salir");
            System.out.println("========================");
            System.out.print("Seleccione una opción: ");

            opcion = scanner.nextInt();
            scanner.nextLine(); // limpia el salto de línea pendiente

            if (opcion == 1) {
                System.out.println();
                System.out.println("--- INGRESAR PRODUCTO ---");

                System.out.println("Ingrese codigo de producto: ");
                String codigoProducto = scanner.nextLine();

                System.out.println("Ingrese nombre de producto: ");
                String nombreProducto = scanner.nextLine();

                System.out.println("Ingrese precio del producto: ");
                Double precioProducto = scanner.nextDouble();

                System.out.println("Ingrese stock: ");
                int stockProducto = scanner.nextInt();

                boolean existe = false;
                for (Producto p: productos) {
                    if(p.getCodigo().equals(codigoProducto)){
                        existe = true;
                        break;
                    }
                }

                if (!existe){
                System.out.println("El codigo "+codigoProducto+" ya existe.");
                }


            } else if (opcion == 2) {
                System.out.println();
                System.out.println("--- ELIMINAR PRODUCTO ---");

                // TODO:
                // 1. Pedir el código.
                // 2. Buscar el producto en la lista.
                // 3. Eliminarlo si existe.

            } else if (opcion == 3) {
                System.out.println();
                System.out.println("--- VENDER PRODUCTO ---");

                // TODO:
                // 1. Pedir código y cantidad.
                // 2. Buscar el producto.
                // 3. Verificar stock.
                // 4. Descontar stock.
                // 5. Crear una Venta y agregarla a la lista de ventas.

            } else if (opcion == 4) {
                System.out.println();
                System.out.println("--- RESUMEN DE CAJA ---");

                // TODO:
                // Recorrer la lista de ventas y calcular el resumen.

            } else if (opcion == 5) {
                System.out.println();
                System.out.println("Gracias por utilizar MarketApp.");

            } else {
                System.out.println();
                System.out.println("Opción no válida. Intente nuevamente.");
            }
        }

        scanner.close();
    }
}