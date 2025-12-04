def summarize_numbers(numbers_list):
    # Calcula mínimo, máximo y promedio usando la lista ya validada
    result = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return result


# --- Código principal ---
numbers_text = input("Ingresa números separados por comas: ")

# Validación: texto no vacío
if not numbers_text.strip():
    print("Error: invalid input")
else:
    try:
        # Convertir a lista de números
        numbers_list = [float(num.strip()) for num in numbers_text.split(",") if num.strip()]

        # Validación: lista no vacía
        if not numbers_list:
            print("Error: invalid input")
        else:
            # Obtener resumen usando la función
            summary = summarize_numbers(numbers_list)

            print("Min:", summary["min"])
            print("Max:", summary["max"])
            print("Average:", summary["average"])

    except ValueError:
        # Si alguno no es número válido
        print("Error: invalid input")