def lambda_handler(event, context):
    # TODO implement
    html_code = """
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Bootstrap demo</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
      crossorigin="anonymous"
    />
  </head>
  <body>
    <div>
      <nav class="navbar navbar-expand-lg navbar-white bg-primary">
        <div class="container-fluid">
          <a class="navbar-brand text-white">Registro de actividades</a
          ><button
            class="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#nav"
            aria-controls="navbarSupportedContent"
          >
            <span class="navbar-toggler-icon"></span>
          </button>
        </div>
        <div class="collapse navbar-collapse" id="nav">
          <ul class="navbar-nav mx-auto mb-2">
            <li class="nav-item active px-lg-5">
              <a class="nav-link text-white active" href="crear"
                >Registrar</a
              >
            </li>
            <li class="nav-item active px-lg-5">
              <a class="nav-link text-white active" href="consultar"
                >Consultar</a
              >
            </li>
          </ul>
          <ul class="navbar-nav mx-auto mb-2">
            <li class="nav-item px-lg-5">
              <button class="btn btn-light">Logout</button>
            </li>
          </ul>
        </div>
      </nav>
    </div>
    <div>
      <div class="container mt-5">
        <div class="row">
          <div class="col">
            <form>
              <div class="mb-4">
                <label for="projectId" class="form-label">Proyecto</label
                ><select id="projectId" class="form-select" name="project">
                  <option value="TRACKER">TRACKER</option>
                  <option value="SISTEMA DE VENTAS">SISTEMA DE VENTAS</option>
                </select>
              </div>
              <div class="mb-4">
                <label for="description" class="form-label">Descripción</label
                ><input
                  type="text"
                  required=""
                  class="form-control"
                  name="description"
                  id="description"
                  value=""
                />
              </div>
              <div class="mb-4">
                <label for="hours" class="form-label">Horas</label
                ><input
                  type="text"
                  required=""
                  class="form-control"
                  name="hours"
                  id="hours"
                  value=""
                />
              </div>
              <div class="d-grid">
                <button type="button" class="btn btn-primary">Guardar</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
    """
    return {
        'statusCode': 200,
        'headers': {'content-type': 'text/html'},
        'body': html_code
    }
