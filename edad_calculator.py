<!DOCTYPE html>
<html>
<head>
  <title>Calculadora de Edad</title>
</head>
<body>
  <h1>Calculadora de Edad</h1>
  <form onsubmit="calcularEdad(event)">
    <input type="date" id="fecha" required>
    <button type="submit">Calcular</button>
  </form>
  <p id="resultado"></p>

  <script>
    function calcularEdad(e) {
      e.preventDefault();
      const fecha = new Date(document.getElementById("fecha").value);
      const hoy = new Date();
      let edad = hoy.getFullYear() - fecha.getFullYear();
      if (
        hoy.getMonth() < fecha.getMonth() || 
        (hoy.getMonth() === fecha.getMonth() && hoy.getDate() < fecha.getDate())
      ) {
        edad--;
      }
      document.getElementById("resultado").textContent = "Tu edad es: " + edad;
    }
  </script>
</body>
</html>
