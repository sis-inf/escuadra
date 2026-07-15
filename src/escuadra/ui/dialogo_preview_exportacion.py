class DialogoPreviewExportacion:
    """
    Componente encargado de mostrar una vista previa del contenido
    en su formato destino antes de confirmar la exportación.
    """

    def __init__(self, formato: str, contenido: str):
        self.formato = formato
        self.contenido = contenido
        self.confirmado = False

    def mostrar(self) -> bool:
        print(f"\n--- VISTA PREVIA DE EXPORTACIÓN [{self.formato.upper()}] ---")
        print(self.contenido)
        print("--------------------------------------------------")

        opcion = input("¿Confirmar exportación? (s/n): ").strip().lower()

        if opcion == "s":
            self.confirmar_exportacion()
        else:
            self.cancelar_exportacion()

        return self.confirmado

    def confirmar_exportacion(self):
        self.confirmado = True

    def cancelar_exportacion(self):
        self.confirmado = False
