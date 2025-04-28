class CarteraCripto:
    def __init__(self, usuario):  # ← aquí el cambio
        self.__usuario = usuario
        self.__saldo_btc = 0.0

    def consultar_saldo(self):
        return self.__saldo_btc

    def comprar_btc(self, monto_usd, precio_actual_btc):
        if precio_actual_btc > 0:
            btc_a_comprar = monto_usd / precio_actual_btc
            self.__saldo_btc += btc_a_comprar
            print(f"Se compraron {btc_a_comprar:.8f} BTC.")
        else:
            print("El precio actual de BTC debe ser mayor que cero.")

    def vender_btc(self, monto_btc, precio_actual_btc):
        if monto_btc <= self.__saldo_btc:
            usd_recibidos = monto_btc * precio_actual_btc
            self.__saldo_btc -= monto_btc
            print(f"Se vendieron {monto_btc:.8f} BTC y se recibieron {usd_recibidos:.2f} USD.")
        else:
            print("No tienes suficiente saldo de BTC para vender esa cantidad.")

# Uso del objeto
mi_cartera = CarteraCripto("Usuario123")

print(f"Saldo inicial: {mi_cartera.consultar_saldo():.8f} BTC")

mi_cartera.comprar_btc(100, 30000)
print(f"Saldo después de comprar: {mi_cartera.consultar_saldo():.8f} BTC")

mi_cartera.vender_btc(0.001, 31000)
print(f"Saldo después de vender: {mi_cartera.consultar_saldo():.8f} BTC")

mi_cartera.vender_btc(10, 31000)
